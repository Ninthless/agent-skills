---
name: git-checkpoint-push
description: 'Use when the user asks to save work with git, create a checkpoint commit, write a Conventional Commit message, stage relevant files, push to GitHub or a remote, checkpoint after a milestone, 提交代码, 推送到 GitHub, 保存进度, or produce "规范的 git commit 信息". Safely handles git status, branch, remote, staging, commit, push, and PR handoff.'
when_to_use: 'Use when the user asks to commit, push, save progress, create a git checkpoint, write a Conventional Commit message, stage relevant files, push to GitHub, or prepare a safe repository handoff after a coherent completed milestone.'
---

# Git Checkpoint Push

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

### 6. Write Conventional Commit messages

Use the Conventional Commits format for checkpoint commits:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Analyze the actual staged diff to determine:

- type: what kind of change this checkpoint contains
- scope: the area, package, app, module, workflow, or GitHub configuration affected
- description: a present-tense, imperative summary under 72 characters
- body/footer: include only when the change needs context, verification notes, issue references, or breaking-change details

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
| `security` | Security hardening or secret removal when project convention accepts it |

Breaking changes may be represented with an exclamation mark or a footer:

```text
feat!: remove deprecated endpoint
```

```text
feat(config): allow config to extend other configs

BREAKING CHANGE: `extends` key behavior changed.
```

Guidelines:

- Keep one coherent checkpoint per commit.
- Use present tense: `add`, not `added`.
- Use imperative mood: `fix login redirect`, not `fixes login redirect`.
- Keep the first line focused on the checkpoint, not the whole project.
- Keep the first line concise enough to scan well in GitHub history.
- Reference issues with GitHub closing keywords only when the completed checkpoint genuinely resolves the issue.
- Do not mention temporary struggle, conversation context, or `AI`.
- Do not stuff multiple unrelated points into one commit message.

Examples:

- `feat(api): add workspace and auth demo endpoints`
- `fix(web): correct login portal layout`
- `refactor(web): rebuild frontend as Ant Design workspace`
- `test(auth): cover refresh token reuse detection`
- `ci(github): add required workflow permissions`
- `security(auth): remove token from persisted config`

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
