---
name: high-constraint-coding
description: 'Mandatory coding-quality and maintainable-architecture companion whenever the agent will generate, write, create, implement, edit, modify, patch, refactor, convert, format, scaffold, regenerate, or otherwise output code or a code-like artifact. Always trigger before producing or changing source, snippets, scripts, commands, queries, regex, configs, schemas, migrations, tests, fixtures, generated code, build files, CI workflows, API definitions, pseudocode, examples, or proposed patches, whether in a repository or only in chat and whether trivial, throwaway, hypothetical, or production. Compose with specialized UI, API, security, platform, or documentation skills. Preserve contracts and ownership, make the smallest maintainable result, and verify proportionately. Do not trigger for explanation, planning, inspection, diagnosis, status, or review when no code-like output will be produced or modified.'
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

## Mandatory Code-Producing Companion

Use this skill whenever the response or task will produce or modify code or a code-like artifact, regardless of size, language, risk, destination, or whether another specialized skill is also active. Activate it before the first code is generated, proposed, patched, or edited.

This includes:

- source, scripts, snippets, commands, queries, regular expressions, tests, fixtures, configs, schemas, migrations, workflows, build files, generated code, and API definitions
- implementation, bug fixing with a code change, refactoring, conversion, formatting, cleanup, scaffolding, regeneration, and exact mechanical edits
- proposed code, pseudocode, example code, patches, replacement blocks, and code shown only in chat
- throwaway, demo, prototype, one-file, isolated, syntax-only, hypothetical, and production code

Do not activate for read-only explanation, planning, exploration, diagnosis, status, or review unless the response will include proposed code or the task later transitions into modifying an artifact. If that transition occurs, activate this skill before producing the code.

Keep the process proportionate: use focused checks for a one-line snippet or mechanical edit and the full contract and lifecycle workflow for risky implementation. Never turn mandatory triggering into mandatory ceremony. When a specialized skill owns the deliverable, compose with it rather than replacing it. The specialized skill governs its artifact-specific requirements; this skill governs bounded changes, clear code, project fit, maintainability, and honest verification.

## 1. Select the delivery mode and depth

Choose one mode before proceeding:

- **Implementation:** inspect, edit, verify, audit the diff, and apply the completion gate.
- **Review:** inspect the diff and affected behavior path, report actionable findings first, and do not edit unless asked.
- **Diagnosis-only:** reproduce or trace the failure, establish the cause, and report evidence without implementing a fix.

If the request changes mode, follow the latest request. Do not turn a review or diagnosis into an implementation without authorization.

For implementation and review with proposed code, choose the lightest sufficient depth:

- **Mechanical:** an exact local edit with no behavioral, contract, state, dependency, or ownership decision. Read the target and immediate context, make the edit, and run a focused check.
- **Bounded behavioral:** one coherent behavior changes within known owners and contracts. Map the affected vertical slice and verify its normal and realistic failure paths.
- **Architectural:** the change creates or moves ownership, crosses independently changing responsibilities, introduces a module or dependency direction, or materially affects shared state, persistence, concurrency, protocols, or multiple consumers. Establish the architecture model and staged change before editing.

Escalate depth when evidence reveals broader coupling. Do not classify by line count or file count. Do not force mechanical work through an architecture ceremony, and do not disguise an architectural decision as a local patch.

Treat hand-written source-file length as a maintainability signal:

- target at most 300 effective lines when creating a file
- review ownership and independent change reasons above 500 lines
- require a justified exception or coherent split above 800 lines
- reject growth beyond 1000 lines by default

Count code consistently with repository tooling and normally ignore blank lines. Exempt generated, vendored, snapshot, static-data, and framework-mandated files when their shape is authoritative. Never split merely to satisfy a threshold; a split must create a real owner, change boundary, lifecycle boundary, or testing seam rather than pass-through files or navigation-only helpers. Read [human-maintainability.md](./references/human-maintainability.md) when a touched file crosses a threshold or file decomposition is part of the decision.

## 2. Route references

Read only the references whose signals are present:

- Read [quality-bar.md](./references/quality-bar.md) for every repository implementation or review.
- Read [human-maintainability.md](./references/human-maintainability.md) for bounded behavioral and architectural work, or whenever ownership, discoverability, abstraction shape, change propagation, or the next realistic hand edit is part of the decision.
- Read [project-structure.md](./references/project-structure.md) when creating, moving, or materially changing packages, modules, directories, workspaces, services, shared code, cross-module dependencies, data ownership, visibility, or test placement.
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

Split broad work into the smallest independently reviewable and verifiable slices. Prefer behavior-protecting tests before structure-changing refactors when current behavior lacks reliable coverage. Keep feature work and unrelated cleanup separate.

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

