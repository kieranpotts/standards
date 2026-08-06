# TS-52 gap analysis

Gaps found comparing TS-52: Security and Secrets Management against the
following reference resources:

- `https://nocomplexity.com/simplify-security/` (landing hub)
- `https://nocomplexity.com/simplifysecurity-manifesto/` (the Manifesto)
- *Mastering Security by Design* — `https://nocomplexity.github.io/securitybydesign/`
  (source: `github.com/nocomplexity/securitybydesign`); cited below as
  `sbd:<file>#<section>`
- `https://nocomplexity.com/documents/securitysolutions/intro.html` (Open
  Security Solutions directory)
- `__TODO__/security.md`, `__TODO__/security/injection.md`,
  `__TODO__/security/README.md` (local reference files — prior run, retained)

**Assessment.** The nocomplexity reference set is dominated by the
*Mastering Security by Design* open book, a broad Security-by-Design
*framework* spanning governance, culture, risk methodology, architecture,
SSDLC process, monitoring, principles, policies, training, and FOSS security.
TS-52's stated scope is narrower — security requirements for applications and
secrets management — so the majority of the book (security management &
frameworks, security culture, awareness/training, risk-assessment
mathematics, SSDLC process steps, security-architecture methodology,
ransomware/BCDR, Python-specific tooling) plausibly sits outside TS-52 and is
listed under Out-of-scope. Within scope, the book adds a consolidated set of
security principles TS-52 never states as principles (defence in depth, fail
secure, separation of duties, compartmentalisation, secure defaults, minimise
attack surface, economy of mechanism, design for secure updates), data-in-use
protection, Zero Trust, dedicated security/audit logging, security monitoring,
dependency integrity & provenance (SBOM, reproducible builds, hash
verification), third-party project-health evaluation, memory-hard password
hashing, a vulnerability patching SLA, external penetration testing,
input/injection validation, key-management lifecycle detail, SSO, broader
MFA, and rate-limiting/DoS protection. Several of these TS-52 touches only
lightly (partial). The prior `__TODO__`-based gaps (injection, IAST,
environment-compliance testing, secure package distribution, deterministic
builds, and SAST/DAST/dependency false-positive caveats) remain open — the
standard has not changed since the initial run.

**Status:** Re-run 2026-08-06 against the nocomplexity.com reference set
(added); prior `__TODO__` findings retained and still open. No gaps checked
off — the standard's `.adoc` files are unchanged since 2026-08-05, so every
prior gap remains open.

## Missing

- [ ] `__TODO__/security.md:50-61` (Secure package distribution) —
      distributing packages securely for third-party consumption, The
      Update Framework (TUF), and package registries (NPM, Maven, NuGet,
      Launchpad) — is not addressed anywhere in the standard. TS-52's
      third-party code section (`01-third-party-code.adoc:1-89`) covers
      *consuming* third-party code, not *publishing* it securely. Recommend
      a new section, or flag as out-of-scope (see below).

- [ ] `__TODO__/security.md:65-73` (Compilation integrity assurance /
      deterministic builds) — using deterministic builds to verify
      pre-compiled delivered code has not been altered (eg. Gitian) — is
      not addressed anywhere in the standard. Recommend placing in a new
      section, or defer to TS-10 (Releasing).

- [ ] `__TODO__/security.md:87-96` (Environment security compliance
      testing) — writing tests to assert environments meet baseline
      security requirements (eg. TLS enforced, plain HTTP disabled) using
      tools like Gauntlt and InSpec — is not addressed anywhere in the
      standard. Recommend placing at `04-vulnerability-scanning.adoc` or a
      new section under network security.

- [ ] `__TODO__/security.md:98-116` (IAST) — Interactive Application
      Security Testing, which instruments the runtime and uses QA inputs
      to detect vulnerabilities with fewer false positives than DAST — is
      not addressed anywhere in the standard. TS-52 lists SAST, DAST, and
      SCA (`04-vulnerability-scanning.adoc:5-11`) but not IAST. Recommend
      placing at `04-vulnerability-scanning.adoc:5-11`.

- [ ] `__TODO__/security/injection.md:1-40` (Injection vulnerabilities) —
      injection flaws (SQL injection, command injection), the principle
      that user input is untrusted on both network and local interfaces,
      and the worked command-injection code example — are not addressed
      anywhere in the standard. TS-52's web application security section
      (`09-web-application-security.adoc`) covers headers, caching, and
      data controls but not input injection. Recommend a new section in
      `09-web-application-security.adoc` or a new `10-input-validation.adoc`
      file.

