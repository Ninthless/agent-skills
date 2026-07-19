import argparse
import json
import math
import sys
from pathlib import Path


WEB_DEFAULT_BUDGETS = {
    "lcp_ms": 2500,
    "inp_ms": 200,
    "cls": 0.1,
}

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


def template():
    return {
        "surface": {
            "name": "",
            "product_family": "",
            "archetype": "",
            "platforms": ["web"],
            "primary_user": "",
            "primary_task": "",
            "required_viewports": ["desktop", "mobile"],
            "scope": "substantial",
        },
        "rendered": {
            "screenshots": [
                {"path": "screenshots/desktop-primary.png", "viewport": "desktop", "state": "primary"},
                {"path": "screenshots/mobile-recovery.png", "viewport": "mobile", "state": "error"},
            ],
            "console_errors": [],
            "asset_failures": [],
        },
        "workflows": [
            {"name": "Primary task", "kind": "primary", "outcome": "", "passed": False},
            {"name": "Recovery path", "kind": "recovery", "outcome": "", "passed": False},
        ],
        "accessibility": {
            "keyboard_primary_flow": False,
            "focus_visible": False,
            "focus_not_obscured": False,
            "color_not_only_signal": False,
            "target_size_min_css_px": 0,
            "uses_dragging": False,
            "drag_alternative": None,
            "has_authentication": False,
            "accessible_authentication": None,
            "automated_critical_violations": 0,
            "zoom_reflow": False,
        },
        "trust": {
            "no_deceptive_urgency": True,
            "no_hidden_material_terms": True,
            "symmetric_choice": True,
            "reversible_consent": None,
            "clear_cancellation": None,
            "has_purchase": False,
            "has_subscription": False,
            "collects_personal_data": False,
        },
        "performance": {
            "kind": "web",
            "measurement_mode": "lab",
            "lcp_ms": None,
            "inp_ms": None,
            "cls": None,
            "budgets": WEB_DEFAULT_BUDGETS.copy(),
            "measurements": [
                {
                    "name": "Primary route lab run",
                    "mode": "lab",
                    "environment": "",
                    "sample_count": 0,
                    "percentile": None,
                    "lcp_ms": None,
                    "inp_ms": None,
                    "cls": None,
                }
            ],
        },
        "user_evidence": {
            "status": "not_run",
            "participants": 0,
            "primary_task_success_rate": None,
            "median_task_time_seconds": None,
            "critical_error_rate": None,
            "limitations": "Representative-user evaluation has not been run.",
        },
        "style": {field: "" for field in STYLE_FIELDS},
    }


def read_json(path):
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        raise ValueError(f"manifest does not exist: {path}")
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}")


def mapping(value, name, errors):
    if isinstance(value, dict):
        return value
    errors.append(f"{name} must be an object")
    return {}


def sequence(value, name, errors):
    if isinstance(value, list):
        return value
    errors.append(f"{name} must be an array")
    return []


def require_text(container, key, name, errors):
    value = container.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{name}.{key} must be non-empty text")
        return ""
    return value.strip()


def require_bool(container, key, name, errors, expected=True):
    value = container.get(key)
    if not isinstance(value, bool):
        errors.append(f"{name}.{key} must be true or false")
        return None
    if expected is not None and value is not expected:
        errors.append(f"{name}.{key} must be {str(expected).lower()}")
    return value


def finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def valid_image_file(path):
    try:
        with path.open("rb") as handle:
            header = handle.read(32)
    except OSError:
        return False
    suffix = path.suffix.lower()
    if suffix == ".png":
        return (
            header.startswith(b"\x89PNG\r\n\x1a\n")
            and len(header) >= 24
            and int.from_bytes(header[16:20], "big") > 0
            and int.from_bytes(header[20:24], "big") > 0
        )
    if suffix in {".jpg", ".jpeg"}:
        return header.startswith(b"\xff\xd8\xff")
    if suffix == ".webp":
        return len(header) >= 12 and header[:4] == b"RIFF" and header[8:12] == b"WEBP"
    return False


