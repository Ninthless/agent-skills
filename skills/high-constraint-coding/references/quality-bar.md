# Quality Bar

Use this checklist when deciding whether a code change is actually high quality.

## 1. Correctness

- The change matches the requested behavior.
- Edge cases introduced by the change have been considered.
- The implementation does not quietly change unrelated behavior.
- Claims of correctness are backed by actual evidence.

## 2. Contract Coherence

- Entry points, input contracts, validation, defaulting, domain logic, persistence, outputs, external consumers, and tests agree on the same semantics.
- Each invariant has one authoritative boundary rather than duplicated or contradictory enforcement.
- A downstream fallback is reachable through a real caller; otherwise it is absent.
- Nullability, normalization, defaults, error mapping, and state transitions remain consistent across the slice.
- Dependency capability claims match the installed version, configuration, registration, generated artifacts, or focused runtime evidence.
- API existence, successful invocation, authoritative state change, round-trip survival, and downstream observation are proven separately when the feature relies on each.
- Multi-call protocols preserve valid ordering, negotiated caller constraints, cross-call state, legal outputs, terminal states, and reset behavior.
- Boundary parameters have proven direction, nullability, ownership, lifetime, mutability, and failure semantics.

## 3. Feature Closure

- Every requested action is connected from caller to observable outcome and recovery behavior.
- Every new field, enum, status, index, route, endpoint, or UI state has a current requirement, producer, consumer, or lifecycle.
- Required data survives serialization, persistence, reload, reconstruction, retry, undo, or transport as applicable.
- Stateful and asynchronous work has explicit ownership, completion, failure, cancellation, stale-completion, and teardown behavior.
- Partial success, commit, rollback, retry, ambiguous success, duplicate delivery, and idempotency semantics are explicit where applicable.
- ABI or FFI boundaries contain unsupported language-level failures and preserve required cleanup and error categories.
- New behavior has the strongest proportionate test supported by the repository.
- Unrequested adjacent features are not generated merely to complete a template or CRUD matrix.
- Pre-existing gaps are reported rather than silently expanded into scope.

## 4. Scope Control

- The diff is limited to the task.
- Unrelated refactors, formatting churn, and renames are absent.
- New abstractions exist only if the task truly needs them.
- The implementation is the smallest complete slice, not the smallest file edit or the largest apparently complete scaffold.

## 5. Project-Native Consistency

- The change follows conventions from analogous maintained modules, enforced tooling, or documented architecture.
- Naming, dependency wiring, mapping, validation, error handling, pagination, concurrency, transactions, and tests are coherent across all new files.
- Existing inconsistency is not copied indiscriminately or used as permission to mix styles within the new slice.
- Relevant history is used only to understand intent, never manufactured to simulate human authorship.

## 6. Integration

- Interfaces, data contracts, and persistence behavior remain coherent.
- Adjacent tests, types, or callers are updated when required.
- Database and API changes include compatible migrations or versioning when required.
- Framework, protocol, serializer, driver, plugin, and generated-client behavior is verified against the repository's actual integration.
- Concurrency and callback behavior accounts for ordering, memory visibility, reentrancy, duplicate delivery, cancellation races, and teardown.
- Relevant build modes, feature combinations, toolchains, architectures, and platforms do not rely on accidental transitive dependencies or initialization order.
- Documentation and operational claims match what the code actually implements.

## 7. Intentionality

- Every introduced class, function, field, branch, abstraction, configuration entry, and dependency has a present reason and consumer.
- Defensive code protects a reachable boundary or alternate caller and is tested.
- No generic layer, pass-through helper, catch-and-rethrow wrapper, dormant status, or future hook exists only because a generator commonly emits it.
- No placeholder implementation, TODO-shaped behavior, or half-wired surface is presented as complete.

## 8. Clarity And Maintainability

- A project contributor can locate the behavior through repository and domain vocabulary.
- The main and failure paths can be traced without reconstructing hidden control flow or framework behavior.
- Each policy, state transition, side effect, and external contract has one clear owner.
- The implementation avoids navigation-only helpers, pass-through layers, and generic ownership buckets.
- A realistic follow-up change is local to one coherent area and its explicit contracts.
- Naming helps the next engineer understand what each piece owns and why it exists.
- The implementation is not shorter at the cost of becoming denser, more implicit, or more clever.
- Tests protect observable behavior and normally survive behavior-preserving refactoring.

## 9. Architecture For Hand Maintenance

- Boundaries follow responsibilities and decisions that change for different reasons, not framework templates.
- Volatile choices are hidden behind the smallest stable interface required by real callers.
- Dependency direction and side effects are explicit and follow project and language conventions.
- Common changes do not require synchronized edits across unrelated modules.
- New layers, services, factories, repositories, events, plugins, containers, or adapters have a current deployment, ownership, variation, integration, or testing reason.
- The design uses language-specific safety and idioms without imposing one cross-language architecture.
- Structural metrics are used as investigation signals, not proof that the architecture is maintainable.

## 10. Performance Discipline

- The implementation is efficient enough for the real use case.
- Performance-sensitive choices are justified by evidence, constraints, or known hot paths.
- Readability has not been traded away for speculative optimization.

## 11. Verification

- There is direct evidence that the changed behavior works.
- Contract boundaries and at least one realistic failure or edge path are covered when applicable.
- Version-sensitive, extension-sensitive, serialization-sensitive, or lifecycle-sensitive dependency behavior has a focused contract test or runtime probe.
- Multi-call behavior is tested as a protocol sequence, including invalid order, repetition, reset, and caller-constrained outputs where applicable.
- Boundary failures, partial commits, retries, reentrancy, concurrency races, and supported build configurations receive proportionate checks.
- The required write-to-read or state-to-observation round trip is verified.
- There is reasonable evidence that nearby behavior did not regress.
- Any unverified area is called out explicitly.

## 12. Brevity With Clarity

- The code is no longer than needed for the problem.
- Repetition is reduced when reduction improves clarity.
- Concision never depends on dense syntax, hidden coupling, or magical helpers.

## 13. Honesty

- Claims match the evidence.
- Assumptions are stated, not hidden.
- Unknowns are surfaced clearly instead of hand-waved away.
- Code quality observations are not presented as proof of human or AI authorship.
- Public-code search is treated as duplication evidence only, never proof that AI was or was not used.

## Project-Native Coherence Gate

Before completion, answer all of these with evidence:

1. Can each new artifact be traced to a requirement, real caller, project convention, or measurement?
2. Do validation, defaults, stored state, returned state, and UI behavior tell one consistent story?
3. Does the requested behavior form a complete, tested slice without speculative adjacent features?
4. Are all new files internally consistent with one evidence-backed project convention?
5. Are documentation, architecture, and completion claims no broader than the working implementation?
6. Can a maintainer locate the behavior, name its owner, trace its paths, and predict the affected contracts?
7. Does one realistic follow-up change remain local without unrelated synchronized edits or broad test rewrites?
8. Are non-trivial dependency capabilities and lifecycle semantics supported by the repository's actual version, configuration, and runtime path?
9. Does the authoritative state survive every round trip and async terminal state the feature promises?
10. Do protocol order, parameter direction, ownership, ABI or FFI error containment, concurrency, and retry semantics match the real boundary contract?
11. Does the change remain correct in the relevant supported build modes and platforms without accidental dependency or initialization assumptions?

If a patch fails one of these categories, tighten the implementation or lower the claim level in the response.
