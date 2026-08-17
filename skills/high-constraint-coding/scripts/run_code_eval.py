import argparse
import hashlib
import json
import os
import signal
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path, PurePosixPath


class EvalError(Exception):
    pass


def load_manifest(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "id",
        "prompt",
        "public_dir",
        "grader_dir",
        "public_test",
        "grader_test",
        "timeout_seconds",
        "allowed_paths",
        "protected_test_paths",
        "dependency_files",
        "forbid_new_dependencies",
    }
    missing = sorted(required - data.keys())
    if missing:
        raise EvalError(f"missing manifest fields: {', '.join(missing)}")
    for field in ("id", "prompt", "public_dir", "grader_dir"):
        if not isinstance(data[field], str) or not data[field]:
            raise EvalError(f"{field} must be a non-empty string")
    for field in ("public_test", "grader_test"):
        value = data[field]
        if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
            raise EvalError(f"{field} must be a non-empty argv array")
    for field in ("allowed_paths", "protected_test_paths", "dependency_files"):
        value = data[field]
        if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
            raise EvalError(f"{field} must be a string array")
    if not data["allowed_paths"]:
        raise EvalError("allowed_paths must not be empty")
    if type(data["forbid_new_dependencies"]) is not bool:
        raise EvalError("forbid_new_dependencies must be a boolean")
    if not isinstance(data["timeout_seconds"], int) or data["timeout_seconds"] <= 0:
        raise EvalError("timeout_seconds must be a positive integer")
    if "grader_target" in data and (
        not isinstance(data["grader_target"], str) or not data["grader_target"]
    ):
        raise EvalError("grader_target must be a non-empty string")
    replacements = data.get("grader_replacements", {})
    if not isinstance(replacements, dict) or not all(
        isinstance(source, str) and isinstance(target, str)
        for source, target in replacements.items()
    ):
        raise EvalError("grader_replacements must map strings to strings")
    for field in ("public_dir", "grader_dir"):
        normalize_relative(data[field])
    for field in ("allowed_paths", "protected_test_paths", "dependency_files"):
        for value in data[field]:
            normalize_relative(value)
    if "grader_target" in data:
        normalize_relative(data["grader_target"])
    return data


def resolve_child(root, value):
    root = root.resolve()
    candidate = (root / value).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise EvalError(f"path escapes fixture root: {value}") from exc
    return candidate


def normalize_relative(value):
    path = PurePosixPath(value.replace("\\", "/"))
    if (
        path.is_absolute()
        or ".." in path.parts
        or not path.parts
        or any(part in ("", ".") for part in path.parts)
        or (path.parts and ":" in path.parts[0])
    ):
        raise EvalError(f"unsafe relative path: {value}")
    return path.as_posix()


def copy_tree(source, destination):
    if not source.is_dir():
        raise EvalError(f"missing directory: {source}")
    shutil.copytree(source, destination, dirs_exist_ok=True)