def validate_surface(data, errors):
    surface = mapping(data.get("surface"), "surface", errors)
    for key in ["name", "archetype", "primary_user", "primary_task", "scope"]:
        require_text(surface, key, "surface", errors)
    platforms = sequence(surface.get("platforms"), "surface.platforms", errors)
    if not platforms or any(not isinstance(item, str) or not item.strip() for item in platforms):
        errors.append("surface.platforms must contain non-empty platform names")
    viewports = sequence(surface.get("required_viewports"), "surface.required_viewports", errors)
    if not viewports or any(not isinstance(item, str) or not item.strip() for item in viewports):
        errors.append("surface.required_viewports must contain non-empty viewport names")
    return surface, {item.strip().lower() for item in viewports if isinstance(item, str) and item.strip()}


def validate_rendered(data, manifest_path, required_viewports, scope, errors):
    rendered = mapping(data.get("rendered"), "rendered", errors)
    screenshots = sequence(rendered.get("screenshots"), "rendered.screenshots", errors)
    covered_viewports = set()
    covered_states = set()
    for index, item in enumerate(screenshots):
        screenshot = mapping(item, f"rendered.screenshots[{index}]", errors)
        screenshot_path = require_text(screenshot, "path", f"rendered.screenshots[{index}]", errors)
        viewport = require_text(screenshot, "viewport", f"rendered.screenshots[{index}]", errors).lower()
        state = require_text(screenshot, "state", f"rendered.screenshots[{index}]", errors).lower()
        if viewport:
            covered_viewports.add(viewport)
        if state:
            covered_states.add(state)
        if screenshot_path:
            resolved = (manifest_path.parent / screenshot_path).resolve()
            if not resolved.is_file():
                errors.append(f"screenshot file does not exist: {screenshot_path}")
            elif not valid_image_file(resolved):
                errors.append(f"screenshot is not a valid PNG, JPEG, or WebP image: {screenshot_path}")
    missing_viewports = sorted(required_viewports - covered_viewports)
    if missing_viewports:
        errors.append(f"screenshots do not cover required viewports: {', '.join(missing_viewports)}")
    if "primary" not in covered_states:
        errors.append("screenshots must include a primary state")
    recovery_states = {"empty", "error", "recovery", "unavailable", "permission"}
    if scope == "substantial" and not covered_states.intersection(recovery_states):
        errors.append("substantial surfaces need a screenshot of an empty, error, recovery, unavailable, or permission state")
    for key in ["console_errors", "asset_failures"]:
        values = sequence(rendered.get(key), f"rendered.{key}", errors)
        if values:
            errors.append(f"rendered.{key} must be empty before completion")


def validate_workflows(data, scope, errors):
    workflows = sequence(data.get("workflows"), "workflows", errors)
    primary_passed = False
    recovery_passed = False
    recovery_kinds = {"empty", "error", "recovery", "unavailable", "permission"}
    for index, item in enumerate(workflows):
        workflow = mapping(item, f"workflows[{index}]", errors)
        require_text(workflow, "name", f"workflows[{index}]", errors)
        kind = require_text(workflow, "kind", f"workflows[{index}]", errors).lower()
        require_text(workflow, "outcome", f"workflows[{index}]", errors)
        passed = require_bool(workflow, "passed", f"workflows[{index}]", errors, expected=None)
        if kind == "primary" and passed:
            primary_passed = True
        if kind in recovery_kinds and passed:
            recovery_passed = True
    if not primary_passed:
        errors.append("at least one primary workflow must pass")
    if scope == "substantial" and not recovery_passed:
        errors.append("substantial surfaces need one passing empty, error, recovery, unavailable, or permission workflow")


