---
name: vibecoding-domain-scout
description: 'Research unfamiliar, current, regulated, or platform-dependent domains before product scoping or coding. Use when an app, product, or tool idea depends on industry workflows, business rules, policies, standards, compliance, real-world operations, or expert terminology the user or agent may not know. Trigger for domain maps, hidden requirements, workflow discovery, MVP cuts, risk and validation criteria, and build-ready briefs grounded in current sources. Do not use for routine apps in familiar domains, pure UI implementation, generic market summaries, or clear technical tasks that do not require domain discovery.'
---

# Vibecoding Domain Scout

## Overview

Use this skill to turn a vague product idea in an unfamiliar domain into a practical field map before writing code. Optimize for helping a non-expert know what matters, what is missing, what to verify, and what the first build should include.

This skill is intentionally research-first. Its value is reducing domain ignorance before implementation, not producing a broad market report unless the user asks for one.

## Operating Stance

- Start by mapping the domain, not by proposing a tech stack.
- Treat the user as smart but under-informed about the field.
- If the domain is unfamiliar or current facts may have changed, browse current primary sources before drafting conclusions.
- Prefer concrete workflows, examples, and decision points over abstract advice.
- Expose hidden assumptions and ask only the few questions that change the plan.
- Make uncertainty visible: label facts, guesses, and items that require expert/user validation.
- If the domain is current, regulated, medical, legal, financial, safety-critical, or platform-policy-dependent, verify with current sources before giving specific rules.

## Workflow

### 0. Decide Whether to Browse

Browse before giving domain-specific conclusions when:

- The user names an unfamiliar industry, profession, platform, regulation, API, standard, pricing model, or operational process.
- The answer depends on current rules, policies, forms, workflows, compliance, vendor behavior, or market practice.
- The product would affect money, health, law, safety, education, privacy, identity, or third-party accounts.
- There is more than a small chance memory alone would miss an important domain constraint.

If browsing is unavailable, say so and mark the domain map as assumption-based.

### 1. Research Current Sources

Look up the unfamiliar domain before concluding anything that could have changed.

- Prefer official docs, vendor docs, standards bodies, regulators, and primary sources.
- Use secondary sources only when primary sources are unavailable, and label them clearly.
- Pull out terminology, rules, constraints, workflows, and anything that affects implementation.
- Keep source links so the user can audit the result.
- Separate verified facts from inferences and assumptions.

### 2. Capture the Raw Intent

Restate the idea in one sentence using this shape:

`Build [thing] for [user] so they can [job] in [situation].`

If any bracket is unknown, mark it as unknown instead of inventing certainty.

### 3. Build the Domain Map

Produce a compact map:

- Users and roles: who uses it, who approves it, who is affected by it.
- Core workflow: the real-world sequence before, during, and after the tool.
- Inputs and sources: data, files, user actions, integrations, manual steps.
- Outputs and decisions: what the tool creates, recommends, stores, sends, or changes.
- Rules and constraints: domain rules, permissions, compliance, pricing, timing, platform limits.
- Failure modes: incorrect data, missing data, abuse cases, user mistakes, recovery paths.
- Success criteria: what makes the result useful, trustworthy, and worth using.

### 4. Find the Missing Questions

Ask at most five high-leverage questions. Choose questions that affect workflow, scope, validation, risk, or data model. Do not ask cosmetic or implementation questions yet unless they affect the product's viability.

Good question patterns:

- "Who is the first real user, and what are they replacing today?"
- "What decision would be costly or dangerous if the tool got it wrong?"
- "What data does the user already have, and in what format?"
- "What must happen when the ideal flow fails?"
- "What would make version one valuable even if it is ugly and manual behind the scenes?"

If enough information exists, proceed with explicit assumptions instead of blocking.

### 5. Cut the MVP

Separate the product into:

- Version 0: the smallest prototype that tests whether the workflow matters.
- Version 1: the smallest useful product a real user can complete end to end.
- Later: automation, scale, integrations, polish, analytics, and advanced permissions.

Default to fewer features and stronger workflow coverage. Keep manual back-office steps if they reduce implementation risk without invalidating the test.

### 6. Define Build-Ready Requirements

Produce requirements in this order:

- Primary user journey.
- Screen or interaction list.
- Data objects and required fields.
- Business rules and validations.
- Error states and recovery behavior.
- Acceptance tests in plain English.
- Explicit non-goals.

### 7. Create the AI Build Brief

End with a concise prompt the user can give to a coding agent. Include:

- Product goal.
- MVP scope.
- Domain assumptions.
- Core workflow.
- Data model.
- Required states and edge cases.
- Acceptance criteria.
- What not to build yet.

## Output Format

When the user is exploring, use this structure:

1. `Sources Checked`
2. `Sharp Restatement`
3. `Domain Map`
4. `Hidden Requirements`
5. `Top Questions`
6. `MVP Cut`
7. `Risks and Validation`
8. `Build Brief`

When the user asks to start coding, first give a short scout pass, then implement only after the domain map and MVP are clear enough.

## Guardrails

- Do not let "AI can code it" substitute for product, domain, or verification judgment.
- Do not rely on memory for facts that may have changed; research and cite current sources instead.
- Do not overbuild dashboards, auth, payments, AI features, admin panels, mobile apps, or analytics unless they are necessary for the first workflow.
- Do not present guesses as domain facts.
- Do not recommend collecting sensitive data unless it is necessary; if necessary, name privacy, security, retention, and access-control implications.
- For regulated domains, say what needs professional validation instead of pretending the app can encode the full rules safely.
