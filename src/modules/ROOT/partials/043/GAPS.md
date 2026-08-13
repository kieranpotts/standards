# TS-43 gap analysis

Gaps found comparing TS-43: Relational databases and SQL against the following
reference resources:

- `__TODO__/columns.adoc`
- `__TODO__/naming-conventions.md`
- `__TODO__/sql.md`
- `__TODO__/types.adoc`
- `__TODO__/databases/_index.md`
- `__TODO__/databases/_100-primary-keys.md`
- `__TODO__/databases/_200-schema-less.md`
- `__TODO__/databases/mysql.md`
- `__TODO__/databases/mysql2.md`
- `__TODO__/databases/_todo/general-db-design.md`
- `__TODO__/sql/index.md`
- `__TODO__/sql/0500-joins.md`
- `__TODO__/sql2/index.md`
- `__TODO__/sql2/_sql.md`
- `__TODO__/sql2/_todo/0100-introduction.md`
- `__TODO__/sql2/_todo/0200-general-style.md`
- `__TODO__/sql2/_todo/0250-reserved-words.md`
- `__TODO__/sql2/_todo/0300-naming-conventions.md`
- `__TODO__/sql2/_todo/0310-tables.md`
- `__TODO__/sql2/_todo/0320-columns.md`
- `__TODO__/sql2/_todo/0330-aliases.md`
- `__TODO__/sql2/_todo/0340-stored-procedures.md`
- `__TODO__/sql2/_todo/0500-formalisms.md`
- `__TODO__/sql2/_todo/0600-types.md`
- `__TODO__/sql2/_todo/0800-functions.md`
- `__TODO__/sql2/_todo/1000-schema-definitions.md`
- `__TODO__/sql2/_todo/1500-comments.md`
- `__TODO__/sql2/_todo/9999-references.md`
- `https://en.wikipedia.org/wiki/ACID` (via `__TODO__/databases/_todo/ACID - Wikipedia.URL`)
- `https://www.mysqltutorial.org/mysql-join/` (via `__TODO__/sql2/MySQL Join Made Easy For Beginners.URL`)

**Assessment.** TS-43 currently contains only its sharding section
(`01-sharding.adoc`) plus a stub `AGENTS.md`. Its stated scope is "general best
practices for working with relational databases and writing SQL", so the
overwhelming majority of the reference material falls inside that scope and is
simply not yet written. Almost everything below is **missing** rather than
partial — the standard does not address SQL style, naming, types, joins,
schema design, transactions, or keys at all. The only point of contact is the
sharding section's passing mention of replication, denormalization, and
eventual consistency, which touches the consistency-models topic shallowly. The
pure DBA/operations material (installation, service control, backup tooling,
user/permission administration) is flagged as out-of-scope for the user to
confirm.

**Status:** First run (2026-08-05). All gaps open. Re-runs should preserve
these citations and check off items as the standard is expanded.

**Second run, 2026-08-06.** Re-run against Brandur Leppka's "Building Robust
Systems with ACID and Constraints" (https://brandur.org/acid). Four points
were routed to TS-43 (atomicity, consistency+constraints, isolation,
durability). All four are already recorded as Missing above (sourced from
the Wikipedia ACID article), so no new Missing items were added; the
article largely restates the same ACID gaps. One new Partial entry added
capturing the article's distinctive contributions beyond the Wikipedia
entries (document-level atomicity critique, "data janitor" consequences, the
four isolation levels enumerated with their phenomena, and the custom-
locking-is-slow/buggy vs. built-in argument). All prior gaps remain open.

**Third run, 2026-08-06.** Re-run against Brandur Leppka's "Using Atomic
Transactions to Power an Idempotent API" (https://brandur.org/http-transactions).
One point was routed to TS-43: SERIALIZABLE isolation for concurrency
protection with retry and UNIQUE defense-in-depth (C). It is Missing —
distinct from the existing Wikipedia isolation Missing entry and the
Brandur "acid" Partial entry, which cover isolation in the abstract and
the four levels/phenomena respectively, but not the practical API race
pattern, retry-on-serialization-failure, or the UNIQUE-as-defense-in-
deepth layering. One new Missing gap added; all prior gaps remain open.

