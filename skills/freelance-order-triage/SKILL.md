---
name: freelance-order-triage
description: "Judge freelance coding orders before quoting or implementation. Use for client briefs, commercial jobs, student requests, small feature requests, bugfixes, rescue work, vague scope, AI-generated project cleanup, take-or-decline decisions, clarifying questions, scope boundaries, quote posture, revisions, and acceptance checklists."
---

# Freelance Order Triage

## Overview

Use this skill to turn a messy incoming order into a controlled decision: take it, clarify it, reshape it, charge discovery, or decline it. Optimize for protecting the freelancer's time, reputation, scope boundary, and delivery confidence before any coding starts.

This skill is for order risk and delivery control. If the main uncertainty is the client's industry or business process, use `vibecoding-domain-scout` for domain research before estimating implementation.

## Operating Stance

- Judge the order before solving the technical problem.
- Treat "small request" as unproven until dependencies, acceptance, and deployment are clear.
- Separate client communication from internal risk analysis.
- Prefer staged scope, paid discovery, or hourly work when requirements or code quality are unknown.
- Use fixed price only when deliverables, acceptance criteria, inputs, deadline, and revisions are bounded.
- Keep student work ethical: support learning, debugging, explanation, review, and compliant scaffolding; do not help submit dishonest work.

## Workflow

### 1. Read the Order

Restate the order in this shape:

`Client wants [deliverable] by [deadline] for [budget/constraint], and acceptance depends on [validator].`

If a field is missing, mark it as unknown. Do not fill unknowns with optimism.

### 2. Classify the Order

Classify by job type:

- Commercial order: business client, real users, reputation or money at stake.
- Student order: coursework, demo, lab, capstone, thesis-adjacent, or learning task.
- Small request: "just add/change/fix this" with hidden complexity risk.
- Rescue order: broken existing project, unfinished AI-generated code, unknown codebase, deployment failure.
- Prototype order: rough demo, PoC, presentation, or validation artifact.
- Production order: live deployment, real data, accounts, payments, compliance, or ongoing use.

### 3. Score the Risk

Produce a quick triage:

- Clarity: clear, workable with assumptions, too vague to quote.
- Scope risk: low, medium, high.
- Domain risk: familiar, learnable, needs expert validation.
- Codebase risk: no codebase, clean codebase, unknown, messy, AI-generated, legacy.
- Access risk: files available, repo available, credentials missing, third-party accounts needed.
- Deadline risk: relaxed, tight, unrealistic, unclear.
- Communication risk: one decision maker, multiple voices, no clear acceptance owner.
- Revision risk: bounded, likely to drift, unlimited expectations.
- Ethics/compliance risk: none obvious, caution, reshape, decline.

### 4. Decide the Posture

Choose one:

- Take: scope is clear, value is acceptable, risks are bounded.
- Clarify: promising but missing information blocks quote or schedule.
- Paid discovery: codebase/domain/access is unknown but client seems serious.
- Stage it: split into milestones to contain uncertainty.
- Hourly only: requirements will move or debugging scope is inherently uncertain.
- Reshape: requested outcome is too broad, unsafe, unethical, or unrealistic.
- Decline: budget, ethics, access, deadline, or client behavior makes success unlikely.

### 5. Identify Hidden Scope

Check for:

- Existing code reading, environment setup, dependency conflicts, and build failures.
- Data migration, data cleaning, sample data, imports, exports, and backups.
- Auth, roles, permissions, payments, email, notifications, file uploads, admin panels.
- Mobile responsiveness, browser compatibility, localization, accessibility, performance.
- Deployment, domain, SSL, cloud accounts, app store review, platform policies.
- Testing, documentation, training, handoff, and support after delivery.
- Revisions, taste-based changes, content entry, design assets, and client delays.

### 6. Draft Questions to Send

Ask only questions that affect quote, schedule, acceptance, or risk. Prefer concise client-facing language.

Core questions:

- What exact output counts as done?
- Who will test and approve it?
- What files, repository, accounts, credentials, sample data, and design assets are ready?
- What is the real deadline, and what can be cut if time runs out?
- How many revision rounds are included, and what counts as a new request?
- Is this for demo, coursework support, internal use, or production users?
- For existing projects: can I inspect the code before giving a fixed quote?

### 7. Define Scope and Acceptance

Produce:

- Included: deliverables and tasks.
- Excluded: anything not covered by the quote.
- Assumptions: facts that must stay true for price and deadline to hold.
- Client inputs: materials, access, accounts, examples, content, test data.
- Acceptance checklist: plain-English tests the client can run.
- Revision boundary: included change rounds and what triggers a new quote.
- Handoff: source code, deployed app, files, documentation, video walkthrough, or tutoring notes.

### 8. Prepare the Response

End with one of these client-ready outputs:

- Clarifying question message.
- Quote boundary note.
- Paid discovery proposal.
- Milestone plan.
- Acceptance checklist.
- Polite decline or reshape message.

If the main blocker is an unfamiliar business/domain process, explicitly recommend using `vibecoding-domain-scout` next to map the domain before estimating implementation.

## Output Format

Use this structure:

1. `Order Read`
2. `Take / Clarify / Discovery / Hourly / Decline`
3. `Risk Triage`
4. `Hidden Scope`
5. `Questions to Send`
6. `Quote Posture`
7. `Scope Boundary`
8. `Acceptance Checklist`
9. `Client-Ready Reply`

## Guardrails

- Do not treat vague enthusiasm as commitment.
- Do not quote fixed price for unknown codebases, unclear acceptance, or shifting requirements without discovery.
- Do not let "just a small change" bypass codebase, deployment, data, and testing checks.
- Do not promise results that depend on third-party approval, platform policies, unstable APIs, or client-provided assets not yet available.
- Do not normalize unlimited revisions; always define change boundaries.
- Do not help students submit dishonest work; redirect toward learning, debugging, explanation, or compliant project support.
