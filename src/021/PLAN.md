# TS-21 Gap Analysis & Implementation Plan

TODO - Finish this!!

A gap analysis between the PayPal API Style Guide (`TODO/api-standards-master/api-style-guide.md`) and PayPal API Patterns (`TODO/api-standards-master/patterns.md`) against TS-21's 19 include files. This plan identifies what's missing or significantly under-covered in TS-21, organized by priority.

---

## Priority Legend

| Symbol | Meaning |
|--------|---------|
| 🔴 | High priority — fundamental API design topic with a significant or complete gap |
| 🟡 | Medium priority — important topic with meaningful coverage gaps |
| 🟢 | Low priority — refinement or supplementary guidance that would improve completeness |

---

## 🔴 High Priority

### 1. Error Handling

**Current state:** Section 16 (`16-payloads.adoc`) defines a `messages` array with `MessageItem` objects (`type`, `code`, `title`, `description`), but the section is a `// TODO` stub.

**Missing:**
- Error response schema — `name`, `details[]` (containing `field`, `value`, `issue`, `location`), `debug_id`, `message`, `links`
- JSON Pointer usage for identifying fields in error responses (e.g. `#/credit_card/expire_month`)
- Input validation error classification — malformed JSON → `400`, validation errors → `400`, semantic errors → `422`
- Bulk error handling — `errors[]` array for multiple heterogeneous error types
- Error declaration in API specifications — how to reference error schemas in OpenAPI
- Error samples in documentation — requirement to show error scenarios in user guides
- Error Catalog system — externalizing and localizing error messages via catalog JSON files (`error_catalog.json`, `error_spec.json`, `error_spec_issue.json`, etc.)
- Status reporting rules — 2xx responses MUST NOT contain error codes; 4xx/5xx responses MUST return an error response body; 5xx responses should limit information to avoid exposing implementation details

**Target section:** Expand section 16 (`16-payloads.adoc`) or create a new dedicated error handling section.

---

### 2. Deprecation Framework

**Current state:** TS-21 has no deprecation guidance at all.

**Missing:**
- `x-deprecated` annotation in API specifications (OpenAPI) for marking deprecated elements
- Deprecation of individual API elements: resources, methods, query parameters, headers, schema properties, enum values
- Schemas for `x-deprecated`: `deprecatedResource`, `deprecatedParameter`, `deprecatedSchema`, `deprecatedSchemaProperty`
- Runtime deprecation notification — custom response header to inform clients they've used deprecated elements
- Requirement that deprecated elements must remain supported for the life of the major version

**Target section:** New section or expand section 17 (`17-versioning.adoc`).

---

### 3. API Lifecycle & EOL Policy

**Current state:** Section 17 (`17-versioning.adoc`) covers the expanding contract pattern and basic breaking change rules, but is missing lifecycle and retirement guidance.

**Missing:**
- API lifecycle states — `PLANNED` → `BETA` → `LIVE` → `DEPRECATED` → `RETIRED`
- Minor version handling — minor versions must be backwards compatible; retired immediately when a newer minor version goes LIVE
- Detailed backwards compatibility rules for URIs — no new required query params, no behavioral changes for existing params, no status code changes, no HTTP verb changes, no header name/type changes
- Detailed backwards compatibility rules for JSON representations — existing properties must keep same name and type, array content types must not change, new properties must not be mandatory, HATEOAS `rel`/`href` values must remain stable, enum values must not change
- EOL policy — different rules for minor vs major version retirement; minimum deprecation period for major versions; immediate retirement if no clients
- Replacement major version justification — business case, API design, migration strategy requirements before introducing a new major version

**Target section:** Expand section 17 (`17-versioning.adoc`).

---

### 4. Missing HTTP Status Codes & Method-to-Status Mapping

**Current state:** Section 05 (`05-http-status-codes.adoc`) lists many status codes but is missing several and lacks mapping guidance.

**Missing status codes:**
- `406 Not Acceptable` — for unsupported `Accept` media types
- `415 Unsupported Media Type` — for unsupported request `Content-Type`
- `422 Unprocessable Entity` — for semantic validation errors (mentioned in section 08 but not in the status codes section)
- `429 Too Many Requests` — for rate limiting
- `412 Precondition Failed` — for ETag/concurrency (mentioned in section 13 but not in the status codes section)

**Missing guidance:**
- Method-to-status-code mapping table — which status codes are appropriate for each HTTP method (GET→200/400/404, POST→200/201/202/400/404/422, PUT→200/204/202/400/404/422, PATCH→200/204/400/404/422, DELETE→200/204/400/404/422)
- Allowed status code list — explicit enumeration of the only status codes APIs may return (prohibiting returning any status code not in the list)
- Status reporting rules — success/failure applies to the whole operation; 5xx should not be used for validation/logic errors

