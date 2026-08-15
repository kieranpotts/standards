# TS-27 gap analysis

Gaps found comparing TS-27: Markdown against the following reference
resources:

- `__TODO__/027/markdown.adoc` (a stub whose only content is a TODO
  comment pointing to the URL below; it contributes no content of its own)
- `__TODO__/027/_markdown.md` (the adam-p markdown-here cheatsheet)
- https://google.github.io/styleguide/docguide/style.html (Google's Markdown
  style guide — referenced by `markdown.adoc`)

**Assessment.** The cheatsheet (`_markdown.md`) is a syntax tour that the
standard already covers more prescriptively; it yielded only a few small
syntax omissions (reference-style images, embedded media, inline Markdown in
table cells). The Google style guide is a broader authoring guide that
overlaps the standard on syntax but adds substantive guidance the standard
omits — chiefly around heading naming, link path conventions, line-length
exceptions, list numbering nuance, and code-in-lists. Several Google
sections are documentation process/philosophy or capitalization guidance
that plausibly belong to TS-26 (Technical writing style guide) rather than
this syntax-focused standard; those are flagged out-of-scope.

**Status:** 15 of 15 actionable gaps closed (2026-08-13). All six `## Missing`
and all nine `## Partial` items are resolved. What remains open: five
`## Out-of-scope` items awaiting the user's confirm-or-overrule decision, and
one `## Unresolved` item already dismissed (the stub file contributed
nothing, and the Google URL it points to was fetched and is fully reflected
in the closed items above).

## Missing

- [x] https://google.github.io/styleguide/docguide/style.html#use-unique-complete-names-for-headings
      is not addressed anywhere in the standard. Google recommends unique,
      fully descriptive heading text because link anchors are constructed
      from headings, so duplicate or vague headings produce unclear anchors.
      Recommend placing at `src/modules/ROOT/partials/027/04-headings.adoc` (new subsection).

      **Resolved.** Closed by a new "Unique and descriptive headings"
      subsection in `04-headings.adoc`. States that headings SHOULD be
      unique and fully descriptive even across sections, explains that most
      renderers derive link anchors from heading text, and warns that the
      numeric-suffix disambiguation renderers fall back to for duplicate
      headings (`#configuration-1`) is fragile because it depends on
      document order. Source added to the page's `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#use-a-single-h1-heading
      is not addressed anywhere in the standard. Google recommends a single
      H1 as the document title (ideally matching the filename), with all
      subsequent headings starting at H2. The standard's heading rules cover
      ATX syntax, spacing, blank lines, and level-stepping, but say nothing
      about restricting H1 to one per document. Recommend placing at
      `src/modules/ROOT/partials/027/04-headings.adoc` (new subsection).

      **Resolved.** Closed by a new "Single top-level heading" subsection in
      `04-headings.adoc`. States that a document SHOULD have a single level 1
      heading used as the title, matching or closely reflecting the file
      name, with all subsequent headings starting at level 2, and explains
      that a second H1 confuses renderers that treat the first H1 as the
      document title. Source added to the page's `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#escape-newlines
      is not addressed anywhere in the standard. Google recommends escaping
      newlines in multi-line shell/command snippets with a trailing backslash
      so the snippet copies and pastes as a single command. The standard's
      code section (`src/modules/ROOT/partials/027/08-code.adoc`) covers fencing and language
      identifiers but not newline escaping for copy-paste. Recommend placing
      at `src/modules/ROOT/partials/027/08-code.adoc` (new subsection).

      **Resolved.** Closed by a new "Escaping newlines in shell snippets"
      subsection in `08-code.adoc`. States that a multi-line shell snippet
      meant to be copy-pasted as one command SHOULD escape its newlines with
      a trailing backslash, gives a worked `gcloud` example, and notes the
      exception for output examples and read-only snippets. Source added to
      the page's `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#use-explicit-paths-for-links-within-markdown
      and https://google.github.io/styleguide/docguide/style.html#avoid-relative-paths-unless-within-the-same-directory
      are not addressed anywhere in the standard. Google recommends using
      explicit paths (with the `.md` extension) for links to other Markdown
      documents, and avoiding `../` relative paths outside the same
      directory. The standard's links section (`src/modules/ROOT/partials/027/09-links.adoc`)
      covers link syntax, titles, autolinks, reference-style, and URL
      encoding, but nothing about inter-document link path conventions.
      Recommend placing at `src/modules/ROOT/partials/027/09-links.adoc` (new subsection).

      **Resolved.** Closed by a new "Explicit paths for internal links"
      subsection in `09-links.adoc`. States that a link to another file in
      the same repository SHOULD use an explicit path including the `.md`
      extension, and that `../` chains climbing outside the current
      directory SHOULD be avoided in favor of a path rooted at a stable
      location, since a long relative chain is fragile if either file moves.
      Source added to the page's `== References`.

