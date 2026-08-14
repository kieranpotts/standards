# GAPS — TS-44 Non-relational (NoSQL) databases

> **Note**: This standard was a stub (`// TODO` only) until 2026-08-14, when
> it was authored from scratch. Both gaps below are now resolved.

---

## Polyglot persistence — choosing the right database per service/use case

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Each database suits some access patterns and not others, so Allegro adopted polyglot persistence; one service switched from Cassandra to MongoDB in a two-week sprint with no client-visible change because the external API stayed stable.
- **Coverage check**: TS-44 is a stub. TS-5 covers per-service databases and domain/persistence decoupling, and TS-45 covers migration mechanics, but the polyglot persistence principle is not covered.
- **Gap**: No standard addresses polyglot persistence or database-selection-per-service guidance.
- **Cross-references**: TS-45 (Data migrations), TS-5 (Application architecture)
- **RESOLVED**: Closed 2026-08-14 by the new "Polyglot persistence" section
  in `04-selecting-a-database.adoc`, citing this source directly and
  cross-referencing TS-5 for the architectural decoupling that makes a
  per-service database switch cheap.

---

## NoSQL database selection criteria and engine migration

- **Source**: https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
- **What the source says**: Bluesky migrated its data layer off PostgreSQL, adopting ScyllaDB for AppViews and SQLite for personal data servers, choosing ScyllaDB for its shard-aware Go driver and scalability characteristics.
- **Coverage check**: TS-44 is a stub. TS-45 covers migration mechanics but not the database-engine selection rationale.
- **Gap**: TS-44 does not cover NoSQL database selection criteria or specific engines.
- **Cross-references**: TS-45 (Data migrations)
- **RESOLVED**: Closed 2026-08-14 by the new "NoSQL database selection
  criteria" section in `04-selecting-a-database.adoc`, listing consistency
  model, scalability/sharding model, driver and ecosystem maturity (citing
  this source's ScyllaDB shard-aware Go driver example), organizational
  operational maturity, and required query capability, in order of how
  costly each is to change after the fact.