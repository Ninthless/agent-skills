import argparse
import json
import re
import sys
from itertools import combinations
from pathlib import Path


STYLE_FIELDS = [
    "layout_model",
    "density",
    "typography_strategy",
    "palette_strategy",
    "geometry",
    "surface_strategy",
    "imagery_strategy",
    "motion_tone",
    "platform_conventions",
]

WORD_PATTERN = re.compile(r"[^\W_]+", re.UNICODE)
CJK_PATTERN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def parse_args():
    parser = argparse.ArgumentParser(description="Compare visual fingerprints across unrelated UI products.")
    parser.add_argument("manifests", nargs="+", type=Path)
    parser.add_argument("--threshold", type=float, default=0.72)
    parser.add_argument("--include-same-family", action="store_true")
    return parser.parse_args()


def read_manifest(path):
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        raise ValueError(f"manifest does not exist: {path}")
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON in {path} at line {error.lineno}, column {error.colno}: {error.msg}")
    if not isinstance(data, dict):
        raise ValueError(f"manifest root must be an object: {path}")
    surface = data.get("surface")
    style = data.get("style")
    if not isinstance(surface, dict) or not isinstance(style, dict):
        raise ValueError(f"manifest needs surface and style objects: {path}")
    name = surface.get("name")
    if not isinstance(name, str) or not name.strip():
        name = path.stem
    family = surface.get("product_family")
    if not isinstance(family, str):
        family = ""
    missing = [field for field in STYLE_FIELDS if not isinstance(style.get(field), str) or not style[field].strip()]
    if missing:
        raise ValueError(f"{path} has empty style fields: {', '.join(missing)}")
    return {"path": path, "name": name.strip(), "family": family.strip().lower(), "style": style}


def normalize(value):
    return " ".join(WORD_PATTERN.findall(value.lower()))


def tokens(value):
    normalized = value.lower()
    cjk_tokens = CJK_PATTERN.findall(normalized)
    word_tokens = WORD_PATTERN.findall(CJK_PATTERN.sub(" ", normalized))
    return set(cjk_tokens + word_tokens)


def token_similarity(left, right):
    left_normalized = normalize(left)
    right_normalized = normalize(right)
    if left_normalized == right_normalized:
        return 1.0
    left_tokens = tokens(left)
    right_tokens = tokens(right)
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens | right_tokens)


def compare(left, right):
    scores = {
        field: token_similarity(left["style"][field], right["style"][field])
        for field in STYLE_FIELDS
    }
    overall = sum(scores.values()) / len(scores)
    return overall, scores


def main():
    args = parse_args()
    if len(args.manifests) < 2:
        print("ERROR: provide at least two manifests", file=sys.stderr)
        return 2
    if not 0 <= args.threshold <= 1:
        print("ERROR: threshold must be from 0 to 1", file=sys.stderr)
        return 2
    try:
        manifests = [read_manifest(path) for path in args.manifests]
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    compared = 0
    failures = 0
    for left, right in combinations(manifests, 2):
        same_family = left["family"] and left["family"] == right["family"]
        if same_family and not args.include_same_family:
            print(f"SKIP {left['name']} <> {right['name']}: shared product family '{left['family']}'")
            continue
        compared += 1
        overall, scores = compare(left, right)
        status = "FAIL" if overall >= args.threshold else "PASS"
        if status == "FAIL":
            failures += 1
        most_similar = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:3]
        dimensions = ", ".join(f"{field}={score:.2f}" for field, score in most_similar)
        print(f"{status} {left['name']} <> {right['name']}: similarity={overall:.3f}; highest {dimensions}")
    if compared == 0:
        print("No unrelated product pairs were compared.")
        return 0
    print("Visual fingerprint comparison is a convergence heuristic, not visual or usability proof.")
    if failures:
        print(f"{failures} pair(s) met or exceeded the similarity threshold {args.threshold:.2f}.")
        return 1
    print(f"All {compared} pair(s) were below the similarity threshold {args.threshold:.2f}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