- [ ] `sbd:principles/securityprinciples.md#Defence in depth` — layering
      multiple, independent security controls so failure of one does not
      lead to system compromise — is not stated anywhere in the standard.
      TS-52 applies multiple controls (encryption, scanning, headers) but
      never articulates defence in depth as a principle. Recommend a new
      "Security principles" section, or place at `04-vulnerability-scanning.adoc`.

- [ ] `sbd:principles/securityprinciples.md#Fail securely` — when a
      system fails it must default to a closed/deny state, never an open
      one — is not addressed anywhere in the standard. Recommend a new
      "Security principles" section.

- [ ] `sbd:principles/securityprinciples.md#Separation of duties (and privilege)`
      — no single person or process should hold excessive authority;
      split critical functions across multiple actors — is not addressed
      anywhere in the standard. TS-52's authorization section
      (`07-authorization-and-access-controls.adoc`) covers least privilege
      and roles but not separation of duties. Recommend placing at
      `07-authorization-and-access-controls.adoc`.

- [ ] `sbd:principles/securityprinciples.md#Compartmentalisation` —
      isolate components so a breach in one area does not compromise the
      whole system — is not addressed anywhere in the standard. Recommend
      placing at `08-network-security.adoc` or a new "Security principles"
      section.

- [ ] `sbd:principles/securityprinciples.md#Minimise attack surface area`
      — remove unnecessary features, endpoints, and entry points; less
      code means fewer holes — is not stated as a requirement anywhere in
      the standard. Recommend a new "Security principles" section.

- [ ] `sbd:principles/securityprinciples.md#Establish secure defaults`
      — default configurations must be secure out of the box and deny by
      default — is not stated anywhere in the standard. Recommend a new
      "Security principles" section.

- [ ] `sbd:principles/securityprinciples.md#Economy of mechanism (Keep it simple!)`
      — keep security-critical designs as simple and small as possible;
      complexity increases vulnerabilities and is harder to verify — is
      not stated anywhere in the standard. Recommend a new "Security
      principles" section.

- [ ] `sbd:principles/securityprinciples.md#Design for secure updates` —
      systems must be able to receive and apply security patches safely
      and reliably — is not addressed anywhere in the standard. Recommend
      a new section, or place at `04-vulnerability-scanning.adoc`.

- [ ] `sbd:principles/securityprinciples.md#Protect data everywhere` —
      data must be protected at rest, in transit, AND in use (processed at
      CPU level / touched by applications) — is not addressed. TS-52's
      encryption section (`02-encryption.adoc:1-6`) covers only at rest
      and in transit. Recommend placing at `02-encryption.adoc`.

- [ ] `sbd:securityarchitecture/zerotrust.md#What is a Zero Trust Architecture?`
      — Zero Trust ("never trust, always verify"; assume breach; verify
      every request; least-privilege JIT/JEA access; minimise blast
      radius) — is not addressed anywhere in the standard. Recommend a
      new section, or place at `08-network-security.adoc`.

- [ ] `sbd:securityarchitecture/logging.md#Security Logging` — dedicated
      security/audit logging requirements (what to log: authentication,
      authorization, sensitive-resource access, configuration changes;
      no PII in logs; structured JSON; immutable/append-only storage;
      retention; `trace_id` correlation; restricted access to audit logs;
      SIEM integration) — are not addressed. TS-52 only requires failed
      authentication attempts to be logged and monitored
      (`06-authentication.adoc:23-24`). Recommend a new "Security logging"
      section. (Secrets-in-logs is already covered by
      `03-secrets.adoc:17`; PII and the rest are not.)

- [ ] `sbd:monitoring/securitymonitoring.md#Why You Cannot Escape Security Monitoring`
      — security monitoring as a discipline: intrusion detection, file
      integrity monitoring, IDS/IPS, SIEM, alerting, and starting simple
      then scaling — is not addressed. TS-52's only monitoring reference
      is monitoring failed-authentication logs (`06-authentication.adoc:23-24`).
      Recommend a new "Security monitoring" section. (Plausibly a separate
      monitoring standard — flagged for the user.)

- [ ] `sbd:foss/softwarepackage.md#Solution` (and
      `sbd:prevention/pbom.md#L1`, `sbd:prevention/mvsp.md#Application implementation controls — Build and release process`)
      — dependency / artefact integrity verification: hash verification of
      downloads, reproducible builds, SBOM, SLSA Build-Level-1 provenance,
      and the Pipeline Bill of Materials (PBOM) — are not addressed.
      TS-52's third-party code section (`01-third-party-code.adoc:80-83`)
      pins versions and checks vulnerability databases but does not verify
      artefact integrity or provenance. Recommend placing at
      `01-third-party-code.adoc`.

