# TS-45: Data Migrations

A data migration is the controlled movement of data from one
representation, schema, system, or storage location to another. It is one
of the higher-risk operations in software engineering: data cannot be
re-created from source, and a migration touches it directly while the
surrounding system continues to operate.

This standard covers the principles, strategies, and practices for
planning, executing, validating, and rolling back data migrations. It
treats two operations as distinct, because conflating them is the most
common source of migration failures:

1. **Data migration** — transforming and copying data into its new
   representation.
2. **Switch-over enablement** — pointing the live system at that new
   representation.

Migrating the data and enabling the switch-over are independent
operations. The data can be migrated long before the switch-over, and the
switch-over can be rehearsed, deferred, or rolled back without
re-migrating anything. Keeping them separate is a core principle of this
standard.

Use this when planning or executing any operation that moves or
transforms live data into a new representation: schema refactors, storage-
or platform migrations, system-to-system replacements, data-model changes.

Do NOT use this for routine data ingestion or ETL pipelines feeding
downstream analytics, or for backup/restore as a disaster-recovery
activity (techniques overlap but the use cases differ). For database
engine and schema specifics, see
[TS-43: Relational Databases and SQL](../043/AGENTS.md) and
[TS-44: Non-Relational (NoSQL) Databases](../044/AGENTS.md). For release
and cutover mechanics, see [TS-10: Releasing](../010/AGENTS.md). For the
migration plan as a documentation artifact, see
[TS-3: Design Docs](../003/AGENTS.md) and
[TS-25: Technical Documentation](../025/AGENTS.md).

## Rules

### Principles

- **Every migration step SHOULD be reversible.** A reversible step can be
  undone without data loss and without depending on state the step itself
  destroyed. Migrations SHOULD preserve the source representation, intact
  and writable, until the target is validated and the switch-over is
  stable (typically through a defined soak period). Where a step is
  genuinely irreversible (eg. a destructive type coercion that loses
  information), it MUST be identified explicitly in the plan, gated on
  validation of preceding steps, and executed only when forward-fix is
  acceptable.

- **Migration steps SHOULD be idempotent.** Running a step twice, or
  against partially-completed state, MUST produce the same result as
  running it once. Migration logic SHOULD key off the source data and the
  target's existing state, not off a separate "what has been processed"
  record. Resume-by-replay is more robust than resume-by-checkpoint.

- **A migration MUST be testable before it runs against production.**
  Migration logic MUST be separable from the production data path, runnable
  against a representative copy of the source, and instrumented well enough
  to verify its result.

- **Migrations MUST be observable independently of the application.**
  Progress, throughput, error rate, and lag signals MUST be visible to the
  operator on duty and separated from application telemetry so a migration
  failure is not lost in the application's noise.

- **Migrations SHOULD minimize blast radius.** Batched processing,
  per-tenant or per-shard isolation, and feature-gated switch-overs all
  reduce the scope of a single failure.

- **Data integrity takes precedence over schedule, downtime, and cost.**
  A migration that compromises integrity to meet a deadline has failed,
  even if it appears to have completed.

- **The data migration and the switch-over are separate concerns.** They
  are planned, executed, validated, and rolled back on independent
  schedules. Conflating them is a defect in the plan, not an
  optimization. The plan SHOULD be structured as two phases with a clear
  gate between them: data migrated and validated first, then switch-over
  proceeds on its own schedule with its own rollback plan.

### Types and cutover profiles

- **Schema migration.** Changes the structure of data within the same
  storage system (add/remove/rename columns or tables, split/merge
  records, change types/constraints/indexes, repartition). Most common and
  automatable; usually handled by a versioned migration tool with forward
  and reverse delta scripts.

- **System migration.** Moves data from one system to another (legacy to
  replacement, or between implementations of the same service contract).
  Higher-risk because the two systems can drift while the migration is in
  flight and correctness cannot be reduced to a schema diff.

