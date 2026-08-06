from __future__ import annotations

import ast
from collections import Counter
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_PATTERN = re.compile(r"(?<![A-Za-z0-9_./-])((?:\./)?references/[A-Za-z0-9._-]+)(?![A-Za-z0-9_./-])")


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter")
        return {}
    values = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{path.relative_to(ROOT)}: unsupported frontmatter line")
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        if raw[:1] in {"'", '"'}:
            try:
                value = ast.literal_eval(raw)
            except (SyntaxError, ValueError):
                errors.append(f"{path.relative_to(ROOT)}: invalid quoted {key.strip()}")
                continue
        else:
            value = raw
        values[key.strip()] = value
    return values


def parse_agent(path: Path, errors: list[str]) -> tuple[dict[str, str], dict[str, object]]:
    interface = {}
    policy = {}
    section = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip():
            continue
        if not raw_line.startswith(" ") and raw_line.endswith(":"):
            section = raw_line[:-1]
            continue
        match = re.match(r"^  ([a-z_]+):\s*(.+)$", raw_line)
        if not match or section not in {"interface", "policy"}:
            errors.append(f"{path.relative_to(ROOT)}: unsupported YAML structure")
            continue
        key, raw = match.groups()
        if raw in {"true", "false"}:
            value = raw == "true"
        elif raw[:1] in {"'", '"'}:
            try:
                value = ast.literal_eval(raw)
            except (SyntaxError, ValueError):
                errors.append(f"{path.relative_to(ROOT)}: invalid quoted value")
                continue
        else:
            value = raw
        target = interface if section == "interface" else policy
        target[key] = value
    return interface, policy


WEB_CONTRACT_FIELDS = {"applies_to", "required_steps", "fallback_when_unavailable", "forbidden_claims"}
WEB_REQUIRED_STEP_IDS = {item_id: "require" for item_id in {"server-reuse", "browser-page", "affected-flow", "responsive-viewports", "console", "conditional-network", "evidence", "fix-retest"}}
WEB_FALLBACK_IDS = {item_id: "require" for item_id in {"static-checks", "report-blocker"}}
WEB_FORBIDDEN_IDS = {item_id: "forbid" for item_id in {"duplicate-server", "unverified-pass", "report-only-failure"}}
ENGINEERING_CONTRACT_IDS = {
    "orientation": {item_id: "require" for item_id in {"language-version", "toolchain", "local-conventions", "behavior-model", "invariants-lifecycle"}},
    "design_judgment": {item_id: "require" for item_id in {"correct-seam", "real-options-only", "evidence-based-choice", "compatibility"}},
    "implementation_quality": {item_id: "require" for item_id in {"idiomatic-types-errors", "resource-ownership", "concurrency-cancellation", "explicit-boundaries", "observable-errors"}},
    "maintainability_audit": {item_id: "require" for item_id in {"cognitive-load", "artifact-justification", "no-template-symmetry", "reasonable-asymmetry", "debuggability"}},
    "verification": {item_id: "require" for item_id in {"behavior-tests", "failure-recovery", "adjacent-risk", "fix-retest", "honest-evidence"}},
    "forbidden_patterns": {item_id: "forbid" for item_id in {"speculative-abstraction", "pass-through-layer", "swallowed-error", "suppression-instead-of-modeling", "test-only-production-hook", "unsupported-performance-claim", "authorship-claim"}},
}


def validate_structured_contract(path: Path, expected_fields_and_ids: dict[str, dict[str, str] | None], errors: list[str]) -> None:
    label = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{label}: invalid structured contract: {exc}")
        return
    if not isinstance(data, dict):
        errors.append(f"{label}: contract root must be an object")
        return
    if set(data) != set(expected_fields_and_ids):
        errors.append(f"{label}: fields must be {sorted(expected_fields_and_ids)}")
    for field, required_ids in expected_fields_and_ids.items():
        values = data.get(field)
        if not isinstance(values, list) or not values:
            errors.append(f"{label}: {field} must be a non-empty array")
            continue
        if required_ids is None:
            if not all(isinstance(item, str) and item.strip() for item in values):
                errors.append(f"{label}: {field} entries must be non-empty strings")
            continue
        ids = []
        for index, item in enumerate(values):
            item_label = f"{label}: {field}[{index}]"
            if not isinstance(item, dict) or set(item) != {"id", "obligation", "text"}:
                errors.append(f"{item_label} must contain only id, obligation, and text")
                continue
            item_id = item.get("id")
            item_text = item.get("text")
            obligation = item.get("obligation")
            if not isinstance(item_id, str) or not item_id.strip():
                errors.append(f"{item_label}: id must be a non-empty string")
            else:
                ids.append(item_id)
            if not isinstance(item_text, str) or not item_text.strip():
                errors.append(f"{item_label}: text must be a non-empty string")
            if obligation not in {"require", "forbid"}:
                errors.append(f"{item_label}: obligation must be require or forbid")
            elif isinstance(item_id, str) and item_id in required_ids and obligation != required_ids[item_id]:
                errors.append(f"{item_label}: obligation must be {required_ids[item_id]} for {item_id}")
        id_counts = Counter(ids)
        duplicate_ids = sorted(item_id for item_id, count in id_counts.items() if count > 1)
        if duplicate_ids:
            errors.append(f"{label}: {field} contains duplicate ids: {duplicate_ids}")
        actual_ids = set(ids)
        expected_ids = set(required_ids)
        missing_ids = sorted(expected_ids - actual_ids)
        if missing_ids:
            errors.append(f"{label}: {field} missing required ids: {missing_ids}")
        unexpected_ids = sorted(actual_ids - expected_ids)
        if unexpected_ids:
            errors.append(f"{label}: {field} contains unexpected ids: {unexpected_ids}")


