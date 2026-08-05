---
name: no-code-comments
description: 'Prefer self-explanatory code and avoid low-value comments when the user explicitly requests comment-free code, the repository has an established no-comment convention, or this skill is selected as a low-priority companion. Discourage comments that merely restate syntax or nearby code. Do not treat every coding task as a must-trigger, and do not block required directives, generated markers, legal headers, public API documentation contracts, useful docstrings/JSDoc/XML docs, or schema-native description and summary fields.'
---
# No Code Comments

## Trigger policy

Use when the user explicitly asks for no comments or clean comment-free output, when repository evidence establishes that convention, or as a low-priority companion that does not conflict with stronger requirements. Do not must-trigger for ordinary writing, editing, refactoring, tests, configs, schemas, or code output solely because they are code-like.

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
