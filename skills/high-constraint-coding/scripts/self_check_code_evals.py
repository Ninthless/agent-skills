import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "evals" / "fixtures"


def run(argv, cwd):
    return subprocess.run(
        argv,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def copy_grader(fixture, workspace, manifest):
    grader = fixture / manifest["grader_dir"]
    target = manifest.get("grader_target")
    files = [path for path in grader.rglob("*") if path.is_file()]
    if target:
        if len(files) != 1:
            raise RuntimeError(f"{fixture.name}: grader_target requires one file")
        destination = workspace / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(files[0], destination)
        return
    for source in files:
        destination = workspace / source.relative_to(grader)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def fixed_text(case_id, path):
    text = path.read_text(encoding="utf-8")
    if case_id == "node-versioned-deferred":
        return (
            "export function createDeferred() {\n"
            "  let resolve;\n"
            "  let reject;\n"
            "  const promise = new Promise((fulfill, fail) => {\n"
            "    resolve = fulfill;\n"
            "    reject = fail;\n"
            "  });\n"
            "  return { promise, resolve, reject };\n"
            "}\n"
        )
    if case_id == "go-metadata-roundtrip":
        return text.replace('json:"-"', 'json:"metadata,omitempty"')
    if case_id == "python-sqlite-retry":
        return (
            "import sqlite3\n\n\n"
            "class RetryableTransactionError(Exception):\n"
            "    def __init__(self, code, message):\n"
            "        super().__init__(message)\n"
            "        self.code = code\n\n\n"
            "def transfer(database, source_account, destination_account, amount, publish, max_attempts=3, fault_hook=None, connection_factory=sqlite3.connect):\n"
            "    for attempt in range(1, max_attempts + 1):\n"
            "        connection = connection_factory(database)\n"
            "        try:\n"
            "            connection.execute(\"UPDATE accounts SET balance = balance - ? WHERE id = ?\", (amount, source_account))\n"
            "            connection.execute(\"UPDATE accounts SET balance = balance + ? WHERE id = ?\", (amount, destination_account))\n"
            "            if fault_hook is not None:\n"
            "                fault_hook(attempt, connection)\n"
            "            connection.commit()\n"
            "            publish({\"source_account\": source_account, \"destination_account\": destination_account, \"amount\": amount})\n"
            "            return\n"
            "        except RetryableTransactionError:\n"
            "            connection.rollback()\n"
            "            if attempt == max_attempts:\n"
            "                raise\n"
            "        except Exception:\n"
            "            connection.rollback()\n"
            "            raise\n"
            "        finally:\n"
            "            connection.close()\n"
        )
    raise RuntimeError(case_id)


def implementation_path(case_id):
    return {
        "node-versioned-deferred": "src/deferred.js",
        "go-metadata-roundtrip": "document/document.go",
        "python-sqlite-retry": "transfer.py",
    }[case_id]


def main():
    failures = []
    results = []
    for fixture in sorted(path for path in FIXTURES.iterdir() if path.is_dir()):
        manifest = json.loads((fixture / "fixture.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory(prefix=f"{manifest['id']}-self-check-") as directory:
            workspace = Path(directory)
            shutil.copytree(fixture / manifest["public_dir"], workspace, dirs_exist_ok=True)
            initial = run(manifest["public_test"], workspace)
            path = workspace / implementation_path(manifest["id"])
            path.write_text(fixed_text(manifest["id"], path), encoding="utf-8")
            public = run(manifest["public_test"], workspace)
            copy_grader(fixture, workspace, manifest)
            grader = run(manifest["grader_test"], workspace)
            expectation = manifest.get("initial_public_expectation", "fail")
            if expectation == "fail":
                initial_public_valid = initial.returncode != 0
            elif expectation == "pass":
                initial_public_valid = initial.returncode == 0
            elif expectation == "runtime-dependent":
                initial_public_valid = True
            else:
                raise RuntimeError(
                    f"{manifest['id']}: invalid initial_public_expectation"
                )
            result = {
                "case_id": manifest["id"],
                "initial_public_valid": initial_public_valid,
                "fixed_public_passed": public.returncode == 0,
                "fixed_grader_passed": grader.returncode == 0,
            }
            results.append(result)
            if not all(result.values()):
                failures.append(manifest["id"])
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
