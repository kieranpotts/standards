# TS-23: Messages and Events

This is a compact version of technical standard TS-23 for AI agents.

Use this when designing or implementing messages and events in message-driven
architectures (MDA) — message systems, message schema, authentication, delivery
and reliability, and documentation. The focus is asynchronous communication
between services within a single organization's internal network
(intra-organization communication).

Do NOT use this for webhooks (event-oriented messages exchanged via HTTP between
systems owned by different organizations) — see
[TS-22: Webhooks](../022/AGENTS.md). Intra-organization and inter-organization
messages serve different purposes with different constraints, but there is
overlap and some aspects cross over. For HTTP API design see
[TS-21: HTTP APIs](../021/AGENTS.md); for versioning see
[TS-11: Versioning](../011/AGENTS.md); for date-time formats see
[TS-47: Dates and Times](../047/AGENTS.md).

## Rules

### Message systems

- **Common architectural patterns for internal message-driven communication:
  message broker, event bus, publish-subscribe, request-reply, and RPC.**

  - **Message broker** (RabbitMQ, ActiveMQ, Kafka): central broker routes
    messages between producers and consumers.
  - **Event bus** (Redis, NATS, internal event buses): lightweight distribution
    to multiple subscribers.
  - **Publish-subscribe** (MQTT, AMQP, Kafka, Redis): one-to-many distribution
    to topics with multiple subscribers.
  - **Request-reply**: synchronous-style over async transport — a request is
    sent and a reply is expected (supported by most message queues).
  - **RPC** (gRPC, Apache Thrift): synchronous service-to-service calls;
    commonly runs alongside queues/streams; suitable for time-sensitive queries
    and commands where low latency and immediate responses are required.

- **Select transport by latency-vs-throughput, delivery guarantees, message
  ordering, scalability, and complexity.**

  Low-latency protocols (gRPC, NATS) suit real-time; Kafka suits high-throughput.
  AMQP and Kafka offer strong delivery guarantees; MQTT offers QoS levels trading
  reliability for performance. Kafka's partitioning supports ordered delivery;
  AMQP queues also provide ordering. Kafka is designed for massive scale;
  RabbitMQ/NATS for moderate scale. Kafka/AMQP are feature-rich but complex;
  MQTT/NATS focus on simplicity. The common modern convention: message brokers
  (RabbitMQ/AMQP) for traditional messaging, event streaming platforms (Kafka)
  for event-driven architectures, gRPC for synchronous service-to-service where
  lowest latency is required.

- **Open message queue protocols: AMQP, MQTT, STOMP.**

  - **AMQP** (Advanced Message Queuing Protocol): binary, over TCP; widely
    supported (RabbitMQ, ActiveMQ, Azure Service Bus); complex routing,
    transactions, delivery guarantees. Best for enterprise messaging requiring
    reliable delivery and complex workflows.
  - **MQTT** (Message Queuing Telemetry Transport): lightweight, over TCP (also
    WebSockets for browser clients); pub-sub with QoS levels; designed for
    resource-constrained environments (low-bandwidth, high-latency); widely used
    in IoT (Mosquitto, HiveMQ, AWS IoT Core).
  - **STOMP** (Simple Text Oriented Messaging Protocol): text-based, over TCP;
    simpler than AMQP, easy to implement/debug; popular in simple messaging via
    scripting languages.

- **Proprietary messaging systems: Apache Kafka, NATS, Redis Pub/Sub and
  Streams.**

  - **Kafka**: distributed streaming platform, own binary protocol; high-
    throughput, low-latency event streaming. Best for event sourcing, log
    aggregation, real-time data pipelines.
  - **NATS**: lightweight, own protocol; simplicity and speed focused on simple
    pub-sub. Popular in microservices and cloud-native applications.
  - **Redis Pub/Sub and Streams**: in-memory data store with simple pub-sub and
    optional persistence (RESP protocol). Best for fast, simple messaging and
    caching integration.

