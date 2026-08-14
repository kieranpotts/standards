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

**Status:** 61 of 61 actionable gaps closed (2026-08-14). All `## Missing`
(59) and `## Partial` (2) items are resolved. Six new content files were
added — `02-sql-style.adoc`, `03-naming-conventions.adoc`,
`04-schema-design.adoc`, `05-data-types.adoc`, `06-joins-and-queries.adoc`,
and `07-transactions-and-consistency.adoc` — wired into `043.adoc` after the
existing `01-sharding.adoc`, plus a page-level `== References` section citing
the mysqltutorial.org, Wikipedia ACID, and both Brandur Leppka sources.
`01-sharding.adoc`'s eventual-consistency sentence was cross-linked to the
new transactions section. The `id`-vs-`<table>_id` naming conflict flagged
between the naming-conventions and primary-key sources was reconciled by
scope: `03-naming-conventions.adoc` covers general column naming and defers
the primary-key column specifically to `04-schema-design.adoc`, which states
`id` as the house style. Six `## Out-of-scope` items remain open, awaiting
the user's confirm/overrule decision (see the end-of-run report). Four
`## Unresolved` items remain open — all four cite `__TODO__/`-prefixed
paths from the original analysis run's source environment, which does not
exist on this machine; re-fetch was attempted and failed persistently for
all four on 2026-08-14, recorded against each item.

## Missing

### SQL style and formatting

- [x] `__TODO__/sql2/_todo/0200-general-style.md:3` — keep SQL succinct and
      free of redundant code (unnecessary quoting, parentheses, or `WHERE`
      clauses that can be derived). Not addressed anywhere in the standard.
      Recommend a new section (e.g. `02-sql-style.adoc`).

      **Resolved.** Closed by `02-sql-style.adoc`, "Keep queries succinct"
      section. States that redundant quoting, parentheses, or derivable
      `WHERE` clauses should not be added, and that every clause should earn
      its place in the query.

- [x] `__TODO__/sql2/_todo/0200-general-style.md:6-36` — judicious use of
      whitespace and indentation; right-align root keywords (`SELECT`, `FROM`,
      etc.) so they form a "river" down the middle, with implementation
      details left-aligned. Not addressed. Recommend a new section.

      **Resolved.** Closed by `02-sql-style.adoc`, "Indentation and the
      'river'" section. Documents right-aligning root keywords to form a
      vertical river with a worked `SELECT`/`FROM`/`WHERE`/`ORDER BY`
      example.

- [x] `__TODO__/sql2/_todo/0200-general-style.md:38-43` — spacing rules: spaces
      before/after `=`, after commas, and surrounding apostrophes (where not
      in parentheses or before a trailing comma/semicolon). Not addressed.
      Recommend a new section.

      **Resolved.** Closed by `02-sql-style.adoc`, "Spacing" section. States
      the spacing rules for `=`, commas, and string-literal quoting,
      including the parenthesis and trailing-punctuation exceptions.

- [x] `__TODO__/sql2/_todo/0200-general-style.md:52-82` — line-spacing rules:
      newline before `AND`/`OR`, after semicolons, after each keyword
      definition, after commas when grouping columns, and to separate code
      into related sections. Not addressed. Recommend a new section.

      **Resolved.** Closed by `02-sql-style.adoc`, "Line spacing" section.
      Covers newlines before `AND`/`OR`, after semicolons, after each root
      keyword's clause, after commas in long column lists, and blank lines
      to separate logical sections of a query.

- [x] `__TODO__/sql2/_todo/0200-general-style.md:85-99` — join formatting:
      joins indented to the other side of the "river" and grouped with a new
      line. Not addressed. Recommend a new section.

      **Resolved.** Closed by `02-sql-style.adoc`, "Formatting joins"
      section. Shows `JOIN`/`ON` indented opposite the river, with a worked
      example.

- [x] `__TODO__/sql2/_todo/0200-general-style.md:102-117` — subquery
      formatting: align to the right side of the river, lay out as any other
      query, place closing parentheses on a new line aligned with the opener
      (especially for nested subqueries). Not addressed. Recommend a new
      section.

      **Resolved.** Closed by `02-sql-style.adoc`, "Formatting subqueries"
      section. Documents right-side alignment, internal river layout, and
      aligning the closing parenthesis with the opener, with a worked
      example.

