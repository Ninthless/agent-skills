---
name: high-constraint-coding
description: 'Apply a careful, minimal, verified workflow to correctness-sensitive source-code review and code changes. Use for production bug fixes, refactors, shared contracts implemented in source, migrations, regression-sensitive features, and reviews that require tracing callers, state, persistence, outputs, and tests. Do not trigger for API documentation creation or review, requirement normalization, Git checkpoint/message/push work, pure conceptual questions, or planning with no source review or code change; those specialized skills lead unless correctness work on implementation source is also requested.'
---

# High Constraint Coding

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Triggers

- The user asks for a bug fix, refactor, code review, or implementation that must be correct.
- The task touches production code, shared behavior, contracts, tests, or regression-sensitive logic.
- The user wants minimal diffs, explicit assumptions, and practical verification.
- The user says `最小改动`, `高质量代码`, `不要 AI 味`, `像人工写的`, `别乱重构`, `先看清楚再改`, `先读代码`, `不要乱改`, or `保证正确`.
- The request implies careful engineering rather than quick speculative changes.
- API documentation review, requirement normalization, and Git checkpoint work are led by their specialized skills unless the request also includes correctness-sensitive source review or code changes.

## Overview

Use this skill to force a disciplined coding workflow that reduces the usual LLM failure modes: guessing unclear requirements, changing too much code, inventing abstractions, skipping verification, and shipping patches with hidden regressions.

Optimize for correct behavior, project-native coherence, code that humans can quickly understand and safely change, and the smallest complete implementation that satisfies the task. Do not optimize for speed if speed would weaken rigor.

Do not treat "human-written" as a cosmetic style or detector-evasion target. Produce code whose every choice is justified by the requirement, an established project convention, a real caller, or measured evidence. Never claim that code is AI-free or infer authorship from style, commit size, or public-code search.

## Priority Order

When tradeoffs appear, resolve them in this order:

1. correctness
2. contract and feature coherence
3. project-native consistency
4. clarity and maintainability
5. verification strength
6. local extensibility
7. performance
8. brevity

Use brevity only when the result stays obvious to another engineer. Use performance work only when it is required by the task, supported by evidence, or clearly necessary on a hot path.

## Operating Contract

Treat every coding request as a bounded engineering task with a quality bar.

- Define the concrete task before editing code.
- Surface assumptions that can change behavior, interfaces, data shape, persistence, or user-visible output.
- Prefer the smallest direct implementation that satisfies the request.
- Avoid speculative refactors, generic frameworks, or future-proofing unless the current task requires them.
- Keep changes local to the relevant files and lines.
- Make every new field, state, branch, abstraction, endpoint, index, and configuration entry earn its place through a current requirement or real consumer.
- Keep validation, defaulting, normalization, nullability, persistence, and state transitions coherent across every touched layer.
- Deliver a complete requested slice rather than a broad but half-connected scaffold.
- Verify the change with the strongest practical evidence before finishing.
- Prefer code that another engineer can understand, modify, and extend without reverse-engineering hidden intent.

If the request is trivial, keep the process lightweight. If the request is ambiguous or risky, tighten the process rather than improvising.

## Required Workflow

### 1. Bound the task

Before coding, identify:

- the exact behavior to add, fix, or preserve
- the files or modules likely involved
- the complete affected behavior path: entry point, contracts, decisions, state, outputs, consumers, and tests as applicable
- the validation target
- the assumptions that matter

If multiple interpretations would lead to materially different implementations, stop and ask a concise question instead of silently choosing one.

### 2. Read before writing

**This step is mandatory. Do not skip it even for small changes.**

Inspect the real implementation path before proposing changes.

- find the entry point, call chain, and affected data flow
- identify any shared helper, normalization rule, or contract that multiple call sites depend on
- check adjacent tests, types, interfaces, schemas, or configuration
- inspect analogous completed features, not only the nearest file, to learn the project's actual conventions
- inspect relevant history or blame when it clarifies why a convention or invariant exists; never manufacture commit history to imitate human development
- read the actual file content, not a remembered or guessed version