- **Platform-specific managed messaging services MAY be appropriate if you're
  already on that cloud provider.**

  Amazon SQS/SNS (AWS, over HTTP), Azure Service Bus (AMQP/HTTP/proprietary),
  Google Cloud Pub/Sub (HTTP or gRPC).

- **RPC frameworks: gRPC and Apache Thrift.**

  - **gRPC**: high-performance, developed by Google; HTTP/2 transport, Protocol
    Buffers serialization; bi-directional streaming; well-suited for
    microservices, polyglot environments, low-latency APIs.
  - **Apache Thrift**: developed by Facebook; multiple transports (TCP, HTTP) and
    serialization formats (JSON, binary); best for multi-language service
    integration.

### HTTP APIs for internal messaging

- **Internal HTTP APIs can be a good choice for simple integrations where
  real-time responses aren't critical and specialist messaging framework
  overhead isn't justified.**

  Conventional HTTP endpoints support synchronous polling; push notifications
  can be implemented via webhooks (HTTP callbacks), Server-Sent Events (SSE), or
  WebSockets for true asynchronous messaging. DIY HTTP-based messaging typically
  uses HTTPS for transport and JSON for data interchange, with full freedom to
  design proprietary conventions. Industry conventions (Standard Webhooks,
  CloudEvents) can provide guidance. Aspects of [TS-21](../021/AGENTS.md) and
  [TS-22](../022/AGENTS.md) are relevant; this section is extended guidance
  specific to HTTP messaging within _internal networks_.

- **Internal networks are NOT inherently secure; HTTPS is REQUIRED to encrypt
  messages in transit, protecting against eavesdropping and
  man-in-the-middle attacks.**

- **JSON is the RECOMMENDED data interchange format (widespread adoption, human
  readability, compatibility with all mainstream languages).**

  Other formats (XML, Protocol Buffers) MAY be used where their features are
  desired, but JSON SHOULD be the default for asynchronous communication between
  most services.

### Message schema

- **Design a robust, flexible, scalable, maintainable message schema; all
  asynchronous communication SHOULD use a consistent, versioned JSON schema, and
  ideally synchronous service-to-service communication should use the same
  schema.**

  Standardization across an entire system reduces complexity, encourages code
  reuse via shared libraries, and improves interoperability. RECOMMENDED to model
  all message types with a unified, extensible schema.

- **Three categories of messages: events, commands, and queries.**

  - **Events** represent things that have happened in the emitting service (eg.
    `user.created`, `order.placed`).
  - **Commands** represent requests for operations to be performed by other
    services (eg. `sendEmail`, `refundOrder`).
  - **Queries** are requests for data (eg. `getUserDetails`, `listOrders`) —
    a sub-type of commands that are read-only and not expected to change state.

  Commands and queries typically spawn one or more new events informing other
  components of the results. A cascade of events may be triggered by a single
  initial command or query. Producers of queries will typically also be consumers
  of subsequent events returning the requested data asynchronously. A good
  schema accommodates all three types consistently.

- **Two parts to a message schema: the payload and the metadata container;
  SHOULD be clearly differentiated.**

  RECOMMENDED high-level design: place the payload inside a `data` field, with
  metadata fields at the top level:

  ```json
  {
    "spec_version": "string",
    "message_id": "string",
    "created_at": "string",
    "type": "string",
    "name": "string",
    "data": { "field1": "<value>", "field2": "<value>" }
  }
  ```

  An alternative places metadata in HTTP headers, leaving only the payload in the
  body (better separation of concerns, easier routing access) but makes the
  payload less portable (tied to HTTP, harder to reuse across transport
  protocols). Messages SHOULD be designed to be transport-agnostic to maximize
  reusability — RECOMMENDED to include all message data within a single JSON
  object in the body rather than relying on transport-specific features like HTTP
  headers. Consumers SHOULD validate incoming messages against a schema.

- **Metadata fields capture essential information for tracking and processing;
  MUST be chosen carefully to accommodate changing requirements.**

  Besides the recommended fields (`spec_version`, `message_id`, `created_at`,
  `type`, `name`), other metadata fields MAY be included (eg. `source`,
  `correlation_id` for tracing).

