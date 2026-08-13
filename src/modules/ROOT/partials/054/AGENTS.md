# TS-54: Threat Modeling

The art and science of threat modeling: identifying potential security
and privacy vulnerabilities in software systems, deciding on mitigation
strategies, and maintaining a risk register — in a structured and
systematic way.

Threat modeling is more of a process than a tool or artifact. The core
is systematic analysis of a system's design to identify potential attack
vectors and vulnerabilities. The output is a set of identified threats,
with associated risk ratings and mitigation strategies, captured
initially in a threat assessment table and ultimately maintained in the
application's risk register.

Use this when designing, reviewing, or iterating on the security posture
of a system — particularly during design phases and at release-cycle
breakpoints.

Do NOT use this for the underlying security controls themselves
(encryption, secrets management, authentication, authorization) — see
[TS-52: Security and Secrets Management](../052/AGENTS.md). For privacy
and data protection (PII handling, data retention, redaction), see
[TS-53: Privacy and Data Protection](../053/AGENTS.md). For general
logging and observability, see
[TS-57: Logging, Monitoring, Observability](../057/AGENTS.md). For the
risk register and threat assessment as documentation artifacts, see
[TS-3: Design Docs](../003/AGENTS.md) and
[TS-25: Technical Documentation](../025/AGENTS.md).

## Rules

### General best practices

- **Threat modeling works best when iterative, baked into the regular
  development process**, rather than a one-time activity.

- **Threat modeling workshops SHOULD begin during the design phase** of
  a new software product. Thereafter, threat assessments SHOULD be
  treated as living documents, regularly revised as the system evolves,
  new threats emerge, or business requirements change.

- **Workshops SHOULD NOT be postponed until the product is nearly ready
  to ship to production.** Iterative threat assessment catches
  vulnerabilities earlier in the development cycle, when they are cheaper
  to remediate. Security and privacy requirements are cross-cutting
  architectural concerns and tend to be expensive to retrofit into an
  established architecture.

- **Schedule workshops at the breakpoint between each iterative
  development/release cycle** (RECOMMENDED). Better still, integrate
  workshops into the normal development lifecycle of individual
  features.

- **Workshops SHOULD be organized and facilitated by a security champion
  within each team.** The rest of the participants play the role of
  security analysts.

- **Use a multi-disciplinary approach.** Participants SHOULD be drawn
  from architecture and security, product and business, and development,
  testing, and operations. The purpose is to view the system from diverse
  perspectives.

- **Use various types of models as input to workshops.** Different
  representations reveal different categories of potential attack
  vectors. RECOMMENDED models:
  - Infrastructure.
  - Data (in situ and in transit).
  - Services and components.
  - Component boundaries and interfaces.
  - Business processes (application logic).
  - External dependencies.

### Threat modeling frameworks

- **Use a structured framework to guide the process.** You MAY use a
  single framework, a combination, or a custom framework tailored to
  your needs. Common frameworks:

#### STRIDE

- **STRIDE** is a Microsoft mnemonic-based framework that categorizes
  threats into six groups. It is a RECOMMENDED minimal framework for
  threat identification (see Identifying threats below).

  | Threat category | Definition | Example countermeasures |
  |---|---|---|
  | **S**poofing | Impersonation of another user or system | SPF, DKIM |
  | **T**ampering | Unauthorized modification of data | Hashes, digital signatures |
  | **R**epudiation | Attacker leaves no trace of malicious actions | Audit/logging, automated log analysis |
  | **I**nformation disclosure | Leaking of sensitive data to unauthorized parties | Encryption, access controls |
  | **D**enial of service (DoS) | Rendering a system unusable | Rate limiting, load balancing |
  | **E**levation of privilege | Gaining higher access levels than authorized | Least privilege, RBAC |

#### PASTA

- **PASTA** (Process for Attack Simulation and Threat Analysis) is a
  multi-stage methodology that aligns business objectives with technical
  requirements. Stages: (1) define business objectives, (2) define
  technical scope, (3) decompose the application, (4) identify
  vulnerabilities, (5) enumerate likelihood and impact. Uses STRIDE or a
  vulnerability database to identify vulnerabilities. Time-consuming;
  best suited to long-lived critical systems, not fast iterative
  development.

#### VAST

- **VAST** (Visual, Agile, and Simple Threat modeling) is designed to
  scale across organizations and work with iterative development. Covers
  two types: *application threat modeling* for development teams
  (process flow diagrams) and *operational threat modeling* for
  infrastructure teams (attack trees).

#### LINDDUN

- **LINDDUN** is a privacy-focused counterpart to STRIDE, for systems
  handling personal information (especially under GDPR or CCPA). The
  acronym covers: **L**inkability, **I**dentifiability, **N**on-
  repudiation, **D**etectability, **D**isclosure of information,
  **U**nawareness, **N**on-compliance.

#### Attack trees

- **Attack trees** are hierarchical diagrams representing how attackers
  might compromise a system. The root is the attacker's ultimate
  objective; branches show paths/sub-goals; leaves are specific actions
  or vulnerabilities. Can be enriched with attributes like cost,
  likelihood, or required skill level. Useful for complex multi-step
  attack scenarios.

