from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def load(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None


def validate_expectations(item: dict, label: str, errors: list[str]) -> None:
    values = item.get("expectations")
    require(isinstance(values, list) and bool(values), f"{label}: expectations must be a non-empty array", errors)
    if isinstance(values, list):
        require(all(isinstance(value, str) and value.strip() for value in values), f"{label}: expectations entries must be non-empty strings", errors)


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
        fixture_root = path.parent / "fixtures"
        files = item.get("files", [])
        require(isinstance(files, list) and bool(files), f"{label}: real fixtures require files", errors)
        if isinstance(files, list):
            for value in files:
                require(isinstance(value, str) and (fixture_root / value).is_file(), f"{label}: missing real fixture {value}", errors)
    if fixture_type == "isolated_repo":
        require(bool(fixture.get("contract")), f"{label}: isolated_repo fixture requires contract", errors)
        side_effects = item.get("expected_side_effects", [])
        require(isinstance(side_effects, list), f"{label}: expected_side_effects must be an array", errors)


def validate_behavior(path: Path, data: dict, errors: list[str]) -> None:
    skill = path.parents[1].name
    require(data.get("skill_name") == skill, f"{path.relative_to(ROOT)}: skill_name must match {skill}", errors)
    evals = data.get("evals")
    require(isinstance(evals, list), f"{path.relative_to(ROOT)}: evals must be an array", errors)
    if not isinstance(evals, list):
        return
    ids = set()
    for index, item in enumerate(evals):
        label = f"{path.relative_to(ROOT)}[{index}]"
        require(isinstance(item, dict), f"{label}: item must be an object", errors)
        if not isinstance(item, dict):
            continue
        item_id = item.get("id")
        require(isinstance(item_id, (str, int)) and str(item_id).strip(), f"{label}: id is required", errors)
        require(item_id not in ids, f"{label}: duplicate id {item_id}", errors)
        ids.add(item_id)
        require(isinstance(item.get("prompt"), str) and item["prompt"].strip(), f"{label}: prompt is required", errors)
        require(isinstance(item.get("expected_output"), str) and item["expected_output"].strip(), f"{label}: expected_output is required", errors)
        require(isinstance(item.get("files", []), list), f"{label}: files must be an array", errors)
        validate_expectations(item, label, errors)
        validate_fixture(item, path, label, errors)


def validate_trigger(path: Path, data: list, errors: list[str]) -> None:
    ids = set()
    for index, item in enumerate(data):
        label = f"{path.relative_to(ROOT)}[{index}]"
        require(isinstance(item, dict), f"{label}: item must be an object", errors)
        if not isinstance(item, dict):
            continue
        item_id = item.get("id")
        require(isinstance(item_id, (str, int)) and str(item_id).strip(), f"{label}: id is required", errors)
        require(item_id not in ids, f"{label}: duplicate id {item_id}", errors)
        ids.add(item_id)
        require(isinstance(item.get("query"), str) and item["query"].strip(), f"{label}: query is required", errors)
        require(isinstance(item.get("should_trigger"), bool), f"{label}: should_trigger must be boolean", errors)
        validate_expectations(item, label, errors)


def main() -> int:
    errors: list[str] = []
    paths = sorted(SKILLS.glob("*/evals/evals.json")) + sorted(SKILLS.glob("*/evals/trigger_eval.json"))
    for path in paths:
        data = load(path, errors)
        if data is None:
            continue
        if path.name == "evals.json":
            require(isinstance(data, dict), f"{path.relative_to(ROOT)}: root must be an object", errors)
            if isinstance(data, dict):
                validate_behavior(path, data, errors)
        else:
            require(isinstance(data, list), f"{path.relative_to(ROOT)}: root must be an array", errors)
            if isinstance(data, list):
                validate_trigger(path, data, errors)
    if errors:
        print("Evaluation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(paths)} evaluation files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())