---
name: requirement-analysis
description: 'Turn rough, mixed-language, conflicting, or incomplete notes into a bounded requirement contract. Use when the user asks to clarify or organize requirements, define scope, resolve contradictions, write FR/NFR, acceptance criteria, a spec, or an implementation handoff, including webpage requirements without code changes. Do not trigger for clear implementation, source changes, unknown-bug diagnosis, API documentation, missing business-domain research, framework/version choices, or UI copy translation only.'
---
# Requirement Analysis

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Ownership

Own the requirement contract when the requested result is clarified scope and acceptance. Do not take over clear implementation, root-cause diagnosis, API contract authoring, domain research, or technical solution selection.

## Modes

- `working-contract`: produce the smallest complete contract needed for planning or implementation.
- `display-spec`: when the user explicitly requests an English spec, show the contract in concise engineering English.
- `internal-normalization`: when asked to think in English without displaying it, normalize privately and answer in the requested language.

## Method

1. Identify goal, actors, inputs, outputs, and current evidence.
2. Separate Scope and Out of Scope.
3. Classify explicit requirements as ER and inferred requirements as IR.
4. Separate constraints, preferences, and assumptions.
5. Surface contradictions and decisions that materially change behavior.
6. Organize functional and non-functional requirements.
7. Write testable acceptance criteria with observable outcomes.
8. Record dependencies, risks, unresolved decisions, and implementation handoff.

Ask only questions whose answers materially change scope, interfaces, data, safety, or acceptance. Never invent facts to make the contract look complete.

## Authorization and handoff

Analysis is read-only unless the user separately authorizes artifact edits. Hand off missing business or regulated facts to `vibecoding-domain-scout`, current library or protocol choices to `technical-solution-research`, API contract production to `write-api-docs`, and source implementation to `high-constraint-coding`.

Read [working-contract.md](./references/working-contract.md) when the request needs a full contract, conflict resolution, or implementation handoff.
