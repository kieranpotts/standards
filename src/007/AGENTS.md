# TS-7: Code Design

This is a compact version of technical standard TS-7 for AI agents.

Use this when writing or reviewing low-level code structure and formatting —
naming, abstraction, decomposition, comments, error handling, code layout,
object-oriented design, and concurrency. Guidelines are language-agnostic,
applicable to any general-purpose high-level language (Python, Java,
JavaScript, etc.); some also apply to lower-level languages like Bash.

Do NOT use this for architecturally-significant decisions (module boundaries,
communication patterns, data structures) — those are covered by
[TS-5: Application Architecture](../005/AGENTS.md) and
[TS-2: Software Design Qualities](../002/AGENTS.md). This standard is
deliberately pragmatic: it sets out principles to balance trade-offs, not hard
rules like line-length caps.

## Rules

- **Don't bike-shed.**

  Low-level concerns (formatting, private variable names, minor abstractions)
  have small impact compared to architectural decisions, and much of code
  design is subjective. Decide conventions, codify them in linters and style
  guides, then focus on higher-level design. Code design MUST be consistent for
  codebase habitability, but SHOULD NOT consume disproportionate time.

- **Apply the boy scout rule proportionately.**

  Leave the codebase a little cleaner than you found it — rename a confusing
  variable, extract a small helper, delete dead code, improve a misleading
  comment. Improvements SHOULD be small and targeted, closely related to the
  task at hand. Resist refactoring entire modules for a small bug fix or
  rewriting functional code for aesthetic preference.

- **Abstract to hide complexity, but seek balance.**

  Abstraction hides complexity behind simplified interfaces, compresses code,
  and enables reuse. Be moderate — overuse and misuse create problems. The
  best abstractions are small, simple, and focused; deep abstractions are
  acceptable when their interfaces can be made simple and stable (eg. file I/O
  or database client libraries). Do not impose arbitrary limits (statement
  counts, method counts) on abstractions.

- **Name abstractions to express all important hidden details.**

  Names SHOULD accurately express all important details users need to
  understand. Name abstractions for the _user_, not the _implementor_; describe
  _what_ not _how_ (eg. `fetchUserData` not `process`). Generic names like
  `handle`, `process`, `data`, `utils` communicate nothing. Do not truncate or
  abbreviate names where doing so decreases expressiveness (`calculateTaxAmount`
  over `calc`). Names should be expressive in all contexts — do not rely on
  adjacent comments to document meaning. Be specific about side effects
  (`fetchAndCacheUser` over `fetchUserData` when caching is involved). Avoid
  jargon and acronyms unless universally understood. Naming conventions
  SHOULD be consistent throughout a codebase.

- **Avoid leaky abstractions and premature abstraction.**

  Deep abstractions tend to leak implementation details through their
  interfaces, which snowballs refactorings when internals change. Good
  abstractions have generic interfaces that do not leak. Extract abstractions
  only when confident the interface can be kept stable — best abstractions
  emerge piecemeal from actual usage, not speculation. Evolve interfaces only
  backwards-compatibly; where that is impossible, create a new abstraction and
  deprecate the old incrementally. Premature-abstraction risk is greatest in
  distributed systems (eg. extracting microservices too early).

- **Keep abstraction levels consistent within layers.**

  Within each architectural layer, maintain a consistent level of abstraction.
  Mixed abstraction levels (eg. one module calling high-level business services
  while another implements low-level string manipulation) are a code smell,
  worse still when present in the same module. Mixed levels indicate things
  SHOULD be extracted to new abstractions.

- **Decompose judiciously; preserve locality of reference.**

  Decomposition increases overall system complexity by creating new
  dependencies — localized simplicity at the cost of global complexity. Do
  not apply "single responsibility" so rigidly that you create many tightly
  coupled tiny abstractions. Locality of reference matters: related things
  SHOULD stay close together, unrelated things far apart. If you cannot
  understand a function without reading the internals of several others, you
  have over-decomposed. Abstraction SHOULD be a net remover of complexity — do
  not introduce abstractions purely for separating concerns when no overall
  reduction results. Do not abstract implementation details that users are
  better off knowing about.

