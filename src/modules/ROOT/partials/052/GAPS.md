# TS-52 gap analysis

Gaps found comparing TS-52: Security and secrets management against the
following reference resources:

- https://blog.nelhage.com/post/computers-can-be-understood/

**Assessment.** One source, Nelson Elhage's "Computers Can Be Understood,"
was compared against this standard. It found a single gap, and that gap is
missing coverage rather than partial treatment: the standard says nothing
about systems-level security — memory safety, undefined behavior, and the
compiler and operating-system mitigations that constrain their exploitation.
This file was converted from the legacy format on 2026-08-13.

**Status:** 1 of 1 actionable gaps closed (2026-08-13). Converted from the
legacy format, and the one gap it recorded — systems-level security — closed
by a new "Memory safety and exploit mitigation" section. Nothing remains
open: 0 missing, 0 partial, 0 out-of-scope, 0 unresolved.

## Missing

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says that
      security reasoning often requires working across multiple layers of
      abstraction, because an attacker is not bound by the documented
      behavior of any one layer: the C specification says only that a buffer
      overflow is "undefined behavior," and turning one into remote code
      execution — or reasoning about countermeasures like ASLR and DEP —
      requires a deep understanding of how the compiler, libc, and hardware
      actually implement that abstract specification. The gap: no standard
      covers systems-level security — undefined behavior, memory-safety
      vulnerabilities, or hardware and OS exploit mitigations (ASLR, DEP) —
      nor the multi-layer reasoning required to understand them. Coverage
      check: TS-52 and TS-54 are application-security focused (third-party
      code review, encryption, secrets, auth, network and web-application
      security, STRIDE/OWASP), and a search for "undefined behavior,"
      "buffer overflow," "ASLR," "DEP," and "memory safety" returns no
      matches anywhere in `src/`. Recommend a new section in TS-52, placed
      after `09-web-application-security.adoc`, since no existing partial is
      about the topic. Cross-references: TS-54 (Threat modeling).

      **Resolved.** Closed by a new partial, `10-memory-safety.adoc`,
      "Memory safety and exploit mitigation," appended to the page after
      web-application security. It requires that components processing
      untrusted input be written in a memory-safe language, and that
      choosing C, C++, or an unsafe/FFI subset for such a component be a
      justified and recorded decision rather than a default. An "Undefined
      behavior" subsection draws the two security-relevant consequences: a
      compiler may delete a bounds or overflow check written after the
      operation it guards, so checks MUST test operands beforehand; and what
      a program actually does is decided by the compiler, libc, allocator,
      and hardware, so triage of a memory-safety defect MUST be carried out
      against the implementation rather than stopping at the specification's
      "undefined." The source is quoted directly for that argument. An
      "Exploit mitigations" subsection defines ASLR, DEP/NX, stack canaries,
      RELRO, and CFI, requires them on every released artifact, requires
      verification against the built binary rather than the build
      configuration, and carries an IMPORTANT block stating that a defect
      unexploitable under today's mitigations MUST NOT be recorded as fixed.
      A "Detecting memory-safety defects" subsection rules out SAST/DAST/SCA
      as the primary control — with an xref to the standard's own
      "Vulnerability scanning" section — and requires a sanitized CI test
      run plus continuous fuzzing of untrusted-input parsers, then requires
      such defects be triaged as vulnerabilities and assumed exploitable
      until analyzed. Cross-references TS-54 (Threat modeling) for modeling
      the trust boundary at which the unsafe component takes its input, as
      the item's own cross-reference field suggested. A TL;DR bullet was
      added to the page, and the source added to a new `== References`
      section — TS-52 had none before this run.

## Partial

(Converted from the legacy format on 2026-08-13. The original analysis
recorded no items of this kind — its single gap was missing coverage, not
partial treatment.)

## Out-of-scope

(Converted from the legacy format on 2026-08-13. The legacy format has no
concept of an out-of-scope item, and the original analysis recorded none.)

## Unresolved

(Converted from the legacy format on 2026-08-13. The legacy format has no
concept of an unresolved reference resource, and the original analysis
recorded none.)