def validate_accessibility(data, errors):
    accessibility = mapping(data.get("accessibility"), "accessibility", errors)
    for key in [
        "keyboard_primary_flow",
        "focus_visible",
        "focus_not_obscured",
        "color_not_only_signal",
        "zoom_reflow",
    ]:
        require_bool(accessibility, key, "accessibility", errors)
    target_size = accessibility.get("target_size_min_css_px")
    if not finite_number(target_size) or target_size < 24:
        errors.append("accessibility.target_size_min_css_px must be at least 24")
    violations = accessibility.get("automated_critical_violations")
    if not isinstance(violations, int) or isinstance(violations, bool) or violations < 0:
        errors.append("accessibility.automated_critical_violations must be a non-negative integer")
    elif violations != 0:
        errors.append("accessibility.automated_critical_violations must be 0")
    uses_dragging = require_bool(accessibility, "uses_dragging", "accessibility", errors, expected=None)
    if uses_dragging:
        require_bool(accessibility, "drag_alternative", "accessibility", errors)
    has_authentication = require_bool(accessibility, "has_authentication", "accessibility", errors, expected=None)
    if has_authentication:
        require_bool(accessibility, "accessible_authentication", "accessibility", errors)


def validate_trust(data, errors):
    trust = mapping(data.get("trust"), "trust", errors)
    for key in ["no_deceptive_urgency", "no_hidden_material_terms", "symmetric_choice"]:
        require_bool(trust, key, "trust", errors)
    has_purchase = require_bool(trust, "has_purchase", "trust", errors, expected=None)
    has_subscription = require_bool(trust, "has_subscription", "trust", errors, expected=None)
    collects_personal_data = require_bool(trust, "collects_personal_data", "trust", errors, expected=None)
    if has_purchase:
        require_bool(trust, "no_hidden_material_terms", "trust", errors)
    if has_subscription:
        require_bool(trust, "clear_cancellation", "trust", errors)
    if collects_personal_data:
        require_bool(trust, "reversible_consent", "trust", errors)


def budget_value(budgets, key, default, errors):
    value = budgets.get(key, default)
    if not finite_number(value) or value < 0:
        errors.append(f"performance.budgets.{key} must be a non-negative number")
        return default
    return value


def measured_value(performance, key, errors):
    value = performance.get(key)
    if not finite_number(value) or value < 0:
        errors.append(f"performance.{key} must be a non-negative measured number")
        return None
    return value


def validate_measurement_context(measurement, name, errors, require_field_percentile=False):
    require_text(measurement, "name", name, errors)
    mode = require_text(measurement, "mode", name, errors).lower()
    if mode not in {"lab", "field"}:
        errors.append(f"{name}.mode must be lab or field")
    require_text(measurement, "environment", name, errors)
    sample_count = measurement.get("sample_count")
    if not isinstance(sample_count, int) or isinstance(sample_count, bool) or sample_count < 1:
        errors.append(f"{name}.sample_count must be a positive integer")
    if mode == "field" and require_field_percentile:
        percentile = measurement.get("percentile")
        if percentile != 75:
            errors.append(f"{name}.percentile must be 75 for Core Web Vitals field evidence")
    return mode


def validate_performance(data, errors):
    performance = mapping(data.get("performance"), "performance", errors)
    kind = require_text(performance, "kind", "performance", errors).lower()
    mode = require_text(performance, "measurement_mode", "performance", errors).lower()
    if mode not in {"lab", "field", "both"}:
        errors.append("performance.measurement_mode must be lab, field, or both")
    measurements = sequence(performance.get("measurements"), "performance.measurements", errors)
    budgets = mapping(performance.get("budgets"), "performance.budgets", errors)
    if kind == "web":
        measured_modes = set()
        for key, default in WEB_DEFAULT_BUDGETS.items():
            budget = budget_value(budgets, key, default, errors)
            measured = measured_value(performance, key, errors)
            if measured is not None and measured > budget:
                errors.append(f"performance.{key} exceeds budget: {measured} > {budget}")
        if not measurements:
            errors.append("web performance requires at least one contextual measurement")
        for index, item in enumerate(measurements):
            name = f"performance.measurements[{index}]"
            measurement = mapping(item, name, errors)
            measured_modes.add(validate_measurement_context(measurement, name, errors, require_field_percentile=True))
            for key, default in WEB_DEFAULT_BUDGETS.items():
                budget = budget_value(budgets, key, default, errors)
                measured = measured_value(measurement, key, errors)
                if measured is not None and measured > budget:
                    errors.append(f"{name}.{key} exceeds budget: {measured} > {budget}")
        required_modes = {"lab", "field"} if mode == "both" else {mode}
        missing_modes = sorted(required_modes - measured_modes)
        if missing_modes:
            errors.append(f"performance.measurements do not cover declared modes: {', '.join(missing_modes)}")
    elif kind == "native":
        measured_modes = set()
        if not budgets:
            errors.append("native performance requires declared project budgets")
        if not measurements:
            errors.append("native performance requires measured scenarios")
        for index, item in enumerate(measurements):
            name = f"performance.measurements[{index}]"
            measurement = mapping(item, name, errors)
            measured_modes.add(validate_measurement_context(measurement, name, errors))
            require_text(measurement, "unit", name, errors)
            value = measurement.get("value")
            budget = measurement.get("budget")
            if not finite_number(value) or not finite_number(budget):
                errors.append(f"{name} needs numeric value and budget")
            elif value > budget:
                errors.append(f"{name} exceeds budget: {value} > {budget}")
        required_modes = {"lab", "field"} if mode == "both" else {mode}
        missing_modes = sorted(required_modes - measured_modes)
        if missing_modes:
            errors.append(f"performance.measurements do not cover declared modes: {', '.join(missing_modes)}")
    else:
        errors.append("performance.kind must be web or native")


