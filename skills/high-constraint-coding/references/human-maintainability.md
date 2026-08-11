# Human Hand-Maintainability

Use this reference when a task changes architecture, module boundaries, shared code, or a feature that humans will extend repeatedly.

## Contents

- Working Definition
- Language-Independent Model
- Architecture Decision Rule
- Human Change Simulation
- Metrics Boundary
- Cross-Language Adaptation
- Evidence Base

## Working Definition

Treat code as hand-maintainable when a competent project contributor can:

1. locate the owner of a behavior
2. trace the normal and failure paths without reconstructing hidden control flow
3. predict the impact of a change from explicit contracts and dependencies
4. make a common change in a small, coherent area
5. verify the result through stable behavioral checks

Do not reduce maintainability to short files, low metric scores, many abstractions, or a named architecture.

## Language-Independent Model

### Locate

- Keep each business rule, state transition, or integration policy under one identifiable owner.
- Name files, modules, functions, types, and tests with repository and domain vocabulary.
- Avoid generic buckets such as `utils`, `common`, `helpers`, `base`, `manager`, or `processor` when a more specific owner exists.
- Keep related behavior and its focused tests close according to repository convention.

### Trace

- Keep the primary path visible from entry point to outcome.
- Prefer explicit inputs, outputs, state transitions, and error propagation.
- Avoid hidden work in constructors, accessors, annotations, global registration, implicit hooks, middleware, operators, reflection, metaprogramming, or framework lifecycle callbacks unless the project already relies on that mechanism and the behavior is easy to locate.
- Do not split one policy across pass-through layers or tiny helpers that force navigation without hiding a volatile decision.
- Use comments only for non-obvious constraints, rationale, or required contracts when clearer structure and naming cannot carry the information.

### Change

- Organize boundaries around responsibilities and decisions that change for different reasons.
- Hide volatile implementation choices behind the smallest stable interface that serves real callers.
- Keep dependencies directed and visible. Prevent convenience imports, callbacks, shared mutable state, or broad service locators from bypassing ownership.
- Prefer high cohesion and low change coupling. A routine change should not require synchronized edits across unrelated modules.
- Add a seam only when it localizes a demonstrated variation, side effect, external dependency, or testing boundary.
- Duplicate a small amount of obvious code when premature unification would couple concepts with different change reasons. Consolidate repetition when one rule must remain identical.

### Verify

- Test observable behavior and contracts rather than private call sequences or internal layout.
- Keep tests readable as examples of supported behavior.
- Use fakes or mocks only at real boundaries; do not mirror every internal collaborator.
- A behavior-preserving refactor should normally leave behavioral assertions unchanged.
- Verify the most likely future change or failure path when it reveals whether the selected boundary is useful.

## Architecture Decision Rule

Do not choose architecture by fashion or by language.

For each meaningful boundary, identify:

- the behavior or policy it owns
- the callers it serves
- the implementation decision it hides
- the likely reason it would change
- the dependencies it is allowed to use
- the contract and tests that protect it

Keep the current architecture when it already makes the requested change local and understandable. Strengthen an existing boundary before adding a new layer. Introduce a new boundary only when current coupling makes a real change cross unrelated ownership, mixes independently changing concerns, or prevents proportionate testing.

Do not introduce microservices, plugins, event buses, repositories, factories, generic adapters, dependency injection containers, base classes, or framework layers solely to appear maintainable. These structures are justified only by current deployment, ownership, variation, integration, or testing needs.

## Human Change Simulation

Before completion, simulate one realistic follow-up change without implementing it.

Ask:

1. Where would a maintainer start?
2. How many concepts, files, and ownership boundaries must they understand?
3. Is the rule to change owned in one place?
4. Can they predict affected callers and persisted or external contracts?
5. Would tests fail for a behavioral regression rather than an internal rearrangement?

If the answer requires repository-wide search, coordinated edits across unrelated modules, knowledge of hidden framework behavior, or broad test rewrites, improve the boundary or lower the maintainability claim.

Do not optimize for a numeric file or layer count. Use the simulation to detect unnecessary navigation, hidden coupling, and scattered ownership.

## Metrics Boundary

Treat line count, cyclomatic complexity, cognitive complexity, dependency counts, maintainability index, and similar metrics as investigation signals only.

- A low score does not prove that code is easy to maintain.
- A high score may identify a location worth reading, but does not prescribe the refactor.
- Combine structural signals with real callers, change history, domain ownership, test behavior, and the likely maintenance task.
- Prefer evidence from actual change propagation and maintainer workflow over metric thresholds.

## Cross-Language Adaptation

Apply the same goals in every language, but express them through local idioms:

- use the language's ordinary error, resource, type, module, concurrency, and testing patterns
- respect repository formatters, linters, visibility rules, package conventions, and generated-code boundaries
- avoid importing patterns from another language when the local ecosystem has a clearer standard form
- do not erase language-specific safety features merely to make implementations look uniform

The invariant is human changeability, not identical syntax or architecture.

## Evidence Base

The model above synthesizes these sources:

- ISO/IEC 25010 product quality model: maintainability includes modularity, analysability, modifiability, and testability.
- D. L. Parnas, "On the Criteria to Be Used in Decomposing Systems into Modules": hide design decisions likely to change behind module interfaces.
- CMU Software Engineering Institute, "Modifiability Tactics": use cohesion, coupling, encapsulation, and intermediaries to control modification cost.
- Google Engineering Practices: reject unnecessary complexity and over-engineering; optimize code health, readability, consistency, and tests.
- Software Engineering at Google, testing guidance: tests should protect behavior and survive refactoring when requirements do not change.
- DORA research on loosely coupled architecture: teams perform better when systems can be changed and tested independently through well-defined interfaces.
- Empirical change-coupling research: repeated co-change correlates with defects, while dependency metrics alone cannot fully explain evolvability.
- Empirical understandability research: structural complexity metrics correlate with some aspects of comprehension but are not accurate enough to replace human and task context.

Sources:

- https://www.iso.org/standard/78176.html
- https://doi.org/10.1145/361598.361623
- https://www.sei.cmu.edu/library/modifiability-tactics/
- https://google.github.io/eng-practices/review/reviewer/looking-for.html
- https://abseil.io/resources/swe-book/html/ch12.html
- https://dora.dev/capabilities/loosely-coupled-teams/
- https://www.inf.usi.ch/lanza/PUBS/P/DAmb2009e.pdf
- https://doi.org/10.1007/s10664-023-10396-7
