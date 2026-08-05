# TS-21 gap analysis

Gaps found comparing TS-21: HTTP APIs against the reference resources listed
in GitHub issue https://github.com/kieranpotts/standards/issues/58.

Reference resources ingested:

- `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md`
- `https://blog.wahab2.com/api-architecture-best-practices-for-designing-rest-apis-bf907025f5f`
- `https://github.com/masteringapi/rest-api-standards` (link directory; no
  standalone claims)
- `https://www.youtube.com/watch?v=etKM5-gGwto` (GOTO 2024, Mike Amundsen —
  compared against the description only; no transcript)
- `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design`
- `https://github.com/microsoft/api-guidelines` / `.../blob/master/Guidelines.md`
- `https://microsoft.github.io/code-with-engineering-playbook/design/design-patterns/rest-api-design-guidance/`
- `https://stackoverflow.com/questions/39789818/best-practice-for-passing-enum-params-in-web-api` (fetch blocked — Cloudflare 403)
- `https://github.com/laravel/framework/discussions/47333`
- `https://en.wikipedia.org/wiki/Enumerated_type`
- `https://appwrite.io/blog/post/enums-api-design`
- `https://google.aip.dev/130`
- `https://digitalspecs.portofantwerpbruges.com/api-guidelines/`
- `https://www.gov.uk/government/collections/api-design-guidance`
- `https://json-schema.org/learn/getting-started-step-by-step`
- `https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/database-transactions-optimistic-concurrency`
- `https://fideloper.com/etags-and-optimistic-concurrency-control`
- `https://learn.microsoft.com/en-us/azure/search/search-howto-concurrency`
- `https://stackoverflow.com/questions/61989114/rest-api-concurrency-check-using-etags` (fetch blocked — Cloudflare 403)
- `https://stackoverflow.blog/2022/06/02/a-beginners-guide-to-json-the-data-format-for-the-internet/`
- `https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/`
- `https://stateless.co/hal_specification.html`
- `https://docs.oasis-open.org/odata/odata-json-format/v4.0/odata-json-format-v4.0.html`
- `https://www.w3.org/TR/json-ld/#lists`
- `https://ionspec.org/`
- `https://github.com/adnan-kamili/rest-api-response-format`
- `https://github.com/adnan-kamili/swagger-response-template`
- `https://json-schema.org/understanding-json-schema/reference/schema#schema`
- `https://www.learnjsonschema.com/2020-12/validation/type/`
- `https://www.jsonschemavalidator.net/` (online tool; not a claim source)
- `https://datatracker.ietf.org/doc/rfc7807/`
- `https://www.jsonrpc.org/specification#overview`
- `https://stackoverflow.com/questions/12806386/is-there-any-standard-for-json-api-response-format` (fetch blocked — Cloudflare 403)
- `https://jsonapi.org/format/1.2/`
- `https://github.com/kevinswiber/siren`
- `https://groups.google.com/g/siren-hypermedia`
- `https://spring-hateoas-siren.ingogriebsch.de/current/index.html`
- `https://github.com/levid-gc/paypal-api-standards/blob/master/api-style-guide.md`
  (ingested in the first run via the local clone
  `src/021/__TODO__/http/api-standards-master/api-style-guide.md` and
  `patterns.md`; findings carried forward below cite those local paths)
- `https://github.com/jharmn/api-standards` (the PayPal API Style Guide —
  identical content to `levid-gc/paypal-api-standards`; already covered by the
  first run)

