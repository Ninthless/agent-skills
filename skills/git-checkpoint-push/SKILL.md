---
name: git-checkpoint-push
description: 'Safely stage, commit, checkpoint, or push completed work using the full Conventional Commits 1.0.0 structure: type, optional scope, optional breaking marker, description, meaningful body when context is not obvious, and valid footer trailers when applicable. Use only when the user explicitly asks to save work in git or GitHub, 提交代码, 推送, 保存进度, Conventional Commit, commit message, milestone push, or GitHub PR handoff. Inspect status, remotes, upstream divergence, verification, unrelated changes, compatibility impact, issue references, and attribution before writing history. Do not trigger for read-only git status, diff, log, review, conceptual Git questions, or imaginary commit examples that do not authorize repository mutation.'
---

# Git Checkpoint Push

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Triggers

- The user asks to commit, push, or save the current work.
- The user wants a git checkpoint after a completed milestone.
- The user asks for a Conventional Commit message.
- The user wants relevant files staged and pushed safely to GitHub or a remote.
- The user says `提交代码`, `推送到 GitHub`, `保存进度`, `规范 commit`, or `规范的 git commit 信息`.

## Overview

Use this skill to turn completed implementation points into clean Git/GitHub checkpoints. Detect whether the current repository has a remote, respect branch protection and repository rules, stage only the relevant files, write a professional commit message, push safely, and report exactly what was saved.

## Workflow

### 1. Confirm that checkpoint pushing is in scope

Use this skill only when at least one of these is true:

- The user explicitly asks you to commit and push.
- The user says to push after each completed point or milestone.
- The user has already established in the current conversation that periodic git pushes are desired.

Do not push just because git exists. The user must want checkpoint pushes.

### 2. Verify repository state before acting

Always inspect these before preparing a checkpoint:

- `git status --short`
- current branch
- `git remote -v`
- upstream branch and sync state when a remote exists
- whether the remote host is GitHub when GitHub-specific safeguards may apply

If there is no remote configured, do not push. You may still create a commit if the user asked for one, but say clearly that no remote was available.

If there are unrelated modifications mixed into the worktree, do not silently include them. Read carefully and stage only the files that belong to the completed point. If separation is not possible without risk, pause and ask the user.

If the current branch tracks a remote branch, fetch or otherwise inspect the divergence before pushing. Do not overwrite remote work. If the local branch is behind, stop and report the safest next action instead of rebasing, merging, or force pushing without explicit user intent.

### 2a. Respect GitHub repository rules

When the remote is GitHub, assume repository rules and branch protections may exist even if they are not visible locally.

- Prefer pushing feature or working branches over pushing directly to protected default branches.
- Do not force push, delete protected branches, bypass required reviews, or bypass required status checks.
- If the default branch or current branch appears protected, create or push to a non-protected branch and tell the user a pull request is the correct next step.
- If required signed commits are likely or configured locally, use the repository's existing signing setup; do not invent signing keys or disable signing.
- If GitHub rejects a push with a ruleset, branch protection, secret scanning, signed commit, or status-check error, stop and report the exact blocker.
- Never commit secrets, tokens, private keys, generated credentials, local env files, or machine-specific authentication material.

### 3. Define a valid checkpoint

A checkpoint must be a coherent slice of work, not a random partial save. Good checkpoints usually mean one of these:

- one completed feature slice
- one infrastructure step finished and verified
- one bug fix plus verification
- one UI or API milestone that now builds or runs

Do not create a checkpoint in the middle of obviously broken or half-moved work unless the user explicitly asks for that.

### 4. Verify before committing

Before committing, run the most appropriate lightweight verification available for the completed point.

Examples:

- build command for frontend work
- compile or lint command for backend work
- targeted test command when tests exist

If verification cannot be run, say so in the final summary. If verification fails, do not push unless the user explicitly wants the failing checkpoint saved.

For GitHub repositories, prefer verification that maps to required checks when this can be inferred from workflows, branch protection errors, or existing project conventions. If GitHub Actions workflows exist, inspect their names and expected commands when practical so the local checkpoint is likely to satisfy CI.

### 5. Stage only the relevant files

Prefer targeted staging over `git add .` whenever possible.

Rules:

- Stage only files that belong to the completed checkpoint.
- Avoid staging unrelated user changes.
- If a deleted file is part of the completed point, stage the deletion.
- Review staged changes before committing when the checkpoint includes generated files, dependency lockfiles, workflow files, permissions, or security-sensitive paths.
- Recheck `git status --short` after staging so you know exactly what will be committed.

### 6. Write complete Conventional Commit messages

Follow Conventional Commits 1.0.0:

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

Analyze the actual staged diff to determine:

- type: what kind of change this checkpoint contains
- scope: the area, package, app, module, workflow, or GitHub configuration affected
- breaking marker: whether consumers must change because a public, persisted, configuration, data, protocol, or operational contract is incompatible
- description: a concise imperative summary without a trailing period
- body: the motivation, previous behavior, chosen approach, and important effects that are not obvious from the diff
- footers: structured breaking-change details, issue references, attribution, review, signoff, or other repository-supported trailers