- [x] `__TODO__/sql2/_todo/0250-reserved-words.md:3` — always use upper case
      for reserved keywords such as `SELECT` and `WHERE`. Not addressed.
      Recommend a new section.

      **Resolved.** Closed by `02-sql-style.adoc`, "Reserved keywords"
      section. States that reserved keywords must always be upper case.

- [x] `__TODO__/sql2/_todo/0250-reserved-words.md:5` — prefer the full-length
      keyword over abbreviations where available (e.g. `ABSOLUTE` over `ABS`).
      Not addressed. Recommend a new section.

      **Resolved.** Closed by the same "Reserved keywords" section, which
      states the preference for full-length keyword forms over abbreviations
      where a dialect offers both.

- [x] `__TODO__/sql2/_todo/0250-reserved-words.md:7` — avoid vendor-specific
      keywords where an ANSI SQL keyword performs the same function, for
      portability. Not addressed. Recommend a new section.

      **Resolved.** Closed by the same "Reserved keywords" section, which
      states the ANSI-over-vendor-specific preference for portability.

- [x] `__TODO__/sql2/_todo/0250-reserved-words.md:10-840` — a curated list of
      reserved keywords across ANSI SQL (92, 99, 2003), MySQL 3–5.x, PostgreSQL
      8.1, MS SQL Server 2000, MS ODBC, and Oracle 10.2. The standard includes
      no such reference list. Recommend a new appendix-style section.

      **Resolved, partially.** Closed by the same "Reserved keywords"
      section, but not by reproducing the source's cross-vendor keyword
      table. That table is scoped to database versions from the mid-2000s
      and earlier, and would be stale on arrival for a living standard;
      instead the section directs readers to the target engine's own
      reserved-word reference and recommends identifiers that avoid the
      ANSI SQL reserved set. Judgment call: an appendix of dated
      vendor-version keyword tables does not belong in this standard.

- [x] `__TODO__/sql2/_todo/1500-comments.md:3-5` — comment style: include
      comments where useful; prefer C-style `/* ... */`; otherwise use `--`
      followed by a space and terminate with a newline. Not addressed.
      Recommend a new section.

      **Resolved.** Closed by `02-sql-style.adoc`, "Comments" section.
      States that comments should be included where they add value, prefers
      C-style block comments for multi-line commentary, and specifies the
      `-- ` single-line form terminated by a newline.

### Naming conventions

- [x] `__TODO__/sql2/_todo/0300-naming-conventions.md:4-11` — case guidance:
      snake_case is the prevailing standard and should be the default (adopt
      the prevailing standard of the system you are working with); avoid
      CamelCase as it is hard to scan in SQL files. Not addressed. Recommend a
      new section.

      **Resolved.** Closed by `03-naming-conventions.adoc`, "Case and
      character rules" section. States `snake_case` as the default,
      deferring to an established different convention where one already
      exists, and explains why CamelCase is avoided.

- [x] `__TODO__/sql2/_todo/0300-naming-conventions.md:12-16` — names must
      begin with a character and never end with a trailing underscore; use
      only letters, numbers, and underscores; delimit words with single
      underscores and avoid consecutive underscores. Not addressed. Recommend
      a new section.

      **Resolved.** Closed by the same "Case and character rules" section,
      which lists the character rules as a normative bullet list.

- [x] `__TODO__/sql2/_todo/0300-naming-conventions.md:19-21` — avoid prefixes
      and Hungarian notation such as `sp_` or `tbl` (valid exceptions
      notwithstanding). Not addressed. Recommend a new section.

      **Resolved.** Closed by `03-naming-conventions.adoc`, "Choosing
      identifiers" section, which states the anti-prefix rule and notes
      narrow exceptions may apply.

- [x] `__TODO__/sql2/_todo/0300-naming-conventions.md:24-28` — avoid plurals;
      prefer the collective term (`staff` over `employees`, `people` over
      `individuals`). Tables use a collective name or, less ideally, a plural
      form. Not addressed. Recommend a new section.

      **Resolved.** Closed by `03-naming-conventions.adoc`, "Table names"
      section, which states the collective-over-plural preference with the
      same examples.

