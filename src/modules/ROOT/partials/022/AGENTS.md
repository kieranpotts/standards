# TS-22: Webhooks

This is a compact version of technical standard TS-22 for AI agents.

Use this when designing or implementing webhooks — either as a producer (pushing
event notifications to consumer webhook endpoints) or as a consumer (implementing
webhook endpoints to receive notifications). Extends
[TS-21: HTTP APIs](../021/AGENTS.md) with webhook-specific guidance. Based on
the [Standard Webhooks](https://www.standardwebhooks.com/) specification and
fully compliant with it.

Do NOT use this for other real-time push mechanisms (WebSockets, Server Sent
Events) — outside scope. For general message-driven design principles (which
also apply to webhooks) see [TS-23: Messages and Events](../023/AGENTS.md). For
version-numbering semantics see [TS-11: Versioning](../011/AGENTS.md).

## Rules

### Definitions

- **Webhooks (web callbacks / HTTP callbacks) are a "reverse API" pattern for
  inter-organization integration: a service pushes event notifications to
  client-implemented HTTP endpoints when events occur, rather than clients
  polling.**

  Webhooks are a subset of message-driven communication — event-oriented
  messages exchanged via HTTP between systems owned by different organizations
  (inter-organization), not within a single internal network (intra-organization).
  They support near-real-time synchronization between independent systems and
  typically sit alongside regular HTTP APIs (though this is not a requirement).
  Webhooks are an asynchronous communication pattern — the webhook notification is
  a _delayed response_ to the client's original request. Webhooks _do not_
  reverse the client-server relationship conceptually (the notifying service is
  still the server), though in HTTP semantics the roles swap during delivery
  (the producer is the HTTP client, the consumer is the HTTP server). This
  standard uses "producer" (sends events) and "consumer" (receives them) to avoid
  confusion.

### Consumers

- **Consumers implement private webhook endpoints to receive event notifications;
  these are NOT part of the public interface and are not in user-facing
  documentation.**

  The main consumer design consideration is the URL scheme — often the only thing
  the consumer controls. The producer dictates payload schema and authentication.

- **Webhook URL schemes MUST be distinct from the service's own HTTP API
  endpoints (if any); the following scheme is RECOMMENDED:**

  ```
  /_webhooks/{party}/{namespace}/v{version}/{event_type}/{...}
  ```

  - `/_webhooks/` prefix (RECOMMENDED) differentiates webhook endpoints from the
    main API; the underscore prefix signals internal use and simplifies
    cross-cutting concerns (security policies, routing, monitoring, logging).
  - `{party}` (REQUIRED) — the name of the third-party event producer.
  - `{namespace}` (OPTIONAL) — scopes a webhook to a particular service of the
    producer, for producers offering multiple services with different event
    formats.
  - `{version}` (OPTIONAL) — identifies the version of the producer's webhook
    API or event schema supported by the endpoint; can be omitted if the endpoint
    handles multiple versions backward-compatibly.
  - `{event_type}` (OPTIONAL) — identifies a particular event type the endpoint
    receives; normally a single endpoint handles all events from a producer, but
    multiple endpoints MAY be useful where different event types require different
    processing. MAY be "callback" or omitted.
  - `{...}` — any additional path components required by the producer.

  This scheme supports multiple producers, event types, and schema versions,
  enabling zero-downtime transitions between service providers and incremental
  transitions to new breaking-change schemas.

- **The `{version}` URL component is independent of the consumer's own API
  versioning; it is determined by the producer's message schema version.**

  If a producer does not explicitly version their webhook payload schema,
  RECOMMENDED to scope URLs to the current major version of the producer's own
  web service API; if that's not possible, invent your own versioning (eg. "latest"
  and "next").

