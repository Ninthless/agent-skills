from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_LIMIT = 64
DESCRIPTION_LIMIT = 1024
SKILL_LINE_RECOMMENDATION = 499
PROMPT_RECOMMENDATION = 1200
CODEX_INITIAL_CATALOG_BUDGET = 8000


def frontmatter(path: Path) -> tuple[str, str]:
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if line == "---":
            break
        if ":" in line:
            key, raw = line.split(":", 1)
            raw = raw.strip()
            values[key] = ast.literal_eval(raw) if raw[:1] in {"'", '"'} else raw
    return values.get("name", ""), values.get("description", "")


def prompt_chars(path: Path) -> int:
    for line in path.read_text(encoding="utf-8").splitlines():
        prefix = "  default_prompt: "
        if line.startswith(prefix):
            raw = line[len(prefix):].strip()
            if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {chr(34), chr(39)}:
                return len(raw[1:-1])
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    failures = []
    warnings = []
    catalog_total = 0
    rows = []
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        name, description = frontmatter(path)
        text = path.read_text(encoding="utf-8")
        references = sorted((path.parent / "references").glob("*")) if (path.parent / "references").is_dir() else []
        reference_files = [item for item in references if item.is_file()]
        reference_chars = sum(len(item.read_text(encoding="utf-8")) for item in reference_files)
        prompts = sum(prompt_chars(path.parent / "agents" / f"{platform}.yaml") for platform in ("openai", "claude"))
        lines = len(text.splitlines())
        catalog = len(name) + len(description) + len(f"skills/{name}/SKILL.md")
        catalog_total += catalog
        rows.append((name, len(name), len(description), len(text), lines, prompts, len(reference_files), reference_chars, catalog))
        if len(name) > NAME_LIMIT:
            failures.append(f"{name}: name exceeds open specification limit {NAME_LIMIT}")
        if not description or len(description) > DESCRIPTION_LIMIT:
            failures.append(f"{name}: description must contain 1-{DESCRIPTION_LIMIT} characters")
        if lines > SKILL_LINE_RECOMMENDATION:
            warnings.append(f"{name}: SKILL.md has {lines} lines; local recommendation is at most {SKILL_LINE_RECOMMENDATION}")
        if prompts > PROMPT_RECOMMENDATION * 2:
            warnings.append(f"{name}: combined agent prompts have {prompts} characters; local recommendation is {PROMPT_RECOMMENDATION} per platform")
    print("name	name_chars	description_chars	skill_chars	skill_lines	agent_prompt_chars	references	reference_chars	catalog_chars")
    for row in rows:
        print("	".join(str(value) for value in row))
    print(f"catalog_total	{catalog_total}")
    if catalog_total > CODEX_INITIAL_CATALOG_BUDGET:
        warnings.append(f"catalog total {catalog_total} exceeds the reported Codex initial catalog platform budget {CODEX_INITIAL_CATALOG_BUDGET}; this is a platform budget, not an open specification limit")
    for warning in warnings:
        print(f"Warning: {warning}")
    if args.check and failures:
        for failure in failures:
            print(f"Error: {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
