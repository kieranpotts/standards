# TS-21: HTTP APIs

This is a compact version of technical standard TS-21 for AI agents.

Use this when designing or reviewing HTTP APIs — primarily public-facing APIs
for integration into third-party client applications, but most guidelines also
apply to private intra-organization HTTP APIs. Covers the RESTful style, HTTP
methods, status codes, URLs, collections, resources, sub-resources, actions,
asynchronous operations, concurrency control, health checks, headers, payloads,
versioning, and documentation.

Do NOT use this for general network API concerns (inter-service communication,
rate limiting, circuit breakers, observability) — those are covered by
[TS-20: Network APIs](../020/AGENTS.md). For webhook patterns (asynchronous
event notifications to clients) see [TS-22: Webhooks](../022/AGENTS.md). For
version-numbering semantics see [TS-11: Versioning](../011/AGENTS.md). For JSON
Schema type libraries see [TS-29: JSON Schema](../029/AGENTS.md).

## Rules

### General design principles

- **HTTP APIs SHOULD follow the RESTful architectural style.**

  In practice, a RESTful API repurposes the semantics of HTTP as a messaging and
  encoding protocol (not merely a transport): URLs represent resources and
  collections, HTTP methods represent CRUD-like operations, and HTTP status
  codes represent outcomes. A RESTful API is also:

  - **Stateless**: each request SHOULD contain all information necessary for the
    server to understand and fulfil it; most client requests SHOULD NOT depend
    on stored server context (with exceptions for security measures). Simplifies
    the server and improves scalability.
  - **Uniform**: a consistent URL structure for resources/collections, a
    consistent subset of HTTP methods and status codes, a consistent payload
    format and schema, and composition from a common library of types and
    patterns. Improves UX and supports code reuse (libraries, SDKs).
  - **Cacheable**: responses SHOULD be cacheable wherever possible, reducing
    server load, latency, and supporting fault tolerance/availability.
  - **A layered system**: cross-cutting concerns (security, caching) implemented
    in discrete layers spanning all endpoints.

- **Prioritize a useful interface over religious adherence to any architectural
  style.**

  If an API is a thin layer around a legacy system that doesn't fit the RESTful
  model, deviate and focus on a functional abstraction of the underlying system.
  Even predominantly RESTful APIs MAY include RPC-like "actions" (see Actions
  below). The best design makes it as easy as possible for clients to interact
  with the underlying system.

- **HATEOAS and code-on-demand are OPTIONAL and not applicable to most HTTP
  APIs.**

  HATEOAS (hypermedia as the engine of application state) is intrinsic to the web
  but not useful for most programmatic-integration APIs — it MAY be appropriate
  for APIs consumed directly by humans exploring evolving resources. Code on
  demand (server sends executable code) is central to the web but not
  applicable to HTTP APIs.

### Authentication, authorization, and security

- **Authentication and authorization MUST be implemented for all HTTP APIs,
  including private (internal network) APIs.**

  Especially important for operations that modify data.

- **Security measures MUST be implemented for both public and private APIs. Do
  not assume private/internal networks are secure.**

  All input MUST be validated and sanitized to prevent vulnerabilities (SQL
  injection, XSS, CSRF) — even input from internal systems you control and
  trust. Doing so reduces the potential blast radius of breaches in any one
  service.

### HTTP methods