- **Apply DRY to knowledge, not to code duplication.**

  DRY means one abstraction per distinct business rule or domain concept, so
  changes happen in one place. It does NOT mean "avoid all code duplication."
  Coincidental duplication between semantically unrelated components SHOULD NOT
  be extracted to a shared abstraction — that couples the components locally
  for minor line savings at the expense of modularity. True complexity comes
  from dependencies and indirection, not lines of code. Modern tooling makes
  duplication cheap — write everything twice (WET) before abstracting, to gain
  confidence the abstraction will be stable and valuable.

- **Write expressive code; prefer clarity over brevity.**

  Code SHOULD read like narrative. Achieve expressiveness through good
  abstraction, clear naming, and thoughtful syntax and control structures.
  Prefer high-level idioms (`collection.map()`, `for item in items:`) over
  manual index management. Use guard clauses and early returns over deeply
  nested conditionals. Prefer positive conditionals over negative ones
  (`if (isActive)` over `if (!isInactive)`); always refactor double negatives.
  Replace magic numbers and string literals with named constants
  (`if (statusCode === FORBIDDEN)` not `if (statusCode === 403)`).

- **Mix programming paradigms where it improves expressiveness.**

  Use whichever paradigm makes intent clearest: OOP for domain modeling,
  functional for data transformation pipelines, procedural for scripts. The goal
  is expressiveness, not paradigm purity.

- **Be selective with external dependencies; isolate and pin them.**

  Dependencies carry maintenance, security, supply-chain, size, and opacity
  costs. Evaluate each dependency: what problem it solves, whether you could
  build it yourself, maintenance burden, project stability, dependency-tree
  size. Make the analysis explicit and document decisions. Once adopted, wrap
  ALL external dependencies (including infrastructure: DB access, file I/O,
  remote services, external APIs) in facades. Pin specific versions in vendor
  configuration — never rely on floating version constraints. Consider
  vendoring libraries directly (no package manager) to ease auditing, force
  shallow dependency trees, guarantee build reproducibility, and enable
  automated rollback.

- **Use dependency injection.**

  Supply a component's dependencies from outside rather than constructing them
  internally. This makes dependencies explicit, eases testing (dependencies
  can be replaced with test doubles), and enables swapping implementations —
  aligning with the facade pattern. It applies the inversion-of-control
  principle: high-level and low-level modules SHOULD both depend on abstractions.

- **Keep configurable values high in the call stack.**

  Environment-specific settings, thresholds, timeouts, feature flags, and
  format strings SHOULD be kept as high in the call stack as possible — in
  configuration objects, constructor parameters, or environment variables read
  at startup. Do NOT hardcode such values into low-level implementation logic
  where they are hard to find, change, and test. The configuration surface of
  the system SHOULD be visible and easy to manage.

- **Comment what the code cannot express.**

  Reject "clean code" orthodoxy that discourages comments. Comments are
  valuable for algorithms, business rules, design rationales, and assumptions
  about black-box dependencies. Focus comments on what is not obvious from the
  code alone. Lower-level languages (shell scripts, etc.) need more comments
  because they offer fewer abstraction constructs. Annotate the rationale for
  unusual or smelly code (legacy constraints, performance hacks) to prevent
  wasted refactoring effort. Remove superfluous or redundant comments. When
  choosing between premature abstraction and well-placed comments, add the
  comments — they are cheaper and more reversible. _If in doubt: leave a
  comment!_

- **Distinguish inline comments from other documentation.**

  Use inline comments for documentation that benefits from proximity to the
  code (complex logic, business rules, assumptions) and that is likely to
  change as the code changes. Use out-of-band documentation (design docs,
  READMEs, wikis) for developer-oriented information not specific to a
  particular piece of code. Inline API documentation (Javadoc, docstrings)
  serves a different purpose from general inline comments.

- **Use a consistent TODO convention.**

  It is okay to leave TODO comments; most software is work-in-progress. It is
  RECOMMENDED that incomplete code and configuration be tagged with a
  consistent inline commenting convention so the codebase can be searched.
  Convention:

  ```
  TODO: <comment>
  [<url>]
  ```

  `<comment>` is REQUIRED (short description of the outstanding task); `<url>`
  is OPTIONAL (link to a related issue-tracker ticket).

