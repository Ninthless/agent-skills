---
name: vibecoding-domain-scout
description: 'Research unfamiliar industry workflows, business rules, regulation, compliance, roles, operational exceptions, or expert terminology before product scope or build. Use when the user asks how a real domain such as pharmacy, insurance, finance, education, or platform policy works and the findings must shape a product. Do not trigger for pure UI or webpage implementation, framework or library research, technical solution selection, requirements based on known facts, or generic market summaries.'
---
# Vibecoding Domain Scout

## Modes

Choose from the user's requested outcome:

- `research-only`: provide sourced facts, terminology, actors, workflows, constraints, uncertainties, and validation needs. Do not add an MVP or AI Build Brief unless requested.
- `product-discovery`: add hidden requirements, high-leverage questions, risks, success criteria, and an MVP only when useful to the product decision. Do not generate an AI Build Brief.
- `build-handoff`: produce the relevant research and discovery outputs, an evidence-based MVP when needed, and a concise AI Build Brief with workflow, data, states, edge cases, acceptance, assumptions, and non-goals.

## Research contract

Use current primary sources for unfamiliar, regulated, safety-critical, financial, legal, medical, educational, privacy, identity, platform-policy, or time-sensitive claims. If browsing is unavailable, state that and label the result assumption-based. Separate verified facts, inferences, assumptions, and items requiring professional or user validation. Keep auditable source links.

Map only what serves the selected mode: users and roles, real workflow, inputs, decisions and outputs, rules, timing, permissions, failure and recovery, sensitive data, and success criteria. Ask at most five questions that materially affect workflow, scope, validation, risk, or data. Do not default to dashboards, auth, payments, admin panels, analytics, or broad automation.

For product discovery or build handoff, prefer one complete valuable workflow over a wide feature list. Version cuts may retain manual operational steps when they reduce risk without invalidating the test. Never present guesses as domain facts or imply software replaces required professional judgment.
