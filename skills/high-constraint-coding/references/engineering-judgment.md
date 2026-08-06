# Engineering Judgment

Orient before editing: state the current behavior, the requested behavior, the owner of the invariant, callers and consumers, compatibility obligations, failure and recovery paths, and evidence available from the repository.

Choose the seam that owns the behavior. A local patch is correct when the behavior is local; a shared seam is correct when multiple callers or layers rely on one semantic rule. Compare only credible options: keep the current shape, use the smallest seam, or make a necessary broader change. Assess compatibility, failure modes, operability, debuggability, cognitive load, migration cost, and verification cost. Reject an option explicitly only when it materially affects review.

Prefer direct, readable structures and project-native interfaces. Do not add abstractions because a pattern can be named, nor generalize for hypothetical callers. Preserve the happy path and make ownership, boundaries, state transitions, and recovery explicit.

Ask the user when an unresolved choice changes public behavior, data, safety, irreversible operations, or acceptance. Hand off to `bug-diagnosis` when the cause is unknown; to `requirement-analysis` when the desired contract is materially ambiguous; and to `technical-solution-research` when current version, compatibility, or external platform evidence decides the implementation.