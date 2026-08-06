# Quality Bar

Use this completion gate for non-trivial source review or code changes.

- [ ] The result matches requested behavior without unrelated changes.
- [ ] Language, ecosystem, version, toolchain, repository rules, and maintained local conventions are known.
- [ ] Relevant callers, inputs, state, errors, persistence, outputs, consumers, and contracts use coherent semantics.
- [ ] The change uses the correct owning seam; alternatives are compared only when a real tradeoff exists.
- [ ] Every new field, state, index, endpoint, abstraction, dependency, and file has a current requirement or consumer.
- [ ] Errors, resources, concurrency, cancellation, lifecycle, and realistic recovery are correct where relevant.
- [ ] Naming, control flow, boundaries, and decomposition minimize cognitive load and remain maintainable and debuggable.
- [ ] Public compatibility, migrations, documentation, and operational claims match the implementation.
- [ ] The implementation stays direct and readable; performance complexity is evidence-based.
- [ ] Behavior-focused tests prove success, failure, and recovery without binding to implementation details; adjacent risk is checked where practical.
- [ ] Unverified behavior, assumptions, and residual risk are reported precisely.
- [ ] Engineering evidence is not used to claim human or AI authorship.

If any item fails, tighten the implementation, strengthen verification, or narrow the completion claim.