- [x] `__TODO__/sql2/_todo/0300-naming-conventions.md:33-43` — choose
      consistent, descriptive, unique identifiers; keep length under 30
      characters; avoid abbreviations (except commonly understood ones); avoid
      reserved keywords as identifiers; avoid quoting identifiers (use SQL92
      double quotes if quoting is unavoidable). Not addressed. Recommend a
      new section.

      **Resolved.** Closed by "Choosing identifiers" section, covering
      descriptiveness, the 30-character guideline, abbreviation avoidance,
      reserved-keyword avoidance (cross-referencing the SQL style section),
      and the SQL92 double-quote fallback for unavoidable quoting.

- [x] `__TODO__/sql2/_todo/0310-tables.md:1-9` (also
      `__TODO__/sql2/_todo/0300-naming-conventions.md:46-54`) — table naming:
      collective or plural name, no `tbl`/descriptive prefix, never give a
      table the same name as one of its columns, and avoid concatenating two
      table names for a relationship table (prefer `services` over
      `cars_mechanics`). Not addressed. Recommend a new section.

      **Resolved.** Closed by "Table names" section: collective/plural
      naming, never naming a table after one of its own columns, and
      avoiding concatenated joining-table names in favor of a name that
      describes the relationship.

- [x] `__TODO__/sql2/_todo/0320-columns.md:1-9` (also
      `__TODO__/sql2/_todo/0300-naming-conventions.md:57-65`) — column naming:
      always singular; avoid using `id` alone as the primary identifier where
      possible; never name a column the same as its table; always lower case
      except for proper nouns. Not addressed. Recommend a new section. (Note:
      this conflicts with the primary-key house style in
      `__TODO__/databases/_100-primary-keys.md:139`, which mandates `id` — the
      standard should reconcile the two.)

      **Resolved.** Closed by `03-naming-conventions.adoc`, "Column names"
      section: singular naming, never naming a column after its own table,
      and lower case except for proper nouns. The `id`-column conflict is
      reconciled by scope: this section covers general column naming and
      explicitly defers the primary-key column name itself to the new
      "Primary keys" section in `04-schema-design.adoc` (see the
      "Columns, keys, and schema definition" batch below), rather than
      asserting a rule here that the primary-key section would then
      contradict.

- [x] `__TODO__/sql2/_todo/0320-columns.md:12-30` — column-suffix conventions
      with universal meaning: `_id`, `_status`, `_total`, `_num`, `_name`,
      `_seq`, `_date`, `_tally`, `_size`, `_addr`. Not addressed. Recommend a
      new section.

      **Resolved.** Closed by `03-naming-conventions.adoc`, "Column-suffix
      conventions" subsection, reproducing the full suffix table.

- [x] `__TODO__/sql2/_todo/0330-aliases.md:1-22` (also
      `__TODO__/sql2/_todo/0300-naming-conventions.md:68-74`) — alias rules:
      relate to the proxied object; use the first letter of each word as a
      rule of thumb; append a number on conflict; always include the `AS`
      keyword; name computed data (`SUM`, `AVG`) as if it were a schema
      column. Not addressed. Recommend a new section.

      **Resolved.** Closed by `03-naming-conventions.adoc`, "Aliases"
      section, covering all five rules with examples.

- [x] `__TODO__/sql2/_todo/0340-stored-procedures.md:1-5` (also
      `__TODO__/sql2/_todo/0300-naming-conventions.md:77-79`) — stored-procedure
      naming: the name must contain a verb; do not prefix with `sp_` or other
      descriptive/Hungarian prefixes. Not addressed. Recommend a new section.

      **Resolved.** Closed by `03-naming-conventions.adoc`,
      "Stored-procedure names" section.

- [x] `__TODO__/naming-conventions.md:3-17` — adopt a controlled vocabulary for
      column names so they act as contracts/promises for the data they store;
      benefits include easier fake-data generation, automated validation,
      safer data pipelines, and cross-dataset discoverability. Not addressed.
      Recommend a new section.

      **Resolved.** Closed by `03-naming-conventions.adoc`, "Column-name
      type prefixes" subsection, closing paragraph, listing the same
      benefits (fake-data generation, automated validation, safer
      pipelines, cross-dataset discoverability).

