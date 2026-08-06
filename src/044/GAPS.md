# GAPS — TS-44 Non-Relational (NoSQL) Databases

> **Note**: This standard is currently a stub (`// TODO` only). All points are gaps because the standard has no written content.

---

## Polyglot persistence — choosing the right database per service/use case

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Each database suits some access patterns and not others, so Allegro adopted polyglot persistence; one service switched from Cassandra to MongoDB in a two-week sprint with no client-visible change because the external API stayed stable.
- **Coverage check**: TS-44 is a stub. TS-5 covers per-service databases and domain/persistence decoupling, and TS-45 covers migration mechanics, but the polyglot persistence principle is not covered.
- **Gap**: No standard addresses polyglot persistence or database-selection-per-service guidance.
- **Cross-references**: TS-45 (Data Migrations), TS-5 (Application Architecture)

---

## NoSQL database selection criteria and engine migration

- **Source**: https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
- **What the source says**: Bluesky migrated its data layer off PostgreSQL, adopting ScyllaDB for AppViews and SQLite for personal data servers, choosing ScyllaDB for its shard-aware Go driver and scalability characteristics.
- **Coverage check**: TS-44 is a stub. TS-45 covers migration mechanics but not the database-engine selection rationale.
- **Gap**: TS-44 does not cover NoSQL database selection criteria or specific engines.
- **Cross-references**: TS-45 (Data Migrations)