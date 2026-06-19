---
name: powershell-safe-commands
description: 'Use this skill whenever an agent will run or generate PowerShell commands on Windows, especially in Codex/CLI tasks involving $, $_, $env:, @{u}, $(...), nested powershell -Command, one-liners, file edits, regex replacements, quoting/escaping, shell wrapper bugs, or user complaints like $ 被吃了, PowerShell 外层吃了, one-liner 翻车, 改用 Python, Codex 把 $_ 吃掉. Trigger before writing commands, editing files from shell, or rerunning failed PowerShell commands; prefer direct executables, Python, or temporary scripts over fragile nested one-liners.'
---

# PowerShell Safe Commands

## Copyright

Copyright (c) 2026 Ninthless. All rights reserved. This skill may not be copied, modified, redistributed, or used to create derivative works without prior written permission.

## Triggers

- The task will run shell commands in PowerShell, Windows Terminal, Codex CLI, or an agent shell whose outer shell may be PowerShell.
- A command contains `$`, `$_`, `$env:`, `${...}`, `$(...)`, `@{...}`, backticks, regex replacements, script blocks, here-strings, nested quotes, or pipes into `ForEach-Object` / `Where-Object`.
- The user reports that PowerShell ate a token, a one-liner failed, `$_` disappeared, `@{u}` became a hashtable, quoting broke, or an edit had to be redone in Python.
- The agent is about to use `powershell -Command`, `pwsh -Command`, `cmd /c`, `bash -lc`, or another wrapper around a command string.
- The task edits files from the shell, especially with inline PowerShell replacement commands.

## Purpose

Use this skill to avoid the common Windows failure mode where an outer PowerShell parser consumes syntax before the intended program sees it. The fix is usually not clever escaping. The fix is to remove one shell layer, call the executable directly, or move non-trivial logic into a temporary script.

## Default Ladder

Stop at the first safe option that works:

1. Call the target executable directly, without wrapping it in `powershell -Command`.
2. For file edits or structured transforms, write a tiny Python script and run it directly.
3. For reusable JavaScript transforms, use Node directly.
4. If PowerShell is actually needed, put the script in a temporary `.ps1` file and run that file.
5. Only for tiny commands, use inline PowerShell with single quotes around the nested command string.
6. If none of those fit, use `-EncodedCommand` and show the decoded script in the transcript before running it.

Prefer option 1 or 2. They are boring and survive nested shells.

## Hard Rules

- Do not retry a failed quoting-heavy PowerShell one-liner by adding more backslashes at random.
- Do not use inline PowerShell for edits that include `$`, `$_`, regex captures, or nested quotes.
- Do not wrap a command in `powershell -Command` when the current shell is already PowerShell unless there is a concrete reason.
- Quote git revision syntax such as `@{u}` in PowerShell: `git rev-parse --abbrev-ref --symbolic-full-name '@{u}'`.
- In Windows PowerShell 5, use `;` instead of `&&`.
- Honor project command prefixes such as `rtk`; put the prefix before the real executable, not before a PowerShell cmdlet that is not on PATH.
- For non-trivial shell logic, leave one small verification command that proves the intended token reached the intended program.

## Safe Patterns

### Direct executable

Use this when possible:

~~~powershell
git -C E:\Projects\repo status -sb
python scripts\edit_file.py
node scripts\check.mjs
~~~

Avoid this if the wrapper adds no value:

~~~powershell
powershell -Command "git -C E:\Projects\repo status -sb"
~~~

### Pipeline automatic variables

Unsafe when nested in a double-quoted outer command:

~~~powershell
powershell -Command "Get-ChildItem | Where-Object { $_.Name -match 'txt' }"
~~~

Safer:

~~~powershell
powershell -Command 'Get-ChildItem | Where-Object { $_.Name -match "txt" }'
~~~

Safest for agents when the logic grows:

~~~powershell
powershell -File .\work\filter-files.ps1
~~~

### File edits

Use Python for edits that include replacements, captures, or multiple lines:

~~~powershell
python work\edit.py
~~~

Keep the script short and delete it only if the user asked for no artifacts. In challenge or debugging work, keeping the script under `work/` is often better because it makes the edit replayable.

## Recovery After a Quoting Failure

1. Stop retrying the same one-liner.
2. Identify the token that was eaten or reinterpreted.
3. Replace the command with a direct executable call or a temporary script.
4. Run the smallest verification that proves the token survived.
5. Continue with the original task.

## Output Style

When this skill changes the command strategy, say it briefly:

~~~text
PowerShell 会吃这里的 $_，我改用 Python 临时脚本做同一个编辑。
~~~

Do not turn every command into a lecture. Fix the command and move on.
