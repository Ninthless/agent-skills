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

## Architecture And Maintainability

Apply this section to bounded behavioral and architectural work. Mark it `not applicable` only for a genuinely mechanical edit with no behavior, contract, state, dependency, or ownership decision.

- Each changed business rule and authoritative state has one discoverable owner.
- The primary and realistic failure paths can be traced from entry to outcome without hidden control flow or ambient mutable state.
- Cross-boundary inputs, outputs, errors, ownership, and optionality use an explicit repository-native contract.
- Callers depend on stable public behavior rather than another owner's private representation, positional protocol, or incidental storage shape.
- Dependency direction remains intentional, and no new cycle or boundary bypass was introduced.
- Independently changing policy, external integration, state transition, persistence, and presentation concerns are not combined without a demonstrated reason.
- Every new boundary, abstraction, named type, or module has a current caller, change reason, lifecycle need, or testing seam.
- A behavior-preserving refactor keeps behavioral assertions stable instead of rewriting tests to mirror the new structure.
- A simulated likely follow-up change is `local` or `coordinated but coherent`, not `scattered`.

Do not infer a pass from smaller files, more types, added layers, lower complexity metrics, higher coverage, or successful tests alone.

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
- Stateful, persistent, asynchronous, retrying, concurrent, or resource-owning changes have lifecycle and round-trip evidence proportional to risk.
- Architectural work includes evidence that allowed dependencies, public contracts, and affected callers remain coherent.

## Final Status

Choose the status mechanically:

- `Completed`: every applicable gate is `pass`.
- `Implemented but unverified`: no applicable gate is `fail`, and at least one required gate is `unverified` because of an explicit limitation.
- `Blocked`: any applicable gate is `fail`, or a material requirement or contract cannot be established safely.

Any applicable `fail` forbids a completion claim. Any applicable `unverified` forbids `Completed`.