#### Kill chains

- **Kill chains** (cyber kill chains, originally Lockheed Martin) model
  the stages of a cyber attack: (1) Reconnaissance, (2) Weaponization,
  (3) Delivery, (4) Exploit, (5) Installation, (6) Command and control,
  (7) Actions on objectives. Helps implement layered defenses;
  particularly valuable for understanding advanced threats.

### Threat modeling workshops

- **Workshops SHOULD follow a structured approach.** The following
  steps are RECOMMENDED:
  1. Review business objectives and scope.
  2. Review component architecture, data flows, system interfaces, etc.
  3. Systematically assess threats against individual components.
  4. Rank risks based on assessment of likelihood and impact.
  5. Identify and prioritize mitigation strategies.

- **Capture outcomes in a formal report**, with the identified threats
  and their mitigation strategies summarized in a threat assessment
  table.

- **Recommended workshop report template** (a starter template
  incorporating STRIDE and PASTA patterns):

  ```markdown
  # Threat modeling workshop <YYYY-MM-DD>

  - **System/application name:** _____
  - **Workshop facilitator:** _____
  - **Participants:**
    - **Business stakeholder:** _____
    - **Technical architect:** _____
    - **Development lead:** _____
    - **Security analyst:** _____
    - **Privacy officer (eg. data controller):** _____
    - **Other stakeholders:** _____

  Pre-workshop checklist:
  - [ ] Schedule participants.
  - [ ] Gather architecture diagrams and documentation.
  - [ ] Review previous threat models (if updating).
  - [ ] Prepare collaboration tools (whiteboard, diagramming software).

  Workshop checklist:
  - [ ] Review business objectives and scope.
  - [ ] Review component architecture, data flows, system interfaces.
  - [ ] Assess STRIDE threat categories against individual components.
  - [ ] Rank risks based on assessment of likelihood and impact.
  - [ ] Identify and prioritize mitigation strategies.

  Post-workshop checklist:
  - [ ] Distribute completed threat assessment to stakeholders.
  - [ ] Create tickets for mitigation work.
  - [ ] Schedule next threat modeling workshop.
  - [ ] Transfer newly identified threats to the risk register.

  ## Business context
  Business objectives; why the system exists; critical business
  functions; key stakeholders; business impact of security/privacy
  failures (financial, reputational, regulatory, operational).

  ## Technical scope
  What is being threat modeled: system boundaries, in-scope components,
  technology stack, deployment environments, integration points.

  ## System decomposition
  How the system works. Include or link to architectural diagrams. Use
  the models to identify key components, data flows, entry points,
  trust boundaries, and the most sensitive assets.

  ### Key components
  | Component | Description | Trust level | Data handled |
  |---|---|---|---|

  ### Data flows
  | Source | Destination | Data type | Protocol | Authentication |
  |---|---|---|---|---|

  ### Sensitive assets
  | Asset | Sensitivity | Integrity reqs | Availability reqs | Privacy concern |
  |---|---|---|---|---|

  ### Entry points
  External interfaces, APIs, and user interfaces to the system.

  ### Trust boundaries
  Where trust changes (eg. internet to DMZ, DMZ to internal network).

  ## Threat assessment
  Assess threats against the identified components, data flows, and
  assets. Use STRIDE (or OWASP Top 10) to rank each threat against each
  component/flow and rank the resulting risks.

  | Ref | Component/Flow | Description | Type | Countermeasures | Likelihood | Impact | Rating |
  |---|---|---|---|---|---|---|---|

  (Add links to issue trackers, resolution deadlines, etc. as required.)
  ```

  An alternative structure analyzes each component against the threat
  types (STRIDE categories, or the OWASP Top 10):

  ```markdown
  ## Component/Flow: _____

  | Threat type | Threat description | Asset at risk | Countermeasures | Likelihood | Impact | Rating |
  |---|---|---|---|---|---|---|
  | Spoofing    |...|...|...|...|...|...|
  | Tampering   |...|...|...|...|...|...|
  | Repudiation|...|...|...|...|...|...|
  | Disclosure |...|...|...|...|...|...|
  | DoS        |...|...|...|...|...|...|
  | Elevation  |...|...|...|...|...|...|
  ```

### Identifying threats

- **The identification of potential threats is the most important part
  of the process.** It is done by systematically analyzing each component
  and data flow against categories of known threats and
  vulnerabilities. It is RECOMMENDED to use a structured framework.

- **STRIDE is a RECOMMENDED minimal framework for threat
  identification.** For complex applications, STRIDE SHOULD be augmented
  with other frameworks plus analysis of public vulnerability databases
  and other sources of information about security and privacy threats.