## Missing

### SQL style and formatting

- [ ] `__TODO__/sql2/_todo/0200-general-style.md:3` — keep SQL succinct and
      free of redundant code (unnecessary quoting, parentheses, or `WHERE`
      clauses that can be derived). Not addressed anywhere in the standard.
      Recommend a new section (e.g. `02-sql-style.adoc`).

- [ ] `__TODO__/sql2/_todo/0200-general-style.md:6-36` — judicious use of
      whitespace and indentation; right-align root keywords (`SELECT`, `FROM`,
      etc.) so they form a "river" down the middle, with implementation
      details left-aligned. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0200-general-style.md:38-43` — spacing rules: spaces
      before/after `=`, after commas, and surrounding apostrophes (where not
      in parentheses or before a trailing comma/semicolon). Not addressed.
      Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0200-general-style.md:52-82` — line-spacing rules:
      newline before `AND`/`OR`, after semicolons, after each keyword
      definition, after commas when grouping columns, and to separate code
      into related sections. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0200-general-style.md:85-99` — join formatting:
      joins indented to the other side of the "river" and grouped with a new
      line. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0200-general-style.md:102-117` — subquery
      formatting: align to the right side of the river, lay out as any other
      query, place closing parentheses on a new line aligned with the opener
      (especially for nested subqueries). Not addressed. Recommend a new
      section.

- [ ] `__TODO__/sql2/_todo/0250-reserved-words.md:3` — always use upper case
      for reserved keywords such as `SELECT` and `WHERE`. Not addressed.
      Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0250-reserved-words.md:5` — prefer the full-length
      keyword over abbreviations where available (e.g. `ABSOLUTE` over `ABS`).
      Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0250-reserved-words.md:7` — avoid vendor-specific
      keywords where an ANSI SQL keyword performs the same function, for
      portability. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0250-reserved-words.md:10-840` — a curated list of
      reserved keywords across ANSI SQL (92, 99, 2003), MySQL 3–5.x, PostgreSQL
      8.1, MS SQL Server 2000, MS ODBC, and Oracle 10.2. The standard includes
      no such reference list. Recommend a new appendix-style section.

- [ ] `__TODO__/sql2/_todo/1500-comments.md:3-5` — comment style: include
      comments where useful; prefer C-style `/* ... */`; otherwise use `--`
      followed by a space and terminate with a newline. Not addressed.
      Recommend a new section.

### Naming conventions

- [ ] `__TODO__/sql2/_todo/0300-naming-conventions.md:4-11` — case guidance:
      snake_case is the prevailing standard and should be the default (adopt
      the prevailing standard of the system you are working with); avoid
      CamelCase as it is hard to scan in SQL files. Not addressed. Recommend a
      new section.

- [ ] `__TODO__/sql2/_todo/0300-naming-conventions.md:12-16` — names must
      begin with a character and never end with a trailing underscore; use
      only letters, numbers, and underscores; delimit words with single
      underscores and avoid consecutive underscores. Not addressed. Recommend
      a new section.

- [ ] `__TODO__/sql2/_todo/0300-naming-conventions.md:19-21` — avoid prefixes
      and Hungarian notation such as `sp_` or `tbl` (valid exceptions
      notwithstanding). Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0300-naming-conventions.md:24-28` — avoid plurals;
      prefer the collective term (`staff` over `employees`, `people` over
      `individuals`). Tables use a collective name or, less ideally, a plural
      form. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0300-naming-conventions.md:33-43` — choose
      consistent, descriptive, unique identifiers; keep length under 30
      characters; avoid abbreviations (except commonly understood ones); avoid
      reserved keywords as identifiers; avoid quoting identifiers (use SQL92
      double quotes if quoting is unavoidable). Not addressed. Recommend a
      new section.

- [ ] `__TODO__/sql2/_todo/0310-tables.md:1-9` (also
      `__TODO__/sql2/_todo/0300-naming-conventions.md:46-54`) — table naming:
      collective or plural name, no `tbl`/descriptive prefix, never give a
      table the same name as one of its columns, and avoid concatenating two
      table names for a relationship table (prefer `services` over
      `cars_mechanics`). Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0320-columns.md:1-9` (also
      `__TODO__/sql2/_todo/0300-naming-conventions.md:57-65`) — column naming:
      always singular; avoid using `id` alone as the primary identifier where
      possible; never name a column the same as its table; always lower case
      except for proper nouns. Not addressed. Recommend a new section. (Note:
      this conflicts with the primary-key house style in
      `__TODO__/databases/_100-primary-keys.md:139`, which mandates `id` — the
      standard should reconcile the two.)

