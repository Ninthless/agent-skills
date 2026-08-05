---
name: high-constraint-coding
description: 'Implement or review correctness-sensitive source changes with controlled scope, project-native style, coherent contracts, intentional artifacts, and proportionate verification. Use for explicit bug fixes with a known root cause, refactors, production edits, migrations, tests, vertical feature slices, and defect-first source reviews. Do not own unknown-root-cause diagnose-only work, requirement contracts, technical solution research, API documentation-only deliverables, or Git checkpoints.'
---
# High Constraint Coding

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Ownership

Own source implementation and source review. Route unknown-root-cause diagnosis to `bug-diagnosis`, unclear requirement contracts to `requirement-analysis`, current technical choices to `technical-solution-research`, API documentation deliverables to `write-api-docs`, and explicit Git actions to `git-checkpoint-push`.

## Fast path

For a small clear change:

1. Read the affected path and nearby tests.
2. State the concrete behavior to change or preserve internally.
3. Make the smallest complete project-native change.
4. Run the strongest targeted check available.
5. Report outcome, evidence, and residual risk.

## Authorization

Implementation authorization permits only the requested project changes and normal verification. It does not authorize unrelated cleanup, dependency expansion, destructive data actions, commits, pushes, deployment, or external mutation. Ask when a missing choice materially changes behavior, interfaces, data, safety, or acceptance.

## Change workflow

1. Trace entry points, callers, contracts, state, outputs, consumers, and tests that define the affected slice.
2. Identify authoritative validation, defaulting, normalization, nullability, and lifecycle boundaries.
3. Learn maintained local conventions from analogous code.
4. Choose the narrowest solution that closes the requested behavior path.
5. Keep every field, branch, abstraction, file, and dependency tied to a current requirement or real consumer.
6. Preserve public contracts unless changing them is required and authorized.
7. Remove artifacts made obsolete by the change without cleaning unrelated legacy code.
8. Verify the changed behavior and at least one adjacent shared-contract path when practical.

Do not patch a downstream symptom when evidence identifies a shared semantic seam. Do not continue speculative patching when the root cause remains unknown; return to diagnosis.

## Implementation constraints

- Do not mix the requested change with opportunistic cleanup.
- Do not add speculative layers, flags, states, or dependencies.
- Do not make sibling paths disagree on validation, defaults, or lifecycle.
- Do not compress control flow when it hides behavior or ownership.
- Do not preserve artifacts made unreachable by the new behavior.

## Review mode

Return actionable findings before summary. Prioritize correctness, regressions, unsafe assumptions, contract contradictions, missing validation, state or mutation hazards, and coverage gaps. Cite evidence and state explicitly when no findings are found. Review is read-only unless edits are separately requested.

## Verification

Prefer targeted behavior tests, then integration checks, nearby regressions, type or build checks, lint or static analysis, and a documented manual reproduction. Never claim success beyond the checks actually run. State what remains unproven when tooling, access, or fixtures are unavailable.

## Reference index

- Read [contract-coherence.md](./references/contract-coherence.md) when behavior crosses validation, service, storage, transport, UI, or tests.
- Read [project-native-style.md](./references/project-native-style.md) before adding a non-trivial implementation shape or when repository conventions conflict.
- Read [intentionality-audit.md](./references/intentionality-audit.md) for new schemas, states, abstractions, dependencies, or broad slices.
- Read [verification-policy.md](./references/verification-policy.md) when risk, shared behavior, migration, concurrency, or unavailable checks complicate verification.
- Read [quality-bar.md](./references/quality-bar.md) before completing a non-trivial change or review.

## Final handoff

Report what changed, why the selected seam was correct, verification performed, assumptions, and residual risks. If diagnosis, requirements, or technical evidence remains unresolved, name the next owner instead of presenting partial implementation as complete.