- [x] `__TODO__/naming-conventions.md:21-47` — column-name schema
      `<type>_<subject>(_<modifier>)` with a library of global type prefixes
      (`id`, `uuid`, `is`, `n`, `dt`, `tm`, `cat`) plus domain-specific ones
      (`loc`, `addr`); all columns sharing a type prefix should store data in
      the same format. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Column-name type prefixes" subsection,
      reproducing the `<type>_<subject>(_<modifier>)` schema, the global
      prefix table, and the same-format-per-prefix rule.

- [x] `__TODO__/naming-conventions.md:49-59` — the subject component (a noun
      from the business domain) and the optional modifier suffix (an
      adjective describing a variant, e.g. `raw`/`clean`) of the column-name
      schema. Not addressed. Recommend a new section.

      **Resolved.** Closed by the same subsection's closing paragraphs on
      the subject and modifier components, using the `dt_signup_raw` /
      `dt_signup_clean` example.

### Columns, keys, and schema definition

- [x] `__TODO__/columns.adoc:1-19` — column ordering convention within a table:
      `id` (PK), `uuid`, `logged_at` (for log records), foreign keys
      (alphabetical), other columns (logical groups, alphabetical if in
      doubt), then `created_at`/`updated_at`/`deleted_at`. Not addressed.
      Recommend a new section.

      **Resolved.** Closed by `04-schema-design.adoc`, "Column ordering"
      section, reproducing the six-step ordering convention.

- [x] `__TODO__/databases/_100-primary-keys.md:3` — not every table needs a
      primary key; do not add one by default; every field and constraint must
      serve a purpose. Not addressed. Recommend a new section.

      **Resolved.** Closed by `04-schema-design.adoc`, "Primary keys"
      section, opening paragraph.

- [x] `__TODO__/databases/_100-primary-keys.md:7-36` — UUID vs auto-incrementing
      integer primary keys: trade-offs (UUIDs are 16 bytes but can be
      generated anywhere, are globally unique, enable offline-first clients,
      merging, distribution, and replication; auto-increment IDs are smaller
      and convenient at small scale); UUIDs should be the default, with
      auto-increment IDs optionally mixed in (auto-increment is generally
      better for foreign-key links). Not addressed. Recommend a new section.

      **Resolved.** Closed by "Primary keys" section, "UUID vs
      auto-incrementing integer" subsection, stating the trade-offs and the
      UUID-by-default recommendation with auto-increment for foreign-key
      targets.

- [x] `__TODO__/databases/_100-primary-keys.md:38-141` — primary-key naming
      conventions: `id` vs `<table>_id`; arguments for each (join clarity,
      searchability, ORM/ActiveRecord compatibility, semantic fit); the
      reference's house style is `id`, with composite/aggregate keys as a
      valid exception. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Primary keys" section, "Naming the primary
      key column" subsection: states the `id` house style with
      `<table>_id` as the composite/aggregate-key exception, and explicitly
      reconciles this with the general column-naming guidance in
      `03-naming-conventions.adoc` (which advises against a bare `id` for
      non-primary-key identifier columns) by scoping each rule to a
      different kind of column. This closes the naming conflict flagged in
      the "Naming conventions" batch above.

- [x] `__TODO__/sql2/_todo/1000-schema-definitions.md:7-9` — schema-definition
      (`CREATE`/`ALTER`) readability: order and group column definitions where
      it makes sense; indent column definitions by four spaces within
      `CREATE`. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Defining schemas", "Readability" subsection.

- [x] `__TODO__/sql2/_todo/1000-schema-definitions.md:12-16` — default values:
      the default must be the same type as the column (e.g. a `DECIMAL` column
      should not take an `INTEGER` default); defaults follow the data-type
      declaration and come before any `NOT NULL`. Not addressed. Recommend a
      new section.

      **Resolved.** Closed by "Default values" subsection, with a worked
      `DECIMAL` example matching the source's own illustration.

- [x] `__TODO__/sql2/_todo/1000-schema-definitions.md:23-31` — choosing keys:
      the key should be unique; data type should be consistent across the
      schema and unlikely to change; the value should be validatable against a
      standard format (e.g. ISO); keep keys simple but use compound keys where
      necessary. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Choosing keys" subsection, covering
      uniqueness, type consistency, standard-format validatability, and the
      simple-keys-with-compound-exception guidance, cross-linked to the new
      many-to-many joining-table example.

