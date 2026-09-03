# Agent Skills

[简体中文](./README.zh-CN.md) | English

A curated collection of production-oriented Agent Skills for repeatable software engineering, learning during AI-assisted development, product discovery, documentation, interface design, platform-specific development, and delivery workflows.

The repository is built around a simple idea: recurring agent work should be governed by explicit operating rules, progressive disclosure, and evidence-based completion instead of relying on a large prompt or improvised instructions every time. It also treats AI-assisted delivery and human learning as compatible goals: the agent can implement the project while exposing the concepts, decisions, and verification evidence needed for the user to understand and eventually modify it.

## What This Repository Provides

Each skill is a self-contained workflow that teaches a compatible coding agent when to activate, what evidence to gather, how to make decisions, which failure modes to avoid, and how to verify the result.

The collection emphasizes:

- bounded scope and explicit assumptions
- project-native implementation instead of generic generated architecture
- human hand-maintainability across programming languages
- active or passive learning during AI-led implementation, debugging, and refactoring
- contract, lifecycle, protocol, and dependency verification
- complete user-facing states and rendered UI evidence
- documentation derived from source and runtime evidence
- safe platform-specific execution and delivery
- reusable evaluation cases for trigger routing and behavior quality

## Skills

| Skill | Purpose |
| --- | --- |
| [`build-user-facing-ui`](./skills/build-user-facing-ui/) | Build, redesign, review, and verify distinctive user-facing interfaces across web, mobile, desktop, games, kiosks, and specialized surfaces. |
| [`english-spec-first`](./skills/english-spec-first/) | Normalize rough, multilingual, or materially ambiguous requests into a concise English working specification before execution. |
| [`freelance-order-triage`](./skills/freelance-order-triage/) | Evaluate client work, hidden scope, quote posture, delivery risk, milestones, revisions, and acceptance criteria before implementation. |
| [`git-checkpoint-push`](./skills/git-checkpoint-push/) | Create coherent Git checkpoints with targeted staging, Conventional Commit messages, remote safety checks, and explicit push results. |
| [`high-constraint-coding`](./skills/high-constraint-coding/) | Apply a minimal, evidence-led coding workflow that produces correct, project-native code humans can locate, trace, modify, and verify directly. |
| [`learn-while-building`](./skills/learn-while-building/) | Passive learning companion during vibecoding: expose the relevant model, decisions, and verification while implementing, without requiring the user to ask or interrupting delivery with quizzes. |
| [`no-code-comments`](./skills/no-code-comments/) | Keep generated and modified code-like artifacts comment-free by default while preserving required directives and documentation contracts. |
| [`powershell-safe-commands`](./skills/powershell-safe-commands/) | Prevent PowerShell interpolation, quoting, wrapper-layer, path, and nested command failures on Windows. |
| [`vibecoding-domain-scout`](./skills/vibecoding-domain-scout/) | Research unfamiliar or regulated domains and convert findings into workflows, constraints, risks, MVP boundaries, and build-ready briefs. |
| [`websearch-first`](./skills/websearch-first/) | Search authoritative current sources before answering or editing, reconcile external evidence with local facts, and cite the sources that materially affect the result. |
| [`write-api-docs`](./skills/write-api-docs/) | Create or review API contracts from routes, schemas, clients, tests, runtime evidence, OpenAPI, GraphQL, gRPC, webhooks, or messages without inventing unsupported behavior. |
| [`xposed-module-dev`](./skills/xposed-module-dev/) | Build, review, migrate, and debug Android Xposed or LSPosed modules across modern libxposed and legacy XposedBridge projects. |

## Design

