# Language And Ecosystem Profile

Use repository evidence to identify the language, version, compiler or runtime, framework, package manager, formatter, linter, type checker, build, and test commands. This is a checklist for discovery, not a hard-coded style manual. Project rules, maintained local code, and enforced tooling take priority; consult current official documentation through `technical-solution-research` or web evidence only when a decisive fact is uncertain.

For the affected subsystem, inspect:

- C and C++: RAII or explicit ownership, allocator and native-resource cleanup, value/reference semantics, undefined behavior, error representation, thread safety, build flags, sanitizers, and ABI boundaries.
- Rust: ownership, borrowing, lifetimes, `Result`/`Option`, async cancellation, `Send`/`Sync`, task shutdown, resource guards, and Cargo feature/toolchain behavior.
- Java, C#, and Kotlin: static types, nullability, async/task cancellation, executor or coroutine lifetime, exception boundaries, resource disposal, transaction scope, and framework lifecycle.
- Python, Ruby, and JavaScript: dynamic boundaries, validation and normalization, `None`/nil/undefined, global or mutable state, exception scope, async cancellation, resource cleanup, package/runtime version, and test isolation.
- TypeScript: strictness and compiler version, discriminated unions, narrowing, nullability, runtime validation at external boundaries, promise cancellation/timeouts, and generated/build output.
- Go: explicit errors, `context.Context`, interfaces at consumer boundaries, goroutine ownership and shutdown, zero values, close behavior, error wrapping, modules, and race tests.
- Shell, configuration, and SQL: quoting and expansion, exit status and cleanup, injection boundaries, typed configuration parsing, transaction and lock scope, idempotence, migration ordering, rollback or recovery, and native lint/test tooling.

When a language family is mixed with another, evaluate each boundary and the actual runtime behavior rather than applying one uniform rule.