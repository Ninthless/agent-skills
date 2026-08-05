---
name: write-api-docs
description: 'Create, rewrite, reconcile, or review implementation-ready API contracts and integration documentation from requirements, frontend types and mocks, routes, handlers, schemas, tests, runtime evidence, OpenAPI/Swagger, GraphQL, gRPC, webhooks/callbacks, AsyncAPI, and message contracts. Use when the requested deliverable is API documentation, a machine-readable contract, API inventory, compatibility analysis, or frontend/backend contract reconciliation. Support mixed implemented, proposed, conflicting, missing, and uncertain operations in one API set without inventing behavior. Do not use for endpoint/client/SDK implementation, pure UI or database work, generic HTTP/OAuth teaching, test-only runs, or ordinary source review that does not request API contract documentation.'
---
# Write API Docs

## Scope and authority

Create evidence-bounded contracts a provider can implement and a consumer can integrate. Preserve repository terminology, formats, and versioning. Use a primary coordination envelope for the task, then assign authority and status per API group, operation, channel, callback, message, and relevant field. One API set may mix `implemented`, `proposed`, `conflicting`, `missing`, and `uncertain`; never force a global single mode.

For each unit, identify authoritative evidence such as requirements, executable implementation, schemas, tests, runtime observations, or existing specifications. Preserve conflicts and do not invent fields, constraints, permissions, errors, side effects, defaults, or deployment status.

## Task routing

- `create` or `rewrite`: default to the repository-supported machine contract plus concise Markdown. Honor an explicit single-format request and produce only that format.
- `review`: return findings ordered by integration risk, then Open Questions and recommendations. Do not rewrite artifacts or write files unless separately authorized.
- `reconcile`: default to a difference list and only contract fragments that evidence determines. A complete rewrite requires explicit authorization.

## Inventory and protocol routing

Inventory operations with real consumers or explicit requirements. Trace backend evidence from route/group/prefix through middleware, validation, handler, serializer, errors, and tests; trace frontend evidence from use case through client call, types, mocks, states, and tests.

Use OpenAPI paths for REST operations. Distinguish provider-initiated HTTP `webhooks` from operation-bound `callbacks`. Use AsyncAPI for message/channel protocols and document publish/subscribe direction, payload, headers, acknowledgement, retry, ordering, and delivery semantics only when evidenced. Use GraphQL schema and operations for GraphQL, and proto services/messages for gRPC. Do not collapse webhooks, callbacks, and messages into one model.

## Contract coverage

For each operation or message document evidenced identity, purpose, auth/authorization/tenant scope, inputs and locations, media or serialization, success output, errors, empty/pagination/async behavior, idempotency, retry, rate limits, cache behavior, and side effects. Distinguish required, optional, nullable, default, conditional, readOnly, and writeOnly fields. Include constraints, format, units, timezone, precision, and unknown-field behavior only when proven.

Examples must validate against schemas, stay consistent across artifacts, use synthetic values, and contain no secrets, PII, internal hosts, or production identifiers.

## Compatibility and validation

Separate specification, API, and documentation versions. Classify compatibility changes as breaking, non-breaking, or uncertain across source, wire, and semantic behavior. Inspect strict clients and unknown-field handling before calling additions safe.

Parse JSON/YAML, run repository validators, resolve references, check unique operation IDs and inventory coverage, validate examples, run supported smoke/contract tests, and use spec diffs where available. Report unavailable checks exactly.

## Output rules

Machine contract and Markdown must agree when both are requested. Label authority and status at the smallest useful group/operation level. Call behavior deployed or production only with runtime/deployment evidence. Use Open Questions only for independent decisions blocking implementation or integration. Keep prose concise and omit generic teaching, history, empty sections, and unsupported metadata.