- **Storage / platform migration.** Changes where or how data is
  physically stored without changing its logical representation (different
  engine, partitioning scheme, cloud region, self-managed to managed).
  Engine-specific behaviors (collation, ordering, precision, encoding) can
  produce subtle incompatibilities.

- **Format migration.** Changes the serialization or encoding of data in
  place or in transit. Usually a special case of schema migration and
  SHOULD be handled with the same expand-and-contract discipline.

- **Choose the cutover profile explicitly in planning.** Each migration
  has a cutover profile that determines switch-over mechanics:
  - **Big-bang.** Source quiesced, migration completes, target enabled in
    one step. Simplest; highest downtime; highest blast radius.
  - **Phased.** Migration and switch-over proceed in batches (by tenant,
    key range, feature). Lower risk per step; more operational complexity.
  - **Zero-downtime.** Source and target run in parallel; switch-over
    occurs without service interruption. Most complex; required when the
    system cannot be taken offline.

  The choice of cutover profile SHOULD be justified against the system's
  availability requirements.

### Planning

- **Plan before writing code.** The plan is the artifact that survives
  the migration and the document an operator reaches for at 03:00. It
  SHOULD be written down, reviewed, and stored alongside the code.

- **Discovery and inventory.** Before designing the migration, the team
  MUST establish:
  - The source data set — volume, growth rate, distribution, known
    anomalies or historical corruption.
  - The schema and constraints at the source, including constraints
    enforced only by application code.
  - External dependencies — downstream consumers, upstream producers,
    foreign keys into and out of the data, integrations that assume a
    specific representation.
  - Access patterns and load, steady-state and peak, against source and
    anticipated target.

- **Mapping and transformation rules.** Every field, record, and
  relationship in the source MUST have a defined target. The mapping
  SHOULD be explicit and reviewable, including:
  - Field-to-field correspondence (fields dropped, split, merged, derived,
    synthesized).
  - Type coercions and their failure modes.
  - Encoding, collation, and timezone handling.
  - Identity and referential integrity — how primary and foreign keys map
    across the migration; how dangling references are handled.

- **Sizing and timing.** The plan MUST estimate wall-clock duration and
  resource cost on production-class hardware using a representative data
  sample. A migration that cannot complete within an available window
  MUST be designed as phased or zero-downtime, not big-bang.

- **Risk and impact assessment.** For each step, the plan SHOULD identify
  what can go wrong, how it will be detected, what the rollback is and what
  it costs, and who is responsible for the rollback-vs-forward-fix
  decision.

- **The cutover plan is separate from the migration.** It SHOULD specify:
  - The exact sequence of enablement steps (reads first, then writes, or
    both; per-tenant or all-at-once).
  - The feature flags or configuration that gate each step.
  - The validation that gates progression between steps.
  - The rollback procedure, including the conditions under which it is
    invoked and who is authorized to invoke it.
  - The communications plan — who is notified, when, through what channel.

  The cutover plan MUST be executable independently of the migration — it
  can be run, fully, against a target populated by a previous migration
  run, without re-running the migration.

### Strategies

- **Big-bang migration.** Source quiesced; data copied/transformed into
  target in one pass; switch-over enabled against the fully-populated
  target. Simplest to design and validate; highest downtime; failure
  during migration leaves the system down until rollback completes.
  Rollback is cheap provided the source was not modified. SHOULD be
  reserved for cases where the downtime cost is genuinely lower than the
  engineering cost of a phased or zero-downtime alternative.

- **Phased migration.** Data partitioned by a stable sharding key (tenant,
  key range, region, feature); each partition migrated and switched over
  independently while the rest of the system continues against the source.
  Requires per-partition routing and a registry of which partitions have
  migrated. Rollback is per-partition — a failed partition can be routed
  back to source while others continue.

