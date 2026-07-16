# TS-28: AsciiDoc

This is a compact version of technical standard TS-28 for AI agents.

Use this when writing or reviewing AsciiDoc documents — file extensions, attributes, include directives, TOC, code blocks, images, admonitions, links, sections, lists, tables, keyboard/menu UI macros, conditional rendering, comments, extensions, and line length. AsciiDoc is RECOMMENDED for technical documentation (preferred over Markdown for technical writing, embedded diagrams, and publishing tooling). Covers Asciidoctor and Antora conventions.

Do NOT use this for sentence-level writing style (voice, formatting, terminology, citations) — see [TS-26: Technical Writing Style Guide](../026/AGENTS.md). For a complete language reference see the [Asciidoctor Documentation](https://asciidoctor.org/docs/).

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT,
OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

- **Prefer native AsciiDoc syntax over Markdown styles that happen to be
  supported by Asciidoctor.**

  Asciidoctor supports a subset of Markdown syntax as an alternative, but
  native AsciiDoc syntax is preferred.

- **Use the `.adoc` file extension.**

  `.adoc` SHOULD be used. `.asciidoc` MAY be used as an alternative. The
  extensions `.ad` and `.asc` MUST NOT be used.

- **Define all attributes in a contiguous block in the document header.**

  Attributes (`:name-of-an-attribute: value`) are variables whose values can be
  used throughout the document, increasing readability and making it easy to
  change content in one place. The document header is terminated by the first
  blank line. Reference attributes in the body with curly braces:
  `{name-of-an-attribute}`.

- **Use the include directive extensively to keep files small and modular.**

  `include::<path>/file[<attrlist>]` — the attrlist is OPTIONAL (eg.
  `leveloffset=+1` adjusts section levels of the included file). Documentation
  sites and books are _composed_ from many files included in one main file.
  Includes also allow reusing content (eg. code examples) in multiple places.

  **Antora conventions MUST be followed:** documents in
  `modules/<module-name>/pages/`, images in
  `modules/<module-name>/assets/images/`, examples in
  `modules/<module-name>/examples/`. When including, you MUST NOT use `pages`,
  `assets/image`, or `examples` in the path component — only the `<path>` bit
  (you MAY use `<module-name>` when linking to another module). If you include
  a standard page into another page, you MUST set the `page-partial` attribute
  in the included page's document header.

- **Use an auto-generated table of contents; do not manually maintain internal
  links.**

  Strongly RECOMMENDED. Simplest: `:toc:` in the header. For position control,
  use `:toc: macro` then `toc::[]` where you want the TOC. Other directives
  (`toc-title`, `toclevels`) configure the TOC.

- **Code blocks use `[source,<language>]` with `----` delimiters; the language
  is optional.**

  RECOMMENDED to write `plaintext` as the language for non-language code
  examples (disables syntax highlighting). For shell examples, distinguish
  `console` (prompt included — `>`, `%`, `$`, `#` may be used; highlighting
  applies only to commands after the prompt) from `bash` (standalone shell
  commands and scripts). For placeholder/prompt formatting conventions see
  [TS-26](../026/AGENTS.md).

- **Literal blocks (pre-formatted text) use `....` delimiters.**

  Literal paragraphs and blocks display text exactly as entered.

- **All images SHOULD have alternative text.**

  Inline: `image:<path>/name[alt text, <options>]`. Block-level:
  `image::<path>/name[alt text, <options>]`. Wrap alt text in single quotes
  (NOT double quotes — can break the Asciidoctor PDF generator) if it includes
  commas. Block-level images MUST be used for large graphics needing captions
  (centered by default; adjust with `align="center|left|right"`).

- **Use complex admonition syntax (RECOMMENDED); five types: NOTE, TIP,
  IMPORTANT, CAUTION, WARNING.**

  Simple: `<label>: Text...`. Complex (RECOMMENDED — stands out in plain text
  and supports nesting of tables, lists, literal blocks):

  ```
  [<label>]
  ====
  Text...
  ====
  ```

  For guidance on when to use each type and how sparingly, see
  [TS-26](../026/AGENTS.md).

- **Preserve line breaks with `+` at the end of the line.**

  A space followed by `+` immediately before the line break preserves it in
  paragraphs, lists, and tables. (Without this, adjacent lines combine into a
  single paragraph.)

- **Apply `%unbreakable` to an open block to prevent page breaks.**

  The attribute MUST be applied to an open block (`--` delimiters) that
  encapsulates the block-level content. Applying it directly to a quoted block
  (`____`) does not work.

- **External links: `http(s)://domain/path[Hyperlinked text]` (bracket part
  optional — URL itself becomes the link text if omitted).**

  The `link:` prefix is required only when the target is not a URI (AsciiDoc
  recognizes `http:` / `https:` as implicit link macros). Prevent auto-linking
  with a backslash prefix (`\https://...`). For long URLs, RECOMMENDED to define
  an attribute (prefixed with `link-`) and reference it. For URLs containing
  underscores, carets, or double quotes, see Asciidoctor's troubleshooting
  guide.

- **Internal links: bold RECOMMENDED for internal links only (to distinguish
  from external).**

  For internal bold links, the outer `*` style
  (`*link:../path[Hyperlinked text]*`) is recommended over
  `link:../path[*Hyperlinked text*]` as it is more reliable in editor preview
  mode. Use a link checker to audit for broken links. For effective link text
  guidance see [TS-26](../026/AGENTS.md).

- **Document titles SHOULD be title case; chapter names and headings SHOULD be
  sentence case (no termination punctuation).**

  Document title: `=` (level 0, top of the header). Section titles: `==` (level
  1) through `======` (level 6) — the number of `=` signs is the nesting level
  (0-based index). Section numbering MUST be in single steps (jumping from `=`
  to `===` produces a warning). Sections automatically create anchors and TOC
  entries; use `[discrete]` above a section to exclude it from the TOC while
  keeping its anchor. Block titles: a line beginning with `.` immediately
  followed by the title text, placed above the element (displayed below for
  figures/images).

- **Lists: use `*` prefix (not Markdown-style `-`); Markdown-style list markers
  SHOULD NOT be used.**

  Nested lists use multiple `*` signs per nesting level. Markdown-style hyphen
  (`-`) is supported but does NOT support nested lists (indentation-style
  nesting produces a flat list). When list items span multiple lines, indent
  continuation lines by at least one space and leave a blank line before the
  next item. A common pattern: bold a short lead-in term terminated by a
  full-stop (best accessibility) followed by a full sentence. For key-value
  pair lists, place the colon inside the bold marker (`**Status:** Active`).
  For numbered-vs-bulleted guidance and punctuation/parallelism see
  [TS-26](../026/AGENTS.md).

- **Tables are delimited by `|===` with cells separated by `|`.**

  Column widths and options via the attribute line
  (eg. `[width="80%",cols="30%,70%",options="header"]`). Columns may be written
  horizontally or underneath each other.

- **Keyboard shortcuts and UI button text: `kbd:[key(+key)*]` and
  `btn:[text]`.**

  Examples: `kbd:[Ctrl+T]`, `kbd:[Ctrl+Shift+N]`, `btn:[OK]`. Menu selections
  require the `:experimental:` attribute to be set — `menu:Settings[Admin >
  Apps]`. You MUST set `:experimental:` to enable the UI macros.

- **Conditional rendering: `ifeval::["{format}" == "html"]` ... `endif::[]`.**

  Handy for hiding content from one output format (eg. PDF) while showing it in
  another (eg. HTML).

- **Comments: `//` for single-line (preferred); `////` for block comments.**

  Use comments to leave information for other documentation maintainers.

- **Asciidoctor extensions (written in Ruby) are generally discouraged.**

  They can make it harder to process AsciiDoc files with different tools, and
  source files become less portable.

- **Lines SHOULD NOT exceed 80 characters; MUST NOT exceed 160 (except in very
  special circumstances like tables or unbreakable URLs).**

  Content longer than 80 chars SHOULD be soft-wrapped (continued on the next
  line without special line-break syntax — adjacent lines combine into a single
  rendered line). A soft wrap MUST NOT be inserted within an inline formatting
  unit (eg. bold `*` or italic `_`) to preserve the formatting markers alongside
  the text they format. The 80-char constraint ensures files render identically
  in every editor regardless of line-wrapping settings. For forced line breaks
  use the `+` syntax (see above).

## References

- [TS-28 source](README.adoc)
- [TS-26: Technical Writing Style Guide](../026/AGENTS.md)
- [Asciidoctor Documentation](https://asciidoctor.org/docs/)
- [AsciiDoc Syntax Quick Reference](https://docs.asciidoctor.org/asciidoc/latest/syntax-quick-reference/)