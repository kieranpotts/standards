# TS-20 gap analysis

Gaps found comparing TS-20: Network APIs against the following reference
resources (the standard's own `__TODO__` planning directory, which is
gitignored and contains the source notes the maintainers used to draft the
standard):

- `src/020/__TODO__/index.md`
- `src/020/__TODO__/_100-general-style.md`
- `src/020/__TODO__/_200-idempotency.md`
- `src/020/__TODO__/_250-latency.md`
- `src/020/__TODO__/_300-async.md`
- `src/020/__TODO__/_400-encoding.md`
- `src/020/__TODO__/_500-versioning.md`
- `src/020/__TODO__/_todo/0100-introduction.md`
- `src/020/__TODO__/_todo/0200-rest.md`
- `src/020/__TODO__/_todo/0205-rpc.md`
- `src/020/__TODO__/_todo/0210-graph.md`
- `src/020/__TODO__/_todo/0220-soap.md`
- `src/020/__TODO__/_todo/0300-best-practices.md`
- `src/020/__TODO__/_todo/0400-headers.md`
- `src/020/__TODO__/_todo/0500-authentication.md`
- `src/020/__TODO__/_todo/0800-hypermedia.md`
- `src/020/__TODO__/_todo/http-caching.md`
- `src/020/__TODO__/_todo/http-methods.md`
- `src/020/__TODO__/_todo/http-primer.md`
- `src/020/__TODO__/_todo/http-secure-protocol.md`
- `src/020/__TODO__/_todo/status-codes.md`
- `src/020/__TODO__/_todo/cookies.md`
- `src/020/__TODO__/_todo/urls.md`
- `src/020/__TODO__/_todo/idl.md`
- `src/020/__TODO__/_todo/linkbacks.md`
- `src/020/__TODO__/_todo/verification.md`
- `src/020/__TODO__/_todo/encoding.md`
- `src/020/__TODO__/_todo/versioning.md`
- `src/020/__TODO__/_todo/authentication.md`
- `src/020/__TODO__/_todo/GENERAL-NOTES.md`
- `src/020/__TODO__/_todo/9999-references.md`
- `src/020/__TODO__/_todo/Clean URL - Wikipedia.URL` → https://en.wikipedia.org/wiki/Clean_URL

**Assessment.** The `__TODO__` notes are substantially broader than the
published TS-20. The published standard deliberately narrows its scope and
explicitly defers HTTP-specific conventions (status codes, caching headers,
method semantics) to TS-21 — see `src/020/AGENTS.md`. Accordingly, a large
share of the notes (HTTP message structure, methods, status codes, headers,
caching, URL design, cookies, HTTPS/HSTS, REST/HATEOAS) is out-of-scope here
and is flagged as such for the user to confirm. Within TS-20's own stated
scope, the biggest genuine gaps are in security (OAuth, OpenID Connect, API
keys, token storage, key management, JWT structure), idempotency, and
encoding-format selection — these are topics the notes develop in depth that
the standard barely touches.

**Status:** Initial run. 0 of 18 in-scope gaps closed; 14 out-of-scope items
flagged for confirmation. Hypermedia reclassified from out-of-scope to missing
per user request (2026-08-05). Last run: 2026-08-05.

## Missing

