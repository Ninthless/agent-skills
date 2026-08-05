---
name: english-spec-first
description: 'Normalize rough, mixed-language, or materially ambiguous requirements into a concise English working contract before planning or implementation. Use when the user asks for an English spec, says think in English first, requests requirement normalization, or provides messy notes needing scope clarification. Distinguish a user-visible display spec from internal normalization. Do not use for simple translation, proofreading, final specifications, or clear direct implementation requests.'
---
# English Spec First

## Output modes

- `display-spec`: use only when the user explicitly asks to see an English spec, brief, normalized prompt, or rewritten requirements. Show a compact English contract before the requested follow-up work.
- `internal-normalization`: when the user only says to think in English first, normalize privately and deliver the requested result directly in the user's language. Do not expose an intermediate spec.

If material ambiguity requires confirmation, show only the minimum working contract needed to frame the decision, then ask the focused question. A request such as “think in English first, but do not show the intermediate spec” always uses internal normalization unless a blocking ambiguity requires that minimum contract.

## Working contract

Capture the goal, provided inputs, hard constraints, required output, material assumptions, and unresolved decisions. Preserve names, files, metrics, APIs, technologies, and deadlines. Separate requirements from preferences and assumptions. Do not invent detail for completeness.

Ask only when different answers would materially change behavior, interfaces, scope, or acceptance. Otherwise proceed with a labeled internal assumption.

When a display spec is requested, prefer compact engineering English using `Goal`, `Inputs`, `Constraints`, `Output`, and optional `Open Decisions`. Return only the normalized spec when that is the sole deliverable. Do not expose private reasoning.
