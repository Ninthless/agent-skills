import argparse
import json
import sys
from pathlib import Path


CONSTRAINT_KEYS = {
    "required",
    "nullable",
    "format",
    "pattern",
    "minimum",
    "maximum",
    "exclusiveMinimum",
    "exclusiveMaximum",
    "multipleOf",
    "minLength",
    "maxLength",
    "minItems",
    "maxItems",
    "uniqueItems",
    "default",
    "enum",
    "const",
    "readOnly",
    "writeOnly",
}


def load_document(path):
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError(
            "YAML input requires PyYAML; use JSON or install PyYAML"
        ) from exc
    return yaml.safe_load(text)


def escape_pointer_part(value):
    return str(value).replace("~", "~0").replace("/", "~1")


def walk(node, pointer=""):
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{pointer}/{escape_pointer_part(key)}"
            yield child, key, value
            yield from walk(value, child)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            child = f"{pointer}/{index}"
            yield from walk(value, child)


def collect_claims(document):
    claims = {}
    for index, claim in enumerate(document.get("claims", [])):
        pointer = claim.get("pointer")
        evidence = claim.get("evidence")
        if not isinstance(pointer, str) or not pointer.startswith("/"):
            raise ValueError(f"claims[{index}].pointer must be a JSON Pointer")
        if not isinstance(evidence, str) or not evidence.strip():
            raise ValueError(f"claims[{index}].evidence must be non-empty")
        if pointer in claims:
            raise ValueError(f"duplicate claim pointer: {pointer}")
        claims[pointer] = claim
    return claims


def collect_sensitive_values(specification):
    values = {}
    for pointer, key, value in walk(specification):
        if key in CONSTRAINT_KEYS:
            values[pointer] = value
        elif key == "type" and (
            value == "null"
            or isinstance(value, list)
            and "null" in value
        ):
            values[pointer] = value
        elif pointer == "/info/version":
            values[pointer] = value
        elif key == "security" and (
            pointer == "/security" or "/paths/" in pointer
        ):
            values[pointer] = value
    return values


def validate(specification, evidence):
    claims = collect_claims(evidence)
    sensitive = collect_sensitive_values(specification)
    errors = []

    for pointer, value in sensitive.items():
        claim = claims.get(pointer)
        if claim is None:
            errors.append(f"unsupported contract claim at {pointer}: {value!r}")
            continue
        if "value" in claim and claim["value"] != value:
            errors.append(
                f"evidence value mismatch at {pointer}: "
                f"expected {claim['value']!r}, found {value!r}"
            )

    for pointer in claims:
        if pointer not in sensitive:
            errors.append(f"unused evidence claim: {pointer}")

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("specification", type=Path)
    parser.add_argument("evidence", type=Path)
    args = parser.parse_args()

    try:
        specification = load_document(args.specification)
        evidence = load_document(args.evidence)
        errors = validate(specification, evidence)
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("OpenAPI evidence validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
