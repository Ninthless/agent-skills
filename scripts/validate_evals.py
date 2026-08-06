from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
STRING_ARRAY_FIELDS = ("required_information", "forbidden_behaviors", "expected_side_effects", "verification", "platform_requirements")


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def display_path(path: Path) -> Path:
    try:
        return path.relative_to(ROOT)
    except ValueError:
        return path


def load(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{display_path(path)}: invalid JSON: {exc}")
        return None


def valid_case_id(value) -> bool:
    return isinstance(value, (str, int)) and not isinstance(value, bool) and bool(str(value).strip())


def record_id(value, ids: set, label: str, errors: list[str], string_only: bool = False) -> None:
    valid = isinstance(value, str) and bool(value.strip()) if string_only else valid_case_id(value)
    require(valid, f"{label}: id is required", errors)
    if not valid:
        return
    require(value not in ids, f"{label}: duplicate id {value}", errors)
    ids.add(value)


def validate_string_array(value, label: str, errors: list[str], allow_empty: bool = False) -> None:
    valid_list = isinstance(value, list) and (allow_empty or bool(value))
    suffix = "an array" if allow_empty else "a non-empty array"
    require(valid_list, f"{label} must be {suffix}", errors)
    if isinstance(value, list):
        require(all(isinstance(item, str) and item.strip() for item in value), f"{label} entries must be non-empty strings", errors)


def validate_fixture(item: dict, path: Path, label: str, errors: list[str]) -> None:
    fixture = item.get("fixture")
    if fixture is None:
        return
    require(isinstance(fixture, dict), f"{label}: fixture must be an object", errors)
    if not isinstance(fixture, dict):
        return
    fixture_type = fixture.get("type")
    require(fixture_type in {"real", "virtual", "isolated_repo"}, f"{label}: unsupported fixture type", errors)
    if fixture_type == "real":
        files = item.get("files")
        require(isinstance(files, list) and bool(files), f"{label}: real fixtures require files", errors)
        if isinstance(files, list):
            for value in files:
                if isinstance(value, str) and value.strip():
                    require((path.parent / "fixtures" / value).is_file(), f"{label}: missing real fixture {value}", errors)
    if fixture_type == "isolated_repo":
        contract = fixture.get("contract")
        require(isinstance(contract, str) and contract.strip(), f"{label}: isolated_repo fixture requires contract", errors)


def validate_behavior(path: Path, data: dict, errors: list[str]) -> None:
    skill = path.parents[1].name
    require(data.get("skill_name") == skill, f"{display_path(path)}: skill_name must match {skill}", errors)
    cases = data.get("evals")
    require(isinstance(cases, list), f"{display_path(path)}: evals must be an array", errors)
    if not isinstance(cases, list):
        return
    ids = set()
    for index, item in enumerate(cases):
        label = f"{display_path(path)}[{index}]"
        require(isinstance(item, dict), f"{label}: item must be an object", errors)
        if not isinstance(item, dict):
            continue
        record_id(item.get("id"), ids, label, errors)
        for field in ("prompt", "expected_output"):
            value = item.get(field)
            require(isinstance(value, str) and value.strip(), f"{label}: {field} is required", errors)
        files = item.get("files")
        validate_string_array(files, f"{label}: files", errors, allow_empty=True)
        validate_string_array(item.get("expectations"), f"{label}: expectations", errors)
        for field in STRING_ARRAY_FIELDS:
            if field in item:
                validate_string_array(item[field], f"{label}: {field}", errors)
        validate_fixture(item, path, label, errors)


def validate_trigger(path: Path, data: list, errors: list[str]) -> dict[str, bool]:
    ids = set()
    queries = {}
    decisions = set()
    for index, item in enumerate(data):
        label = f"{display_path(path)}[{index}]"
        require(isinstance(item, dict), f"{label}: item must be an object", errors)
        if not isinstance(item, dict):
            continue
        record_id(item.get("id"), ids, label, errors)
        query = item.get("query")
        decision = item.get("should_trigger")
        valid_query = isinstance(query, str) and bool(query.strip())
        require(valid_query, f"{label}: query is required", errors)
        require(isinstance(decision, bool), f"{label}: should_trigger must be boolean", errors)
        validate_string_array(item.get("expectations"), f"{label}: expectations", errors)
        if valid_query and isinstance(decision, bool):
            require(query not in queries, f"{label}: duplicate query", errors)
            queries[query] = decision
            decisions.add(decision)
    require(decisions == {True, False}, f"{display_path(path)}: each final skill requires at least one true and one false trigger", errors)
    return queries


def valid_skill_array(value, skill_names: set[str]) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and item.strip() and item in skill_names for item in value)