def validate_web_contract(path: Path, errors: list[str]) -> None:
    validate_structured_contract(
        path,
        {
            "applies_to": None,
            "required_steps": WEB_REQUIRED_STEP_IDS,
            "fallback_when_unavailable": WEB_FALLBACK_IDS,
            "forbidden_claims": WEB_FORBIDDEN_IDS,
        },
        errors,
    )

def main() -> int:
    errors = []
    warnings = []
    manifest_path = ROOT / "skills-manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Skill validation failed:\n- skills-manifest.json: {exc}")
        return 1
    validate_web_contract(SKILLS / "high-constraint-coding" / "evals" / "web-verification-contract.json", errors)
    validate_structured_contract(
        SKILLS / "high-constraint-coding" / "evals" / "engineering-quality-contract.json",
        ENGINEERING_CONTRACT_IDS,
        errors,
    )
    entries = manifest.get("skills")
    if manifest.get("extension") != "repository-local" or manifest.get("repository_local_extension") is not True:
        errors.append("skills-manifest.json: repository-local extension marker is required")
    if not isinstance(entries, list):
        errors.append("skills-manifest.json: skills must be an array")
        entries = []
    actual = {path.parent.name for path in SKILLS.glob("*/SKILL.md")}
    declared = set()
    manifest_entries = {}
    for index, entry in enumerate(entries):
        label = f"skills-manifest.json skills[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label}: must be an object")
            continue
        required = {"name", "mode", "role", "implicit", "side_effects", "handoff"}
        if set(entry) != required:
            errors.append(f"{label}: fields must be {sorted(required)}")
        name = entry.get("name")
        if isinstance(name, str):
            if name in declared:
                errors.append(f"{label}: duplicate name {name}")
            declared.add(name)
            manifest_entries[name] = entry
        if entry.get("mode") not in {"analysis", "execution", "action", "companion"}:
            errors.append(f"{label}: invalid mode")
        role = entry.get("role")
        mode = entry.get("mode")
        if role not in {"primary", "companion"}:
            errors.append(f"{label}: invalid role")
        if role == "companion":
            if mode != "companion":
                errors.append(f"{label}: companion role requires companion mode")
            if entry.get("side_effects") is not False:
                errors.append(f"{label}: companion role requires side_effects=false")
        if role == "primary" and mode == "companion":
            errors.append(f"{label}: primary role cannot use companion mode")
        if not isinstance(entry.get("implicit"), bool) or not isinstance(entry.get("side_effects"), bool):
            errors.append(f"{label}: implicit and side_effects must be booleans")
        handoff = entry.get("handoff")
        if not isinstance(handoff, list) or not all(isinstance(value, str) for value in handoff):
            errors.append(f"{label}: handoff must be a string array")
        else:
            if len(handoff) != len(set(handoff)):
                errors.append(f"{label}: handoff cannot contain duplicates")
            if name in handoff:
                errors.append(f"{label}: handoff cannot contain self")
    if actual != declared:
        errors.append(f"manifest mismatch: actual={sorted(actual)} declared={sorted(declared)}")
    for entry in entries:
        for target in entry.get("handoff", []) if isinstance(entry, dict) else []:
            if target not in declared:
                errors.append(f"skills-manifest.json: unknown handoff {target}")
    for skill in sorted(actual):
        path = SKILLS / skill / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        metadata = parse_frontmatter(path, errors)
        name = metadata.get("name")
        description = metadata.get("description")
        if name != skill:
            errors.append(f"{path.relative_to(ROOT)}: name must match directory")
        if not isinstance(name, str) or len(name) > 64 or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{path.relative_to(ROOT)}: name must be lowercase kebab-case with at most 64 characters")
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            errors.append(f"{path.relative_to(ROOT)}: description must contain 1-1024 characters")
        lines = len(text.splitlines())
        if lines >= 500:
            warnings.append(f"{path.relative_to(ROOT)}: {lines} lines exceeds local 499-line recommendation")
        for platform in ("openai", "claude"):
            agent_path = path.parent / "agents" / f"{platform}.yaml"
            if not agent_path.is_file():
                errors.append(f"{agent_path.relative_to(ROOT)}: missing")
                continue
            interface, policy = parse_agent(agent_path, errors)
            for key in ("display_name", "short_description", "default_prompt"):
                if not isinstance(interface.get(key), str) or not interface[key].strip():
                    errors.append(f"{agent_path.relative_to(ROOT)}: interface.{key} is required")
            allow_implicit = policy.get("allow_implicit_invocation")
            if not isinstance(allow_implicit, bool):
                errors.append(f"{agent_path.relative_to(ROOT)}: policy.allow_implicit_invocation must be boolean")
            else:
                manifest_entry = manifest_entries.get(skill)
                if isinstance(manifest_entry, dict) and isinstance(manifest_entry.get("implicit"), bool) and allow_implicit != manifest_entry["implicit"]:
                    errors.append(f"{agent_path.relative_to(ROOT)}: policy.allow_implicit_invocation must match manifest implicit")
            prompt = interface.get("default_prompt", "")
            if isinstance(prompt, str) and skill not in prompt:
                errors.append(f"{agent_path.relative_to(ROOT)}: default_prompt must reference {skill}")
        if chr(92) + "references" in text or "references" + chr(92) in text:
            errors.append(f"{path.relative_to(ROOT)}: reference paths must use forward slashes")
        for match in REFERENCE_PATTERN.finditer(text):
            reference = match.group(1).lstrip("./")
            if not (path.parent / reference).is_file():
                errors.append(f"{path.relative_to(ROOT)}: missing referenced file {reference}")
    for warning in warnings:
        print(f"Warning: {warning}")
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(actual)} skills and {len(entries) * 2} agent files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