- **HTTP methods MUST be used for their designated purpose and APIs MUST use
  only this subset: `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, `QUERY`.**

  - **`GET`** (Read, safe, idempotent): retrieve resources/collections. MUST NOT
    modify state or have other side effects.
  - **`HEAD`** (Read, safe, idempotent): same as `GET` but the response body is
    empty (headers only). RECOMMENDED that all `GET` endpoints also support
    `HEAD` (useful for checking resource existence without downloading the full
    representation).
  - **`POST`** (Create, not safe, not idempotent): create a new resource. The
    server MUST generate a new resource identifier and return a full
    representation including the new identifier and server-generated properties.
    Not natively idempotent, but idempotency can be achieved by clients including
    a unique idempotency key (eg. `request_id`).
  - **`PUT`** (Create/Update, not safe, idempotent): fully replace a resource
    with the request payload, or create a new resource where the client takes
    responsibility for generating the unique identifier.
  - **`PATCH`** (Update, not safe, idempotent): partial updates. The payload
    SHOULD contain only the fields being updated. SHOULD be designed to be
    idempotent, although HTTP does not require this.
  - **`DELETE`** (Delete, not safe, idempotent): delete a resource. Should be
    repeatable, always with a positive response even if the resource is already
    deleted. Clients MUST NOT send a body with `DELETE` requests.
  - **`QUERY`** (Read, safe, idempotent): defined by
    [RFC 10008](https://www.rfc-editor.org/info/rfc10008/). Retrieve resources
    using a request payload for complex query criteria that cannot be encoded
    in a URL. Like `GET`, MUST NOT modify state or have side effects. Responses
    MAY be cached, but the cache key MUST incorporate the request body. `QUERY`
    is a recent addition (mid-2026) with non-universal support; until tooling
    matures, SHOULD be used only where end-to-end support can be guaranteed
    (private APIs) and is NOT RECOMMENDED for public-facing APIs.

  `OPTIONS`, `TRACE`, and `CONNECT` are technical methods supporting the HTTP
  protocol itself and are not part of API interface definitions. Where
  operations may be long-running, it is RECOMMENDED to implement them using
  asynchronous communication patterns (method behavior is identical; only status
  codes and payload delivery differ).

### HTTP status codes

- **Appropriate HTTP status codes MUST be used in responses; the supported
  subset MUST be documented as part of the API's interface definition.**

  Commonly-used codes:

  - **1xx (informational)**: `100 Continue` (initial part received; client
    should continue — used for large payloads).
  - **2xx (success)**: `200 OK`; `201 Created` (new resource created); `202
    Accepted` (asynchronous — accepted for later processing, outcome not yet
    known); `204 No Content` (success, no content — MUST be returned with an
    empty body).
  - **3xx (redirection)**: `301 Moved Permanently` (new URL MUST be specified);
    `302 Found` (temporarily under a different URL).
  - **4xx (client error)**: `400 Bad Request`; `401 Unauthorized` (requires
    authentication); `403 Forbidden` (understood but refusing to authorize);
    `404 Not Found`; `405 Method Not Allowed` (method not allowed on the target
    resource, but the resource exists and other methods can run on it).
  - **5xx (server error)**: `500 Internal Server Error`; `502 Bad Gateway`
    (gateway/proxy received an invalid upstream response); `503 Service
    Unavailable` (maintenance or overload).

### URLs

- **URLs identify resources, collections, and actions; the forward slash `/`
  delimits path segments.**

  Be consistent with trailing slashes (RECOMMENDED to omit them in
  documentation). An API SHOULD accept requests with or without a trailing
  slash but SHOULD NOT respond with a redirect to the canonical version
  (Postel's Law: be liberal in what you accept, conservative in what you send).

- **HTTP APIs MUST be versioned; version information SHOULD be encoded in the
  URL path.**

  HTTP APIs MUST use [Semantic Versioning](https://semver.org/) per
  [TS-11](../011/AGENTS.md), but only the major version number needs to be
  exposed in the URL. RECOMMENDED that the major version number be the first
  path segment (eg. `/v1`), making version-specific behavior easier for clients
  and parallel major-version maintenance easier on the server.

- **The next path segment after the version SHOULD be a namespace grouping
  related resources, collections, and actions.**

  Namespaces reflect the customer's perspective of how the product works, not
  necessarily the internal system structure or business domains. SHOULD be nouns
  but MAY be singular or plural as appropriate. Good practice: open a `GET`
  endpoint for each namespace root listing available resources and operations.

  ```
  /v{major}/{namespace}
  ```

- **Remaining segments identify resources and collections; consistent path
  components SHOULD refer to the same resources across endpoints.**

  Templates:
  ```
  GET    /v{major}/{namespace}/{resource}
  GET    /v{major}/{namespace}/{resource}/{resource_id}
  POST   /v{major}/{namespace}/{resource}/{resource_id}
  PUT    /v{major}/{namespace}/{resource}/{resource_id}
  PATCH  /v{major}/{namespace}/{resource}/{resource_id}
  DELETE /v{major}/{namespace}/{resource}/{resource_id}
  ```

  Sub-resources and sub-collections MAY be supported. `{resource}` and
  `{sub_resource}` SHOULD be nouns — singular form where there will only ever be
  one instance, plural form for collections. Resource-oriented endpoints SHOULD
  use lowercase hyphen-delimited slugs (eg. `charge-points`, `credit-cards`).

### Collections

- **A collection is a list of multiple resources of the same type plus related
  metadata; collections and their resources SHOULD be named consistently across
  endpoints.**

  Resource representations in collections MAY be partial; clients MAY need to
  fetch individual resources for full representations.

- **Any collection that could contain a large, potentially unbounded list SHOULD
  implement pagination.**

  Pages referred to by `page` and `per_page` query parameters (`per_page` is a
  non-zero positive integer; `page` is 1 or more). `per_page` SHOULD be optional
  (server falls back to a sensible default); `page` SHOULD be optional (server
  MUST return the first page if not provided — default value MUST be 1). Both
  MUST be validated by the server; `400 Bad Request` for semantically invalid
  values. If the requested range is outside available results (eg. `page=2`
  when there are only 50 results), return `200 OK` with an empty result list,
  not `404 Not Found`. A `page_token` parameter MAY be used to optimize query
  execution based on the previous page's result set. Responses MAY include
  `total_items` and `total_pages` metadata; where providing these requires
  expensive queries, clients SHOULD be able to opt in (eg.
  `?include_totals=true`). Hypermedia links with `rel` attributes for "next",
  "previous", "first", and "last" pages SHOULD be included; the `page` and
  `per_page` parameters MUST be maintained for each link.

- **Collections MAY be filtered by default.**

  Resources a user is not authorized to access MUST NOT be included; if all
  resources are unauthorized, `403 Forbidden` is appropriate. Additional
  optional filtering via query parameters: time range (`start_time` /
  `{property_name}_after`, `end_time` / `{property_name}_before` — ISO-8601
  strings mapping to time fields in the representation), search (`q` — a single
  parameter MAY search across multiple fields), and sorting (`sort_by`
  dimension mapping to an attribute; `sort_order` one of "asc" or "desc"). Time
  filtering parameters SHOULD be consistent across all supporting endpoints.
  The default sort field and order MUST be documented for each collection.

- **For empty collections, return `200 OK` with an empty `items` array, not `404
  Not Found` — the collection exists, it is just empty.**

  Invalid query parameters SHOULD be signalled with `400 Bad Request`.

### Resources

- **Resource identifiers SHOULD be unique across all resources of all types;
  UUIDs are RECOMMENDED.**

  Identifiers for sensitive data SHOULD be non-sequential and preferably
  non-numeric; immutable string identifiers SHOULD be used where data is used as
  a subordinate (for readability and debugging). If a provided identifier is not
  found (even if "soft deleted"), return `404 Not Found`; otherwise `200 OK`.

- **Update resources with `PUT` (full replace) or `PATCH` (partial).**

  Input shape SHOULD be consistent with the GET representation. For `PUT`,
  system-calculated values (`create_time`, `update_time`) SHOULD be optional
  and ignored on deserialization. For `PATCH`, clients SHOULD omit these fields;
  the server SHOULD return `400 Bad Request` if they are included (the client
  cannot update them, so trying is a client error). [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902)
  MAY be implemented for `PATCH` (clients send a list of operations — "add",
  "remove", "replace", "move", "copy", "test" — with JSON Pointer paths;
  fixed-schema resources need only "add", "remove", "replace"). After a
  successful update, `PUT`/`PATCH` SHOULD normally respond with `204 No
  Content`; `200 OK` with the updated resource MAY be returned where clients
  need system-calculated field updates, or clients may opt in via
  `Prefer:return=representation`. Failed validation MUST receive `400 Bad
  Request`; attempts to modify read-only fields or resources in non-updatable
  states are also `400`. Where interaction with upstream servers/external APIs
  is required, `422 Unprocessable Entity` MAY be more appropriate than `400`.

- **`DELETE` operations MUST be idempotent.**

  Successful `DELETE` MUST always respond with `204 No Content`, even if the
  resource is already deleted — `404 Not Found` is not appropriate (it suggests
  the resource never existed). Clients can use `GET` to verify existence prior to
  `DELETE`. `410 Gone` MAY be returned for a resource that unexpectedly
  disappeared (expired, retention cleanup) to tell the client it had already
  existed. To support the widest range of clients, it is good practice NOT to
  require a `DELETE` request body.

- **Create resources with `POST` (server generates identifier) or `PUT` (client
  generates identifier).**

  `PUT` is idempotent by default (the payload carries the client-generated ID).
  `POST` is NOT idempotent by default — duplicates may be created on retry;
  where this must be prevented, clients MUST include a unique request identifier
  (eg. `request_id`) and the server uses it to process only the first instance.
  For `PUT`, system-calculated read-only fields SHOULD be optional and ignored
  on deserialization; for `POST`, clients SHOULD omit them and the server SHOULD
  return `400 Bad Request` if included. Both payloads MAY include only a subset
  of fields (server fills optional fields with defaults). Minimize required
  fields and implement as many default/fallback values as reasonable. Both
  successful `POST` and `PUT` creation operations MUST be signalled by `201
  Created` with a representation of the created resource (including
  server-generated fields) in the response body. Response messages SHOULD
  include hypermedia links representing available operations on the new
  resource.

### Sub-resources and sub-collections

- **Sub-resources and sub-collections SHOULD be used sparingly and only where
  essential.**

  Where a resource can exist independently, elevate it to a top-level resource.
  If one resource cannot exist without another, it is a candidate for a
  sub-resource. Sub-resources require composite keys (multiple identifiers),
  which is a source of client complexity. Even with tight coupling, look to
  promoting dependent resources to top-level resources where practical. Where
  necessary, try to have no more than one level of sub-resources (two levels of
  resources total) — complexity grows exponentially with each additional tier.

- **Sub-resources MUST have a named type.**

  `/v{major}/{namespace}/{resource}/{resource_id}/{sub_resource_id}` is not
  acceptable because `sub_resource_id` has ambiguous meaning. Use
  `/v{major}/{namespace}/{resource}/{resource_id}/{sub_resource}/{sub_resource_id}`
  instead. Linking identifiers to types supports extensibility and different
  identifier naming conventions per sub-resource type.

- **Singleton sub-resources are identified by a static sub-resource name (not a
  dynamically-generated identifier) and named using singular nouns.**

  ```
  /v{major}/{namespace}/{resource}/{resource_id}/{sub_resource}/{sub_resource_name}
  ```

  There is a one-to-one relationship between a resource and each of its
  singleton sub-resources; they are expected to always exist if the parent
  exists (they may have null values — do not return `404 Not Found` if a
  singleton sub-resource does not exist; return `null`). Singleton sub-resources
  are attached to their parent and SHOULD be created/updated via operations on
  the parent (no dedicated endpoints). They SHOULD NOT duplicate resources from
  other collections but SHOULD be unique to their parent.

### Safeness and idempotency

- **Safe operations (read-only): `GET` and `HEAD`. Idempotent operations:
  `GET`, `HEAD`, `PUT`, `DELETE` — HTTP APIs MUST implement these as
  idempotent.**

  `PATCH` is not specified by HTTP as safe or idempotent, but it is strongly
  RECOMMENDED to implement it as idempotent. `POST` is by definition neither
  safe nor idempotent — for most APIs it will need to be implemented as
  idempotent to avoid unwanted duplicates (there may be legitimate exceptions,
  eg. a "like" toggle).

- **Idempotency keys MUST be used to implement idempotency in `POST`, `PUT`,
  `PATCH`, and `DELETE` as required.**

  An idempotency key is generated client-side and is a unique identifier for
  each discrete request; the server processes only the first instance and
  ignores subsequent requests with the same key, returning the _same response_
  as for the first request. Idempotency keys also double as correlation IDs
  and trace IDs — RECOMMENDED to implement universally across all operations
  including `GET` and `HEAD`. In HTTP APIs, the `X-Request-Id` header SHOULD be
  used as the idempotency key. If the client does not provide one, the server
  MAY generate one, though for most use cases responding with `400 Bad Request`
  and a documentation link is more appropriate. Whether client- or
  server-generated, the key MUST be returned in response messages (also in
  `X-Request-Id`). Each key MUST be unique and MUST NOT be reused with different
  payloads; for uniqueness across all clients, UUID v4 is RECOMMENDED. If a
  client reuses a key with a different payload, the server MUST reply with
  `422`. The server MUST cache response payloads against their keys and return
  the cached response for subsequent requests with the same key, even if the
  status is not `200 OK`. Key validity SHOULD be time-based (default 24 hours)
  so the server can purge cached payloads; after expiry, return `400 Bad
  Request`.

### Actions

- **Actions are standalone RPC-like operations that don't fit the RESTful
  resource model (eg. login, logout, reset password, charge a credit card,
  resend a notification, configure permissions).**

  Prefer designing as much of the API as possible around the resource model and
  augment with actions where operations don't fit. Don't force everything into
  the resource model for purity. Composite actions mutate multiple resources in
  a single transaction (eg. "refund" changing payment, customer, and merchant
  accounts). Transient actions do not mutate state (eg. a "dry run" that
  validates input). Actions carry trade-offs: action-oriented APIs can be harder
  to scale (more URLs, less test-code reuse), but some operations are simply
  better expressed as actions.

- **Actions MUST be performed using `POST`, except for read-only actions (logs,
  reports) which MUST use `GET` (for client-side caching — `POST` responses are
  not cacheable).**

- **Action URLs use lowerCamelCase verbs (eg. `activateAccount`,
  `cancelSubscription`, `validateEmail`), distinguishing them from
  resource-oriented endpoints (hyphen-delimited slugs).**

  The name SHOULD suggest the CRUD operation type rather than baking it into
  the HTTP method; typically start with a verb and use the singular form.

- **Scope actions to namespaces wherever possible; actions operating across
  multiple namespaces go in the API root.**

  ```
  POST|GET /v{major}/{action}
  POST|GET /v{major}/{namespace}/{action}
  POST    /v{major}/{namespace}/actions/{action}
  ```

  Actions and resources MAY coexist in the same namespace, but all actions
  within a namespace MUST only operate on resources in the same namespace (if
  not achievable, elevate to global scope). A good practice: group actions in
  a collection named "actions" within each namespace; a
  `GET /v{major}/{namespace}/actions` endpoint MAY list available actions.

- **Resource-scoped actions: `POST /v{major}/{namespace}/{resource}/{resource_id}/actions/{action}`.**

  Useful for separating business processes from core resource state changes.
  A classic use case: attaching freeform comments to a cancellation (comments
  aren't part of the subscription model) — also works around `DELETE`'s
  no-payload constraint. Actions SHOULD be terminal resources (no sub-resources
  or sub-actions relative to them). Successful status codes: `200` (action
  executed, response body contains the result); `201` (action created one or
  more new resources — appropriate for composite actions); `204` (no payload —
  often appropriate for actions triggering out-of-band processes like
  notifications). Appropriate `4XX`/`5XX` error codes MAY be returned.

### Asynchronous operations

- **Prefer synchronous operations; use asynchronous where necessary or
  beneficial (long-running tasks, external-system interactions with
  unpredictable response times).**

  Responses to resource creation, update, and deletion operations SHOULD return
  `202 Accepted` (request accepted for processing, not yet completed). The
  response body MAY include hypermedia links to created/updated resources. Two
  polling options: the final resource URL (where the ID and path are known —
  `GET` returns `404 Not Found` until the resource is ready or after deletion);
  or a temporary status URL with a request identifier. It is RECOMMENDED that
  all HTTP APIs with asynchronous processing also support a webhook clients MAY
  implement for push notifications (see [TS-22: Webhooks](../022/AGENTS.md)).
  Endpoints MAY support both synchronous and asynchronous processing (clients
  opt in to async with the `Prefer=respond-async` header).

### Concurrency control

- **Manage concurrent operations with ETags (optimistic concurrency control).**

  ETags are unique identifiers assigned to a specific version of a resource;
  when the resource changes, its ETag changes. On a `GET`, the client receives
  an `ETag` header representing the current version. On a subsequent update, the
  client sends the ETag in the `If-Match` header. The server checks if the
  request ETag matches the current version; if they match, the update proceeds,
  and if not (another client updated the resource in the meantime), the update
  fails with `412 Precondition Failed`.

### Health check endpoints

- **All HTTP APIs SHOULD implement a health check endpoint.**

  Based on the [IETF draft standard](https://datatracker.ietf.org/doc/html/draft-inadarei-api-health-check-02).
  Place at a memorable, commonly-used URI, RECOMMENDED at the root level
  outside the versioned API path (`GET /health`), or per version if versions are
  hosted independently (`GET /v1/health`). Responses MUST use JSON with media
  type `application/health+json` and MUST include a `status` field with one of
  three values: `pass` (operating normally), `warn` (operational but degraded),
  `fail` (not operational). Optional fields: `version`, `releaseId`, `notes`,
  `serviceId`, `description`, `links`. The HTTP status code MUST correspond to
  the `status` field: `pass`/`warn` → 2xx or 3xx (typically `200 OK`); `fail` →
  4xx or 5xx (typically `503 Service Unavailable`). Responses SHOULD be
  cacheable (a reasonable default `Cache-Control` lifetime is 1 hour).

### Headers

- **HTTP header field names are case-insensitive (RFC 7230 §3.2); where you
  have control, RECOMMENDED to write them in Pascal Case with hyphen-delimited
  words (`Content-Type`, `User-Agent`, `Accept-Encoding`).**

  Avoid underscores or camelCase, even for non-standard headers. Non-standard
  headers SHOULD be prefixed with `X-` to indicate custom headers and avoid
  conflicts with future standards (eg. `X-Request-Id`, `X-Correlation-Id`,
  `X-Client-Id`).

- **HTTP APIs MAY support the `Prefer` header ([RFC 7240](https://tools.ietf.org/html/rfc7240))
  for clients to opt in to specific behaviors.**

  Common use: `Prefer:return=representation` to opt in to receiving a response
  body (updated resource) for `PUT`/`PATCH` requests that would otherwise return
  `204 No Content`. `Prefer:return=minimal` for partial representations (the
  definition of "minimal" is at the service's discretion but SHOULD be
  documented). A `fields` query parameter MAY be used instead for granular field
  selection (comma-separated field names; the response includes only those plus
  required fields). If implemented, `fields` SHOULD be supported globally and
  SHOULD NOT be used with `Prefer:return=minimal` (clients supply one or the
  other, not both).

- **HTTP API servers MUST provide guidance to clients on appropriate caching of
  responses.**

  Client-side caching is typically guided by `Cache-Control` (directives:
  max-age, no-cache, private), optionally combined with `ETag` (conditional
  requests), `Last-Modified` (timestamps), and `Vary` (headers affecting response
  content). Upstream caching: CDN/edge, application-level (in-memory or
  distributed), database query. Consider cache invalidation techniques.

### Payloads

- **Payloads SHOULD be JSON for the majority of use cases.**

  JSON is natively supported by most languages, human-readable, machine-parsable,
  and the _de facto_ standard for HTTP APIs. RECOMMENDED to always return some
  content (except for `204 No Content`) — even a message that doesn't add
  semantic meaning beyond the status code can be useful for testing. A little
  redundancy between payload content, headers, and status codes is okay.

- **Payload structure SHOULD be consistent across all endpoints; an appropriate
  schema SHOULD be designed for each API's needs.**

  There is no universal standard (OData is the closest but overly complex;
  lighter standards include JSON API and JSON RPC). The following is a
  RECOMMENDED starting point (heavily influenced by JSON API but not
  compatible), describing response payloads (a subset MAY be adopted for request
  payloads).

- **The schema defines four top-level properties: `resources` (object),
  `metadata` (object), `links` (array), `messages` (array).**

  Only `resources` is REQUIRED for non-empty response bodies (it MAY be an empty
  object). Minimum payload: `{ "resources": {} }`.

  - **`resources`**: a `ResourcesContainer` object whose keys map to resource
    type names (matching URL paths of resource-oriented endpoints). Each value
    is a `ResourceTypeContainer` with REQUIRED `items` (a `ResourceCollection`
    array of `ResourceItem` objects) and OPTIONAL `metadata` and `links`. Each
    `ResourceItem` MUST have an `id` (unique identifier) and MAY have
    `attributes` (a hashmap of business-domain field/value pairs — the naming
    convention MAY differ from other schema fields, eg. lowerCamelCase for
    attributes vs lower_snake_case elsewhere), `metadata`, `related`, and
    `links`. RECOMMENDED that `ResourceItem` attributes be composed from a
    consistent set of common types defined separately using JSON Schema (see
    [TS-29: JSON Schema](../029/AGENTS.md)).
  - **`metadata`**: a `MetadataContainer` hashmap (string keys; string/number/
    boolean values). Provides granularity about response status where HTTP
    status codes are insufficient, collection information (eg. `total_items`,
    `total_pages`), or individual-resource metadata. MUST NOT duplicate
    information already provided in HTTP headers (eg. `Content-Type`,
    `Content-Length`).
  - **`related`**: an OPTIONAL `RelatedCollection` of `RelatedItem`s on
    `ResourceItem` objects, creating relationships between entities of different
    resource types (all of which MUST exist within the same `ResourcesContainer`
    instance). Each `RelatedItem` has `type` and `id` fields.
  - **`links`**: hypermedia controls. Links MAY be associated with the response
    message itself, a collection, or individual resources. Each link is an
    object with `rel` (relationship, eg. "self", "next", "delete", "patch"),
    `href` (URL), and `method` (HTTP method). Hypermedia links make APIs
    self-descriptive, improving discoverability, extensibility, and reducing
    client-server coupling. Conventions take cues from HAL, JSON API, Siren,
    and PayPal's convention. Pagination links ("next", "prev", "first", "last")
    SHOULD be included in paginated collections; the `page` and `per_page`
    parameters MUST be maintained for each link. `first` and `last` MUST NOT be
    returned when page tokens are used for navigation; `prev` MUST NOT be
    provided on the first page; `next` MAY be omitted if the current page is
    known to be last.

### Versioning and managing breaking changes

- **HTTP APIs SHOULD have a major version number incremented whenever there are
  breaking changes, encoded in the first path segment (`/v{major}`).**

  Use the **expanding contract** (additive) pattern: breaking changes MUST NOT
  be made to APIs already in use; developers MUST NOT add new required parameters
  to existing APIs; MUST NOT remove existing required parameters; MUST NOT
  change the meaning of existing parameters; APIs MUST be designed to be
  extensible. A scalable design avoids arrays of scalar types (impossible to
  extend without breaking changes) — prefer arrays of objects (eg.
  `[{ "name": "Brazil" }]` over `["Brazil"]`). Breaking changes include changes
  to request/response message formats, API semantics, or API behavior. Where
  unavoidable, breaking changes MUST be implemented in a new major version; the
  old version MUST be maintained for a reasonable period for client migration.
  APIs MUST have a documented lifecycle policy describing the support and
  maintenance of each major version.

### Documentation

- **HTTP APIs MUST be thoroughly documented.**

  (The source file flags this section as a TODO for notes on preferred IDLs
  such as OpenAPI; the normative requirement to document thoroughly stands.)

## References

- [TS-21 source](../../pages/021-http-apis.adoc)
- [TS-11: Versioning](../011/AGENTS.md)
- [TS-20: Network APIs](../020/AGENTS.md)
- [TS-22: Webhooks](../022/AGENTS.md)
- [TS-29: JSON Schema](../029/AGENTS.md)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [RFC 10008 (QUERY method)](https://www.rfc-editor.org/info/rfc10008/)
- [JSON Patch (RFC 6902)](https://datatracker.ietf.org/doc/html/rfc6902)
- [IETF health check draft](https://datatracker.ietf.org/doc/html/draft-inadarei-api-health-check-02)