- **Zero-downtime (dual-write, backfill, verify, switch).** For systems
  that cannot be taken offline. Proceeds in stages:
  1. **Expand.** Introduce the target schema/system alongside source,
     without directing any traffic to it.
  2. **Dual-write.** Write new/updated records to both source and target.
     Source remains system of record; target writes are additive and MUST
     NOT block or fail the request.
  3. **Backfill.** Copy existing source data into target in the
     background, in idempotent batches, reconciling continuously with the
     dual-written stream so the target converges on the source.
  4. **Verify.** Compare source and target exhaustively or by sampling
     until demonstrably consistent.
  5. **Switch reads.** Direct reads to the target, starting with a small
     fraction and ramping. Both source and target continue to receive
     writes.
  6. **Switch writes.** Stop writing to source; target becomes system of
     record.
  7. **Contract.** Remove the source, or keep it as read-only fallback
     during a soak period.

  Each stage is independently reversible. Cost of rollback rises sharply
  once "switch writes" has executed. The dual-write path is the
  failure-prone part — edge cases (out-of-order writes, retries, partial
  failures, idempotency keys, interaction with backfill) are where
  correctness is won or lost. The dual-write path SHOULD be exercised
  against production traffic in shadow mode before it is relied upon.

- **Default to the simplest strategy that meets the availability
  requirement.** Zero-downtime is a tool for when the simpler strategies
  cannot meet the constraint, not a badge of sophistication.

### Schema changes

- **Schema changes MUST be deployable without downtime and reversibly.**
  The fundamental pattern is **expand-and-contract** (parallel change).
  Decompose a schema change into a sequence of smaller, independently
  deployable and reversible steps:
  1. **Expand.** Add new schema elements alongside the old; both
     representations coexist. Application writes to both, reads from the
     old.
  2. **Migrate.** Backfill the new representation from the old, in the
     background, idempotently.
  3. **Switch.** Deploy a version that reads from the new representation;
     both representations are still written to.
  4. **Contract.** Stop writing to the old representation; after a soak
     period, remove the old schema elements.

  Each step is independently deployable and reversible. A failed step is
  rolled back to the previous step, not to the start of the migration.

- **Never combine expand and contract in a single deploy.** A change
  that adds the new column, backfills it, switches reads to it, and drops
  the old column in one release is a big-bang migration in disguise — it
  has the downtime and rollback profile of one.

- **Application code MUST be compatible with every schema state it can
  encounter.** During expand, the application MUST tolerate the new
  representation being absent or present-but-empty. During switch, it
  MUST tolerate both representations present. During contract, it MUST
  tolerate the old representation being absent. Heuristic: any application
  version SHOULD be compatible with the schema state produced by one
  schema change forward or backward from the state it was deployed
  against.

- **Forward and backward compatibility.** A schema change is backward
  compatible if the new schema can serve old application versions, and
  forward compatible if the old schema can serve new application
  versions. Both SHOULD hold during an expand-and-contract migration so
  schema and application can deploy in either order. Where forward
  compatibility is not achievable, the migration MUST sequence deployments
  to preserve correctness (expand → application → contract) and MUST
  state this ordering explicitly in the plan.

- **Prefer online schema change tooling.** For relational databases, use
  tooling that performs the change without holding long-running exclusive
  locks (native online DDL, `gh-ost`, `pt-online-schema-change`, Spirit, or
  equivalents). For non-relational stores, the equivalent is a managed
  index rebuild or re-partition that does not block the live workload.
  Online tooling does not relax the expand-and-contract discipline — even
  an online `ALTER` SHOULD be deployed in isolation from the application
  changes that depend on it.

- **Use versioned migration scripts.** Schema changes SHOULD be applied
  through a versioned migration tool that records each change as an
  ordered, timestamped delta script with a paired reverse script. A
  reverse script SHOULD accompany every forward script. Where a change is
  genuinely irreversible, the reverse script MUST be a no-op that emits a
  clear warning, and the irreversibility MUST be flagged in the plan.

### Execution and cutover

- **Run the migration as a monitored, controllable process.** Not
  fire-and-forget. Specifically:
  - **Resumable.** The migration MUST be resumable after an interruption,
    without re-processing completed work and without losing in-flight
    work.
  - **Throttled.** The migration MUST be rate-limited to protect the live
    system from resource contention and to stay within source and target
    throughput limits. Throttling SHOULD be tunable at runtime without
    restarting.
  - **Pausable.** The operator on duty MUST be able to pause and resume
    without intervention from the migration's author.
  - **Logged.** Every batch, every error, every retry MUST be logged with
    enough context to identify the affected records.

