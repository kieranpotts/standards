# TS-26: Technical Writing Style Guide

This is a compact version of technical standard TS-26 for AI agents.

Use this when writing or editing the prose of a technical document: voice,
headings, terminology, emphasis, lists, links, numbers/dates/units, admonitions,
code blocks, or citations.

## Rules

- **Use active voice and present tense for current behavior.**

  "The server rejects invalid requests," not "invalid requests are rejected."
  Present tense for current behavior, future tense only for consequences of a
  reader's action, past tense for historical records (changelogs). Address the
  reader as "you" in instructions; avoid "we" for the software's own behavior.

- **Sentence case for headings; don't skip heading levels.**

  "Referencing style guides," not "Referencing Style Guides." Headings describe
  the content, not tease it.

- **One term per concept, used consistently.**

  Don't vary vocabulary for style ("endpoint"/"route"/"handler" for the same
  thing). Prefer plain words ("use" over "utilize"). Maintain a glossary for
  domain-specific terms, linked on first use.

- **Spell out abbreviations and acronyms on first use.**

  "Content delivery network (CDN)," then "CDN" thereafter — except acronyms so
  common to the audience that spelling them out is noise (HTTP, URL, JSON).

- **Prefer neutral, plain, non-idiomatic language.**

  Use neutral terms over ones with violent/ableist connotations where a clear
  alternative exists (allowlist/denylist, primary/replica). Avoid idioms and
  culturally specific references that don't translate for an international
  audience.

- **Match emphasis style to what the text represents.**

  Monospace for anything typed or output literally (paths, commands, flags,
  code). Bold for UI elements to interact with. Italics only to introduce a new
  term or for genuine emphasis. Don't stack multiple forms of emphasis.

- **Use admonitions sparingly, for skippable-but-important asides.**

  Admonitions in AsciiDoc are NOTE/TIP/IMPORTANT/WARNING/CAUTION. Not a
  substitute for well-organized prose. Overuse trains readers to skip them.

- **Keep list items parallel; numbered for sequence, bulleted otherwise.**

  Don't mix sentence fragments with full sentences in one list. Avoid nesting
  more than two levels deep.

- **Link text describes the destination.**

  Never "click here" or a bare URL.

- **Numerals 10+, spelled out below 10 in prose; always numerals with units.**

- **Always combine numerals with units.**

- **Dates in ISO 8601 (`2026-07-02`), never locale-ambiguous `MM/DD/YYYY`.**

- **CLI commands MUST NOT be prefixed with `$`**

  Except when documenting output, where `$` disambiguates command from output.
  Use `<angle brackets>` for placeholders, `[square brackets]` for optional
  arguments.

- **Citations use a Chicago/Harvard hybrid:**

  `<author> (<year>). _<title>_. <publication>`

  Truncate 4+ authors to "Smith et al." Prefer citing the organization/publisher
  over a byline author for press releases and news stories.

- **Remove AI writing tells.**

  These patterns are not ungrammatical, but they read as generic, evasive, or
  hollow, and erode trust once a reader spots them.

  - Inflated significance: "stands as a testament to," "marks a pivotal
    moment," "underscores the importance of." State what happened; let the
    reader judge significance.

  - Vague attribution: "industry reports suggest," "experts argue." Name the
    source, or state the claim directly.

  - Formulaic "challenges" framing: reflexive "Despite these challenges...",
    generic "Future outlook" / "Challenges and legacy" closers. State specific
    problems and plans, or omit the section.

  - Hollow "-ing" clauses: trailing participles that restate the point vaguer
    than it already was — "..., ensuring reliability," "..., highlighting its
    flexibility." Cut unless it adds a new concrete fact.

  - Promotional language: "boasts," "vibrant," "cutting-edge," "seamless,"
    "in the heart of," "nestled." Also unearned superlatives/buzzwords —
    "revolutionary," "powerful," "intuitive," "state-of-the-art." Documentation
    states facts; it doesn't sell. Replace with the specific fact that makes
    the claim true, or delete it.
  - Vague benefits: "enhanced productivity," "improved workflow," "optimized
    performance." Ask what the underlying fact is — faster at what, by how
    much, which steps were removed — and state that instead.
  - Information priority: lead with the fact the reader needs (what changed,
    what's now possible, how it works) before background or rationale.

  - Overused AI vocabulary: "delve," "crucial," "leverage," "foster,"
    "landscape" (abstract), "tapestry," "testament," "underscore" (verb),
    "intricate." Not forbidden individually, but rewrite plainer if several
    cluster together.

  - Copula avoidance: "serves as," "stands as," "represents a," "boasts a"
    instead of a plain "is/are/has." Say what a thing is directly.

  - Negative parallelism and rule-of-three padding: "not only... but...,"
    "it's not just X, it's Y," and padding to three list items when two would
    say it (or four are true).

  - False ranges: "from X to Y" used only to suggest breadth, where X and Y
    aren't points on a real scale.

  - Chatbot artifacts and sycophancy: "Great question!," "I hope this helps,"
    "Let me know if you'd like me to expand," "You're absolutely right that."
    Never belongs in a published document.

  - Knowledge-cutoff hedges: "as of my last update," "details are limited,"
    "based on available information." State what's actually known and its
    source, or state plainly it isn't known yet.

  - Filler and stacked hedging: "in order to" → "to," "due to the fact that"
    → "because," "it is important to note that" → delete, "has the ability
    to" → "can." Avoid "could potentially possibly" — state the claim once,
    at the confidence it deserves.

  - Generic positive conclusions: "the future looks bright," "exciting times
    lie ahead." End on the last concrete fact or actual next step instead.

  - Uniform rhythm: every sentence/paragraph the same length and shape reads
    as mechanical even when each one is individually correct — see
    "sentences and paragraphs" above for varying length deliberately.

  - Stacked em dashes and bold: overusing em dashes for asides, or bolding
    many phrases in running prose — see the emphasis and punctuation rules
    above for when each is warranted.