For bounded behavioral and architectural work, also establish:

- the authoritative owner of each changed rule and state
- the public, persisted, or cross-module contracts that expose it
- the dependency direction and any boundary currently bypassed
- the decisions likely to change independently
- the expected location of the next realistic maintenance change
- the smallest project-native module or directory that should own the change

Choose one authoritative owner for each invariant. Do not preserve contradictory validation or defaults across layers.

## 5. Choose the narrowest complete solution

Prefer:

- an existing path over a new layer
- direct control flow over clever compression
- one clear owner over scattered helpers
- stable public contracts over broad rewrites
- language and repository idioms over generic architecture
- observable behavioral tests over private-call assertions
- named cross-boundary data over positional or shape-dependent protocols
- boundaries around independently changing policy, state, side effects, or external integrations
- top-level organization by business capability, stable responsibility, or ecosystem-native module when the domain has meaningful boundaries
- feature-internal technical subdivision only when complexity, visibility, lifecycle, dependency, or testing evidence requires it
- compiler, build, package, project-reference, lint, or architecture-test enforcement for important dependency boundaries

Reject:

- speculative frameworks, extension points, generic utilities, or future states
- template-symmetric layers, CRUD surfaces, fields, indexes, or configuration with no current consumer
- pass-through wrappers, catch-and-rethrow helpers, and navigation-only decomposition
- unrelated renames, formatting churn, cleanup, or dependency upgrades
- plausible API calls unsupported by the repository's actual version and integration
- magic indexes, undocumented tuple or array protocols, and loosely shaped cross-function results whose fields have independent meaning
- silent broad exception handling, hidden mutable globals, and duplicate business rules
- functions or modules that combine independently changing request construction, parsing, policy, state transition, persistence, and presentation without a demonstrated reason
- architecture chosen from a fashionable name, symmetric template, file-size target, or generic layer count
- new hand-written files above 300 effective lines without checking whether independent responsibilities were combined
- adding responsibilities to hand-written files above 500 lines without a documented ownership review
- hand-written files above 800 lines without a coherent single-owner justification or evidence-based decomposition
- hand-written files above 1000 lines unless an explicit repository constraint makes a smaller maintainable shape worse
- global technical-layer buckets that force every business change across unrelated controllers, services, repositories, models, or handlers
- cross-module access to private implementation types, mutable state, tables, persistence models, or provider SDKs
- shared `utils`, `common`, `helpers`, `base`, `manager`, or `processor` areas with no narrow owner and dependency policy
- fixed symmetric directory templates, empty layers, one-file directories, or one-implementation interfaces without a current boundary need
- module or service splits based only on team names, file size, architectural fashion, or hypothetical future extraction

A local-looking patch is not narrow if it leaves sibling paths inconsistent. A short implementation is not minimal if it hides behavior or omits a required failure path.

When maintainability is material, name the expected maintenance path:

`A future change to [behavior] should primarily modify [owner] and its [contract/tests].`

Strengthen an existing boundary before adding one. Add a boundary only when it localizes a demonstrated change reason, state owner, side effect, external dependency, or testing seam for current behavior. Do not split code into navigation-only helpers or layers.

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
- make cross-boundary inputs, results, errors, and ownership explicit when callers otherwise depend on position, mutation, ambient state, or undocumented shape
- keep dependency flow toward stable contracts and prevent callers from reaching into another owner's private representation
- separate independently changing responsibilities only as far as the current slice and verification evidence justify
- keep each module's public contract smaller than its internal implementation surface
- keep mutable data, migrations, and state transitions with one authoritative module owner
- preserve ecosystem-native source, package, workspace, test, migration, and generated-file locations

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

For bounded behavioral and architectural work, perform an architecture health audit:

- each changed rule and state has one discoverable authoritative owner
- the primary and failure paths remain traceable without reconstructing hidden control flow
- cross-boundary dependencies use explicit contracts rather than private data, magic positions, or ambient state
- no new dependency cycle, scattered duplicate policy, or unrelated synchronized edit was introduced
- tests protect observable behavior and contracts rather than the new internal layout
- new or changed modules have explicit owners, callers, public contracts, hidden decisions, allowed dependencies, data ownership, and focused verification
- common changes remain local or coordinated through a small set of explicit contracts rather than global technical buckets or shared mutable storage

Simulate one likely follow-up change without implementing it. Identify where a maintainer would start, which owners and contracts would change, and which tests would catch a regression. If the change would require repository-wide discovery or coordinated edits across unrelated owners, improve the boundary or classify maintainability as failed or unverified.

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
