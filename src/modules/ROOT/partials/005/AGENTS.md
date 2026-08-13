# TS-5: Application Architecture

This is a compact version of technical standard TS-5 for AI agents.

Use this when designing or reviewing the architecture of standalone software
applications — executables, libraries, services, or microservices that are
deployed in a single operation and usually maintained in a single repository.

Do NOT use this for client-side web GUI architecture — use
[TS-18: Web GUIs](../018/AGENTS.md) for that. For general software design
qualities see [TS-2: Software Design Qualities](../002/AGENTS.md); for low-level
code design see [TS-7: Code Design](../007/AGENTS.md). Distributed data and
caching concerns are covered by [TS-46](../046/AGENTS.md).

## Rules

- **Adopt a layered architecture.**

  Applications SHOULD organize code into conceptual layers that each represent
  distinct concerns. This standard RECOMMENDS a five-layer model (layer names
  map to Evans's domain-driven design layers):

  - **I/O** (≡ UI/presentation): captures input and returns responses. Parses
    incoming messages, validates input, and maps requests to commands, event
    handlers, or services in the kernel. May support multiple protocols (HTTP,
    WebSockets, gRPC, message queues) and interfaces (CLI + GUI).
  - **Kernel** (≡ application): the core of the application. All input to, and
    all output from, the application MUST pass through this layer. Thin and
    mediating — coordinates I/O handlers with domain services/objects. May hold
    UI/task-progress state but MUST NOT hold domain-model state.
  - **Model** (≡ domain/model): the business domain modeled as interconnected
    objects using OOP constructs. Captures business rules and manages business
    state (persistence of state is delegated to the system layer). Models are
    domain models, not data models (eg. ORM-generated).
  - **System** (≡ infrastructure): abstractions for the runtime platform and
    external components — databases, message queues, local and remote
    services. General technical capabilities (DB access, file system, network,
    messaging, logging, monitoring) live here.
  - **Vendors** (OPTIONAL): facades to third-party libraries, APIs, and external
    services. Application code imports facades rather than the underlying
    dependencies, easing replacement of vendor components.

- **Enforce one-way layer dependencies.**

  Components within each layer SHOULD depend only on components in the layers
  below it. All communication between the I/O layer and the deeper layers MUST
  pass through the kernel, making the kernel the central control point.

  Layers stack alphabetically (I/O, Kernel, Model, System, Vendors); if
  represented as directories, they appear in conceptual order by default:

  ```
  .
  ├── IO
  ├── Kernel
  ├── Model
  ├── System
  └── Vendors
  ```

- **Use vertical slices for modular monoliths.**

  An extension adds vertical slices through the top three layers (I/O, Kernel,
  Model), organizing application-specific code into modules. Each module has
  its own I/O, kernel, and model representing a subdomain. Modules SHOULD NOT
  call each other directly — they SHOULD communicate indirectly (ideally
  asynchronously, via messages or events) through a channel provided by the
  system layer. This reduces coupling and enables incremental extraction of
  modules into independent services.

  Filesystem layout reflects the architecture:

  ```
  .
  ├── Modules
  │   ├── <ModuleA>
  │   │   ├── IO
  │   │   ├── Kernel
  │   │   └── Model
  │   └── <ModuleB>
  │       └── ...
  ├── System
  └── Vendors
  ```

- **Make feature flags foundational.**

  Feature flags MUST be a foundational part of every application's architecture.
  They decouple deployment (engineering) from release (business), enabling
  frequent merges to `main`, continuous deployment, and strategic release
  based on business readiness. They support canary channels, staged rollouts,
  and A/B testing.

  Start simple (config file, database table, or environment variables) and
  migrate to a specialist system as needs grow. The fundamental pattern is a
  conditional check:

  ```js
  if (isFeatureEnabled("my-cool-new-feature")) {
    // New feature logic
  } else {
    // Previous behavior (or fallback)
  }
  ```

- **Minimize third-party dependencies.**

  Dependence on third-party libraries and services SHOULD be kept to a minimum.
  Each dependency adds complexity, potential security vulnerabilities, and
  maintenance overhead. Each dependency — including everything bundled with the
  application framework — MUST be carefully considered and justified: verify
  provenance, examine the dependency tree, and review code and tests before
  adding.

  Keep dependencies updated incrementally; do not let updates accumulate.
  Regularly audit for security vulnerabilities using automated tools. Runtime
  dependencies warrant the most scrutiny, but build/test tooling also increases
  the supply-chain attack surface.

- **Implement vendor facades.**

  Applications SHOULD implement facades for all vendor dependencies, located in
  the vendors layer. Interfaces are specified by the application, not by the
  framework. If a third-party library changes or must be replaced, only the
  facade requires updating. Ideally even framework components (mailers, queue
  workers, logging, cache managers, HTTP request objects) are surfaced through
  application-defined interfaces with adapters translating the framework's
  representation. GUI frameworks like React are inherently invasive and full
  decoupling is often impractical there.

- **Treat application frameworks as destinations, not starting points.**

  Align application architecture with the patterns the framework enforces (eg.
  MVC for an MVC framework). Choose a framework based on application
  requirements, not feature count or popularity; prefer proven stability and
  longevity. Choose a framework because it closely matches the design you would
  arrive at independently — not to impose constraints from outside. Do not fit
  an application into an ill-fitting framework; a simpler, less opinionated
  framework (or none) may serve better.

- **Fail gracefully when dependencies are unavailable.**

  Applications MUST fail gracefully when external dependencies are unavailable
  or performing unacceptably (eg. high latency). Detect failure and adapt —
  disable features temporarily, fall back to simpler algorithms, queue
  messages locally, or serve stale cache data. Define minimal viable behavior
  for each critical dependency and implement fallback logic. Set reasonable
  timeouts. Log failures. Test failure scenarios regularly — do not assume
  graceful-degradation code works if it has never run.

- **Adopt service-oriented architecture where appropriate.**

  Services are self-contained applications that each encapsulate the code and
  data for a complete business function, communicating through well-defined
  interfaces. Services MUST transform domain concepts at bounded-context
  boundaries — the interface/protocol between services is its own distinct
  bounded context, and translation layers are needed where contexts meet.

- **Do not decompose into services prematurely.**

  Keep tightly coupled or volatile components together — ideally in the same
  codebase sharing the same deployment pipeline — until service APIs are stable
  and well-understood. The modular monolith is a natural stepping stone:
  modules with clear boundaries and indirect communication, extracted into
  independent services once interfaces stabilize. Premature decomposition locks
  in unstable interfaces and introduces distributed-systems problems before
  domain boundaries are validated.

  Microservices' defining characteristic is independent deployability. The
  challenge lies in the interfaces between services, which must be defined
  up-front and kept stable and non-breaking over the long term.

- **Model services as state machines (reactive systems).**

  Events produce changes in state, and that is all; service state is the
  cumulative result of every event processed, enabling replay for restoration,
  diagnosis, and reproduction. Reliable, durable messaging infrastructure is
  the primary failure point. Three constraints MUST hold:

  - **Ordering**: message order MUST be preserved; the system MUST also handle
    lost messages.
  - **Determinism**: service state can be mutated ONLY via messages — no
    backdoors that bypass the message stream.
  - **Durability**: messaging infrastructure MUST be highly available; its
    failure stalls the system.

  Reactive design decouples services in time and space and pairs naturally with
  microservices (each maintains its own unshared state, typically its own
  database).

- **Use CQRS to separate reads from writes.**

  Command-Query Responsibility Segregation separates the part of the system that
  handles commands (writes/mutations) from the part that handles queries
  (reads). Commands produce events that mutate state; queries read from
  optimized projections. Read and write sides MAY be scaled, optimized, and
  evolved independently.

## References

- [TS-5 source](../../pages/005.adoc)
- [TS-2: Software Design Qualities](../002/AGENTS.md)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-18: Web GUIs](../018/AGENTS.md)
- [TS-46: Distributed Data and Caching](../046/AGENTS.md)
