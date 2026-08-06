---
name: write-api-docs
description: 'Create, rewrite, reconcile, or review concise, implementation-ready API documentation from routes, handlers, schemas, tests, runtime evidence, OpenAPI/Swagger, GraphQL, gRPC, webhooks, AsyncAPI, or messages. Use for frontend-to-backend or backend-to-frontend contracts, endpoint references, machine-readable API specifications, and integration reviews. Document only evidence-supported behavior and never invent fields, constraints, permissions, errors, side effects, or deployment status. Do not trigger for endpoint, client, SDK, webpage, or test implementation, ordinary source review, unknown-bug diagnosis, generic HTTP teaching, or incidental API mentions.'
---
# Write API Docs

## Outcome

Produce reference documentation that a provider can implement or a consumer can call without reading source code. Keep the deliverable factual, compact, predictable, and shaped like the API. Preserve repository terminology, formats, grouping, and versioning.

Determine authority per operation or message from requirements, executable implementation, schemas, tests, runtime observations, or an existing specification. One API set may mix `implemented`, `proposed`, `conflicting`, `missing`, and `uncertain`. Preserve material conflicts, but keep evidence analysis outside the reference body unless the user requests an audit or reconciliation report.

## Choose the deliverable

1. Honor the requested format exactly.
2. Otherwise update the repository's existing API documentation format.
3. If no format exists, use OpenAPI for REST, GraphQL SDL for GraphQL, proto for gRPC, and AsyncAPI for message protocols when the contract must support tooling or implementation. Use concise Markdown when the user primarily needs a readable handoff.
4. Do not create both machine-readable and Markdown copies by default. Produce multiple artifacts only when the user requests them or the repository already maintains both.

For `review`, return findings ordered by integration risk and do not rewrite files. For `reconcile`, return the differences and only the corrected contract fragments unless a full rewrite is requested.

## Build the contract

Inventory operations with real consumers or explicit requirements. Trace backend evidence from route/group/prefix through middleware, validation, handler, serializer, errors, and tests; trace frontend evidence from use case through client call, types, mocks, states, and tests.

Use OpenAPI paths for REST operations. Distinguish provider-initiated HTTP `webhooks` from operation-bound `callbacks`. Use AsyncAPI for message/channel protocols and document publish/subscribe direction, payload, headers, acknowledgement, retry, ordering, and delivery semantics only when evidenced. Use GraphQL schema and operations for GraphQL, and proto services/messages for gRPC. Do not collapse webhooks, callbacks, and messages into one model.

For each operation or message include only applicable, evidenced details:

- identity and one-sentence purpose
- authentication or authorization when it differs from the shared rule
- path, query, header, cookie, body, or message inputs
- success status and response schema
- operation-specific errors the consumer must handle
- pagination, asynchronous completion, idempotency, retry, rate limits, caching, or side effects when relevant

Distinguish required, optional, nullable, default, conditional, read-only, and write-only fields. Put constraints, formats, units, timezone, precision, and unknown-field behavior on the affected field instead of repeating them in prose.

Examples must validate against the schema, use synthetic values, and contain no secrets, PII, internal hosts, or production identifiers. Prefer one representative request and success response per operation. Add an error example only when its shape or handling is not already clear from a shared error model.

## Markdown reference shape

Use this order when Markdown is the primary deliverable, omitting every inapplicable section:

1. title and one-sentence scope
2. base URL, content type, authentication, and shared error or pagination rules
3. endpoints grouped by resource or consumer workflow
4. shared schemas referenced by more than one endpoint

Each endpoint should normally contain the method and path, one-sentence purpose, parameters or request body, success response, applicable errors, and examples. Do not add a table of contents, overview essay, architecture narrative, source inventory, evidence matrix, status legend, frontend implementation notes, risk register, recommendations, changelog, or conclusion unless the user explicitly requests it or the repository already requires it.

Use short operation summaries beginning with a direct verb. Avoid duplicating the summary in the description, narrating obvious JSON, or repeating shared authentication, error, pagination, and schema details under every endpoint.

## Uncertainty and conflicts

Do not mix internal analysis into an otherwise settled reference document. Resolve evidence before writing when possible. If an unresolved fact blocks implementation or integration, mark the smallest affected operation or field as `TBD` with one neutral sentence describing the decision needed. Do not add a broad Open Questions section for non-blocking observations.

For a requested reconciliation or audit, keep differences separate from the clean target contract. State the conflicting values, their sources, the owner who must decide when known, and the smallest affected fragment. Do not silently choose a side.

## Compatibility and validation

Separate specification, API, and documentation versions only when those versions exist or the user asks for version analysis. Classify an actual proposed change as breaking, non-breaking, or uncertain across wire and semantic behavior; do not add a generic versioning lecture.

Parse JSON or YAML, resolve references, check operation IDs and inventory coverage, validate examples, and run repository-supported specification or contract checks. Use specification diffs when comparing versions. Report unavailable checks in the work summary, not inside the API reference.

## Final edit

Remove any sentence that does not help a consumer construct a valid request, handle a response, or understand an evidenced contract constraint. Remove empty sections, duplicated facts, generic HTTP teaching, history, implementation speculation, unsupported metadata, and process narration. Call behavior deployed or production only with runtime or deployment evidence. When multiple artifacts are requested, keep them semantically consistent.
