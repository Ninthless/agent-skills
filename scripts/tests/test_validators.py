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

    def test_high_constraint_web_routing_contract(self) -> None:
        trigger_path = ROOT / "skills" / "high-constraint-coding" / "evals" / "trigger_eval.json"
        cases = {item["id"]: item["should_trigger"] for item in json.loads(trigger_path.read_text(encoding="utf-8-sig"))}
        expected = {
            "routing-web-responsive-implementation": True,
            "routing-web-react-interaction": True,
            "routing-web-css-browser-verify": True,
            "routing-web-requirements-only": False,
            "routing-web-framework-research": False,
            "routing-web-api-docs-only": False,
            "routing-web-unknown-bug-diagnose": False,
            "routing-ui-copy-translation": False,
        }
        for case_id, decision in expected.items():
            self.assertIn(case_id, cases)
            self.assertIs(cases[case_id], decision)

    def test_high_constraint_requires_browser_verification_loop(self) -> None:
        skill_root = ROOT / "skills" / "high-constraint-coding"
        contract_path = skill_root / "evals" / "web-verification-contract.json"
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        errors = []
        validate_skills.validate_web_contract(contract_path, errors)
        self.assertEqual(errors, [])
        self.assertEqual(
            {item["id"] for item in contract["required_steps"]},
            set(validate_skills.WEB_REQUIRED_STEP_IDS),
        )
        self.assertEqual(
            {item["id"] for item in contract["fallback_when_unavailable"]},
            set(validate_skills.WEB_FALLBACK_IDS),
        )
        self.assertEqual(
            {item["id"] for item in contract["forbidden_claims"]},
            set(validate_skills.WEB_FORBIDDEN_IDS),
        )
        skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Web verification branch", skill)
        self.assertIn("continue fixing and repeat", skill)
        for platform in ("openai", "claude"):
            prompt = (skill_root / "agents" / f"{platform}.yaml").read_text(encoding="utf-8")
            self.assertIn("browser tools when available", prompt)
            self.assertIn("fix and rerun", prompt)

    def test_web_contract_rejects_missing_step_and_duplicate_id(self) -> None:
        source = ROOT / "skills" / "high-constraint-coding" / "evals" / "web-verification-contract.json"
        contract = json.loads(source.read_text(encoding="utf-8"))
        contract["required_steps"] = [
            item for item in contract["required_steps"] if item["id"] != "fix-retest"
        ]
        contract["required_steps"].append(dict(contract["required_steps"][0]))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "web-verification-contract.json"
            path.write_text(json.dumps(contract), encoding="utf-8")
            errors = []
            validate_skills.validate_web_contract(path, errors)
        self.assertTrue(any("fix-retest" in error for error in errors))
        self.assertTrue(any("duplicate ids" in error for error in errors))

    def test_closed_world_routing_rejects_undeclared_true_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cross-skill-routing.json"
            query = "Implement the bounded source change."
            data = {
                "routing_cases": [
                    {
                        "id": "primary-only",
                        "query": query,
                        "expected_primary_skill": "coding",
                        "allowed_companions": [],
                        "forbidden_skills": [],
                        "expected_no_skill": False,
                        "expected_sequence": ["coding"],
                        "runs": 3,
                        "minimum_primary_trigger_rate": 0.67,
                        "maximum_forbidden_trigger_rate": 0.0,
                        "expectations": ["Routes only to coding."],
                    }
                ]
            }
            path.write_text(json.dumps(data), encoding="utf-8")
            triggers = {"coding": {query: True}, "research": {query: True}}
            errors = []
            validate_evals.validate_routing(path, {"coding", "research"}, triggers, errors)
        self.assertTrue(any("research trigger_eval" in error and "should_trigger=false" in error for error in errors))

    def test_closed_world_routing_accepts_declared_companion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cross-skill-routing.json"
            query = "Implement the source change without comments."
            data = {
                "routing_cases": [
                    {
                        "id": "companion-case",
                        "query": query,
                        "expected_primary_skill": "coding",
                        "allowed_companions": ["comments"],
                        "forbidden_skills": [],
                        "expected_no_skill": False,
                        "expected_sequence": ["coding"],
                        "runs": 3,
                        "minimum_primary_trigger_rate": 0.67,
                        "maximum_forbidden_trigger_rate": 0.0,
                        "expectations": ["Allows the declared companion."],
                    }
                ]
            }
            path.write_text(json.dumps(data), encoding="utf-8")
            triggers = {"coding": {query: True}, "comments": {query: True}, "research": {query: False}}
            errors = []
            validate_evals.validate_routing(path, {"coding", "comments", "research"}, triggers, errors)
        self.assertEqual(errors, [])
    def test_engineering_quality_contract_passes(self) -> None:
        path = ROOT / "skills" / "high-constraint-coding" / "evals" / "engineering-quality-contract.json"
        errors = []
        validate_skills.validate_structured_contract(path, validate_skills.ENGINEERING_CONTRACT_IDS, errors)
        self.assertEqual(errors, [])

    def test_engineering_quality_contract_rejects_missing_and_duplicate_ids(self) -> None:
        source = ROOT / "skills" / "high-constraint-coding" / "evals" / "engineering-quality-contract.json"
        contract = json.loads(source.read_text(encoding="utf-8"))
        contract["orientation"] = [item for item in contract["orientation"] if item["id"] != "toolchain"]
        contract["verification"].append(dict(contract["verification"][0]))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "engineering-quality-contract.json"
            path.write_text(json.dumps(contract), encoding="utf-8")
            errors = []
            validate_skills.validate_structured_contract(path, validate_skills.ENGINEERING_CONTRACT_IDS, errors)
        self.assertTrue(any("toolchain" in error for error in errors))
        self.assertTrue(any("duplicate ids" in error for error in errors))

    def test_engineering_quality_contract_rejects_unexpected_id(self) -> None:
        source = ROOT / "skills" / "high-constraint-coding" / "evals" / "engineering-quality-contract.json"
        contract = json.loads(source.read_text(encoding="utf-8"))
        contract["orientation"].append({"id": "invented-step", "obligation": "require", "text": "Must be rejected."})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "engineering-quality-contract.json"
            path.write_text(json.dumps(contract), encoding="utf-8")
            errors = []
            validate_skills.validate_structured_contract(path, validate_skills.ENGINEERING_CONTRACT_IDS, errors)
        self.assertTrue(any("unexpected ids" in error and "invented-step" in error for error in errors))

    def test_engineering_quality_contract_rejects_reversed_obligation(self) -> None:
        source = ROOT / "skills" / "high-constraint-coding" / "evals" / "engineering-quality-contract.json"
        contract = json.loads(source.read_text(encoding="utf-8"))
        contract["orientation"][0]["obligation"] = "forbid"
        contract["forbidden_patterns"][0]["obligation"] = "require"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "engineering-quality-contract.json"
            path.write_text(json.dumps(contract), encoding="utf-8")
            errors = []
            validate_skills.validate_structured_contract(path, validate_skills.ENGINEERING_CONTRACT_IDS, errors)
        self.assertTrue(any("obligation must be require" in error for error in errors))
        self.assertTrue(any("obligation must be forbid" in error for error in errors))

    def test_web_contract_rejects_reversed_obligation(self) -> None:
        source = ROOT / "skills" / "high-constraint-coding" / "evals" / "web-verification-contract.json"
        contract = json.loads(source.read_text(encoding="utf-8"))
        contract["forbidden_claims"][0]["obligation"] = "require"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "web-verification-contract.json"
            path.write_text(json.dumps(contract), encoding="utf-8")
            errors = []
            validate_skills.validate_web_contract(path, errors)
        self.assertTrue(any("obligation must be forbid" in error for error in errors))

    def test_high_constraint_prompts_require_cross_language_quality(self) -> None:
        skill = (ROOT / "skills" / "high-constraint-coding" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("every programming language", skill)
        self.assertIn("language- and ecosystem-native", skill)
        self.assertIn("deliberate senior project work", skill)
        self.assertIn("fixing and repeat", skill)
        for platform in ("openai", "claude"):
            prompt = (ROOT / "skills" / "high-constraint-coding" / "agents" / f"{platform}.yaml").read_text(encoding="utf-8")
            self.assertIn("all programming languages", prompt)
            self.assertIn("language- and ecosystem-native", prompt)
            self.assertIn("deliberate senior project work", prompt)
            self.assertIn("fix and rerun", prompt)
    def test_current_repository_validators_pass(self) -> None:
        for script in ("validate_skills.py", "validate_evals.py"):
            result = subprocess.run([sys.executable, str(SCRIPTS / script)], cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
