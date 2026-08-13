---
name: websearch-first
description: 'Use this skill by default for every user request: search the web before answering, explaining, planning, reviewing, coding, editing local files, running commands, or making recommendations. Search authoritative sources for current facts, unfamiliar domains, APIs, libraries, versions, standards, policies, security, prices, platform behavior, and implementation choices, and still perform a brief relevance search for simple local tasks. Trigger for 先联网搜索, 先查资料, 先搜索, web search, browse first, do research first, or webserach. Reconcile web evidence with local repository, runtime, and user-provided facts; cite sources that affect the result. Skip only when the user explicitly forbids network access or the search capability is unavailable, and report the exception.'
---

# Websearch First

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Overview

Use web research as the default evidence-gathering step before making a decision, giving an explanation, or editing local code. Search provides current external facts and candidate implementation patterns; it does not replace the repository's actual version, configuration, source, tests, or runtime behavior.

## Operating Contract

- Invoke web search before every task, including local code changes, repository inspection, file edits, command execution, formatting, calculations, and simple explanations. Do not decide that a task is too trivial to search.
- Search before action when the task has any material external fact, current behavior, unfamiliar concept, dependency capability, version, standard, policy, security, pricing, platform, or implementation-choice question.
- For local code changes, search official API documentation, versioned docs, standards, release notes, source repositories, or maintainer guidance before editing when those sources can reduce uncertainty.
- Treat local repository evidence as the final authority for project-specific behavior. Treat runtime and test evidence as stronger than assumptions from web pages or names.
- Distinguish verified external facts, local facts, measured observations, inferences, and unresolved assumptions.
- Cite only sources actually consulted and state which decision each source supports.
- Do not browse aimlessly. Stop when the relevant contract, current fact, or competing option is sufficiently established.

## Workflow

### 1. Classify the evidence need

Before searching, state the decision the search must support:

- current fact or changing policy
- unfamiliar domain or terminology
- exact API, dependency, version, or platform capability
- standard, security, compatibility, or operational requirement
- implementation pattern or tradeoff
- local code change that needs external justification

If none applies, run a brief general search related to the task or its subject, then state whether it affected the result. Never silently skip because the task appears mechanical or obvious.

### 2. Search in source order

Prefer:

1. official vendor, library, framework, regulator, standards body, or primary source
2. official release notes, source repository, issue tracker, or generated specification
3. reputable technical documentation or maintainer discussion
4. secondary material only to discover terminology or competing interpretations

Search the exact product, version, platform, jurisdiction, or date when the task provides one. Do not combine incompatible major-version documentation.

For detailed source selection, evidence recording, and conflict handling, read [source-and-evidence.md](./references/source-and-evidence.md).

### 3. Reconcile with local reality

For repository work, search is not implementation proof. Inspect the manifest or lockfile, local registrations, adapters, generated artifacts, callers, tests, configuration, and runtime path. Resolve conflicts in this order:

1. explicit user requirement and safety constraints
2. repository behavior and checked-in contracts
3. verified runtime or test evidence
4. exact-version primary documentation
5. general web guidance

If the repository contradicts current online documentation, preserve the repository contract unless changing it is explicitly requested. Report the mismatch and compatibility risk.

### 4. Use and verify the result

Apply only conclusions supported by the gathered evidence. For implementation tasks, use the smallest supported change and verify it locally. For research or explanation tasks, separate fact, inference, recommendation, and uncertainty. Do not turn one search result, code example, or passing API call into a universal guarantee.

### 5. Report sources

End with a compact evidence note when web research affected the result:

- Sources: title and URL for the material sources used
- Established: the facts or contracts supported
- Applied: the decision, code path, or recommendation changed by those facts
- Remaining uncertainty: what still depends on local testing, user confirmation, or expert review

If search was skipped, say why. The only normal skip is an explicit no-network instruction. If search failed or is unavailable, continue only with clearly labeled local or prior evidence and state what remains unproven.

## Hard Boundaries

- Never fabricate a source, URL, quote, version, current date, search result, or claim of having browsed.
- Never cite search snippets as if they prove behavior when the underlying source was not inspected.
- Never treat the latest documentation as proof that the repository's installed version supports a capability.
- Never replace local tests, source inspection, or runtime checks with web citations.
- Never send private source code, secrets, credentials, personal data, or proprietary repository content to a public search query.
- Respect an explicit user request not to browse and report the evidence limitation.