- **`spec_version` indicates the message schema version; consumers use it to
  differentiate processing.**

  Transitions to new schema versions SHOULD be incremental: producers emit
  duplicate messages in both old and new versions for a period while consumers
  are migrated, allowing breaking changes if required — but better to evolve
  non-breaking wherever possible. Schema versioning SHOULD follow semantic
  versioning ([TS-11](../011/AGENTS.md)) and SHOULD evolve separately from the
  service's public API (independent of API versioning — see
  [TS-21](../021/AGENTS.md)).

- **`message_id` is an idempotency key; SHOULD be a UUID.**

  Allows consumers to safely process duplicate messages and supports retries and
  other reliability mechanisms. Producers MUST generate a unique `message_id` for
  each message.

- **`type` (event/command/query) and `name` (specific event/command/query name)
  together form a message type identifier.**

  Events, commands, and queries MAY have different naming conventions (events:
  dot-noted like `user.created`; commands/queries: camelCase like `sendEmail`).
  All possible names form a _message catalog_ documenting all events, commands,
  and queries the system communicates internally. Prefer a large catalog of
  granular message types aligned to specific use cases — but don't fragment
  unnecessarily such that subscribers must reconstruct discrete state changes
  from multiple disparate messages.

- **`created_at` captures the original creation time; MUST NOT change on retry
  or redelivery.**

  SHOULD be RFC 3339/ISO 8601 format in UTC ([TS-47](../047/AGENTS.md)). Allows
  consumers to understand timing and avoid processing out of order (delivery
  order is not guaranteed). If processing must not skip messages, RECOMMENDED to
  include a `sequence` field in metadata (an integer incrementing by one per
  message in a sequence) so consumers can detect and handle gaps. Can also be
  used by consumers to protect against replay attacks (see Authentication).

- **`data` contains the payload; structure is specific to each `type`+`name`;
  payloads MUST be composed from a global library of common data types.**

  If multiple events include user information, they SHOULD all use the same
  `User` data structure. Keep payloads small (under 1MB) and focused on essential
  data; consider opening API endpoints from which consumers can fetch additional
  information if needed.

### Authentication

- **Use message-level authentication to verify authenticity and integrity;
  transport-level TLS/HTTPS is not sufficient on its own.**

  Messages may be intercepted and modified by malicious actors within the
  internal network. The most common pattern is HMAC with SHA-256 (symmetric).
  Other options: asymmetric signatures (public/private key pairs), bearer token
  (JWT — good for encoding claims and scopes). Basic auth is not recommended
  (depends entirely on transport encryption). OAuth and mutual TLS are generally
  not appropriate for internal messaging (complexity and operational overhead).
  See [TS-22: Webhooks](../022/AGENTS.md) for an overview of all options and
  their trade-offs.