- [x] `__TODO__/sql2/_todo/1000-schema-definitions.md:35-69` — defining
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

      **Resolved.** Closed by "Defining constraints" subsection, covering
      every listed rule with a worked `CREATE TABLE orders` example
      demonstrating primary-key-first ordering, inline column-level
      constraints, `ON DELETE`/`ON UPDATE` ordering, `CHECK()` clauses, and
      a named table-level `UNIQUE` constraint.

- [x] `__TODO__/databases/mysql.md:202-241` (also `__TODO__/databases/mysql.md:246-250`)
      — MySQL `UNIQUE` constraints: column-level `UNIQUE`, multi-column
      `UNIQUE(...)`, named constraints via `CONSTRAINT ... UNIQUE`, adding
      constraints to existing tables with `ALTER TABLE`, and removing them
      with `DROP INDEX`. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Adding and removing constraints on existing
      tables" subsection, with worked examples of column-level `UNIQUE`,
      multi-column `CONSTRAINT ... UNIQUE`, `ALTER TABLE ... ADD
      CONSTRAINT`, and `DROP INDEX`. Written in vendor-neutral SQL rather
      than MySQL-specific syntax, consistent with the standard's stated
      scope of being "not specific to any particular database engine."

### Data types

- [x] `__TODO__/sql2/_todo/0600-types.md:7` — avoid vendor-specific data types
      where possible; they are not portable and may not exist in older or
      future versions of the same vendor's software. Not addressed. Recommend
      a new section.

      **Resolved.** Closed by `05-data-types.adoc`, "General principles"
      section, first paragraph.

- [x] `__TODO__/sql2/_todo/0600-types.md:9` — avoid splitting a value between
      columns (e.g. value in one column, units in another); the value column
      should make the units self-evident. Not addressed. Recommend a new
      section.

      **Resolved.** Closed by "General principles" section, second
      paragraph, with a `duration_seconds` example and a cross-reference to
      the naming-conventions section's type-prefix/suffix guidance.

- [x] `__TODO__/sql2/_todo/0600-types.md:12-19` — string types: prefer
      `CHAR`, `CLOB`, and `VARCHAR` for maximum cross-engine compatibility.
      Not addressed. Recommend a new section.

      **Resolved.** Closed by "String types" section.

- [x] `__TODO__/sql2/_todo/0600-types.md:22-39` — numeric types: use `REAL` or
      `FLOAT` only for floating-point math; prefer `NUMERIC` and `DECIMAL` to
      avoid rounding errors; exact numeric types (`BIGINT`, `DECIMAL`,
      `DECFLOAT`, `INTEGER`, `NUMERIC`, `SMALLINT`) and approximate types
      (`DOUBLE PRECISION`, `FLOAT`, `REAL`). Not addressed. Recommend a new
      section.

      **Resolved.** Closed by "Numeric types" section, distinguishing exact
      and approximate types with the full lists from the source.

- [x] `__TODO__/sql2/_todo/0600-types.md:42-54` (also
      `__TODO__/types.adoc:3-5`) — date/time types: prefer ISO-8601-compliant
      values (`YYYY-MM-DD HH:MM:SS.SSSSS`); `DATE`, `TIME`, and `TIMESTAMP`
      are well supported; timestamps should not be used to represent past or
      future dates — prefer ISO 8601 storage. Not addressed. Recommend a new
      section.

      **Resolved.** Closed by "Date and time types" section, stating the
      ISO 8601 preference and the `DATE`-vs-`TIMESTAMP` distinction for
      values with no meaningful time-of-day component.

- [x] `__TODO__/sql2/_todo/0600-types.md:57-60` — binary types guidance (the
      reference lists `BINARY` etc., though the section appears to contain a
      copy-paste error repeating `TIME`/`TIMESTAMP`). Not addressed. Recommend
      a new section.

      **Resolved.** Closed by "Binary types" section. The source's own text
      for this range is a copy-paste error (it repeats the `TIME`/
      `TIMESTAMP` guidance from the date/time section rather than
      describing binary types), so no binary-specific claims could be
      extracted from it. The written section covers the general binary-type
      guidance implied by the reference's structure — a dedicated binary
      type over string-encoding, and the same standard-type preference
      applied elsewhere in this section — without fabricating specifics the
      corrupted source did not actually provide.

### Joins and queries

