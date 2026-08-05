# TS-21 gap analysis

Gaps found comparing TS-21: HTTP APIs against the following reference
resources:

- `src/021/__TODO__/http/api-standards-master/api-style-guide.md`
- `src/021/__TODO__/http/api-standards-master/patterns.md`
- `src/021/__TODO__/http/api/api-keys.md`
- `src/021/__TODO__/http/api/errors.md`
- `src/021/__TODO__/http/api/http-methods.md`
- `src/021/__TODO__/http/api/index.md`
- `src/021/__TODO__/http/api/resources.md`
- `src/021/__TODO__/http/api/versioning.md`

**Assessment.** The bulk of the reference material (PayPal's API standards,
plus a set of short stub summaries) is already covered by TS-21 — the
standard was clearly derived from PayPal's guidelines and in most places is
more current and more thorough (it cites RFC 10008 `QUERY`, draft 2020-12
JSON Schema, and 2026-era guidance the reference lacks). Most findings below
are therefore *partial* rather than *missing*: targeted rules, response-payload
details, or alternative patterns the reference spells out that TS-21 omits or
under-specifies. A handful of genuine *missing* items cluster around the
standard's still-stub authentication section and a few URL/collection design
rules.

**Status:** First run. All gaps open. Date of last run: 2026-08-05.

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
      TS-29 (which the standard already cross-references). Flagged for the
      user to confirm or overrule.

- [ ] `api-style-guide.md:1776` and `api-style-guide.md:2501` cover this, but
      they plausibly sit outside this standard's stated purpose because they
      are implementation-language/infrastructure concerns (Oracle VARCHAR2
      column sizing for `maxLength`; Java `printf`-style formatting of error
      catalog strings) rather than API-design rules. Flagged for the user to
      confirm or overrule.