from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import validate_evals
import validate_skills


class ValidatorTests(unittest.TestCase):
    def behavior_path(self, root: Path) -> Path:
        path = root / "skills" / "sample-skill" / "evals" / "evals.json"
        path.parent.mkdir(parents=True)
        return path

    def behavior_case(self) -> dict:
        return {
            "skill_name": "sample-skill",
            "evals": [
                {
                    "id": "case-one",
                    "prompt": "Inspect the supplied case.",
                    "expected_output": "A bounded result.",
                    "files": [],
                    "expectations": ["Returns the expected result."],
                }
            ],
        }

    def test_unhashable_behavior_id_reports_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.behavior_path(Path(directory))
            data = self.behavior_case()
            data["evals"][0]["id"] = ["invalid"]
            errors = []
            validate_evals.validate_behavior(path, data, errors)
            self.assertTrue(any("id is required" in error for error in errors))

    def test_missing_files_reports_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.behavior_path(Path(directory))
            data = self.behavior_case()
            del data["evals"][0]["files"]
            errors = []
            validate_evals.validate_behavior(path, data, errors)
            self.assertTrue(any("files must be an array" in error for error in errors))

    def test_sequence_skill_requires_true_trigger(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cross-skill-routing.json"
            query = "Diagnose the issue and then implement the fix."
            data = {
                "routing_cases": [
                    {
                        "id": "sequence-case",
                        "query": query,
                        "expected_primary_skill": "diagnosis",
                        "allowed_companions": [],
                        "forbidden_skills": [],
                        "expected_no_skill": False,
                        "expected_sequence": ["diagnosis", "coding"],
                        "runs": 3,
                        "minimum_primary_trigger_rate": 0.67,
                        "maximum_forbidden_trigger_rate": 0.0,
                        "expectations": ["Runs diagnosis before coding."],
                    }
                ]
            }
            path.write_text(json.dumps(data), encoding="utf-8")
            triggers = {"diagnosis": {query: True}, "coding": {}}
            errors = []
            validate_evals.validate_routing(path, {"diagnosis", "coding"}, triggers, errors)
            self.assertTrue(any("coding trigger_eval" in error and "should_trigger=true" in error for error in errors))

    def test_bare_reference_pattern_detects_missing_path(self) -> None:
        matches = [match.group(1) for match in validate_skills.REFERENCE_PATTERN.finditer("Read references/missing-file.md, then continue.")]
        self.assertEqual(matches, ["references/missing-file.md"])

    def test_current_repository_validators_pass(self) -> None:
        for script in ("validate_skills.py", "validate_evals.py"):
            result = subprocess.run([sys.executable, str(SCRIPTS / script)], cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