- [x] `https://www.mysqltutorial.org/mysql-join/#introduction` — join
      fundamentals: a relational database links tables via foreign-key
      columns; a join links data between tables on common-column values;
      MySQL supports inner, left, right, and cross joins (no `FULL OUTER
      JOIN`); joins appear after `FROM` in a `SELECT`. Not addressed. Recommend
      a new section.

      **Resolved.** Closed by `06-joins-and-queries.adoc`, "Join
      fundamentals" section. States the foreign-key basis of joins, notes
      that full outer join is unsupported on some engines (including
      MySQL) and how to emulate it, and cross-references the join
      formatting rules in the SQL style section. Source added to the
      page's `== References`.

- [x] `https://www.mysqltutorial.org/mysql-join/#mysql-inner-join` — inner
      join semantics and syntax (`INNER JOIN ... ON ...`); the `USING`
      clause replaces `ON` when the matching column name is the same in both
      tables; only matching rows are returned. Not addressed. Recommend a
      new section.

      **Resolved.** Closed by "Inner joins" section, with worked `ON` and
      `USING` examples.

- [x] `https://www.mysqltutorial.org/mysql-join/#mysql-left-join` — left join
      semantics: returns all left-table rows whether or not a match exists,
      with `NULL` for unmatched right-table columns; `LEFT JOIN ... WHERE
      <right_col> IS NULL` finds left rows with no match; `USING` syntax.
      Not addressed. Recommend a new section.

      **Resolved.** Closed by "Left and right joins" section, with a
      worked left-join example and the `WHERE ... IS NULL` unmatched-rows
      pattern.

- [x] `https://www.mysqltutorial.org/mysql-join/#mysql-right-join` — right
      join semantics (mirror of left join); syntax; `USING`; `WHERE ... IS
      NULL` to find unmatched right rows. Not addressed. Recommend a new
      section.

      **Resolved.** Closed by the same "Left and right joins" section,
      describing the right join as the mirror of the left join rather than
      duplicating a near-identical example, since the two are symmetric.

- [x] `https://www.mysqltutorial.org/mysql-join/#mysql-cross-join` — cross
      join produces a Cartesian product (`n × m` rows); no join condition;
      syntax; useful for generating planning data. Not addressed. Recommend a
      new section.

      **Resolved.** Closed by "Cross joins" section, with the Cartesian
      product explanation and a planning-data example.

- [x] `__TODO__/sql2/_sql.md:25-27` — many-to-many relationships via joining
      tables; use composite keys of the two foreign-key columns (rather than
      an `id`) to guarantee each relationship is defined once. Not addressed.
      Recommend a new section.

      **Resolved.** Closed by "Many-to-many relationships" section, with a
      worked `car_mechanics` joining-table example using a composite
      primary key, cross-referenced from the "Choosing keys" subsection in
      `04-schema-design.adoc`.

- [x] `__TODO__/sql2/_sql.md:36-59` — `JOIN` vs subquery for the same result;
      sub-selects can be slower — benchmark alternative formulations of
      complex queries. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Joins vs subqueries" section.