**Before writing, pass an internal readiness gate:** be able to state precisely what the current code does, which callers and contracts are affected, and what evidence supports the change. Keep reading if that statement would be vague. Share it with the user only when confirmation is needed for a material assumption or ambiguity.

Do not start from a guessed implementation shape.
If the visible bug is downstream from a shared semantic seam, fix the seam rather than only patching the leaf caller.

**If you have already tried a fix twice and it is still failing:** stop patching. Diagnose the root cause from the evidence you have. Explain what went wrong and propose a fundamentally different approach before writing more code.

### 2a. Build a contract map

For non-trivial behavior, map the touched slice before implementation:

- entry points and callers
- request, input type, schema, and validation rules
- defaulting, normalization, and null semantics
- service or domain decisions
- domain model, storage schema, index, migration, and persistence behavior
- response, event, UI, and downstream consumers
- tests, fixtures, docs, and operational claims

Choose one authoritative boundary for each invariant. Do not validate a value as mandatory at one boundary and also add an unreachable fallback for its absence downstream without a real bypassing caller. Do not let two layers silently assign different defaults or meanings.

Mark pre-existing gaps as `in scope`, `out of scope`, or `blocking`. Do not invent unrelated functionality merely to make an existing schema look complete.

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

### 3b. Mirror the local style

Before writing, identify 3–5 concrete style patterns in analogous, maintained code and carry them through the entire feature slice. Look for:

- naming conventions: casing, prefixes, verb vs noun choices, abbreviation habits
- control flow preferences: early return vs nested if, guard clauses vs else branches
- error handling shape: exceptions vs result types vs sentinel values
- function length and decomposition granularity
- how the codebase expresses intent: inline logic vs named helpers, explicit vs implicit
- dependency wiring, transaction, pagination, mapping, validation, concurrency, and test conventions where applicable

A change that is correct but conventionally foreign is harder for maintainers to trust and extend. Make new code look native to the project because it follows its actual engineering decisions, not because it imitates superficial syntax.

If the repository is inconsistent, choose in this order: enforced tooling or architecture rules, the convention used by analogous maintained modules, then the dominant recent pattern. Use one coherent convention across the new slice. Do not mix styles within the feature, and do not clean up unrelated legacy inconsistencies.

### 3c. Preserve local extensibility

Write code that can be changed safely when nearby requirements evolve, without building a speculative framework.

- isolate task-specific logic behind clear boundaries when the code already has those boundaries
- keep interfaces stable unless changing them is necessary
- avoid coupling unrelated concerns into one function or component
- leave a natural place for the next likely change
- do not generalize for imaginary future cases

Good extensibility means low-friction modification of the local area, not building a reusable platform.

### 3d. Close the requested feature slice

Treat completeness as traceable behavior, not file count.

- connect every requested action from caller to outcome and recovery path
- give every new persisted field, enum, status, or index a current producer, consumer, lifecycle, or explicit domain requirement
- keep request validation, service behavior, stored data, returned data, and UI behavior aligned
- include the targeted test level supported by the repository for new behavior
- update documentation or completion claims only when the implementation proves them

Do not generate administrator workflows, CRUD endpoints, states, or UI merely because an entity could support them. If they are not requested, omit their supporting schema when newly introduced and unnecessary. If they already exist, report the gap without expanding scope unless it blocks correctness.

### 3e. Run an intentionality audit

Before editing and again before completion, ask of every introduced artifact: why does this exist now, who calls or consumes it, and what evidence supports this shape?

Remove or reject:

- defensive defaults or null guards made unreachable by upstream validation and real call paths
- input, domain, persistence, transport, service, or presentation layers created only by template symmetry
- unused fields, statuses, indexes, extension hooks, configuration, or generic base types added for imagined future work
- catch-and-rethrow wrappers, redundant conversions, and pass-through helpers that add no policy
- broad README, architecture, or completion claims not demonstrated by working code

