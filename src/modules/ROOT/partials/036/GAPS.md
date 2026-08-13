# TS-36 gap analysis

Gaps found comparing TS-36: ECMAScript (JavaScript/TypeScript) against the
following reference resources:

- https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture

**Assessment.** The single reference resource is The Pragmatic Engineer's
write-up of Bluesky's engineering culture, and the one gap it yielded is a
missing architectural decision rather than a missing coding convention: the
standard mandates TypeScript, but nowhere states the case for — or the limits
of — using it across every tier of an application. Converted from the legacy
format on 2026-08-13.

**Status:** 1 of 1 actionable gaps closed (2026-08-13). Converted from the
legacy format and worked in the same run; the single gap is closed by a new
"One language across the stack" section in `12-architecture-and-design.adoc`.
Nothing remains open: 0 missing, 0 partial, 0 out-of-scope, 0 unresolved.

## Missing

- [x] https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
      says Bluesky uses TypeScript for the backend, frontend, and mobile apps
      so engineers can work across the stack without switching languages,
      citing shared schema understanding, code-generation ergonomics, and
      rapid prototyping. The gap: TS-36 does not address the full-stack
      single-language strategy or its trade-offs. This may be out of scope
      for TS-36 (closer to TS-5/TS-7), but no standard in the index clearly
      owns it. Coverage check: TS-36 is a coding-conventions standard, and a
      search of its architecture-and-design section for shared-language /
      full-stack / isomorphic concepts returned no matches — the standard
      addresses how to write ECMAScript, not the architectural decision to
      standardize on one language across the stack. Recommend a new section
      in `12-architecture-and-design.adoc`.
      Cross-references: TS-5 (Application architecture).

      **Resolved.** Closed by a new "One language across the stack" section
      in `12-architecture-and-design.adoc`, placed ahead of "API design" as
      the broadest of the standard's architectural decisions. It states that
      TypeScript SHOULD be the language of every tier and of the packages
      shared between them, and gives the four reasons the source cites — one
      definition of the contract, code generation off the schema, engineer
      mobility across tiers, and prototyping speed — then spends the rest of
      the section on the limits. Three subsections carry those: "Share
      contracts, not implementations" restricts sharing to host-agnostic code
      and warns that a shared package couples every dependent tier to one
      release cadence, which an installed mobile client cannot follow;
      "A shared type is not a validated input" names the strategy's main
      failure mode, that TypeScript types are erased at compile time, so
      every value crossing into the program MUST still be validated at
      runtime, with the static type derived from the validator rather than
      declared beside it; and "Where the strategy stops" makes the default
      overridable for a tier ECMAScript serves poorly, and requires the two
      monoculture consequences — one supply chain and one runtime failure
      mode — to be accounted for. Cross-references TS-5 (Application
      architecture) for how the tiers are divided in the first place, and
      TS-11 (Versioning) for shared-package compatibility, plus the
      standard's own "Universal JavaScript" and "Dependency management"
      sections. Source added to the page's `== References`.

      On the scope caveat in the item above: the section was written into
      TS-36 rather than TS-5 or TS-7 because the decision is specifically
      about the ECMAScript language, and TS-36 already makes language-level
      mandates of exactly this kind ("TypeScript MUST be used to enforce
      strong typing across all JavaScript code", and the "Using a subset of
      TypeScript" section). TS-5 owns how tiers are divided, not which
      language they are written in, and the new section defers to it by
      xref.

## Partial

(Converted from the legacy format; the original analysis recorded no partial
items.)

## Out-of-scope

(Converted from the legacy format, which has no concept of out-of-scope
items; the original analysis recorded none.)

## Unresolved

(Converted from the legacy format, which has no concept of unresolved
resources; the original analysis recorded none.)