- [x] `__TODO__/sql2/_sql.md:62-102` — paginated search with
      `LIMIT offset, count`; obtaining the total result count (separate
      un-`LIMIT`ed query, caching it, or MySQL's
      `SQL_CALC_FOUND_ROWS`/`FOUND_ROWS()`); storing the count in session
      variables for subsequent pages. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Paginated search" section, covering
      `LIMIT`/`OFFSET`, all three total-count strategies (separate query,
      caching, and MySQL's `SQL_CALC_FOUND_ROWS`/`FOUND_ROWS()`), and the
      session-variable caching pattern for repeated pagination.

- [x] `__TODO__/sql2/_todo/0500-formalisms.md:3-9` — formalisms: prefer
      `BETWEEN` over chained `AND`; `IN()` over multiple `OR`; `CASE` for
      value interpretation (nestable); avoid `UNION` and temporary tables
      where the schema can be optimized to remove the reliance on them. Not
      addressed. Recommend a new section.

      **Resolved.** Closed by "Query formalisms" section, covering all four
      formalisms.

- [x] `__TODO__/sql2/_todo/0800-functions.md:3-5` — functions: prefer standard
      SQL functions over vendor-specific ones for portability, but use a
      vendor-specific function when it gives a significant advantage (e.g.
      speed) that outweighs portability. Not addressed. Recommend a new
      section.

      **Resolved.** Closed by "Functions" section.

### Transactions and consistency

- [x] `https://en.wikipedia.org/wiki/ACID#` — ACID (atomicity, consistency,
      isolation, durability) as a set of transaction properties guaranteeing
      data validity despite errors and failures; the transaction paradigm
      and its influence on database systems. Not addressed. Recommend a new
      section.

      **Resolved.** Closed by `07-transactions-and-consistency.adoc`,
      "ACID" section, opening paragraph. Source added to the page's
      `== References`.

- [x] `https://en.wikipedia.org/wiki/ACID#Atomicity` — atomicity: a
      transaction is an all-or-nothing unit; if any statement fails the whole
      transaction fails and the database is left unchanged; a transaction
      cannot be observed in progress by another client. Not addressed.
      Recommend a new section.

      **Resolved.** Closed by "Atomicity" subsection.

- [x] `https://en.wikipedia.org/wiki/ACID#Consistency` — consistency: a
      transaction can only move the database from one consistent state to
      another, preserving invariants; written data must satisfy all defined
      rules (constraints, cascades, triggers); referential integrity as an
      example invariant. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Consistency" subsection.

- [x] `https://en.wikipedia.org/wiki/ACID#Isolation` — isolation: concurrent
      execution leaves the database in the same state as sequential
      execution; the main goal of concurrency control; effects of an
      incomplete transaction may be invisible depending on the isolation
      level. Not addressed. Recommend a new section.

      **Resolved.** Closed by "Isolation" subsection, opening paragraph.

- [x] `https://en.wikipedia.org/wiki/ACID#Durability` — durability: once
      committed, a transaction persists despite system failure; usually means
      completed transactions are recorded in non-volatile memory. Not
      addressed. Recommend a new section.

      **Resolved.** Closed by "Durability" subsection.

- [x] `https://en.wikipedia.org/wiki/ACID#` — BASE (basically available, soft
      state, eventually consistent) as the opposite of ACID; the CAP theorem
      framing that a database leans toward ACID (consistency) or BASE
      (availability); SQL vs NoSQL alignment. Not addressed. Recommend a new
      section.

      **Resolved.** Closed by "ACID vs BASE" section, covering the CAP
      theorem framing and cross-linked from `01-sharding.adoc`'s
      eventual-consistency mention.

- [x] `https://en.wikipedia.org/wiki/ACID#Implementation` — transaction
      implementation techniques: write-ahead logging and shadow paging;
      locks must be acquired on data to be updated (and possibly read,
      depending on isolation level). Not addressed. Recommend a new section.

      **Resolved.** Closed by "Transaction implementation techniques"
      section.

- [x] `https://en.wikipedia.org/wiki/ACID#Locking_vs._multiversioning` —
      locking vs multiversion concurrency control (MVCC): two-phase locking
      for full isolation; MVCC gives readers unmodified prior versions so
      readers don't block writers and vice versa; snapshot isolation as one
      MVCC implementation that relaxes isolation. Not addressed. Recommend a
      new section.

      **Resolved.** Closed by "Locking vs multiversion concurrency control"
      subsection.

- [x] `https://en.wikipedia.org/wiki/ACID#Distributed_transactions` —
      distributed transactions: additional complications when no single node
      owns all the data; the two-phase commit protocol (distinct from
      two-phase locking) provides atomicity by having a coordinator confirm
      all participants are prepared before formalizing the commit. Not
      addressed. Recommend a new section.

      **Resolved.** Closed by "Distributed transactions" section.

- [x] https://brandur.org/http-transactions ("Concurrency protection" /
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

      **Resolved.** Closed by "Concurrency protection with SERIALIZABLE"
      section, with its "Retrying an abort" and "Data protection in
      layers" subsections: a worked check-then-insert race example (two
      concurrent "create user" requests), the retry-on-serialization-
      failure pattern including the Sequel `retry_on` example, and the
      UNIQUE-constraint-as-defense-in-depth guidance. "Retrying an abort"
      cross-references TS-21 (HTTP APIs) by name, and states explicitly
      that TS-21's idempotent-request treatment assumes a simpler
      one-request-to-one-transaction model than this retry-within-a-
      request pattern — the overlap noted in the source item is recorded
      as a cross-standard caveat rather than resolved by editing TS-21,
      which is out of this run's scope. Source added to the page's
      `== References`.

