import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_code_eval import EvalError, evaluate, load_manifest


class RunCodeEvalTests(unittest.TestCase):
    def create_fixture(self, root, public_code="value = 0", timeout=5):
        public = root / "public"
        grader = root / "grader"
        public.mkdir()
        grader.mkdir()
        (public / "app.py").write_text(public_code, encoding="utf-8")
        (public / "test_public.py").write_text(
            "from app import value\nassert value == 1\n",
            encoding="utf-8",
        )
        (grader / "test_hidden.py").write_text(
            "from app import value\nassert value == 1\n",
            encoding="utf-8",
        )
        manifest = {
            "id": "fixture",
            "prompt": "Fix the value.",
            "public_dir": "public",
            "grader_dir": "grader",
            "public_test": [sys.executable, "test_public.py"],
            "grader_test": [sys.executable, "test_hidden.py"],
            "timeout_seconds": timeout,
            "allowed_paths": ["app.py"],
            "protected_test_paths": ["test_public.py"],
            "dependency_files": [],
            "forbid_new_dependencies": True,
        }
        path = root / "fixture.json"
        path.write_text(json.dumps(manifest), encoding="utf-8")
        return path

    def test_rejects_missing_manifest_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.json"
            path.write_text("{}", encoding="utf-8")
            with self.assertRaises(EvalError):
                load_manifest(path)

    def test_rejects_path_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root)
            data = json.loads(path.read_text(encoding="utf-8"))
            data["public_dir"] = "../outside"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(EvalError):
                evaluate(path, None)

    def test_rejects_invalid_policy_types(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root)
            data = json.loads(path.read_text(encoding="utf-8"))
            data["allowed_paths"] = "app.py"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(EvalError):
                load_manifest(path)

    @unittest.skipIf(sys.platform == "win32", "symbolic link creation requires optional Windows privileges")
    def test_rejects_grader_symlink_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root, "value = 1")
            command = [
                sys.executable,
                "-c",
                "from pathlib import Path; Path('test_hidden.py').symlink_to(Path('outside.py'))",
            ]
            with self.assertRaises(EvalError):
                evaluate(path, None, command)

    def test_passes_fixed_candidate_and_injects_grader_after_agent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root)
            command = [
                sys.executable,
                "-c",
                "from pathlib import Path; assert not Path('test_hidden.py').exists(); Path('app.py').write_text('value = 1\\n', encoding='utf-8')",
            ]
            result = evaluate(path, None, command)
            self.assertTrue(result["passed"])
            self.assertEqual(result["candidate_changes"], ["app.py"])
            self.assertEqual(result["grader_files"], ["test_hidden.py"])

    def test_fails_protected_test_change(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root, "value = 1")
            command = [
                sys.executable,
                "-c",
                "from pathlib import Path; Path('test_public.py').write_text('pass\\n', encoding='utf-8')",
            ]
            result = evaluate(path, None, command)
            self.assertFalse(result["passed"])
            self.assertIn("protected tests changed", result["hard_failures"])

    def test_detects_dependency_file_change(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root, "value = 1")
            public = root / "public"
            (public / "requirements.txt").write_text("", encoding="utf-8")
            data = json.loads(path.read_text(encoding="utf-8"))
            data["allowed_paths"].append("requirements.txt")
            data["dependency_files"] = ["requirements.txt"]
            path.write_text(json.dumps(data), encoding="utf-8")
            command = [
                sys.executable,
                "-c",
                "from pathlib import Path; Path('requirements.txt').write_text('requests\\n', encoding='utf-8')",
            ]
            result = evaluate(path, None, command)
            self.assertFalse(result["passed"])
            self.assertIn("dependency files changed", result["hard_failures"])

    def test_fails_disallowed_path_change(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root, "value = 1")
            command = [
                sys.executable,
                "-c",
                "from pathlib import Path; Path('extra.txt').write_text('x', encoding='utf-8')",
            ]
            result = evaluate(path, None, command)
            self.assertFalse(result["passed"])
            self.assertIn("changed paths outside allowed scope", result["hard_failures"])

    def test_reports_agent_timeout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root, "value = 1", timeout=1)
            command = [sys.executable, "-c", "import time; time.sleep(5)"]
            result = evaluate(path, None, command)
            self.assertFalse(result["passed"])
            self.assertTrue(result["agent"]["timed_out"])

    def test_cli_returns_nonzero_for_failed_eval(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.create_fixture(root)
            script = Path(__file__).with_name("run_code_eval.py")
            completed = subprocess.run(
                [sys.executable, str(script), str(path)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 1)


if __name__ == "__main__":
    unittest.main()
