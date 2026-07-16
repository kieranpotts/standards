# TS-20: Network APIs

This is a compact version of technical standard TS-20 for AI agents.

Use this when designing or reviewing network APIs of any kind — REST, GraphQL,
gRPC, WebSocket, etc. — and when implementing abstractions for network APIs in
application code. Covers inter-service communication patterns, performance,
reliability, scalability, security, observability, documentation/versioning,
testing, and compliance. Emphasis on security, reliability, and especially
performance optimization.

Do NOT use this for HTTP-specific API conventions (status codes, caching
headers, method semantics) — those are covered by
[TS-21: HTTP APIs](../021/AGENTS.md). Network APIs are distinct from in-process
APIs (library/module interfaces called directly within the same process —
synchronous, failures immediate). Network APIs introduce latency, potential
failures, and security concerns that MUST be explicitly handled.

## Rules

### Inter-service communication patterns

- **Three ways to implement inter-service communication: commands, messages,
  events.**

  Each trades off coupling and decoupling. Command-driven systems are tightly
  coupled but simple; event-driven systems achieve the greatest decoupling at
  the cost of added complexity. Most distributed systems use a mix of all three:
  commands for synchronous request-response (especially at system boundaries),
  events for asynchronous fire-and-forget. Communication from the outside world
  tends to be RPC-style; gateway services typically make blocking RPC-style
  requests to core services.

- **RPC-style: direct, synchronous calls. Appropriate for request-response
  where the caller needs an immediate answer; use judiciously.**

  Familiar (mirrors function calls), simple, explicit control flow. Creates
  tight coupling — the caller depends on the called service's availability,
  failures propagate directly, network latency is exposed, and blocking holds
  resources while waiting. Reserve primarily for gateway-to-service boundaries
  and where coupling is acceptable. RPC can also be asynchronous (caller doesn't
  wait) — improves decoupling but introduces retry/timeout/error-handling
  complexity in the caller. Better: redirect asynchronous requests through a
  message broker, which takes responsibility for reliable delivery, retries, and
  error handling (the essence of message-driven communication).

- **Message-driven: asynchronous, indirect, via a central message broker.**

  Similar intent to RPC (one service instructs another to perform an action) but
  asynchronous and indirect. Decouples direct dependencies — the target can be
  temporarily unavailable without immediately failing the caller; the message is
  persisted and the broker retries until successful (improves resilience over
  synchronous RPC). Inherently asynchronous (better resource utilization and
  throughput). However, message-driven communication remains fundamentally
  imperative — one service commands another; services remain semantically
  coupled even if decoupled in location and availability. Sits between RPC and
  event-driven on the coupling spectrum. Prefer event-driven patterns where
  possible for the ultimate decoupling and flexibility.

- **Event-driven: services tell other parts of the system about things that
  have happened; listeners may or may not be listening, and may act or ignore.**

  The publisher does not expect responses. The fundamental pattern used in all
  modern GUI systems and JavaScript event loops; scales to distributed systems
  via messaging infrastructure. Event broadcasts are self-contained, atomic
  messages; routing and lifecycle management are delegated to dedicated
  infrastructure (event bus, message broker) which handles scaling, resilience,
  and persistence — leaving application code free to specialize in the problem
  domain. The sign of a well-designed distributed system is when all accidental
  complexity moves to infrastructure, leaving service code focused purely on
  domain modeling. The messaging system also provides a centralized place to
  monitor inter-service communication, inject observability, and implement
  cross-cutting concerns. Event objects SHOULD model real-world processes and
  carry business meaning (orders placed, subscriptions cancelled) — be wary of
  too many technical or tactical events. Event-driven architecture lets systems
  grow in unforeseen ways (add a new service listening to "order" events
  without modifying existing services), isolating change and allowing
  incremental growth.

### Abstracting network APIs in application code

- **Network APIs SHOULD NOT be overly abstracted such that the network is
  hidden from application developers.**

  Abstracting network calls behind "in-memory" object calls leads to the false
  assumption that network calls are instantaneous (the "latency is zero"
  fallacy). Over-abstraction causes a lack of awareness about underlying network
  operations, their latencies, and failure modes — leading to application logic
  that doesn't account for latency, wastes bandwidth with unbounded payloads, or
  doesn't gracefully handle network failures. Distributed systems require
  patterns such as timeouts, retries, and fallbacks; for fault tolerance and
  robustness, design application code to reflect the underlying network
  operations and their potential latencies, even if this means more verbose
  code. Aim for **network transparency** — network operations explicit and
  visible in the codebase.