- [ ] `src/020/__TODO__/_200-idempotency.md:3-11` — Idempotency: network
      retries risk performing a state-changing operation more than once;
      protocols MUST de-duplicate via a client-generated unique request ID
      (UUID) that the server logs. TS-20 does not mention idempotency
      anywhere. Recommend placing at `04-reliability-and-resilience.adoc` (new
      "Idempotency" section before "Error handling") — this is a core
      network-API reliability concern, not HTTP-specific.

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:236-278` — OAuth 1.0
      and 2.0 as a delegated authentication/authorization framework, including
      the four grant-type flows (authorization code, implicit, resource-owner
      password, client credentials). TS-20's security section
      (`06-security-and-privacy.adoc:6-17`) only recommends JWT and mentions
      scopes/refresh tokens, with no coverage of OAuth. Recommend placing at
      `06-security-and-privacy.adoc` (new "OAuth" subsection under
      "Authentication and authorization").

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:284-298` — OpenID
      Connect as an identity layer on OAuth 2.0 (ID tokens as JWTs, discovery
      via `.well-known/openid-configuration`, SSO). Not addressed anywhere in
      TS-20. Recommend placing at `06-security-and-privacy.adoc` (new
      "OpenID Connect" subsection).

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:302-329` — API keys as
      an auth mechanism: the `Authorization: Apikey <token>` convention, the
      rule that keys must NOT go in the query string, and their security
      weaknesses (suitable mainly for read-only APIs). TS-20 does not mention
      API keys at all. Recommend placing at `06-security-and-privacy.adoc`
      (new "API keys" subsection).

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:633-797` — Client-side
      token storage: the trade-offs between in-memory, Web Storage
      (localStorage/sessionStorage), and cookies, and the XSS/XSRF attack
      surface of each; the same-origin-proxy pattern. TS-20 says nothing
      about where clients should store tokens. Recommend placing at
      `06-security-and-privacy.adoc` (new "Token storage" subsection).

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:977-1047` —
      Cryptographic key management for signed tokens: symmetric vs
      asymmetric (public/private) signing, the `kid`/`jwk`/`x5u`/`jku`
      header claims, embedded vs distributed keys, and key-rotation policy.
      TS-20 mentions JWT signing but none of this. Recommend placing at
      `06-security-and-privacy.adoc` (new "Key management" subsection).

- [ ] `src/020/__TODO__/_400-encoding.md:3-5` and
      `src/020/__TODO__/_todo/encoding.md:1` — Encoding/serialization as a
      distinct network concern: unlike local calls, network requests must
      encode all parameters into bytes, and the choice of encoding format
      becomes significant for larger payloads or heavy traffic. TS-20's
      performance section (`03-performance-optimization.adoc`) covers
      compression and payload size but not encoding-format selection.
      Recommend placing at `03-performance-optimization.adoc` (new
      "Encoding" subsection) or a new dedicated file.

- [ ] `src/020/__TODO__/_todo/0100-introduction.md:5` — Process guidance:
      sometimes the client/server API should be designed first, sometimes
      the client UI should be designed first and the API shaped to make that
      UI efficient. TS-20 gives no design-process guidance. Recommend placing
      at `README.adoc` (new introductory paragraph) or a new "Design process"
      section.

- [ ] `src/020/__TODO__/_todo/0100-introduction.md:3` — The standard
      arguably should define the term "web service" (a programmatic
      interface). TS-20 defines "network API" and "in-process API" but not
      "web service". Recommend placing at `README.adoc:9-17` (extend the
      definitions paragraph).

- [ ] `src/020/__TODO__/_todo/0800-hypermedia.md:3-163` — Hypermedia as a
      network-API design principle (HATEOAS): a client requests the root
      resource and receives links to all currently-available operations and
      resources, so the API is discoverable at runtime and clients need not
      be hard-coded with the API's structure. The notes develop this in
      depth, including the JSON-LD (+ Hydra), HAL, and JSON Hyper-Schema
      formats, and the trade-off that hypermedia-driven APIs are far harder
      to build but yield simpler, more decoupled systems. TS-20 does not
      address hypermedia at all. Recommend placing at
      `01-inter-service-communication-patterns.adoc` (new "Hypermedia"
      section) or a new dedicated file, since TS-20 scopes itself to network
      APIs broadly (REST, GraphQL, gRPC, WebSocket) and hypermedia is a
      cross-protocol API-design concern rather than an HTTP-only convention.

- [ ] `src/020/__TODO__/_100-general-style.md:3-5` — It is acceptable (and
      common) for an API to mix resource-based CRUD and RPC styles, since
      different operations naturally suit different styles. TS-20's
      inter-service-communication chapter
      (`01-inter-service-communication-patterns.adoc`) covers commands,
      messages, and events but never addresses resource-vs-RPC style choice
      or mixing. Recommend placing at `01-inter-service-communication-patterns.adoc`
      (new section) or `README.adoc`.

## Partial

- [ ] `src/020/__TODO__/_250-latency.md:3-7` covers network latency more
      thoroughly than `03-performance-optimization.adoc:15-24` and
      `02-abstracting-network-apis.adoc` — specifically: latency is wildly
      variable (congestion, remote overload); on timeout the client should
      close the connection to free resources AND gracefully fall back
      (default value, cached value, or queued retry). TS-20 sets a 3x
      timeout target but omits the graceful-fallback pattern and the
      variability framing.

- [ ] `src/020/__TODO__/_300-async.md:5-7` covers async remote procedures
      more thoroughly than `01-inter-service-communication-patterns.adoc:47-62`
      — specifically: async remote procedures behave very differently from
      local async functions (which return promises); async remote
      procedures should not be expected to return anything, and a client
      needing a result should hook into events exposed by the remote
      service. TS-20 discusses async RPC improving decoupling but omits this
      "don't expect a return value" guidance.

- [ ] `src/020/__TODO__/_500-versioning.md:3-7` and
      `src/020/__TODO__/_todo/versioning.md:1-3` cover version placement
      more thoroughly than `08-documentation-and-versioning.adoc:21-33` —
      specifically: the common conventions for WHERE the version goes (path
      prefix `/v1`, `/v2`; the HTTP `Accept` header; tying each API key to a
      specific version). TS-20 mandates semantic versioning and backward
      compatibility but says nothing about where the version is exposed.

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:98-122` (Basic and
      Digest auth) and `:123-191` (Bearer auth) cover HTTP authentication
      schemes more thoroughly than `06-security-and-privacy.adoc:6-17` —
      specifically: TS-20 says to "choose mechanisms appropriate to your
      transport protocol" and recommends JWT, but gives no treatment of
      Basic, Digest, or Bearer schemes, their trade-offs, or the rule that
      Basic/Bearer must only be used over HTTPS. Note: these are
      HTTP-specific schemes, so this borders on out-of-scope (TS-21); flagged
      as partial because TS-20 itself opens the door by recommending JWT for
      "stateless HTTP APIs".

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:337-628` covers JWT
      internals more thoroughly than `06-security-and-privacy.adoc:11-17` —
      specifically: the three-part structure (header/payload/signature),
      registered claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`),
      the `jti` claim as an anti-replay/idempotency key, signing algorithms
      (HS*, RS*, PS*), and the fact that JWT claims are signed but NOT
      encrypted (so no PII in the payload; use JWE if needed). TS-20
      recommends JWT and mentions scopes/lifetimes/refresh but omits all
      structural and claim-level detail.

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:804-960` covers
      CSRF/XSS and MITM threats more thoroughly than
      `06-security-and-privacy.adoc:19-30` — specifically: the three
      session-hijack vectors (MITM, CSRF/XSRF, XSS), anti-forgery tokens,
      double-submit cookies, the `SameSite` cookie policy, `HttpOnly`/`Secure`
      flags, and the recommendation to require re-authentication before
      creative/destructive actions. TS-20 mandates TLS and input
      validation/sanitization/output encoding but does not name or address
      CSRF/XSS as threat classes. (HTTP/web-leaning — flagged partial, not
      missing, because TS-20's data-protection guidance partially overlaps.)

- [ ] `src/020/__TODO__/_todo/verification.md:1-7` covers request/response
      verification more thoroughly than `06-security-and-privacy.adoc:24-28`
      — specifically: verify field NAMES (treat as case-sensitive), not just
      values; confirm all mandatory fields are present; mandatory fields
      MUST be clearly distinguished in the API documentation. TS-20 says
      "validate and sanitize all input parameters" but omits these
      field-level specifics.

- [ ] `src/020/__TODO__/_todo/0205-rpc.md:1-7` covers RPC more thoroughly
      than `01-inter-service-communication-patterns.adoc:20-62` —
      specifically: references JSON-RPC (`https://www.jsonrpc.org/`) as a
      standard for structuring JSON RPC payloads, and Slack's Web API as a
      real-world RPC-style example. TS-20 describes RPC-style communication
      generically but names no concrete RPC standards or examples.