- **Public vulnerability databases and resources:**
  - [Common Vulnerabilities and Exposures (CVE)](https://www.cve.org/)
  - [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/)
  - [Common Attack Pattern Enumerations and Classifications (CAPEC)](https://capec.mitre.org/)
  - [National Vulnerability Database (NVD)](https://nvd.nist.gov/vuln/search)
  - [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) including
    the [Attack Surface Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
    and the [OWASP Top 10](https://owasp.org/Top10/)

- **Prepare prompt questions to guide workshops.** Prompts help
  systematically interrogate system design against common
  vulnerabilities. Example prompt questions are listed below; the full
  set in the source covers STRIDE categories and OWASP vulnerability
  categories (authentication failures, broken access controls,
  cryptographic failures, injection, deployment pipelines, dependency
  management and software supply chain vulnerabilities, logging and
  monitoring, secure-by-design).

  Example STRIDE prompts:

  - **Spoofing:** Who has their identity verified before processing
    data? How are authentication credentials transmitted and validated?
    Can external entities be verified as who they claim to be?
  - **Tampering:** How are inputs validated and sanitized? Are there
    integrity checks on stored and transmitted data? Is data-in-transit
    protected (HTTPS, signatures)? Can unauthorized users modify stored
    data and configurations?
  - **Repudiation:** Are actions logged with sufficient context to trace
    responsible parties? Can changes be attributed to specific users or
    systems? Are logs protected from tampering?
  - **Information disclosure:** Could sensitive data be unintentionally
    exposed via error messages, logs, or debug information? Is
    sensitive data encrypted at rest and access-controlled? Can
    sensitive data be intercepted during transmission? Do external
    parties receive only necessary data?
  - **Denial of service:** Can the system be overwhelmed through
    resource exhaustion or flooding? Are rate limits and throttling in
    place? Can storage be exhausted or locked? Are DoS protections
    implemented?
  - **Elevation of privilege:** Are role-based access controls properly
    implemented? Could users escalate privileges through logic or
    configuration flaws? Are permissions default-deny and properly
    enforced? Can external entities access restricted functions?

  See the source for the full set of OWASP-category prompt questions,
  which cover authentication failures, broken access controls,
  cryptographic failures, injection, deployment pipelines, dependency
  management, logging and monitoring, and secure-by-design.

### Risk ratings

- **Each identified threat SHOULD be rated based on its likelihood of
  occurrence and scale of impact.** Combining likelihood and impact
  scores gives an overall severity level, typically rated from high to
  low.

- **Be consistent in how you rank potential threats.** You may design
  your own scoring system; the important thing is consistency.

### Mitigation strategies

- **Record the rationale for chosen countermeasures** — or the reasons
  why no mitigation will be done — against each threat.

- **Examples of countermeasures against common threats:**
  - Two-factor authentication.
  - Role-based access controls.
  - Encryption of sensitive data at rest.
  - Encrypted transport protocols.
  - Message signatures.
  - Logging, monitoring, and alerts.
  - Rate limiting.
  - Reducing data retention periods.
  - Code review.
  - Log rotation.
  - Penetration testing.
  - Dependency updates.
  - Dependency version pinning.
  - Scheduled security scans.

### Risk register

- **Newly identified threats SHOULD be added to the application's risk
  register.** Risk registers contain data concerning risk information
  and how risks have evolved over time. A risk register SHOULD take the
  form of a spreadsheet or other tabular data format.

- **RECOMMENDED risk register columns/fields:**
  - **Reference number** (eg. "TA1"; use different codes by context —
    TA for Threat Assessment, AS for AppSec).
  - **Threat name** (short, descriptive, unique; must describe what
    process in the product is impacted or vulnerable).
  - **Threat type** (eg. "Spoofing" — use STRIDE, OWASP, NIST, or other
    frameworks; use consistent categorization).
  - **Threat details** (eg. where the threat can occur, which endpoints
    or users are susceptible — be specific).
  - **Risk probability** (eg. "Probable", "Likely", "Possible",
    "Unlikely", "Rare").
  - **Risk impact** (eg. "Catastrophic", "Critical", "Severe",
    "Marginal", "Negligible").
  - **Risk severity** (overall rating combining probability and impact:
    "Critical", "High", "Medium", "Low").
  - **Mitigation steps** (eg. "Workstation accounts require MFA";
    detailed step-by-step instructions can live in a runbook or alert
    response table).
  - **Mitigation status** (eg. "Pending", "In progress", "Completed",
    or deadline for completion).
  - **Residual risk** (the risk that remains after applying mitigation
    steps: "Critical", "High", "Medium", "Low").
  - **Countermeasures** (additional countermeasures to further mitigate
    the risk; mark N/A when there is no residual risk; note the date
    applied, or whether pending/in progress).
  - **Date reviewed** (the date the status of the threat was last
    reviewed).

## References

- [TS-54: Threat Modeling (source)](../../pages/054.adoc)
- [TS-3: Design Docs](../003/AGENTS.md)
- [TS-25: Technical Documentation](../025/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [TS-57: Logging, Monitoring, Observability](../057/AGENTS.md)
- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/)
- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
- [CVE](https://www.cve.org/), [CWE](https://cwe.mitre.org/),
  [CAPEC](https://capec.mitre.org/), [NVD](https://nvd.nist.gov/)
- Tools: [pytm](https://github.com/izar/pytm),
  [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool),
  [ThreatModeler](https://threatmodeler.com/),
  [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/)