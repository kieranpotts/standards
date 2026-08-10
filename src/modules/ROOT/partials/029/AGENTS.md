# TS-29: JSON Schema

This is a compact version of technical standard TS-29 for AI agents.

Use this when designing or using JSON Schema — content types, versions,
`$ref` cross-references, JSON Hyper-Schema, OpenAPI, JSON-LD, JSON Pointer, and
JSON Type Definition (JTD). The emphasis is on _designing_ JSON Schema, though
there is also guidance on using published schemas such as JSON-LD. JSON Schema
provides a vocabulary for describing the structure of JSON data; the primary use
case is validating JSON documents, but documentation, code, and other artifacts
can also be generated from definitions. Commonly used to define data structures
transferred via network APIs, for input validation, runtime interface
definition, and data persistence schema (eg. document stores).

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT,
OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

- **Use the `application/schema+json` content type when serving JSON Schema via
  HTTP.**

  This is the official content type for JSON Schema. It is RECOMMENDED.

- **Use Draft 2020-12 for new projects.**

  The current version of JSON Schema is Draft 2020-12 (metaschema:
  `https://json-schema.org/draft/2020-12/schema`). Versions 00–04 were published
  as IETF drafts; draft-05 moved to the
  [community project](https://json-schema.org/). Draft 2020-12 is RECOMMENDED.

- **Use `$ref` to share common structures; prefer schema composition over
  inheritance.**

  Modular, reusable schema design manages growing complexity at scale — like
  code. Example: a `Locale` schema with `country_code`, `language`, and
  `timezone` properties each `$ref`-ing separate `.schema.json` files. However,
  it is RECOMMENDED NOT to require client applications to automatically resolve
  referenced schema. Instead, JSON Schema publishers SHOULD automatically swap
  `$ref` properties for inline schema using a build step (a
  [command-line bundling tool](https://github.com/sourcemeta/jsonschema/blob/main/docs/bundle.markdown)
  is available).

- **JSON Hyper-Schema embeds hypermedia links in JSON documents via a `links`
  array of link description objects (LDOs).**

  Use cases: enabling APIs to be navigated and explored dynamically (without
  clients having prior knowledge of all endpoints). Each LDO has `rel`
  (relationship — any IANA-registered link relation type), `href` (URI
  template), and optional `title`, `targetSchema`, `targetHints`,
  `templatePointers`. Common `rel` types: `self` (the resource itself),
  `next`/`prev` (sequence navigation, eg. paginated lists), `first`/`last`
  (sequence bounds), `up` (parent resource). It is RECOMMENDED to use a small
  subset of link relation types consistently across all endpoints and to always
  include `self` links where relevant. SHOULD NOT define custom relations unless
  no standard ones fit. Best practices: minimal links per response (just enough
  to navigate deeper); do not expose an entire API graph in a single response
  (except for very simple APIs); simple minimalist URI templates with only
  necessary path parameters; provide all required template variables in the
  response object; use `templatePointers` to map data to template variables;
  use `targetSchema` for expected response formats; use `targetHints` for media
  types and methods; add `title` for human-readable descriptions.

- **OpenAPI is a superset/dialect of JSON Schema for describing HTTP "RESTful"
  APIs.**

  It adds properties for HTTP-specific concepts. (The source file flags this
  section as a TODO for OpenAPI-specific best practices — broadly the same as
  for all JSON Schema.)

- **JSON-LD imbues JSON documents with semantic meaning via `@context` (a
  vocabulary reference) and `@type` (entity type).**

  Bridges semantic web concepts (RDF, OWL) and modern web service APIs.
  [Schema.org](https://schema.org/) is the most popular vocabulary (also
  embeddable in HTML via microdata or RDFa). It is RECOMMENDED to reuse existing
  vocabularies like Schema.org wherever there's a good fit — even partial reuse
  saves design effort and keeps data interoperable (interoperability may be
  needed in the future even if not now). Example: Schema.org's
  [Person type](https://schema.org/Person) (`givenName`, `familyName`,
  `jobTitle`, `telephone`) is a good basis for user/customer entity schemas. The
  W3C maintains [JSON-LD Best Practices](https://w3c.github.io/json-ld-bp/).

- **JSON Pointer (RFC 6901) identifies specific values in JSON documents; use
  it for cross-references within JSON documents.**

  A string beginning with `/`, with slashes separating path segments:
  `/path/to/property`. Array elements use zero-indexed numeric indices
  (`/users/0/name`). An empty string `""` refers to the entire document. Special
  escapes: `/` in property names is `~1`; `~` is `~0`. It is RECOMMENDED NOT to
  include `/`, `~`, or other special characters in property names, to make
  traversal as easy as possible for all clients. JSON Pointer is used for data
  extraction, validation, transformation, and partial updates via JSON Patch
  operations. RECOMMENDED for creating cross-references within JSON documents
  (eg. `"categoryRef": "/categories/2"`).

- **JSON Type Definition (JTD, RFC 8927) is a simpler alternative to JSON
  Schema, focusing on structural and type validation.**

  Lighter weight vocabulary, fewer constraints. Good for simple use cases where
  type safety is the primary concern rather than full schema validation. JSON
  Schema remains the _de facto_ standard and is RECOMMENDED for its expressive
  power and readily-available libraries/tooling; JTD is mentioned for
  completeness.

## References

- [TS-29 source](../../pages/029-json-schema.adoc)
- [JSON Schema](https://json-schema.org/)
- [JSON Schema Store](https://www.schemastore.org/json/)
- [JSON-LD](https://json-ld.org/)
- [Schema.org](https://schema.org/)
- [JSON Pointer (RFC 6901)](https://datatracker.ietf.org/doc/html/rfc6901)
- [JSON Type Definition (RFC 8927)](https://datatracker.ietf.org/doc/rfc8927/)
- [JSON-LD Best Practices (W3C)](https://w3c.github.io/json-ld-bp/)