**Target section:** Expand section 05 (`05-http-status-codes.adoc`).

---

## 🟡 Medium Priority

### 5. JSON Schema & Primitive Type Guidance

**Current state:** TS-21 references TS-18 for JSON Schema guidance, but the PayPal standard has detailed rules that TS-21 doesn't surface.

**Missing:**
- `anyOf`/`oneOf` prohibition — should not be used due to codegen, documentation, and deserialization issues; prefer flat structures with optional fields
- `allOf` usage — only for extending objects
- `additionalProperties: false` prohibition — must not be set as it breaks backward compatibility
- `readOnly` property — for immutable fields in PUT/PATCH operations
- String constraints — `minLength`/`maxLength` must always be defined; `maxLength` 255 for enums; practical DB limits
- Enumeration safety — `enum` keyword risks for backwards compatibility; use `string` + `pattern` for changeable values
- Number handling — never use `number` type (use `string` for decimals); `integer` only for 32-bit signed range with explicit min/max
- Array constraints — `maxItems` must always be defined (max 32767); `minItems` should be defined (0 or 1)
- Null prohibition — APIs MUST NOT produce or consume `null` values; explanation of cross-language issues

**Target section:** May belong in TS-18, but should be referenced from TS-21 section 16 (`16-payloads.adoc`).

---

### 6. Common Types

**Current state:** TS-21 references TS-18 for JSON Schema common types, but doesn't cover any specific common types.

**Missing:**
- Address — portable address format compatible with hCard, Google i18n-api, HTML5 autofill
- Money — non-negative, string value, currency code required, sub-currency handling
- Percentage/Interest Rate/APR — fixed-point decimal string, represented as percentage (not fraction)
- Internationalization types — ISO 3166-1 country codes, ISO 4217 currency codes, BCP-47 language tags, ISO-3166-2 provinces, IANA timezone database
- Date/Time guidance — RFC 3339 `date-time` format, UTC-only in responses, accept UTC offsets in requests, separate timezone field for business logic, floating times, date-only and time-only formats

**Target section:** May belong in TS-18, with cross-references from TS-21 section 16 (`16-payloads.adoc`).

---

### 7. Bulk Operations

**Current state:** TS-21 has no coverage of bulk operations.

**Missing:**
- Homogeneous bulk operations — same operation on collection of same-type resources
- Heterogeneous bulk operations — explicitly NOT recommended; refer to standards like OData Batch Specification if truly needed
- Bulk request format — `items[]` array
- Bulk response format — `batch_result[]` with per-item success or error objects
- Atomic vs partial failure — atomic (all-or-nothing) or partial (overall `200 OK` with per-item status)
- Response-request correlation — JSON Pointer expressions with filter syntax (e.g. `/items/@account_number=='2097094104180012047'/address_id`) or same-order responses with index-based pointers (e.g. `/items/0/address_id`)
- HTTP status codes for bulk — atomic uses normal REST codes; partial uses `200 OK` with per-item status; async uses `202 Accepted`
- Bulk replace and update — if the bulk add creates a first-class batch resource (uniquely identifiable by an ID), subsequent `PUT`/`PATCH` operations can use this ID to update constituent elements as if updating a single resource
- Atomicity for replace/update — every effort should be made to make bulk replace/update atomic; when not possible, response should be similar to partial response of bulk add

**Target section:** New section, or expand section 11 (`11-actions.adoc`) or section 07 (`07-collections.adoc`).

---

### 8. File Upload Patterns

**Current state:** TS-21 has no coverage of file upload patterns.

**Missing:**
- Standalone file upload — dedicated URI with `multipart/form-data`, then reference uploaded file URI in subsequent requests
- File upload as attachment — `multipart/mixed` or `multipart/related` for combining file upload with request body
- Prohibition on Base64 encoding files within JSON bodies

**Target section:** New section, or expand section 11 (`11-actions.adoc`).

---

### 9. Content Negotiation

**Current state:** TS-21 mentions JSON as the preferred format but has no content negotiation rules.

**Missing:**
- `Accept` header — clients SHOULD send it; server behavior when `application/json` not acceptable
- `Accept-Charset` — should include `utf-8`
- `Content-Type` requirements — must include charset=UTF-8 for text types; must be sent with all request bodies
- `Content-Language` — should be provided in responses; default `en-US`
- `406 Not Acceptable` response for unsupported media types
- `415 Unsupported Media Type` response for unsupported request content types

**Target section:** Expand section 15 (`15-headers.adoc`) or section 04 (`04-http-methods.adoc`).