- **Consumers SHOULD handle webhook messages asynchronously and return success
  quickly.**

  Producers typically impose timeouts (commonly 15–30 seconds; if unspecified,
  assume 10 seconds). RECOMMENDED that webhook endpoints log messages to a queue
  for later processing and quickly return `202 Accepted`. If a producer specifies
  expected status codes, consumers MUST comply. If the producer does not specify,
  RECOMMENDED: `202 Accepted` for success; `400 Bad Request` for schema validation
  failures; `401 Unauthorized` for failed authentication; `403 Forbidden` for failed
  authorization; `404 Not Found` when the endpoint doesn't exist; `429 Too Many
  Requests` when rate limits are exceeded; `500 Internal Server Error` for
  unexpected conditions (signals "please retry later").

### Producers

Producers push event notifications to consumer webhook endpoints. These
notifications are part of the producer's API.

- **Producers SHOULD follow the [Standard Webhooks](https://www.standardwebhooks.com/)
  specification.**

  This standard specifies an extended subset of Standard Webhooks — fully
  compliant but narrowing some choices and extending guidance in other areas.

#### Secure protocol and HTTP methods

- **Webhook event messages MUST be delivered over HTTPS.**

  Digital signatures guarantee authenticity and integrity but not confidentiality;
  insecure transport risks interception and leakage of sensitive data.

- **All messages sent to consumer webhook endpoints MUST use HTTP's `POST`
  method.**

#### HTTP headers

- **Three HTTP headers are REQUIRED with every webhook message:**

  - **`Webhook-ID`**: a unique identifier for each discrete message (UUID
    RECOMMENDED). MUST remain the same for every attempted delivery of the same
    message (including retries). Consumers can use it as an idempotency key. Also
    part of the security scheme.
  - **`Webhook-Timestamp`**: Unix timestamp (integer seconds since epoch) of the
    time the message was sent from the producer's servers. MUST be updated for
    each delivery attempt.
  - **`Webhook-Signature`**: a space-delimited list of HTTP message signatures
    for verifying authenticity and integrity. A list (not a single signature) to
    support zero-downtime secret rotation.

  All three values MUST be generated by the producer and MUST NOT be configurable
  by the consumer. RECOMMENDED Title-Case header naming (`Webhook-Id`) —
  compliant with Standard Webhooks because HTTP header names are case-insensitive
  (RFC 7230 §3.2). These three headers are an exception to the `X-` prefix
  convention from TS-21 — not prefixed, to maintain Standard Webhooks compliance.

#### Payload schema

- **The payload MUST be encoded in the HTTP message body; HTTP headers MUST NOT
  transmit any part of the payload (headers are reserved for message metadata).**

  Payload SHOULD be JSON with `Content-Type: application/json` (other formats like
  XML or form-encoded MAY be used for specific requirements).

- **Payload structure: an object with `type`, `timestamp`, `data` (all REQUIRED
  for Standard Webhooks compliance) plus OPTIONAL `metadata` and `links`
  (extensions suggested by this standard).**

  ```json
  {
    "type": "user.created",
    "timestamp": "2022-11-01T09:15:00Z",
    "data": { "id": "123", "name": "John Doe", "email": "john.doe@example.com" },
    "metadata": { "created_at": "2022-11-01T09:15:00Z" },
    "links": [{ "rel": "self", "href": "https://api.example.com/users/123" }]
  }
  ```

  Producers MAY further extend the schema with additional properties.

- **Event `type` SHOULD be organized hierarchically with dot-notation
  (`user.created`, `invoice.paid`); components restricted to `[a-zA-Z0-9_]`.**

  Each event type MUST have a single consistent `data` schema. Make types granular
  enough for effective consumer filtering; map to meaningful business-relevant
  state changes likely to require differential processing. Fine-grained,
  business-relevant events tend to be most future-proof (coarse types lead to
  bloated payloads). If two or more events can be processed the same way, that's
  a design smell — they may be too fine-grained and could be merged.

- **`timestamp` is an ISO 8601 date-time string (not a Unix timestamp — the naming
  inconsistency is REQUIRED for Standard Webhooks compliance); it represents when
  the event occurred (earlier than message-send time) and MUST NOT change on
  retry.**

  Contrast with the `Webhook-Timestamp` header (a Unix timestamp that MUST change
  on every retry). Signing the timestamp lets consumers verify its integrity and
  reject messages older than a threshold, protecting against replay attacks.

- **`data` MUST be an object with at least one property (not empty); each event
  type MUST have a well-defined `data` schema.**

  Err on the side of "thin" objects communicating minimal data for state sync.
  Extreme thinness: only an identifier, with consumers fetching full state via
  the producer's HTTP API. "Full" objects include all resource fields (stateful
  design — consumers need no further API calls). Thin payloads offer better
  performance, future-proofing (you can make thin full but not vice versa without
  breaking compatibility), keep the HTTP API as source of truth (less out-of-order
  risk, simpler audit trails), and better security (fewer replay/PII-leakage
  risks). The optimum is often in the middle.

- **`metadata` is OPTIONAL (not part of Standard Webhooks); SHOULD NOT include
  data essential for processing.**

  Use for machine-generated data readable but not writable by clients (eg.
  `created_at`, `updated_at`), event IDs, source information, debugging info.
  MUST be used only for metadata about the resources in `data` and the event —
  MUST NOT be used for HTTP message metadata (that's the role of headers).

- **`links` is OPTIONAL; its value MUST be an array of objects with `rel`,
  `method`, and `href` properties (the hypermedia convention from
  [TS-21](../021/AGENTS.md)).**

  Encodes how consumers can fetch related data and perform related operations via
  the producer's regular HTTP API. Provides in-band API documentation.

- **Keep payloads smaller than 20kb (RECOMMENDED). For large data (images,
  media), make it available via `GET` endpoints and use webhook messages to
  communicate links.**

  Payloads MAY be minified (more beneficial for large payloads; if done, apply
  consistently across all messages).

#### Versioning

- **Producers SHOULD implement versioned payload schemas from the outset, even
  if breaking changes aren't foreseen.**

  Two options: a `Webhook-Version` HTTP header (RECOMMENDED where events follow
  the same versioning scheme as an adjacent HTTP API) or a `version` field in the
  payload (better where events evolve independently). Incremental versioning (1,
  2, 3) is RECOMMENDED over date-based, though date-based MAY suit volatile
  schemas. For easier multi-version maintenance, implement a transformation layer
  generating broadcast events at delivery time from a canonical internal
  representation.

- **Versions MUST be stable (per [TS-11](../011/AGENTS.md)): transition periods
  between breaking versions, deprecation windows, migration guides, changelogs.**

  Schema versions SHOULD be backwards-compatible (additive changes only within
  each major version) — easier to maintain when starting with thin, flat
  structures and adding fields as customers ask.

#### Security and authenticity

- **Consumers MUST verify the authenticity and integrity of every webhook message
  before processing it.**

  TLS provides confidentiality in transit but does not guarantee end-to-end
  message integrity (intermediaries like proxies and load balancers terminate
  and re-establish connections).

- **Authentication mechanisms, ordered simplest/least-secure → hardest/most-secure:
  IP allow-listing, HTTP basic auth, bearer token/API key, HMAC signatures
  (symmetric), public key signatures (asymmetric), OAuth 2.0, mutual TLS.**

  - **IP allow-listing**: infrastructure-level traffic filtering only; does not
    guarantee authenticity or integrity. RECOMMENDED producers support it as an
    extra layer alongside another mechanism; MUST NOT be the sole authentication
    mechanism (IPs can be spoofed).
  - **HTTP basic auth**: raw credentials transmitted; security depends entirely
    on HTTPS; message integrity not guaranteed. MAY suit single-consumer or
    internal-network scenarios.
  - **Bearer token / API key**: consumer-generated token embedded in messages
    via `Authorization`. JWTs add claims, expiration, revocation, scopes; JWS can
    sign the entire payload. Token auth is popular and familiar but signatures
    tend to be a better fit for message-driven use cases.
  - **HMAC-SHA256 (symmetric)**: producer creates an HMAC hash of message
    payloads with a shared secret; consumer recreates the hash and compares.
    Strong authenticity (no secrets transmitted), verifies integrity, timestamp
    verification protects against replay, industry standard (used by GitHub,
    Stripe, Spotify), good library support, fast, zero-downtime rotation possible.
    Trade-off: a single secret shared between parties (insider threat; secure
    distribution required; clock synchronization needed for timestamp
    verification). **RECOMMENDED default choice** for most use cases.
  - **Ed25519 (asymmetric)**: producer signs with a private key, consumer
    verifies with a public key. Strongest authenticity guarantees (no secrets
    shared; private key fully under producer control; public key freely
    distributable). Modern Ed25519 avoids side-channel attack patterns. More
    complex to implement, less library support, more CPU-intensive. RECOMMENDED
    as the sole mechanism in high-security scenarios; producers MAY offer it
    alongside HMAC-SHA256.
  - **OAuth 2.0**: producer authenticates with the consumer's auth server to
    obtain a short-lived access token per message. Complex; appropriate where
    delegated access is required (destructive actions requiring elevated
    privileges) — tends to be outside webhook scope.
  - **Mutual TLS (mTLS)**: both sides authenticate with certificates. Strongest
    guarantees (authenticity of both producer and consumer; protection against
    MITM). Highly complex; appropriate only in highest-security environments
    (financial trading, niche enterprise integrations).

- **Secret generation and lifecycle management.**

  Tokens MUST be managed by consumers. Public-private key pairs for asymmetric
  signatures MUST be generated and managed by the producer (one key per customer
  RECOMMENDED to reduce blast radius, though a single pair for all consumers is
  an option). For symmetric signatures, each consumer needs its own shared secret;
  RECOMMENDED that producers generate and manage keys by default (eases
  onboarding) but also let consumers provide their own keys for more control over
  rotation.

- **The signature scheme MUST sign all of: the message identifier (`Webhook-ID`),
  the message timestamp (`Webhook-Timestamp`), and the message payload (HTTP
  body), concatenated with dot notation: `{id}.{timestamp}.{payload}`.**

  If the JSON payload is minified for transit, the minified version MUST be used
  to generate the signature. The payload sent MUST match exactly the payload
  signed. Signing all three parts (not just the payload) is REQUIRED to protect
  against the full range of attack vectors: timestamp signing enables replay
  protection; message ID verification helps against spoofing and replay; payload
  verification protects against tampering/MITM/injection. `Webhook-ID` and
  `Webhook-Timestamp` MUST NOT contain periods (to avoid parsing problems).
  Consumers SHOULD access the raw HTTP body as a byte stream/string without
  intermediate parsing/serialization when verifying signatures (differential
  serialization causes verification failures).

- **Standard Webhooks specifies two signature systems; producers MAY implement
  one or both in parallel.**

  - **Symmetric**: HMAC-SHA256, random secret (24–64 bytes / 192–512 bits),
    base64-encoded prefixed with `whsec_`, signature version identifier `v1`.
  - **Asymmetric**: Ed25519, standard key pair, base64-encoded prefixed with
    `whsk_` (secret key) and `whpk_` (public key), signature version identifier
    `v1a`.

  Signatures are base64-encoded and prefixed with `v1,` or `v1a,` in the
  `Webhook-Signature` header. Consumers MUST use this prefix to identify
  signatures they can verify; consumers MUST remove the `whsec_`/`whsk_`/`whpk_`
  prefixes before verifying. Multiple space-delimited signatures MAY be sent for
  zero-downtime rotation. (Alternative: [RFC 9421 HTTP Message Signatures](https://datatracker.ietf.org/doc/rfc9421/)
  offers more flexibility — producers declare which message components are signed
  via `Signature-Input` — but is more complex and doesn't cover other webhook
  security aspects.)

- **Key rotation: `Webhook-Signature` MAY contain multiple space-delimited
  signatures for the same message, supporting zero-downtime secret rotation.**

  During rotation, messages are signed with both old and new keys; consumers try
  each signature until one matches. If a key is compromised, producers MUST
  immediately rotate it and stop signing new/retried messages with it. Consumers
  can still verify delayed messages signed with the old key; new messages signed
  with the new key will fail until the consumer installs the new verification
  key, but those can be retried later. This system also supports incremental
  upgrades from symmetric to asymmetric keys.

- **Other security requirements (RECOMMENDED baseline).**

  - Secure message transport over TLS/HTTPS.
  - HMAC or asymmetric signatures for primary authentication and message
    integrity.
  - Timestamp validation on the consumer side to protect against replay attacks
    (typical tolerance window: 5 minutes / 300 seconds; messages outside the
    window MUST be rejected and logged as a potential security incident).
  - Unique message IDs to support idempotency and further replay protection
    (consumers SHOULD store `Webhook-ID` values for recently processed messages;
    retention MUST be longer than the timestamp tolerance window; a message with
    a `Webhook-ID` already processed and within the tolerance window MUST be
    rejected but doesn't need to be logged as a security threat — likely just a
    duplicate).
  - Highly-automated key revocation and rotation on the producer side to limit
    blast radius.
  - Rate limiting on the consumer side to protect against DoS.
  - Logging of failed signature verification attempts on the consumer side;
    RECOMMENDED that producers provide a mechanism to report such incidents back.
  - Static IP addresses on the producer side, enabling consumer IP allow-listing.

  Signing keys MUST be unique _per endpoint_ for symmetric signatures and unique
  _per customer_ for asymmetric (MAY be unique per endpoint too). Producers MUST
  NOT reuse signing keys across customers. Producers MUST use a secure random
  number generator; symmetric key length MUST be 24–64 bytes; asymmetric MUST use
  the standard ed25519 key pair. Producers MUST implement highly-automated key
  invalidation and rotation. Shared secrets MUST be transmitted securely (eg.
  HTTPS) and MUST NOT be exposed in logs or error messages. Producers are
  REQUIRED to have accurate clocks (synchronized via NTP); consumers are also
  RECOMMENDED to synchronize clocks. When verifying symmetric signatures,
  consumers MUST use a constant-time comparison function (eg. Python's
  `hmac.compare_digest`) — regular string comparison exposes consumers to timing
  attacks.

#### Delivery and reliability

- **Producers SHOULD set a reasonable timeout (15–30 seconds) for webhook
  requests; timeouts SHOULD be handled the same way as `429 Too Many Requests`.**

  Producers MAY allow consumers to configure timeouts.

- **Webhooks are inherently unreliable; retry mechanisms are RECOMMENDED, with
  exponential back-off over multiple days.**

  Default retry schedule (producers SHOULD adjust per use case; consumers SHOULD
  be able to override):

  | Attempt | Delay | Cumulative |
  | --- | --- | --- |
  | 1 | immediate | 00:00:00 |
  | 2 | 5 seconds | 00:00:05 |
  | 3 | 5 minutes | 00:05:05 |
  | 4 | 30 minutes | 00:35:05 |
  | 5 | 2 hours | 02:35:05 |
  | 6 | 5 hours | 07:35:05 |
  | 7 | 10 hours | 17:35:05 |
  | 8 | 14 hours | 31:35:05 |
  | 9 | 20 hours | 51:35:05 |
  | 10 | 24 hours | 75:35:05 |

  Producers MAY add random jitter to spread load when consumers recover.
  Consumers MAY respond with `503 Service Unavailable` and a `Retry-After`
  header, which producers SHOULD honor. If delivery fails beyond the last retry,
  consumers SHOULD be notified via other channels (email, SMS); after the last
  retry, the consumer's endpoint SHOULD be disabled in the producer's
  configuration, and no further messages sent until the consumer requests
  re-enablement.

- **Producers MUST NOT batch-process delivery (to avoid overloading consumers).**

#### Status codes (producer-side policy)

- **The following response-code policy is RECOMMENDED for producers:**

  - Accept any `2xx` as successful processing (treat as `202 Accepted`).
  - Treat `5xx` as consumer errors triggering retry and dead-letter queues;
    `502`/`504` indicate server load, so producers SHOULD throttle subsequent
    requests.
  - Recurring `410 Gone` (persisting > 1 day) means the consumer no longer wants
    messages — automatically disable their webhook configuration and stop
    sending.
  - `404 Not Found` indicates misconfiguration or moved/deleted endpoints —
    handle like `410` but also notify the consumer.
  - `429 Too Many Requests` — pause sending, then resume through the normal retry
    mechanism; OPTIONAL to automatically adjust retry intervals based on
    `Retry-After` headers.
  - Other `4xx` client errors — treat like `5xx` but also log for investigation
    (the producer's implementation may be at fault).
  - `1xx`, `3xx`, and all other codes — treat as generic `500` server errors.
    Producers MUST NOT follow redirects (security risk and unnecessary load);
    consumers who move endpoints are REQUIRED to update their configuration.

#### Webhook management

- **Webhooks are an optional convenience alongside a regular HTTP API; consumers
  SHOULD NOT depend on webhooks alone for synchronization.**

  Consumers SHOULD be able to retrieve everything they need by polling the
  producer's API. Webhooks SHOULD be treated like a subscription service:
  consumers explicitly opt in (via HTTP API endpoints) to particular event types
  and SHOULD NOT be burdened with messages they're not interested in. Example
  management endpoints: `GET /webhook/types`, `GET /webhook/subscriptions`,
  `POST /webhook/subscriptions`, `DELETE /webhook/subscriptions/{id}`.

- **Delivery MUST be disabled by default; consumers MUST explicitly enable
  webhooks and configure event types and versions before any messages are sent.**

  For some event types (eg. security notifications), delivery alongside other
  channels (email, SMS) is RECOMMENDED. Consumers SHOULD manage configuration
  (webhook endpoint URLs, retry policies, rate limits, signature scheme, key
  rotation, event types/versions, expiration times, payload thickness) via API,
  GUI, or both. Consumers SHOULD be able to initiate retries of failed messages
  and replays of successful ones; messages SHOULD be available for replay for a
  reasonable period (eg. 30 days). Consumers SHOULD be able to read and query
  message history (including dead letters) via HTTP API and/or a GUI dashboard.
  Producers SHOULD offer monitoring and alerting for delivery problems.
  Consumers MAY define multiple webhook endpoints for fan-out distribution; where
  supported, each endpoint MUST be independently configurable.

#### Webhook endpoint verification

- **Consumers MUST NOT be able to configure arbitrary webhook endpoint URLs
  (SSRF risk).**

  URLs set to internal resources (`http://localhost`, `http://192.168.1.1`) or
  cloud metadata endpoints (`http://169.254.169.254/...`) expose producers to
  server-side request forgery. At minimum, URLs MUST be validated as public
  internet addresses on registration. Producers can further protect against SSRF
  with a proxy (eg. smokescreen) filtering internal-IP requests and by placing
  webhook workers in their own private subnet.