def validate_user_evidence(data, errors):
    evidence = mapping(data.get("user_evidence"), "user_evidence", errors)
    status = require_text(evidence, "status", "user_evidence", errors).lower()
    allowed = {"not_run", "internal", "representative", "field"}
    if status not in allowed:
        errors.append("user_evidence.status must be not_run, internal, representative, or field")
        return
    participants = evidence.get("participants")
    if not isinstance(participants, int) or isinstance(participants, bool) or participants < 0:
        errors.append("user_evidence.participants must be a non-negative integer")
        participants = 0
    limitations = evidence.get("limitations")
    if not isinstance(limitations, str) or not limitations.strip():
        errors.append("user_evidence.limitations must state evidence limits")
    if status == "not_run":
        if participants != 0:
            errors.append("user_evidence.participants must be 0 when status is not_run")
        return
    if participants < 1:
        errors.append("user_evidence.participants must be at least 1 when user evidence was run")
    for key in ["primary_task_success_rate", "critical_error_rate"]:
        value = evidence.get(key)
        if not finite_number(value) or value < 0 or value > 1:
            errors.append(f"user_evidence.{key} must be a number from 0 to 1")
    task_time = evidence.get("median_task_time_seconds")
    if task_time is not None and (not finite_number(task_time) or task_time < 0):
        errors.append("user_evidence.median_task_time_seconds must be null or a non-negative number")


def validate_style(data, errors):
    style = mapping(data.get("style"), "style", errors)
    for key in STYLE_FIELDS:
        require_text(style, key, "style", errors)


def validate(data, manifest_path):
    errors = []
    if not isinstance(data, dict):
        return ["manifest root must be an object"]
    surface, viewports = validate_surface(data, errors)
    scope = surface.get("scope", "").strip().lower() if isinstance(surface.get("scope"), str) else ""
    if scope not in {"small", "substantial"}:
        errors.append("surface.scope must be small or substantial")
    validate_rendered(data, manifest_path, viewports, scope, errors)
    validate_workflows(data, scope, errors)
    validate_accessibility(data, errors)
    validate_trust(data, errors)
    validate_performance(data, errors)
    validate_user_evidence(data, errors)
    validate_style(data, errors)
    return errors


def write_template(path):
    if path.exists():
        raise ValueError(f"refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(template(), handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def parse_args():
    parser = argparse.ArgumentParser(description="Validate evidence for a user-facing UI surface.")
    parser.add_argument("manifest", nargs="?", type=Path)
    parser.add_argument("--init", dest="init_path", type=Path)
    return parser.parse_args()


def main():
    args = parse_args()
    if args.init_path:
        try:
            write_template(args.init_path)
        except ValueError as error:
            print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print(f"Created UI evidence template: {args.init_path}")
        return 0
    if not args.manifest:
        print("ERROR: provide a manifest path or use --init", file=sys.stderr)
        return 2
    try:
        data = read_json(args.manifest)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    errors = validate(data, args.manifest.resolve())
    if errors:
        print(f"UI evidence failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"UI evidence passed: {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
