# Quality Bar

Use this checklist when deciding whether a code change is actually high quality.

## 1. Correctness

- The change matches the requested behavior.
- Edge cases introduced by the change have been considered.
- The implementation does not quietly change unrelated behavior.
- Claims of correctness are backed by actual evidence.

## 2. Scope Control

- The diff is limited to the task.
- Unrelated refactors, formatting churn, and renames are absent.
- New abstractions exist only if the task truly needs them.

## 3. Integration

- The change follows existing project patterns where those patterns are still valid.
- Interfaces, data contracts, and persistence behavior remain coherent.
- Adjacent tests, types, or callers are updated when required.

## 4. Clarity And Maintainability

- The code can be read without reconstructing hidden intent.
- The main behavior is visible without jumping through too many indirections.
- Naming helps the next engineer understand what each piece is for.
- The implementation is not shorter at the cost of becoming denser or more clever.
- A local future change can be made without reopening the entire design.

## 5. Performance Discipline

- The implementation is efficient enough for the real use case.
- Performance-sensitive choices are justified by evidence, constraints, or known hot paths.
- Readability has not been traded away for speculative optimization.

## 6. Verification

- There is direct evidence that the changed behavior works.
- There is reasonable evidence that nearby behavior did not regress.
- Any unverified area is called out explicitly.

## 7. Brevity With Clarity

- The code is no longer than needed for the problem.
- Repetition is reduced when reduction improves clarity.
- Concision never depends on dense syntax, hidden coupling, or magical helpers.

## 8. Honesty

- Claims match the evidence.
- Assumptions are stated, not hidden.
- Unknowns are surfaced clearly instead of hand-waved away.

If a patch fails one of these categories, tighten the implementation or lower the claim level in the response.
