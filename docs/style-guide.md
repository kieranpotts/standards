# Style guide

This style guide defines the language, formatting, and structural conventions
for authoring the technical standards in this repository. It is the
authoritative reference for contributors and AI agents editing content under
`src/`.

For prose-level writing conventions that apply within any individual document —
voice, headings, terminology, citations — see
[TS-26: Technical Writing Style Guide](../src/026/README.adoc). For AsciiDoc
syntax specifics, see [TS-28: AsciiDoc](../src/028/README.adoc). The repository
structure and file layout are documented in [AGENTS.md](../AGENTS.md). The
[`template/`](../template/) directory is a representative entry with lorem-ipsum
body text that demonstrates the conventions below; use it as the starting point
for new standards.

## Language and tone

- All content MUST be written in American English (en-US).

- The target audience is experienced software engineers and technical leads.
  Content SHOULD assume familiarity with mainstream software development
  concepts. Foundational concepts do not need to be explained.

- Write in a direct, authoritative style. Avoid hedging language. State what the
  standard requires or recommends, and why — briefly.

- Use the RFC 2119 requirement keywords (MUST, SHOULD, MAY, etc.) in body prose
  to signal normative requirements, exactly as they are used throughout the
  existing standards.

## AsciiDoc formatting

- Every standard's `README.adoc` MUST begin with a level-1 title in the form
  `= TS-N: Title`, followed by `:toc: macro` and `:toc-title: Contents`
  attributes, then an introductory paragraph, then `toc::[]`, then the
  `include::` directives.

- Content files (`01-topic.adoc`, `02-topic.adoc`, etc.) MUST NOT contain a
  document-level title (level 0, `=`). They start with a level-1 section header
  (`=`), which becomes a level-2 heading when included with `[leveloffset=+1]`.

- All `include::` directives in a README MUST use the `[leveloffset=+1]`
  attribute.

- Cross-references to other standards MUST use relative AsciiDoc link syntax,
  and MUST be bold: `*link:../NNN/README.adoc[TS-N: Title]*`.

- Internal links MUST be bold; external links MUST NOT be. An internal link is
  one to another technical standard in this repository; everything else —
  including links to `github.com/kieranpotts` repositories — is external.

- A link MUST NOT be broken across lines. The whole macro — target, brackets,
  and link text — MUST sit on one source line, even where that puts the line
  over 80 characters. This overrides the line-length convention.

- Code blocks MUST specify the language where applicable: `[source,bash]`,
  `[source,sh]`, `[source,json]`, etc.

- Admonition blocks (TIP, NOTE, IMPORTANT, WARNING, CAUTION) SHOULD use the
  long-form open-block delimited syntax (`======`), not the single-line
  paragraph syntax.

- Use `''''` (four single-quotes on their own line) to insert a horizontal rule,
  eg. before a `== References` section.

- Quoted prose MUST use plain double quotes (`"quoted text"`). Do not use
  AsciiDoc's curly-quote syntax (`` "`quoted text`" ``).

- Backticks MUST NOT appear inside a quoted string in prose. Quote the phrase
  or set the term in monospace, never both:

  ```
  ✅ "list responses within 300 ms at the 95th percentile"
  ✅ The `Scenario Outline` keyword.
  ❌ "the `Scenario Outline` keyword"
  ```

  This applies to prose only. Backticks inside code blocks are untouched by
  this rule, including where the language being shown uses them as syntax.

- Internal cross-references between sections of the same standard MUST use xref
  syntax (`<<Section title>>`), not `link:` to the file. The section files are
  merged into a single document by `include::`, so a file-relative link resolves
  to the wrong place. Use `link:` only for cross-references to *other*
  standards.

  Prose references ("see the section on executable specifications") are
  acceptable for passing mentions. Prefer an xref where the reader is being
  directed to go and read the other section.

For the full AsciiDoc language reference, see
[TS-28: AsciiDoc](../src/028/README.adoc).

## Lists

- Numbered lists MUST use explicit Arabic numbering (`1.`, `2.`, `3.`), not the
  `.` shorthand. A blank line MUST separate each item.

- When a list item introduces a named term or step, the lead-in label MUST be
  bold and terminated with a period, followed by the description on the same
  line: `1. *Label.* Description.`. The same bold-lead-in form
  (`* *Label.* Description.`) applies to bulleted lists. Do not use the
  italic-plus-em-dash form (`_Label_ — description`) for lead-ins.

## File naming

- Content files MUST be named with a two-digit numeric prefix followed by a
  hyphen and a descriptive kebab-case name: `01-topic-name.adoc`.

