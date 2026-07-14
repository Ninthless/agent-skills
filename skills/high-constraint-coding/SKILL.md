---
name: high-constraint-coding
description: 'Apply a careful, minimal, verified workflow to correctness-sensitive coding work. Use for bug fixes, refactors, code reviews, production edits, shared contracts, tests, migrations, or regression-prone behavior, and for requests such as 最小改动, 高质量代码, 别乱重构, 先看清楚再改, read the code first, or guarantee correctness. Trigger when implementation or review requires controlled scope, local style matching, and evidence before claiming success. Do not use for pure conceptual questions, status reporting, or non-code planning with no source review or code change.'
---

# High Constraint Coding

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Triggers

- The user asks for a bug fix, refactor, code review, or implementation that must be correct.
- The task touches production code, shared behavior, contracts, tests, or regression-sensitive logic.
- The user wants minimal diffs, explicit assumptions, and practical verification.
- The user says `最小改动`, `高质量代码`, `别乱重构`, `先看清楚再改`, `先读代码`, `不要乱改`, or `保证正确`.
- The request implies careful engineering rather than quick speculative changes.

## Overview

Use this skill to force a disciplined coding workflow that reduces the usual LLM failure modes: guessing unclear requirements, changing too much code, inventing abstractions, skipping verification, and shipping patches with hidden regressions.

Optimize for correct behavior, code that humans can quickly understand and safely change, and the smallest clear implementation that satisfies the task. Do not optimize for speed if speed would weaken rigor.

## Priority Order

When tradeoffs appear, resolve them in this order:

1. correctness
2. clarity and maintainability
3. local extensibility
4. performance
5. brevity

Use brevity only when the result stays obvious to another engineer. Use performance work only when it is required by the task, supported by evidence, or clearly necessary on a hot path.

## Operating Contract

Treat every coding request as a bounded engineering task with a quality bar.

- Define the concrete task before editing code.
- Surface assumptions that can change behavior, interfaces, data shape, persistence, or user-visible output.
- Prefer the smallest direct implementation that satisfies the request.
- Avoid speculative refactors, generic frameworks, or future-proofing unless the current task requires them.
- Keep changes local to the relevant files and lines.
- Verify the change with the strongest practical evidence before finishing.
- Prefer code that another engineer can understand, modify, and extend without reverse-engineering hidden intent.

If the request is trivial, keep the process lightweight. If the request is ambiguous or risky, tighten the process rather than improvising.

## Required Workflow

### 1. Bound the task

Before coding, identify:

- the exact behavior to add, fix, or preserve
- the files or modules likely involved
- the validation target
- the assumptions that matter

If multiple interpretations would lead to materially different implementations, stop and ask a concise question instead of silently choosing one.

### 2. Read before writing

**This step is mandatory. Do not skip it even for small changes.**

Inspect the real implementation path before proposing changes.

- find the entry point, call chain, and affected data flow
- identify any shared helper, normalization rule, or contract that multiple call sites depend on
- check adjacent tests, types, interfaces, schemas, or configuration
- notice existing patterns and follow them unless they are the problem
- read the actual file content, not a remembered or guessed version

**Before writing a single line of code, state in one sentence what the current code does in the relevant area.** If you cannot produce that sentence confidently, keep reading. A vague or hedged description means the understanding is not yet sufficient to make a safe change.

Do not start from a guessed implementation shape.
If the visible bug is downstream from a shared semantic seam, fix the seam rather than only patching the leaf caller.

**If you have already tried a fix twice and it is still failing:** stop patching. Diagnose the root cause from the evidence you have. Explain what went wrong and propose a fundamentally different approach before writing more code.

### 3. Choose the narrowest solution

Select the lowest-complexity change that fully solves the task.

- prefer extending an existing path over introducing new layers
- prefer direct logic over abstractions used once
- prefer explicit control flow over compact cleverness
- prefer preserving public contracts over broad rewrites
- prefer simple seams over speculative extension systems

Reject changes that are larger than the problem.
Do not mistake a local-looking call-site patch for the narrowest solution if it leaves sibling paths inconsistent.

### 3a. Preserve human understandability

Code should be easy for a competent engineer to read in one pass.

- make the happy path easy to follow
- keep important state transitions visible
- avoid hiding business logic inside dense helpers, chained transforms, or clever expressions
- use names that explain the role of a value, not just its type
- keep functions focused enough that their job is obvious

If a shorter version is harder to read, choose the slightly longer version.

### 3c. Mirror the local style

