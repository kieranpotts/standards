# TS-25 gap analysis

Gaps found comparing TS-25: *Technical Documentation* against the following
reference resources:

- `__TODO__/documentation-standards.adoc`
- `__TODO__/docs/README.md`
- `__TODO__/docs/formats.md`
- `__TODO__/docs/language.md`

**Assessment.** The reference set is small — four short files, much of it
commented-out TODO notes (an AsciiDoc `////` block in `documentation-standards.adoc`
and HTML `<!-- -->` comments in `docs/README.md`). Most of its substantive
points — the value of up-to-date documentation, preferring small modular
documents, and the use of Markdown/AsciiDoc — are already covered by TS-25,
usually more deeply. The genuine gaps concentrate in two areas: explicit
format-selection guidance (a default format, and when to prefer AsciiDoc), and
the "document-first" API design idea. A few items plausibly belong in sibling
standards (TS-26 for language conventions, TS-28 for AsciiDoc feature detail)
and are flagged out-of-scope.

**Status:** First run, 2026-08-05. Re-verified 2026-08-05 against the
same reference set; the standard has not changed, so all gaps remain open.

## Missing

- [ ] `__TODO__/docs/formats.md:8` — Markdown as the default documentation
      format, with the rationale that it has the widest support in development
      tools (IDEs, package registries). The standard names Markdown and
      AsciiDoc (`20-tooling.adoc:38-44`, `14-docs-as-code.adoc:16-19`) but does
      not pick a default or give the tooling-support rationale. Recommend
      placing at `20-tooling.adoc:38` (Markup languages section).

- [ ] `__TODO__/docs/formats.md:10` — AsciiDoc preferred for comprehensive
      technical documentation where more control over the publishing format is
      wanted, e.g. public websites for open source projects. The standard
      mentions AsciiDoc but does not state when it is preferred over Markdown
      or give the "comprehensive docs / publishing control" use case.
      Recommend placing at `20-tooling.adoc:38` (Markup languages section), or a
      new "Choosing between Markdown and AsciiDoc" subsection.

- [ ] `__TODO__/docs/README.md:10` (HTML comment) — "Document-first approach
      helps to design better APIs": using documentation as an API design tool.
      The standard does not address this; `08-descriptive-versus-prescriptive.adoc`
      in fact argues documentation should _follow_ implementation, which is in
      tension with the document-first idea. The "documentation as design
      lever" perspective is missing. Recommend placing at
      `05-api-documentation.adoc:1` or a new section, explicitly reconciling it
      with the descriptive-not-prescriptive rule.

## Partial

- [ ] `__TODO__/documentation-standards.adoc:4` (commented) — "Agile methods
      are not opposed to documentation, only to low-value documentation." The
      standard covers the substance (low-value documentation is the problem, not
      documentation itself) in `11-when-not-to-document.adoc:1`, but does not
      frame it against Agile methods or address the common "Agile means no
      docs" misconception. The standard omits the Agile context/framing the
      reference provides.

- [ ] `__TODO__/docs/formats.md:14` — Scott Chacon, "Living the future of
      technical writing" (2012), on AsciiDoc and source control for the second
      Pro Git edition. The standard's References (`README.adoc:45-48`) lists
      only Write the Docs; this article is not referenced. A borderline item —
      a single essay — but it is a concrete reference the standard could cite.

## Out-of-scope

- [ ] `__TODO__/docs/formats.md:10` — Enumeration of AsciiDoc capabilities
      (table formatting, cross references, indexing, callouts, source code
      examples). Feature-level detail of the AsciiDoc language belongs in
      TS-28 (*AsciiDoc*); TS-25 correctly links out to TS-28 rather than
      duplicating it. Flagged for the user to confirm.

- [ ] `__TODO__/docs/formats.md:10` — AsciiDoctor tooling transforming AsciiDoc
      to a wide range of output formats beyond HTML. Tooling-level detail of
      the AsciiDoc ecosystem belongs in TS-28 (*AsciiDoc*). Flagged for the
      user to confirm.

- [ ] `__TODO__/docs/language.md:3` — "All our technical documentation MUST be
      written in American English." This is a sentence-level writing convention
      (language/terminology), which `README.adoc:14-18` explicitly defers to
      TS-26 (*Technical Writing Style Guide*). It plausibly sits outside
      TS-25's stated scope (informational architecture and lifecycle, not
      prose-level conventions). Flagged for the user to confirm.

## Unresolved

- None. All four reference files were read in full.