# Testing Strategy

Start with the behavior or public contract that must remain true. Select the project-native test command and the narrowest useful level, then add adjacent coverage when the change crosses a shared seam.

Cover success plus relevant failure, recovery, cancellation, timeout, duplicate, ordering, transaction, resource, and compatibility behavior. Use unit tests for local rules, property tests for broad invariants, contract tests for producer-consumer agreements, integration tests for real boundaries, browser tests for browser-visible behavior, migration checks for forward and recovery assumptions, and benchmarks only when a performance question and baseline exist.

Use test doubles at meaningful external boundaries. Do not mock every collaborator or assert internal call order when observable behavior can prove the contract. Avoid tests coupled to incidental decomposition, private names, exact helper counts, or implementation-only branches. Close the loop: run the focused check, fix failures attributable to the change, rerun, and report checks that remain unavailable.