### Performance optimization

- **Performance targets SHOULD be based on the nature of the operation.**

  - **Critical operations**: response times of 200ms or less.
  - **Standard operations**: 500ms or less.
  - **Complex operations**: 2000ms or less.
  - **Client timeouts**: set to 3x the target response time.
  - **Payload sizes**: general APIs SHOULD stay within 10MB; file upload
    endpoints can accommodate up to 100MB.

- **Optimize payloads through a multi-faceted approach.**

  Implement pagination for collections exceeding 100 items by default (avoid
  overwhelming clients with large responses). Enable gzip or brotli compression
  for payloads larger than 1KB. For large datasets and real-time data, use
  streaming with chunked responses rather than monolithic payloads. Support
  field filtering (eg. `?fields=id,name,email`) to prevent over-fetching.
  Provide batch endpoints to fetch multiple resources in a single request
  (reduces under-fetching and round trips). Support partial updates using HTTP
  PATCH operations or equivalent mechanisms.

- **Implement caching on both sides: upstream (server-side) for backend
  performance, downstream (client-side) for reduced network traffic.**

  Pay careful attention to cache invalidation and purging strategies so stale
  data doesn't cause problems. See [TS-21: HTTP APIs](../021/AGENTS.md) for
  caching strategies. Other techniques: CDNs for static assets, load balancing
  across multiple servers, bandwidth-efficient data formats, connection
  pooling, asynchronous processing, and offloading routing/security to an API
  gateway.

### Reliability and resilience

- **Error responses MUST be standardized across all network APIs.**

  Include actionable error messages with enough context for clients to
  understand what went wrong, paired with documented error codes that can be
  reliably parsed. Use consistent response status codes throughout the API. For
  HTTP APIs, this typically means 200, 400, 401, 403, 404, 429, 500, and 503
  with clear semantics for each. In batch operations where some requests succeed
  and others fail, report partial successes so clients understand which
  operations succeeded and which need retrying.

- **Apply rate limiting at the appropriate level (per client, per endpoint, or
  per resource).**

  Include rate-limit information in response headers so clients can see how close
  they are to limits and adjust. Clients SHOULD implement exponential backoff
  for retry logic when hitting rate limits or transient failures. Distinguish
  between rate limits (temporary restrictions to protect the API) and usage
  quotas (permanent restrictions on what a customer is allowed to do) — they
  have different semantics and SHOULD be communicated differently.

- **Implement circuit breakers to prevent cascading failures when downstream
  services become unhealthy.**

  Monitor downstream services (latency, error rates, other health metrics) and
  automatically adjust upstream behavior. Track open, closed, and half-open
  states for each downstream dependency: an open circuit rejects requests
  immediately, a closed circuit passes them through, and a half-open state
  allows a limited number of test requests to determine if the service has
  recovered. Provide fallback mechanisms that degrade functionality gracefully
  when dependencies are unavailable, rather than failing completely. Test
  service recovery in an automated way so you know the system can actually
  recover when a problem is fixed.

### Scalability

- **Three dimensions of scaling: distributing load across existing servers,
  scaling horizontally by adding more servers, and auto-scaling in response to
  demand.**

- **Load distribution: choose algorithms appropriate to the workload.**

  Common options: round-robin (even distribution), least-connections (varying
  request durations), weighted (heterogeneous server capabilities). Implement
  both active health monitoring (explicitly checking server health) and passive
  monitoring (observing request failures). Handle stateful operations
  carefully — some applications require session persistence so requests from a
  single client route to the same server. Route requests to the nearest
  available servers to minimize latency for geographically distributed users.

