---
name: bug-diagnosis
description: 'Diagnose unknown software defects through symptoms, evidence, falsifiable hypotheses, reproduction, and safe experiments. Use when the user asks to investigate, debug, reproduce, find the root cause, or explain an unexplained crash, wrong response, flaky test, broken UI, or performance regression before repair. Do not trigger for a proven-cause fix or direct source implementation, requirements, API contract work, technical research, or ordinary code review; remain read-only unless separately authorized.'
---
# Bug Diagnosis

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Boundary

Own unknown-root-cause investigation. If the root cause is already demonstrated and the user wants a change, route directly to `high-constraint-coding`. If the user asks to diagnose and fix, finish diagnosis first and hand the evidence to coding.

## Default authorization

Remain read-only. Repository inspection, logs, existing tests, safe reproduction, and non-mutating probes are allowed. Do not edit source, change configuration, install dependencies, mutate external systems, or exploit a security weakness without separate authorization.

## Diagnostic flow

1. Restate the observed symptom, expected behavior, environment, frequency, and impact.
2. Separate direct evidence from reports, assumptions, and missing observations.
3. Trace the relevant execution and data path.
4. Form a small set of falsifiable hypotheses ranked by evidence and reachability.
5. Choose the cheapest discriminating reproduction, log check, test, or controlled experiment.
6. Update hypotheses from results instead of patching around the symptom.
7. State the root cause with confidence and the causal chain only when evidence supports it.
8. Report unproven items, repair direction, regression risks, and a verification plan.

Stop when access, destructive reproduction, sensitive data, or unsafe security testing would be required. Ask for the minimum safe next input.

## Output

Return symptom, evidence, experiments, root cause and confidence, unproven items, fix direction, and verification plan. Never claim that a proposed fix was implemented or verified when only diagnosis occurred.

Read [diagnostic-method.md](./references/diagnostic-method.md) for multi-hypothesis, intermittent, cross-layer, or production-only defects.
