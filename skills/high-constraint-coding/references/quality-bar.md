# Quality Bar

Use this completion gate for non-trivial source review or code changes.

- [ ] The result matches requested behavior without unrelated changes.
- [ ] Relevant callers, inputs, validation, defaults, state, persistence, outputs, consumers, and tests use coherent semantics.
- [ ] Each invariant has an explainable owner; defensive behavior protects a reachable boundary.
- [ ] Every new field, state, index, endpoint, abstraction, dependency, and file has a current requirement or consumer.
- [ ] The requested slice is complete, including realistic failure or recovery behavior, without speculative adjacent features.
- [ ] Naming, wiring, control flow, errors, mapping, transactions, pagination, and tests follow one evidence-backed repository convention.
- [ ] Public compatibility, migrations, documentation, and operational claims match the implementation.
- [ ] The implementation stays direct and readable; performance complexity is evidence-based.
- [ ] Targeted verification proves the changed behavior and checks adjacent regression risk where practical.
- [ ] Unverified behavior, assumptions, and residual risk are reported precisely.
- [ ] Engineering evidence is not used to claim human or AI authorship.

If any item fails, tighten the implementation, strengthen verification, or narrow the completion claim.