def validate_routing(path: Path, skill_names: set[str], triggers: dict[str, dict[str, bool]], errors: list[str]) -> None:
    data = load(path, errors)
    if not isinstance(data, dict):
        errors.append(f"{display_path(path)}: root must be an object")
        return
    cases = data.get("routing_cases")
    require(isinstance(cases, list) and bool(cases), f"{display_path(path)}: routing_cases must be a non-empty array", errors)
    if not isinstance(cases, list):
        return
    ids = set()
    for index, item in enumerate(cases):
        label = f"{display_path(path)}[{index}]"
        require(isinstance(item, dict), f"{label}: item must be an object", errors)
        if not isinstance(item, dict):
            continue
        case_id = item.get("id")
        query = item.get("query")
        primary = item.get("expected_primary_skill")
        companions = item.get("allowed_companions")
        forbidden = item.get("forbidden_skills")
        no_skill = item.get("expected_no_skill")
        sequence = item.get("expected_sequence")
        record_id(case_id, ids, label, errors, string_only=True)
        valid_query = isinstance(query, str) and bool(query.strip())
        require(valid_query, f"{label}: query is required", errors)
        require(primary is None or isinstance(primary, str) and primary.strip() and primary in skill_names, f"{label}: unknown primary skill", errors)
        arrays_valid = True
        for field, values in (("allowed_companions", companions), ("forbidden_skills", forbidden), ("expected_sequence", sequence)):
            valid = valid_skill_array(values, skill_names)
            require(valid, f"{label}: {field} contains an unknown or invalid skill", errors)
            arrays_valid = arrays_valid and valid
        require(isinstance(no_skill, bool), f"{label}: expected_no_skill must be boolean", errors)
        runs = item.get("runs")
        require(isinstance(runs, int) and not isinstance(runs, bool) and runs >= 1, f"{label}: runs must be at least 1", errors)
        for field in ("minimum_primary_trigger_rate", "maximum_forbidden_trigger_rate"):
            rate = item.get(field)
            require(isinstance(rate, (int, float)) and not isinstance(rate, bool) and 0 <= rate <= 1, f"{label}: {field} must be between 0 and 1", errors)
        validate_string_array(item.get("expectations"), f"{label}: expectations", errors)
        if not arrays_valid or not valid_query:
            continue
        companion_set = set(companions)
        forbidden_set = set(forbidden)
        sequence_set = set(sequence)
        require(len(companions) == len(companion_set), f"{label}: allowed_companions cannot contain duplicates", errors)
        require(len(forbidden) == len(forbidden_set), f"{label}: forbidden_skills cannot contain duplicates", errors)
        require(len(sequence) == len(sequence_set), f"{label}: expected_sequence cannot contain duplicates", errors)
        require(primary not in companion_set, f"{label}: primary skill cannot be an allowed companion", errors)
        require(primary not in forbidden_set, f"{label}: primary skill cannot be forbidden", errors)
        require(not companion_set & forbidden_set, f"{label}: allowed companions and forbidden skills cannot overlap", errors)
        if no_skill is True:
            require(primary is None and companions == [] and sequence == [], f"{label}: no-skill cases cannot declare primary, companions, or sequence", errors)
            true_skills = set()
            false_skills = set(skill_names)
        else:
            require(primary is not None, f"{label}: routed cases require a primary skill", errors)
            require(bool(sequence) and sequence[0] == primary, f"{label}: expected_sequence must start with the primary skill", errors)
            true_skills = companion_set | sequence_set
            if isinstance(primary, str) and primary in skill_names:
                true_skills.add(primary)
            conflicts = true_skills & forbidden_set
            require(not conflicts, f"{label}: skills cannot be both required true and forbidden: {sorted(conflicts)}", errors)
            false_skills = forbidden_set
        for skill in true_skills:
            actual = triggers.get(skill, {}).get(query)
            require(actual is True, f"{label}: {skill} trigger_eval must contain query with should_trigger=true", errors)
        if no_skill is False:
            false_skills = skill_names - true_skills
        for skill in false_skills:
            actual = triggers.get(skill, {}).get(query)
            require(actual is False, f"{label}: {skill} trigger_eval must contain query with should_trigger=false", errors)


def main() -> int:
    errors = []
    skill_names = {path.parent.name for path in SKILLS.glob("*/SKILL.md")}
    triggers = {}
    paths = []
    for skill in sorted(skill_names):
        behavior_path = SKILLS / skill / "evals" / "evals.json"
        trigger_path = SKILLS / skill / "evals" / "trigger_eval.json"
        for path in (behavior_path, trigger_path):
            paths.append(path)
            if not path.is_file():
                errors.append(f"{display_path(path)}: missing")
        behavior = load(behavior_path, errors) if behavior_path.is_file() else None
        trigger = load(trigger_path, errors) if trigger_path.is_file() else None
        if isinstance(behavior, dict):
            validate_behavior(behavior_path, behavior, errors)
        elif behavior is not None:
            errors.append(f"{display_path(behavior_path)}: root must be an object")
        if isinstance(trigger, list):
            triggers[skill] = validate_trigger(trigger_path, trigger, errors)
        elif trigger is not None:
            errors.append(f"{display_path(trigger_path)}: root must be an array")
    validate_routing(ROOT / "evals" / "cross-skill-routing.json", skill_names, triggers, errors)
    if errors:
        print("Evaluation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(paths)} skill evaluation files and the cross-skill routing contract.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
