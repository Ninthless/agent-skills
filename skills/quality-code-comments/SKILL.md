---
name: quality-code-comments
description: 'Mandatory comment-quality companion whenever the agent will generate, show, edit, patch, refactor, format, scaffold, or otherwise produce code or a code-like artifact. Always trigger before writing source, snippets, scripts, shell commands, queries, regex, configs, schemas, migrations, tests, fixtures, workflows, Dockerfiles, pseudocode, examples, or proposed patches, including trivial, throwaway, production, and explicitly comment-free requests. Trigger for write, create, generate, implement, fix, modify, refactor, 写代码, 帮我写, 实现, 修一下, 改代码, 重构, 加注释, JSDoc, docstring, and similar delivery work. It governs whether each comment should exist: prefer clear code, preserve required directives and documentation contracts, and add only accurate information the artifact cannot express locally. A no-comments request means zero optional comments; it never disables this skill. Do not trigger for read-only explanation, planning, inspection, diagnosis, status, or review when no code-like content will be produced.'
---

# Quality Code Comments

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Purpose

Govern every comment decision in code-producing work. Activation does not require adding a comment; zero optional comments is often the correct result.

Optimize in this order:

1. verify evidenced behavior and public contracts
2. follow repository conventions when they are tool-valid and consistent with those contracts
3. make names, types, structure, and executable checks carry what they can enforce
4. identify the caller or maintainer knowledge still missing
5. record the smallest accurate statement at the scope that owns that fact
6. update or delete the comment when the code changes

A useful comment reduces the risk or cost of a future misuse, wrong edit, or reverse-engineering step. Do not optimize for comment count, documentation appearance, or line-by-line narration.

## Mandatory Code-Producing Companion

Activate whenever the response will produce, modify, or show code or a code-like artifact, including snippets, configs, tests, migrations, schemas, workflows, commands, queries, regex, Dockerfiles, pseudocode, and patches.

Do not wait for 加注释, 写好注释, JSDoc, docstring, or "add comments". Ordinary coding is enough. This remains true for tiny examples, generated files, and requests that explicitly say 不要注释 or "no comments": activate, then emit zero optional comments.

This skill owns comment policy. `high-constraint-coding` owns bounded implementation. `learn-while-building` owns teaching in chat. Specialized skills own their artifacts. Put rationale in chat unless the fact must live next to the code to prevent a wrong future edit.

Do not activate for read-only explanation, planning, inspection, diagnosis, review, or status only when no code-like content will be written or shown. If a later turn starts producing code, activate before the first artifact.

This skill is mutually exclusive with `no-code-comments`. Install only one. An explicit comment-free request controls the output, not invocation: honor it without adding optional comments or removing unrelated existing comments.

## Comment Kinds

Treat these as different artifacts:

- **Implementation comments**: rationale, invariants, non-local constraints, or an abstraction-level explanation of necessarily low-level code.
- **Documentation comments**: the caller-facing contract: purpose, correct use, valid inputs, outputs, side effects, errors, safety, and restrictions. Write them where the language or repository expects them.
- **Directive comments**: compiler, linter, formatter, generated-file, or license markers required by tooling. Keep them exact and local.
- **Tutorial annotations**: mechanics written for a learner. Use them only when the requested artifact is explicitly educational; do not make production source read like a walkthrough.

Read [language-conventions.md](./references/language-conventions.md) when the current language's documentation comment form, docstring contract, or directive syntax would change the comment you write.

## Evidence Before Prose

Treat every factual claim in a comment as part of the code's correctness:

- Ground it in the current code, tests, types, user requirement, specification, or a durable upstream issue.
- Do not infer a business rule or historical reason from a magic number or unusual branch.
- Do not invent owners, tickets, benchmarks, incidents, compatibility promises, or removal versions.
- Check causality, not just vocabulary. A duplicate-write risk constrains when retries are safe; by itself it does not justify retrying.
- For a workaround, record the affected condition and a concrete removal condition. Link the durable upstream issue when one is known.
- Treat tests as supporting evidence, not as a substitute for caller-facing documentation or a local warning that prevents a wrong edit.

If the evidence is incomplete, improve the code without asserting a reason, ask when the missing fact blocks correctness, or report the uncertainty in chat.

## Admission Test

Before adding or keeping an optional comment, ask:

