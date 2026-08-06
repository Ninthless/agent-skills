# Agent Skills

[简体中文](README.zh-CN.md)

A proprietary collection of ten focused Agent Skills for repeatable analysis, execution, action, and companion workflows.

## Skills

- `bug-diagnosis`: investigate unknown software defects and produce evidence-backed root causes before repair.
- `freelance-order-triage`: decide how to accept, clarify, stage, quote, reshape, or decline commercial coding work.
- `git-checkpoint-push`: perform only explicitly authorized Git checkpoint actions against the real repository state.
- `high-constraint-coding`: implement and review actual source in all programming languages with language- and ecosystem-native, senior-engineer-quality properties: deliberate project-native design, maintainable/readable code, bounded scope, and verified behavior. This is an engineering-quality claim, never an authorship claim; web work retains browser-backed verification when available.
- `no-code-comments`: enforce comment-free code-like output as an explicit or repository-established companion policy.
- `powershell-safe-commands`: protect commands from PowerShell-specific parsing, quoting, interpolation, and encoding hazards.
- `requirement-analysis`: turn rough or conflicting material into a bounded, testable implementation contract.
- `technical-solution-research`: research current libraries, frameworks, protocols, standards, versions, and solution choices.
- `vibecoding-domain-scout`: research unfamiliar industry workflows, business rules, policy, compliance, and expert terminology.
- `write-api-docs`: create, reconcile, or review evidence-backed API contracts and integration documentation.

## Format and extensions

Each `skills/<name>/SKILL.md` follows the Agent Skills open standard and carries the portable name, description, and instructions. `agents/openai.yaml` and `agents/claude.yaml` provide platform-specific interface prompts and invocation policy. `skills-manifest.json` is a repository-local extension for routing mode, role, implicit invocation, side effects, and handoff metadata; it is not part of the open standard and does not duplicate skill descriptions.

See `docs/skill-routing.md` for final-artifact ownership, companions, zero-skill behavior, sequences, and authorization boundaries.

## Layout

```txt
skills/
  <skill-name>/
    SKILL.md
    agents/
    evals/
    references/
evals/
docs/
scripts/
```

## Validation

Run the complete local contract from the repository root:

```powershell
python scripts/validate_all.py
```

The command validates skill metadata and references, both agent files, manifest consistency, behavior and trigger evals, cross-skill routing synchronization, machine-readable contract obligation polarity, repository JSON, and size reports. `scripts/audit_skill_sizes.py` distinguishes open-format hard limits from repository recommendations and reports the Codex 8000-character initial catalog budget as a platform budget rather than an open standard rule.

The GitHub Actions workflow in `.github/workflows/validate.yml` runs the same command with read-only repository permissions. Routing cases define future multi-run model-rate expectations, but the repository validator does not execute live model routing trials. Web implementation routes to `high-constraint-coding`, whose verification contract requires dev-server reuse/startup checks, browser flow and responsive checks, console inspection, relevant network inspection, useful visual or DOM evidence, and fix/retest closure when tools are available.

## Install

Copy a skill folder to a compatible project or user skill directory such as `.agents/skills/`, `.cursor/skills/`, `.claude/skills/`, `.codex/skills/`, or their user-level equivalents.

```powershell
Copy-Item -Recurse .\skills\* $env:USERPROFILE\.agents\skills
```

## License

Copyright (c) 2026 Ninthless. All rights reserved.

These skills are proprietary personal workflow materials. They may not be copied, modified, redistributed, republished, sublicensed, or used to create derivative works without prior written permission.
