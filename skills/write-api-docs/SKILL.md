---
name: write-api-docs
description: 'Create, generate, write, update, rewrite, reconcile, or review an API document or contract from routes, handlers, schemas, types, client calls, tests, runtime evidence, OpenAPI/Swagger, GraphQL, gRPC, webhooks, AsyncAPI, or messages. Use when the final artifact is an API reference, endpoint documentation, API specification, frontend-to-backend or backend-to-frontend handoff, integration guide, or API documentation review. Trigger Chinese requests such as 接口文档, API文档, 接口说明, 接口契约, 接口规范, 接口对接文档, 根据前端生成接口文档, 根据后端代码补齐接口文档, and documentation work phrased as 整理, 补齐, 重写, 对接, or review. Document only evidence-supported behavior; never invent fields, constraints, permissions, errors, side effects, or deployment status. Do not trigger for endpoint/client/SDK implementation, webpage changes, tests, ordinary source review, bug diagnosis, generic HTTP teaching, API research without a documentation deliverable, translation, or incidental API mentions.'
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

For every request parameter, request body, and request-body field, state its presence status explicitly: `required`, `optional`, `conditionally required`, or `unconfirmed`. Do not omit this status from a Markdown table or readable handoff merely because the evidence is incomplete. For response fields, state `always returned`, `conditionally returned`, `optional`, or `unconfirmed` when that distinction matters to consumers. Distinguish presence from nullability: `optional` means the member may be absent, while `nullable` means the member may be present with `null`. Also distinguish input, output-only, read-only, and write-only fields. Put constraints, formats, units, timezone, precision, and unknown-field behavior on the affected field instead of repeating them in prose.

Treat each source according to what it can prove:

- An authoritative schema, validated type contract, explicit requirement, implementation branch, or focused test may establish only the behavior it directly defines.
- A captured request, response, log, fixture, or example establishes an observed instance, not a universal schema guarantee.
- A field name or plausible-looking value establishes no format, unit, semantic type, default, enum, or validation rule.
- Absence from inspected evidence establishes neither optionality nor the absence of rate limits, caching, retries, errors, or side effects.

Never infer `required`, optional, nullable, `format`, pattern, range, length, default, enum, `const`, read-only, write-only, API version, or exact error text from one example or naming convention. Do not transfer a constraint between related fields, such as from path `userId` to response `id`. Add each constraint only when evidence proves that exact field-level guarantee. When evidence shows a field in an observed payload but not its presence guarantee, document its type and example, mark presence as `unconfirmed`, and do not add it to `required`. A TypeScript `?`, JSON Schema `required`, validator branch, explicit requirement, or focused test can prove a presence rule only for the exact field and operation it covers; do not treat a response example as proof that a response field is always returned.

Examples must validate against the supported schema, use realistic synthetic values, and contain no secrets, PII, internal hosts, or production identifiers. Examples illustrate possible values and never strengthen the schema. Do not use `TBD`, prose, or placeholder labels as example values. Prefer one representative request and success response per operation. Add an error example only when its shape or handling is not already clear from a shared error model.

Machine-readable output must itself be valid for its declared specification version. Run the repository's OpenAPI, AsyncAPI, GraphQL, or protobuf validator when available, then validate every example against the emitted schema. Never emit structurally incomplete placeholders such as an OAuth2 security scheme with empty `flows`, an invalid security requirement shape, an unresolved `$ref`, or a `TBD` value in a field whose format forbids it. Never invent placeholder hosts, authorization URLs, token URLs, issuer URLs, callback URLs, scope descriptions, or other security metadata, including values using `example.invalid`, `localhost`, or dummy domains. If evidence proves that authentication or a scope is required but does not identify enough scheme or flow metadata to encode it validly, omit the security scheme and operation-level security object from the machine-readable artifact, state the observed authentication requirement in the completion report, and request the missing evidence. Do not invent a scheme, flow, scope mapping, or authentication failure response.

## Markdown reference shape

Use this order when Markdown is the primary deliverable, omitting every inapplicable section:

1. title and one-sentence scope
2. base URL, content type, authentication, and shared error or pagination rules
3. endpoints grouped by resource or consumer workflow
4. shared schemas referenced by more than one endpoint

Each endpoint should normally contain the method and path, one-sentence purpose, parameters or request body, an explicit presence-status column for every request field, success response, applicable errors, and examples. Mark response presence only when it is evidenced or integration-relevant. Do not add a table of contents, overview essay, architecture narrative, source inventory, evidence matrix, status legend, frontend implementation notes, risk register, recommendations, changelog, or conclusion unless the user explicitly requests it or the repository already requires it.

Use short operation summaries beginning with a direct verb. Avoid duplicating the summary in the description, narrating obvious JSON, or repeating shared authentication, error, pagination, and schema details under every endpoint.

## Uncertainty and conflicts

Do not mix internal analysis into an otherwise settled reference document. Resolve evidence before writing when possible. Omit unsupported optional metadata and constraints. If an unresolved fact blocks implementation or integration, mark the smallest affected operation or field as `TBD` with one neutral sentence describing the decision needed. For a required machine-format field such as OpenAPI `info.version`, reuse an evidenced repository value; otherwise use an explicit draft `TBD` only when the user accepts a draft, or ask for the value before claiming a final contract. Never silently invent `1.0.0`. Do not add a broad Open Questions section for non-blocking observations.

For a requested reconciliation or audit, keep differences separate from the clean target contract. State the conflicting values, their sources, the owner who must decide when known, and the smallest affected fragment. Do not silently choose a side.

## Compatibility and validation

Separate specification, API, and documentation versions only when those versions exist or the user asks for version analysis. Classify an actual proposed change as breaking, non-breaking, or uncertain across wire and semantic behavior; do not add a generic versioning lecture.

Parse JSON or YAML, resolve references, check operation IDs and inventory coverage, validate examples against schemas, and run repository-supported specification or contract checks. Before completion, audit every request field for an explicit presence status and every emitted `required`, nullable, `format`, pattern, range, length, default, enum, `const`, security requirement, status code, and version against its exact evidence. Remove any unsupported constraint instead of keeping it because it looks conventional. For OpenAPI, represent proven presence rules in `required`; if presence is genuinely unconfirmed, do not silently encode it as required or optional—keep the machine artifact valid and report the unresolved field in the completion report or ask for evidence. Create a temporary evidence manifest and run `python scripts/validate_openapi_evidence.py <specification> <evidence.json>`; include one JSON Pointer, optional exact value, and concise source citation for every sensitive claim, then delete the temporary manifest after validation. Treat validator errors as blockers to claiming a valid artifact. Use specification diffs when comparing versions. Report unavailable checks in the work summary, not inside the API reference.

## Final edit

Remove any sentence that does not help a consumer construct a valid request, handle a response, or understand an evidenced contract constraint. Remove empty sections, duplicated facts, generic HTTP teaching, history, implementation speculation, unsupported metadata, and process narration. Call behavior deployed or production only with runtime or deployment evidence. When multiple artifacts are requested, keep them semantically consistent.