Use a subject-only commit only when all of these are true:

- the change is small and single-purpose
- its reason and effect are obvious from the subject and diff
- it has no compatibility, migration, operational, security, or non-obvious architectural consequence
- it has no issue reference, attribution, signoff, or other required trailer

Otherwise write a body. A non-trivial feature, fix, refactor, migration, dependency change, CI change, security change, or cross-layer checkpoint should normally have a body.

### 6a. Header rules

The header must match:

```text
<type>[optional scope][optional !]: <description>
```

- Use a lowercase type.
- Use a concise noun for scope when it improves understanding; omit it when no single stable scope exists.
- Put `!` immediately before `:` for a breaking change.
- Start the description immediately after `: `.
- Use imperative mood and describe the checkpoint outcome.
- Keep the header under 72 characters when practical; prefer about 50 characters for simple commits.
- Do not end the description with a period.
- Do not use multiple types or scopes to hide an incoherent checkpoint.

Choose the subject language from the user's explicit request:

- If the user does not explicitly specify a commit-message language, default the entire commit message to English regardless of the conversation language or repository history, such as `fix(web): correct login redirect`.
- If the user explicitly requests a language, keep the Conventional Commits type and scope in English and write the description in the requested language: `<English type>(<English scope>): <description in the requested language>`.
- Apply this rule to every valid type, including `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `build`, `ci`, `style`, `perf`, and project-specific types.
- Do not translate the type or scope. Do not mix languages in the description unless a technical identifier, API name, or product name requires it.
- Apply the same imperative, concise, no-trailing-period rules in the requested language. For example, use `fix(api): 修复字段校验` rather than `fix(api): 修复了字段校验问题`.

Commit types:

| Type       | Purpose                        |
| ---------- | ------------------------------ |
| `feat`     | New feature                    |
| `fix`      | Bug fix                        |
| `docs`     | Documentation only             |
| `style`    | Formatting/style with no logic |
| `refactor` | Code refactor with no feature/fix |
| `perf`     | Performance improvement        |
| `test`     | Add or update tests            |
| `build`    | Build system or dependencies   |
| `ci`       | CI configuration or workflows  |
| `chore`    | Maintenance or miscellaneous work |
| `revert`   | Revert a previous commit       |
| `security` | Security hardening or secret removal only when project convention accepts it |

Conventional Commits mandates `feat`, `fix`, and breaking-change semantics. Other types are allowed but repository convention remains authoritative. Prefer an existing repository type over inventing a synonym.

### 6b. Body rules

Separate the body from the header with one blank line. Write one or more short paragraphs that explain useful context, especially:

- why the change was necessary
- what behavior or contract existed before
- how the checkpoint changes that behavior
- why this approach was chosen over the relevant alternative
- compatibility, migration, rollout, performance, security, or operational effects
- verification limitations only when they materially affect confidence

Do not use the body as a file list, diff narration, chat summary, or test transcript. Do not repeat the header. Focus on intent and consequences that future maintainers cannot recover cheaply from the diff.

For a meaningful checkpoint, prefer a concise body of two to five sentences over omitting context. Multiple paragraphs are valid when the change has distinct motivation and impact.

### 6c. Footer rules

Separate footers from the body with one blank line. Each footer must use a valid Conventional Commits or Git trailer shape:

```text
Token: value
Token #value
```

- Use hyphens instead of spaces in footer tokens, such as `Co-authored-by`, `Reviewed-by`, and `Signed-off-by`.
- `BREAKING CHANGE` and `BREAKING-CHANGE` are the only space-token exception defined by Conventional Commits.
- Use one footer per logical metadata item.
- Continue a long footer value on following lines only when required.
- Do not invent issue IDs, reviewers, co-authors, signoffs, or release metadata.
- Add `Signed-off-by` only when the project requires it or the user explicitly requests it; signoff has legal or contribution-policy meaning.
- Add `Co-authored-by` only for real co-authors with evidence-supported identity and email.
- Use issue-closing footers only when the checkpoint genuinely resolves the issue and the identifier is known.

Common footers:

```text
BREAKING CHANGE: clients must use the new provider configuration
Fixes #123
Refs #456
Co-authored-by: Name <email@example.com>
Reviewed-by: Name <email@example.com>
Signed-off-by: Name <email@example.com>
```

Follow the repository's existing issue-footer convention when it differs. GitHub closing keywords may also use forms such as `Fixes #123`; do not rewrite a working project convention solely for stylistic uniformity.

### 6d. Breaking changes

Breaking changes must be marked with `!`, a `BREAKING CHANGE:` footer, or both:

```text
feat!: remove deprecated endpoint
```

```text
feat(config): allow config to extend other configs

BREAKING CHANGE: `extends` key behavior changed.
```

Prefer both `!` and a footer when the header alone cannot tell consumers exactly what must migrate:

```text
feat(config)!: replace legacy provider variables

Use a provider map so validation and provider discovery share one
configuration contract.

BREAKING CHANGE: remove PROVIDER_A_URL and PROVIDER_B_URL; configure
providers through PROVIDERS_JSON.
```