**Assessment.** TS-21 is broad and notably current — it cites RFC 10008
`QUERY`, draft 2020-12 JSON Schema, RFC 6902 JSON Patch, the IETF health-check
draft, and an explicit expanding-contract versioning model — so most of the
40-odd reference resources it was compared against are already covered, often
more thoroughly than the references. The first run (PayPal API standards plus
short stubs) produced mostly *partial* findings. This second run, against the
wider issue #58 list (Microsoft API Guidelines, Azure architecture guidance,
Google AIP-130, Port of Antwerp-Bruges, GOV.UK, hypermedia specs, RFC 7807,
JSON-RPC, JSON:API, Siren, Ion, HAL, OData, JSON Schema primers, enum and
ETag articles), again yields mostly *partial* findings: targeted rules or
response/operation patterns the references spell out that TS-21 omits or
under-specifies. The genuine *missing* items are few and cluster around CORS,
URI-length handling, JSON-property-order interoperability, and the still-stub
authentication section. The hypermedia media-type specs (HAL, JSON:API, Siren,
Ion, OData, JSON-LD) are largely *out-of-scope*: TS-21 deliberately defines its
own lighter envelope and only "takes cues from" those formats, so their
internal structure is not something the standard needs to reproduce.

**Status:** Second run. All gaps from the first run remain open (the standard
was not modified). New gaps from issue #58 are appended to each section below.
Date of last run: 2026-08-05.

## Missing

- [ ] `__TODO__/http/api/api-keys.md:3-9` — API keys as an authentication
      pattern (pass via a custom header such as `X-Api-Key`; keys MUST have
      expiry and be revocable; keys used to call external services MUST NOT be
      checked into source control) is not addressed anywhere in the standard.
      The standard's auth file is a stub with a TODO to extend it. Recommend
      placing at `02-authentication-and-authorization.adoc` (new section).

- [ ] `__TODO__/http/api/resources.md:17-19` — A client-driven mechanism to
      request "expanded" resource representations (related resources embedded
      to avoid round-trips), eg. an `expand`/`include` query parameter, is not
      addressed anywhere in the standard. The standard's `related` field
      (`16-payloads.adoc:503`) embeds related resources but is server-controlled
      only. Recommend placing at `16-payloads.adoc` (Related resources, new
      subsection) or `07-collections.adoc`.

- [ ] `api-style-guide.md:1371` — The rule that query parameters SHOULD only
      restrict/search/filter a collection, and a resource identifier SHOULD NOT
      be used as a query filter (it belongs in the URL path), is not stated
      anywhere in the standard. Recommend placing at `07-collections.adoc`
      (Filtering) or `06-urls.adoc`.

- [ ] `api-style-guide.md:1384` — The rule that query parameters SHOULD NOT be
      used on single-resource endpoints is not stated anywhere in the standard.
      Recommend placing at `06-urls.adoc` (Resources and collections).

- [ ] `api-style-guide.md:1390-1397` and `patterns.md:178-203` — The
      `POST`-based complex search action that paginates via query parameters
      (the rare, justified `POST` body + query-parameters exception) is not
      covered. The standard covers actions (`11-actions.adoc`) and collection
      pagination/searching (`07-collections.adoc`) separately but does not
      address paginating the results of a `POST` search action. Recommend
      placing at `11-actions.adoc` (new subsection) or `07-collections.adoc`
      (Searching).

- [ ] `api-style-guide.md:1353` — Enumeration values MAY be used as sub-resource
      identifiers (using the string representation). Not addressed in the
      standard's sub-resources guidance. Recommend placing at
      `09-sub-resources-and-sub-collections.adoc`.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#8-cors`
      and `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#security`
      — CORS handling for browser clients (`Access-Control-Allow-Origin`,
      preflight, avoiding preflight on performance-critical paths) is not
      addressed anywhere in the standard, which otherwise targets public-facing
      APIs integrated into third-party client applications (including browser
      apps). Recommend placing at `03-security.adoc` or `15-headers.adoc` (new
      section). Flagged: this may be considered a deployment/security concern
      deferred to another standard.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-2-url-length`
      and `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#uri-path-design`
      — A URL-length limit (the references cite 2083 / 2048 characters) and the
      `414 URI Too Long` status code for unparseable over-long request targets
      are not addressed. Recommend placing at `06-urls.adoc`.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#6-2-variable-order-rule`
      — The rule that clients MUST NOT rely on JSON property/field order (and
      that services MAY support explicit ordering only via a documented sort
      contract) is not stated anywhere in the standard. Recommend placing at
      `16-payloads.adoc`.

