# Source And Evidence Discipline

Use this reference when choosing sources, reconciling conflicting claims, or deciding how strongly web research supports an answer or implementation.

## Source Selection

Match the source to the claim:

- Product behavior and APIs: exact-version official documentation, source, release notes, generated clients, or maintainer issue trackers.
- Standards and protocols: the governing standards body or normative specification.
- Laws, policies, and compliance: regulators, legislatures, courts, official policy pages, or responsible institutions.
- Security: vendor advisories, CVE records, national response teams, maintainers, and primary vulnerability reports.
- Prices, availability, and current product terms: the responsible vendor's current page.
- Research findings: original papers, datasets, or institutional publications.
- Operational practice: responsible organizations and experienced practitioner sources, with assumptions labeled.

Use secondary sources to find vocabulary, disagreements, or primary material. Do not let source popularity substitute for authority.

## Query Safety

Search with public concepts, dependency names, versions, generic error text, and sanitized symptoms.

Do not include:

- secrets, tokens, credentials, keys, cookies, or private URLs
- proprietary source code or unpublished business rules
- personal, customer, employee, health, financial, or identifying data
- internal hostnames, repository names, ticket IDs, or production identifiers when they reveal private context

Rewrite sensitive details into a minimal public abstraction before searching.

## Evidence Strength

Treat claims separately:

1. The source exists and says something relevant.
2. The source applies to the named version, date, jurisdiction, or environment.
3. The repository actually uses that version or configuration.
4. The proposed call or design works in the local integration.
5. The required state or behavior survives the complete workflow.

Evidence for one level does not prove the next.

## Conflict Handling

When sources disagree:

1. check dates, versions, jurisdictions, editions, and intended audiences
2. prefer normative or primary sources for factual contracts
3. inspect whether the repository intentionally preserves older behavior
4. test the local behavior when practical
5. report the disagreement if it changes the decision

Do not silently average incompatible claims or choose the newest source solely because it is newest.

## Search Stopping Rule

Stop when:

- the material fact is supported by an applicable primary source
- the important alternative interpretation has been checked
- local evidence confirms or rejects applicability
- additional results repeat the same evidence without changing the decision

Continue when the current source is only a snippet, secondary summary, incompatible version, unverifiable claim, or one side of a material disagreement.

## Evidence Note

Record only material sources:

- source title and URL
- accessed or current date when time sensitivity matters
- exact claim established
- local decision affected
- remaining limitation

Do not produce a citation dump. A source that did not influence the result does not belong in the evidence note.