---

### 10. Detailed Backwards Compatibility Rules

**Current state:** Section 17 (`17-versioning.adoc`) mentions the expanding contract pattern but lacks detailed compatibility rules.

**Missing:**
- URI backwards compatibility rules — no new required query params, no behavioral changes for existing params, no status code changes, no HTTP verb changes, no header name/type changes
- JSON representation backwards compatibility rules — existing properties must keep same name and type, array content types must not change, new properties must not be mandatory, HATEOAS `rel`/`href` values must remain stable, enum values must not change

**Target section:** Expand section 17 (`17-versioning.adoc`).

---

## 🟢 Low Priority

### 11. Naming Conventions

**Current state:** TS-21 covers resource naming (lowercase hyphen-delimited) but is missing field-level naming rules.

**Missing:**
- Field naming convention — explicit rule for JSON field names (standardize on one convention: snake_case or camelCase)
- Boolean prefix prohibition — `is_` or `has_` prefixes should not be used for boolean fields
- Array field naming — should use plural nouns
- Enum naming — uppercase alphanumeric + underscore
- Link relation naming — must be lowercase
- Query parameter naming — explicit convention (underscores vs hyphens)
- File naming — underscore syntax for JSON schema files

**Target section:** Expand section 06 (`06-urls.adoc`) or section 16 (`16-payloads.adoc`).

---

### 12. Resource Identifier Rules

**Current state:** TS-21 mentions UUIDs in section 08 but lacks detailed identifier guidance.

**Missing:**
- Prohibition on database sequence numbers as resource identifiers
- HMAC-based identifiers as an alternative to UUIDs
- Sub-resource ID scoping — sub-resource IDs must be scoped within parent resource only
- No consecutive resource identifiers — `/{resource}/{resource_id}/{resource_id}` is not acceptable
- Percent-encoding requirement for resource IDs and query parameter values
- ASCII/non-UTF-8 recommendation for resource IDs

**Target section:** Expand section 08 (`08-resources.adoc`).

---

### 13. Query Parameter Multi-Value Handling

**Current state:** Section 07 (`07-collections.adoc`) covers pagination, filtering, searching, and sorting but not multi-value parameters.

**Missing:**
- Multiple values for same query parameter — repeated params recommended (`?status=CLOSED&status=INVALID`); comma-separated as alternative (`?statuses=CLOSED,INVALID`); parameter must be marked as repeatable in API spec
- POST with query parameters — allowed for paged search results to enable hypermedia links
- Cache-friendly APIs — GET with query params preferred over POST when cacheability matters
- Query parameters on single resources — should not be used
- Search via POST — when search criteria is too complex for query parameters (complex syntax or URL length limitations), use `POST` with a request body to specify search parameters; pagination MUST be maintained in query parameters (not the request body) so that HATEOAS links can include `next`, `previous`, `first`, `last` page relationships in the URL

**Target section:** Expand section 07 (`07-collections.adoc`).

---

### 14. HATEOAS Use Case Patterns

**Current state:** TS-21 covers HATEOAS link structure well but is missing the use case patterns.

**Missing:**
- Single API entry point — every API should strive for a single entry point with HATEOAS links to all other methods. Three specific patterns:
  - **Pattern 1 (top-level resource):** A natural top-level collection or object serves as the entry point (e.g., `GET /users`)
  - **Pattern 2 (multi-step workflow):** A complex multi-step operation has a logical entry point that returns links to subsequent steps based on runtime state (e.g., `/apply-credit` → `apply.sign` → approval)
  - **Pattern 3 (utility API):** For APIs with independent controller-style utility methods, provide a `/actions` resource that returns links to all available methods (e.g., `GET /actions` → links to `/generate-otp`, `/encrypt`, `/decrypt`)
- Service-controlled flow — links change based on resource state (e.g., `cancel` link only shown for PENDING orders, not COMPLETED); prevents clients from embedding business logic; enables server to add new state transitions without client changes
- Error resolution links — error responses include HATEOAS links to help resolve the error (e.g., `422` response with `activate` link when account is inactive)
- Bandwidth saving — `Prefer: return=minimal` with HATEOAS links for composite APIs
- Standard link relation types beyond pagination — `create`, `edit`, `delete`, `replace`, `collection`, `latest-version`, `search`, `up`

**Target section:** Expand section 16 (`16-payloads.adoc`) or section 11 (`11-actions.adoc`).

---

### 15. Header Propagation & Prohibitions

**Current state:** Section 15 (`15-headers.adoc`) covers header naming, non-standard header prefixes, `Prefer` header, and response caching, but is missing several items.

