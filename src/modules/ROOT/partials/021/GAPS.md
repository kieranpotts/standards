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
  `__TODO__/021/http/api-standards-master/api-style-guide.md` and
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

**Third run, 2026-08-06.** Re-run against Brandur Leppka's "Using Atomic
Transactions to Power an Idempotent API" (https://brandur.org/http-transactions).
Three points were routed to TS-21: the 1:1 request↔transaction model (A),
idempotent endpoint design (B), and non-idempotent requests (E). All three
are Partial — TS-21 has the building blocks (composite-action atomicity,
PUT-for-create, async operations, idempotency keys) but not the central
request-as-transaction principle, the "design endpoints to be naturally
idempotent" philosophy, or multi-stage transactions for genuinely
non-idempotent operations. Three new Partial gaps added; all prior gaps
remain open.

**Fourth run, 2026-08-06.** Re-run against Brandur Leppka's "Implementing
Stripe-like Idempotency Keys in Postgres" (https://brandur.org/idempotency-keys)
— the "part two" deep dive on the multi-stage-transaction model that entry E
above anticipates. Nine points were routed to TS-21; all are Partial (TS-21
has the idempotency-key cache-and-replay substrate and general fault-
tolerance framing, but not the state-machine recovery, atomic phases,
recovery points, idempotency-key locking/409/SERIALIZABLE upsert, DAG,
completer/reaper, or indeterminate-error handling). Three new Partial entries
added capturing the concrete design beyond entry E; all prior gaps remain
open.

**Status:** Eleventh run, 2026-08-14. All Missing (sixth run) and all 39
Partial items (seventh through eleventh runs) are now closed. The tenth run
closed 9 items: bulk update/replace as a batch resource, async-operation
hypermedia links, the error catalog's `legacy_code` field and worked
example, JSON-Pointer field-id migration, API contract authoring
(design-first vs code-first), error propagation/masking from upstream
services, error-response implementation-detail leakage, and ranged/partial
content retrieval. The eleventh run closed the six Brandur idempotency-key
entries as one coherent batch, substantially restructuring
`10-safeness-and-idempotency.adoc` with new "Naturally-idempotent endpoint
design", "Genuinely non-idempotent operations", "Idempotency-key locking",
"Idempotency keys with atomic phases" (recovery points/state machine, atomic
phases), "Foreign state mutations" (indeterminate errors, completer/reaper),
and "Passive safety" sections, plus a new "Request-scoped transactions"
section in `11-actions.adoc` for the 1:1 request↔transaction principle.
`409 Conflict` and `206 Partial Content` were added to the documented
status-code subset in `05-http-status-codes.adoc` to support this content.

**Twelfth run, 2026-08-14.** Walked all 13 Out-of-scope items and the 4
Unresolved items with the user. All 13 Out-of-scope items were resolved: 9
confirmed out-of-scope outright; 2 confirmed out-of-scope for TS-21 but
routed to another standard's `GAPS.md` as a new Missing item rather than
dropped (document-level conventions → TS-26; rate-limit headers → TS-20); 1
confirmed out-of-scope with a small cross-reference added to TS-21 itself
(PII in URLs → `03-security.adoc`, pointing to TS-52/TS-53); and 1 largely
confirmed out-of-scope but, at the user's request, closed by a new "Alternative
HTTP API styles" section (`20-alternative-styles.adoc`, inserted before the
references partial, which was renumbered `20-references.adoc` →
`21-references.adoc`) briefly surveying HAL, JSON:API, Siren, Ion, OData, and
JSON-LD, folding in the JSON-RPC item too. Of the 4 Unresolved items, the 3
Stack Overflow items (blocked by Cloudflare) were re-attempted, still blocked,
and dismissed per the user's direction, since each topic is independently
covered elsewhere. The GOTO 2024 video transcript item was left open — it was
not part of the three the user asked to dismiss, and its premise (no
transcript available) is unrelated to the Cloudflare block.

**This file is now fully resolved except for one Unresolved item**: 0
Missing, 0 Partial, 0 Out-of-scope awaiting the user, 1 Unresolved (the GOTO
2024 video, blocked on a missing transcript rather than a fetch error).

## Missing

- [x] `__TODO__/http/api/api-keys.md:3-9` — API keys as an authentication
      pattern (pass via a custom header such as `X-Api-Key`; keys MUST have
      expiry and be revocable; keys used to call external services MUST NOT be
      checked into source control) is not addressed anywhere in the standard.
      The standard's auth file is a stub with a TODO to extend it. Recommend
      placing at `02-authentication-and-authorization.adoc` (new section).

      **Resolved.** Closed by `02-authentication-and-authorization.adoc`, new
      "API keys" section. States the `X-Api-Key` custom-header convention with
      a worked request example, requires expiry and revocability, and
      requires keys used for outbound calls to external services not be
      checked into source control, cross-referencing TS-52 (Security and
      secrets management) for storage and rotation practice. Written together
      with the OAuth 2.0 / Basic Authentication gap below, since both fill the
      same stub section.

- [x] `__TODO__/http/api/resources.md:17-19` — A client-driven mechanism to
      request "expanded" resource representations (related resources embedded
      to avoid round-trips), eg. an `expand`/`include` query parameter, is not
      addressed anywhere in the standard. The standard's `related` field
      (`16-payloads.adoc:503`) embeds related resources but is server-controlled
      only. Recommend placing at `16-payloads.adoc` (Related resources, new
      subsection) or `07-collections.adoc`.

      **Resolved.** Closed by `16-payloads.adoc`, new "Requesting related
      resources" subsection under "Related resources". Documents an `expand`
      query parameter accepting a comma-separated list of `type` values in
      the same `{namespace}/{resource}` form used by the `related` field,
      requires endpoints to document their supported expandable relations,
      and specifies that an unsupported relation name is ignored rather than
      rejected, consistent with the standard's existing tolerant-reader
      posture.

- [x] `api-style-guide.md:1371` — The rule that query parameters SHOULD only
      restrict/search/filter a collection, and a resource identifier SHOULD NOT
      be used as a query filter (it belongs in the URL path), is not stated
      anywhere in the standard. Recommend placing at `07-collections.adoc`
      (Filtering) or `06-urls.adoc`.

      **Resolved.** Closed by `07-collections.adoc`, "Filtering" section, new
      paragraph. States that query parameters SHOULD only restrict, search, or
      filter a collection, and that a resource identifier SHOULD NOT be used
      as a query parameter value to select a single resource, cross-referring
      to the URLs section's "Resources and collections" subsection.

- [x] `api-style-guide.md:1384` — The rule that query parameters SHOULD NOT be
      used on single-resource endpoints is not stated anywhere in the standard.
      Recommend placing at `06-urls.adoc` (Resources and collections).

      **Resolved.** Closed by `06-urls.adoc`, "Resources and collections"
      section, new paragraph. States that query parameters SHOULD NOT be used
      on single-resource endpoints, with the rationale (nothing left for a
      query parameter to narrow once the URL path already identifies one
      resource) and a cross-reference to the complementary collection-scoped
      rule.

