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

## 3. Feature Closure

- Every requested action is connected from caller to observable outcome and recovery behavior.
- Every new field, enum, status, index, route, endpoint, or UI state has a current requirement, producer, consumer, or lifecycle.
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
- Documentation and operational claims match what the code actually implements.

## 7. Intentionality

- Every introduced class, function, field, branch, abstraction, configuration entry, and dependency has a present reason and consumer.
- Defensive code protects a reachable boundary or alternate caller and is tested.
- No generic layer, pass-through helper, catch-and-rethrow wrapper, dormant status, or future hook exists only because a generator commonly emits it.
- No placeholder implementation, TODO-shaped behavior, or half-wired surface is presented as complete.

## 8. Clarity And Maintainability

- The code can be read without reconstructing hidden intent.
- The main behavior is visible without jumping through too many indirections.
- Naming helps the next engineer understand what each piece is for.
- The implementation is not shorter at the cost of becoming denser or more clever.
- A local future change can be made without reopening the entire design.

## 9. Performance Discipline

- The implementation is efficient enough for the real use case.
- Performance-sensitive choices are justified by evidence, constraints, or known hot paths.
- Readability has not been traded away for speculative optimization.

## 10. Verification

- There is direct evidence that the changed behavior works.
- Contract boundaries and at least one realistic failure or edge path are covered when applicable.
- There is reasonable evidence that nearby behavior did not regress.
- Any unverified area is called out explicitly.

## 11. Brevity With Clarity

- The code is no longer than needed for the problem.
- Repetition is reduced when reduction improves clarity.
- Concision never depends on dense syntax, hidden coupling, or magical helpers.

## 12. Honesty

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

If a patch fails one of these categories, tighten the implementation or lower the claim level in the response.