- [ ] `src/020/__TODO__/_todo/idl.md:1-5` covers interface-definition
      languages / API documentation more thoroughly than
      `08-documentation-and-versioning.adoc:6-19` — specifically: it raises
      IDLs as a category (the OpenAPI-Specification issue, "how should REST
      services be documented"). TS-20 mentions OpenAPI by name but does not
      discuss IDLs as a general concept or the trade-offs of
      documentation-by-specification.

## Out-of-scope

- [ ] `src/020/__TODO__/_todo/http-primer.md:1-263` covers HTTP message
      structure, versions, methods, status codes, headers, URIs, persistent
      connections, and session state in detail. Flagged out-of-scope
      because TS-20's `AGENTS.md` explicitly states that HTTP-specific
      conventions (method semantics, status codes, caching headers) are
      covered by TS-21: HTTP APIs.

- [ ] `src/020/__TODO__/_todo/http-methods.md:1-79` covers HTTP method
      semantics (GET/POST/PUT/DELETE/PATCH), PUT-vs-POST idempotency, and
      CSRF tokens. Out-of-scope: HTTP method semantics → TS-21.

- [ ] `src/020/__TODO__/_todo/status-codes.md:1-5` covers HTTP status-code
      semantics (e.g. 400 vs 200 for invalid input). Out-of-scope: HTTP
      status codes → TS-21.

- [ ] `src/020/__TODO__/_todo/0400-headers.md:1-21` covers HTTP headers,
      security headers, the `X-` prefix deprecation (RFC 6648), and
      structured fields. Out-of-scope: HTTP headers → TS-21.

- [ ] `src/020/__TODO__/_todo/http-caching.md:1-24` covers HTTP caching
      (`Cache-Control`, `ETag`, `If-Modified-Since`, 304 responses).
      Out-of-scope: HTTP caching headers → TS-21 (TS-20's
      `03-performance-optimization.adoc:45-54` already defers caching
      strategy to TS-21).

- [ ] `src/020/__TODO__/_todo/http-secure-protocol.md:1-10` covers HTTPS,
      HSTS, mixed content, and strict-transport-security. Out-of-scope:
      HTTP-transport security → TS-21. (Note: TS-20 already mandates TLS 1.2+
      at `06-security-and-privacy.adoc:21-22`, so the protocol-level
      requirement is covered; the HTTP-header-level detail is not.)

- [ ] `src/020/__TODO__/_todo/urls.md:1-105` covers URL design (scheme,
      subdomains, paths, file extensions, query strings, hash fragments,
      trailing slashes, clean URLs). Out-of-scope: URL design is HTTP/web
      API convention → TS-21.

- [ ] `src/020/__TODO__/_todo/Clean URL - Wikipedia.URL` →
      `https://en.wikipedia.org/wiki/Clean_URL` covers clean/pretty URLs,
      slugs, and SEO. Out-of-scope: URL design → TS-21.

- [ ] `src/020/__TODO__/_todo/cookies.md:1-129` covers cookie management,
      cookie sizes/lifespans, third-party cookies, and the EU/UK "cookie
      law" / online-privacy consent. Out-of-scope for the cookie mechanics
      (HTTP/browser-specific → TS-21); the privacy-consent principle is
      already covered by TS-20's compliance section
      (`10-compliance-and-governance.adoc:7-16`).

- [ ] `src/020/__TODO__/_todo/0200-rest.md:3-18` covers REST architectural
      constraints (resources, unique identifiers, statelessness, linking).
      Out-of-scope: REST is an HTTP-application architectural style → TS-21.

- [ ] `src/020/__TODO__/_todo/0220-soap.md:1` and
      `src/020/__TODO__/_todo/0210-graph.md:1` are stubs for SOAP and
      GraphQL/SOAP sections. Out-of-scope as written (no content), but note
      that TS-20's `README.adoc:5-7` names REST, GraphQL, gRPC, and WebSocket
      as in-scope protocols without further treatment — the user may want to
      add brief protocol overviews.

- [ ] `src/020/__TODO__/_todo/GENERAL-NOTES.md:1-142` is a large collection
      of external reference links on REST, HTTP status codes (401/403,
      400/422), caching, versioning, deprecation, error codes, and general
      API design. Mostly out-of-scope (HTTP/REST-specific → TS-21); the
      substantive non-HTTP points (deprecation policy, error catalogs,
      general API design) are already covered by TS-20's documentation,
      versioning, and reliability chapters.

- [ ] `src/020/__TODO__/_todo/linkbacks.md:1-30` covers Pingback, Trackback,
      Refback, and Webmention. Out-of-scope: the file itself notes this
      content "might be more appropriate for the Crafting Websites book";
      these are web-publishing standards, not network-API concerns.

- [ ] `src/020/__TODO__/_todo/0500-authentication.md:1053-1056` covers
      non-auth uses of JWTs (one-time passwords, password-reset flows).
      Out-of-scope: these are application-feature patterns, not network-API
      design guidance.

## Unresolved

- None. All reference files were read successfully (the `__TODO__` directory
  is gitignored, so its `_todo/` subdirectory was read via `cat` rather than
  the project file tools). The `Clean URL - Wikipedia.URL` shortcut was
  fetched successfully. Two stub files (`0215-odata.md`, `0230-websockets.md`,
  `0250-binary.md`, `encoding.md`) were empty and contributed no claims;
  `0210-graph.md`, `0220-soap.md`, and `9999-references.md` contained only
  section headers.