1. What misuse, wrong edit, or expensive reconstruction does this prevent?
2. Is the information non-obvious at the point of use despite the local names, types, and structure?
3. Is every factual and causal claim supported?
4. Is a comment the right artifact rather than a type, assertion, test, API document, or clearer design?
5. Is it placed at the smallest stable scope that owns the fact?

The comment earns its place when the answers identify real reader value. Documentation and directive comments instead earn their place through the public or tooling contract.

Typical qualifying information includes:

- why this approach beat the obvious one
- an invariant, unit, range, encoding, ordering, or null/sentinel meaning the type does not carry
- a business, security, protocol, or compatibility constraint with no local structural guard
- a concise algorithm or protocol summary when the implementation is necessarily low-level
- a workaround for an external bug, with the upstream issue and the removal condition
- a documentation contract required by public API tooling or the repository
- a required directive, legal header, or generated-file marker

## Write These

Keep implementation comments close to the code they constrain. Put broader invariants at the function, type, or module that owns them.

Good shapes:

- `Retry only with the original idempotency key: the server may commit before the connection drops.`
- `Indices are UTF-8 byte offsets, not Unicode scalar positions.`
- `Caller must hold the session lock; this method mutates shared cursor state.`
- `Use Horner's method here to avoid allocating intermediate powers in this hot path.`
- `Gift-card refunds remain capped at 24h; the standard refund window must not widen them.`

For documentation comments, state caller-observable behavior and correct use. Do not omit a useful purpose summary merely because the signature is typed, but do not repeat types or parameters without adding semantics. Omit documentation that adds nothing to an inherited or repository-defined contract.

For `TODO` or `FIXME`, include a tracked issue or accountable owner when the repository uses them, plus a condition that makes the work actionable or removable. Never fabricate that metadata.

## Never Write These

- restatements of the next line, such as increment, loop, return, or import narrations
- comments that create a second source of truth by copying a literal, type, or signature without adding semantics
- decorative separators, content-free banners, or changelog/authorship notes; preserve semantic headings recognized by documentation tooling
- comments that apologize, praise, warn vaguely, or merely say the code is complex
- teaching walkthroughs inside production code; explain in chat unless the user explicitly asked for an annotated tutorial artifact
- guessed constraints, invented causality, ticket numbers, benchmark results, or undocumented public-API fields
- comments that duplicate a local type or name without independent reader value; a test may verify the same contract for a different audience

A wrong comment is worse than no comment. If you cannot state the invariant precisely, omit the comment and keep the uncertainty in the response.

## Style

- Write complete sentences unless the repository's local comments are consistently terse.
- For implementation comments, prefer rationale and constraints over a translation of mechanics.
- Do not turn "why, not what" into a blind rule. API docs must say what an interface does, and low-level algorithms may need a high-level what/how summary.
- Put the comment at the closest stable scope that owns the information; avoid distant essays and repeated copies.
- Use the language-correct documentation form. Documentation, implementation, and required directive comments may coexist when each serves a distinct contract.
- Follow the file's established punctuation and prose style.

## Comment Language

- Write new or rewritten comment prose in the natural language the user predominantly uses across the current and recent conversation.
- An explicit request for a comment language overrides the inferred conversation language.
- Infer from the user's own prose, not pasted code, quoted material, logs, identifiers, or isolated technical terms.
- For genuinely mixed-language conversation, use the primary natural language of the current request. If that is still unclear, fall back to the repository's established comment language and intended contributor audience.
- Keep identifiers, API and product names, protocol keywords, code tokens, and required directive syntax exact. Translate surrounding prose, not machine-sensitive text.
- Do not translate untouched comments merely for consistency. When a touched comment must be rewritten, use the selected user language.

## Editing Existing Code

- Do not comment-wash unrelated regions.
- If a touched comment is now false, update or delete it in the same change.
- If replacing a block, rewrite its comments under this skill rather than copying stale narration.
- Preserve required headers, generated markers, and directive comments.
- Do not add documentation comments to private helpers just to look complete; document a real non-obvious contract when one exists.
- For an explicit comment-free request, add no optional comments and leave unrelated existing comments alone.

## Completion

Comment policy is complete when:

- this skill was active before every code-like artifact was produced
- every new or edited comment passes the admission test
- every factual claim is supported by the available evidence
- public documentation comments match evidenced behavior and local tooling
- new and rewritten comment prose uses the selected user language
- no added comment narrates obvious mechanics
- stale comments in the touched area were fixed or removed
- explicit comment-free output contains no optional comments
- teaching stayed in chat unless the user asked for annotated tutorial code