- [ ] `__TODO__/sql2/_todo/0320-columns.md:12-30` — column-suffix conventions
      with universal meaning: `_id`, `_status`, `_total`, `_num`, `_name`,
      `_seq`, `_date`, `_tally`, `_size`, `_addr`. Not addressed. Recommend a
      new section.

- [ ] `__TODO__/sql2/_todo/0330-aliases.md:1-22` (also
      `__TODO__/sql2/_todo/0300-naming-conventions.md:68-74`) — alias rules:
      relate to the proxied object; use the first letter of each word as a
      rule of thumb; append a number on conflict; always include the `AS`
      keyword; name computed data (`SUM`, `AVG`) as if it were a schema
      column. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0340-stored-procedures.md:1-5` (also
      `__TODO__/sql2/_todo/0300-naming-conventions.md:77-79`) — stored-procedure
      naming: the name must contain a verb; do not prefix with `sp_` or other
      descriptive/Hungarian prefixes. Not addressed. Recommend a new section.

- [ ] `__TODO__/naming-conventions.md:3-17` — adopt a controlled vocabulary for
      column names so they act as contracts/promises for the data they store;
      benefits include easier fake-data generation, automated validation,
      safer data pipelines, and cross-dataset discoverability. Not addressed.
      Recommend a new section.

- [ ] `__TODO__/naming-conventions.md:21-47` — column-name schema
      `<type>_<subject>(_<modifier>)` with a library of global type prefixes
      (`id`, `uuid`, `is`, `n`, `dt`, `tm`, `cat`) plus domain-specific ones
      (`loc`, `addr`); all columns sharing a type prefix should store data in
      the same format. Not addressed. Recommend a new section.

- [ ] `__TODO__/naming-conventions.md:49-59` — the subject component (a noun
      from the business domain) and the optional modifier suffix (an
      adjective describing a variant, e.g. `raw`/`clean`) of the column-name
      schema. Not addressed. Recommend a new section.

### Columns, keys, and schema definition

- [ ] `__TODO__/columns.adoc:1-19` — column ordering convention within a table:
      `id` (PK), `uuid`, `logged_at` (for log records), foreign keys
      (alphabetical), other columns (logical groups, alphabetical if in
      doubt), then `created_at`/`updated_at`/`deleted_at`. Not addressed.
      Recommend a new section.

- [ ] `__TODO__/databases/_100-primary-keys.md:3` — not every table needs a
      primary key; do not add one by default; every field and constraint must
      serve a purpose. Not addressed. Recommend a new section.

- [ ] `__TODO__/databases/_100-primary-keys.md:7-36` — UUID vs auto-incrementing
      integer primary keys: trade-offs (UUIDs are 16 bytes but can be
      generated anywhere, are globally unique, enable offline-first clients,
      merging, distribution, and replication; auto-increment IDs are smaller
      and convenient at small scale); UUIDs should be the default, with
      auto-increment IDs optionally mixed in (auto-increment is generally
      better for foreign-key links). Not addressed. Recommend a new section.

- [ ] `__TODO__/databases/_100-primary-keys.md:38-141` — primary-key naming
      conventions: `id` vs `<table>_id`; arguments for each (join clarity,
      searchability, ORM/ActiveRecord compatibility, semantic fit); the
      reference's house style is `id`, with composite/aggregate keys as a
      valid exception. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/1000-schema-definitions.md:7-9` — schema-definition
      (`CREATE`/`ALTER`) readability: order and group column definitions where
      it makes sense; indent column definitions by four spaces within
      `CREATE`. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/1000-schema-definitions.md:12-16` — default values:
      the default must be the same type as the column (e.g. a `DECIMAL` column
      should not take an `INTEGER` default); defaults follow the data-type
      declaration and come before any `NOT NULL`. Not addressed. Recommend a
      new section.

- [ ] `__TODO__/sql2/_todo/1000-schema-definitions.md:23-31` — choosing keys:
      the key should be unique; data type should be consistent across the
      schema and unlikely to change; the value should be validatable against a
      standard format (e.g. ISO); keep keys simple but use compound keys where
      necessary. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/1000-schema-definitions.md:35-69` — defining
      constraints: tables must have at least one key; give constraints custom
      names except `UNIQUE`/`PRIMARY KEY`/`FOREIGN KEY` (vendor names are
      usually intelligible); specify the primary key first after
      `CREATE TABLE`; place constraints directly beneath the corresponding
      column, indented to the right of the column name; place multi-column
      constraints near both columns or at the end; table-level constraints at
      the end; `ON DELETE` before `ON UPDATE` (alphabetical); use
      `LIKE`/`SIMILAR TO` for string integrity; use `CHECK()` ranges for
      numeric values (at least `> 0`); keep `CHECK()` constraints in separate
      clauses for debuggability. Not addressed. Recommend a new section.

