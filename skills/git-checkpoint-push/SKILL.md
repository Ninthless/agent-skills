---
name: git-checkpoint-push
description: Create professional git checkpoint commits and push them when the user wants milestone-based progress saved to a remote repository. Use this skill whenever the user asks to commit and push after each completed point, says to push regularly during implementation, wants "规范的 git commit 信息", asks to save progress to git while coding, or wants work pushed once a coherent task slice is done. Also use it when a remote repository exists and the user has already established that periodic checkpoint pushes are desired.
---

# Git Checkpoint Push

## Overview

Use this skill to turn completed implementation points into clean git checkpoints. Detect whether the current repository has a remote, stage only the relevant files, write a professional commit message, push safely, and report exactly what was saved.

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

If there is no remote configured, do not push. You may still create a commit if the user asked for one, but say clearly that no remote was available.

If there are unrelated modifications mixed into the worktree, do not silently include them. Read carefully and stage only the files that belong to the completed point. If separation is not possible without risk, pause and ask the user.

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

### 5. Stage only the relevant files

Prefer targeted staging over `git add .` whenever possible.

Rules:

- Stage only files that belong to the completed checkpoint.
- Avoid staging unrelated user changes.
- If a deleted file is part of the completed point, stage the deletion.
- Recheck `git status --short` after staging so you know exactly what will be committed.

### 6. Write professional commit messages

Use concise, production-style commit messages. Prefer Conventional Commit style when it fits.

Format:

`type(scope): summary`

Good types:

- `feat`
- `fix`
- `refactor`
- `chore`
- `docs`
- `build`
- `perf`

Guidelines:

- Use present-tense, action-oriented summaries.
- Keep the first line focused on the checkpoint, not the whole project.
- Do not mention temporary struggle, conversation context, or "AI".
- Do not stuff multiple unrelated points into one commit message.

Examples:

- `feat(api): add workspace and auth demo endpoints`
- `feat(api): align data layer with document architecture`
- `feat(api): seed academic domain and query workspace from mysql`
- `fix(web): correct login portal layout and workspace header structure`
- `refactor(web): rebuild frontend as Ant Design workspace`

### 7. Push safely

After creating the commit:

- push the current branch to the matching remote
- prefer non-interactive commands only
- report any push failure clearly

If the branch has no upstream yet, set it during push if appropriate.

### 8. Report the checkpoint clearly

After commit and push, always summarize:

- what checkpoint was completed
- commit hash and commit message
- branch name
- remote push result
- verification result
- any remaining unstaged or uncommitted changes

## Safety Boundaries

- Never use destructive git commands like reset, checkout discard, or force-push unless the user explicitly requests them.
- Never include unrelated work just to make a checkpoint convenient.
- Never invent a successful push. Confirm it from command output.
- Never amend an existing commit unless the user explicitly asks.

## Decision Rule

If the repository has a remote and the user wants milestone-based pushes, then after each meaningful completed point:

1. verify the checkpoint
2. stage only relevant files
3. commit with a professional message
4. push
5. summarize exactly what happened

If any of those steps are blocked, explain the blocker instead of pretending the checkpoint is complete.