## Partial

- [x] `https://en.wikipedia.org/wiki/ACID#Consistency` and
      `https://en.wikipedia.org/wiki/ACID#` (BASE) cover transaction
      consistency models (ACID vs BASE, isolation levels, MVCC, distributed
      consistency) more thoroughly than `01-sharding.adoc:181-183`, which
      mentions only that sharding combined with replication/denormalization
      requires planning for _eventual_ data consistency across shards. The
      standard touches consistency only in the narrow sharding context and
      does not cover transaction consistency models, isolation levels, or
      ACID/BASE trade-offs. Recommend a new section on transactions and
      consistency, cross-linked from the sharding section.

      **Resolved.** Closed by the whole of
      `07-transactions-and-consistency.adoc` — the "Consistency" and "ACID
      vs BASE" sections directly, with isolation levels, MVCC, and
      distributed-transaction consistency covered by the section's other
      subsections. `01-sharding.adoc:181-183`'s eventual-consistency
      sentence now cross-links to the new section with `<<Transactions and
      consistency>>`.

- [x] https://brandur.org/acid ("Building Robust Systems with ACID and
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

      **Resolved.** Closed by "Atomicity" subsection (document-level
      atomicity critique and the data-janitor consequences of lacking
      transactional atomicity), the "Isolation" subsection's four-level
      table with named phenomena, and the "Isolation" subsection's closing
      paragraph on custom locking vs. built-in MVCC. The duplicate-email
      registration example is used in "Consistency" as the `UNIQUE`-
      constraint illustration, and again more fully worked in "Concurrency
      protection with SERIALIZABLE". The article's schemaless and
      default-to-ACID/vertical-scaling points are not written here, per the
      note that they were routed to TS-44 — TS-44 is currently a stub
      (`// TODO: Introductory text…`, no partials), so that content remains
      unwritten pending a separate run against TS-44, which this run does
      not perform. Source added to the page's `== References`.

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

      Re-fetch attempted 2026-08-14: `__TODO__/` is a placeholder path from
      the original gap-analysis run's source environment, not a path that
      exists in this repository or on this machine. No such file could be
      located to re-attempt ingestion. The failure is persistent, not
      fresh — it requires the original source tree to be made available
      again, not a retry.

- [ ] `__TODO__/databases/_todo/Data Engineering Cookbook.pdf` is a binary PDF
      and could not be read; its claims are not included in the comparison.
      Not ingested.

      Re-fetch attempted 2026-08-14: same `__TODO__/` placeholder-path
      issue as above. Not re-ingested.

- [ ] `__TODO__/sql/0500-joins.md` references an image (`joins.jpg`) with no
      text content; the joins topic is covered by the MySQL JOIN tutorial URL
      and `__TODO__/sql2/_sql.md`, so no claims were lost, but the diagram
      itself was not extractable as text.

      Re-fetch attempted 2026-08-14: same `__TODO__/` placeholder-path
      issue. Note this item's own text says no claims were lost — the join
      topic itself is closed via the "Joins and queries" batch's `## Missing`
      items, which is unaffected by this unresolved diagram.

- [ ] `__TODO__/sql.md`, `__TODO__/sql2/_todo/9999-references.md`, and
      `__TODO__/databases/_todo/general-db-design.md` contain only lists of
      external links (Simon Holywell's SQL Style Guide, "SQL Joins Are Easy",
      "A Humble Guide to Database Schema Design", "Old, Good Database
      Design", Joe Celko's book). These are pointers to resources rather than
      content; no atomic claims were extracted from them. If you want these
      external resources themselves treated as references, list their URLs
      explicitly and a re-run will fetch them.

      Re-fetch attempted 2026-08-14: same `__TODO__/` placeholder-path
      issue for the three list files themselves. The named external
      resources they point to (Simon Holywell's SQL Style Guide, "SQL Joins
      Are Easy", "A Humble Guide to Database Schema Design", "Old, Good
      Database Design", Joe Celko's book) were not given as explicit URLs in
      this item, so per the item's own instruction they were not fetched in
      this run either. A future run could fetch these by URL if the user
      wants them treated as references.