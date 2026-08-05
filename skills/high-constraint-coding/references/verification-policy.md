# Verification Policy

Read this when selecting checks for risky or shared changes.

Match evidence to the changed contract. Prefer a failing-before and passing-after targeted test when practical. For a shared seam, add or run an adjacent consumer check. For migrations, verify forward behavior, compatibility assumptions, rollback or recovery expectations, and representative data. For concurrency, verify ordering, ownership, cancellation, retry, and duplicate behavior relevant to the change.

Static checks prove structure, not runtime behavior. Manual reproduction is valid when automation is unavailable, but record exact inputs and observed results. Never convert an unavailable check into a claim that the behavior is safe.

Report commands or checks run, their outcome, and remaining uncertainty. Stop when verification reveals a contradictory contract or unknown root cause that requires a different primary skill.