- **HMAC signatures with SHA-256 hashing is the default RECOMMENDED
  authentication mechanism.**

  A scheme similar to that described in TS-22, based on
  [Standard Webhooks](https://www.standardwebhooks.com/), is RECOMMENDED to
  protect messages from tampering and reduce susceptibility to replay attacks
  and other threats. Signatures SHOULD be base64-encoded for compactness in
  transit.

- **IP allow-listing MUST NOT be depended upon for authentication, but MAY be
  used in addition to authentication as an extra layer of security.**

### Delivery and reliability

- **Message delivery and correct sequencing can never be guaranteed; messages
  may be dropped or delayed.**

  The following guidelines are protocol-agnostic and apply to all message
  delivery systems (brokers, event buses, pub-sub, HTTP-based). See also
  [TS-22: Webhooks](../022/AGENTS.md), which retreads some of this ground.

- **Messages SHOULD be designed to be idempotent.**

  The same message can be resent multiple times without unintended side effects —
  crucial for safely processing duplicates from retries or network issues.
  Producers MUST generate a unique `message_id` (UUID RECOMMENDED) for each
  message; consumers can log it and recognize duplicates.

- **Message delivery systems MUST implement reasonable timeout values (typically
  10–30 seconds); after timeout, delivery is marked failed and enters retry.**

- **Implement retry logic with exponential backoff plus jitter; producers MUST
  implement sensible defaults and consumers SHOULD be able to configure
  intervals.**

  Common pattern: immediate retry, then 1min, 5min, 30min, 2hrs, 8hrs before
  giving up. Adjust intervals by message time-sensitivity. Adding random jitter
  prevents "retry storms" / "thunder herd" problems where synchronized retries
  across multiple clients overwhelm a recovering service. Consumers SHOULD be
  able to override default retry intervals. Consumers MUST be able to retrieve
  "dead letters" (messages that couldn't be delivered after multiple retries) —
  typically by requesting a replay via an API endpoint or dashboard, or by
  retrieving from a log to reconcile synchronized state.

- **Producers MUST implement circuit breakers to temporarily stop deliveries to
  consistently-failing endpoints.**

  Circuit breaker timeouts SHOULD be configurable by consumers to accommodate
  different failure-recovery characteristics.

- **Consumers MAY implement rate limiting; producers SHOULD respect the
  `Retry-After` header.**

  Rate limiting protects against DoS and manages overall load. Consumers MAY use
  the `Retry-After` header to inform producers when they're being rate limited and
  when to resume; producers SHOULD use this to customize retry intervals for
  that consumer.

- **Producers SHOULD design events to be stateless (self-contained) where
  possible.**

  Each message includes all information needed for processing, without relying
  on external state or context — especially beneficial when processing doesn't
  depend on prior events (whose delivery can't be guaranteed). RECOMMENDED to
  avoid `sequence` fields in event metadata and not require consumers to
  reconstruct state from the full sequence in order without gaps. An alternative:
  transmit no state at all — events are just notifications that something
  changed, and consumers synchronize by making regular API requests. "Thin"
  payloads tend to be beneficial in webhooks/public APIs; "fat" payloads tend to
  be more appropriate for internal messaging. The right balance depends on the
  use case.

- **Retries, timeouts, rate limiting, and other delivery policies MUST be
  clearly defined in service level agreements (SLAs).**

- **When messages are delivered over HTTP, the consumer MUST return an HTTP
  status code that indicates whether the message was received and processed
  successfully.**

  - `200 OK` — received and processed successfully; producer SHOULD NOT retry.
  - `202 Accepted` — received and queued for processing; RECOMMENDED for
    asynchronous processing; producer SHOULD NOT retry.
  - `4xx` — rejected due to a problem with the message itself (malformed
    payload, schema validation failure, authentication failure); producer
    SHOULD NOT retry; consumer SHOULD include a descriptive error message.
  - `5xx` — consumer error while processing; producer SHOULD retry following
    the retry logic above.

  A `2xx` response acknowledges receipt; it does not guarantee processing
  completed. For at-least-once delivery, the producer MUST treat any
  non-`2xx` response as a failure and retry.

### Documentation

- **Message publishers MUST provide comprehensive documentation, including a
  full message catalog of all events, commands, and queries emitted by each
  service.**

  Large catalogs SHOULD be easily searchable.
  [Event Catalog](https://www.eventcatalog.dev/) is an open-source tool for
  creating and maintaining message catalogs. Message schemas MAY be documented
  using [JSON Schema](https://json-schema.org/). Interface description languages
  (IDLs) like [AsyncAPI](https://www.asyncapi.com/en) and
  [OpenAPI](https://www.openapis.org/) tend to be more appropriate for public
  APIs and webhooks.

## References

- [TS-23 source](README.adoc)
- [TS-11: Versioning](../011/AGENTS.md)
- [TS-21: HTTP APIs](../021/AGENTS.md)
- [TS-22: Webhooks](../022/AGENTS.md)
- [TS-47: Dates and Times](../047/AGENTS.md)
- [Standard Webhooks](https://www.standardwebhooks.com/)
- [CloudEvents](https://cloudevents.io/)
- [Event Catalog](https://www.eventcatalog.dev/)