- **Process in small idempotent batches.** For very large data sets, the
  migration SHOULD process work in small, idempotent batches keyed off the
  source data (eg. by primary key range) so a batch can be retried,
  skipped, or inspected in isolation. Batch size SHOULD make a single
  batch's failure a recoverable event, not a migration-wide incident.

- **Idempotency in execution.** Writes to the target MUST be upserts
  keyed off the source data, not inserts keyed off a separate processing
  log. The migration MUST tolerate records that already exist in the
  target (created by a previous run) and update them to match the source
  rather than failing.

- **Switch-over is a separate operation.** Once the target is populated
  and validated, the switch-over is planned and executed as its own
  operation — it does not migrate data, it directs the live system to the
  data the migration has already placed. The switch-over SHOULD be
  staged, with each stage gated on validation:
  1. **Read switch.** Direct a fraction of read traffic to the target;
     ramp up. Source and target remain writable.
  2. **Write switch.** Stop writing to source; target becomes system of
     record.
  3. **Soak.** Run with the target as system of record, source preserved
     as fallback, for a defined period (typically days, not hours).
  4. **Decommission.** After soak, retire the source.

  Each stage is independently reversible, at declining cost. Reversing
  the read switch is cheap. Reversing the write switch is expensive but
  possible, provided the source remained writable. Decommissioning the
  source is the point of no return.

- **Rehearse the cutover.** The cutover plan SHOULD be rehearsed
  end-to-end against a non-production environment before execution. The
  rehearsal uses the same runbook, feature flags, and validation gates
  against a target populated by a prior migration run. A rehearsal that
  cannot complete is a strong signal that the production cutover is not
  ready.

- **Communicate on a defined schedule.** A migration and its cutover
  SHOULD be communicated to stakeholders — service owners, on-call
  engineers, downstream consumers — including the planned window,
  expected impact, validation criteria, and conditions under which the
  migration will be paused or rolled back.

### Validation

- **Validation is the gate between migration and switch-over.** The
  switch-over MUST NOT proceed until validation has passed. Validation is
  a precondition for switch-over, not a step in it.

- **Validation SHOULD establish, at minimum:**
  - **Completeness.** Every record that should be in the target is in the
    target; every record in the target corresponds to a record in the
    source (or a defined transformation of one).
  - **Correctness.** Each field in the target holds the value that the
    mapping and transformation rules dictate for the corresponding source
    record.
  - **Integrity.** Every constraint — primary keys, foreign keys,
    uniqueness, application-level invariants — holds in the target.
  - **Consistency under concurrency.** For zero-downtime migrations, the
    target reflects every source write acknowledged up to a defined point
    in time, and the lag between source and target is bounded and known.

- **Combine multiple validation techniques.** A single check —
  particularly a row count — is not validation. Techniques:

  | Technique | What it establishes |
  |---|---|
  | Row count | Coarse completeness. Necessary, never sufficient. |
  | Checksum / hash aggregate | Stronger completeness + correctness over a subset of fields. Sensitive to ordering and encoding. |
  | Record-level diff | Field-level correctness, by comparing source and target records pairwise. Expensive at full scale; typically sampled. |
  | Referential integrity check | Every foreign key in the target resolves. Catches orphaned records and broken mappings. |
  | Reconciliation against independent source | Target agrees with a third system (billing ledger, audit log, analytics warehouse) that does not depend on source or target. |
  | Replay verification | For zero-downtime: replaying a captured stream of source writes against the target produces the same result the live dual-write path produced. |

- **Validation MUST include at least one correctness check, not only a
  completeness check.** Migrations have shipped with matching row counts
  and systematically wrong field values.

