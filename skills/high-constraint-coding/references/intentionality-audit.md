# Intentionality Audit

Read this when introducing new artifacts or before completing a broad slice.

For every new field, state, branch, helper, layer, endpoint, index, dependency, configuration entry, and test, ask why it exists now, who consumes it, and what evidence supports its shape.

Remove unreachable fallbacks, duplicate validation, pass-through wrappers, template-symmetry layers, unused statuses, speculative extension hooks, broad configuration, and documentation claims not proven by behavior. Defensive code is justified only at a reachable boundary or alternate caller and should be tested there.

Completeness means the requested behavior is connected from caller to outcome and recovery, not that every possible architectural layer or CRUD operation exists.
