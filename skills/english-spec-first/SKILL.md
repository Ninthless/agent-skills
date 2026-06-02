---
name: english-spec-first
description: 'Use when a request is rough, multilingual, mixed Chinese-English, ambiguous, emotional, scattered, or needs precise execution; triggers include think in English first, standard English spec, request normalization, 先用英文, 先整理需求, 把需求变专业. First rewrite the user request into a compact English specification before planning, coding, writing, analysis, implementation, or decision making.'
when_to_use: 'Use when the user wants a messy, multilingual, vague, or rough request normalized before execution. Also use when the user asks to think in English first, turn an idea into a professional English spec, or clarify requirements before planning.'
---

# English Spec First

## Triggers

- The user asks to think in English first before solving.
- The request is rough, scattered, multilingual, or ambiguous.
- The user wants a professional English specification from messy notes.
- The task needs requirements clarified before planning or execution.
- The user says `先用英文`, `先整理需求`, `把需求变专业`, `整理成英文需求`, or `中英混合`.

## Overview

Convert the user's raw request into a clean English specification first. Use that specification as the working contract for reasoning, planning, coding, writing, or analysis, then respond in the user's language unless they ask for a different output language.

## Operating Rule

Do not begin implementation, planning, or detailed analysis directly from the raw request when this skill is active.

Always do the work in this order:

1. Parse the user's actual intent, constraints, and desired output.
2. Rewrite that understanding into a standard English specification.
3. Check the English specification for missing requirements, contradictions, and hidden assumptions.
4. Use the English specification as the basis for the actual reasoning and execution.
5. Return the user-facing answer in the user's language unless the user explicitly wants English.

## English Specification Standard

Write the English specification as a short, strict working brief. Prefer clear engineering English over polished prose.

Use this structure whenever enough information is available:

- `Goal:` the end state or outcome
- `Inputs:` source material, context, files, or assumptions provided by the user
- `Constraints:` hard limits, preferences, forbidden approaches, quality bar, format rules
- `Output:` what must be produced
- `Process Notes:` any critical interpretation needed to avoid mistakes

If some sections are unknown, keep them brief and explicit:

- `Constraints: Not explicitly provided; preserve existing behavior and avoid unnecessary assumptions.`
- `Output: Final deliverable not fully specified; infer the most practical default and state it.`

## Normalization Rules

Apply these rules while rewriting the request:

- Convert vague verbs into operational verbs when the intent is clear.
- Convert subjective phrases into observable standards when possible.
- Preserve named entities, file names, metrics, APIs, technologies, and deadlines exactly.
- Separate hard requirements from inferred preferences.
- Remove filler, repetition, and emotional wording unless it changes meaning.
- Do not invent requirements just to make the spec look complete.
- If the request is underspecified in a way that changes the result, say so explicitly instead of guessing silently.

## Clarification Rule

If a missing detail is blocking correct execution, ask a short clarification question before continuing.

If the missing detail is not blocking, proceed with a clearly labeled assumption inside the English specification.

Do not ask broad discovery questions when a reasonable default exists.

## Response Pattern

When the user is asking for real work rather than meta-discussion, use this response shape:

1. `Standard English Spec`
2. `Execution` or the requested deliverable
3. `Assumptions` only when needed

Keep the `Standard English Spec` compact. It is a working contract, not a long essay.

If the user explicitly asks for only the normalized English request, return only that plus essential assumptions or questions.

## Hidden Reasoning Boundary

Use the standardized English specification as the internal frame for reasoning. Do not expose chain-of-thought or private deliberation. Show only the specification, necessary assumptions, and the final useful output.

## Example Transformations

**Example 1**

User request:
`你帮我把这个需求整理一下，我要做一个后台，先别急着写代码，用户管理、权限、日志都要有，后面可能要接飞书。`

Standard English Spec:
`Goal: Define a backend admin system scope before implementation. Inputs: User requests an admin platform with user management, permissions, and logs, and may integrate Feishu later. Constraints: Do not start coding yet. Preserve room for later Feishu integration. Output: A structured scope definition and implementation plan. Process Notes: Treat Feishu integration as a future extension, not an immediate requirement.`

**Example 2**

User request:
`把我这个想法变专业一点再回答，我想做个页面，大概高级一点，别土，要快。`

Standard English Spec:
`Goal: Design and implement a polished page. Inputs: User wants a fast-delivered page with a premium visual tone. Constraints: Avoid generic or low-quality styling. Prioritize speed without sacrificing baseline design quality. Output: A professional page proposal or implementation. Process Notes: "高级一点" implies a refined, intentional aesthetic rather than excessive decoration.`

## Quality Bar

The rewritten English specification should be:

- shorter than the raw request when possible
- more precise than the raw request
- faithful to the user's intent
- strong enough that another capable agent could execute from it with minimal ambiguity
