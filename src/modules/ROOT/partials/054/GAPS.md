# TS-54 gap analysis

Gaps found comparing TS-54: Threat modeling against the following reference
resources:

- https://blog.nelhage.com/post/computers-can-be-understood/

**Assessment.** A single source, Nelson Elhage's _Computers Can Be
Understood_, was compared against this standard, and it found one gap:
missing coverage of the systems level — memory-safety defects, the
undefined-behavior-to-exploit chain, and the hardware and OS exploit
mitigations that bear on it — which the standard's application-layer
framing (STRIDE, OWASP) does not reach. The same gap is recorded, in
identical wording, in `src/modules/ROOT/partials/052/GAPS.md`. This file was
converted from the legacy format on 2026-08-13.

**Status:** 1 of 1 actionable gaps closed (2026-08-13). Converted from the
legacy format, and the systems-level security gap closed by new
"Systems-level threats" and "Memory safety and exploit mitigations" sections
in `05-identifying-threats.adoc`. Remaining: 0 missing, 0 partial, 0
out-of-scope awaiting the user, 0 unresolved. This file is fully worked.

## Missing

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says that
      security reasoning often requires working across multiple abstraction
      layers — the C spec calls a buffer overflow "undefined behavior," but
      turning one into RCE, or reasoning about mitigations like ASLR and
      DEP, requires understanding the compiler, libc, and hardware
      implementation. The gap: no standard covers systems-level security —
      undefined behavior, memory-safety vulnerabilities, or hardware/OS
      exploit mitigations — and the multi-layer reasoning required to
      understand them. Coverage check: TS-54 is application-security focused
      (STRIDE/OWASP threat categories); a search for "undefined behavior,"
      "buffer overflow," "ASLR," "DEP," and "memory safety" returns no
      matches. Recommend placing in `05-identifying-threats.adoc`, as a new
      section alongside the existing framework-based threat identification
      guidance. Cross-references: TS-52 (Security and secrets management).

      **Resolved.** Closed by two additions to `05-identifying-threats.adoc`:
      a "Systems-level threats" section, and a "Memory safety and exploit
      mitigations" subsection under the existing "Prompt questions" section.
      The first states that a system carrying native code MUST be modeled
      below the application layer, explains why via the source's example —
      the C standard classifies a buffer overflow only as undefined behavior,
      so whether it yields a crash, a leak, or RCE is decided by the
      compiler, allocator, libc, and hardware, and a specification-level
      model therefore cannot rate exploitability — and draws two rules from
      it: exploitability MUST be rated against the implementation, with an
      unreasoned defect rated exploitable rather than treated as a mere
      correctness bug; and ASLR, DEP/NX, stack canaries, CFI, hardened
      allocators, and PIE MUST be recorded as countermeasures rather than
      remediation, because each has a known bypass and leaves non-zero
      residual risk, so the defect stays open in the risk register. It names
      elimination — memory-safe languages, and sandboxing native code that
      cannot be replaced — as the only mitigation that removes the threat
      class, and requires a workshop that finds no native code to record that
      as an explicit scope finding, qualified by the native code inherited
      through runtimes, parsers, and compression libraries. The second adds
      eight workshop prompts across memory safety (unsafe components at a
      trust boundary, the classic defect classes, fuzzing and sanitizers,
      TOCTOU) and exploit mitigations (mitigation flags verified in the build
      pipeline, availability of CFI and hardened allocators, what one further
      primitive would defeat each mitigation, and sandbox isolation).
      Cross-references TS-52 (Security and secrets management) for the
      supply-chain concerns that inherited native code carries. Source added
      to a new `== References` section on the page. Note that this same gap
      is also recorded, verbatim, in
      `src/modules/ROOT/partials/052/GAPS.md`; what is written here is the
      threat-modeling half — how to identify and rate these threats in a
      workshop — and the security controls themselves remain TS-52's to
      cover.

## Partial

(Converted from the legacy format. The original analysis recorded no partial
items — its single finding was classified as missing.)

## Out-of-scope

(Converted from the legacy format, which has no concept of out-of-scope
items. The original analysis recorded none.)

## Unresolved

(Converted from the legacy format, which has no concept of unresolved
resources. The original analysis recorded none; its one source fetched
successfully.)