- **Throw exceptions only for bugs and exceptional circumstances in your code.**

  Exceptions represent bugs or conditions requiring developer investigation —
  not ordinary expected failures. Exceptions are expensive (interrupt control
  flow, unwind the stack, trigger logging/monitoring). Do NOT throw exceptions
  for routine failures like network timeouts, missing resources, or invalid
  user input — these are normal operating conditions. Model such outcomes
  explicitly in return types or data structures so callers handle them as
  normal control flow. If an abstraction you use throws in non-exceptional
  cases, catch it on immediate return and handle gracefully — do not let it
  propagate up the stack.

- **Apply the robustness principle contextually.**

  Postel's Law: be liberal in what you accept, conservative in what you send.
  At system boundaries (API endpoints, user input handlers, file parsers) be
  liberal — apply reasonable normalization and coercion, do not let minor
  input irregularities escalate to exceptions. Within internal code (business
  logic, domain models, data processing) be conservative and defensive —
  enforce invariants strictly so bugs surface early and close to their source.

- **Never throw exceptions from the UI layer.**

  The UI/presentation layer is the boundary with the outside world. All error
  conditions — bugs or expected external failures — MUST be caught here,
  normalized, and converted into user-friendly messages. Throwing exceptions
  through the UI layer risks leaking sensitive internals (security concern)
  and produces poor user experience.

- **Fail gracefully.**

  When operations fail, applications SHOULD: catch errors at appropriate
  boundaries; transform technical details into meaningful, actionable user
  messages; hide internal implementation details and infrastructure
  specifics; offer recovery options (retry, alternative actions) where
  possible. Users SHOULD experience failures as understandable, recoverable
  situations, not cryptic error dumps or crashes.

- **Minimize exception types.**

  Each distinct exception type you throw is part of your module's public
  interface and forces callers to handle it. Prefer a small number of
  well-defined types that communicate what went wrong over a proliferation of
  fine-grained types mirroring internal failure modes. Better still: design
  the system to minimize special cases and edge cases by reducing conditional
  logic and normalizing data early in the pipeline.

- **Structure source files like a newspaper.**

  High-level concepts at the top, details below. Public functions and entry
  points near the top; private helpers below. When one function calls another,
  define the caller above the callee so a top-to-bottom reader encounters
  abstractions before implementations. Keep related code vertically dense
  (callers close to callees, related variables grouped); use blank lines to
  separate unrelated concepts. Declare variables close to where they are first
  used — do not declare all variables at the top of a function.

- **Keep lines short; avoid horizontal alignment.**

  Conventional guideline is around 80–120 characters per line. Long lines
  force horizontal scrolling and are harder to read in diff/review views. Do
  NOT use horizontal alignment (aligning assignment operators or values into
  columns) — it looks tidy but makes routine edits disruptive and produces
  large diffs. Use whitespace within lines to clarify groupings (spaces
  around operators, consistent argument-list spacing, appropriate parentheses).

- **Automate formatting.**

  Structure conventions SHOULD be consistent throughout a codebase. Configure
  a code formatter or linter to enforce layout rules automatically — on save,
  as a pre-commit hook, or as a CI check. This removes formatting from code
  review discussions and ensures consistency as the codebase grows.

- **Prefer composition over inheritance.**

  Deep inheritance hierarchies SHOULD be avoided (shallow abstractions are
  preferred). Compose complex logic from small, shallow abstractions. Notable
  exception: domain modeling, where inheritance hierarchies can model
  real-world taxonomies usefully. In most other cases inheritance SHOULD be
  shallow or avoided altogether.

- **Prefer polymorphism over type-discriminating conditionals.**

  Long `if/else` or `switch/case` chains that branch on object type, category,
  or state are a code smell — brittle (every new variant requires updating
  each chain) and spread type-discriminating logic across the codebase. Define
  a common interface and let each concrete type implement its own behavior;
  callers invoke the interface method. This is NOT a rule against all
  conditional logic — simple conditions for genuine business decisions are
  fine. The heuristic applies to conditionals that discriminate on object type
  to select behavior.