- [ ] `__TODO__/databases/mysql.md:202-241` (also `__TODO__/databases/mysql.md:246-250`)
      — MySQL `UNIQUE` constraints: column-level `UNIQUE`, multi-column
      `UNIQUE(...)`, named constraints via `CONSTRAINT ... UNIQUE`, adding
      constraints to existing tables with `ALTER TABLE`, and removing them
      with `DROP INDEX`. Not addressed. Recommend a new section.

### Data types

- [ ] `__TODO__/sql2/_todo/0600-types.md:7` — avoid vendor-specific data types
      where possible; they are not portable and may not exist in older or
      future versions of the same vendor's software. Not addressed. Recommend
      a new section.

- [ ] `__TODO__/sql2/_todo/0600-types.md:9` — avoid splitting a value between
      columns (e.g. value in one column, units in another); the value column
      should make the units self-evident. Not addressed. Recommend a new
      section.

- [ ] `__TODO__/sql2/_todo/0600-types.md:12-19` — string types: prefer
      `CHAR`, `CLOB`, and `VARCHAR` for maximum cross-engine compatibility.
      Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0600-types.md:22-39` — numeric types: use `REAL` or
      `FLOAT` only for floating-point math; prefer `NUMERIC` and `DECIMAL` to
      avoid rounding errors; exact numeric types (`BIGINT`, `DECIMAL`,
      `DECFLOAT`, `INTEGER`, `NUMERIC`, `SMALLINT`) and approximate types
      (`DOUBLE PRECISION`, `FLOAT`, `REAL`). Not addressed. Recommend a new
      section.

- [ ] `__TODO__/sql2/_todo/0600-types.md:42-54` (also
      `__TODO__/types.adoc:3-5`) — date/time types: prefer ISO-8601-compliant
      values (`YYYY-MM-DD HH:MM:SS.SSSSS`); `DATE`, `TIME`, and `TIMESTAMP`
      are well supported; timestamps should not be used to represent past or
      future dates — prefer ISO 8601 storage. Not addressed. Recommend a new
      section.

- [ ] `__TODO__/sql2/_todo/0600-types.md:57-60` — binary types guidance (the
      reference lists `BINARY` etc., though the section appears to contain a
      copy-paste error repeating `TIME`/`TIMESTAMP`). Not addressed. Recommend
      a new section.

### Joins and queries

- [ ] `https://www.mysqltutorial.org/mysql-join/#introduction` — join
      fundamentals: a relational database links tables via foreign-key
      columns; a join links data between tables on common-column values;
      MySQL supports inner, left, right, and cross joins (no `FULL OUTER
      JOIN`); joins appear after `FROM` in a `SELECT`. Not addressed. Recommend
      a new section.

