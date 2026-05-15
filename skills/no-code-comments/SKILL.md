---
name: no-code-comments
description: Aggressively keep generated and edited code free of comments. Use this skill by default whenever writing, editing, refactoring, scaffolding, or regenerating code, even if the user does not explicitly mention comments. Assume code should ship without inline comments, block comments, banner comments, docstrings, JSDoc, XML comments, and TODO/FIXME placeholders unless the user explicitly asks for documentation or the tooling strictly requires a directive comment.
metadata:
  short-description: Generate comment-free code by default
---

# No Code Comments

## Overview

Default to comment-free code for nearly all coding tasks.
Move explanations into the chat response instead of the code whenever possible.
This keeps patches cleaner and usually leads to clearer naming and structure.

## Default Behavior

When working on code:

- Do not add inline comments, block comments, banner comments, docstrings, JSDoc, XML documentation comments, or placeholder TODO/FIXME notes.
- Prefer clearer names, smaller helpers, and straightforward control flow instead of explaining logic inside comments.
- Keep code samples clean even when the surrounding explanation is detailed.
- Treat comment-free code as the default output style so the code explains itself through structure.

## Trigger Policy

Use this skill automatically for almost any coding request, including:

- Writing new source files
- Editing or refactoring existing code
- Scaffolding components, APIs, scripts, tests, or configs
- Rewriting code for readability or maintainability
- Producing example code in chat

Do not wait for the user to say "不要注释". Assume that preference unless they clearly say otherwise.

## Allowed Exceptions

Add or preserve comments only when at least one of these is true:

- The user explicitly asks for comments, docstrings, or teaching-style annotations.
- The language, framework, or tooling requires a directive comment such as `# type: ignore`, `// eslint-disable-next-line`, or `@ts-expect-error`.
- The repository already requires a legal header, generated-file marker, or other mandatory file-level comment.
- Removing an existing comment would be risky, unrelated to the task, or would create unnecessary diff churn.
- A public API, schema, or framework convention truly depends on a documentation comment for correct tooling behavior.

## Editing Existing Code

When modifying existing files:

- Do not introduce new comments.
- Do not rewrite unrelated existing comments just to match this preference.
- If a touched-area comment is obsolete and its meaning can be expressed clearly in code, remove it as part of the same change.
- If you are replacing or regenerating a block of code, regenerate it without comments unless an exception applies.

## Communication

If the task is educational or the user seems to want explanation, keep the code itself comment-free and explain the reasoning in normal prose after the code.
Prefer "clean code plus external explanation" over "commented code".

## Trigger Examples

Use this skill for prompts like:

- "帮我写这个功能"
- "帮我写这个功能，代码里不要注释"
- "Refactor this file and keep the code clean, no comments"
- "Generate the component, but avoid docstrings and inline comments"
- "Scaffold this service"
- "Write a Python script for this task"

Do not force this skill when the user explicitly asks for commented examples, onboarding code, API docs, or generated documentation.
