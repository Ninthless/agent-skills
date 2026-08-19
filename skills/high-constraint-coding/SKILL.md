---
name: high-constraint-coding
description: 'Use this skill for every task that writes, edits, reviews, refactors, generates, converts, formats, tests, or otherwise produces code or code-like artifacts in any language, including source files, scripts, queries, configs, schemas, migrations, tests, snippets, and CI. Apply it as the universal coding-quality companion: read the real context, make the smallest complete project-native result, preserve contracts, keep code hand-maintainable, and verify what is claimed. Also trigger for production fixes, APIs, persistence, dependencies, async work, protocols, concurrency, transactions, ABI/FFI, build compatibility, 最小改动, 最少代码实现, 高质量代码, 便于手写维护, 不要 AI 味, 别乱重构, 先看清楚再改, or 保证正确. Use alongside a specialized UI, API-documentation, security, or platform skill when that skill owns the artifact; do not use for prose-only discussion, status-only requests, or non-code planning.'
---

# High Constraint Coding

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Purpose

Produce the smallest complete repository-native result that satisfies the request and survives proportionate verification. Optimize in this order:

1. correctness
2. contract and lifecycle coherence
3. human hand-maintainability
4. project-native consistency
5. verification strength
6. brevity

Do not infer authorship from code style. Treat "human-written" as code whose behavior, ownership, dependencies, and tests are easy for a contributor to locate, trace, change, and verify.

## Universal Coding Companion

Use this skill whenever the task includes code or a code-like artifact, regardless of size, language, risk, or whether another specialized skill is also active. This includes:

- source, scripts, snippets, queries, regular expressions, tests, fixtures, configs, schemas, migrations, workflows, build files, and generated code
- implementation, bug fixing, review, diagnosis with code output, refactoring, conversion, formatting, cleanup, scaffolding, and exact mechanical edits
- throwaway, demo, prototype, one-file, isolated, and syntax-only code tasks

Keep the process proportionate: use the full contract and lifecycle workflow for risky work, and compress it for trivial work without dropping the code-quality companion role. When a specialized skill owns the deliverable, compose with it rather than replacing it. The specialized skill governs its artifact-specific requirements; this skill governs bounded changes, clear code, project fit, and honest verification.

## 1. Select the delivery mode

Choose one mode before proceeding:

- **Implementation:** inspect, edit, verify, audit the diff, and apply the completion gate.
- **Review:** inspect the diff and affected behavior path, report actionable findings first, and do not edit unless asked.
- **Diagnosis-only:** reproduce or trace the failure, establish the cause, and report evidence without implementing a fix.

If the request changes mode, follow the latest request. Do not turn a review or diagnosis into an implementation without authorization.

## 2. Route references

Read only the references whose signals are present:

- Read [quality-bar.md](./references/quality-bar.md) for every repository implementation or review.
- Read [human-maintainability.md](./references/human-maintainability.md) when ownership, discoverability, abstraction shape, change propagation, or the next realistic hand edit is part of the decision.
- Read [dependency-contracts.md](./references/dependency-contracts.md) when correctness depends on an installed version, configuration, registration, generated artifact, serializer, framework state model, persistence round trip, or external async capability.
- Read [protocol-boundaries.md](./references/protocol-boundaries.md) for ordered protocols, ownership transfer, ABI/FFI, concurrency, reentrancy, transactions, retries, idempotency, partial commits, teardown, or supported build matrices.
- Read both dependency and protocol references when an external capability also owns ordering, lifetime, transaction, retry, concurrency, or teardown semantics.

For each selected reference, classify its named checks as `pass`, `fail`, `not applicable`, or `unverified`. Only applicable checks are mandatory, but no applicable failed or unverified check may be silently treated as passed.

## 3. Bound the task

Identify:

- the exact behavior to add, fix, preserve, diagnose, or review
- the likely entry point, owners, callers, state, outputs, and tests
- the public, persisted, generated, or operational contracts that may change
- the strongest practical validation target
- assumptions that could materially change the solution

Ask one concise question when competing interpretations would produce materially different behavior. Mark pre-existing gaps as `in scope`, `out of scope`, or `blocking`.

## 4. Read before deciding

Inspect the real implementation path before proposing code or review conclusions:

- read the actual files, callers, types, schemas, configuration, and focused tests
- inspect analogous maintained modules to identify project conventions
- inspect manifests, lockfiles, registrations, adapters, generated artifacts, and runtime paths when dependency behavior matters
- inspect relevant history only when it explains an invariant or convention