- **Follow the Law of Demeter.**

  A method SHOULD only interact with: the object itself, its direct fields,
  its method arguments, and objects it creates directly. Do not "reach
  through" objects (eg. `order.getCustomer().getAddress().getCity()`) — that
  couples callers to the internal structure of intermediate objects. Fix by
  adding a delegating method to the intermediate object (`order.getDeliveryCity()`).

- **Do not conflate objects and data structures.**

  Objects hide data and expose behavior; data structures expose data and have
  little or no significant behavior. Both are useful, but they are
  complementary opposites. A class that exposes data via getters/setters AND
  contains significant business logic is a poor "hybrid" design — choose one
  or the other: hide data and expose behavior, or expose data and keep
  behavior elsewhere.

- **Prefer value objects over raw primitives for domain concepts.**

  Avoid _primitive obsession_: represent meaningful domain concepts with
  dedicated wrappers (`UserId`, `EmailAddress`, `MonetaryAmount`) rather than
  raw strings, integers, booleans. Value objects make function signatures
  self-documenting, let the type system reject misuse, and centralize
  validation of invariants. Value objects SHOULD be immutable — once created
  with valid state, they SHOULD NOT be modifiable.

- **Encapsulate boundary conditions in dedicated abstractions.**

  Range checks, upper/lower limits, off-by-one calculations are error-prone;
  when scattered, inconsistencies creep in. Encapsulate boundary logic in
  abstractions like `DateRange` or `PageSlice` that put the edge-case handling
  in a single, testable place. Code that works with the concept uses the
  abstraction rather than duplicating defensive checks at every call site.

- **Prefer non-static methods.**

  Static methods cannot be overridden through inheritance or replaced via
  dependency injection — they introduce tight coupling that is hard to break
  and make code harder to test and evolve. Non-static methods can be injected,
  substituted, mocked, and participate in polymorphism. Reserve static
  methods for genuinely stateless, context-free utility functions where lack
  of substitutability is an acceptable trade-off (pure math, simple string
  transforms with no alternative implementations ever needed).

- **Separate concurrency mechanics from business logic.**

  The single most important rule for concurrent code: keep concurrency
  infrastructure (thread pools, task queues, executors, async wrappers) in its
  own layer. Business logic SHOULD be written as if single-threaded and
  composed with the concurrency layer at a higher level, so it can be tested
  in isolation without non-determinism.

- **Minimize shared mutable state.**

  Shared mutable state is the root cause of most concurrency bugs (race
  conditions, data corruption, deadlocks). Eliminate it where possible via two
  complementary strategies: _immutability_ (immutable objects are inherently
  thread-safe; produce new values rather than mutating), and _message-passing_
  (each component owns private state and communicates only via messages —
  the model behind actor frameworks, CSP-style channels, and event-driven
  architectures).

- **Keep synchronized sections minimal; beware multi-lock deadlocks.**

  When shared mutable state is unavoidable, protect it with locks, mutexes,
  semaphores, atomics, or `synchronized` blocks. Only the minimal critical
  section — the exact reads/writes that must be atomic — SHOULD be inside the
  lock; holding locks across large blocks increases contention, reduces
  throughput, and risks deadlock. Code acquiring more than one lock is at
  deadlock risk if other code acquires the same locks in a different order; if
  multiple locks are necessary, establish and document a consistent
  acquisition ordering across the codebase and follow it without exception.

- **Test concurrent code rigorously.**

  Concurrency bugs are often non-deterministic — they may appear only under
  specific timing, hardware, or load. A passing dev-environment suite may fail
  in production. Run tests repeatedly and under stress to expose intermittent
  races; use thread sanitizers and concurrency analysis tools where available.
  Design business logic to be testable in isolation from concurrency
  infrastructure, so the bulk of correctness testing happens
  deterministically in a single-threaded context.

## References

- [TS-7 source](README.adoc)
- [TS-2: Software Design Qualities](../002/AGENTS.md)
- [TS-5: Application Architecture](../005/AGENTS.md)
