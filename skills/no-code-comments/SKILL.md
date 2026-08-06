---
name: no-code-comments
description: 'Apply a comment-style companion when the user explicitly asks for no comments, remove comments, comment-free code, or the repository clearly requires that policy. Use only alongside the primary implementation or documentation skill. Do not trigger for ordinary coding, webpage work, read-only analysis, translation, or API docs without an explicit or repository-established no-comment policy; preserve required directives, generated markers, legal headers, and public API documentation.'
---
# No Code Comments

## Trigger policy

Use only when the user explicitly asks for no comments or clean comment-free output, or when repository evidence establishes that convention. Do not trigger as an implicit low-priority companion for ordinary writing, editing, refactoring, tests, configs, schemas, webpage work, API implementation, or other code output solely because it is code-like. A platform may select this skill only when that explicit or repository-established evidence exists.

Priority order:

1. explicit user requirements
2. platform safety and required directives
3. enforced repository conventions and public API documentation contracts
4. this comment-style preference

## Default behavior

Avoid new comments that merely restate names, syntax, assignments, control flow, or obvious intent. Prefer clear names and direct structure. This is not a ban on all comments or documentation.

Allow and preserve when applicable:

- required directives such as lint, type-checker, coverage, shell, encoding, or framework directives
- mandatory legal headers and generated-file markers
- public API docstrings, JSDoc, XML docs, and documentation comments required by repository or tooling contracts
- concise comments explaining non-obvious invariants, external constraints, safety reasoning, or workarounds when code alone cannot carry the intent
- unrelated existing comments, including comments outside the changed area

Do not remove existing comments merely to satisfy this preference. Update a touched comment only when the change makes it false or the user explicitly requests cleanup.

## Artifact boundaries

- Markdown API prose is documentation, not a code comment; follow the documentation task.
- OpenAPI, AsyncAPI, proto, JSON Schema, and similar machine contracts may use specification-defined semantic fields such as `description`, `summary`, deprecation text, examples, and field documentation.
- Source doc comments are governed by public API, repository, language, and tooling contracts before this preference.

When active with another skill, the domain skill owns architecture and deliverables. This skill only suppresses low-value explanatory comments where no stronger requirement applies.
