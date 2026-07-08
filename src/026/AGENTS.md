# TS-26: Technical Writing Style Guide

This is a compact version of technical standard TS-26 for AI agents.

Use this when writing or editing the prose of a technical document: voice,
headings, terminology, emphasis, lists, links, numbers/dates/units, admonitions,
code blocks, or citations.

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

-   **Use active voice and present tense for current behavior.**

    "The server rejects invalid requests," not "invalid requests are rejected."
    Present tense for current behavior, future tense only for consequences of a
    reader's action, past tense for historical records (changelogs). Address
    the reader as "you" in instructions; avoid "we" for the software's own
    behavior.

-   **Sentence case for headings; don't skip heading levels.**

    "Referencing style guides," not "Referencing Style Guides." Headings
    describe the content, not tease it.

-   **One term per concept, used consistently.**

    Don't vary vocabulary for style ("endpoint"/"route"/"handler" for the same
    thing). Prefer plain words ("use" over "utilize"). Maintain a glossary for
    domain-specific terms, linked on first use.

-   **Spell out abbreviations and acronyms on first use.**

    "Content delivery network (CDN)," then "CDN" thereafter — except acronyms
    so common to the audience that spelling them out is noise (HTTP, URL, JSON).

-   **Prefer neutral, plain, non-idiomatic language.**

    Use neutral terms over ones with violent/ableist connotations where a clear
    alternative exists (allowlist/denylist, primary/replica). Avoid idioms and
    culturally specific references that don't translate for an international
    audience.

-   **Match emphasis style to what the text represents.**

    Monospace for anything typed or output literally (paths, commands, flags,
    code). Bold for UI elements to interact with. Italics only to introduce a
    new term or for genuine emphasis. Don't stack multiple forms of emphasis.

-   **Use admonitions sparingly, for skippable-but-important asides.**

    Admonitions in AsciiDoc are NOTE/TIP/IMPORTANT/WARNING/CAUTION. Not a
    substitute for well-organized prose. Overuse trains readers to skip them.

-   **Keep list items parallel; numbered for sequence, bulleted otherwise.**

    Don't mix sentence fragments with full sentences in one list. Avoid
    nesting more than two levels deep.

-   **Link text describes the destination.**

    Never "click here" or a bare URL.

-   **Numerals 10+, spelled out below 10 in prose; always numerals with units.**

-   **Always combine numerals with units.**

-   **Dates in ISO 8601 (`2026-07-02`), never locale-ambiguous `MM/DD/YYYY`.**

-   **CLI commands MUST NOT be prefixed with `$`**

    Except when documenting output, where `$` disambiguates command from output.
    Use `<angle brackets>` for placeholders, `[square brackets]` for optional
    arguments.

-   **Citations use a Chicago/Harvard hybrid:**

    `<author> (<year>). _<title>_. <publication>`

    Truncate 4+ authors to "Smith et al." Prefer citing the
    organization/publisher over a byline author for press releases and
    news stories.
