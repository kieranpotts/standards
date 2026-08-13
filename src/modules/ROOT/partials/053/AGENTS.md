# TS-53: Privacy and Data Protection

General principles and practices for protecting the privacy of
individuals and the data that is collected about them.

Use this when designing, implementing, or reviewing systems that collect,
store, transmit, or process personal data — especially personally
identifiable information (PII) and data subject to regulations such as
GDPR, HIPAA, or PCI.

Do NOT use this for security controls (encryption at rest, secrets
management, authentication) — see
[TS-52: Security and Secrets Management](../052/AGENTS.md). For threat
modeling methodologies, see [TS-54: Threat Modeling](../054/AGENTS.md).
For general logging and observability, see
[TS-57: Logging, Monitoring, Observability](../057/AGENTS.md). For
retention policy as a design artifact, see
[TS-3: Design Docs](../003/AGENTS.md) and
[TS-25: Technical Documentation](../025/AGENTS.md).

## Rules

### Privacy by design

- **Applications MUST be designed with privacy and data protection
  embedded as core design principles.** This is *privacy by design* (or
  *privacy by default*): data processing procedures and data
  protection controls are considered at the design stage of an IT system
  or any subsequent change, rather than added on later. GDPR explicitly
  requires that technical and organizational measures for protecting
  data be proactively designed into business processes and systems.

- **Follow the seven principles of privacy by design:**
  1. Be proactive about privacy, not reactive. Anticipate and prevent
     privacy breaches before they happen.
  2. Build maximum privacy into default settings. Users may explicitly
     opt in to reduce privacy settings, but maximum privacy safeguards
     must be the default. If users do nothing, they are protected.
  3. Embed privacy into the design of IT systems and business processes.
     Privacy should be integral to a system, not an add-on.
  4. Privacy may need to be balanced against other legitimate interests,
     but the goal is a positive-sum (not zero-sum) outcome — privacy is
     not traded off against other objectives.
  5. End-to-end security: embed strong encryption and other security
     measures across the complete lifecycle of data.
  6. Be open and transparent about your privacy policies and standards.
     Inform users about how their data is processed and stored. Allow
     for independent verification of your privacy practices.
  7. Give users control over their data, and make it easy for them to
     manage their privacy settings.

### Personally identifiable information (PII)

- **PII is any information that can be used to identify an individual.**
  It includes, but is not limited to:
  - Names.
  - Postal addresses.
  - Email addresses.
  - Phone numbers.
  - Passport numbers, social security numbers, and other
    government-issued identifiers.
  - Bank account numbers and other financial credentials.

  Combinations of values can also form PII — neither a date of birth nor
  a postcode can identify an individual alone, but combined they can.
  Some values are "borderline" PII (eg. IP addresses); whether to
  handle borderline values as PII depends on context (an IP address
  logged with timestamps and user agent strings may be PII).

- **PII MUST NOT be stored anywhere other than production databases and
  their backup systems.** For non-production systems, synthetic (dummy)
  data MUST be used in place of real PII. Alternatively, a hash of real
  PII MAY be used, as long as a strong cipher is used (making the hash
  irreversible without the cipher) and the cipher is handled as a secret
  — see [TS-52: Security and Secrets Management](../052/AGENTS.md).

- **Annotate synthetic data where it is hard to distinguish from real
  PII.** Where it is not easy to distinguish between real and synthetic
  PII, the data SHOULD be clearly annotated as being synthetic.

- **Use automated tools to detect and prevent storage of PII in
  non-production systems** such as source code repositories. For
  example, pre-commit hooks can be enabled in Git to run secret
  scanning tools.

### Data retention

- **Data applications MUST have a data retention policy**, documented as
  part of the application's design.

- **Define a data retention schedule for each discrete type of data
  stored.** The policy MUST clearly define the retention period for each
  type of data, the conditions under which data will be automatically
  deleted, and the data types that may be stored indefinitely (which
  MUST include technical data such as logs and monitoring data).

- **Data MUST NOT be retained for longer than required** to fulfil
  specific business or user functions. This is a legal requirement
  throughout Europe and in many other jurisdictions worldwide.

- **Provide an automated mechanism for deleting data per the retention
  policy.** A common implementation pattern is scheduled tasks. Data
  deletion schedules and operations MUST be planned to minimize impact
  on the performance or availability of production systems.

- **Provide a documented manual process** for finding and deleting data
  outside its retention period. The manual process MUST be undertaken at
  regular intervals to verify the automatic deletion mechanism is
  functioning as expected.

- **Deletion processes MAY need to involve caches, replicas, backups,
  and failovers** as well as primary data sources, depending on the
  data synchronization strategies in use.

- **Log data deletion events for auditing.** Applications MUST log data
  deletion events. Logs MUST capture:
  - When the process ran, and when it completed.
  - Who initiated the run (user or automated agent).
  - Which data was deleted (eg. the number of entities deleted for
    each data type).
  - Any errors encountered (errors SHOULD also be captured in a
    separate error log).

- **Data deletion audit logs MUST be easily accessible and searchable**
  for reporting purposes.

### Data redaction

- **Applications that store PII MUST provide a mechanism for users to
  request the redaction or erasure of their data.** This is mandated by
  data protection legislation in many jurisdictions — most notably GDPR,
  which enshrines the right to erasure (the "right to be forgotten") in
  Article 17. Organizations must respond to such requests in a timely
  manner (typically within 30 days under GDPR).

- **Identify and remove all personal data from all systems.** When a
  user requests redaction, applications MUST identify all personal data
  belonging to that user and remove it from:
  - Primary databases and data stores.
  - Backup systems and snapshots.
  - Caches.
  - Replicas and failovers.
  - Log files and audit trails (where PII has been captured).

- **Legally retained data MAY be retained, and OPTIONALLY anonymized or
  pseudonymized.** Data retained for legitimate legal or business
  purposes (transaction records required for accounting, tax, or fraud
  prevention) MAY be retained. It MAY be anonymized or pseudonymized to
  remove association with the individual.

- **Provide an automated mechanism for redaction requests.** A common
  pattern is to mark user accounts as deleted or redacted, then run a
  scheduled process that removes all associated data from production
  systems and backups.

- **Plan and test redaction to avoid performance/availability impact.**
  Data redaction processes MUST be planned and tested to ensure they do
  not impact system performance or availability. Care MUST be taken when
  redacting data from backup systems, as restoration of a backup may
  inadvertently restore redacted data.

- **Log all data redaction events.** For auditing and compliance,
  applications MUST log all data redaction events. Logs MUST capture:
  - When the redaction request was received.
  - Who initiated the request (the user or an authorized representative).
  - What data was redacted or deleted.
  - When the redaction process completed.
  - Any errors or exceptions encountered.

- **Retain redaction audit logs for the applicable limitation period.**
  Data redaction audit logs MUST be retained for the duration of any
  applicable limitation period for legal claims, typically 3–6 years
  depending on jurisdiction.

### Logging and monitoring data

- **Logs and monitoring data SHOULD be persisted in separate storage**
  from an application's primary data stores (for state and session
  data).

- **PII MUST NOT be sent to log output.**

## References

- [TS-53: Privacy and Data Protection (source)](../../pages/053.adoc)
- [TS-3: Design Docs](../003/AGENTS.md)
- [TS-25: Technical Documentation](../025/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-54: Threat Modeling](../054/AGENTS.md)
- [TS-57: Logging, Monitoring, Observability](../057/AGENTS.md)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [Information and Privacy Commissioner of Ontario: privacy design](https://www.ipc.on.ca/en/resources-and-decisions/privacy-design)