- **Horizontal scaling: prefer stateless API designs; start with read replicas
  and connection pooling for databases before sharding.**

  If all state is external (databases, caches), scaling is simply a matter of
  adding more servers. For databases, begin with read replicas and connection
  pooling before attempting more complex sharding strategies. Isolate
  resources between services to prevent resource contention (a resource leak
  in one service shouldn't affect others).

- **Auto-scaling: metrics-based, triggering when CPU, memory, or request
  metrics cross thresholds; ensure scaling is gradual and graceful.**

  More sophisticated approaches use predictive or proactive scaling based on
  historical patterns to anticipate demand spikes before they occur. Balance
  performance improvements against resource costs throughout all scaling
  decisions.

### Security and privacy

- **Security MUST be built into network APIs from the start.**

  Addresses both authentication and data protection.

- **Authentication and authorization: choose mechanisms appropriate to the
  transport protocol.**

  For stateless HTTP APIs, token-based authentication using JWT is RECOMMENDED.
  Use fine-grained permission models based on **scopes** rather than broad
  roles — scopes allow precise control over what clients can do. Set
  appropriate token lifetimes with expiration dates so compromised tokens have
  limited utility. Implement refresh mechanisms that allow clients to renew
  tokens using a secure process, typically involving a separate refresh token
  that can only be used to obtain new access tokens.

- **Data protection: encrypt all data in transit using TLS 1.2 or higher — no
  exceptions.**

  Validate and sanitize all input parameters to prevent clients from
  submitting malicious data. Prevent injection attacks through proper output
  encoding (so data cannot be interpreted as code). Log security-relevant
  events and access patterns to create an audit trail that can help detect
  compromises and troubleshoot security incidents.

### Logging and monitoring (observability)

- **Collect the "golden signals": latency, traffic, errors, and saturation.**

  Beyond these foundational metrics, collect business metrics (API usage,
  feature adoption, user behavior) to understand how the API is actually used.
  Monitor server resources and network performance to understand changing
  infrastructure requirements. Implement custom, domain-specific performance
  indicators meaningful for your business.

- **Logs MUST be highly structured (JSON RECOMMENDED) with a documented schema,
  validated for consistency.**

  Use correlation IDs to track requests across service boundaries, making it
  possible to reconstruct complete request flows across multiple services.
  Implement appropriate log levels (debug, info, warning, error, critical) and
  adjust verbosity per environment — production logs SHOULD contain only
  essential information (and no PII) while development logs can be more verbose.
  Define and enforce log storage and rotation policies to manage disk space and
  comply with data retention requirements.

- **Alert on SLA violations and performance degradation; implement automated
  anomaly detection.**

  Define clear incident response procedures (escalation policies) so that when
  an alert fires, the right person is notified and knows what to do. Write
  runbooks to define your response plan. Provide real-time visibility into API
  health through GUI dashboards.

### Documentation and versioning

- **Provide interactive, executable API specifications (eg. OpenAPI) that
  clients can use to understand the API and generate client libraries.**

  Consider providing client code examples in multiple programming languages.
  Maintain API changelogs documenting all changes, and provide migration guides
  to help clients understand what they need to change when new versions are
  released. Maintain an error catalog documenting all possible error conditions
  and responses so clients know how to handle every failure mode.

- **Use a conventional versioning scheme (semantic versioning) and be strict
  about backward compatibility within major versions.**

  Avoid breaking changes that force all clients to update. Publish a deprecation
  policy with clear timelines for deprecating features, giving clients adequate
  time to migrate. Offer guidelines and tools to support migrations between
  major versions.

### Testing

- **Implement testing at multiple levels: unit, integration, and system
  (end-to-end endpoint verification).**

  Add load testing (validates performance under expected traffic) and security
  testing (checks for common vulnerabilities and attack vectors).

- **Maintain production-like staging environments; use representative dummy data
  while protecting privacy (avoid real customer data).**

  Test deployment and rollback procedures so you know they work and can recover
  quickly if a deployment goes wrong. Test system resilience under failure
  conditions using chaos engineering techniques.

### Compliance and governance

- **APIs handling sensitive data or serving important business functions MUST
  comply with regulations and operate under clear governance.**

  Regularly review compliance with privacy regulations (GDPR, CCPA). Define
  and enforce data retention policies so you don't keep data longer than
  necessary. Classify data by sensitivity and apply appropriate controls (highly
  sensitive data needs more protection than public data). Use access controls
  to implement the principle of least privilege — each service gets only the
  permissions it needs.

- **Establish API design review processes so new APIs meet your standards
  before release; implement automated enforcement of standards and policies.**

  Define API lifecycle stages and gates so APIs progress through development,
  testing, and deprecation in an orderly way. Monitor API adoption and usage
  patterns to understand which APIs are important, identify unused APIs that can
  be deprecated, and spot emerging patterns in how APIs are being used.

## References

- [TS-20 source](README.adoc)
- [TS-21: HTTP APIs](../021/AGENTS.md)