- [ ] `https://www.mysqltutorial.org/mysql-join/#mysql-inner-join` — inner
      join semantics and syntax (`INNER JOIN ... ON ...`); the `USING`
      clause replaces `ON` when the matching column name is the same in both
      tables; only matching rows are returned. Not addressed. Recommend a
      new section.

- [ ] `https://www.mysqltutorial.org/mysql-join/#mysql-left-join` — left join
      semantics: returns all left-table rows whether or not a match exists,
      with `NULL` for unmatched right-table columns; `LEFT JOIN ... WHERE
      <right_col> IS NULL` finds left rows with no match; `USING` syntax.
      Not addressed. Recommend a new section.

- [ ] `https://www.mysqltutorial.org/mysql-join/#mysql-right-join` — right
      join semantics (mirror of left join); syntax; `USING`; `WHERE ... IS
      NULL` to find unmatched right rows. Not addressed. Recommend a new
      section.

- [ ] `https://www.mysqltutorial.org/mysql-join/#mysql-cross-join` — cross
      join produces a Cartesian product (`n × m` rows); no join condition;
      syntax; useful for generating planning data. Not addressed. Recommend a
      new section.

- [ ] `__TODO__/sql2/_sql.md:25-27` — many-to-many relationships via joining
      tables; use composite keys of the two foreign-key columns (rather than
      an `id`) to guarantee each relationship is defined once. Not addressed.
      Recommend a new section.

- [ ] `__TODO__/sql2/_sql.md:36-59` — `JOIN` vs subquery for the same result;
      sub-selects can be slower — benchmark alternative formulations of
      complex queries. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_sql.md:62-102` — paginated search with
      `LIMIT offset, count`; obtaining the total result count (separate
      un-`LIMIT`ed query, caching it, or MySQL's
      `SQL_CALC_FOUND_ROWS`/`FOUND_ROWS()`); storing the count in session
      variables for subsequent pages. Not addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0500-formalisms.md:3-9` — formalisms: prefer
      `BETWEEN` over chained `AND`; `IN()` over multiple `OR`; `CASE` for
      value interpretation (nestable); avoid `UNION` and temporary tables
      where the schema can be optimized to remove the reliance on them. Not
      addressed. Recommend a new section.

- [ ] `__TODO__/sql2/_todo/0800-functions.md:3-5` — functions: prefer standard
      SQL functions over vendor-specific ones for portability, but use a
      vendor-specific function when it gives a significant advantage (e.g.
      speed) that outweighs portability. Not addressed. Recommend a new
      section.

### Transactions and consistency

- [ ] `https://en.wikipedia.org/wiki/ACID#` — ACID (atomicity, consistency,
      isolation, durability) as a set of transaction properties guaranteeing
      data validity despite errors and failures; the transaction paradigm
      and its influence on database systems. Not addressed. Recommend a new
      section.

- [ ] `https://en.wikipedia.org/wiki/ACID#Atomicity` — atomicity: a
      transaction is an all-or-nothing unit; if any statement fails the whole
      transaction fails and the database is left unchanged; a transaction
      cannot be observed in progress by another client. Not addressed.
      Recommend a new section.

- [ ] `https://en.wikipedia.org/wiki/ACID#Consistency` — consistency: a
      transaction can only move the database from one consistent state to
      another, preserving invariants; written data must satisfy all defined
      rules (constraints, cascades, triggers); referential integrity as an
      example invariant. Not addressed. Recommend a new section.

- [ ] `https://en.wikipedia.org/wiki/ACID#Isolation` — isolation: concurrent
      execution leaves the database in the same state as sequential
      execution; the main goal of concurrency control; effects of an
      incomplete transaction may be invisible depending on the isolation
      level. Not addressed. Recommend a new section.

