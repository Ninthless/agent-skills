---
name: no-code-comments
description: 'Apply a low-priority comment-style companion to coding tasks that create or modify source code, tests, scripts, configs, schemas, or webpage code. Suppress low-value explanatory comments while preserving required directives, generated markers, legal headers, public API documentation, and necessary comments for non-obvious constraints. Do not trigger for read-only analysis, requirements-only work, research, translation, API documentation-only work, or Git actions unless the user explicitly requests comment-free output.'
---
# No Code Comments

## Trigger policy

Trigger as a low-priority companion whenever the primary task will create or modify code-like artifacts. An explicit no-comment request or repository convention strengthens the preference, but is not required for ordinary coding changes. Do not trigger for read-only review, requirements-only work, research, translation, API documentation-only work, or Git actions unless the user explicitly requests comment-free output.

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