- [x] `__TODO__/027/_markdown.md` (Images section) shows reference-style
      images — `![alt text][logo]` paired with a `[logo]: url "title"`
      definition — which the standard does not address. The standard's
      images section (`src/modules/ROOT/partials/027/10-images.adoc`) covers inline image syntax,
      alt text, linking an image, and HTML `<img>` for sizing, but not the
      reference-style image form. Recommend placing at
      `src/modules/ROOT/partials/027/10-images.adoc`.

      **Resolved.** Closed by a new "Reference-style images" subsection in
      `10-images.adoc`. Shows the `![Alt text][logo]` plus `[logo]: url
      "title"` form, cross-references the equivalent link-level pattern
      already documented in "Reference-style links", and notes it is most
      useful for an image reused in multiple places or where an inline URL
      would disrupt the prose.

- [x] `__TODO__/027/_markdown.md` (Embedded Media section) shows a
      pattern for embedding video (e.g. YouTube) via an HTML `<a>` wrapping
      an `<img>` thumbnail, which the standard does not address. The
      standard's HTML section (`src/modules/ROOT/partials/027/16-html.adoc`) mentions `<details>`
      disclosure blocks, image dimensions, and text color as HTML use cases,
      but not embedded media. Recommend placing at `src/modules/ROOT/partials/027/16-html.adoc`
      (or a new section).

      **Resolved.** Closed by a new "Embedding video" subsection in
      `16-html.adoc`. States that Markdown has no native video-embed syntax
      and most renderers strip `<video>`/`<iframe>` embeds, shows the
      linked-thumbnail `<a>` wrapping `<img>` pattern, and notes this keeps
      the document portable and avoids embedding third-party iframes
      directly.

## Partial

