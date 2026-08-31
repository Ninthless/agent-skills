# Project Structure

Use this reference when creating, reorganizing, or materially extending packages, modules, directories, workspaces, services, or cross-module dependencies.

Do not use a universal directory template. Treat a project structure as healthy when a common change has a discoverable starting point, stays within one owner or a small coherent set of owners, crosses explicit contracts, and has focused verification.

## Contents

- Structure Decision Model
- Module Contract
- Organization Strategy
- Dependency And Visibility Rules
- Data And State Ownership
- Shared Code Policy
- Test Structure
- Granularity And Depth
- Ecosystem Fit
- Change Simulation
- Failure Patterns
- Completion Gate
- Evidence Base

## Structure Decision Model

Before adding or moving a structural boundary, identify:

- the business capability, stable responsibility, state, external integration, or design decision it owns
- the current callers and consumers
- the implementation detail or volatile decision it hides
- the realistic reason it will change
- the public contract other owners may depend on
- the dependencies it may use
- the tests that prove its behavior

Prefer a boundary around a design decision likely to change independently. Do not decompose primarily by execution order, file type, architectural fashion, or directory symmetry.

Keep the current structure when the requested change is already local, traceable, and verifiable. Strengthen visibility or naming before introducing another package, module, project, crate, service, or repository.

## Module Contract

Every meaningful module must have:

- **Owner:** one identifiable responsibility, rule set, state, or integration
- **Callers:** current consumers rather than hypothetical future users
- **Public contract:** the minimum inputs, outputs, errors, events, or queries consumers need
- **Hidden decisions:** internal models, algorithms, storage, framework, SDK, retry, cache, or serialization details consumers must not rely on
- **Allowed dependencies:** the direction of valid calls and imports
- **Data ownership:** authoritative mutable state and permitted mutation paths
- **Verification:** focused behavioral, integration, or contract tests

If these cannot be stated, the boundary is probably premature, overloaded, or only visual.

## Organization Strategy

For applications with meaningful business capabilities, prefer top-level organization by capability, feature, bounded context, or stable responsibility. Within a sufficiently complex capability, subdivide by technical responsibility only where it improves ownership or dependency control.

Use package-by-layer at the top level only when project scale, framework constraints, team specialization, or the absence of stable feature boundaries makes it clearer. Do not let global `controllers`, `services`, `repositories`, `models`, or `handlers` become unbounded buckets that every feature must cross.

Allow modules to have different internal shapes. A simple capability does not need empty domain, application, infrastructure, contracts, repository, or adapter layers merely because a larger sibling needs them.

Start small structures flat. Add a subdirectory or module when a second real responsibility, visibility boundary, independent lifecycle, external integration, or testing seam appears. Merge directories again when their distinction no longer carries design meaning.

## Dependency And Visibility Rules

- Keep dependencies directed and explainable.
- Expose the smallest stable public surface.
- Keep internal types, storage models, provider SDKs, and implementation helpers private.
- Prevent one module from importing another module's private representation.
- Reject dependency cycles unless the verified platform contract makes one unavoidable and explicitly managed.
- Enforce boundaries with language visibility, package rules, build targets, project references, lint rules, or architecture tests when the repository supports them.
- Prefer compiler or build enforcement over convention-only documentation for important boundaries.
- Do not use a global event bus, service locator, callback registry, or dependency container to bypass ownership.

Cross-module communication should express behavior or a stable query, not leak internal storage or mutable entities.

## Data And State Ownership

- Give each business table, persisted aggregate, cache namespace, mutable state machine, and externally synchronized record one authoritative owner.
- Let other modules request behavior or consume an explicit query, event, or contract.
- Do not allow unrelated modules to write another owner's tables or mutate its in-memory state directly.
- Treat a shared physical database as infrastructure, not as shared ownership.
- Keep migrations and persistence models with the state owner.
- When data is copied across boundaries, define source of truth, update flow, consistency, idempotency, and recovery.

A source tree is not modular when modules still coordinate through shared mutable storage.

## Shared Code Policy

Move code into a shared area only when:

- at least two current consumers use the same semantics
- the rule must evolve identically for those consumers
- ownership and lifecycle are compatible
- sharing reduces change coupling rather than hiding it

Keep business-specific policy with its owner even if another module has similar code. Prefer small explicit duplication over a generic abstraction that couples different change reasons.

Reject `utils`, `common`, `shared`, `base`, `manager`, `processor`, or `helpers` as default destinations. Such names are acceptable only when the contents have a narrower documented responsibility and allowed dependency policy.

Shared modules must not become dependency roots that own unrelated domain rules.

## Test Structure