- [ ] `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#security`
      and `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#security`
      — Specific authentication schemes for HTTP APIs (OAuth 2.0 with Bearer
      tokens over TLS; HTTP Basic Auth) are not prescribed; the standard's auth
      file is a stub (`02-authentication-and-authorization.adoc` carries only a
      TODO to extend it). Complements the API-keys gap above. Recommend placing
      at `02-authentication-and-authorization.adoc` (new section).

## Partial

- [ ] `api-style-guide.md:944` covers hypermedia link `href` more precisely than
      `16-payloads.adoc:630` — specifically, the reference requires `href` to be
      a URI Template per RFC 6570 and to be an absolute URI, whereas the
      standard's `LinkItem` schema types `href` as a bare string with no such
      constraint.

- [ ] `api-style-guide.md:967` covers hypermedia link `method` more precisely
      than `16-payloads.adoc:630` — specifically, the reference makes `method`
      optional with a default of `GET` when omitted, whereas the standard's
      `LinkItem` defines `method` as a plain string with no default and its
      examples always include it.

- [ ] `api-style-guide.md:810` covers hypermedia client behaviour more
      prescriptively than `16-payloads.adoc:879` — specifically, the reference
      states clients SHOULD treat URIs as opaque identifiers and SHOULD NOT
      compose URIs themselves; the standard implies this in its "single entry
      point" use case (clients should not have every URL pattern hard-coded)
      but does not state the opaque-URI principle directly.

- [ ] `patterns.md:152` covers transient actions more prescriptively than
      `11-actions.adoc` — specifically, the reference states transient actions
      MUST return `200 OK` with a response body of calculated values (which
      could differ if re-run) and SHOULD only be used after other alternatives
      are considered; the standard mentions the "dry run" concept but omits
      these response-shape and cautionary rules.

- [ ] `patterns.md:123` covers composite action responses more prescriptively
      than `11-actions.adoc` — specifically, the reference shows a composite
      action response including HATEOAS links to every affected resource
      (`self`, `parent_payment`, `capture`); the standard describes composite
      actions conceptually but does not require or illustrate links to all
      affected resources in the response.

- [ ] `patterns.md:270-306` covers the standalone file upload more thoroughly
      than `08-resources.adoc:274` — specifically, the reference illustrates the
      full `multipart/form-data` request body (boundary, `Content-Disposition`
      with `filename`/`name`, a text metadata part plus a binary part) and
      requires the response to return a full file metadata set (`id`,
      `created_at`, `size`, `url`, `type`); the standard only requires "an
      identifier or URL" and shows no multipart body structure.

- [ ] `patterns.md:782` covers bulk-operation error correlation more
      thoroughly than `07-collections.adoc:196` — specifically, the reference
      documents an attribute-filter JSON Pointer form
      (`/items/@account_number=='2097094104180012047'/address_id`) as an
      alternative to index-based correlation; the standard only describes the
      index-based form (`/items/1/currency_code`).

- [ ] `patterns.md:730-734` covers bulk update/replace more thoroughly than
      `07-collections.adoc:196` — specifically, the reference models the bulk
      request as a first-class, uniquely identifiable batch resource returned
      to the client, against which subsequent `PUT`/`PATCH` operations act via
      the batch id; the standard covers bulk create but not this batch-as-
      resource pattern for later updates.

- [ ] `patterns.md:565` covers asynchronous-operation hypermedia more
      thoroughly than `12-asynchronous-operations.adoc` — specifically, the
      reference says links SHOULD let the client find operation status AND
      perform get/update/delete on the operation; the standard only addresses
      `GET` status links.

- [ ] `api-style-guide.md:2088` covers the address `admin_area` field more
      precisely than `19-common-types.adoc:80` — specifically, the reference
      ties the administrative-area component to ISO 3166-2 subdivisions; the
      standard uses a generic `admin_area` field name without referencing the
      ISO 3166-2 standard.