- The prefix MUST be purely numeric. A letter suffix (`01a-`, `05b-`) MUST NOT
  be used to slot a new section between two existing ones — renumber the files
  that follow it instead. Section files are referenced by title through xrefs
  rather than by filename, so renumbering is cheap.

- Asset directories MUST be named `_/`.

- Subdirectory names MUST be prefixed with a two-digit number matching their
  position in the parent README's include order.

- File names MUST use only lowercase ASCII letters, digits, and hyphens.

## Content structure

- A standard's `README.adoc` MUST include all content files via `include::`
  directives in the order they should appear. There MUST NOT be content files in
  a standard's directory that are not included by the README – except examples
  (which MUST go in an `examples/` subdirectory).

- The introductory section in `README.adoc` SHOULD describe the scope and
  purpose of the standard, and SHOULD link to related standards where
  appropriate.

- A `== References` section MAY be added at the end of `README.adoc` (after
  `''''`) to list external sources. References MUST NOT be split into a separate
  content file — the `README.adoc` is their only home, so that every standard
  carries its references in the same place.

- Reference entries MUST follow the author-date convention specified in
  [TS-26 §12: Referencing](../src/026/12-referencing.adoc), which is a mix of
  the Chicago and Harvard styles:

  ```
  <author> (<year>). _<title>_. <publication>
  ```

  Applied to a standard's reference list, this gives a bulleted AsciiDoc
  hyperlink on the title, followed by a short descriptive annotation:

  ```asciidoc
  * Ubl, M (2020). https://www.industrialempathy.com/posts/design-docs-at-google/[_Design Docs at Google_].
    Industrial Empathy. — The primary source for the Google-style design-doc
    conventions used in this standard.
  ```

  The conventions from TS-26 §12 apply in full: surnames only where there are
  two or three authors, "et al" beyond three, and the publisher cited as author
  in preference to a byline for blog posts, news stories, and press releases.
  Where a work has no identifiable author, begin with the title.

  The trailing annotation is an addition to TS-26 §12, which does not provide
  for one. It is REQUIRED here, because a reference list in a technical standard
  has to tell a reader why the source is worth following. It begins with an em
  dash and a capital letter. A blank line MUST separate entries.

- Do not add content to stubs (standards with only a `README.adoc` containing
  placeholder text) unless explicitly asked to. Stubs are intentional
  placeholders for future work.

## Writing new content

- New section content MUST be placed in a new numbered `.adoc` file, not
  appended directly to `README.adoc`.

- When adding a new content file, the `include::` directive MUST be inserted
  into `README.adoc` in the correct position to maintain logical ordering.

- Do not reorder existing include directives unless explicitly asked to.

## Conventions

URLs containing variables are written according to
[IETF RFC 6570: URI Template](https://tools.ietf.org/html/rfc6570). For example,
a URL containing a variable called `account_id` would be shown as
`api.example.com/v1/accounts/{account_id}`.

Placeholders in code blocks and templates use angle brackets — `<placeholder>` —
per [TS-26 §11](../src/026/11-code-blocks.adoc). The exception is a URI template,
which follows RFC 6570 above. Markdown is also an exception: placeholders MUST
use square brackets (`[placeholder]`) because angle brackets are reserved for
raw HTML. See [TS-27](../src/027/08-code.adoc).

A literal `{...}` — a URI template variable, a shell `${var}` expansion, a
JSDoc `{type}` annotation, or similar — is safe inside a delimited block
(` ---- `), where AsciiDoc does not perform attribute substitution. But the
same text written inline in prose, in a table cell, or in a list item MUST
have its opening brace escaped as `\{...}`, otherwise Asciidoctor treats it as
a reference to a document attribute and logs "skipping reference to missing
attribute". The escape renders identically and keeps the real syntax intact —
do not switch such text to angle-bracket placeholder notation, which would
misrepresent it.

Where a standard documents a language that itself uses angle brackets — Gherkin
scenario outlines, for example — the two uses are indistinguishable on the page.
Say so explicitly in the surrounding prose rather than switching notation.

Named published standards MUST be cited with a version, and with a conformance
level where the standard defines one: "WCAG 2.2 Level AA", not "accessible";
TLS 1.3, not SSL/TLS. A standard named without a version is not a testable
threshold, and it ages badly.

Illustrative examples MUST NOT pin a real version number of a fast-moving tool
or runtime (Node.js, npm, TypeScript, etc.) where the point being made is a
policy or pattern, not a testable version requirement. State the policy in
prose (e.g. "the two most recent maintenance LTS releases") and use
placeholder notation (`<placeholder>`) for any version numbers in the
accompanying code example, so the standard does not need re-editing every time
the ecosystem moves on. This does not apply to a version cited as an actual
testable requirement (per the rule above), which MUST be a real number.