def snapshot(root):
    files = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        files[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return files


def changed_paths(before, after):
    return sorted(path for path in before.keys() | after.keys() if before.get(path) != after.get(path))


def path_matches(path, rules):
    normalized = PurePosixPath(path)
    for rule in rules:
        clean = normalize_relative(rule)
        target = PurePosixPath(clean)
        if clean.endswith("/"):
            if normalized.is_relative_to(PurePosixPath(clean.rstrip("/"))):
                return True
        elif normalized == target or normalized.is_relative_to(target):
            return True
    return False


def run_command(argv, cwd, timeout_seconds, env=None):
    started = time.monotonic()
    creationflags = subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
    try:
        process = subprocess.Popen(
            argv,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            shell=False,
            env=env,
            start_new_session=os.name != "nt",
            creationflags=creationflags,
        )
        stdout, stderr = process.communicate(timeout=timeout_seconds)
        return {
            "argv": argv,
            "exit_code": process.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "timed_out": False,
            "duration_ms": round((time.monotonic() - started) * 1000),
        }
    except subprocess.TimeoutExpired as exc:
        terminate_process_tree(process)
        stdout, stderr = process.communicate()
        return {
            "argv": argv,
            "exit_code": None,
            "stdout": stdout or exc.stdout or "",
            "stderr": stderr or exc.stderr or "",
            "timed_out": True,
            "duration_ms": round((time.monotonic() - started) * 1000),
        }
    except OSError as exc:
        return {
            "argv": argv,
            "exit_code": None,
            "stdout": "",
            "stderr": str(exc),
            "timed_out": False,
            "duration_ms": round((time.monotonic() - started) * 1000),
        }


def terminate_process_tree(process):
    if process.poll() is not None:
        return
    if os.name == "nt":
        subprocess.run(
            ["taskkill", "/PID", str(process.pid), "/T", "/F"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            shell=False,
        )
    else:
        os.killpg(process.pid, signal.SIGKILL)


def ensure_safe_destination(workspace, relative):
    workspace = workspace.resolve()
    destination = workspace / relative
    current = destination.parent
    while current != workspace:
        if current.exists() and current.is_symlink():
            raise EvalError(f"grader destination crosses a symbolic link: {relative}")
        resolved = current.resolve()
        try:
            resolved.relative_to(workspace)
        except ValueError as exc:
            raise EvalError(f"grader destination escapes workspace: {relative}") from exc
        current = current.parent
    if destination.exists() or destination.is_symlink():
        raise EvalError(f"grader destination already exists: {relative}")
    return destination


def copy_grader(grader_dir, workspace, grader_target=None):
    copied = []
    if not grader_dir.is_dir():
        raise EvalError(f"missing grader directory: {grader_dir}")
    files = [path for path in sorted(grader_dir.rglob("*")) if path.is_file()]
    if grader_target:
        if len(files) != 1:
            raise EvalError("grader_target requires exactly one grader file")
        target = PurePosixPath(normalize_relative(grader_target))
        destination = ensure_safe_destination(workspace, target)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(files[0], destination)
        return [{"source": files[0], "target": target.as_posix()}]
    for source in files:
        relative = source.relative_to(grader_dir)
        destination = ensure_safe_destination(workspace, relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append({"source": source, "target": relative.as_posix()})
    return copied


def dependency_changes(before, after, dependency_files):
    changes = []
    for value in dependency_files:
        path = normalize_relative(value)
        if before.get(path) != after.get(path):
            changes.append(path)
    return changes


def remove_injected_grader(workspace, grader_files):
    for item in grader_files:
        path = workspace / item["target"]
        if path.exists():
            path.unlink()
        parent = path.parent
        while parent != workspace and parent.exists() and not any(parent.iterdir()):
            parent.rmdir()
            parent = parent.parent


def rewrite_grader_files(workspace, grader_files, replacements):
    for item in grader_files:
        path = workspace / item["target"]
        text = path.read_text(encoding="utf-8")
        for source, replacement in replacements.items():
            text = text.replace(source, replacement)
        path.write_text(text, encoding="utf-8")


def evaluate(manifest_path, workspace, agent_command=None, keep_workspace=False):
    manifest_path = manifest_path.resolve()
    fixture_root = manifest_path.parent
    manifest = load_manifest(manifest_path)
    public_dir = resolve_child(fixture_root, manifest["public_dir"])
    grader_dir = resolve_child(fixture_root, manifest["grader_dir"])
    timeout = manifest["timeout_seconds"]
    owns_workspace = workspace is None
    temporary = None
    if owns_workspace:
        temporary = tempfile.TemporaryDirectory(prefix=f"{manifest['id']}-")
        workspace = Path(temporary.name) / "workspace"
    else:
        workspace = workspace.resolve()
        if workspace.exists() and any(workspace.iterdir()):
            raise EvalError(f"workspace must be empty: {workspace}")
    workspace.mkdir(parents=True, exist_ok=True)
    copy_tree(public_dir, workspace)
    baseline = snapshot(workspace)
    agent_result = None
    if agent_command:
        env = os.environ.copy()
        env["CODE_EVAL_PROMPT"] = manifest["prompt"]
        agent_result = run_command(agent_command, workspace, timeout, env)
    candidate = snapshot(workspace)
    candidate_changes = changed_paths(baseline, candidate)
    allowed = manifest["allowed_paths"]
    protected = {normalize_relative(path) for path in manifest["protected_test_paths"]}
    forbidden = sorted(path for path in candidate_changes if not path_matches(path, allowed))
    protected_changes = sorted(path for path in candidate_changes if path in protected)
    dependencies = dependency_changes(baseline, candidate, manifest["dependency_files"])
    hard_failures = []
    if agent_result and (agent_result["timed_out"] or agent_result["exit_code"] != 0):
        hard_failures.append("agent command failed")
    if forbidden:
        hard_failures.append("changed paths outside allowed scope")
    if protected_changes:
        hard_failures.append("protected tests changed")
    if manifest["forbid_new_dependencies"] and dependencies:
        hard_failures.append("dependency files changed")
    public_result = run_command(manifest["public_test"], workspace, timeout)
    if public_result["timed_out"] or public_result["exit_code"] != 0:
        hard_failures.append("public tests failed")
    grader_files = copy_grader(grader_dir, workspace, manifest.get("grader_target"))
    rewrite_grader_files(workspace, grader_files, manifest.get("grader_replacements", {}))
    grader_result = run_command(manifest["grader_test"], workspace, timeout)
    if grader_result["timed_out"] or grader_result["exit_code"] != 0:
        hard_failures.append("grader tests failed")
    remove_injected_grader(workspace, grader_files)
    result = {
        "case_id": manifest["id"],
        "passed": not hard_failures,
        "hard_failures": hard_failures,
        "candidate_changes": candidate_changes,
        "forbidden_changes": forbidden,
        "protected_test_changes": protected_changes,
        "dependency_changes": dependencies,
        "grader_files": [item["target"] for item in grader_files],
        "agent": agent_result,
        "public_tests": public_result,
        "grader_tests": grader_result,
    }
    if keep_workspace:
        result["workspace"] = str(workspace)
        if temporary:
            temporary._finalizer.detach()
    if temporary and not keep_workspace:
        temporary.cleanup()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--agent-command", nargs=argparse.REMAINDER)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--keep-workspace", action="store_true")
    args = parser.parse_args()
    try:
        result = evaluate(
            args.manifest,
            args.workspace,
            args.agent_command,
            args.keep_workspace,
        )
    except (EvalError, json.JSONDecodeError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
