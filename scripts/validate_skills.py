from __future__ import annotations

import ast
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


def main() -> int:
    errors = []
    warnings = []
    manifest_path = ROOT / "skills-manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Skill validation failed:\n- skills-manifest.json: {exc}")
        return 1
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