- **RECOMMENDED: implement a challenge-response system on URL registration.**

  A "challenge" token is sent to the endpoint, which must return a valid response
  with the token encoded somewhere — verifying reachability and TLS certificate
  validity. For best security, verify domain _ownership_ via DNS lookups (TXT
  record) or email at the same domain. Ideally, human-moderate domain names.
  Producers SHOULD implement automated health checks on consumer endpoints and
  MAY require periodic domain revalidation to protect against hijacking.

#### Documentation, integration testing, and SDKs

- **Producers SHOULD document webhook message formats and payload schema in a
  dedicated section of their regular API documentation.**

  [AsyncAPI](https://www.asyncapi.com/) is well-suited to webhooks;
  [OpenAPI](https://www.openapis.org/) (since v3.1) supports webhook payload
  schema definition (but not other aspects like signature schemes). RECOMMENDED
  to provide payload examples for each event type alongside the formal
  specification.

- **Producers MUST offer endpoints through which consumers can trigger test
  messages to verify integration.**

- **Producers MAY provide SDKs in popular languages; basic SDKs SHOULD include
  functions abstracting signature verification complexity.**

## References

- [TS-22 source](../../pages/022.adoc)
- [TS-11: Versioning](../011/AGENTS.md)
- [TS-21: HTTP APIs](../021/AGENTS.md)
- [TS-23: Messages and Events](../023/AGENTS.md)
- [Standard Webhooks](https://www.standardwebhooks.com/)
- [RFC 9421: HTTP Message Signatures](https://datatracker.ietf.org/doc/rfc9421/)