- [x] `api-style-guide.md:1390-1397` and `patterns.md:178-203` — The
      `POST`-based complex search action that paginates via query parameters
      (the rare, justified `POST` body + query-parameters exception) is not
      covered. The standard covers actions (`11-actions.adoc`) and collection
      pagination/searching (`07-collections.adoc`) separately but does not
      address paginating the results of a `POST` search action. Recommend
      placing at `11-actions.adoc` (new subsection) or `07-collections.adoc`
      (Searching).

      **Resolved.** Closed by `11-actions.adoc`, new "Complex search actions"
      subsection. Explains when a `POST`-based search action is justified
      over query-parameter filtering, and documents the one sanctioned
      exception to the standard's "actions don't mix `POST` body with query
      parameters" norm: pagination parameters (`page`/`per_page`) MUST be
      carried as query parameters on the search action's URL, alongside the
      JSON search-criteria body, so that ordinary hypermedia pagination links
      can be generated. Cross-references the Filtering and Pagination
      sections of Collections.

- [x] `api-style-guide.md:1353` — Enumeration values MAY be used as sub-resource
      identifiers (using the string representation). Not addressed in the
      standard's sub-resources guidance. Recommend placing at
      `09-sub-resources-and-sub-collections.adoc`.

      **Resolved.** Closed by `09-sub-resources-and-sub-collections.adoc`, new
      paragraph after the named-type rule. States that the string
      representation of an enumeration value MAY be used as a sub-resource
      identifier where the enumeration has a fixed, well-known set of
      members, with a worked `limits/monthly` example.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#8-cors`
      and `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#security`
      — CORS handling for browser clients (`Access-Control-Allow-Origin`,
      preflight, avoiding preflight on performance-critical paths) is not
      addressed anywhere in the standard, which otherwise targets public-facing
      APIs integrated into third-party client applications (including browser
      apps). Recommend placing at `03-security.adoc` or `15-headers.adoc` (new
      section). Flagged: this may be considered a deployment/security concern
      deferred to another standard.

      **Resolved.** Closed by `15-headers.adoc`, new "CORS" section, placed
      before "Prefer header". Requires CORS support for browser-integrated
      APIs, recommends an allowed origin of `*` enforced via OAuth 2.0 Bearer
      tokens rather than per-origin credential validation (cross-referencing
      the Authentication and authorization section), and documents the
      "simple" vs preflighted request distinction and the
      `Access-Control-Allow-Methods`/`Access-Control-Allow-Headers` response
      requirement. Note: on re-verification, the digitalspecs.
      portofantwerpbruges.com source's Security section was found not to
      address CORS at all — that citation was a mis-attribution in the
      original analysis. The section as written is sourced from the
      Microsoft API Guidelines only.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-2-url-length`
      and `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#uri-path-design`
      — A URL-length limit (the references cite 2083 / 2048 characters) and the
      `414 URI Too Long` status code for unparseable over-long request targets
      are not addressed. Recommend placing at `06-urls.adoc`.

      **Resolved.** Closed by `06-urls.adoc`, new "URL length" section, and
      `05-http-status-codes.adoc`, a new `414 URI Too Long` entry in the
      status-code subset. Recommends a 2048-character practical limit
      (Robinyo's figure, the more conservative of the two cited), requires
      `414` on an unparseable over-long target, and cross-references the
      multi-value filtering and complex-search-action sections as the
      standard's existing escape hatches for endpoints that would otherwise
      risk the limit.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#6-2-variable-order-rule`
      — The rule that clients MUST NOT rely on JSON property/field order (and
      that services MAY support explicit ordering only via a documented sort
      contract) is not stated anywhere in the standard. Recommend placing at
      `16-payloads.adoc`.

      **Resolved.** Closed by `16-payloads.adoc`, "Naming conventions"
      section, new paragraph. States that clients MUST NOT rely on JSON
      object field order, and that a required explicit order MUST be
      conveyed structurally (eg. array position), cross-referencing the
      Sorting section of Collections as the standard's existing mechanism for
      client-requested ordering.

- [x] `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#security`
      and `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#security`
      — Specific authentication schemes for HTTP APIs (OAuth 2.0 with Bearer
      tokens over TLS; HTTP Basic Auth) are not prescribed; the standard's auth
      file is a stub (`02-authentication-and-authorization.adoc` carries only a
      TODO to extend it). Complements the API-keys gap above. Recommend placing
      at `02-authentication-and-authorization.adoc` (new section).

      **Resolved.** Closed by `02-authentication-and-authorization.adoc`, new
      "OAuth 2.0" and "HTTP Basic Authentication" sections. OAuth 2.0 is
      recommended as the default scheme for public-facing APIs, with a worked
      Bearer-token request example; Basic Authentication is permitted for
      simpler or machine-to-machine cases. Both sections state the TLS
      requirement, and a lead-in paragraph states it once for the whole
      "Authentication and authorization" page so it is not repeated per
      scheme.

## Partial

- [x] `api-style-guide.md:944` covers hypermedia link `href` more precisely than
      `16-payloads.adoc:630` — specifically, the reference requires `href` to be
      a URI Template per RFC 6570 and to be an absolute URI, whereas the
      standard's `LinkItem` schema types `href` as a bare string with no such
      constraint.

      **Resolved.** Closed by `16-payloads.adoc`, "Links" section prose
      (requires `href` to be an absolute URI, SHOULD resolve as a URI
      Template per RFC 6570) and both `LinkItem` JSON Schema definitions
      (illustrative and full appendix), which now add `"format": "uri"` to
      `href` and list `href` as `required`.

- [x] `api-style-guide.md:967` covers hypermedia link `method` more precisely
      than `16-payloads.adoc:630` — specifically, the reference makes `method`
      optional with a default of `GET` when omitted, whereas the standard's
      `LinkItem` defines `method` as a plain string with no default and its
      examples always include it.

      **Resolved.** Closed by `16-payloads.adoc`, "Links" section prose (`method`
      MAY be omitted, defaulting to `GET`) and both `LinkItem` JSON Schema
      definitions, which now add `"default": "GET"` to `method`. Written
      together with the `href` gap above, since both edit the same schema
      definitions and prose paragraph.

- [x] `api-style-guide.md:810` covers hypermedia client behaviour more
      prescriptively than `16-payloads.adoc:879` — specifically, the reference
      states clients SHOULD treat URIs as opaque identifiers and SHOULD NOT
      compose URIs themselves; the standard implies this in its "single entry
      point" use case (clients should not have every URL pattern hard-coded)
      but does not state the opaque-URI principle directly.

      **Resolved.** Closed by `16-payloads.adoc`, "Hypermedia use cases"
      section, new paragraph directly after the "single entry point" bullets.
      States that clients SHOULD treat `href` values as opaque identifiers
      and SHOULD NOT construct or compose URIs themselves, with the
      forward-compatibility rationale.

- [x] `patterns.md:152` covers transient actions more prescriptively than
      `11-actions.adoc` — specifically, the reference states transient actions
      MUST return `200 OK` with a response body of calculated values (which
      could differ if re-run) and SHOULD only be used after other alternatives
      are considered; the standard mentions the "dry run" concept but omits
      these response-shape and cautionary rules.

      **Resolved.** Closed by `11-actions.adoc`, extending the existing
      transient-operations paragraph. Requires `200 OK` with a calculated-result
      response body, notes the result MAY differ on repetition, and recommends
      considering resource-oriented alternatives first.

- [x] `patterns.md:123` covers composite action responses more prescriptively
      than `11-actions.adoc` — specifically, the reference shows a composite
      action response including HATEOAS links to every affected resource
      (`self`, `parent_payment`, `capture`); the standard describes composite
      actions conceptually but does not require or illustrate links to all
      affected resources in the response.

      **Resolved.** Closed by `11-actions.adoc`, new paragraph after the
      composite-actions introduction. Requires links to every affected
      resource in a composite action's response, with the refund example's
      `self`/`parent_payment`/`capture` links named directly.

- [x] `patterns.md:270-306` covers the standalone file upload more thoroughly
      than `08-resources.adoc:274` — specifically, the reference illustrates the
      full `multipart/form-data` request body (boundary, `Content-Disposition`
      with `filename`/`name`, a text metadata part plus a binary part) and
      requires the response to return a full file metadata set (`id`,
      `created_at`, `size`, `url`, `type`); the standard only requires "an
      identifier or URL" and shows no multipart body structure.

      **Resolved.** Closed by `08-resources.adoc`, "File uploads" section,
      extended with a worked `multipart/form-data` request (boundary,
      `Content-Disposition` with `name`/`filename`, a JSON metadata part plus
      a binary part) and a required response metadata set (`id`,
      `create_time`, `size`, `url`, `type`).

- [x] `patterns.md:782` covers bulk-operation error correlation more
      thoroughly than `07-collections.adoc:196` — specifically, the reference
      documents an attribute-filter JSON Pointer form
      (`/items/@account_number=='2097094104180012047'/address_id`) as an
      alternative to index-based correlation; the standard only describes the
      index-based form (`/items/1/currency_code`).

      **Resolved.** Closed by `07-collections.adoc`, "Bulk operations"
      section, extending the existing `field` JSON Pointer paragraph with the
      attribute-filter alternative form and a requirement that an API pick
      one form and document it, used consistently.

- [x] `patterns.md:730-734` covers bulk update/replace more thoroughly than
      `07-collections.adoc:196` — specifically, the reference models the bulk
      request as a first-class, uniquely identifiable batch resource returned
      to the client, against which subsequent `PUT`/`PATCH` operations act via
      the batch id; the standard covers bulk create but not this batch-as-
      resource pattern for later updates.

      **Resolved.** Closed by `07-collections.adoc`, new "Bulk update and
      replace" subsection. Documents a bulk-create response optionally
      returning a `batch_id`, and subsequent `PUT`/`PATCH` requests addressed
      to that batch to update its constituent items, with the same
      atomic/partial response-shape rules as bulk create.

- [x] `patterns.md:565` covers asynchronous-operation hypermedia more
      thoroughly than `12-asynchronous-operations.adoc` — specifically, the
      reference says links SHOULD let the client find operation status AND
      perform get/update/delete on the operation; the standard only addresses
      `GET` status links.

      **Resolved.** Closed by `12-asynchronous-operations.adoc`, extending
      the temporary-status-URL option with a worked example showing a
      `cancel`/`DELETE` link alongside `self`/`GET`, and a rule that every
      supported operation on the resource gets its own link. Note: the ninth
      run's "Operations resource" section already added `GET`/`DELETE`
      support on the underlying resource; this closes the remaining gap,
      that the *hypermedia links themselves* should expose all supported
      operations, not only `self`.

- [x] `api-style-guide.md:2088` covers the address `admin_area` field more
      precisely than `19-common-types.adoc:80` — specifically, the reference
      ties the administrative-area component to ISO 3166-2 subdivisions; the
      standard uses a generic `admin_area` field name without referencing the
      ISO 3166-2 standard.

      **Resolved.** Closed by `19-common-types.adoc`, "Addresses" section,
      extended with a sentence recommending the ISO 3166-2 subdivision code
      for `admin_area` where the value needs programmatic validation or
      comparison, rather than only display.

- [x] `api-style-guide.md:2147` covers floating month/year values more
      thoroughly than `19-common-types.adoc:91` — specifically, the reference
      defines a dedicated `date_year_month.json` common type for floating
      month/year values such as card expiry (`2016-09`); the standard mentions
      card expiry as a floating-date example but defines no year-month
      representation.

      **Resolved.** Closed by `19-common-types.adoc`, "Dates, times, and time
      zones" section, new bullet after the floating-value rule. Defines a
      `year_month` string in `YYYY-MM` format for floating month/year values
      such as card expiry.

- [x] `api-style-guide.md:2462` covers the error catalog more thoroughly than
      `16-payloads.adoc:1306` — specifically, the reference includes a
      `legacy_code` field for backward compatibility with existing published
      error metadata; the standard's catalog spec omits it.

      **Resolved.** Closed by `16-payloads.adoc`, "Error catalog" section, new
      `legacy_code` bullet in the error specification field list, scoped to
      already-published codes that must remain supported. Written together
      with the worked-example gap below, since both extend the same list.

- [x] `api-style-guide.md:2543` covers error catalog usage more concretely than
      `16-payloads.adoc:1306` — specifically, the reference provides worked
      sample catalogs for several namespaces showing realistic error names,
      status codes, and issue mappings; the standard describes the catalog
      structure but gives no full worked example.

      **Resolved.** Closed by `16-payloads.adoc`, "Error catalog" section, new
      worked `payments`-namespace catalog entry example.

- [x] `api-style-guide.md:2220` covers JSON-Pointer field identification more
      thoroughly than `16-payloads.adoc:1126` — specifically, the reference
      states that existing APIs using other means to identify the `field` may
      continue, but migrating to JSON Pointer requires a major version bump;
      the standard mandates JSON Pointer without addressing migration of
      legacy field-identification schemes.

      **Resolved.** Closed by `16-payloads.adoc`, "JSON Pointer usage"
      section, new paragraph. Permits an already-`LIVE` API to keep an
      existing non-JSON-Pointer `field` scheme, and requires migrating one to
      JSON Pointer to ship as a new major version, cross-referencing
      Versioning.

- [x] `api-style-guide.md:2807` covers new-major-version justification more
      concretely than `17-versioning.adoc:107` — specifically, the reference
      structures the justification into three categories (Business Case, API
      Design, Migration Strategy) with explicit sub-questions; the standard
      states the principle ("document why, what value, how consumers will be
      supported") but not the structured checklist.

      **Resolved.** Closed by `17-versioning.adoc`, extending the existing
      new-major-version paragraph with the three-category checklist (Business
      case, API design, Migration strategy), each with the reference's
      sub-questions, including the security-issue exception for the
      alternatives-considered item.

- [x] `patterns.md:390` covers multi-step action hypermedia more thoroughly
      than `16-payloads.adoc:879` — specifically, the reference notes that an
      unsuccessful step in a multi-step process MAY return only a link to send
      the corrected/missing data (eg. a `PATCH` link); the standard describes
      the happy-path chaining of a multi-step entry point but not the
      error-correction link.

      **Resolved.** Closed by `16-payloads.adoc`, "Hypermedia use cases"
      section, extending the multi-step-process bullet with the
      error-correction case: a failed step MAY return only a `PATCH`-style
      link back to itself instead of a next-step link.

- [x] `https://datatracker.ietf.org/doc/rfc7807/#section-3` and
      `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#http-status-codes-and-errors`
      cover HTTP error response formats more standardly than
      `16-payloads.adoc:1080` — specifically, RFC 7807 Problem Details
      (`application/problem+json` with `type`/`title`/`status`/`detail`/
      `instance` and extension members) is the IETF's portable error format;
      the standard defines a thorough custom error schema but never references
      or aligns with RFC 7807 (now obsoleted by RFC 9457). Recommend noting
      the relationship at `16-payloads.adoc` (Error handling).

      **Resolved.** Closed by `16-payloads.adoc`, "Error handling" section,
      new NOTE admonition before the error response schema. States that the
      schema is not an RFC 7807 implementation, maps RFC 7807's members to
      the schema's closest equivalents, and explains the schema is retained
      for its richer `details` array, `links`, and catalog machinery.

- [x] `https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/database-transactions-optimistic-concurrency#implement-optimistic-concurrency-control-using-etag-and-http-headers`
      and `https://learn.microsoft.com/en-us/azure/search/search-howto-concurrency#how-it-works`
      cover conditional requests more thoroughly than
      `13-concurrency-control.adoc` — specifically, the references describe
      `If-None-Match` for cache validation (the client decides whether a
      refetch is needed) and the `304 Not Modified` response, whereas the
      standard documents only `If-Match`/`412` for optimistic concurrency and
      mentions `ETag` "conditional requests" in `15-headers.adoc` without
      specifying the `If-None-Match`/`304` path. Recommend placing at
      `13-concurrency-control.adoc` or `15-headers.adoc` (Response caching).

      **Resolved.** Closed by `13-concurrency-control.adoc`, new "Cache
      validation" section. Requires `If-None-Match` support and `304 Not
      Modified`, distinguishes this client-driven refetch-avoidance use from
      `If-Match`'s lost-update guard, and cross-references Response caching.
      Written together with the client retry pattern gap below, since both
      extend the same file.

- [x] `https://learn.microsoft.com/en-us/azure/search/search-howto-concurrency#design-pattern`
      and `https://fideloper.com/etags-and-optimistic-concurrency-control#notes`
      cover the optimistic-concurrency client retry pattern more thoroughly
      than `13-concurrency-control.adoc` — specifically, the references
      prescribe a bounded loop (GET latest → apply changes locally → attempt
      conditional update with `If-Match` → on `412` re-fetch and retry) and
      note the server policy for requests with no `If-Match`; the standard
      describes the precondition check but not the client retry loop or the
      missing-header policy. Recommend placing at `13-concurrency-control.adoc`
      (new subsection).

      **Resolved.** Closed by `13-concurrency-control.adoc`: a new paragraph
      states the API-side policy question for a missing `If-Match` header,
      and a new "Client retry pattern" section documents the bounded
      GET-apply-attempt-retry loop.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#13-2-9-retry-after`
      and `https://datatracker.ietf.org/doc/rfc7807/#section-4` cover the
      `Retry-After` header more thoroughly than `05-http-status-codes.adoc:85`
      — specifically, the standard mentions `Retry-After` only for `429 Too
      Many Requests`, whereas the references also use it for `202 Accepted`
      (long-running operations) and retryable `5xx`/transient errors
      (`503`), and allow it to be either seconds or an HTTP-date. Recommend
      extending at `12-asynchronous-operations.adoc` and the `503` entry in
      `05-http-status-codes.adoc`.

      **Resolved.** Closed by `05-http-status-codes.adoc`: the `503` entry now
      recommends `Retry-After`, and a new paragraph after the status-code list
      states `Retry-After` also applies to `202 Accepted` and other retryable
      errors, and MAY be seconds or an HTTP-date per RFC 7231.

- [x] `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#implement-asynchronous-methods`
      covers asynchronous resource creation completion more concretely than
      `12-asynchronous-operations.adoc` — specifically, the reference prescribes
      returning `303 See Other` with a `Location` header pointing to the newly
      created resource once an async resource-creating operation completes;
      the standard describes polling the final URL (which returns `404` until
      ready) but not the `303 See Other` completion pattern. Recommend placing
      at `12-asynchronous-operations.adoc`.

      **Resolved.** Closed by `12-asynchronous-operations.adoc`, new paragraph
      after the temporary-status-URL option. Requires the status endpoint to
      respond `303 See Other` with a `Location` header once a resource-creating
      async operation completes, with a worked example.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#13-2-stepwise-long-running-operations`
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

      **Resolved.** Closed by `12-asynchronous-operations.adoc`, new
      "Operations resource" section. Documents a `/operations` collection
      with pagination/sorting/filtering, the required `status`/`create_time`/
      `update_time`/`percent_complete` fields, idempotent `DELETE` for
      cancellation, and per-API-documented tombstone retention. Note: on
      re-verification, the source specifies no fixed minimum retention
      period ("services MAY choose to delete tombstones after a service
      defined period of time") — the "minimum 24-hour" figure in this gap's
      original wording does not appear in the source, so the resolution
      requires retention to be documented per API rather than prescribing a
      specific duration. The `Operation-Location` header was folded into the
      existing "second option" `href`/status-URL pattern rather than added
      as a separate header, since the standard already conveys the
      equivalent information via hypermedia links rather than headers, per
      *Header reliability* in `15-headers.adoc`.

- [x] `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#patch-requests`
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

      **Resolved.** Closed by `08-resources.adoc`, "Updating" section: names
      the plain partial-representation form as JSON Merge Patch
      (`application/merge-patch+json`) with its `null`-ambiguity caveat,
      labels the JSON Patch example with the correct
      `application/json-patch+json` media type (the existing example
      incorrectly used bare `application/json-patch`), and requires
      `415 Unsupported Media Type` for an unsupported `Content-Type`. Note:
      correcting the pre-existing incorrect media type in the worked example
      was necessary to avoid the new prose contradicting it.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#11-4-durations`
      (and `#11-5-intervals`, `#11-6-repeating-intervals`) and
      `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#json-guidelines`
      cover ISO 8601 durations and intervals more thoroughly than
      `19-common-types.adoc:91` — specifically, the references serialize
      durations (`P3Y6M4DT12H30M5S`), intervals (start/end, start/duration),
      and repeating intervals (`R[n]/`) per ISO 8601; the standard's dates
      section covers RFC 3339 date-times and floating dates but no duration or
      interval representation. Recommend placing at `19-common-types.adoc`
      (Dates, new subsection).

      **Resolved.** Closed by `19-common-types.adoc`, new "Durations and
      intervals" section. Documents ISO 8601 duration strings, the three
      interval forms (start/end, start/duration, duration/end), and repeating
      intervals, each with a worked example.

- [x] `https://www.learnjsonschema.com/2020-12/validation/type/` and
      `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#11-json-standardizations`
      cover JSON number precision more generally than
      `19-common-types.adoc:30` — specifically, the references state the
      general interoperability rule that integers beyond 2^53 (and any number
      exceeding IEEE 754 double precision) should be serialized as strings, and
      OData's `IEEE754Compatible` mode for 64-bit integers; the standard
      applies the string-for-precision rule to monetary amounts only. Recommend
      placing at `19-common-types.adoc` (new subsection on number
      representation).

      **Resolved.** On re-verification, the premise was stale: TS-21 already
      states the general 2^53/IEEE-754 rule at `16-payloads.adoc`'s
      "Primitive types" section (not monetary-specific), which predates this
      gap analysis. Extended that existing rule with a sentence naming
      OData's `IEEE754Compatible` mode as an alternative approach this
      standard does not adopt, and added a cross-reference from
      `19-common-types.adoc`'s Money section back to the general rule, so the
      two are discoverable from each other. No new subsection was needed.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#6-1-ignore-rule`
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

      **Resolved.** Closed by `17-versioning.adoc`, "Payload stability"
      section, two new paragraphs after the compatibility-rules list. States
      the Tolerant Reader rule for responses (clients MUST ignore unknown
      fields) and the deliberate asymmetry for requests (servers SHOULD
      reject an unrecognized request field with `400 Bad Request`), with the
      rationale for each.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-6-standard-response-headers`
      and `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#standard-response-headers`
      cover the `Preference-Applied` response header more thoroughly than
      `15-headers.adoc:109` — specifically, the references require a
      `Preference-Applied` response header indicating whether a `Prefer`
      request preference was honoured; the standard documents the `Prefer`
      request header and its tokens but not the `Preference-Applied` response.
      Recommend placing at `15-headers.adoc` (Prefer section).

      **Resolved.** Closed by `15-headers.adoc`, `Prefer` header section, new
      paragraph after the token documentation. Requires a `Preference-Applied`
      response header naming which requested preferences were honoured, with
      a worked example.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-5-standard-request-headers`
      (and `#7-6-standard-response-headers`) cover the `Date` header more
      thoroughly than `15-headers.adoc` — specifically, the references require a
      `Date` header (RFC 5322, GMT) on all responses; the standard does not
      mention the `Date` header. Recommend placing at `15-headers.adoc`.

      **Resolved.** Closed by `15-headers.adoc`, new "`Date` header" section.
      Requires every response to include a `Date` header, RFC 5322-formatted,
      in GMT, with a worked example.

- [x] `https://microsoft.github.io/code-with-engineering-playbook/design/design-patterns/rest-api-design-guidance/#creating-api-contracts`
      (and `#design-first-approach`, `#code-first-approach`) covers API
      contract authoring more thoroughly than `18-documentation.adoc` —
      specifically, the reference sets out the design-first (OpenAPI contract
      first) vs code-first trade-offs (early feedback, parallel
      producer/consumer development, generated SDKs vs OpenAPI drift,
      committing generated OpenAPI to VCS); the standard's documentation file
      is a stub containing only a TODO to "Add notes on preferred IDLs such as
      OpenAPI". Recommend placing at `18-documentation.adoc`.

      **Resolved.** Closed by `18-documentation.adoc`, which is no longer a
      stub: a lead-in paragraph recommends a machine-readable IDL such as
      OpenAPI, and a new "Design-first versus code-first" section documents
      both approaches' trade-offs (early feedback and parallel work vs rapid
      iteration and drift risk), plus a rule to commit the interface
      definition to version control regardless of approach.

- [x] `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#errors`
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

      **Resolved.** Closed by `16-payloads.adoc`, "Error catalog" section, new
      "Canonical error names" subsection. Recommends the nine canonical
      `name` values (`INVALID_ARGUMENT` through `UNAVAILABLE`) as a shared
      vocabulary across an organization's APIs, permits API-specific
      additions, and states that adding a new canonical name is a breaking
      change, cross-referencing Versioning.

- [x] `https://github.com/Robinyo/restful-api-design-guidelines/blob/master/readme.md#error-propagation`
      covers error propagation from upstream services more thoroughly than
      `16-payloads.adoc` and `05-http-status-codes.adoc` — specifically, the
      reference states services MUST NOT blindly propagate upstream errors
      (hide implementation details; re-map responsibility, eg. upstream `400`
      → own `500`); the standard mentions upstream interactions only in the
      context of `422` and does not address error masking/remapping. Recommend
      placing at `16-payloads.adoc` (Error handling) or
      `05-http-status-codes.adoc`.

      **Resolved.** Closed by `16-payloads.adoc`, "Status reporting rules"
      section, new bullet. Requires a service not to blindly propagate an
      upstream dependency's error response, with the upstream-`400`-becomes-
      own-`500` example and the implementation-detail-leakage rationale.

- [x] `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#http-status-codes-and-errors`
      and `https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/#handle-errors-gracefully-and-return-standard-error-codes`
      cover leakage of implementation details in errors more explicitly than
      `03-security.adoc` — specifically, the references state that error
      responses MUST NOT expose stack traces or information useful to
      attackers; the standard's security file is a stub and its error section
      does not state this hygiene rule. Recommend placing at `03-security.adoc`
      or `16-payloads.adoc` (Error handling).

      **Resolved.** Closed by `03-security.adoc`, new paragraph prohibiting
      stack traces, internal file paths, database error messages, and
      internal framework/library identification in error responses, with the
      known-vulnerability-fingerprinting rationale, cross-referenced from a
      tightened `16-payloads.adoc` "5xx SHOULD limit information" bullet
      (now also `MUST NOT` include a stack trace specifically).

- [x] `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#support-partial-responses`
      covers partial-content retrieval of large/binary resources more
      thoroughly than `08-resources.adoc:274` — specifically, the reference
      prescribes `Accept-Ranges`/`Range`/`Content-Range` and `206 Partial
      Content` for ranged GETs (plus `HEAD` to discover metadata first); the
      standard covers multipart file upload but not ranged/partial download.
      Flagged: borderline scope (the standard is JSON-focused), but symmetric
      with its upload guidance. Recommend placing at `08-resources.adoc` (new
      subsection).

      **Resolved.** Closed by `08-resources.adoc`, new "Partial content"
      subsection under "Reading". Documents `Accept-Ranges: bytes`
      discovery, an optional `HEAD`-first size check, the `Range` request
      header, and the `206 Partial Content`/`Content-Range` response, with a
      worked example. `206` was added to the documented status-code subset
      in `05-http-status-codes.adoc`.

- [x] https://brandur.org/http-transactions ("Using Atomic Transactions to
      Power an Idempotent API" — The 1:1 Model) covers the request-as-
      transaction principle more directly than `11-actions.adoc:25-33`
      (composite actions commit all changes together) and
      `07-collections.adoc:255,265` (bulk operations SHOULD be atomic) —
      specifically, the article states the general principle that every
      idempotent HTTP request maps 1:1 to a single backend database
      transaction, so all operations in the request commit or abort
      together; frames the ordinary request lifecycle (clear beginning,
      end, single result) as a transactional boundary; and motivates it
      with the failure modes (client disconnects mid-request, application
      bugs failing a request partway, timeouts) that occur regularly at
      volume and against which a wrapping transaction protects integrity.
      TS-21 states atomicity only for composite actions and bulk
      operations, never as a general per-request principle. Recommend a
      new "Request-scoped transactions" subsection in `11-actions.adoc` (or
      a new file) stating the 1:1 request↔transaction model for idempotent
      requests. Note: the transaction-isolation mechanism this relies on
      is TS-43's scope.

      **Resolved.** Closed by `11-actions.adoc`, new "Request-scoped
      transactions" section, placed after the composite-actions
      introduction. States the 1:1 request↔transaction principle as a
      general default (not only for composite actions/bulk operations),
      the failure-mode rationale, and the local/foreign distinction that
      hands off to the "Genuinely non-idempotent operations" section below.
      A NOTE attributes the isolation mechanism to TS-43.

- [x] https://brandur.org/http-transactions ("A simple user creation
      service") covers naturally-idempotent endpoint design more directly
      than `10-safeness-and-idempotency.adoc:25-31` (GET/HEAD/PUT/DELETE
      idempotent by definition; PATCH SHOULD be) and
      `04-http-methods.adoc:32` (PUT for create with a client-generated
      identifier) — specifically, the article's philosophy that a healthy
      majority of endpoints can be made idempotent *by massaging verbs and
      behaviour* (eg. `PUT /users?email=...` with a check-then-insert inside
      the transaction returning `201 Created` on first creation and `200 OK`
      on a repeat), preferring such naturally-idempotent shapes before
      reaching for idempotency keys, and moving non-idempotent network
      calls to background jobs. TS-21 covers PUT-for-create and async
      operations (`12-asynchronous-operations.adoc:8-13`) but takes the
      opposite posture on the rest — treating POST as inherently
      non-idempotent and prescribing idempotency keys as the universal
      remedy (`10-safeness-and-idempotency.adoc:45`) — and never describes
      the check-then-insert `201`/`200` pattern or the "design the endpoint
      itself to be idempotent" guidance. Recommend a new "Naturally-
      idempotent endpoint design" subsection in `10-safeness-and-idempotency.adoc`
      advocating idempotent shapes before idempotency keys.

      **Resolved.** Closed by `10-safeness-and-idempotency.adoc`, new
      "Naturally-idempotent endpoint design" section, placed before
      "Idempotency keys". Documents the check-then-insert `PUT` pattern with
      a worked `201`/`200` example, states the preference for
      naturally-idempotent shapes over idempotency keys, and recommends
      moving non-idempotent network calls to background jobs, cross-
      referencing Asynchronous operations.

- [x] https://brandur.org/http-transactions ("Non-idempotent requests")
      covers genuinely non-idempotent operations more directly than
      `10-safeness-and-idempotency.adoc:33-104` (the idempotency-key
      cache-and-replay mechanism) and `11-actions.adoc:9-11` (lists
      "charge a credit card" as an action) — specifically, the article
      argues that response-cache idempotency keys are *insufficient* for
      operations with irreversible external side effects (calling an
      external payment gateway with a credit card, provisioning a server,
      any synchronous network request), because the side effect cannot be
      safely replayed; such operations must instead be built on
      *multi-stage transactions* where each stage is recorded as a
      separate transactional step so retries resume from the last
      committed state. TS-21 prescribes idempotency-key cache-and-replay
      as the complete solution for all non-idempotent operations, never
      calls out this distinct class, never warns that cache-and-replay
      does not protect external side effects, and never describes
      multi-stage transactions or any resumable/recoverable model.
      Recommend a new "Genuinely non-idempotent operations" subsection
      in `10-safeness-and-idempotency.adoc` distinguishing external-side-
      effect operations and describing multi-stage transactions (with a
      forward reference to idempotency keys per the article's part two).

      **Resolved.** Closed by `10-safeness-and-idempotency.adoc`, new
      "Genuinely non-idempotent operations" section, placed before
      "Idempotency keys". Defines the local/foreign distinction, explains
      precisely why cache-and-replay is insufficient (it protects only
      post-response retries, not the disconnect-before-response case that
      actually motivates retries), and forward-references "Idempotency
      keys with atomic phases" for the multi-stage-transaction mechanism.

- [x] https://brandur.org/idempotency-keys ("Implementing Stripe-like
      Idempotency Keys in Postgres") realizes the multi-stage-transaction
      model that entry E above anticipates, adding concrete machinery TS-21
      lacks — specifically: (a) the idempotency-key record carries request
      *status*, and on retry with the same key the server *continues the
      state machine from where it left off* rather than merely replaying a
      cached response (`10-safeness-and-idempotency.adoc:45-104` is
      cache-and-replay only); (b) *atomic phases* — local state mutations
      executed in a transaction *between* foreign state mutations, with each
      phase committed *before* initiating any foreign mutation so local
      state records what happened for retry (TS-21's atomicity is whole-
      request via composite actions `11-actions.adoc:21-33`, not phased);
      (c) *recovery points* — named checkpoints (`started` → … →
      `finished`) stored on the idempotency-key record, the transition
      committed with the phase, letting a retried request jump to just
      before the last failure; and (d) the request as a *directed acyclic
      graph state machine* whose states are recovery points, moving
      forward-only to `finished`. Recommend a new "Idempotency keys with
      atomic phases" subsection in `10-safeness-and-idempotency.adoc`
      (extending entry E's proposed "Genuinely non-idempotent operations"
      subsection) covering state-machine recovery, atomic phases, recovery
      points, and the DAG. Note: the SERIALIZABLE-upsert mechanism is TS-43's
      scope.

      **Resolved.** Closed by `10-safeness-and-idempotency.adoc`, new
      "Idempotency keys with atomic phases" section with two subsections:
      "Recovery points and the request state machine" (a)/(c)/(d) — the
      `recovery_point` field, the DAG-shaped forward-only state machine, and
      resuming a retry from the stored checkpoint — and "Atomic phases" (b)
      — the three phase-structuring rules and why committing each local
      phase before the next foreign mutation is what makes the sequence
      resumable.

- [x] https://brandur.org/idempotency-keys ("The idempotency key relation" /
      "Idempotency key upsert") covers idempotency-key concurrency control
      not addressed in TS-21 — specifically: a `locked_at` field and lock-
      acquisition on a seen key; `409 Conflict` for an in-progress
      (already-locked) key or for a params mismatch (TS-21 uses `422` for
      the mismatch at `10-safeness-and-idempotency.adoc:91-92` and does not
      list `409` in its status-code subset at `05-http-status-codes.adoc:46-88`);
      the upsert run under `SERIALIZABLE` isolation so two concurrent
      transactions locking the same key see one aborted; unlock-on-error so
      another request can retry; and an already-`finished` key short-
      circuiting to return the stored response. Recommend a new
      "Idempotency-key locking" subsection in `10-safeness-and-idempotency.adoc`
      (and consider documenting `409 Conflict` for in-progress idempotency
      keys). Note: the SERIALIZABLE-upsert mechanism is TS-43's scope.

      **Resolved.** Closed by `10-safeness-and-idempotency.adoc`, new
      "Idempotency-key locking" section: `locked_at` field, the five-way
      lookup-and-lock outcome (create-and-lock / acquire-and-proceed /
      `409` in-progress / `422` params mismatch, preserving TS-21's existing
      rule / short-circuit on already-finished), the `SERIALIZABLE`
      requirement (attributed to TS-43), and unlock-on-error. `409 Conflict`
      added to the documented status-code subset in
      `05-http-status-codes.adoc`, cross-referencing this section.

- [x] https://brandur.org/idempotency-keys ("Foreign state mutations" /
      "Other processes" / "Complications" / "Cultivating passive safety")
      covers operational and design-philosophy aspects not addressed in
      TS-21 — specifically: (a) the explicit *local (ACID, rollbackable) vs
      foreign (irreversible — once the first foreign mutation is made
      you're committed and must not lose track of it)* taxonomy, including
      that internal infrastructure calls (eg. Kafka) count as foreign, not
      atomic; (b) *supporting processes* — a *completer* that finds
      unfinished requests whose clients have dropped and pushes them to
      completion, and a *reaper* that deletes old idempotency keys after a
      ~72h threshold (long enough to survive a bad Friday deploy through the
      weekend) and surfaces permanently-failed requests for human attention
      (TS-21 has only a 24h response-purge at
      `10-safeness-and-idempotency.adoc:100-104`, no completer); (c)
      *indeterminate-error handling* — when a foreign mutation is non-
      idempotent and the foreign service provides no idempotency-key
      mechanism, a failure may have to be persisted as permanently errored,
      and indeterminate errors (connection reset, timeout) must be marked
      failed (conservative), with an exception for an explicit "safe to
      retry" signal; and (d) *passive safety* as an explicit design goal —
      a backend should end in a stable state regardless of failures, with
      users never left broken, idempotent transactions and idempotency keys
      with atomic phases being the two complementary techniques. Recommend
      folding (a)-(d) into the new idempotency-key/atomic-phase subsections
      proposed above. Note: (b)'s enqueuer is the transactional outbox (see
      `../023/GAPS.md`).

      **Resolved.** Closed by `10-safeness-and-idempotency.adoc`: (a) new
      "Foreign state mutations" section states the local-vs-foreign
      taxonomy, explicitly including internal infrastructure (eg. Kafka) as
      foreign; (b) its "Completer and reaper" subsection documents both
      processes, the ~72h retention threshold (superseding the prior 24h
      figure, which is now folded into this subsection rather than standing
      alone), and surfacing permanently-failed requests for human
      attention; (c) its "Indeterminate errors" subsection states the
      conservative default and the "safe to retry" exception; (d) new
      "Passive safety" section states the design goal and names
      request-scoped transactions plus idempotency keys with atomic phases
      as the two complementary techniques. Note: (b)'s enqueuer being the
      transactional outbox was not restated here, since it is TS-23's
      concern and TS-23's own `GAPS.md` already carries the cross-reference
      the other direction.

## Out-of-scope

- [x] `api-style-guide.md:194-232` covers this, but it plausibly sits outside
      this standard's stated purpose because the concepts are PayPal-internal
      organizational constructs (Capability APIs vs Experience-specific APIs,
      the Business Capability Model, and the domain/capability orthogonality)
      rather than general HTTP API design rules. Flagged for the user to
      confirm or overrule.

      **Confirmed out-of-scope.** 2026-08-14. PayPal-internal organizational
      modeling is not general HTTP API design content.

- [x] `api-style-guide.md:27-44` covers this, but it plausibly sits outside
      this standard's stated purpose because it is document-level convention
      (RFC 2119 keyword interpretation, all-caps rendering of "REST"/"JSON",
      fixed-width rendering of machine-readable text, URI Template RFC 6570 for
      variable blocks) governed by the project's style guide rather than by
      TS-21's content. Flagged for the user to confirm or overrule.

      **Confirmed out-of-scope for TS-21.** 2026-08-14. Per the user's
      direction, routed to TS-26 (Technical writing style guide) instead, as
      a new Missing item in its own `GAPS.md`, rather than being dropped —
      these document-level conventions belong to the standard that governs
      authoring style, not this one.

- [x] `api-style-guide.md:1297` and `api-style-guide.md:1443-1602` cover this,
      but it plausibly sits outside this standard's stated purpose because
      JSON Schema draft-version pinning (draft-04), OpenAPI tooling `$schema`
      handling, draft-03→draft-04 migration notes, and one-type-per-file schema
      file naming are JSON-Schema-authoring concerns deferred by TS-21 to
      TS-29 (which the standard already cross-references). Flagged for the user
      to confirm or overrule.

      **Confirmed out-of-scope.** 2026-08-14. JSON Schema authoring concerns
      belong to TS-29, which TS-21 already cross-references.

- [x] `api-style-guide.md:1776` and `api-style-guide.md:2501` cover this, but
      they plausibly sit outside this standard's stated purpose because they
      are implementation-language/infrastructure concerns (Oracle VARCHAR2
      column sizing for `maxLength`; Java `printf`-style formatting of error
      catalog strings) rather than API-design rules. Flagged for the user to
      confirm or overrule.

      **Confirmed out-of-scope.** 2026-08-14. Language/database-specific
      implementation details are orthogonal to what an HTTP API design
      standard should prescribe.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#9-7-filtering`,
      `#9-6-sorting-collections`, and `#9-8-pagination` (OData-style
      `$filter`/`$orderBy`/`$top`/`$skip` and `@nextLink`) cover this, but it
      plausibly sits outside TS-21's stated purpose because the standard
      deliberately specifies a lighter filtering/sorting/pagination model
      (`sort_by`/`sort_order`, `page`/`per_page`/`page_token`, hypermedia
      `next`/`prev`/`first`/`last` links) rather than the full OData query
      language; adopting OData's expression grammar would be a design change,
      not a gap. Flagged for the user to confirm or overrule.

      **Confirmed out-of-scope.** 2026-08-14. Adopting OData's query grammar
      wholesale would be a design change to TS-21's model, not a gap in it.
      OData is named, with a pointer to its full JSON format spec, in the new
      "Alternative HTTP API styles" section (`20-alternative-styles.adoc`).

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#10-delta-queries`
      and `https://docs.oasis-open.org/odata/odata-json-format/v4.0/odata-json-format-v4.0.html#deltaResponse`
      cover delta queries / change tracking (`$delta`, `@odata.deltaLink`,
      `@removed`), but it plausibly sits outside TS-21's stated purpose as an
      advanced, specialized collection-sync capability beyond the standard's
      pagination/filtering scope. Flagged for the user to confirm or overrule.

      **Confirmed out-of-scope.** 2026-08-14. Delta queries are a
      specialized sync capability beyond what a general HTTP API design
      standard needs to prescribe.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#14-push-notifications-via-webhooks`
      covers webhook subscription validation (`validationToken`
      challenge/response, `notificationUrl`, retry/back-off, no `301/302`
      redirects), but it plausibly sits outside TS-21's stated purpose because
      webhook implementation is deferred to TS-22 (which
      `12-asynchronous-operations.adoc` already cross-references). Flagged for
      the user to confirm or overrule.

      **Confirmed out-of-scope.** 2026-08-14. TS-22 is the dedicated webhooks
      standard, already cross-referenced from `12-asynchronous-operations.adoc`.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#8-cors`
      and rate-limit headers (`X-RateLimit-Limit`/`Remaining`/`Reset` per
      `https://digitalspecs.portofantwerpbruges.com/api-guidelines/#http-status-codes-and-errors`)
      cover this, but the rate-limiting mechanics plausibly sit outside TS-21's
      stated purpose because `05-http-status-codes.adoc:90` already carries a
      TODO to link to a dedicated rate-limiting standard once one exists, and
      cross-cutting network concerns are deferred to TS-20. (Note: the
      `429`+`Retry-After` status-code rule itself is already covered.) Flagged
      for the user to confirm or overrule.

      **Confirmed out-of-scope for TS-21.** 2026-08-14. Per the user's
      direction, routed to TS-20 (Network APIs) instead, as a new Missing
      item in its own `GAPS.md`, rather than being dropped — rate limiting is
      a cross-cutting network concern.

- [x] `https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#multitenant-web-apis`
      covers multitenancy identification (subdomain vs `X-Tenant-ID`/JWT claim
      vs path-based, and the cache-interaction caveat), but it plausibly sits
      outside TS-21's stated purpose as a deployment/architecture concern
      rather than an API-interface design rule. Flagged for the user to confirm
      or overrule.

      **Confirmed out-of-scope.** 2026-08-14. Multitenancy identification is
      more of an architecture/deployment decision than an HTTP interface
      design rule.

- [x] `https://www.gov.uk/government/collections/api-design-guidance#api-technologies`
      covers when to use GraphQL as an alternative to REST, but it plausibly
      sits outside TS-21's stated purpose because TS-21 is explicitly about the
      RESTful HTTP API style; choosing between paradigms is an architecture
      decision. Flagged for the user to confirm or overrule.

      **Confirmed out-of-scope.** 2026-08-14. TS-21 is scoped to RESTful HTTP
      APIs by its own stated purpose; when to reach for GraphQL instead is a
      separate architecture decision.

- [x] `https://github.com/microsoft/api-guidelines/blob/master/Guidelines.md#7-9-pii-parameters`
      covers not transmitting PII in URLs (use headers instead), but it
      plausibly sits outside TS-21's stated purpose because it overlaps the
      dedicated security and privacy standards (TS-52, TS-53). Flagged for the
      user to confirm or overrule.

      **Confirmed out-of-scope, with a cross-reference added.** 2026-08-14.
      The user asked for a pointer to TS-52/TS-53 to be added to TS-21 rather
      than leaving it entirely unaddressed. Closed by `03-security.adoc`, new
      paragraph prohibiting PII in URLs (path segments or query parameter
      values), with the logging/history rationale and cross-references to
      TS-52 (Security and secrets management) and TS-53 (Privacy and data
      protection) for the organization's broader PII handling requirements.

- [x] `https://stateless.co/hal_specification.html`,
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

      **Largely confirmed out-of-scope, with a brief survey added.** 2026-08-14.
      The user agreed these specifications' internal structure is out of
      scope, but asked for a short new closing section briefly covering these
      alternative HTTP API design styles, so a reader knows they exist and
      roughly what each one is for. Closed by a new
      `20-alternative-styles.adoc` partial ("Alternative HTTP API styles"),
      inserted before the references partial (renumbered
      `20-references.adoc` → `21-references.adoc`, `git mv`, page's include
      list updated). Its "Hypermedia media types" section gives one paragraph
      each for HAL, JSON:API, Siren, Ion, OData JSON Format (also naming its
      broader query-language and delta-query capabilities, cross-referencing
      the two Out-of-scope items below), and JSON-LD, cross-referencing the
      existing "takes cues from" mention in `16-payloads.adoc`'s Links
      section rather than duplicating it.

- [x] `https://www.jsonrpc.org/specification#overview` covers the JSON-RPC 2.0
      wire protocol (`jsonrpc`/`method`/`params`/`id`, notifications, batches,
      reserved error codes), but it plausibly sits outside TS-21's stated
      purpose because the standard is explicitly about the RESTful HTTP style
      and JSON-RPC is a different, transport-agnostic RPC paradigm (the
      standard mentions JSON RPC only as a lighter alternative envelope it does
      not adopt). Flagged for the user to confirm or overrule.

      **Confirmed out-of-scope, folded into the same new survey section.**
      2026-08-14. Closed by `20-alternative-styles.adoc`'s "RPC-style
      alternatives" section, contrasting JSON-RPC's single-endpoint,
      method-in-body model against TS-21's Actions (resource-oriented with
      RPC-style actions layered on top), and noting when an overwhelmingly
      RPC-shaped API might prefer JSON-RPC outright.

