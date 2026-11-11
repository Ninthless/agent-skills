---
name: delivery-discipline
description: 'Mandatory delivery companion. Always trigger before any write, edit, implement, fix, refactor, scaffold, doc, commit, PR, UI copy, or backend integration, including trivial, one-line, and ordinary requests such as 帮我写, 改一下, 修一下, 写文案, 提交, 对接接口. Do not wait to be named. Use only the sections the task needs: search and the closing checklist when something changes; Chinese prose for Chinese UI copy, docs, and commit messages. Do not trigger for a conceptual question or status check when no artifact will be produced.'
---

# Delivery Discipline

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Mandatory companion

Activate this skill before the first edit, UI string, doc, commit, PR, or backend integration. Do not wait for the user to name it. Trivial and one-line requests still activate it.

Ordinary requests count, including `帮我写`, `改一下`, `修一下`, `写文案`, `提交`, and `对接接口`.

Apply only the sections the task needs:

- A change uses the search, sync, scope, and closing checklist.
- Backend work also uses the contract rules.
- User-visible artifacts also use the final-state rules.
- Chinese UI copy, docs, and commit messages also use the Chinese prose rules.

Do not run the edit checklist on a question that changes nothing. Do not skip the skill because the change looks small.

Do not activate for a conceptual question or status check when no artifact will be produced. If that task later becomes an edit, activate before producing it.

## Before editing

1. Search the whole repo for the related symbols, copy, routes, and fields (`rg` / `grep`). List the files that hit. Then edit.
2. Do not change only the UI. A behavior change also updates the API, validation, permissions, data model and migrations, enums, copy, tests, scripts, and docs that say the same thing.
3. If the scope is unclear, ask where the boundary is. Do not start editing before that is confirmed.

## While editing

4. Do only the thing the user named. Do not refactor along the way or widen the scope.
5. When deleting or changing a field or unit, check both readers and writers, serialization, defaults, and old data. Hiding it in the UI is not done.
6. A missing backend entry is not proof that none exists. Search again with other words: Chinese and English, plurals, old names, and abbreviations.

## Before finishing

7. Put this checklist in the reply:
   - Which files changed, by layer: frontend / API / DB / other
   - Which keywords were searched, and whether any hits remain
   - Whether a migration or compatibility change is required. If it was not done, say it was not done
8. If tests exist, run the ones that cover the change. If none exist, say how to check it by hand.
9. If the search is uncertain or incomplete, stop and name the gap. Do not close with "that should be all".

Breaking any rule above means the task is not finished. Finish the missing part before handing it over.

## Chinese prose

Chinese comments, docs, UI copy, and commit messages must sound like everyday mainland speech. Do not write translationese.

Required:

- Short, spoken sentences. One sentence when one is enough.
- Say 你 / 我 directly. Use fewer of 进行, 完成, 进行了, 相关, 基于, 针对, 从而.
- Use Chinese punctuation: full-width 。，、；：！？. Do not stack clauses with English commas.
- Proper nouns may stay in English (API, PR). The Chinese around them must still read naturally.
- Lead with the conclusion, then add only the detail that is needed.

Forbidden:

- Translationese such as 「在…的情况下」, 「使得…成为可能」, 「值得注意的是」, 「综上所述」.
- Empty slogans and inflated headings.
- Awkward mixed language, such as 「我们 need to 去 fix 这个问题」, unless the user is writing code.
- A sudden manual or customer-support tone.

Before sending, read it once: does it sound like a note to a person? If it sounds translated, rewrite it.

## Report unrelated problems

If reading code, logs, config, or the task itself reveals a real problem outside the current request, say so. Do not skip it.

Report:

- Clear bugs, security risks, bad config, and broken dependencies or paths
- Anything that will make a later step fail or corrupt data
- A current state that blocks the user's goal, such as a broken B while they asked to change A

How to report:

1. Finish, or move forward, the thing the user named.
2. Add a short "顺便发现" note: one sentence for the problem, why it matters, and whether to fix it now.
3. Do not expand into unrelated work without permission. Tell them, then wait.
4. If it might be a problem, label it as a possible problem and give the evidence: file, line, or what you saw.

Forbidden:

- Pretending not to see it and delivering only the requested slice
- Quietly changing unrelated code
- Inventing problems to look thorough

## Final-state delivery copy

User-visible output and its wrapping — code comments, docstrings, UI copy, errors, empty states, titles, filenames, labels, commits, PRs, READMEs, and handoff notes — describe only the state that shipped. Assume the reader did not see this session.

Hard rules:

- Do not write rejected, tried-and-dropped, or user-corrected options into the artifact, including phrases such as "no X", "do not use Y", "Z was removed", or "as requested, no longer…".
- Do not prove obedience with a negation. "Don't mention Dongpo pork" does not become the title "tomato and eggs (no Dongpo pork)". Write the positive result from scratch. Do not edit the rejected sentence word by word.
- Do not recap abandoned attempts, branch comparisons, why another option was skipped, tool calls, or the session inside comments, PRs, or commits.
- Do not add a closing claim such as "cleaned up", "nothing left", or "omitted as requested" just to pass a self-check.

Copy and hints, including purchase limits, forms, and text beside buttons:

- If one sentence is enough, do not write a second. If the interaction can say it, leave it out of the copy. A purchase limit locks the quantity or disables plus. A disabled control is gray. Do not add a follow-up such as "buying earlier today counts too".
- Do not put edge cases, guardrail logic, or internal reasons into user-visible copy. Let the product behavior carry them.
- Copy says what the user does now or what they get. It does not say why the design is this way, or what the feature does not include.

Keep a note only when this surface actually needs it:

- A real invariant a later maintainer cannot see from the diff: compatibility, security, law, or an external action that already happened
- A change the user already had before this task, or a comparison, ADR, or audit note the user explicitly asked to keep
- A necessary technical name, diagnosis, test, or snapshot. Do not change an API, migration, or test meaning just to make the text look clean

Before closing, ask of each delivered surface: would a reader who missed this conversation need this line? Would omitting it make the result factually wrong or unsafe? Is it a real change in the authoritative baseline that this surface must explain? If any answer is no, delete it or rewrite it as the final state. Then reread filenames, metadata, UI copy, and rewritten hooks. An outsider should not be able to tell that another option was ever on the table.

## Backend contracts

When integrating with a backend, follow the confirmed API contract. If an endpoint is missing, a field is insufficient, or the meaning does not match, report the gap. Do not fill it from a list, cache, local storage, mock data, or a default and hide the problem. Do not add cross-endpoint joins or fallback behavior before that is confirmed. Fields marked optional may be handled as specified. When there is a gap, finish the parts that are unaffected, and list the blockers plus what the backend still needs to provide.