- [ ] `api-style-guide.md:2147` covers floating month/year values more
      thoroughly than `19-common-types.adoc:91` — specifically, the reference
      defines a dedicated `date_year_month.json` common type for floating
      month/year values such as card expiry (`2016-09`); the standard mentions
      card expiry as a floating-date example but defines no year-month
      representation.

- [ ] `api-style-guide.md:2462` covers the error catalog more thoroughly than
      `16-payloads.adoc:1306` — specifically, the reference includes a
      `legacy_code` field for backward compatibility with existing published
      error metadata; the standard's catalog spec omits it.

- [ ] `api-style-guide.md:2543` covers error catalog usage more concretely than
      `16-payloads.adoc:1306` — specifically, the reference provides worked
      sample catalogs for several namespaces showing realistic error names,
      status codes, and issue mappings; the standard describes the catalog
      structure but gives no full worked example.

- [ ] `api-style-guide.md:2220` covers JSON-Pointer field identification more
      thoroughly than `16-payloads.adoc:1126` — specifically, the reference
      states that existing APIs using other means to identify the `field` may
      continue, but migrating to JSON Pointer requires a major version bump;
      the standard mandates JSON Pointer without addressing migration of
      legacy field-identification schemes.

- [ ] `api-style-guide.md:2807` covers new-major-version justification more
      concretely than `17-versioning.adoc:107` — specifically, the reference
      structures the justification into three categories (Business Case, API
      Design, Migration Strategy) with explicit sub-questions; the standard
      states the principle ("document why, what value, how consumers will be
      supported") but not the structured checklist.

- [ ] `patterns.md:390` covers multi-step action hypermedia more thoroughly
      than `16-payloads.adoc:879` — specifically, the reference notes that an
      unsuccessful step in a multi-step process MAY return only a link to send
      the corrected/missing data (eg. a `PATCH` link); the standard describes
      the happy-path chaining of a multi-step entry point but not the
      error-correction link.

- [ ] `https://datatracker.ietf.org/doc/rfc7807/#section-3` and
      `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#http-status-codes-and-errors`
      cover HTTP error response formats more standardly than
      `16-payloads.adoc:1080` — specifically, RFC 7807 Problem Details
      (`application/problem+json` with `type`/`title`/`status`/`detail`/
      `instance` and extension members) is the IETF's portable error format;
      the standard defines a thorough custom error schema but never references
      or aligns with RFC 7807 (now obsoleted by RFC 9457). Recommend noting
      the relationship at `16-payloads.adoc` (Error handling).

- [ ] `https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/database-transactions-optimistic-concurrency#implement-optimistic-concurrency-control-using-etag-and-http-headers`
      and `https://learn.microsoft.com/en-us/azure/search/search-howto-concurrency#how-it-works`
      cover conditional requests more thoroughly than
      `13-concurrency-control.adoc` — specifically, the references describe
      `If-None-Match` for cache validation (the client decides whether a
      refetch is needed) and the `304 Not Modified` response, whereas the
      standard documents only `If-Match`/`412` for optimistic concurrency and
      mentions `ETag` "conditional requests" in `15-headers.adoc` without
      specifying the `If-None-Match`/`304` path. Recommend placing at
      `13-concurrency-control.adoc` or `15-headers.adoc` (Response caching).

- [ ] `https://learn.microsoft.com/en-us/azure/search/search-howto-concurrency#design-pattern`
      and `https://fideloper.com/etags-and-optimistic-concurrency-control#notes`
      cover the optimistic-concurrency client retry pattern more thoroughly
      than `13-concurrency-control.adoc` — specifically, the references
      prescribe a bounded loop (GET latest → apply changes locally → attempt
      conditional update with `If-Match` → on `412` re-fetch and retry) and
      note the server policy for requests with no `If-Match`; the standard
      describes the precondition check but not the client retry loop or the
      missing-header policy. Recommend placing at `13-concurrency-control.adoc`
      (new subsection).

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#13-2-9-retry-after`
      and `https://datatracker.ietf.org/doc/rfc7807/#section-4` cover the
      `Retry-After` header more thoroughly than `05-http-status-codes.adoc:85`
      — specifically, the standard mentions `Retry-After` only for `429 Too
      Many Requests`, whereas the references also use it for `202 Accepted`
      (long-running operations) and retryable `5xx`/transient errors
      (`503`), and allow it to be either seconds or an HTTP-date. Recommend
      extending at `12-asynchronous-operations.adoc` and the `503` entry in
      `05-http-status-codes.adoc`.

- [ ] `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#implement-asynchronous-methods`
      covers asynchronous resource creation completion more concretely than
      `12-asynchronous-operations.adoc` — specifically, the reference prescribes
      returning `303 See Other` with a `Location` header pointing to the newly
      created resource once an async resource-creating operation completes;
      the standard describes polling the final URL (which returns `404` until
      ready) but not the `303 See Other` completion pattern. Recommend placing
      at `12-asynchronous-operations.adoc`.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#13-2-stepwise-long-running-operations`
      (and `#13-2-4-operations-resource`, `#13-2-5-operation-resource`,
      `#13-3-retention-policy-for-operation-results`) covers the long-running
      operation-status resource model more thoroughly than
      `12-asynchronous-operations.adoc` — specifically, the reference
      prescribes an `Operation-Location` header, an `/operations` resource
      with state (`NotStarted`/`Running`/`Succeeded`/`Failed`),
      `createdDateTime`/`lastActionDateTime`/`percentComplete`, idempotent
      `DELETE` for cancellation, tombstoning, and a minimum 24-hour result
      retention; the standard's "temporary status URL with a request
      identifier" leaves all of this unspecified. Recommend placing at
      `12-asynchronous-operations.adoc` (new subsection).

- [ ] `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#patch-requests`
      and `https://github.com/adnan-kamili/rest-api-response-format#references`
      cover PATCH media types more thoroughly than `08-resources.adoc`
      (`04-http-methods.adoc` and the resources update guidance) —
      specifically, the references distinguish JSON Merge Patch
      (`application/merge-patch+json`, RFC 7396, which cannot represent explicit
      `null`) from JSON Patch (`application/json-patch+json`, RFC 6902) and
      note `415 Unsupported Media Type` when the patch format is unsupported;
      the standard mentions RFC 6902 only and does not address merge patch, the
      media-type selection, or the `415` case for patch formats. Recommend
      placing at `08-resources.adoc` (PATCH) or `15-headers.adoc`.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#11-4-durations`
      (and `#11-5-intervals`, `#11-6-repeating-intervals`) and
      `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#json-guidelines`
      cover ISO 8601 durations and intervals more thoroughly than
      `19-common-types.adoc:91` — specifically, the references serialize
      durations (`P3Y6M4DT12H30M5S`), intervals (start/end, start/duration),
      and repeating intervals (`R[n]/`) per ISO 8601; the standard's dates
      section covers RFC 3339 date-times and floating dates but no duration or
      interval representation. Recommend placing at `19-common-types.adoc`
      (Dates, new subsection).

- [ ] `https://www.learnjsonschema.com/2020-12/validation/type/` and
      `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#11-json-standardizations`
      cover JSON number precision more generally than
      `19-common-types.adoc:30` — specifically, the references state the
      general interoperability rule that integers beyond 2^53 (and any number
      exceeding IEEE 754 double precision) should be serialized as strings, and
      OData's `IEEE754Compatible` mode for 64-bit integers; the standard
      applies the string-for-precision rule to monetary amounts only. Recommend
      placing at `19-common-types.adoc` (new subsection on number
      representation).

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#6-1-ignore-rule`
      and `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#compatibility`
      cover unknown-field handling more explicitly than
      `17-versioning.adoc` — specifically, the references state that clients
      MUST ignore unknown response fields (Tolerant Reader) and that servers
      SHOULD reject unknown request fields with `400 Bad Request` (Port of
      Antwerp's deliberate deviation from Postel's law); the standard implies
      tolerance via its additive expanding-contract model and cites Postel's
      law for trailing slashes, but does not state the field-level
      ignore-unknown-response / reject-unknown-request rules. Recommend placing
      at `17-versioning.adoc` or `16-payloads.adoc`.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-6-standard-response-headers`
      and `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#standard-response-headers`
      cover the `Preference-Applied` response header more thoroughly than
      `15-headers.adoc:109` — specifically, the references require a
      `Preference-Applied` response header indicating whether a `Prefer`
      request preference was honoured; the standard documents the `Prefer`
      request header and its tokens but not the `Preference-Applied` response.
      Recommend placing at `15-headers.adoc` (Prefer section).

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-5-standard-request-headers`
      (and `#7-6-standard-response-headers`) cover the `Date` header more
      thoroughly than `15-headers.adoc` — specifically, the references require a
      `Date` header (RFC 5322, GMT) on all responses; the standard does not
      mention the `Date` header. Recommend placing at `15-headers.adoc`.

- [ ] `https://microsoft.github.io/code-with-engineering-playbook/design/design-patterns/rest-api-design-guidance/#creating-api-contracts`
      (and `#design-first-approach`, `#code-first-approach`) covers API
      contract authoring more thoroughly than `18-documentation.adoc` —
      specifically, the reference sets out the design-first (OpenAPI contract
      first) vs code-first trade-offs (early feedback, parallel
      producer/consumer development, generated SDKs vs OpenAPI drift,
      committing generated OpenAPI to VCS); the standard's documentation file
      is a stub containing only a TODO to "Add notes on preferred IDLs such as
      OpenAPI". Recommend placing at `18-documentation.adoc`.

- [ ] `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#errors`
      and `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-10-2-error-condition-responses`
      cover a canonical error-code vocabulary more thoroughly than
      `16-payloads.adoc:1306` — specifically, the references provide a portable
      set of canonical error names (`INVALID_ARGUMENT`, `FAILED_PRECONDITION`,
      `OUT_OF_RANGE`, `UNAUTHENTICATED`, `PERMISSION_DENIED`, `NOT_FOUND`,
      `ALREADY_EXISTS`, `ABORTED`, `UNAVAILABLE`, …) for cross-API
      consistency, and the Microsoft guidance makes adding a new top-level code
      a breaking change (extend `innererror` instead); the standard has its
      own error names and catalog but no recommended canonical, portable
      vocabulary. Recommend placing at `16-payloads.adoc` (Error catalog).

- [ ] `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#error-propagation`
      covers error propagation from upstream services more thoroughly than
      `16-payloads.adoc` and `05-http-status-codes.adoc` — specifically, the
      reference states services MUST NOT blindly propagate upstream errors
      (hide implementation details; re-map responsibility, eg. upstream `400`
      → own `500`); the standard mentions upstream interactions only in the
      context of `422` and does not address error masking/remapping. Recommend
      placing at `16-payloads.adoc` (Error handling) or
      `05-http-status-codes.adoc`.

- [ ] `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#http-status-codes-and-errors`
      and `https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/#handle-errors-gracefully-and-return-standard-error-codes`
      cover leakage of implementation details in errors more explicitly than
      `03-security.adoc` — specifically, the references state that error
      responses MUST NOT expose stack traces or information useful to
      attackers; the standard's security file is a stub and its error section
      does not state this hygiene rule. Recommend placing at `03-security.adoc`
      or `16-payloads.adoc` (Error handling).

- [ ] `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#support-partial-responses`
      covers partial-content retrieval of large/binary resources more
      thoroughly than `08-resources.adoc:274` — specifically, the reference
      prescribes `Accept-Ranges`/`Range`/`Content-Range` and `206 Partial
      Content` for ranged GETs (plus `HEAD` to discover metadata first); the
      standard covers multipart file upload but not ranged/partial download.
      Flagged: borderline scope (the standard is JSON-focused), but symmetric
      with its upload guidance. Recommend placing at `08-resources.adoc` (new
      subsection).

## Out-of-scope

- [ ] `api-style-guide.md:194-232` covers this, but it plausibly sits outside
      this standard's stated purpose because the concepts are PayPal-internal
      organizational constructs (Capability APIs vs Experience-specific APIs,
      the Business Capability Model, and the domain/capability orthogonality)
      rather than general HTTP API design rules. Flagged for the user to
      confirm or overrule.

- [ ] `api-style-guide.md:27-44` covers this, but it plausibly sits outside
      this standard's stated purpose because it is document-level convention
      (RFC 2119 keyword interpretation, all-caps rendering of "REST"/"JSON",
      fixed-width rendering of machine-readable text, URI Template RFC 6570 for
      variable blocks) governed by the project's style guide rather than by
      TS-21's content. Flagged for the user to confirm or overrule.

- [ ] `api-style-guide.md:1297` and `api-style-guide.md:1443-1602` cover this,
      but it plausibly sits outside this standard's stated purpose because
      JSON Schema draft-version pinning (draft-04), OpenAPI tooling `$schema`
      handling, draft-03→draft-04 migration notes, and one-type-per-file schema
      file naming are JSON-Schema-authoring concerns deferred by TS-21 to
      TS-29 (which the standard already cross-references). Flagged for the user
      to confirm or overrule.

- [ ] `api-style-guide.md:1776` and `api-style-guide.md:2501` cover this, but
      they plausibly sit outside this standard's stated purpose because they
      are implementation-language/infrastructure concerns (Oracle VARCHAR2
      column sizing for `maxLength`; Java `printf`-style formatting of error
      catalog strings) rather than API-design rules. Flagged for the user to
      confirm or overrule.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#9-7-filtering`,
      `#9-6-sorting-collections`, and `#9-8-pagination` (OData-style
      `$filter`/`$orderBy`/`$top`/`$skip` and `@nextLink`) cover this, but it
      plausibly sits outside TS-21's stated purpose because the standard
      deliberately specifies a lighter filtering/sorting/pagination model
      (`sort_by`/`sort_order`, `page`/`per_page`/`page_token`, hypermedia
      `next`/`prev`/`first`/`last` links) rather than the full OData query
      language; adopting OData's expression grammar would be a design change,
      not a gap. Flagged for the user to confirm or overrule.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#10-delta-queries`
      and `https://docs.oasis-open.org/odata/odata-json-format/v4.0/odata-json-format-v4.0.html#deltaResponse`
      cover delta queries / change tracking (`$delta`, `@odata.deltaLink`,
      `@removed`), but it plausibly sits outside TS-21's stated purpose as an
      advanced, specialized collection-sync capability beyond the standard's
      pagination/filtering scope. Flagged for the user to confirm or overrule.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#14-push-notifications-via-webhooks`
      covers webhook subscription validation (`validationToken`
      challenge/response, `notificationUrl`, retry/back-off, no `301/302`
      redirects), but it plausibly sits outside TS-21's stated purpose because
      webhook implementation is deferred to TS-22 (which
      `12-asynchronous-operations.adoc` already cross-references). Flagged for
      the user to confirm or overrule.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#8-cors`
      and rate-limit headers (`X-RateLimit-Limit`/`Remaining`/`Reset` per
      `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#http-status-codes-and-errors`)
      cover this, but the rate-limiting mechanics plausibly sit outside TS-21's
      stated purpose because `05-http-status-codes.adoc:90` already carries a
      TODO to link to a dedicated rate-limiting standard once one exists, and
      cross-cutting network concerns are deferred to TS-20. (Note: the
      `429`+`Retry-After` status-code rule itself is already covered.) Flagged
      for the user to confirm or overrule.

- [ ] `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#multitenant-web-apis`
      covers multitenancy identification (subdomain vs `X-Tenant-ID`/JWT claim
      vs path-based, and the cache-interaction caveat), but it plausibly sits
      outside TS-21's stated purpose as a deployment/architecture concern
      rather than an API-interface design rule. Flagged for the user to confirm
      or overrule.

- [ ] `https://www.gov.uk/government/collections/api-design-guidance#api-technologies`
      covers when to use GraphQL as an alternative to REST, but it plausibly
      sits outside TS-21's stated purpose because TS-21 is explicitly about the
      RESTful HTTP API style; choosing between paradigms is an architecture
      decision. Flagged for the user to confirm or overrule.

- [ ] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-9-pii-parameters`
      covers not transmitting PII in URLs (use headers instead), but it
      plausibly sits outside TS-21's stated purpose because it overlaps the
      dedicated security and privacy standards (TS-52, TS-53). Flagged for the
      user to confirm or overrule.

- [ ] `https://stateless.co/hal_specification.html`,
      `https://jsonapi.org/format/1.2/`, `https://github.com/kevinswiber/siren`,
      `https://ionspec.org/`, and
      `https://docs.oasis-open.org/odata/odata-json-format/v4.0/odata-json-format-v4.0.html`
      (and `https://www.w3.org/TR/json-ld/#lists`) cover full hypermedia
      media-type specifications (HAL `_links`/`_embedded` and CURIEs; JSON:API
      `included`/compound documents, sparse fieldsets, `fields[TYPE]`;
      Siren `entities`/`actions`/`fields`; Ion value/collection objects, forms,
      and registered types; OData control annotations; JSON-LD `@list`/`@set`
      and node/value objects), but these plausibly sit outside TS-21's stated
      purpose because the standard deliberately defines its own lighter
      `resources`/`metadata`/`links`/`related` envelope and states it only
      "takes cues from" these formats; reproducing their internal structure is
      not within the standard's scope. Flagged for the user to confirm or
      overrule.

- [ ] `https://www.jsonrpc.org/specification#overview` covers the JSON-RPC 2.0
      wire protocol (`jsonrpc`/`method`/`params`/`id`, notifications, batches,
      reserved error codes), but it plausibly sits outside TS-21's stated
      purpose because the standard is explicitly about the RESTful HTTP style
      and JSON-RPC is a different, transport-agnostic RPC paradigm (the
      standard mentions JSON RPC only as a lighter alternative envelope it does
      not adopt). Flagged for the user to confirm or overrule.

## Unresolved

- [ ] `https://www.youtube.com/watch?v=etKM5-gGwto` (GOTO 2024, Mike Amundsen,
      "RESTful API Patterns & Practices") — compared against the video's
      description only; a full transcript could not be fetched (YouTube watch
      pages are JS-rendered). The description advertises 75+ patterns across
      Design / Clients / Services / Data / Workflow categories. Claims
      present only in the spoken audio could not be verified. On the basis of
      the description, the Design/Services categories overlap TS-21's existing
      coverage, while the Clients / Data / Workflow categories plausibly sit
      outside TS-21 (client-app robustness, distributed data, cross-service
      workflow — closer to TS-20 / TS-22). No specific new gap was derived from
      the description beyond those already identified above; re-running with a
      transcript may yield further findings.

- [ ] `https://stackoverflow.com/questions/39789818/best-practice-for-passing-enum-params-in-web-api`
      — fetch blocked by a Cloudflare anti-bot challenge (HTTP 403). Not
      included in the comparison. (The enum topic was covered via the Appwrite,
      Wikipedia, and Laravel references, plus the standard's own
      `16-payloads.adoc` enum guidance.)

- [ ] `https://stackoverflow.com/questions/61989114/rest-api-concurrency-check-using-etags`
      — fetch blocked by a Cloudflare anti-bot challenge (HTTP 403). Not
      included in the comparison. (The ETag/concurrency topic was covered via
      the Cosmos DB, Azure Search, and fideloper references.)

- [ ] `https://stackoverflow.com/questions/12806386/is-there-any-standard-for-json-api-response-format`
      — fetch blocked by a Cloudflare anti-bot challenge (HTTP 403). Not
      included in the comparison. (The response-format topic was covered via
      RFC 7807, JSON:API, JSON-RPC, and the adnan-kamili references.)