Before editing, be able to state in one sentence what the current code does in the affected area. If that sentence is uncertain, keep reading.

For a non-trivial slice, map:

- entry and caller
- validation, normalization, defaults, and null semantics
- policy and state transitions
- persistence, serialization, events, output, and downstream observation
- failure, recovery, cancellation, retry, and teardown where applicable
- behavioral tests and supported build environments

Choose one authoritative owner for each invariant. Do not preserve contradictory validation or defaults across layers.

## 5. Choose the narrowest complete solution

Prefer:

- an existing path over a new layer
- direct control flow over clever compression
- one clear owner over scattered helpers
- stable public contracts over broad rewrites
- language and repository idioms over generic architecture
- observable behavioral tests over private-call assertions

Reject:

- speculative frameworks, extension points, generic utilities, or future states
- template-symmetric layers, CRUD surfaces, fields, indexes, or configuration with no current consumer
- pass-through wrappers, catch-and-rethrow helpers, and navigation-only decomposition
- unrelated renames, formatting churn, cleanup, or dependency upgrades
- plausible API calls unsupported by the repository's actual version and integration

A local-looking patch is not narrow if it leaves sibling paths inconsistent. A short implementation is not minimal if it hides behavior or omits a required failure path.

When maintainability is material, name the expected maintenance path:

`A future change to [behavior] should primarily modify [owner] and its [contract/tests].`

## 6. Implement the bounded slice

While editing:

- change only what the requested behavior requires
- keep validation, state, persistence, outputs, and consumers coherent
- remove artifacts made obsolete by this change
- preserve compatible interfaces unless the request requires a contract change
- keep error, resource, async, transaction, and teardown behavior explicit
- make every new artifact answer: why now, who consumes it, and what evidence supports it
- do not replace authoritative state transitions with rendered changes or manual success notifications
- do not claim adjacent unimplemented behavior

If two attempted fixes fail, stop patching. Re-establish the cause from runtime or repository evidence and choose a materially different approach.

## 7. Verify the result

Run the strongest practical checks in this order as applicable:

1. targeted behavior and contract tests
2. exact-version dependency probes or round-trip tests
3. protocol, transaction, retry, concurrency, failure, and teardown tests
4. integration or end-to-end checks for changed vertical slices
5. adjacent regression tests for shared seams
6. typecheck, build, lint, static analysis, and supported configuration checks
7. manual reproduction only when automation is unavailable

Do not stop at a symptom test when shared behavior changed. Distinguish:

- tests that passed
- tests that failed because of the change
- known baseline failures
- checks not run and why

Audit the final diff:

- no unrelated files or generated artifacts
- no new dependency without a demonstrated requirement
- no deleted or weakened test used to make the change pass
- no placeholder, unreachable fallback, dormant state, or half-wired surface introduced by the change

## 8. Apply the completion gate

Use exactly one final status:

### Completed

Use only when:

- the requested implementation or review deliverable is complete
- every applicable required check is `pass`
- direct evidence proves the changed behavior or review conclusion
- no relevant regression introduced by the change is known

### Implemented but unverified

Use only when:

- the requested code change is present
- a required check is `unverified` because of an explicit environment, access, tool, or time limitation
- no applicable check is known to have failed

Do not say `fixed`, `verified`, `done`, or equivalent. List the missing checks and the claims they leave unproven.

### Blocked

Use when:

- a material requirement or contract cannot be determined safely
- a required dependency capability is unsupported or unproven and no repository-supported path exists
- an applicable required check fails and cannot be corrected within scope
- completing the slice would require unauthorized scope, access, or destructive action

Do not ship a guessed or half-connected implementation as completion.

Any applicable `fail` forbids `Completed` and `Implemented but unverified`. Any applicable `unverified` forbids `Completed`.

## 9. Review mode

Report findings before summary:

1. correctness and security defects
2. contract, lifecycle, persistence, protocol, and compatibility regressions
3. missing or misleading tests and completion claims
4. maintainability risks caused by scattered ownership, hidden behavior, or needless complexity

Include file and line evidence when available. Distinguish confirmed defects from risks and questions. State explicitly when no findings are found and identify the review coverage and limits.

## 10. Report concisely

Report:

- final status
- what changed, diagnosed, or found
- verification evidence
- assumptions, residual risks, or blockers

Do not claim more than the evidence proves.
