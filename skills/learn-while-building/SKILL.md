---
name: learn-while-building
description: "Embed learning into AI-assisted software development without blocking delivery. Use when a user wants to understand the concepts, architecture, decisions, debugging, testing, or engineering tradeoffs involved in an AI-built project; wants AI to act as a tutor while implementing, modifying, or explaining a project; or wants recall, code-tracing, reflection, and transfer exercises alongside coding work."
---

# Learn While Building

## Overview

Use AI as the primary implementation partner while preserving the user's role as an active learner. Identify the knowledge behind the current slice, teach only what is relevant, expose important decisions, and create proportionate opportunities for the user to predict, explain, verify, and reuse what was learned.

## Operating Principles

- Keep project delivery and learning coupled but independently adjustable. Do not withhold complete code when the user needs implementation; add the smallest learning intervention that protects understanding.
- Prefer a short explanation of the system model and decisions over line-by-line narration.
- Ask for active recall before revealing an answer only when the task is important, unfamiliar, or conceptually rich. Do not turn trivial edits into quizzes.
- Teach from the repository and runtime evidence. Do not invent project behavior, undocumented constraints, or unsupported explanations.
- Distinguish facts observed in code or tests, engineering inferences, and recommendations.
- Never pretend that an explanation proves understanding. Use a small prediction, trace, modification, or transfer task when learning evidence matters.
- Respect the user's requested learning intensity:
  - `quiet`: implement normally and provide a compact learning card
  - `guided`: explain the model and key decisions, then ask one or two focused questions
  - `practice`: provide hints first, ask the user to predict or attempt a small step, and reveal the solution progressively
  - `review`: focus on explaining existing code, misconceptions, and transfer
- If the user has not chosen an intensity, use `guided` for unfamiliar or architectural work and `quiet` for mechanical work.

## Workflow

### 1. Establish the learning contract

Before substantial implementation, infer or ask:

- What does the user already know about the relevant stack or concept?
- What does the user want to learn from this slice?
- Which intensity applies: `quiet`, `guided`, `practice`, or `review`?
- Which concepts are essential now, and which should be deferred?

Ask at most one concise question when the answer materially changes the teaching approach. Otherwise choose a sensible default and proceed.

### 2. Map the knowledge behind the slice

Inspect the actual entry point, affected files, tests, configuration, and runtime path. Identify at most three learning targets, prioritizing:

1. concepts necessary to understand the changed behavior
2. decisions that reveal project architecture or engineering tradeoffs
3. reusable knowledge likely to transfer to another task

For each target, state the expected outcome in observable terms, such as “trace the request from route to persistence” or “explain why this state belongs in this module.”

Read [learning-protocol.md](./references/learning-protocol.md) when the task is non-trivial, unfamiliar, architectural, stateful, asynchronous, or debugging-focused.

### 3. Teach at the right moment

- Before implementation: explain the problem model, affected path, and the decision that matters.
- During implementation: explain only non-obvious choices, invariants, boundaries, and failure behavior.
- After implementation: connect the result to tests, runtime evidence, and a likely future change.

For `practice` intensity, use hint-first guidance and let the user attempt a bounded reasoning step before showing the complete implementation. For `quiet`, do not interrupt the implementation with questions.

### 4. Create evidence of learning

Choose one proportionate activity:

- prediction: predict output, control flow, or failure behavior
- trace: follow one input through state changes and boundaries
- explain-back: describe a module, decision, or error in the user's own words
- micro-change: modify a small adjacent behavior
- transfer: apply the concept to a new but related scenario
- debugging: form a hypothesis before inspecting the next evidence

Use [question-patterns.md](./references/question-patterns.md) for prompts. Reveal the answer after the user attempts it, asks to skip, or the task is blocked.

### 5. Produce a learning card

For every bounded behavioral or architectural slice, include a concise learning card:

- `What changed`: the behavior and the path it follows
- `Learn`: one to three relevant concepts
- `Why`: the key design or implementation decision
- `Verify`: the tests or runtime evidence that support the explanation
- `Try`: one recall or transfer prompt, with the answer withheld when appropriate
- `Next`: one useful concept to revisit later, if any

For a mechanical change, compress this to one or two sentences. Do not produce a learning card for a pure explanation unless it improves clarity.

### 6. Maintain project learning context

When the project is expected to continue, maintain a concise learning record only if the repository has an established location for project notes. Otherwise provide the record in the response and ask before creating a new persistent file. Record concepts encountered, the user's demonstrated understanding, important architecture decisions, recurring misconceptions, and open questions.

Use [knowledge-notes.md](./references/knowledge-notes.md) as the format when a persistent record is requested or already exists. Never store secrets, personal data, or unsupported claims.

## Completion Criteria

Consider the learning part complete when:

- the user can locate the changed behavior in the project
- the key concept or decision is explained at the level needed for this task
- the implementation and explanation agree with repository and test evidence
- at least one proportionate opportunity for recall, tracing, explanation, debugging, or transfer was offered for non-trivial work
- the user is told what remains uncertain or worth learning next

Do not measure success by the amount of explanation, number of questions, or refusal to write code. Optimize for useful understanding with minimal interruption to project progress.