Defensive code is valid when it protects a real boundary or alternate caller. Name that boundary in the design reasoning and test it.

### 4. Implement with hard constraints

While editing:

- change only what is required for the task
- do not rewrite unrelated code for style
- do not rename unrelated symbols
- do not mix bug fixes with opportunistic cleanup
- remove any import, branch, helper, or test made obsolete by your own change
- preserve existing comments unless the touched comment becomes incorrect
- keep all new files in the slice consistent with the selected project conventions
- remove scaffolding, placeholder branches, and unused artifacts introduced by the change

When writing code, bias toward:

- obvious names
- simple data flow
- short functions with one job
- direct error handling
- stable interfaces
- linear control flow when practical
- a small number of moving parts

Avoid patterns that weaken project-native quality:

- nested ternaries for multi-branch behavior
- one-liners that compress multiple transformations and hide intent
- wrapper abstractions with only one caller
- generic utilities introduced only to avoid writing a few explicit lines
- premature caching, memoization, batching, or async complexity without evidence
- blanket null handling, fallback values, or exception wrapping without a reachable case
- full CRUD or multi-layer boilerplate generated by entity shape rather than requested behavior

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

1. targeted tests that prove the changed behavior and contract boundaries
2. integration or end-to-end checks for a changed vertical slice
3. nearby regression tests
4. typecheck, build, lint, or static analysis
5. manual reproduction steps when automated checks are unavailable

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
- keep contradictory validation, defaults, or state semantics across layers
- add dormant schema, statuses, indexes, endpoints, or abstractions for hypothetical future work
- mix injection, mapping, error handling, pagination, or test conventions inside one new feature slice
- generate every architectural layer or CRUD operation merely for symmetry
- claim a fix without testing or a credible reproduction path
- bury uncertainty behind confident language or leave partially implemented ideas in the patch
- confuse minimal diff with minimal understandable solution — the goal is the latter
- claim code is human-written, AI-free, copied, or AI-generated from stylistic clues, commit size, or search results

## Review Mode

When the user asks for a review, prioritize findings over summaries.

- report correctness bugs first
- then regression risk, missing validation, unsafe assumptions, and needless complexity
- pay extra attention to removed guards, changed normalization semantics, caller-owned mutation, ordering rules, and missing coverage around the modified behavior
- trace contradictions between validation, service defaults, persistence states, UI affordances, and documentation
- distinguish maintainability evidence from provenance speculation; code search can reveal duplication but cannot prove authorship or absence of AI use
- include file and line references when possible
- state explicitly if no findings were found

## Decision Rules

Use these rules to keep the skill sharp:

- If the task is unclear, ask.
- If the change is broad, split it into coherent verified slices without leaving the requested behavior half-wired.
- If two layers own the same invariant, choose one authoritative boundary.
- If a new field or state has no current lifecycle, remove it or obtain a requirement.
- If a requested slice is incomplete, finish the slice before adding adjacent features.
- If local conventions conflict, choose one evidence-backed convention for the new slice and leave unrelated cleanup alone.
- If the code is clever, simplify it.
- If the verification is weak, strengthen it.
- If the patch includes unrelated edits, remove them.
- If a shorter implementation is less obvious, expand it slightly.
- If extensibility requires a framework, it is probably overdesigned.
- If performance work lacks evidence, defer it or state it as a risk rather than implementing it.

## Quality Bar

Read [quality-bar.md](./references/quality-bar.md) before completing any non-trivial implementation or review. Treat its project-native coherence gate as required, not optional.

## Example Response Shape

For non-trivial coding tasks, use this internal sequence:

1. Scope the task and state material assumptions.
2. Inspect the relevant code path and tests.
3. Implement the smallest viable change.
4. Run targeted verification.
5. Report outcome, evidence, and residual risk.

For simple tasks, compress the same logic into a shorter execution path without skipping the underlying discipline.
