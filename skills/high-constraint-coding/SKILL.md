---
name: high-constraint-coding
description: 'Implement, change, fix, build, or review actual source code in all programming languages with controlled scope, language- and ecosystem-native judgment, senior-engineer-quality design, and maintainable, readable, verified behavior. Own frontend, backend, web, scripts, tests, migrations, refactors, known-cause fixes, and defect-first code reviews. Web edits retain browser verification when available. Do not use for unknown-root-cause diagnosis only, requirements without implementation, current framework/version research, API documentation-only work, translation, or Git checkpoints.'
---
# High Constraint Coding

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Ownership and boundary

Own authorized implementation and source review in every programming language. Route unknown-root-cause diagnosis to `bug-diagnosis`, unclear implementation contracts to `requirement-analysis`, current technical choices to `technical-solution-research`, API documentation deliverables to `write-api-docs`, and explicit Git actions to `git-checkpoint-push`. Review-only work remains read-only.

Implementation authorization covers requested project changes and normal verification, not unrelated cleanup, dependency expansion, destructive data actions, commits, pushes, deployment, or external mutation. Ask when a missing choice materially changes behavior, interfaces, data, safety, or acceptance.

## Choose the path

Use the fast path only when evidence shows the change is truly trivial, local, and low risk: one obvious owner, no shared contract or lifecycle effect, no meaningful design choice, and a focused check can prove it. Read the affected code and test, make the smallest complete project-native edit, run that check, and fix then retest on failure.

Use the engineering path for everything else, including shared behavior, unfamiliar code, public contracts, state, persistence, errors, concurrency, resources, migrations, security boundaries, or multiple plausible seams.

## Engineering path

### 1. Orient

1. Identify the language and version, compiler or runtime, framework, build and package tools, formatter, linter, type checker, and project-native test commands from repository evidence.
2. Read repository rules and maintained analogous code in the same subsystem. Enforced tooling and local conventions outrank generic preferences.
3. Model current behavior through entry points, callers, inputs, data and state transitions, outputs, errors, concurrency, cancellation, resource lifetime, recovery, tests, and external consumers.
4. Name the invariants and compatibility that must remain true. If the cause, requirement, or current platform fact is unresolved, stop and hand off to diagnosis, requirements, or research.

### 2. Choose the design

1. Locate the layer that owns the behavior or invariant; do not patch a downstream symptom when evidence identifies a shared semantic seam.
2. Compare a small number of candidates only when a real tradeoff exists. Include keeping the current design or the smallest viable seam when credible; do not manufacture an options ceremony.
3. Select from project evidence, compatibility, failure behavior, operability, debuggability, cognitive load, and verification cost. Prefer understandable and maintainable code over shortest code or premature generality.
4. Record rejected options only when the distinction affects review, risk, or future maintenance.

### 3. Implement

- Use language- and ecosystem-native APIs, types, names, errors, ownership and resource patterns, async cancellation and timeouts, concurrency controls, transactions, and public interface conventions.
- Keep dependencies, boundaries, state transitions, failure behavior, and lifecycle ownership explicit. Keep the happy path visible and preserve authorized compatibility.
- Complete the requested behavior from caller through outcome and realistic recovery, while leaving unrelated legacy code alone.
- Avoid mechanically mirrored layers, pass-through wrappers, generic utility buckets, unreachable fallbacks, boolean soup, stringly typed states, catch-all handling, silent error swallowing, and test-only production branches.
- Do not use assertions, casts, non-null suppression, or warning suppression to conceal a modeling defect. Do not claim performance gains or optimize without relevant evidence.

### 4. Audit deliberate project work

Do not claim or imply human authorship. The target is code that reads as deliberate senior project work through observable engineering properties.

For each new field, state, branch, helper, layer, dependency, file, and test, identify its current requirement or consumer. Remove accidental duplication, template symmetry, excessive layering, unreachable defensive code, vague generalized names, homogenized helpers, and comments that compensate for avoidable complexity. Preserve reasonable local asymmetry when domain behavior or maintained project structure justifies it.

### 5. Test and verify

Prefer behavior and public-contract tests over internal call ordering. Cover relevant failure and recovery, and use test doubles only at meaningful boundaries rather than mocking the whole unit. Select project-native unit, property, contract, integration, browser, migration, or benchmark checks in proportion to risk. Verify the changed behavior and adjacent shared-contract risk. When a check exposes a defect introduced by the current change, or a defect whose repair is necessary to complete the user's explicit request, fix it and rerun until it passes or a concrete blocker prevents completion. Report pre-existing or adjacent defects without fixing them unless the user separately authorizes that work.

Never claim beyond evidence actually obtained. State failed or unavailable checks, unproven behavior, assumptions, and residual risk.

## Review mode

Return actionable findings before summary, ordered by severity. Evaluate correctness, compatibility, idioms, lifecycle and resource ownership, errors, concurrency, security boundaries, maintainability, regressions, and missing behavior coverage. Cite evidence, state explicitly when no findings exist, and do not edit unless separately authorized.

## Web verification branch

For webpage, frontend, UI, style, interaction, or browser-facing changes:

1. Check for and reuse a healthy relevant dev server; start the project-native server only when needed and permitted.
2. With browser tools available, navigate to the actual changed page, exercise the affected flow, and verify relevant desktop and mobile viewports.
3. Inspect console errors and relevant network requests for request-driven behavior.
4. Capture screenshot, DOM, or accessibility evidence when it materially proves output, semantics, layout, or state.
5. If server, browser, credentials, fixtures, or page are unavailable, report the exact blocker, run strongest available project-native checks, and name browser-visible behavior left unverified.
6. If verification exposes a defect introduced by the current change, or a defect whose repair is necessary to complete the user's explicit request, continue fixing and repeat the relevant checks. Report pre-existing or adjacent defects without fixing them unless separately authorized. A broken result within the authorized repair boundary is not complete because it was observed.

Non-browser code does not require browser verification unless its requested behavior is browser-visible.

## Final gate

Before handoff, confirm code health did not decline; the authorized scope is complete but focused; a maintainer can understand behavior, ownership, errors, and recovery; every artifact is justified; compatibility is intentional; and every completion claim has evidence. Report what changed, why the seam was correct, verification performed, assumptions, and residual risk.

## Reference index

- Read [language-and-ecosystem-profile.md](./references/language-and-ecosystem-profile.md) when identifying language, runtime, ecosystem, or toolchain obligations.
- Read [engineering-judgment.md](./references/engineering-judgment.md) for non-trivial orientation, seam choice, tradeoffs, compatibility, or escalation.
- Read [maintainability-audit.md](./references/maintainability-audit.md) before completing non-trivial implementation or review.
- Read [testing-strategy.md](./references/testing-strategy.md) when selecting coverage and verification evidence.
- Read [contract-coherence.md](./references/contract-coherence.md) when behavior crosses layers or shared invariants.
- Read [project-native-style.md](./references/project-native-style.md) when local conventions are unclear or inconsistent.
- Read [intentionality-audit.md](./references/intentionality-audit.md) for broad slices or numerous new artifacts.
- Read [verification-policy.md](./references/verification-policy.md) for risky, shared, migration, concurrency, or web verification.
- Read [quality-bar.md](./references/quality-bar.md) at the final gate for non-trivial work.