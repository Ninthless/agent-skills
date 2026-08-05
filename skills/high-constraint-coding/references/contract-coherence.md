# Contract Coherence

Read this when a change crosses more than one layer or changes a shared invariant.

Map entry points, validation, normalization, defaults, service decisions, domain state, persistence, transport, presentation, downstream consumers, and tests. Identify one authoritative owner for each invariant. Do not let layers assign contradictory meanings to missing, null, default, invalid, or terminal values.

Trace every new field or state from producer through lifecycle to consumer. A persisted artifact needs a current purpose, transition rules, recovery behavior, and coverage. Keep request, stored, returned, and displayed semantics aligned.

Classify pre-existing gaps as in scope, out of scope, or blocking. Do not expand the feature merely to make an existing model appear symmetrical.