- [x] https://google.github.io/styleguide/docguide/style.html#character-line-limit
      covers line-length exceptions more thoroughly than
      `src/modules/ROOT/partials/027/18-line-length.adoc:3` — specifically, Google explicitly lists
      links, tables, headings, and code blocks as exceptions to the
      80-character rule, with a worked example showing text wrapped around a
      long link. The standard only calls out tables and long URLs as
      exceptions (lines 12–14), and does not mention headings or code blocks.

      **Resolved.** Closed by a new paragraph in `18-line-length.adoc`,
      after the existing 160-character ceiling rule. States that a heading
      MUST NOT be wrapped across lines (Markdown has no heading continuation
      syntax), and that a fenced code block's content MUST be reproduced
      verbatim including any long line, since reformatting would misrepresent
      the code being shown. Source added to the page's `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#use-lazy-numbering-for-long-lists
      covers ordered-list numbering more thoroughly than
      `src/modules/ROOT/partials/027/07-lists.adoc:20-25` — specifically, Google recommends "lazy"
      numbering (repeating `1.` for every item) for long or frequently-changed
      lists, and full sequential numbering only for small, stable lists. The
      standard gives a single blanket rule that numbers SHOULD be sequential
      in source, with no allowance for lazy numbering of mutable lists.

      **Resolved.** Closed by a new paragraph in `07-lists.adoc`, directly
      after the existing sequential-numbering note. States that sequential
      numbering is RECOMMENDED for short, stable lists, and lazy numbering
      (repeating `1.`) is RECOMMENDED for long or frequently-edited lists,
      with a worked example, and explains that lazy numbering avoids noisy
      diffs and off-by-one mistakes when items are inserted or removed mid
      list. Source added to the page's `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#nest-codeblocks-within-lists
      covers code blocks inside list items more thoroughly than
      `src/modules/ROOT/partials/027/07-lists.adoc:31-44` — specifically, Google shows that a
      fenced code block inside a list item must be indented to align with the
      item content (and gives the indented-code-block alternative). The
      standard's continuation guidance is generic ("indent continuation
      lines to align with the first line") and never addresses fenced code
      blocks within lists, which are a common source of list-breaking.

      **Resolved.** Closed by a new paragraph and worked example in
      `07-lists.adoc`, directly after the existing continuation-indent
      guidance. States that a fenced code block inside a list item MUST be
      indented to the same column as the item's own content or CommonMark
      treats it as ending the list, shows a worked example, and notes the
      four-space indented-code-block alternative is valid but fenced blocks
      remain RECOMMENDED per the "Code" section. Source added to the page's
      `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#use-reference-links-for-long-links
      (and the surrounding reference-link subsections) cover reference-style
      links more thoroughly than `src/modules/ROOT/partials/027/09-links.adoc:43-57` —
      specifically, Google gives guidance on when reference links help (long
      links that would disrupt surrounding text, links inside tables, the
      same destination repeated multiple times) and when they do not (short
      links). The standard only says reference-style links "can improve
      readability in documents that contain many long URLs."

      **Resolved.** Closed by a new paragraph in the "Reference-style links"
      section of `09-links.adoc`. States the specific cases where a
      reference-style link helps — a long URL, a link inside a table cell
      where an inline URL breaks column alignment in source, or a
      destination reused more than once — and recommends an inline link by
      default for a short, single-use link. Source added to the page's
      `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#define-reference-links-after-their-first-use
      covers reference-definition placement more thoroughly than
      `src/modules/ROOT/partials/027/09-links.adoc:56-57` — specifically, Google recommends
      placing definitions just before the heading that follows their first
      use (treating a section like a page), and at the end of the document
      only for definitions reused across multiple sections. The standard
      only offers "immediately after the paragraph that uses them or at the
      end of the document," with no section-aware guidance.

      **Resolved.** Closed by extending the existing reference-definition
      sentence in the "Reference-style links" section of `09-links.adoc`.
      Recommends placing a definition just before the next heading following
      its first use, treating each section like a small page, and reserves
      end-of-document placement for labels reused across multiple sections.
      Source added to the page's `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#use-informative-markdown-link-titles
      covers link text quality more thoroughly than `src/modules/ROOT/partials/027/09-links.adoc`
      — specifically, Google recommends writing the sentence naturally and
      wrapping the most descriptive phrase as the link, and warns against
      "here", "link", or bare-URL-as-link-text. The standard describes the
      title attribute as a tooltip but says nothing about link text quality.
      (This overlaps TS-26: Technical writing style guide, which the
      standard already defers to for prose style — flagged for the user to
      decide whether it belongs here or there.)

      **Resolved.** Closed by a new "Link text quality" section in
      `09-links.adoc`, since the guidance is Markdown-syntax-adjacent (how
      link text is written into the `[text](url)` construct) rather than
      general prose style, distinguishing it from TS-26's remit. States that
      link text SHOULD describe the destination, not the click action,
      gives a worked "here" versus descriptive-phrase example, and notes the
      accessibility rationale (screen readers navigating link lists out of
      context) and the print/URL-change rationale. Source added to the
      page's `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#images
      covers image usage more thoroughly than `src/modules/ROOT/partials/027/10-images.adoc` —
      specifically, Google recommends using images sparingly, preferring
      simple screenshots, and reaching for an image only when it is easier to
      show a reader something than to describe it (e.g. UI navigation). The
      standard covers alt text and syntax but gives no usage guidance.

      **Resolved.** Closed by a new "When to use images" section in
      `10-images.adoc`. States that images SHOULD be used sparingly, favors
      simple screenshots over composited graphics, and recommends reaching
      for an image only where it is genuinely easier to show something than
      describe it; also notes images are not searchable or diffable, and
      defers to AsciiDoc for diagrams. Source added to the page's
      `== References`.

- [x] https://google.github.io/styleguide/docguide/style.html#tables
      covers when to prefer a list over a table more thoroughly than
      `src/modules/ROOT/partials/027/13-tables.adoc:25-28` — specifically, Google gives decision
      criteria (avoid a table when the data could be a list) and warns about
      poor column distribution, unbalanced row/column ratios, and rambling
      cell prose, with a worked table-to-list rewrite. The standard only
      says tables "SHOULD be used sparingly" and defers complex tables to
      AsciiDoc.

      **Resolved.** Closed by a new "Tables versus lists" section in
      `13-tables.adoc`. Gives decision criteria for when a table is a poor
      fit — a column with only one or two distinct values, a heavily skewed
      row/column ratio, or full-sentence cell content — with a worked
      table-to-list rewrite, and states a table earns its place only where
      the reader needs to compare values across two or more dimensions at a
      glance. Source added to the page's `== References`.

