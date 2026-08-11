# Protocol And Execution Boundaries

Use this reference when code implements a multi-stage protocol, callback interface, ABI or FFI boundary, plugin contract, concurrent workflow, transaction, retry loop, resource-owning API, or platform-sensitive build.

## Contents

- Protocol State
- Parameter And Ownership Semantics
- ABI And FFI Safety
- Concurrency And Reentrancy
- Failure Atomicity And Idempotency
- Build And Platform Integrity
- Verification Matrix

## Protocol State

Treat related callbacks and methods as one protocol, not isolated functions.

Identify:

- valid call order
- state carried between calls
- caller capabilities or constraints negotiated earlier
- legal outputs in each state
- reset behavior after completion, rejection, cancellation, disconnect, or teardown
- behavior for repeated, skipped, or out-of-order calls

Do not return a locally plausible value that contradicts an earlier decision or caller constraint. Store minimal session state only when the protocol requires it; otherwise revalidate from authoritative inputs.

## Parameter And Ownership Semantics

For every boundary parameter, determine:

- input, output, or input-output direction
- required, optional, nullable, or sentinel semantics
- borrowed, shared, transferred, retained, or consumed ownership
- mutability and aliasing guarantees
- valid lifetime
- allowed value set and caller-supplied constraints
- whether partial output is valid on failure

Do not infer semantics from pointer, reference, handle, buffer, or parameter names. Preserve caller restrictions when choosing an output. Initialize out parameters to a safe contract value before later failure when the protocol requires it.

## ABI And FFI Safety

Do not allow a language-specific failure mechanism to cross a boundary that does not define it.

- translate exceptions, panics, error objects, status codes, and cancellation into the boundary's supported error model
- catch failures from allocation, conversion, callbacks, user-supplied handlers, and container operations when they can reach the boundary
- preserve meaningful categories such as resource exhaustion, invalid input, cancellation, conflict, and generic failure when the contract distinguishes them
- validate calling convention, data layout, alignment, encoding, nullability, thread affinity, and ownership rules
- keep callbacks and referenced memory alive for the full required lifetime without leaking them
- perform cleanup before returning a boundary error

Do not catch everything inside ordinary internal code by default. Contain failures at the narrow boundary that cannot safely transport them.

## Concurrency And Reentrancy

Define:

- shared state and its owner
- allowed threads, tasks, processes, or executors
- synchronization and memory-visibility guarantees
- whether callbacks may be concurrent or reentrant
- ordering requirements
- cancellation and completion races
- duplicate delivery behavior
- teardown while work is active

Do not hold locks across unknown callbacks or blocking external calls unless the contract requires it and deadlock behavior is understood. Do not assume a callback cannot synchronously reenter the object that invoked it. Commit state before notification when observers are allowed to query the new state.

Prefer designs whose correctness follows from explicit ownership, immutability, message passing, transactions, or narrow critical sections. Add synchronization only around demonstrated shared state.

## Failure Atomicity And Idempotency

For every operation that can partially progress, choose and verify one contract:

- all-or-nothing
- partial success with an explicit result
- resumable progress with a durable checkpoint
- best effort with reported failures

Do not silently return success after partial failure. Do not expose partially initialized state as complete.

For retries, establish:

- which failures are retryable from structured evidence
- whether the operation is idempotent
- which resources must be recreated
- whether a prior attempt may have committed despite an ambiguous response
- deduplication, transaction, sequence, or idempotency-key behavior
- retry limit, backoff, cancellation, and final error

Success notifications and side effects must follow the authoritative commit boundary.

## Build And Platform Integrity

Treat successful compilation in one environment as limited evidence.

- include or import direct dependencies explicitly unless the language or project guarantees re-export
- verify generated artifacts, feature flags, conditional compilation, build profiles, link modes, architecture, and supported runtime versions
- avoid relying on transitive includes, incidental import order, undefined behavior, global initialization order, or platform-specific defaults
- preserve source and binary compatibility where callers require it
- test representative supported environments when code crosses compiler, standard-library, operating-system, architecture, or build-mode boundaries

Do not add portability machinery for unsupported environments. Match the repository's declared support matrix.

## Verification Matrix

Select applicable checks:

- valid, invalid, repeated, skipped, and out-of-order protocol calls
- caller allows all, some, or none of the possible outputs
- null, empty, maximum-size, malformed, and partially valid inputs
- allocation, conversion, callback, I/O, and user-handler failures at the boundary
- exception or panic containment and exact error mapping
- success, partial failure, rollback, ambiguous commit, and retry exhaustion
- concurrent calls, reentrant callback, cancellation race, duplicate delivery, and teardown race
- debug and release builds, relevant feature combinations, and supported toolchains or platforms
- independent compilation that exposes missing direct dependencies

Test the protocol as a sequence and the boundary as a contract. Per-method happy-path tests are not sufficient.
