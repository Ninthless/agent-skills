# Dependency Capabilities And Lifecycles

Use this reference when correctness depends on proving an external capability in the repository's actual version, configuration, registration, generated artifacts, state model, or round trip.

Use [protocol-boundaries.md](./protocol-boundaries.md) instead for call ordering, ABI or FFI, parameter direction, ownership transfer, concurrency, reentrancy, transactions, retries, idempotency, partial commits, or build matrices. Use both when an external dependency also owns those semantics.

## Contents

- Core Rule
- Capability Evidence
- End-To-End Contract
- Lifecycle Model
- Async And Callback Boundaries
- State Authority
- Verification Matrix
- Unsupported Inference Patterns

## Core Rule

Do not implement from a plausible API name or a remembered pattern.

Before relying on non-trivial dependency behavior, prove that the repository's actual version, configuration, registration, generated artifacts, and runtime path support the required capability.

Treat these as separate claims:

1. an API symbol exists
2. the current project can call it
3. the call changes the authoritative state
4. the state survives serialization, persistence, reload, undo, retry, or reconstruction as required
5. consumers observe the intended result

Evidence for one claim does not prove the others.

## Capability Evidence

Establish the exact dependency contract from the strongest available source:

1. lockfile, manifest, resolved dependency tree, generated code, or runtime version
2. repository registration, configuration, adapters, extensions, or custom types
3. local type declarations and implementation
4. official documentation for the exact installed version
5. focused runtime probe or existing test

Do not mix documentation or examples from incompatible major versions. Do not assume a default extension supports custom fields, formats, hooks, operators, annotations, middleware, serializers, or protocol features without finding the registration or implementation that provides them.

If the capability cannot be proven, either use a repository-supported path, add the smallest required integration with tests, or report the missing evidence. Do not hide uncertainty behind a plausible call.

## End-To-End Contract

Trace data and behavior through the complete round trip that the feature promises:

- input or user action
- normalization and validation
- library or framework representation
- authoritative in-memory state
- serialization or transport
- persistence
- reload or reconstruction
- downstream observation
- error and recovery behavior

For edits, verify that the official state model changes, not only a rendered view or notification. For persistence, verify both write and read paths. For extensible data formats, verify unknown-field and custom-field behavior. For generated clients or schemas, verify that source definitions and generated artifacts agree.

Do not manually emit success or change notifications as a substitute for proving that the underlying state transition occurred.

## Lifecycle Model

For each stateful or asynchronous operation, identify:

- owner
- start condition
- authoritative state
- valid transitions
- completion condition
- failure paths
- cancellation path
- timeout policy when required
- cleanup responsibility
- behavior after caller, component, request, process, or resource destruction

Reject operations that can remain pending indefinitely without an intentional long-lived contract. Reject callbacks or promises whose completion depends on an unverified consumer. Prevent late completion from mutating destroyed, superseded, or detached state.

When an operation captures a position, selection, revision, handle, transaction, cursor, token, or other time-sensitive reference, define whether completion uses:

- the state captured at start
- the current state at completion
- a stable placeholder or identity that moves with edits
- conflict detection and retry

Do not choose silently. Preserve the existing product contract or obtain a requirement.

## Async And Callback Boundaries

- Prefer one explicit owner for starting, completing, cancelling, and observing an operation.
- Use the repository's established async abstraction before inventing callback protocols.
- Ensure every accepted operation reaches a terminal state or is intentionally transferred to a longer-lived owner.
- Make duplicate completion, late completion, cancellation, and teardown behavior safe.
- Do not reuse partially consumed streams, failed transactions, expired handles, stale selections, or mutable request state unless the dependency contract explicitly permits it.
- Keep retries outside single-attempt work when that makes resource recreation and failure classification explicit.

## State Authority

Choose one authoritative state model.

- Framework state, domain state, rendered state, cached state, persisted state, and emitted events must not tell different stories.
- Direct DOM, memory, cache, or internal-object mutation is valid only when that layer is authoritative or the official model is updated coherently.
- Notifications describe completed or committed state; they do not create correctness.
- Manual event emission must not impersonate a framework-native change when undo, serialization, subscriptions, dirty tracking, or persistence depend on the native state model.

## Verification Matrix

Select the rows applicable to the feature:

- supported and unsupported dependency versions
- default and repository-customized configuration
- ordinary content and content containing only structured or embedded values
- write, serialize, reload, and read round trip
- create, edit, delete, undo, and redo
- success, validation failure, dependency failure, cancellation, timeout, and retry exhaustion
- operation completion before and after owner teardown
- state changes during an in-flight operation
- duplicate, delayed, missing, or out-of-order callbacks
- compatibility with existing callers and stored data

Prefer focused contract tests or runtime probes over broad assertions that only show initialization succeeded.

## Unsupported Inference Patterns

Reject reasoning such as:

- the method name implies the desired capability
- the latest documentation probably matches the installed version
- a rendered change proves persistence
- an emitted event proves authoritative state changed
- a callback will eventually complete because consumers should call it
- a captured index, cursor, token, or handle remains valid across asynchronous work
- an extension field will survive round trips because the in-memory object accepted it
- a successful happy path proves teardown, retry, or cancellation safety

These are hypotheses until supported by repository or runtime evidence.
