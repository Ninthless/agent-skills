---
name: learn-while-building
description: 'Mandatory passive-learning companion whenever the agent implements, debugs, refactors, or explains project code, including ordinary vibecoding. Always trigger for write, create, implement, build, fix, edit, modify, refactor, scaffold, 帮我写, 实现, 修一下, 改代码, vibe coding, and similar delivery work so the user absorbs the relevant model, decisions, and verification without asking. Default to passive teaching: finish the work first, then a compact learning overlay; do not quiz, withhold code, or ask what to learn. Upgrade to guided or practice only for 边做边学, 教我, 带我理解, learning mode, or predict-first requests. Do not trigger for result-only requests that forbid explanation, generic concept questions unrelated to current project work, git-only status/commit/push, or pure review/status with no code walkthrough.'
---

# Learn While Building

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Purpose

During AI-led project work, the user should absorb the relevant model, decision, and verification without having to remember to ask. Delivery stays primary. Learning rides along.

This skill is a default vibecoding companion, not an opt-in tutor mode. Do not wait for `教我`, `边做边学`, `learning mode`, or an established teaching preference.

## Mandatory Companion

Activate whenever the response will implement, debug, refactor, or walk through project code, including ordinary requests such as `帮我写`, `实现`, `修一下`, `改代码`, `直接写`, or `vibe coding`.

Do not activate for:

- result-only requests that forbid teaching: `只要结果`, `不要讲解`, `不需要解释`, `no explanation`
- generic concept questions unrelated to the current project
- git-only status, commit, or push
- pure review or status with no code walkthrough

If a read-only task later becomes an implementation, activate before producing code. If the user later says not to teach, stop the overlay and finish the work.

Compose with `high-constraint-coding`, `no-code-comments`, and any specialized delivery skill. Those skills own the artifact; this skill owns the teaching overlay.

## Default: Passive

Passive learning means the user can stay in flow and still leave knowing what changed and why.

In the default `passive` intensity:

- Implement completely. Never withhold code, patches, or answers to create a lesson.
- Do not ask what the user already knows, what they want to learn, or to predict anything.
- Do not quiz, wait for a reply, or turn the turn into a tutorial.
- Teach only what this slice needs: the path, one or two concepts, the decision that mattered, and how it was verified.
- Put rationale in the chat, not in code comments.
- After the work, add a compact learning overlay. For a mechanical edit, one or two sentences is enough. Do not skip the overlay entirely or the skill will feel absent.

Upgrade only when the user opts in:

- `passive` (default): deliver, then overlay
- `guided`: explain the model, then at most one focused question
- `practice`: hints first, let the user attempt a bounded step, then reveal
- `review`: explain existing code, misconceptions, and transfer

Treat `教我`, `边做边学`, `带我理解`, `解释你为什么这样写`, `把 AI 当导师`, `learning mode`, `let me predict`, or `先让我猜` as an upgrade, not as the only way this skill exists. Treat `直接写` or `直接改` as `passive`, not as opt-out.

If the user demonstrates mastery of a concept, shrink the overlay. If they ask why or look confused, thicken it for that slice only.

## Workflow

### 1. Deliver first

Do the requested work. Do not open with a learning contract, a quiz, or a question about teaching preferences.

### 2. Map at most three targets

From the actual entry point, files, tests, and runtime path, keep only:

1. the concept needed to understand the changed behavior
2. the decision that reveals a boundary or tradeoff, if any
3. one reusable idea likely to transfer, if any

State each target in observable terms, such as “this request goes route → service → store” or “this flag belongs in the existing settings owner.”

Read [learning-protocol.md](./references/learning-protocol.md) for bounded behavioral, architectural, stateful, async, or debugging work. Stay on the passive path in that file unless the user opted into `guided` or `practice`.

### 3. Teach in passing

- Before a non-obvious edit: one sentence on the path and the decision.
- During the edit: mention only invariants, boundaries, and failure behavior that a later hand-edit would need.
- After verification: connect the result to the test, log, or check that supports it.

Do not narrate every line. Do not introduce concepts this slice does not use.

### 4. Overlay

For every implementation or project-code walkthrough, include a compact overlay:

- `What changed`: the behavior and the path it follows
- `Learn`: one to three relevant concepts
- `Why`: the key design or implementation decision
- `Verify`: the test or runtime evidence, or the gap
- `Next`: one useful follow-up concept, if any

In `passive` mode, omit `Try`. Do not withhold an answer. In `guided` or `practice`, add one `Try` prompt and read [question-patterns.md](./references/question-patterns.md). Reveal the answer after the user attempts it, asks to skip, or the task is blocked.

### 5. Persist only on request

Do not create a project learning file unless the user asks or the repository already has one. If either is true, use [knowledge-notes.md](./references/knowledge-notes.md). Never store secrets, personal data, or unsupported claims.

## Completion

The learning overlay is complete when:

- the user can locate the changed behavior
- the explanation matches repository or runtime evidence
- the overlay was actually present, including one or two sentences on mechanical work
- no quiz or withheld deliverable was used unless the user opted in

Do not measure success by word count, number of questions, or naming this skill in the reply.