Every skill follows the [Agent Skills open standard](https://agentskills.io) and uses progressive disclosure:

1. Frontmatter metadata decides when the skill should activate.
2. `SKILL.md` provides the core operating workflow.
3. Bundled resources are loaded or executed only when the task needs them.

A skill directory may contain:

```text
skills/
  <skill-name>/
    SKILL.md
    agents/
      claude.yaml
      openai.yaml
    references/
    scripts/
    evals/
      evals.json
      trigger_eval.json
```

Only `SKILL.md` is required by the standard. This repository uses the optional directories for:

- `agents/`: platform-facing names, descriptions, default prompts, and invocation policy
- `references/`: detailed guidance that should not occupy the base skill context
- `scripts/`: deterministic validation or evidence-processing tools
- `evals/`: positive and negative trigger cases plus realistic behavioral scenarios

The files in `agents/` are repository extensions for specific agent platforms and are not part of the base Agent Skills standard.

## How Skills Work Together

Skills can operate independently or compose around one task. Typical flows include:

- `english-spec-first` -> `vibecoding-domain-scout` -> implementation skill
- `freelance-order-triage` -> paid discovery or bounded delivery plan
- `websearch-first` + any task skill -> current external evidence reconciled with local facts
- `high-constraint-coding` + `no-code-comments` -> controlled production code with a clean source style
- `high-constraint-coding` + `no-code-comments` + `learn-while-building` -> controlled implementation, clean source, and a compact learning overlay
- `build-user-facing-ui` + `high-constraint-coding` -> complete UI behavior with disciplined implementation
- `write-api-docs` -> evidence-backed integration contract
- completed work -> `git-checkpoint-push`

The active task still determines scope. A companion skill should strengthen the workflow without expanding the requested deliverable.

## Installation

Compatible agents discover project-level or user-level skills from these locations:

| Path | Scope |
| --- | --- |
| `.agents/skills/` | Project-level, generic |
| `.cursor/skills/` | Project-level, Cursor |
| `.claude/skills/` | Project-level, Claude Code |
| `~/.agents/skills/` | User-level, generic |
| `~/.cursor/skills/` | User-level, Cursor |
| `~/.claude/skills/` | User-level, Claude Code |

Codex currently discovers repository skills from `.agents/skills/` and personal skills from `~/.agents/skills/`. Platform-specific paths depend on the host agent's own discovery rules.

Install one skill on Windows:

```powershell
New-Item -ItemType Directory -Force $env:USERPROFILE\.agents\skills | Out-Null
Copy-Item -Recurse .\skills\high-constraint-coding $env:USERPROFILE\.agents\skills\
```

Install the complete collection:

```powershell
New-Item -ItemType Directory -Force $env:USERPROFILE\.agents\skills | Out-Null
Copy-Item -Recurse .\skills\* $env:USERPROFILE\.agents\skills\
```

Use `.cursor\skills` or `.claude\skills` instead when that platform's discovery rules require a platform-specific location.

On macOS or Linux:

```bash
mkdir -p ~/.agents/skills
cp -r ./skills/high-constraint-coding ~/.agents/skills/
cp -r ./skills/* ~/.agents/skills/
```

Restart or reload the agent when its skill discovery implementation requires it.

## Usage

Compatible agents can invoke skills automatically from their metadata. Skills may also be referenced explicitly when the agent supports named skill invocation.

Example requests:

```text
Use high-constraint-coding to fix this regression with the smallest complete change.

Use build-user-facing-ui to redesign this workflow and verify every responsive state.

Use write-api-docs to reconcile the frontend client and backend routes into one API contract.

Fix this bug and run the tests.

Use learn-while-building in guided mode while implementing this feature. Write the code, but teach me the request flow, key decisions, and how the tests prove the behavior.
```

Read the target skill's `description` and workflow before assuming it applies. Negative trigger examples intentionally prevent specialized skills from taking over simple conceptual or unrelated tasks.

## Evaluation And Validation

Complex skills include complementary evaluation surfaces:

- `trigger_eval.json` checks whether representative requests should or should not activate the skill.
- `evals.json` checks expected workflow behavior on realistic tasks without prescribing one implementation.
- Code-eval fixtures execute real repository changes against public tests, grader-only acceptance tests, dependency restrictions, and diff scope policies.

Some skills also include deterministic scripts. Examples include UI evidence validation, visual fingerprint comparison, and OpenAPI evidence validation.

`high-constraint-coding` includes four cross-platform code fixtures for runtime-version compatibility, persistence round trips, transaction retry boundaries, and provider-integration maintainability. Its runner copies only the public fixture into an isolated workspace, runs an optional agent command, injects grader tests after implementation, and treats test, protected-path, dependency, and scope violations as hard failures.

Run the deterministic checks:

```powershell
python -m unittest skills/high-constraint-coding/scripts/test_run_code_eval.py -v
python skills/high-constraint-coding/scripts/self_check_code_evals.py
```

Run one candidate through the isolated evaluator:

```powershell
python skills/high-constraint-coding/scripts/run_code_eval.py skills/high-constraint-coding/evals/fixtures/go-metadata-roundtrip/fixture.json --agent-command <executable> <arguments>
```

The evaluator passes the task through the `CODE_EVAL_PROMPT` environment variable. An applicable failed gate blocks completion; an unverified required gate permits only `Implemented but unverified`.

When modifying a skill:

1. keep `SKILL.md` concise and move detailed material into direct references
2. update platform metadata when the skill's purpose or default behavior changes
3. add trigger and behavioral evaluations for generalizable rules
4. run relevant scripts and structural validation
5. forward-test complex changes with fresh tasks that do not reveal the expected answer

## Repository Principles

- Prefer evidence over plausible API names or remembered behavior.
- Treat correctness, contracts, lifecycle closure, and human maintenance as stronger goals than brevity.
- Keep implementation and guidance native to the target repository and language.
- Add abstractions only when they isolate a real policy, side effect, dependency, ownership boundary, or change reason.
- Do not infer code authorship from style or optimize for detector evasion.
- Do not claim completion beyond the verification that was actually performed.

## License

Copyright (c) 2026 Ninthless. All rights reserved.

This repository contains proprietary personal workflow materials. Viewing the repository does not grant permission to copy, modify, redistribute, publish, sublicense, host, republish, sell, or create derivative works from any part of it.

See [LICENSE](./LICENSE) for the complete terms.
