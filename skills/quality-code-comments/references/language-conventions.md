# Language Conventions

Read only the section for the language you are editing. These rules change the comment form, not the admission test in `SKILL.md`. Repository convention still wins when it is explicit and consistent.

## Python

Comments (`#`) explain why or warn. Docstrings are a runtime contract, not an implementation comment.

- Write docstrings for public modules, classes, functions, and methods when the repository already documents them or the artifact is a public API. Use `"""triple double quotes"""`.
- A one-line docstring is an imperative phrase ending in a period: `"""Return the cached session, or None if expired."""`
- Multi-line docstrings keep a one-line summary, a blank line, then arguments, return values, side effects, exceptions, and call restrictions that the signature does not show. Closing quotes sit on their own line.
- Do not restate the signature. Do not invent `Args`/`Returns` fields the code does not enforce.
- Non-public helpers do not need docstrings. If a private method has a non-obvious contract, a short comment after `def` is enough.
- Use inline comments sparingly, with two spaces before `#`.

## JavaScript and TypeScript

- Use `//` for implementation comments.
- Write JSDoc only for exported public APIs, or when the repository's TypeDoc, ESLint, or declaration emit depends on it.
- Document behavior the type does not already state: units, side effects, throws, accepted strings, and ownership. Do not duplicate `{string}` or obvious `@param` names.
- `/* eslint-disable */`, `@ts-expect-error`, and `prettier-ignore` must name the exact rule or reason and stay as narrow as possible.

## Rust

- `//` is an implementation comment.
- `///` documents the following item; `//!` documents the enclosing crate or module.
- Document public items the way rustdoc will render them: purpose, panics, errors, and ownership. Put examples only when they are compile-worthy or already the crate's style.
- Do not use `///` on private helpers to look documented.

## Go

- Godoc comments are full sentences immediately before the exported name, starting with that name: `// Lookup returns the first matching record.`
- Comment exported packages, types, functions, and constants. Unexported code gets an implementation comment only when the admission test passes.
- Do not write `/* */` banners or comments that repeat the identifier.

## Java, Kotlin, and C#

- Documentation comments (`/** */`, `///`) belong on public API types and members the repository already documents.
- Record nullability, ownership, thread-safety, and exceptions only when the type system does not already say so.
- Overrides need a comment only when they change the inherited contract.

## C and C++

- Prefer `//` unless the file already uses `/* */`.
- Comment non-obvious classes, functions, and data members with use, ownership, nullability, and invariants.
- Do not describe the next statement to a reader who already knows the language. Explain why a lock is held, why a fallback exists, or what a sentinel means.
- `TODO` needs an issue, owner, or removal event.

## SQL, YAML, JSONC, and shell

- Comment operational meaning: units, time zones, idempotency, rollback hazards, and why a value is not the default.
- Do not restating keys, flags, or SQL clauses the syntax already states.
- Preserve shebangs, linter pragmas, and generated-file headers exactly.
