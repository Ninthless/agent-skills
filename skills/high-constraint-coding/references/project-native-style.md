# Project-Native Style

Read this before choosing the shape of a non-trivial change.

Inspect analogous maintained code and identify concrete conventions for naming, control flow, error handling, decomposition, dependency wiring, validation, mapping, concurrency, and tests. Prefer enforced tooling and architecture, then analogous maintained modules, then the dominant recent pattern.

Use one coherent convention across the requested slice. Keep the happy path visible, state transitions explicit, names role-oriented, and interfaces stable. Avoid clever compression, one-use wrappers, generic utilities, and unrelated style cleanup.

If the repository is inconsistent, choose the convention best supported by the affected subsystem and explain only decisions that materially affect review.
