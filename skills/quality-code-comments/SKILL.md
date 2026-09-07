---
name: quality-code-comments
description: 'Mandatory comment-quality companion whenever the agent generates, writes, edits, refactors, or shows code. Keep comments sparse and load-bearing: prefer self-explanatory names and structure, then record only intent, invariants, constraints, workarounds, or documentation contracts the code cannot express. Trigger for write, create, implement, fix, edit, refactor, 写代码, 加注释, 写好注释, 优雅注释, or JSDoc/docstring requests. Do not trigger for comment-free output, pure analysis without code, or when the user has chosen no-code-comments instead.'
---

# Quality Code Comments

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Purpose

Govern comments as part of the code, not as decoration. Most lines need no comment. When a comment exists, it must still be true after a refactor, and it must tell a future reader or agent something the code cannot.

Optimize in this order:

1. make the code name and structure carry the meaning
2. add the smallest comment that records a non-local fact
3. match the repository's existing comment and documentation contract
4. keep comments current; a stale comment is a bug

Do not optimize for looking thoroughly documented. Do not narrate control flow. Do not use comments as a substitute for clearer names, types, tests, or structure.

## Mandatory Code-Producing Companion

Activate whenever the response will produce, modify, or show code or a code-like artifact, including snippets, configs, tests, migrations, schemas, workflows, and patches.

This skill owns comment policy. `high-constraint-coding` owns bounded implementation. `learn-while-building` owns teaching in chat. Specialized skills own their artifacts. Put rationale in chat unless the fact must live next to the code to prevent a wrong future edit.

Do not activate for read-only explanation, planning, review, or status when no code will be written or shown. If a later turn starts producing code, activate before writing it.

This skill is mutually exclusive with `no-code-comments`. Install only one. If the user explicitly asks for comment-free output, follow that request and do not add comments.

## Comment Kinds

Treat these as different artifacts:

- **Implementation comments**: why this shape exists, what must remain true, what would break if simplified.
- **Documentation comments**: the public or tooling-facing contract: how to call it, valid inputs, side effects, errors. Write them only where the language or repository actually consumes them.
- **Directive comments**: compiler, linter, formatter, generated-file, or license markers required by tooling. Keep them exact and local.

Read [language-conventions.md](./references/language-conventions.md) when the current language's documentation comment form, docstring contract, or directive syntax would change the comment you write.

## Admission Test

Before adding or keeping a comment, it must pass this test:

> Delete it. If a competent reader who knows the language still has the same next-edit decision, it was noise.

A comment earns its place only when it records at least one of:

- why this approach beat the obvious one
- an invariant, unit, range, encoding, ordering, or null/sentinel meaning the type does not carry
- a business, security, protocol, or compatibility constraint with no local structural guard
- a workaround for an external bug, with the upstream issue and the removal condition
- a documentation contract required by public API tooling or the repository
- a required directive, legal header, or generated-file marker

If a clearer name, type, helper, enum, or test would make the comment unnecessary, make that change instead.

## Write These

Keep implementation comments at the point of use, not in a file essay.

Good shapes:

- `Retry twice because the vendor API duplicates ~2% of accepted writes.`
- `Timeout is 5s: upstream p99 is 3.8s plus margin. Do not lower without checking the gateway budget.`
- `Caller must hold the session lock; this method mutates shared cursor state.`
- `Work around https://github.com/nodejs/node/issues/48893; remove when Node >= 22 is required.`
- `Gift-card refunds cap at 24h even when the order still has an expedited window.`

For documentation comments, document use rather than mechanics: inputs, outputs, ownership, nullability, side effects, errors, and restrictions that callers cannot see from the signature. Omit them for obvious accessors, trivial constructors, and overrides that add no new contract.

For `TODO`, include an owner or issue and a removal condition. Do not leave a bare `TODO` or `FIXME`.

## Never Write These

- restatements of the next line, such as increment, loop, return, or import narrations
- comments that copy a literal already in the code (`timeout is 5000` next to `timeout = 5000`)
- section banners, decorative separators, or changelog/authorship notes
- comments that apologize, praise, or say the code is complex
- teaching walkthroughs inside production code; explain in chat unless the user explicitly asked for an annotated tutorial artifact
- guessed constraints, invented ticket numbers, or undocumented public-API fields
- comments that duplicate a test, type, or name that already states the fact

A wrong comment is worse than no comment. If you cannot state the invariant precisely, omit the comment and keep the uncertainty in the response.

## Style

- Write complete sentences unless the repository's local comments are consistently terse.
- Prefer why and constraints over how. How belongs in the code.
- Do not restate names, types, or values the compiler already knows.
- Keep comments adjacent to the constrained code. File-level essays do not steer the next edit.
- Follow the file's existing language, punctuation, and documentation format. Do not mix JSDoc, docstrings, rustdoc, and banner comments in one file.
- Prefer the repository's documentation language. If the file has no convention, write comments in the same language as the surrounding identifiers and existing comments.

## Editing Existing Code

- Do not comment-wash unrelated regions.
- If a touched comment is now false, update or delete it in the same change.
- If replacing a block, rewrite its comments under this skill rather than copying stale narration.
- Preserve required headers, generated markers, and directive comments.
- Do not add documentation comments to private helpers just to look complete.

## Completion

Comment policy is complete when:

- every new or edited comment passes the admission test
- public documentation comments, if required, match evidenced behavior
- no added comment narrates obvious mechanics
- stale comments in the touched area were fixed or removed
- teaching stayed in chat unless the user asked for annotated tutorial code
