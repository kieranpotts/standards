# TS-52 gap analysis

Gaps found comparing TS-52: Security and Secrets Management against the
following reference resources:

- `__TODO__/security.md`
- `__TODO__/security/injection.md`
- `__TODO__/security/README.md` (stub, no content)

**Assessment.** The reference material (`__TODO__/security.md`) is a
broad security-tooling survey organised around the build lifecycle (code,
build, testing, release, configuration, monitoring). TS-52 already covers
the reference's core recommendations on SAST, DAST, dependency scanning,
and version pinning, but omits several adjacent tooling categories the
reference introduces (IAST, environment security compliance testing,
secure package distribution, deterministic builds) and adds no caveat
about SAST/DAST false positives and false negatives. The second reference
(`__TODO__/security/injection.md`) covers injection vulnerabilities
(SQL/command injection), which TS-52 does not address at all. Most gaps
are missing; a couple are partial where TS-52 names a category but omits
the reference's nuance.

**Status:** Initial run (2026-08-05). All gaps open; none checked off.

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

## Unresolved

- None. All three reference files were read successfully; the
  `__TODO__/security/README.md` file is a stub ("# Security") with no
  content to compare.