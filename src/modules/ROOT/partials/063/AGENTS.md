# TS-63: URL Design

Design of URLs for all kinds of HTTP services — websites, web
applications, and HTTP APIs. Covers URL anatomy, path design, query
strings, fragments, and URL permanence.

Use this when designing or reviewing the URL structure of any HTTP
service.

Do NOT use this for HTTP API resource modeling, HTTP methods, or
status codes — see [TS-21: HTTP APIs](../021/AGENTS.md). For the HTTP
protocol and web platform APIs, see [TS-37: Web Platform
APIs](../037/AGENTS.md). For general user interface design principles,
see [TS-15: User Interfaces](../015/AGENTS.md). For web GUI
implementation, see [TS-18: Web GUIs](../018/AGENTS.md). For SEO
considerations that overlap with URL design, see [TS-19: Search
Engine Optimization (SEO)](../019/AGENTS.md).

## Rules

### Anatomy of a URL

- **HTTPS is REQUIRED for any production service.** URLs in
  documentation and links SHOULD use the `https` scheme.

- **Non-default ports SHOULD be avoided** in production URLs. Omit the
  port when it is the default for the scheme (80 for HTTP, 443 for
  HTTPS).

- **Scheme and host are case-insensitive and SHOULD be lowercase.**
  Path, query, and fragment are case-sensitive; to avoid ambiguity,
  treat them as case-sensitive and write them in lowercase.

### Path design

- **Path segments SHOULD be human-readable words** that describe the
  resource. Opaque identifiers, internal codes, and implementation
  details SHOULD NOT appear in paths intended for human consumption.

- **Path segments SHOULD use lowercase letters, digits, and hyphens
  only.** Words within a segment SHOULD be separated with hyphens
  (kebab-case), not underscores or camelCase.

  ```
  # Good:
  /charge-points/42
  /blog/how-to-design-urls

  # Poor:
  /ChargePoints/42
  /charge_points/42
  /chargePoints/42
  ```

- **Keep paths shallow.** Paths SHOULD NOT exceed three or four segments
  for websites, or five or six for HTTP APIs that model resource
  hierarchies.

- **Be consistent with trailing slashes.** A trailing slash indicates a
  collection or directory-like resource; its absence indicates a
  specific resource. Canonical URLs SHOULD omit the trailing slash for
  individual resources and use it only for collections. A service
  SHOULD accept both but SHOULD NOT redirect to the canonical version.

- **File extensions SHOULD NOT appear in URLs** (`.html`, `.php`,
  `.aspx`). They expose implementation details. Exceptions MAY be made
  where the extension carries semantic meaning (eg. `report.pdf`,
  `data.json`).

- **Resource identifiers SHOULD be the final path segment.** Opaque
  sequential identifiers MAY be used, but human-readable slugs are
  RECOMMENDED where the identifier is visible to end users.

### Query strings

- **The path identifies the resource; the query string parameterizes
  the request.** Values that change _which_ resource is identified belong
  in the path; values that change _how_ it is represented or selected
  belong in the query string.

  ```
  # Good:
  /articles?sort=date&order=desc

  # Poor:
  /articles?category=web
  ```

- **Query parameter names SHOULD be short, lowercase, and descriptive.**
  Multi-word names SHOULD use hyphens or underscores consistently within
  a single service; hyphens are RECOMMENDED.

- **Boolean parameters MAY be key-only flags (`?verbose`) or key-value
  pairs (`?verbose=true`).** A service SHOULD pick one convention and
  apply it consistently. Key-value pairs are RECOMMENDED for HTTP APIs.

- **Reserved characters in query strings MUST be percent-encoded.**
  Spaces SHOULD be encoded as `+` (in form-encoded contexts) or `%20`
  (elsewhere); a service SHOULD accept both.

### Fragments

- **Fragments identify a secondary resource** (typically a section within
  an HTML document) and are resolved client-side; they are not sent to
  the server.

- **In HTML, fragments SHOULD identify sections by heading text or an
  explicit `id`.** Fragments matching heading text are stable across
  content edits; auto-generated numeric IDs are not.

- **HTTP APIs SHOULD NOT rely on fragments** to convey request
  parameters, since fragments never reach the server.

### Permanence

- **A URL is a contract.** Once published, a URL SHOULD continue to
  resolve to the intended resource for as long as the resource exists
  (see [Cool URIs don't change](https://www.w3.org/Provider/Style/URI)).

- **Design for permanence from the start** by avoiding implementation
  details, technology choices, and transient organizational structures
  in URLs.

  ```
  # Good:
  /blog/url-design

  # Poor:
  /wordpress/2023/01/url-design.php
  ```

- **When a resource moves, the old URL SHOULD redirect** with an HTTP
  `301 Moved Permanently` to the new URL. Redirects SHOULD be maintained
  indefinitely. A `410 Gone` MAY be used for permanently removed
  resources with no replacement.

- **Avoid dates in URLs unless the date is part of the identity.**
  Including a publication date makes the URL brittle if the date is
  corrected. Dates are appropriate only when intrinsic to the resource
  (eg. a daily archive `/news/2023-01-15`).

## References

- [TS-63: URL Design (source)](../../pages/063.adoc)
- [TS-15: User Interfaces](../015/AGENTS.md)
- [TS-18: Web GUIs](../018/AGENTS.md)
- [TS-19: Search Engine Optimization (SEO)](../019/AGENTS.md)
- [TS-21: HTTP APIs](../021/AGENTS.md)
- [TS-37: Web Platform APIs](../037/AGENTS.md)
- [Cool URIs don't change — Tim Berners-Lee](https://www.w3.org/Provider/Style/URI)
- [Examples of Great URLs — Jim Nielsen](https://blog.jim-nielsen.com/2023/examples-of-great-urls/)
- [RFC 3986 — Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986)
- [URL Standard — WHATWG](https://url.spec.whatwg.org/)
- [URL structure — Google Search Central](https://developers.google.com/search/docs/crawling-indexing/url-structure)
