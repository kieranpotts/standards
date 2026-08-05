# TS-6 gap analysis

Gaps found comparing TS-6: *Distributed System Design* against the following
reference resource:

- https://12factor.net/concurrency (Factor VIII: Concurrency, "The Twelve-Factor
  App", Adam Wiggins, 2017)

**Assessment.** TS-6 is currently an unwritten stub — its `README.adoc` contains
only a title, a `// TODO` marker, and a table-of-contents macro with no included
content files. There is nothing to compare the reference material against, so
every claim in the Concurrency factor is "missing" in the trivial sense that the
whole standard is missing. This is recorded as a single Unresolved item rather
than as a list of Missing gaps, since itemizing gaps against a blank page adds
no information beyond "write this standard."

The Concurrency factor's subject matter — scaling an application horizontally
via a process model, with distinct process types for distinct workloads — is
squarely inside TS-6's stated scope (distributed system design) and would be a
reasonable anchor for the standard's first content. Related material already
exists elsewhere: TS-5 (`../005/06-services.adoc`) covers microservices,
reactive/event-driven services, and CQRS, which are adjacent but distinct
concerns (service decomposition, not process-level concurrency within a single
deployable). TS-49 (`../049/`) covers platform-level environment lifecycle but
not the app-level process model.

**Status:** First run, 2026-08-05. All gaps open.

## Missing

(Not itemized — see Unresolved.)

## Partial

(None — there is no existing content to be partial against.)

## Out-of-scope

(None identified in this run.)

## Unresolved

- [ ] TS-6 has no content to analyze. https://12factor.net/concurrency's core
      claims — processes as first-class citizens; the Unix process model
      assigning distinct process *types* to distinct workloads (eg. a web
      process type and a worker process type); horizontal scaling by running
      more processes, potentially across multiple physical machines; processes
      MUST NOT daemonize or write PID files; process lifecycle (starting,
      stopping, output capture, crash recovery, restarts) delegated to an
      external process manager (systemd, a cloud platform's process
      supervisor, or a tool like Foreman) rather than self-managed; and
      processes MUST be share-nothing and horizontally partitionable — would
      make a reasonable first section for this standard once it is authored.
      Recommend the user prioritize writing TS-6's baseline content (possibly
      starting from this reference), after which this gap analysis should be
      re-run to produce real Missing/Partial findings.
