# Content Design

Read this reference when language, labels, instructions, errors, empty states, or information organization affect task success.

## Contents

- Start With The User Task
- Name Objects And Actions
- Design Instructions And Help
- Design Forms
- Design Empty, Loading, And Error States
- Design Consequential Actions
- Structure Information
- Localize And Format
- Verify Content In The Interface

## Start With The User Task

- Write for what the user needs to know or do at this moment.
- Put required information before the decision or input it affects.
- Remove copy that only advertises visible features or explains obvious UI structure.
- Separate product facts from promotional claims.
- Keep important limitations, prices, dates, permissions, and consequences visible.

## Name Objects And Actions

- Use the user's language for objects, statuses, and workflows.
- Keep the same object and destination names across screens.
- Label commands with the real outcome: `Export PDF`, `Cancel subscription`, or `Pay $48.00`.
- Avoid vague labels such as `Continue`, `Submit`, `Manage`, or `Learn more` when a specific action is available.
- Keep visible labels and accessible names aligned.
- Use familiar verbs and nouns instead of internal system terminology.

## Design Instructions And Help

- Put instructions where they are needed, before the user fails.
- Explain uncommon formats, constraints, irreversible effects, and required preparation.
- Use progressive disclosure for secondary detail.
- Keep help consistent across a multi-step process.
- Do not use tooltips as the only location for essential information.
- Prefer examples that exercise real content rather than generic filler.

## Design Forms

- Use persistent labels and clearly distinguish required from optional information.
- Match field order to the user's mental model and source documents.
- Explain why sensitive or unusual information is requested.
- Preserve valid input after errors.
- Write validation messages that identify the problem and the correction.
- Avoid blaming language and raw system errors.
- Do not request the same information twice when it can be reused safely.

## Design Empty, Loading, And Error States

- Empty states should explain the condition and provide the most useful next action when one exists.
- No-results states should preserve filters and offer a clear recovery path.
- Loading copy should describe meaningful progress only when it helps users wait or decide.
- Error messages should state what failed, what remains safe, and how to recover.
- Permission and offline states should explain available alternatives.
- Success messages should confirm persistence, timing, or consequence when the result is not already obvious.

## Design Consequential Actions

- State price, billing cadence, renewal, data loss, visibility, permission, and irreversible consequences before commitment.
- Use confirmation only when risk justifies interruption.
- Make destructive confirmations identify the affected object.
- Keep rejection, cancellation, revocation, and deletion language neutral and direct.
- Do not use urgency, shame, ambiguity, or visual imbalance to manipulate choice.

## Structure Information

- Lead with the information needed for the next decision.
- Group content by user task and relationship rather than database shape.
- Use headings that describe the section's purpose.
- Keep metadata subordinate but scannable.
- Use tables for comparison, lists for sequences or collections, and prose for explanation.
- Avoid repeating the same summary in headings, cards, and body copy.

## Localize And Format

- Use locale-aware dates, time, numbers, currency, units, names, addresses, and plural forms.
- Test expansion, contraction, long unbroken values, and right-to-left direction where relevant.
- Do not embed critical text in images.
- Avoid fixed-width assumptions based on English labels.
- Preserve meaning when text wraps or truncates; expose the full value when truncation is necessary.

## Verify Content In The Interface

Test with realistic short, typical, and long content. Read the rendered interface as a user:

1. Can the user identify the current state?
2. Is the next action named by outcome?
3. Are material consequences visible before action?
4. Can the user recover from a failure without guessing?
5. Does any copy exist only to fill space or market the interface?
6. Does localization preserve hierarchy and control access?