- [ ] `https://en.wikipedia.org/wiki/ACID#Durability` — durability: once
      committed, a transaction persists despite system failure; usually means
      completed transactions are recorded in non-volatile memory. Not
      addressed. Recommend a new section.

- [ ] `https://en.wikipedia.org/wiki/ACID#` — BASE (basically available, soft
      state, eventually consistent) as the opposite of ACID; the CAP theorem
      framing that a database leans toward ACID (consistency) or BASE
      (availability); SQL vs NoSQL alignment. Not addressed. Recommend a new
      section.

- [ ] `https://en.wikipedia.org/wiki/ACID#Implementation` — transaction
      implementation techniques: write-ahead logging and shadow paging;
      locks must be acquired on data to be updated (and possibly read,
      depending on isolation level). Not addressed. Recommend a new section.

- [ ] `https://en.wikipedia.org/wiki/ACID#Locking_vs._multiversioning` —
      locking vs multiversion concurrency control (MVCC): two-phase locking
      for full isolation; MVCC gives readers unmodified prior versions so
      readers don't block writers and vice versa; snapshot isolation as one
      MVCC implementation that relaxes isolation. Not addressed. Recommend a
      new section.

- [ ] `https://en.wikipedia.org/wiki/ACID#Distributed_transactions` —
      distributed transactions: additional complications when no single node
      owns all the data; the two-phase commit protocol (distinct from
      two-phase locking) provides atomicity by having a coordinator confirm
      all participants are prepared before formalizing the commit. Not
      addressed. Recommend a new section.

- [ ] https://brandur.org/http-transactions ("Concurrency protection" /
      "Retrying an abort" / "Data protection in layers") covers practical
      SERIALIZABLE-isolation usage not captured by the existing isolation
      entries above — specifically: (a) using `SERIALIZABLE` to emulate
      serial execution and abort one of two concurrent check-then-insert
      requests that would otherwise duplicate a row (eg. two "create user"
      requests both passing `SELECT ... WHERE email = ?` then both
      `INSERT`); (b) retrying a serialization failure within the same
      request loop, manually or automatically via an ORM facility like
      Sequel's `retry_on: [Sequel::SerializationFailure]`; and (c) "data
      protection in layers" — adding a `UNIQUE` constraint even when using
      `SERIALIZABLE`, as defense-in-depth against incorrectly invoked
      transactions or buggy code (the constraint as a second layer
      beyond the isolation level). TS-43 has no transactions/isolation
      content (only `01-sharding.adoc`), so none of this is addressed.
      Recommend folding into the new "Transactions and consistency"
      section proposed by the existing entries, with a worked check-then-
      insert example, the retry pattern, and the constraint-plus-
      isolation defense-in-depth guidance. Note: the request-level retry
      loop overlaps TS-21 (HTTP APIs), which lacks the 1:1
      request↔transaction model (see `../021/GAPS.md`).

## Partial

- [ ] `https://en.wikipedia.org/wiki/ACID#Consistency` and
      `https://en.wikipedia.org/wiki/ACID#` (BASE) cover transaction
      consistency models (ACID vs BASE, isolation levels, MVCC, distributed
      consistency) more thoroughly than `01-sharding.adoc:181-183`, which
      mentions only that sharding combined with replication/denormalization
      requires planning for _eventual_ data consistency across shards. The
      standard touches consistency only in the narrow sharding context and
      does not cover transaction consistency models, isolation levels, or
      ACID/BASE trade-offs. Recommend a new section on transactions and
      consistency, cross-linked from the sharding section.