**Missing:**
- Header propagation — services MUST pass relevant custom + standard headers to downstream services
- Prohibition of `Location` and `Link` headers for `201`/`3xx` responses — use HATEOAS links in response body instead
- `Prefer` header tokens — `respond-async` (for async processing), `read-consistent`, `read-eventual-consistent`, `read-cache` (for read consistency preferences)
- Assumptions about header availability — intermediaries may drop headers; business logic should not depend on headers

**Target section:** Expand section 15 (`15-headers.adoc`).

---

### 16. Service Design Principles

**Current state:** Section 01 (`01-general-design-principles.adoc`) covers RESTful architectural principles (Stateless, Uniform, Cacheable, Layered System) but is missing service-oriented design principles.

**Missing:**
- Loose Coupling — services should be independent and avoid tight dependencies
- Encapsulation — hide implementation details behind stable interfaces
- Stability — APIs should evolve without breaking existing clients
- Reusability — services should be designed for reuse across multiple consumers
- Contract-based — explicit contracts between service providers and consumers
- Consistency — uniform patterns across all APIs
- Ease of Use — APIs should be intuitive and self-describing
- Externalizability — APIs should be designed for both internal and external use

**Target section:** Expand section 01 (`01-general-design-principles.adoc`).

---

### 17. Input/Output Strictness

**Current state:** TS-21 mentions Postel's Law only in the context of trailing slashes in section 06.

**Missing:**
- Strictness principle — APIs MUST be strict in what they produce, SHOULD be strict in what they consume
- Postel's Law caveat — must be weighed against the dangers of permissive parsing

**Target section:** Expand section 01 (`01-general-design-principles.adoc`) or section 16 (`16-payloads.adoc`).

---

### 18. Reified Actions Pattern

**Current state:** TS-21 section 11 (`11-actions.adoc`) covers actions well, including composite actions, transient operations, resource-scoped actions, and the guidance to prefer resource-oriented design where possible. However, it does not describe the reified actions pattern as a resource-oriented alternative to controller-style actions.

**Missing:**
- Reified actions — when there is a need to see the history of actions taken on a resource, reify the action verb into a plural noun collection (e.g., `execute` → `executions`, `cancel` → `cancellations`) and expose it as a sub-resource collection via `GET /{resource}/{resource_id}/{reified-action}`
- Event sourcing alignment — the reified actions pattern aligns with event sourcing concepts, where the history of events can drive further functionality
- Mixed pattern guidance — simple state transitions (e.g., changing a `status` field) should still use `PUT`/`PATCH`, while complex operations requiring extra data (e.g., a cancellation reason) should use actions; it is appropriate to mix both patterns on the same resource to minimize the number of operations

**Target section:** Expand section 11 (`11-actions.adoc`).

---

## Summary Table

| # | Priority | Gap | Target Section | Effort |
|---|----------|-----|----------------|--------|
| 1 | 🔴 High | Error handling (schema, validation, catalog) | Expand section 16 or new section | Large |
| 2 | 🔴 High | Deprecation framework | New section or expand section 17 | Medium |
| 3 | 🔴 High | API lifecycle & EOL policy | Expand section 17 | Medium |
| 4 | 🔴 High | Missing status codes & method-to-status mapping | Expand section 05 | Small |
| 5 | 🟡 Medium | JSON Schema & primitive type guidance | TS-18 or expand section 16 | Medium |
| 6 | 🟡 Medium | Common types (money, address, i18n, dates) | TS-18 or expand section 16 | Medium |
| 7 | 🟡 Medium | Bulk operations | New section or expand section 11/07 | Medium |
| 8 | 🟡 Medium | File upload patterns | New section or expand section 11 | Small |
| 9 | 🟡 Medium | Content negotiation | Expand section 15 or 04 | Small |
| 10 | 🟡 Medium | Detailed backwards compatibility rules | Expand section 17 | Small |
| 11 | 🟢 Low | Naming conventions (fields, enums, booleans, arrays) | Expand section 06 or 16 | Small |
| 12 | 🟢 Low | Resource identifier rules | Expand section 08 | Small |
| 13 | 🟢 Low | Query parameter multi-value handling | Expand section 07 | Small |
| 14 | 🟢 Low | HATEOAS use case patterns | Expand section 16 or 11 | Small |
| 15 | 🟢 Low | Header propagation & prohibitions | Expand section 15 | Small |
| 16 | 🟢 Low | Service design principles | Expand section 01 | Small |
| 17 | 🟢 Low | Input/output strictness | Expand section 01 or 16 | Small |
| 18 | 🟢 Low | Reified actions pattern | Expand section 11 | Small |