- [x] `__TODO__/027/_markdown.md` (Tables section) notes that inline
      Markdown (emphasis, code) renders inside table cells, which
      `src/modules/ROOT/partials/027/13-tables.adoc:25-27` omits — specifically, the standard
      states that block-level elements cannot be placed inside cells, but
      does not affirm that inline Markdown (italics, bold, code, links)
      does work within cells.

      **Resolved.** Closed by a new paragraph and worked example directly
      after the existing block-level-elements constraint in
      `13-tables.adoc`. States that inline Markdown formatting — emphasis,
      bold, inline code, and links — MAY be used within a table cell and
      renders as expected, and distinguishes this explicitly from the
      block-level restriction already documented.

## Out-of-scope

- [ ] https://google.github.io/styleguide/docguide/style.html#minimum-viable-documentation
      and https://google.github.io/styleguide/docguide/style.html#better-is-better-than-best
      cover documentation process philosophy (keep docs fresh, delete cruft,
      review etiquette, the "better/best rule"). This sits outside this
      standard's stated purpose — TS-27 is a Markdown syntax/authoring
      standard, and documentation process guidance belongs to TS-26
      (Technical writing style guide). Flagged for the user to confirm or
      overrule.

- [ ] https://google.github.io/styleguide/docguide/style.html#capitalization
      covers preserving the original capitalization of product, tool, and
      binary names (e.g. `Markdown` not `markdown`). This is a prose writing
      convention that belongs to TS-26 (Technical writing style guide), which
      TS-27 already defers to. Flagged for the user to confirm or overrule.

- [ ] https://google.github.io/styleguide/docguide/style.html#capitalization-of-titles-and-headers
      covers title/heading capitalization by deferring to the Google
      Developer Documentation Style Guide. This is a writing-style concern
      belonging to TS-26, not a Markdown syntax rule. Flagged for the user to
      confirm or overrule.

- [ ] https://google.github.io/styleguide/docguide/style.html#document-layout
      recommends a document skeleton (`# Document Title`, short introduction,
      `[TOC]`, `## Topic`, `## See also`). This is document-structure
      guidance that overlaps TS-26, and parts of it rely on the Gitiles-only
      `[TOC]` directive. TS-27 deliberately positions generated tables of
      contents as a "when not to use Markdown" case (`src/modules/ROOT/partials/027/01-overview.adoc:21-28`),
      directing such needs to AsciiDoc. Flagged for the user to confirm or
      overrule.

- [ ] https://google.github.io/styleguide/docguide/style.html#table-of-contents
      recommends the `[TOC]` directive (a Gitiles-specific extension). TS-27
      explicitly excludes generated TOCs from Markdown's scope
      (`src/modules/ROOT/partials/027/01-overview.adoc:21-28`), so this is a deliberate scope
      disagreement rather than a gap. Flagged for the user to confirm or
      overrule.

- [ ] `__TODO__/027/_markdown.md` (References) links to John Gruber's
      original 2004 Markdown spec. TS-27 deliberately avoids the original
      Markdown.pl dialect (`src/modules/ROOT/partials/027/02-flavors.adoc:20-22`) and recommends
      GFM/CommonMark instead, so referencing the original spec as a resource
      is out of step with the standard's stated stance. Flagged for the user
      to confirm or overrule.

## Unresolved

- [x] `__TODO__/027/markdown.adoc` contributed no content of its own —
      it is a stub containing only a TODO comment that points to the Google
      style guide URL. The Google URL was fetched successfully and its
      content is reflected in the findings above; the stub file itself added
      nothing further.

      **Resolved, 2026-08-15.** The `__TODO__/` tree was found to still
      exist locally (gitignored, not actually removed). Re-confirmed
      `markdown.adoc` is genuinely just the TODO stub described above. Its
      sibling in the same directory, `__TODO__/027/_markdown.md` (not
      previously cited in this file), was also read: it is the well-known
      "adam-p/markdown-here" basic-Markdown cheat sheet (headers, emphasis,
      lists, links, images, code, tables, blockquotes, horizontal rules,
      inline HTML, embedded media). Compared against TS-27's current
      content — every one of those topics already has its own dedicated
      partial (`04-headings.adoc` through `17-footnotes.adoc`), each more
      detailed and GFM/CommonMark-specific than the cheat sheet's generic
      syntax examples. No new gap found.