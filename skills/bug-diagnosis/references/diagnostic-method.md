# Diagnostic Method

## Evidence ledger

Record observations with source, time or version when relevant, and whether they are repeatable. Separate observed behavior from interpretation.

## Hypothesis quality

A useful hypothesis names a mechanism, predicts an observation, and can be disproved. Prefer hypotheses that explain all known symptoms with the fewest unsupported conditions.

## Experiment design

Change one discriminating variable at a time. Prefer existing tests, logs, traces, deterministic fixtures, and local reproductions. Define the expected result under each leading hypothesis before running the experiment.

## Confidence

Use high confidence only when the causal mechanism is reproduced or directly observed and alternatives are contradicted. Use medium confidence for a strongly supported mechanism with an unavailable final observation. Use low confidence for a plausible lead requiring more evidence.

## Handoff

Give implementation the failing path, causal chain, affected contract, minimal repair seam, regression cases, and any uncertainty that should constrain the patch.
