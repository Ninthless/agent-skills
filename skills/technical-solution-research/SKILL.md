---
name: technical-solution-research
description: 'Research current technical solutions using evidence about libraries, frameworks, protocols, standards, versions, compatibility, and operational constraints. Use when the requested result is a bounded technical recommendation, compatibility finding, migration choice, or evidence-backed comparison that includes keeping the current approach when viable. Separate facts, inferences, options, and recommendation, and use a bounded spike only when documents cannot resolve a decisive uncertainty. Do not implement, perform business-domain discovery, or manufacture multiple options for a single factual answer.'
---
# Technical Solution Research

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Ownership

Own current technical evidence and solution decisions. `vibecoding-domain-scout` owns industry workflows, policy, compliance, and business rules. `requirement-analysis` owns the working contract. `high-constraint-coding` owns implementation.

## Research flow

1. Define the decision, constraints, current state, and required evidence freshness.
2. Inspect project versions and compatibility boundaries when available.
3. Prefer primary documentation, specifications, release notes, and maintained project evidence.
4. Answer a single factual question directly when comparison is unnecessary.
5. For a real decision, compare a limited set of viable options including the status quo when it remains viable.
6. Separate verified evidence, inference, uncertainty, and recommendation.
7. Evaluate fit, compatibility, migration cost, operational burden, reversibility, security, and maintenance only where relevant.
8. Recommend one option or state why evidence is insufficient.

A bounded spike is allowed only to resolve a decisive uncertainty that documentation and existing evidence cannot answer. Define its question, limit, success signal, cleanup, and non-production nature before execution. Do not turn a spike into implementation.

## Output

Provide the decision, constraints, evidence with versions or dates when relevant, options if needed, recommendation, trade-offs, uncertainties, and next verification step. Never imply the recommendation has been implemented.

Read [evidence-and-decision.md](./references/evidence-and-decision.md) for version-sensitive decisions, migrations, or bounded spikes.