Before writing, identify 3–5 concrete style patterns in the surrounding code and carry them into your change. Look for:

- naming conventions: casing, prefixes, verb vs noun choices, abbreviation habits
- control flow preferences: early return vs nested if, guard clauses vs else branches
- error handling shape: exceptions vs result types vs sentinel values
- function length and decomposition granularity
- how the codebase expresses intent: inline logic vs named helpers, explicit vs implicit

A change that is correct but stylistically foreign reads as AI-written. A change that blends in reads as human-written. The goal is the latter.

If the surrounding style is inconsistent, follow the pattern used in the most recently touched or most closely adjacent code.

### 3b. Preserve local extensibility

Write code that can be changed safely when nearby requirements evolve, without building a speculative framework.

- isolate task-specific logic behind clear boundaries when the code already has those boundaries
- keep interfaces stable unless changing them is necessary
- avoid coupling unrelated concerns into one function or component
- leave a natural place for the next likely change
- do not generalize for imaginary future cases

Good extensibility means low-friction modification of the local area, not building a reusable platform.

### 4. Implement with hard constraints

While editing:

- change only what is required for the task
- do not rewrite unrelated code for style
- do not rename unrelated symbols
- do not mix bug fixes with opportunistic cleanup
- remove any import, branch, helper, or test made obsolete by your own change
- preserve existing comments unless the touched comment becomes incorrect

When writing code, bias toward:

- obvious names
- simple data flow
- short functions with one job
- direct error handling
- stable interfaces
- linear control flow when practical
- a small number of moving parts

Avoid patterns that often make AI-written code worse:

- nested ternaries for multi-branch behavior
- one-liners that compress multiple transformations and hide intent
- wrapper abstractions with only one caller
- generic utilities introduced only to avoid writing a few explicit lines
- premature caching, memoization, batching, or async complexity without evidence

## Performance Rule

Aim for code that is efficient enough for the real workload while staying easy to reason about.

- preserve existing performance-critical behavior unless the task requires changing it
- optimize when there is evidence, a known hot path, or an explicit performance goal
- prefer the simplest efficient approach over clever micro-optimizations
- explain any readability tradeoff made for performance
- if performance is uncertain and important, say what should be measured

Do not sacrifice maintainability for hypothetical performance wins.

### 5. Verify before claiming success

Run the strongest practical verification available.

Preferred order:

1. targeted tests that prove the changed behavior
2. nearby regression tests
3. typecheck, build, lint, or static analysis
4. manual reproduction steps when automated checks are unavailable

If the fix touches shared logic, do not stop at the first passing symptom test. Run at least one adjacent contract or regression check that exercises another consumer of the same seam when practical.
If verification cannot be run, say so explicitly and explain what remains unproven.

### 6. Report like an engineer

Final output should be concise and concrete:

- what changed
- how it was verified
- what assumptions or residual risks remain

Do not over-explain implementation details unless the user asks.

## Strict Do Nots

Do not:

- infer missing requirements when the risk of being wrong is meaningful — ask instead
- introduce dependencies, configuration toggles, or reusable frameworks for one-off logic
- claim a fix without testing or a credible reproduction path
- bury uncertainty behind confident language or leave partially implemented ideas in the patch
- confuse minimal diff with minimal understandable solution — the goal is the latter

## Review Mode

When the user asks for a review, prioritize findings over summaries.

- report correctness bugs first
- then regression risk, missing validation, unsafe assumptions, and needless complexity
- pay extra attention to removed guards, changed normalization semantics, caller-owned mutation, ordering rules, and missing coverage around the modified behavior
- include file and line references when possible
- state explicitly if no findings were found

## Decision Rules

Use these rules to keep the skill sharp:

- If the task is unclear, ask.
- If the change is broad, shrink it.
- If the code is clever, simplify it.
- If the verification is weak, strengthen it.
- If the patch includes unrelated edits, remove them.
- If a shorter implementation is less obvious, expand it slightly.
- If extensibility requires a framework, it is probably overdesigned.
- If performance work lacks evidence, defer it or state it as a risk rather than implementing it.

## Quality Bar

Read [quality-bar.md](./references/quality-bar.md) when you need a stricter checklist for deciding whether a patch is actually good enough to ship.

## Example Response Shape

For non-trivial coding tasks, use this internal sequence:

1. Scope the task and state material assumptions.
2. Inspect the relevant code path and tests.
3. Implement the smallest viable change.
4. Run targeted verification.
5. Report outcome, evidence, and residual risk.

For simple tasks, compress the same logic into a shorter execution path without skipping the underlying discipline.