- Place focused tests where a maintainer looking for the behavior will find them according to repository convention.
- Test module public behavior and contracts rather than private directory layout.
- Put integration tests at real storage, process, protocol, or external-service boundaries.
- Use contract tests for cross-module or cross-service assumptions.
- Keep fixtures with their primary owner; share them only when their semantics are truly common.
- Avoid global test helpers that recreate application architecture or force every module through one mock framework.
- Keep end-to-end tests for critical cross-owner flows rather than using them as the only verification for local behavior.

The test structure should reveal how behavior is verified without requiring repository-wide discovery.

## Granularity And Depth

Avoid both extremes:

- one module containing the whole project
- one module, package, directory, interface, or build target per file without a real boundary

Add structural depth only when the new level names an owner, limits visibility, controls dependencies, owns a lifecycle, or provides a coherent testing boundary.

Reject:

- directories containing only an index and one pass-through implementation
- fixed multi-layer templates copied into every feature
- one-implementation interfaces without a contract, lifecycle, replacement, or test need
- deep navigation for simple linear behavior
- symmetric empty folders added for possible future use
- microservice extraction justified only by file size or architectural fashion

Directory count, layer count, service count, and file count are not quality metrics.

## Ecosystem Fit

Use the language and framework's standard project layout as the baseline:

- respect package, module, crate, workspace, project, source-root, test, example, migration, and generated-file conventions
- use native visibility and dependency mechanisms
- follow established naming and import rules
- preserve framework-required entry points and registration locations
- avoid translating another ecosystem's package structure mechanically

Repository conventions remain authoritative when they are maintained, coherent, and enforced. Do not preserve convention drift merely because an older module exists; compare analogous healthy modules and current tooling.

## Change Simulation

Before accepting a structural change, simulate the requested change and one likely follow-up:

1. Where does a maintainer start?
2. Which module owns the behavior and state?
3. Which contracts and consumers are affected?
4. Does the change stay within one owner or a small coherent set?
5. Are dependency direction and data ownership preserved?
6. Which focused tests catch a regression?
7. Does any extracted unit hide a real decision, or only add navigation?

Classify the structure:

- **Local:** one owner and its tests contain the change.
- **Coordinated but coherent:** a small related set changes through explicit contracts.
- **Scattered:** unrelated modules, private data, duplicate rules, global utilities, or broad mock rewrites must change together.

Reject a newly created `Scattered` structure. Report a pre-existing scattered structure as risk when correcting it is outside the authorized slice.

## Failure Patterns

Treat these as structural warnings:

- one business change always crosses global technical-layer directories
- duplicate validation, defaults, state transitions, or policy across owners
- cross-module database writes or shared mutable entities
- private implementation types used as public contracts
- circular dependencies or unrestricted visibility
- business rules accumulated in generic shared folders
- feature modules with identical empty layer templates
- many tiny files whose only purpose is forwarding
- tests coupled to internal call order and directory layout
- a module name that does not tell maintainers where a realistic change belongs
- boundaries chosen to mirror teams temporarily rather than stable responsibilities
- service extraction without independent operational, scaling, security, ownership, or release needs

## Completion Gate

For structural work, require:

- every introduced or changed module has an identifiable owner and current callers
- public contracts expose no unnecessary internal representation
- dependency direction is explicit and enforceable where practical
- mutable data and state have one authoritative owner
- common changes are `Local` or `Coordinated but coherent`
- tests align with behavior and contracts
- directory and module depth is justified by real boundaries
- ecosystem and repository conventions are preserved
- no speculative module, empty layer, generic bucket, cycle, or boundary bypass is introduced

Do not mark the structure healthy because it resembles Clean Architecture, DDD, a modular monolith, vertical slices, or microservices. Judge the actual ownership, contracts, dependency graph, data boundaries, and maintenance path.

## Evidence Base

This policy applies:

- Parnas information hiding: isolate independently changing design decisions behind stable interfaces.
- Parnas module guides: structure should lead a maintainer to the module that must change.
- DORA loosely coupled architecture: teams and systems should be independently changeable and testable through well-defined contracts.
- Bazel dependency guidance: module granularity and explicit dependencies materially affect maintenance, and both overly coarse and overly fine modules have costs.
- Package-by-feature guidance: group code that changes for one capability while allowing justified internal technical subdivision.
- Language and build-tool layout conventions: use ecosystem-native package, workspace, test, and visibility mechanisms.

Sources:

- https://doi.org/10.1145/361598.361623
- https://faculty.cs.olemiss.edu/~hcc/csci555/notes/localcopy/Parnas_Modular_Structure.pdf
- https://dora.dev/capabilities/loosely-coupled-teams/
- https://bazel.build/basics/dependencies
- https://vaadin.com/docs/latest/building-apps/architecture/packages
- https://doc.rust-lang.org/stable/cargo/guide/project-layout.html
