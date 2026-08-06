# TS-44 gap analysis

Gaps found comparing TS-44: *Non-Relational (NoSQL) Databases* against the
following reference resource:

- https://brandur.org/acid (Brandur Leppka, "Building Robust Systems with
  ACID and Constraints")

**Assessment.** TS-44 is currently an unwritten stub — its `README.adoc`
contains only a title, TOC configuration, and a `// TODO` marker, with no
`include::` directives and no content files. There is nothing to compare the
reference material against, so every claim is "missing" in the trivial sense
that the whole standard is missing. This is recorded as a single Unresolved
item rather than as a list of Missing gaps, since itemizing gaps against a
blank page adds no information beyond "write this standard." Two points from
the reference were routed here and are squarely in-scope for TS-44: the
schemaless-is-"easy"-not-"simple" trade-off (Rich Hickey's distinction;
schema/constraints for long-term maintainability), and database-selection
guidance (default to an ACID relational store; vertical scaling suffices for
most; don't prematurely trade ACID for horizontal scaling; newer systems
like Citus and Spanner offer ACID + scaling).

**Status:** First run, 2026-08-06. TS-44 is an unwritten stub; see
Unresolved.

**Second run, 2026-08-06.** Re-run against Brandur Leppka's "Implementing
Stripe-like Idempotency Keys in Postgres" (https://brandur.org/idempotency-keys).
One point was routed to TS-44: the non-ACID-stores limitation (without ACID,
atomic phases are impossible and every database operation becomes equivalent
to a foreign state mutation). TS-44 remains an unwritten stub; the point is
added to the Writing backlog below.

## Missing

(None — TS-44 is an unwritten stub; itemizing gaps against a blank page is
not informative. See Unresolved.)

## Partial

(None identified in this run.)

## Out-of-scope

(None identified in this run.)

## Writing backlog

Topics routed to TS-44 from assessed references, to be covered when the
standard is authored (then re-run this gap analysis for real Missing/Partial
findings):

- **Schemaless is "easy" not "simple"** (https://brandur.org/acid, P5):
  Rich Hickey's distinction — "simple" (opposite of complex) vs "easy" (at
  hand / approachable, short-term gratification to the detriment of
  long-term maintainability); schemaless databases are easy, not simple;
  the faster-prototyping claim isn't even true (RDBMS + ORM + migrations
  keep up); well-defined schema and self-consistent data ease long-term
  production life; bolted-on object-modeling frameworks arrive too late
  (inconsistent data, difficult migrations, twisted app code).
- **Database selection / default to ACID relational** (https://brandur.org/acid,
  P6): ACID databases scale further than commonly claimed; vertical scaling
  serves the vast majority of services (possibly millions of users) with
  archiving/offloading of "junk" data; only at Google-scale is giving up
  aspects of ACID defensible; newer systems offer ACID + scaling (Citus
  per-shard ACID, Google Spanner distributed read-write transactions);
  don't trade ACID for "novelties du jour" or an unexamined
  horizontal-scaling assumption; the database is a foundational substrate
  providing leverage — reimplementing its guarantees in app code is worse;
  default to starting with an RDBMS providing ACID and constraints
  (Postgres).
- **Non-ACID stores and atomic phases** (https://brandur.org/idempotency-keys,
"Non-ACID data stores"): without transactional semantics (eg. MongoDB), a
database can't guarantee that any two operations commit atomically, so the
notion of an atomic phase is impossible — every database operation becomes
equivalent to a foreign state mutation. A key trade-off/limitation of
non-ACID stores to weigh against the schemaless/scaling benefits above.

## Unresolved

- [ ] TS-44 has no content to analyze. Recommend the user prioritize
      writing TS-44's baseline content — at minimum addressing when to
      choose a NoSQL store over a relational one, the schemaless/
      easy-vs-simple trade-off, and the horizontal-scaling assumptions that
      drive NoSQL adoption (per https://brandur.org/acid) — after which
      this gap analysis should be re-run to produce real Missing/Partial
      findings.