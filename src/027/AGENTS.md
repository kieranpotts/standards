# TS-27: Markdown

This is a compact version of technical standard TS-27 for AI agents.

Use this when writing or reviewing Markdown documents — `README` files,
changelogs, PR descriptions, issue comments, co-located code/API docs, and
chat messages.

Do NOT use this for technical documentation that needs tables of contents,
cross-references, file includes, admonitions, diagrams, or conditional
rendering. Use [TS-28: AsciiDoc](../028/AGENTS.md) for those cases.

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

-   **Target a single, well-specified dialect.**

    GitHub Flavored Markdown (GFM) is RECOMMENDED. GFM is a strict superset
    of the CommonMark specification, adding tables, strikethrough, task lists,
    and autolinks. Documents SHOULD be valid CommonMark at minimum. Avoid
    dialects not backed by a formal specification (eg. the original
    Markdown.pl) and non-portable proprietary extensions.

-   **Use the `.md` file extension.**

    `.markdown`, `.mdown`, and `.mkd` MAY be used; `.md` is preferred.
    Tool-specific extensions MAY be used where a tool requires them.

-   **Use ATX-style headings only.**

    One to six `#` followed by a single space and the text. Setext-style
    headings (underlining text with `=` or `-`) SHOULD NOT be used. A single
    space MUST be between the `#` and the text. A blank line SHOULD precede
    and follow every heading. Heading levels MUST increase by single steps
    (no skipping from level 1 to level 3).

-   **Do not indent paragraphs.**

    Leading indentation of four or more spaces may be parsed as a code block.
    Separate paragraphs with blank lines.

-   **Use hard line breaks sparingly.**

    A hard line break (`<br>`) is two or more trailing spaces or a trailing
    backslash. Prefer separate paragraphs or lists. Be aware trailing
    whitespace is invisible in most editors.

-   **Use asterisks, not underscores, for emphasis.**

    Underscores inside a word are not interpreted as emphasis by some
    processors; asterisks are reliable in all positions. `*italic*`, `**bold**`,
    `***bold and italic***`. GFM strikethrough uses `~~`. Do not nest emphasis
    unnecessarily or apply it to whole paragraphs.

-   **Use one list marker consistently.**

    Unordered lists use `-` plus a single space. Do not mix `-`, `*`, `+`
    within a list. Ordered lists use a number, period, single space; numbers
    SHOULD be sequential in source even though CommonMark renumbers output.
    Nested list indentation MUST be consistent; four spaces per nesting level
    is RECOMMENDED. Continuation paragraphs/blocks in a list item are indented
    four spaces (or marker-width + trailing space). GFM task lists (`- [x]`,
    `- [ ]`) MAY be used where supported.

-   **Prefer fenced code blocks.**

    Fenced blocks (three backticks) are RECOMMENDED over indented code blocks.
    A language identifier SHOULD follow the opening fence for syntax
    highlighting; use `text` or `plaintext` to disable highlighting. Inline
    code uses single backticks; double backticks for code containing backticks.

-   **Write links as `[text](url)`.**

    An optional title in double quotes may follow the URL. Bare URLs/email
    SHOULD be wrapped in `<...>` to auto-link. To prevent auto-linking, wrap
    the URL in backticks. Reference-style links (`[text][label]` +
    `[label]: url "title"`) MAY be used for readability. Spaces in URLs
    SHOULD be URL-encoded as `%20`; for URLs containing parentheses, use
    reference-style links or HTML `<a>` tags.

-   **All images MUST have alternative text.**

    Syntax: `![alt](path "title")`. Link an image by wrapping it:
    `[![alt](path)](url)`. Markdown has no standard image sizing; use
    an HTML `<img>` tag with explicit `width`/`height` where required.

-   **Blockquotes use `>` plus a single space, surrounded by blank lines.**

    Multi-paragraph blockquotes need `>` on the blank line between paragraphs.
    Nesting and other block elements are supported by prefixing lines with `>`.
    Use blockquotes for short quotations only; for notes/warnings/tips in
    technical docs, prefer AsciiDoc admonitions
    ([TS-28: AsciiDoc](../028/AGENTS.md)).

-   **Tables are a GFM extension — use sparingly.**

    Header row separated by hyphens, cells separated by pipes; a pipe
    SHOULD start and end each row. Column alignment via colons in the
    separator row (`:---`, `:---:`, `---:`). No cell spanning; block-level
    elements cannot be placed inside cells. For complex tables, use
    AsciiDoc ([TS-28: AsciiDoc](../028/AGENTS.md)). A literal pipe in a
    cell uses `&#124;`.

-   **Horizontal rules use `---`, preceded by a blank line.**

    `***`, `---`, or `___` on a line by themselves. A blank line MUST
    precede a rule or `---` after text may be parsed as a setext heading.
    Use sparingly; prefer headings.

-   **Escape characters only where necessary.**

    Prefix with `\` to render a literal formatting character. Escapable
    characters: `` \ ` * _ { } [ ] < > ( ) # + - . ! | ``. Prefer restructuring
    (eg. adding blank lines) over excessive escaping.

-   **Use inline HTML sparingly.**

    Block-level HTML elements (`<div>`, `<table>`, `<pre>`, etc.) MUST be
    separated from surrounding Markdown by blank lines and SHOULD NOT be
    indented. Markdown syntax is NOT processed inside block-level HTML tags.
    For content requiring rich HTML, prefer AsciiDoc or direct HTML.

-   **Avoid footnotes in portable documents.**

    Footnotes (`[^label]` + `[^label]: text`) are a GFM/extension feature,
    not pure CommonMark. Prefer inline links for citations when the document
    must render across a wide range of processors.

-   **Keep source lines under a soft limit of 120 characters.**

    Long lines MAY be soft-wrapped; CommonMark joins wrapped lines within a
    paragraph. Hard line breaks should be semantic only.

-   **Lint, format, and link-check Markdown.**

    [markdownlint](https://github.com/DavidAnson/markdownlint) is RECOMMENDED.
    [Prettier](https://prettier.io/) MAY be used for formatting; reconcile
    lint and format config so they don't conflict. Run a link checker in CI.
    Editor config SHOULD highlight trailing whitespace, end files with a
    single newline, and use spaces (not tabs) for indentation.

## References

- [TS-27 source](README.adoc)
- [TS-26: Technical Writing Style Guide](../026/AGENTS.md)
- [TS-28: AsciiDoc](../028/AGENTS.md)
- [CommonMark Specification](https://spec.commonmark.org/)
- [GitHub Flavored Markdown Specification](https://github.github.com/gfm/)
