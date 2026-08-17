# Quality Bar

Use this checklist for every repository implementation or review governed by this skill.

Classify every gate as:

- `pass`
- `fail`
- `not applicable`
- `unverified`

Do not infer `pass` from silence. Record the evidence for each applicable gate.

## Requested Result

- The requested behavior or review deliverable is complete.
- The observable result matches the requirement.
- No unrelated behavior was intentionally changed.

## Scope

- The diff is limited to the required behavior, contracts, and tests.
- Unrelated refactors, renames, formatting churn, generated artifacts, and dependency changes are absent.
- Every introduced file, field, branch, abstraction, configuration entry, and dependency has a current requirement or consumer.

## Contract Coherence

- Every touched invariant has one authoritative owner.
- Validation, normalization, defaults, nullability, state transitions, persistence, outputs, and consumers agree.
- Public and persisted compatibility is preserved or the requested compatibility change is explicit.
- Selected dependency or protocol reference gates have been classified and satisfied.

## Project-Native Shape

- The implementation follows analogous maintained code and enforced tooling.
- Naming, control flow, errors, dependencies, and tests use one coherent local convention.
- No generic layer, pass-through helper, dormant state, or speculative extension point was introduced.
- The code remains direct enough for a contributor to locate and trace.

## Feature Closure

- Each requested action reaches an observable outcome and applicable recovery path.
- New state and side effects have a complete lifecycle.
- No placeholder, unreachable fallback, TODO-shaped behavior, or half-wired surface is presented as complete.
- Documentation and completion claims describe only implemented behavior.

## Verification

- Direct evidence covers the changed behavior or review finding.
- At least one realistic failure, edge, or recovery path is covered when applicable.
- Shared behavior has an adjacent regression check when practical.
- Tests were not deleted, skipped, or weakened to manufacture success.
- Build, typecheck, lint, static analysis, or supported configuration checks ran when material.

## Final Status

Choose the status mechanically:

- `Completed`: every applicable gate is `pass`.
- `Implemented but unverified`: no applicable gate is `fail`, and at least one required gate is `unverified` because of an explicit limitation.
- `Blocked`: any applicable gate is `fail`, or a material requirement or contract cannot be established safely.

Any applicable `fail` forbids a completion claim. Any applicable `unverified` forbids `Completed`.