## Unresolved

- [x] `https://www.youtube.com/watch?v=etKM5-gGwto` (GOTO 2024, Mike Amundsen,
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

      **Dismissed.** 2026-08-15. Re-attempted via WebFetch; the page still
      returns only YouTube's footer/navigation chrome, no transcript or
      description text — confirming the JS-rendering limitation is
      persistent, not transient. No new gap derivable without a transcript.

- [x] `https://stackoverflow.com/questions/39789818/best-practice-for-passing-enum-params-in-web-api`
      — fetch blocked by a Cloudflare anti-bot challenge (HTTP 403). Not
      included in the comparison. (The enum topic was covered via the Appwrite,
      Wikipedia, and Laravel references, plus the standard's own
      `16-payloads.adoc` enum guidance.)

      **Dismissed.** 2026-08-14. Re-fetch attempted again; still blocked
      ("Claude Code is unable to fetch from stackoverflow.com"), confirming
      the block is persistent, not transient. Per the user's direction, this
      is dismissed rather than left open indefinitely, since the enum-params
      topic is already independently covered by the Appwrite, Wikipedia, and
      Laravel sources plus the standard's own existing enum guidance.

- [x] `https://stackoverflow.com/questions/61989114/rest-api-concurrency-check-using-etags`
      — fetch blocked by a Cloudflare anti-bot challenge (HTTP 403). Not
      included in the comparison. (The ETag/concurrency topic was covered via
      the Cosmos DB, Azure Search, and fideloper references.)

      **Dismissed.** 2026-08-14. Re-fetch attempted again; still blocked.
      Per the user's direction, dismissed — the ETag/concurrency topic is
      already independently covered by the Cosmos DB, Azure Search, and
      fideloper sources, all of which closed content in this run's
      "Idempotency-key locking" and "Cache validation" sections.

- [x] `https://stackoverflow.com/questions/12806386/is-there-any-standard-for-json-api-response-format`
      — fetch blocked by a Cloudflare anti-bot challenge (HTTP 403). Not
      included in the comparison. (The response-format topic was covered via
      RFC 7807, JSON:API, JSON-RPC, and the adnan-kamili references.)

      **Dismissed.** 2026-08-14. Re-fetch attempted again; still blocked.
      Per the user's direction, dismissed — the JSON-response-format-standard
      topic is already independently covered by RFC 7807, JSON:API, JSON-RPC
      (all closed or surveyed in this run), and the adnan-kamili source.