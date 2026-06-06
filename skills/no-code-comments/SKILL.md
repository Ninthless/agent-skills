---
name: no-code-comments
description: 'Keep generated or edited code comment-free. Use when writing, fixing, refactoring, patching, scaffolding, showing code, 不要注释, 无注释, or 干净代码.'
---

# No Code Comments

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Triggers

- The answer will include generated, edited, refactored, or patched code.
- The task creates or modifies scripts, configs, tests, components, APIs, workflows, Dockerfiles, migrations, or snippets.
- The user wants clean code, production-ready code, or code without explanatory annotations.
- The user says `写代码`, `生成代码`, `修改代码`, `修复代码`, `重构`, `不要注释`, `无注释`, or `干净代码`.
- Use together with any domain-specific skill when code will be produced.

## Overview

Default to comment-free code for nearly all coding tasks.
Move explanations into the chat response instead of the code whenever possible.
This keeps patches cleaner and usually leads to clearer naming and structure.

This skill is a default coding companion, not a standalone feature workflow. Use it together with the task's domain-specific skill whenever code will be produced or changed.

## Default Behavior

When working on code:

- Do not add inline comments, block comments, banner comments, docstrings, JSDoc, XML documentation comments, or placeholder TODO/FIXME notes.
- Prefer clearer names, smaller helpers, and straightforward control flow instead of explaining logic inside comments.
- Keep code samples clean even when the surrounding explanation is detailed.
- Treat comment-free code as the default output style so the code explains itself through structure.

## Trigger Policy

Invoke this skill whenever the current user request or planned response includes any of these actions:

- Writing new source files
- Editing or refactoring existing code
- Scaffolding components, APIs, scripts, tests, or configs
- Rewriting code for readability or maintainability
- Generating commands, snippets, examples, patches, migrations, schemas, or configuration that contain code-like syntax
- Producing example code in chat

Do not wait for the user to say "不要注释", "no comments", "clean code", or "production-ready". Treat comment-free output as the default for coding work unless the user clearly asks for comments or documentation.

### Must Trigger

Use this skill as a must-trigger companion for prompts such as:

- "write", "create", "generate", "implement", "build", "scaffold", "add", "fix", "edit", "modify", "refactor", "rewrite", "regenerate", "patch"
- "写", "创建", "生成", "实现", "开发", "搭建", "新增", "修复", "修改", "重构", "改写", "脚手架", "补丁"
- requests that mention source files, tests, configs, scripts, components, APIs, database migrations, CI workflows, Dockerfiles, manifests, or code blocks

### Do Not Trigger

Do not force this skill for pure analysis, explanation, planning, debugging discussion, repository inspection, or review when no code is being written, edited, regenerated, or shown.

If a mostly-read-only task later requires code output, switch this skill on before producing that code.

## Allowed Exceptions

Add or preserve comments only when at least one of these is true:

- The user explicitly asks for comments, docstrings, or teaching-style annotations.
- The language, framework, or tooling requires a directive comment such as `# type: ignore`, `// eslint-disable-next-line`, or `@ts-expect-error`.
- The repository already requires a legal header, generated-file marker, or other mandatory file-level comment.
- Removing an existing comment would be risky, unrelated to the task, or would create unnecessary diff churn.
- A public API, schema, or framework convention truly depends on a documentation comment for correct tooling behavior.

When an exception applies, keep comments minimal and limited to the required directive, header, generated marker, or documentation contract.

## Editing Existing Code

When modifying existing files:

- Do not introduce new comments.
- Do not rewrite unrelated existing comments just to match this preference.
- If a touched-area comment is obsolete and its meaning can be expressed clearly in code, remove it as part of the same change.
- If you are replacing or regenerating a block of code, regenerate it without comments unless an exception applies.
- If existing comments are outside the edited area, leave them alone unless the user explicitly asks to remove comments globally.

## Response Behavior

When code is needed:

- Prefer self-explanatory names, straightforward control flow, and small helpers over explanatory comments.
- Put rationale, caveats, and usage notes in the chat response rather than inside the code.
- Keep code blocks, patches, and generated files free of inline comments, block comments, docstrings, JSDoc, XML comments, and TODO/FIXME placeholders unless an allowed exception applies.
- If the user explicitly requests comments, follow that request and do not treat comment-free output as mandatory.

## Communication

If the task is educational or the user seems to want explanation, keep the code itself comment-free and explain the reasoning in normal prose after the code.
Prefer "clean code plus external explanation" over "commented code".

If this skill is active alongside another skill, let the other skill determine architecture, APIs, validation, and domain rules while this skill governs whether generated or edited code contains comments.

## Trigger Examples

Use this skill for prompts like:

- "帮我写这个功能"
- "帮我写这个功能，代码里不要注释"
- "Refactor this file and keep the code clean, no comments"
- "Generate the component, but avoid docstrings and inline comments"
- "Scaffold this service"
- "Write a Python script for this task"
- "修复这个 bug"
- "生成一个配置文件"
- "给我一个最小可运行示例"

Do not force this skill when the user explicitly asks for commented examples, onboarding code, API docs, or generated documentation.
