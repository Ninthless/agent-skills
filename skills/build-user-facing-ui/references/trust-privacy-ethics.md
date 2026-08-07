# Trust, Privacy, And Ethical Interaction

Read this reference for purchases, subscriptions, consent, personal data, permissions, account deletion, health, finance, public services, children, or any interface where manipulation or ambiguity can materially harm users.

## Contents

- Trust Contract
- Choice Architecture
- Pricing And Purchase
- Subscription And Cancellation
- Consent And Personal Data
- Risk-Sensitive Interfaces
- Claims And Evidence
- Verification
- Sources

## Trust Contract

A good interface helps users make an informed choice and produces the outcome the interface represented. It does not use visual craft to hide material facts or manufacture pressure.

Hard failures include:

- Disguised advertising or sponsored content
- False urgency, scarcity, activity, or social proof
- Hidden mandatory fees or material terms revealed late
- Preselected optional purchases or data sharing
- A prominent accept path paired with an obscure reject path
- Easy signup paired with intentionally difficult cancellation or deletion
- Misdirection that causes a user to trigger an unintended action
- Confirm-shaming or language that attacks the user's choice
- Permission requests without a task-relevant reason
- Claims of safety, validation, accessibility, or user approval without evidence

## Choice Architecture

- Present materially equivalent choices with comparable prominence, language, and interaction cost.
- Name consequences before commitment, not after.
- Separate necessary processing from optional personalization, analytics, or marketing.
- Preserve the user's previous refusal and avoid repeated prompts designed to wear down resistance.
- Make consent reversible through a path comparable to the original choice.
- Use defaults that protect the user when consequences are costly, public, irreversible, or privacy-sensitive.
- Allow users to review and correct data before a consequential submission.

Visual hierarchy may recommend a sensible default, but it must not conceal or distort alternatives.

## Pricing And Purchase

- Show the payable price, billing period, currency, taxes, mandatory fees, shipping, renewal terms, and material restrictions before commitment.
- Keep price changes visible when configuration, quantity, delivery, or location changes.
- Label actions by their real outcome, such as `Pay $48.00`, `Start paid subscription`, or `Request quote`.
- Do not fabricate countdowns, inventory, recent purchases, ratings, reviews, or comparison prices.
- Keep optional add-ons unselected unless the user explicitly requested a bundle.
- Provide a final review step proportional to cost and reversibility.
- Show confirmation, receipt, fulfillment status, and recovery paths after purchase.

## Subscription And Cancellation

- State trial duration, trial end date, post-trial price, billing cadence, renewal behavior, and cancellation effect before signup.
- Do not imply that a free action is free when payment or automatic renewal is required.
- Make cancellation discoverable from the account or subscription surface.
- Keep the cancellation path no harder than signup unless identity or fraud risk requires a justified step.
- Explain whether access ends immediately or at the period end and what happens to stored data.
- Do not force a sales call, repeated retention screens, or unnecessary survey to complete cancellation.
- Confirm cancellation and provide a record of the effective date.

## Consent And Personal Data

- Collect only data needed for the stated task or an explicitly chosen secondary purpose.
- Explain purpose, retention, sharing, and consequence at the point where the decision is made.
- Avoid bundling unrelated purposes into one mandatory choice.
- Provide an equally usable reject or customize path for optional processing.
- Let users inspect, correct, export, revoke, and delete data where the product contract or law requires it.
- Handle permission denial, partial permission, and later revocation without a dead end.
- Do not put secrets, sensitive personal data, or private content into screenshots, fixtures, analytics, or generated examples.

This skill does not substitute for legal review. Record jurisdictional uncertainty instead of inventing compliance claims.

## Risk-Sensitive Interfaces

For health, finance, safety, legal, identity, public benefits, and other high-impact domains:

- Distinguish information from professional advice and automated recommendations from verified decisions.
- Show data source, freshness, confidence, limitations, and escalation routes when they affect action.
- Require confirmation for consequential actions and support correction or appeal when applicable.
- Avoid using color, emotion, urgency, or authority cues to overstate certainty.
- Protect private content in notifications, shared screens, logs, and previews.
- Test with representative users and domain experts when feasible.
- Report the absence of representative validation as a limitation.

## Claims And Evidence

Use claim language that matches the evidence:

| Evidence | Allowed description |
| --- | --- |
| Source inspection only | Implemented, not runtime verified |
| Automated checks | Passed the named automated checks |
| Manual task run | Manually exercised in the named runtime and conditions |
| Internal participants | Tested with the stated participants and limitations |
| Representative users | Evaluated with the stated recruitment, task, and results |
| Production field data | Observed in the stated population and time window |

Do not say `user validated`, `proven intuitive`, `accessible`, `fast for users`, or similar absolute claims without matching evidence. Prefer bounded statements such as `the primary checkout task succeeded for 7 of 8 recruited participants; mobile screen-reader use was not evaluated`.

## Verification

For a relevant workflow, record:

- Material terms shown before commitment
- Choice symmetry for accept, reject, subscribe, cancel, delete, and permission decisions
- Consent reversal and cancellation outcome
- Purchase or subscription conditions
- Personal-data collection and declared purpose
- Screenshots of the decision and completion states
- Tested workflow outcomes
- Evidence level for usability, accessibility, and performance claims
- Known legal, policy, or representative-user gaps

Any unresolved deceptive pattern is a release blocker.

## Sources

- [FTC report on dark patterns](https://www.ftc.gov/news-events/news/press-releases/2022/09/ftc-report-shows-rise-sophisticated-dark-patterns-designed-trick-trap-consumers)
- [GOV.UK Design Principles](https://www.gov.uk/guidance/government-design-principles)
- [ISO 9241-11 usability](https://www.iso.org/standard/63500.html)
- [Nielsen Norman Group usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
