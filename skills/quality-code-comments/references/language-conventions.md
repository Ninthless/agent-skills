# Language Conventions

Read only the section for the language you are editing. These rules change the comment form and documentation contract, not the evidence and admission tests in `SKILL.md`. Follow repository convention when it is explicit, consistent, tool-valid, and compatible with evidenced behavior.

## Python

Comments (`#`) explain implementation context. Docstrings are user- and tooling-facing documentation available through `__doc__`, not ordinary implementation comments.

- PEP 8 and PEP 257 normally expect docstrings on public modules, classes, functions, and methods. Follow the repository's chosen docstring format and use `"""triple double quotes"""`.
- A one-line function or method docstring is an imperative phrase ending in a period: `"""Return the cached session, or None if expired."""` Module and class summaries describe their purpose or behavior.
- Multi-line docstrings keep a concise summary, a blank line, then the applicable arguments, return values, side effects, exceptions, and call restrictions. Put closing quotes on their own line.
- Do not restate the signature. Types and parameter names may still need semantic descriptions such as units, ownership, accepted ranges, or keyword behavior.
- Non-public helpers do not require docstrings. If a non-public method needs explanation, PEP 8 permits a comment immediately after `def`; use a docstring instead when repository tooling treats the helper as documented API.
- Use inline comments sparingly, with at least two spaces before `#` and one space after it.

## JavaScript and TypeScript

- Use `//` for implementation comments.
- Use JSDoc for public APIs when the repository publishes it, and in JavaScript when TypeScript uses JSDoc for type checking. In `.ts` files, avoid tags that merely duplicate TypeScript types.
- Document semantics the type does not state: units, side effects, thrown errors, accepted values, ownership, deprecation, and mutation.
- TypeScript recognizes documentation tags such as `@deprecated`, `@see`, and `@link` in JavaScript and TypeScript, while many type tags affect only JavaScript. Do not add unsupported tags expecting compiler behavior.
- Keep `eslint-disable`, `@ts-expect-error`, and `prettier-ignore` directives as narrow as possible and state the evidenced incompatibility or rule when the syntax permits it.

## Rust

- `//` is an implementation comment.
- `///` documents the following item; `//!` documents the enclosing crate or module.
- Document public crates and items with a one-line summary followed by details. Public items should normally have a copyable, doctested example; omit one or link to another example only when that is clearly more useful.
- Add `# Panics`, `# Errors`, and `# Safety` sections when those contracts apply. Do not repeat types that rustdoc already links from the signature.
- Treat examples as code: make them compile and run as doctests when practical. Prefer a specific `no_run`, `compile_fail`, or target condition over a generic ignored block when execution is unsuitable.
- Do not use `///` on private helpers merely to look documented; use it when the item is intentionally surfaced in generated internal docs.

## Go

- Every exported name, including exported methods, should have a doc comment immediately before its declaration. Start the first sentence with the declared name when practical: `// Lookup returns the first matching record.`
- Package comments begin with `Package name` and explain the package as a whole.
- Explain the meaning of exported fields either in the type's doc comment or on each field.
- Non-trivial unexported declarations may deserve comments, but do not generate boilerplate merely for coverage.
- Use Go's documented paragraph, heading, list, link, and `Deprecated:` forms when tooling consumes them.
- Do not write `/* */` banners or comments that repeat the identifier.

## Java, Kotlin, and C#

- Documentation comments (`/** */`, `///`) belong on public API types and members when the repository publishes or validates generated API documentation.
- Give the declaration a useful summary and document parameters, return values, and exceptions according to the active Javadoc/KDoc/XML-doc contract. Add semantics, not just rewritten names and types.
- Record nullability, ownership, mutation, thread-safety, and exceptions when callers cannot recover them from the type system or inherited contract.
- Overrides need a comment only when they change the inherited contract.

## C and C++

- Prefer `//` unless the file already uses `/* */`.
- Declaration comments explain use and contract; definition comments explain non-obvious implementation choices. Follow the repository's Doxygen or kernel-doc format when present.
- Comment non-obvious ownership, nullability, locking, memory ordering, units, sentinels, and invariants at the declaration or point that owns them.
- Do not describe the next statement to a reader who already knows the language. A short function-level summary of necessarily low-level code is valid when it saves reverse engineering.
- Linux kernel style prefers function-level WHAT/WHY and warns against HOW narration inside function bodies; other C/C++ repositories may place rationale at the point of use.
- `TODO` needs the repository's expected issue or owner form and an actionable condition. Never invent one.

## SQL, YAML, JSONC, and shell

- Comment operational meaning: units, time zones, idempotency, rollback hazards, and why a value is not the default.
- Do not restate keys, flags, or SQL clauses the syntax already states.
- Preserve shebangs, linter pragmas, and generated-file headers exactly.
- Treat commands and configuration shown only in chat as code-like artifacts under the same comment policy.

## Primary Sources

- [Google Documentation Best Practices](https://google.github.io/styleguide/docguide/best_practices.html)
- [Google C++ Style Guide: Comments](https://google.github.io/styleguide/cppguide.html#Comments)
- [PEP 8: Comments and Documentation Strings](https://peps.python.org/pep-0008/#comments)
- [PEP 257: Docstring Conventions](https://peps.python.org/pep-0257/)
- [TypeScript JSDoc Reference](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html)
- [The rustdoc book: How to write documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
- [The rustdoc book: Documentation tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
- [Rust API Guidelines: Documentation](https://rust-lang.github.io/api-guidelines/documentation.html)
- [Go Doc Comments](https://go.dev/doc/comment)
- [JavaDoc Documentation Comment Specification](https://docs.oracle.com/en/java/javase/24/docs/specs/javadoc/doc-comment-spec.html)
- [Linux kernel coding style: Commenting](https://www.kernel.org/doc/html/latest/process/coding-style.html#commenting)
- [RFC 9110: Retrying Requests](https://datatracker.ietf.org/doc/html/rfc9110#section-9.2.2)
