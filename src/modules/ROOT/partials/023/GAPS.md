# TS-23 gap analysis

Gaps found comparing TS-23: Messages and events against the following reference
resources:

- `__TODO__/023/event-driven.md`

**Assessment.** The reference is a single short TODO note on event-driven
programming. Most of its content is general paradigm commentary that sits
outside TS-23's stated scope (design and implementation of messages and events
for intra-organization asynchronous communication). One point — the necessity of
logging, monitoring, and alerting for event-driven systems — is a genuine
operational gap not addressed anywhere in the standard, despite TS-23 already
covering delivery reliability, retries, and dead letters.

**Status:** First run (2026-08-05). No prior `GAPS.md` existed. One missing gap
(observability) and two out-of-scope items flagged for the user.

**Second run, 2026-08-06.** Re-run against Brandur Leppka's "Using Atomic
Transactions to Power an Idempotent API" (https://brandur.org/http-transactions).
One point was routed to TS-23: the transactionally-staged job drain
(transactional outbox) pattern (D). It is Missing — TS-23 recommends
idempotent messages (`03-delivery-and-reliability.adoc:16-28`, a
prerequisite) but never addresses producer-side atomic enqueuing or the
outbox pattern. One new Missing gap added; all prior gaps remain open.

**Third run, 2026-08-06.** Re-run against Brandur Leppka's "Transactionally
Staged Job Drains in Postgres" (https://brandur.org/job-drain). This is a
deeper treatment of the same outbox pattern recorded as Missing above (the
http-transactions D entry). The standard still doesn't cover it, so no new
Missing item is added; instead one new Partial entry captures the deeper
article's additions beyond the existing D entry — the before-commit race
failure mode, the bad-alternatives anti-patterns (after_commit silent loss;
retry-thrash), enqueuer implementation details (single-enqueuer lock,
repeatable read for DELETE/SELECT consistency, batch + exponential backoff),
and the in-database-queue scaling/locking critique. All prior gaps remain
open.

## Missing

- [ ] `__TODO__/023/event-driven.md:7` states that logging, monitoring, and
      alerting become necessary to stay on top of event-driven systems and
      ensure they are working as expected. TS-23 addresses delivery
      reliability, retries, circuit breakers, dead letters, and SLAs
      (`src/modules/ROOT/partials/023/03-delivery-and-reliability.adoc:1-143`) but gives no guidance
      on observability — logging message flows, monitoring delivery health,
      or alerting on stuck/failed/dead-lettered messages. Recommend a new
      section in `src/modules/ROOT/partials/023/03-delivery-and-reliability.adoc` after "Service
      level agreements" (around line 120) or a new top-level section on
      observability. (Scope call: arguably belongs in a dedicated
      observability standard, but since TS-23 already covers operational
      reliability concerns, observability is a natural fit here.)

- [ ] https://brandur.org/http-transactions ("Transaction-staged jobs")
      covers the transactional outbox pattern, which is not addressed
      anywhere in the standard. The reference describes the
      "transactionally-staged job drain": enqueueing a background job
      (eg. to Sidekiq) within an HTTP request risks an invalid job if the
      surrounding database transaction rolls back (the job references
      data that no longer exists and can never succeed); the solution is
      to write jobs to a job-staging table *within* the transaction (so
      by isolation the staged job is invisible to other transactions
      until commit, and a rolled-back job is never seen), and a separate
      enqueuer process drains the staging table in batches, enqueues
      each job to the real queue, and deletes the staged rows in the same
      transaction. The enqueuer guarantees at-least-once (not exactly-
      once) delivery, so jobs must be idempotent; and putting the job
      queue directly in the database (eg. Que) risks table bloat on
      systems like Postgres. TS-23 treats delivery reliability as a
      transport/network concern (`03-delivery-and-reliability.adoc:1-143`)
      and recommends idempotent messages with a `message_id` idempotency
      key (`:16-28`) — a prerequisite for the outbox's correctness — but
      never addresses the producer-side atomicity problem (enqueuing
      outside the transaction it depends on), staging tables, the
      enqueuer-drain pattern, or in-database-queue bloat. Recommend a
      new "Transactional outbox" subsection in
      `03-delivery-and-reliability.adoc` covering the staged-drain
      pattern and its at-least-once/idempotent-consumer requirements.
      Note: the database-transaction mechanism this relies on is TS-43's
      scope.

## Partial

- [ ] https://brandur.org/job-drain ("Transactionally Staged Job Drains in
      Postgres") is a deeper treatment of the outbox pattern recorded as
      Missing above (the http-transactions "Transaction-staged jobs" entry)
      and adds specifics that entry doesn't capture — specifically: (a) the
      *before-commit* failure mode, distinct from rollback: a fast queue
      lets a worker run a job before its enclosing transaction commits, so
      the job fails to find data that isn't visible yet (eg. a job to look
      up a just-inserted user record); (b) the common bad alternatives and
      why they're worse — enqueueing after commit (eg. Rails' `after_commit`)
      risks a crash between commit and enqueue producing *silent,
      unmonitored* job loss, and letting early retries fail to rely on the
      queue's retry scheme thrashes and floods errors; (c) enqueuer
      implementation details — a single enqueuer (held under a lock),
      `REPEATABLE READ` isolation so the post-enqueue `DELETE` sees the
      same jobs as the `SELECT`, batched selection, and exponential backoff
      sleep when the staging table is empty; and (d) the scaling critique of
      in-database queues (delayed_job, que, queue_classic) — workers
      locking jobs directly in the DB don't scale under load (long-running
      transactions slow job locking, the queue spirals), so the staged
      drain selects primed jobs in bulk and feeds them to a store like
      Redis better-suited to distributing to competing workers. TS-23's
      existing idempotency guidance (`03-delivery-and-reliability.adoc:16-28`)
      is a prerequisite but none of the above is addressed. Recommend
      folding these specifics into the "Transactional outbox" subsection
      proposed by the existing Missing entry. Note: the `REPEATABLE READ`
      isolation rationale is TS-43's scope.

## Out-of-scope

- [ ] `__TODO__/023/event-driven.md:5` observes that event-driven
      programming is more complex due to the lack of a clear flow of control.
      This is general commentary on the event-driven programming paradigm
      rather than a design/implementation rule for messages and events. It
      plausibly sits outside TS-23's stated purpose, which is best practices
      for designing and implementing messages and events in message-driven
      architectures — not a treatise on the paradigm's characteristics.
      Flagged for the user to confirm or overrule; if kept, it would fit as a
      motivating note in `src/modules/ROOT/pages/023.adoc:5-17`.

- [ ] `__TODO__/023/event-driven.md:5` observes that event-driven
      programming is often unavoidable in web client application interfaces,
      distributed systems, and multi-threaded environments. TS-23's scope is
      explicitly narrowed to asynchronous communication within a single
      organization's internal network (`src/modules/ROOT/pages/023.adoc:8-9`); web client
      UIs and multi-threaded environments are outside that focus, and the
      "distributed systems" mention is too generic to be actionable. Flagged
      for the user to confirm or overrule.

## Unresolved

_(None. The single reference file was read in full.)_