- [ ] `sbd:foss/checklist_evalfoss.md` (and `sbd:foss/foss_intro.md#tip`)
      — evaluating the health and security practices of a third-party
      project before adopting it (OpenSSF Best Practices badge,
      OpenSSF Scorecards/deps.dev, maintainer diversity, release recency,
      security audits, security-response track record, sandbox testing,
      malicious-code checks per Backstabber's Knife Collection) — is not
      addressed. TS-52's third-party code section
      (`01-third-party-code.adoc:62-78`) covers reviewing code for
      malicious patterns but not evaluating the upstream project's
      sustainability or security practices. Recommend placing at
      `01-third-party-code.adoc`.

- [ ] `sbd:prevention/mvsp.md#Application implementation controls — Vulnerability prevention`
      — training developers and implementing guidelines to prevent
      authorization bypass, insecure session management, injection
      (SQL/NoSQL/XXE/OS command), cross-site scripting (XSS), and
      cross-site request forgery (CSRF) — is not addressed. TS-52's web
      application security section (`09-web-application-security.adoc`)
      covers headers, caching, and client-side data controls but not
      input validation or these vulnerability classes (overlaps the prior
      `__TODO__/security/injection.md` gap, which covers only SQL/command
      injection). Recommend a new section in
      `09-web-application-security.adoc` or a new `10-input-validation.adoc`.

- [ ] `sbd:prevention/mvsp.md#Business controls — External testing` (and
      `sbd:prevention/mvsp.md#Business controls — Customer testing`) —
      contracting annual comprehensive penetration tests and enabling
      customer/delegate security testing on a non-production environment
      — is not addressed anywhere in the standard. Recommend placing at
      `04-vulnerability-scanning.adoc`.

- [ ] `sbd:policies/softwareupdate.md#Checklist for a Software Update Policy`
      (and `sbd:prevention/mvsp.md#Application implementation controls — Time to fix vulnerabilities`)
      — a vulnerability patching SLA / software-update policy (apply
      security updates of severity "medium" or higher per a patching
      schedule; deploy patches for materially impactful vulnerabilities
      within 90 days; rapid-deployment of critical patches; devices that
      cannot be updated must be isolated/revoked) — is not addressed.
      TS-52's vulnerability scanning section
      (`04-vulnerability-scanning.adoc:13-15`) requires prioritising
      findings but sets no patching SLA or update policy. Recommend
      placing at `04-vulnerability-scanning.adoc`.

- [ ] `sbd:prevention/mvsp.md#Application design controls — Security Headers`
      — a minimally-permissive Content-Security-Policy, limiting iframing
      via `X-Frame-Options` OR CSP `frame-ancestors`, and disabling
      caching for APIs/endpoints returning sensitive data — is covered
      more shallowly by TS-52. `09-web-application-security.adoc:11-30`
      requires CSP, `X-Frame-Options`, and `X-Content-Type-Options` but
      does not mention limiting iframing via CSP `frame-ancestors` as an
      alternative, nor disabling caching specifically for sensitive
      APIs/endpoints (the caching guidance at `:34-41` is general). Marked
      partial rather than missing. See Partial below.

## Partial

- [ ] `__TODO__/security.md:13-15` covers SAST more thoroughly than
      `04-vulnerability-scanning.adoc:5-7` — specifically, the caveat that
      SAST produces false positives and false negatives (yielding a false
      sense of assurance) and can be overwhelming when introduced late due
      to the volume of findings. TS-52 recommends SAST without these
      caveats.

- [ ] `__TODO__/security.md:37-39` covers dependency scanning more
      thoroughly than `01-third-party-code.adoc:80-83` — specifically, the
      caveat that dependency scanners produce false positives (flagging
      vulnerable classes not actually in use) and that the best tools
      distinguish dependencies that are *imported* from those actually
      *used*, reducing false positives. TS-52 requires checking against
      vulnerability databases but omits this nuance.

- [ ] `__TODO__/security.md:102` covers DAST more thoroughly (and
      contradictorily) than `04-vulnerability-scanning.adoc:5-7` —
      specifically, the claim that DAST is "highly discouraged" due to the
      volume of false positives and false negatives it reports, and that
      IAST sees significantly fewer of both. TS-52 RECOMMENDS DAST without
      acknowledging these limitations.

- [ ] `__TODO__/security.md:75-83` (Secure dependency consumption) is
      partially covered by `01-third-party-code.adoc:80-83`. The reference
      adds the explicit guidance to avoid wildcard (`*`) version
      specifiers and to only pull dependency updates for security fixes or
      new features the application will actually use. TS-52 requires
      pinning (which implies no wildcards) but does not state the rationale
      or the update-policy guidance.

- [ ] `sbd:principles/securityprinciples.md#Open design (Avoid security by obscurity)`
      — security must not depend on secrecy of design or implementation;
      assume attackers have the code and documentation — is applied only
      narrowly by TS-52. `07-authorization-and-access-controls.adoc:10-20`
      forbids relying on hidden fields/URLs/cookies for authorization
      decisions, but the standard never states open design / avoid
      security-by-obscurity as a general principle. Recommend lifting it
      into a new "Security principles" section.

- [ ] `sbd:prevention/mvsp.md#Application design controls — Password policy`
      — storing passwords hashed and salted with a memory-hard or CPU-hard
      one-way hash (eg. Argon2, bcrypt, scrypt) — is covered more
      thoroughly than `06-authentication.adoc:72-77`, which requires
      SHA-3/SHA-2. SHA-2/SHA-3 are fast general-purpose hashes, not the
      memory-hard/CPU-hard functions recommended for password storage.
      TS-52 omits memory-hard password hashing entirely. Recommend
      updating `06-authentication.adoc:72-77`.

- [ ] `sbd:securitymanagement/keymanagement.md` (Key Inventory, Access
      Control, Lifecycle, Secure Storage, Monitoring, Documentation
      sections) — a dedicated key-management lifecycle: central key
      inventory with classification and ownership, quarterly key-access
      reviews, automated rotation, tested revocation procedures, secure
      destruction of retired keys, HSM/vault storage, key backup/recovery,
      and SIEM integration for key usage — is covered only partially by
      `03-secrets.adoc`. TS-52 covers secrets/keys generally (Vault,
      rotation ≤1 week, narrow scoping, compromised-secret handling) but
      omits key inventory, access reviews, secure destruction, and key
      backup/recovery. Recommend extending `03-secrets.adoc` or a new
      key-management section.

- [ ] `sbd:prevention/mvsp.md#Application design controls — Single Sign-On`
      (and `sbd:securityarchitecture/securityarchitecture.md#3. Solution Building Blocks`)
      — implementing SSO using modern, maintained, industry-standard
      protocols (OIDC, OAuth 2.0, SAML) — is covered only partially by
      `06-authentication.adoc:1-9`, which prefers token/certificate
      authentication but never names SSO or the standard protocols.
      Recommend placing at `06-authentication.adoc`.

- [ ] `sbd:prevention/mvsp.md#Operational controls — Logical access` (and
      `sbd:prevention/examples.md#Use Multi-factor authentication`) —
      requiring MFA for remote access to customer data/production systems
      and for privileged actions — is covered more narrowly by
      `06-authentication.adoc:7-9`, which only "strongly RECOMMENDS" 2FA at
      initial login. TS-52 does not require MFA for privileged or remote
      access to production/data. Recommend extending
      `06-authentication.adoc`.

- [ ] `sbd:prevention/mvsp.md#Application design controls — Security Headers`
      covers TS-52's web-application security headers
      (`09-web-application-security.adoc:6-41`) more thoroughly —
      specifically, limiting iframing via CSP `frame-ancestors` (as an
      alternative/complement to `X-Frame-Options`) and explicitly
      disabling caching for APIs/endpoints returning sensitive data. TS-52
      requires `X-Frame-Options` and general `Cache-Control` but omits
      these two specifics.

- [ ] `sbd:threatmodeling/stride_example.md#Denial of Service (Availability)`
      (and `sbd:prevention/mvsp.md`) — rate limiting (eg. 60 req/min per
      identity) and payload-size limits to mitigate DoS/API-flood — is not
      addressed. TS-52's network security section
      (`08-network-security.adoc`) limits inbound/outbound traffic but
      says nothing about application-layer rate limiting or DoS
      protection. Recommend placing at `08-network-security.adoc` or
      `09-web-application-security.adoc`.

## Out-of-scope

- [ ] `__TODO__/security.md:50-61` (Secure package distribution) covers
      the secure *publication* of packages for third-party consumption
      (TUF, registries). This plausibly sits outside TS-52's stated
      purpose — TS-52 is about security requirements for *applications*
      and secrets management, and the AGENTS.md defers release mechanics
      to TS-10. Flagged for the user to confirm or overrule (also listed
      under Missing above, since it could fit as a new section).

- [ ] `__TODO__/security.md:65-73` (Compilation integrity assurance /
      deterministic builds) covers build/release integrity for
      pre-compiled deliverables. This plausibly sits outside TS-52's
      stated purpose and overlaps with TS-10 (Releasing), to which the
      AGENTS.md defers release mechanics. Flagged for the user to confirm
      or overrule (also listed under Missing above).

- [ ] `__TODO__/security.md:118-122` (Release: artifact immutability,
      host ephemerality), `:124-128` (Configuration: config-as-code, secret
      management), and `:130-136` (Monitoring: RASP, threat intelligence)
      are stub TODOs in the reference with no substantive content. Not
      included in the comparison.

- [ ] `sbd:ssdlc/` (Secure SDLC: 17 minimum activities, secure coding
      standards, CI/CD pipeline integrity, embedding security in every
      phase) covers the development *process*, not application security
      requirements. Plausibly sits outside TS-52 and overlaps a
      development-lifecycle/SSDLC standard. Flagged for the user to
      confirm or overrule.

- [ ] `sbd:riskassesment/` (Risk assessment methodology: r = p × i,
      Knightian uncertainty, probability axioms, expected value) covers
      risk-assessment mathematics. Plausibly sits outside TS-52 and
      overlaps TS-54 (Threat Modeling) / a dedicated risk standard.
      Flagged for the user to confirm or overrule.

- [ ] `sbd:securitymanagement/` (Security management & frameworks: ISO/IEC
      27001, NIST CSF, Cyber Essentials, governance, resource allocation)
      covers organisational security management, not application
      requirements. Out of scope for TS-52. (Key management from the same
      chapter is listed under Partial above.)

- [ ] `sbd:culture/` and `sbd:training/training_intro.md` (Security
      culture, blameless retrospectives, awareness programmes, security
      training) cover organisational/people practices. Out of scope for
      TS-52 as an application-security-requirements standard.

- [ ] `sbd:policies/` (Security policies as governance documents:
      policy/procedure/standard/guideline distinctions, policy design)
      covers governance documentation. Out of scope for TS-52. (The
      software-update policy from the same chapter is listed under
      Missing above.)

- [ ] `sbd:prevention/ransomware.md` (Ransomware resilience, offline
      backups, BCDR planning) and `sbd:prevention/zerodays.md` cover
      operational resilience and disaster recovery. Out of scope for TS-52.

- [ ] `sbd:threatmodeling/` (STRIDE methodology, six-step process, DFD
      rules, attack trees, worked example) covers threat-modeling
      methodology, which TS-52 explicitly defers to TS-54
      (`05-threat-modeling.adoc:17-18`). Out of scope for TS-52.

- [ ] `sbd:securityarchitecture/abbs.md`, `sbd:securityarchitecture/create.md`
      (Architecture Building Blocks / Solution Building Blocks
      methodology, reference-architecture creation steps) cover
      security-architecture methodology. Plausibly sits outside TS-52 and
      overlaps a security-architecture standard. (Zero Trust, extracted
      from the same chapter, is listed under Missing above.) Flagged for
      the user to confirm or overrule.

- [ ] `sbd:introduction/tacitknowledge.md` (Tacit vs explicit knowledge,
      mentoring, communities of practice) and the Manifesto
      (`https://nocomplexity.com/simplifysecurity-manifesto/`) cover
      security philosophy and knowledge management. Out of scope for TS-52
      as an application-security-requirements standard.

- [ ] `sbd:foss/pythonsecsoftware.md` and
      `https://nocomplexity.github.io/pythonsecurity/` (Python-specific
      security tooling and the Python security-application evaluation
      checklist) are language-specific. Out of scope for a
      language-agnostic standard.

- [ ] `https://nocomplexity.com/documents/securitysolutions/intro.html`
      (Open Security Solutions directory — "prefer FOSS for security
      tools") is a tool-selection philosophy and directory. The
      evaluative criteria it shares are captured under Missing above; the
      pure "prefer open tools" stance is out of scope for TS-52.

- [ ] The landing page's links to cyber-security conferences, (free)
      cyber-security courses, Simplify Digital Privacy, and Simplify
      Machine Learning (`https://nocomplexity.com/simplify-security/`)
      are topical hubs unrelated to TS-52's scope. Not ingested.

## Unresolved

- None. All reference resources were retrieved successfully: the landing
  page, the Manifesto, the Open Security Solutions intro, and all ~50
  source files of the *Mastering Security by Design* book. The
  `__TODO__/security/README.md` file is a stub ("# Security") with no
  content to compare.