- [ ] https://brandur.org/acid ("Building Robust Systems with ACID and
      Constraints") adds article-specific framing beyond the Wikipedia ACID
      entries above (Missing: atomicity, consistency, isolation, durability) —
      specifically: (a) "document-level atomicity" (MongoDB/RethinkDB/CouchBase)
      is atomic per row only and insufficient for multi-object writes, and the
      consequences of lacking transactional atomicity — invalid intermediate
      state, retries, "fixer scripts," engineers as "data janitors," and code
      mutating to defensively handle accumulated bad-state combinations; (b)
      the four isolation levels enumerated by name (read uncommitted, read
      committed, repeatable read, serializable) with the phenomena each allows
      (dirty read, nonrepeatable read, phantom read, serialization anomaly),
      and the argument that custom pessimistic locking is slow, inefficient,
      labor-intensive, and probably buggy versus a built-in ACID MVCC locking
      system; (c) the duplicate-email registration example for uniqueness-
      constraint-based consistency. Recommend folding these specifics into the
      new transactions/consistency section proposed by the existing entries.
      Note: the article's broader schemaless-easy-not-simple and default-to-
      ACID/vertical-scaling points were routed to TS-44.

## Out-of-scope

- [ ] `__TODO__/databases/mysql.md:14-100` covers MySQL installation
      (`apt-get install mysql-server`, `mysql_secure_installation`), service
      controls (`systemctl start/stop/restart/enable mysqld`), and `my.cnf`
      resource tuning — this is OS/DBA administration, plausibly outside a
      "writing SQL / working with relational databases" standard. Flagged
      for the user to confirm or overrule.

- [ ] `__TODO__/databases/mysql.md:103-180` covers MySQL user and permission
      administration (`CREATE USER`, `GRANT`, `REVOKE`, `FLUSH PRIVILEGES`,
      `DROP USER`, privilege types) — database administration rather than
      application SQL best practices. Flagged for the user to confirm or
      overrule.

- [ ] `__TODO__/databases/mysql.md:257-273` covers MySQL table
      defragmentation via scheduled `OPTIMIZE TABLE`/`mysqlcheck` cron jobs —
      DBA maintenance operations. Flagged for the user to confirm or
      overrule.

- [ ] `__TODO__/databases/mysql.md:274-291` and `__TODO__/databases/mysql2.md:47-90`
      cover MySQL backup and restore tooling (`automysqlbackup`,
      `mysqldump` export/import of single, multiple, and all databases) —
      backup/restore administration. Flagged for the user to confirm or
      overrule.

- [ ] `__TODO__/databases/mysql2.md:1-44` covers MySQL/MariaDB version
      checking, connecting via the CLI, and listing databases at the
      `mysql>` prompt — client/CLI operation. Flagged for the user to confirm
      or overrule.

- [ ] `__TODO__/databases/_200-schema-less.md:1` is a stub titled "Schema-less
      data" containing only `TODO`. Schema-less / NoSQL data modelling likely
      belongs to TS-44 (Non-Relational Databases) rather than this relational
      standard; no extractable claims either way. Flagged for the user to
      confirm or overrule.

## Unresolved

- [ ] `__TODO__/SDCP-1065288521-290722-1004.pdf` is a binary PDF and could not
      be read; its claims are not included in the comparison. Not ingested.

- [ ] `__TODO__/databases/_todo/Data Engineering Cookbook.pdf` is a binary PDF
      and could not be read; its claims are not included in the comparison.
      Not ingested.

- [ ] `__TODO__/sql/0500-joins.md` references an image (`joins.jpg`) with no
      text content; the joins topic is covered by the MySQL JOIN tutorial URL
      and `__TODO__/sql2/_sql.md`, so no claims were lost, but the diagram
      itself was not extractable as text.

- [ ] `__TODO__/sql.md`, `__TODO__/sql2/_todo/9999-references.md`, and
      `__TODO__/databases/_todo/general-db-design.md` contain only lists of
      external links (Simon Holywell's SQL Style Guide, "SQL Joins Are Easy",
      "A Humble Guide to Database Schema Design", "Old, Good Database
      Design", Joe Celko's book). These are pointers to resources rather than
      content; no atomic claims were extracted from them. If you want these
      external resources themselves treated as references, list their URLs
      explicitly and a re-run will fetch them.