- **Sampling rules.** Where full record-level diffing is impractical:
  - The sample SHOULD be stratified across the key space, not from the
    first N records.
  - The sample SHOULD explicitly include known edge cases: largest
    records, oldest records, records with unusual encodings, records
    that exercised known bug-fix paths in the source.
  - The sampling rate SHOULD be high enough that a systematic error in a
    large sub-population would be detected with high confidence.
  - A sample that passes does not prove correctness; it raises
    confidence. The decision to switch over on the basis of a sample
    SHOULD be recorded, with the sampling design and residual risk, in
    the migration plan.

- **Continuous validation for zero-downtime migrations.** Source and
  target SHOULD be continuously compared — by checksum, sampling,
  reconciliation — through the dual-write and backfill phases, and
  divergence SHOULD be monitored. Rising divergence is an early signal
  that the dual-write path is losing writes.

- **Validation runs SHOULD be reproducible and timestamped.** The
  switch-over plan SHOULD reference validation results by name (eg.
  "switch-over is gated on a passing validation run identified by
  `<id>`") so the gate is auditable after the fact.

### Rollback and recovery

- **Two distinct rollbacks.** Keeping migration and switch-over separate
  yields two rollback operations with very different costs:
  - **Switch-over rollback.** Repoint the live system from target back to
    source. Cheap and fast, provided the source has remained writable and
    current. This is the rollback that should be on call during cutover.
  - **Migration rollback.** Undo the migration itself — restore the
    source representation the migration modified or destroyed, or revert
    the target to pre-migration state. Expensive, slow, sometimes
    impossible.

  The plan SHOULD prefer designs in which the cheap rollback
  (switch-over) is the one needed in the common case. This is the
  principal reason to keep the source writable and intact through the
  switch-over and into the soak period.

- **Backups and point-in-time recovery.** A migration that will modify or
  destroy the source MUST take a verified backup of the source before it
  begins, and MUST confirm the backup is restorable — not merely that it
  was written. A backup that has not been tested for restore is not a
  rollback plan. For time-sensitive migrations, point-in-time recovery
  (PITR) SHOULD be enabled on both source and target so either can be
  restored to a known instant.

- **Forward-fix vs. rollback.** Not every failure should trigger
  rollback. A migration at 95% with a correct target and a single broken
  batch is often better served by fixing the batch than reverting the
  whole migration. The plan SHOULD state, for each step, the conditions
  for rollback vs. forward-fix, and identify who is authorized to make
  that call. Heuristic: roll back when the failure is systematic or
  unknown; forward-fix when the failure is localized, understood, and
  bounded.

- **Irreversible steps.** A genuinely irreversible step (destructive type
  coercion, column drop without backup, source decommission) MUST be:
  - Identified explicitly in the plan, in advance.
  - Gated on successful validation of every preceding step.
  - Executed only when the cost of a forward-fix is acceptable — never as
    a routine part of the migration.
  - Recorded, with the identity of the approver and the reasoning, in the
    migration's audit log.

### Testing

- **A migration MUST be tested before it runs against production.**
  Testing a migration is distinct from testing the application that uses
  the data. A migration test suite SHOULD cover:
  - **Transformation correctness.** Each mapping/transform rule exercised
    against representative source values — nulls, empty strings, unicode,
    max-length fields, out-of-range values, known historical anomalies.
  - **Edge cases.** Boundary values, empty and single-record data sets,
    records that violate soft constraints, records that exercise every
    branch of the transformation logic.
  - **Idempotency.** Running the migration twice produces the same result
    as running it once, including against partially-populated targets.
  - **Resumability.** Interrupting the migration at representative points
    and resuming it completes correctly, without re-processing or losing
    work.
  - **Failure handling.** A failure in a batch, a connectivity loss to
    source or target, and a partial write to the target are handled
    without corrupting target state.
  - **Performance and resource cost.** Throughput, memory, and
    contention profile on production-class hardware against a realistic
    data volume.

- **Test against a copy of production data, not synthetic data alone.**
  Synthetic data rarely reproduces the anomalies, distributions, and
  scale that break migrations. The test environment SHOULD match
  production in the dimensions that affect the migration: storage engine
  version, schema, indexes, partitioning, data volume and distribution.
  Where a full-size copy is impractical, a stratified representative
  subset is preferable to synthetic data.

- **Shadow runs for zero-downtime migrations.** Before running against
  production, the dual-write path SHOULD be exercised in shadow mode —
  writes duplicated to the target, but the target is not read by the live
  system and the duplication cannot affect the request path. Shadow
  running surfaces dual-write bugs under real load.

- **Dry runs for big-bang and phased migrations.** A full end-to-end dry
  run against a full copy of the source SHOULD be performed, including
  validation, to confirm the migration completes within its budget and
  produces a validated target.

- **Rehearse the cutover end-to-end** against a non-production
  environment populated by a previous migration run, using the same
  runbook, feature flags, and validation gates as the production
  cutover.

### Observability

- **A migration MUST be observable independently of the application.**
  For the general principles, see
  [TS-57: Logging, Monitoring, Observability](../057/AGENTS.md). What is
  specific to migrations:

- **Migration-specific signals.** A migration SHOULD emit, at minimum:
  - **Progress.** Records processed, records remaining, percentage
    complete.
  - **Throughput.** Records per unit time, with a baseline so degradation
    is detectable.
  - **Error rate.** Errors per batch and per record, categorized so
    transient errors (retried) are distinguished from terminal errors
    (skipped or failed).
  - **Lag.** For zero-downtime migrations, the time between a write being
    acknowledged at source and the corresponding write applied at target.
    Lag SHOULD be bounded and the bound SHOULD be alerted on.
  - **Resource utilization.** CPU, memory, I/O, lock contention on source
    and target, attributed to the migration, so contention with the live
    workload is detectable.
  - **Divergence.** For zero-downtime migrations, the divergence between
    source and target as measured by continuous validation. Rising
    divergence is the leading indicator of a dual-write bug.

- **Separate dashboards.** Migration signals SHOULD be presented on
  their own dashboard, distinct from application dashboards.

- **Alerting.** Alerting on a migration SHOULD be calibrated to its
  operational profile:
  - A stalled migration (no progress for a defined interval) SHOULD
    alert.
  - A rising error rate or rising divergence SHOULD alert, with a
    threshold below the level at which the migration's correctness is in
    doubt.
  - A lag breach (lag exceeding the defined bound) SHOULD alert, and
    SHOULD be treatable as a cutover-blocking condition.
  - Resource contention with the live workload SHOULD alert, and SHOULD
    be treatable as a trigger to throttle or pause the migration.

- **Audit log.** Every migration SHOULD produce an audit log that
  records, for each batch: the batch identifier and the records it
  covered; the result (success, partial, failed, retried); the timestamp
  and any operator action (start, pause, resume, throttle change, manual
  retry). The audit log SHOULD be preserved alongside the migration plan.

### Risk, security, and privacy

- **Classify data before the migration begins.** Data being moved MUST
  be classified according to the organization's data classification
  scheme. The classification determines handling requirements:
  encryption, access control, retention, cross-border transfer
  restrictions, and the regulatory regimes (GDPR, HIPAA, PCI, others)
  that govern the data. A migration plan that does not state the
  classification of its data is incomplete. See
  [TS-53: Privacy and Data Protection](../053/AGENTS.md).

- **Encryption.** Data in transit between source and target MUST be
  encrypted. Data at rest at the target MUST be encrypted to a standard at
  least equal to the source's. A migration to a target with weaker
  encryption than the source is a downgrade and MUST be flagged in the
  plan.

- **Access control.** A migration typically requires elevated access to
  both source (read entire data set) and target (write). This access
  SHOULD be:
  - Scoped to the smallest set of permissions the migration actually
    requires, not a blanket administrative credential.
  - Granted for the duration of the migration only, and revoked on
    completion.
  - Audited, with a record of who held it and when.

  Migration credentials SHOULD be distinct from any long-lived
  application or operator credential, so they can be revoked without
  affecting other work. See
  [TS-52: Security and Secrets Management](../052/AGENTS.md).

- **Personal and regulated data.** For personal data, the plan MUST
  address:
  - **Lawful basis and purpose.** The migration is a new processing of
    the data; the lawful basis SHOULD be confirmed, not assumed.
  - **Cross-border transfer.** If the migration moves data across
    jurisdictional boundaries, the transfer mechanism (adequacy decision,
    standard contractual clauses, binding corporate rules) MUST be in
    place before the migration begins.
  - **Minimization.** A migration is an opportunity to retire data that
    is no longer needed; where retention periods have expired, data
    SHOULD be deleted rather than migrated.
  - **Data subject rights.** A long-running migration can interfere with
    data subject access and erasure requests; the plan SHOULD define how
    such requests are honored during the migration window.

- **Backups of sensitive data inherit all handling requirements.**
  Migration backups SHOULD be encrypted at rest, access-controlled to the
  migration's scoped credential, and deleted on completion of the soak
  period unless retained as the production backup.

- **Insider risk.** For sensitive data, the migration SHOULD be designed
  so operators do not need to read the data in cleartext (eg. by
  transferring encrypted exports the target imports without operator
  visibility). Where operator access is unavoidable, it SHOULD be logged
  and reviewed.

### Best practices and anti-patterns

**Do:**

- Separate the migration from the switch-over; plan them as two
  operations with a gate between them.
- Preserve the source — keep it writable and intact through the
  switch-over and into the soak period so switch-over rollback is cheap.
- Design for idempotency and resumability — a failed or interrupted
  migration MUST be resumable by re-running it.
- Expand and contract — decompose schema changes into independently
  deployable, reversible steps; never combine expand and contract in a
  single deploy.
- Validate before switching over — the gate is a passing validation run
  that includes a correctness check, not only a completeness check.
- Rehearse the cutover end-to-end against a non-production environment
  before production.
- Test against real data — synthetic data does not reproduce the
  anomalies and scale that break migrations.
- Throttle and observe — run the migration as a monitored, throttleable
  workload on its own dashboard.
- Take and verify backups — a backup that has not been tested for
  restore is not a rollback plan.
- Classify data before you move it — the classification determines
  handling requirements.

**Don't:**

- Don't combine the migration and the switch-over — it produces a single
  failure with the worst-case rollback profile of both.
- Don't trust a row count — validation MUST include a correctness check.
- Don't ship a migration you can't pause — the operator MUST be able to
  pause, resume, and throttle without the author present.
- Don't ship an irreversible step unmarked — irreversible steps MUST be
  identified, gated on prior validation, and approved explicitly.
- Don't drop the source on cutover — decommissioning is a separate step
  after a soak period, and it is the point of no return.
- Don't migrate data you don't need — a migration is an opportunity to
  retire expired data, not an obligation to carry it forward.
- Don't treat zero-downtime as a goal — default to the simplest strategy
  that fits the availability requirement.
- Don't skip the dual-write shadow run — the dual-write path is where
  zero-downtime migrations fail; exercise it under real load first.
- Don't reuse an administrative credential — scope a dedicated credential
  and revoke it on completion.

## References

- [TS-45: Data Migrations (source)](README.adoc)
- [TS-3: Design Docs](../003/AGENTS.md)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-11: Versioning](../011/AGENTS.md)
- [TS-12: Quality Assurance](../012/AGENTS.md)
- [TS-13: Functional Testing](../013/AGENTS.md)
- [TS-25: Technical Documentation](../025/AGENTS.md)
- [TS-43: Relational Databases and SQL](../043/AGENTS.md)
- [TS-44: Non-Relational (NoSQL) Databases](../044/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [TS-57: Logging, Monitoring, Observability](../057/AGENTS.md)
- [Refactoring Databases (Ambler & Sadalage)](https://martinfowler.com/books/refactoringDatabases.html) — source of the expand-and-contract pattern
- [Online migrations at Stripe](https://stripe.com/blog/online-migrations) — dual-write/backfill/verify/switch pattern