Do not mark a change as breaking merely because internal code, tests, or file layout changed. Check actual public, persisted, configuration, protocol, data, CLI, build, or operational consumers.

### 6e. Message construction

Construct multi-line commit messages without losing blank lines or trailer boundaries. Prefer a message file or a shell-native multi-line value. Review the complete staged message before committing.

The final commit message should usually resemble:

```text
fix(auth): preserve sessions during token refresh

Keep the previous token valid until the replacement session is
persisted. This prevents concurrent requests from observing a
temporary logged-out state.

Fixes #123
```

Do not add a body or footer merely to fill the template. Omit empty sections rather than writing placeholders.

Guidelines:

- Keep one coherent checkpoint per commit.
- Use present tense: `add`, not `added`.
- Use imperative mood: `fix login redirect`, not `fixes login redirect`.
- Keep the first line focused on the checkpoint, not the whole project.
- Keep the first line concise enough to scan well in GitHub history.
- Reference issues with GitHub closing keywords only when the completed checkpoint genuinely resolves the issue.
- Do not mention temporary struggle, conversation context, or `AI`.
- Do not stuff multiple unrelated points into one commit message.
- Explain why and important consequences in the body for non-trivial checkpoints.
- Preserve footer syntax and blank-line separation exactly.

Examples:

- `feat(api): add workspace and auth demo endpoints`
- `fix(web): correct login portal layout`
- `feat(auth): 增加登录校验`
- `fix(web): 修复登录重定向`
- `docs(api): 更新接口说明`
- `refactor(core): 简化配置加载`
- `test(auth): 增加令牌复用检测`
- `chore(deps): 更新依赖版本`
- `refactor(web): rebuild frontend as Ant Design workspace`
- `test(auth): cover refresh token reuse detection`
- `ci(github): add required workflow permissions`
- `security(auth): remove token from persisted config`

Examples with bodies and footers:

```text
refactor(coding): separate provider integration boundaries

Keep provider request and response handling independent from status
persistence and presentation so new providers have one maintenance path.
```

```text
fix(inventory): restore stock after cancellation

Move inventory restoration into the committed cancellation path so a
failed transaction cannot leave order and stock state inconsistent.

Fixes #214
```

### 7. Push safely

After creating the commit:

- push the current branch to the matching remote
- prefer non-interactive commands only
- report any push failure clearly

If the branch has no upstream yet, set it during push if appropriate.

For GitHub repositories:

- Do not use `--force` or `--force-with-lease` unless the user explicitly requested history rewriting for this branch.
- Do not push directly to `main`, `master`, or a release branch when a protected-branch or pull-request workflow is evident.
- Prefer `git push -u origin <branch>` for a new checkpoint branch.
- If the GitHub CLI is already available and authenticated, it may be used to report PR URLs or check workflow status, but do not require it for a basic checkpoint push.

**PowerShell 5 note:** `&&` is not a valid statement separator. Use `;` to chain commands instead of `&&`. For example: `git add README.md; git commit -m "..."; git push origin main`

### 8. Report the checkpoint clearly

After commit and push, always summarize:

- what checkpoint was completed
- commit hash and commit message
- branch name
- remote push result
- verification result
- GitHub branch protection, ruleset, or CI status if it affected the push
- pull request URL or next PR step when relevant
- any remaining unstaged or uncommitted changes

### 9. Optional GitHub pull request handoff

If the user asked for a GitHub-ready checkpoint and the completed work belongs behind review, prepare the handoff instead of merging.

- Confirm the branch was pushed.
- Provide a concise pull request title and body, or create the pull request only if the user explicitly asked for PR creation and the GitHub CLI is authenticated.
- Include what changed, how it was verified, and any risk or follow-up needed.
- Do not self-approve, merge, enable auto-merge, close issues, create releases, or change repository settings unless the user explicitly asked for that action.

## Safety Boundaries

- Never use destructive git commands like reset, checkout discard, or force-push unless the user explicitly requests them.
- Never include unrelated work just to make a checkpoint convenient.
- Never invent a successful push. Confirm it from command output.
- Never amend an existing commit unless the user explicitly asks.
- Never bypass GitHub branch protection, required reviews, required checks, signed-commit rules, secret scanning, or repository rulesets.
- Never commit credentials, tokens, private keys, `.env` secrets, local auth files, or generated secrets.
- Never change GitHub repository settings, workflow permissions, branch protection, CODEOWNERS, or security configuration as part of checkpointing unless those files are the explicit completed work.
- Never merge a pull request, approve a pull request, tag a release, or publish a release as part of checkpointing unless the user explicitly asked for that release or merge action.

## Decision Rule

If the repository has a remote and the user wants milestone-based pushes, then after each meaningful completed point:

1. verify the checkpoint
2. inspect remote, branch, and GitHub protection constraints
3. stage only relevant files
4. commit with a professional message
5. push without bypassing repository rules
6. summarize exactly what happened and what GitHub still needs

If any of those steps are blocked, explain the blocker instead of pretending the checkpoint is complete.
