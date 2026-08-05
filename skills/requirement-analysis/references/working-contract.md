# Working Contract

Use this structure selectively. Omit sections that add no decision value.

## Goal and evidence

State the intended outcome and distinguish supplied evidence from inference.

## Scope

List included behavior, excluded behavior, actors, inputs, outputs, and affected boundaries.

## Requirement classes

Mark user-stated obligations as ER and necessary deductions as IR. Keep constraints, preferences, and assumptions separate. An assumption must be reversible or explicitly accepted.

## Conflicts and decisions

Name incompatible statements, their practical consequence, and the smallest decision needed. Do not hide a conflict by choosing silently.

## Functional and non-functional requirements

Describe observable behavior as FR items. Use NFR items only for measurable quality attributes such as latency, availability, security, accessibility, compatibility, or operability.

## Acceptance

Each criterion should identify preconditions when needed, an action or event, and an observable result. Avoid acceptance based on internal implementation shape unless the shape is itself required.

## Handoff

Include dependencies, risks, unresolved decisions, evidence gaps, and the next owner. Do not prescribe an architecture unless the evidence already fixes it.
