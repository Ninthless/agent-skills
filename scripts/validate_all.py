from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    failed = False
    commands = (
        [sys.executable, "scripts/validate_skills.py"],
        [sys.executable, "scripts/validate_evals.py"],
        [sys.executable, "scripts/audit_skill_sizes.py", "--check"],
        [sys.executable, "-m", "unittest", "discover", "-s", "scripts/tests"],
    )
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, check=False)
        failed = failed or result.returncode != 0
    json_errors = []
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            json_errors.append(f"{path.relative_to(ROOT)}: {exc}")
    if json_errors:
        print("JSON validation failed:")
        for error in json_errors:
            print(f"- {error}")
        failed = True
    else:
        print("Validated all repository JSON files.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
