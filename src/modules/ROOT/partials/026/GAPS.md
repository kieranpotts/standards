# TS-26 gap analysis

Gaps found comparing TS-26: Technical Writing Style Guide against the following
reference resources in `__TODO__/026/`:

- `__TODO__/O'Reilly Style Guide.url` → http://oreillymedia.github.io/production-resources/styleguide/ (O'Reilly Style Guide and Word List)
- `__TODO__/copywriting.adoc`, `__TODO__/principles.adoc`
- `__TODO__/_todo/0100-forward.md` … `1100-foreign.md` (draft web-copywriting style guide)
- `__TODO__/_todo/blogs.md`, `reference-resources.md`, `writing.md`, `styleguides.md`, `accessibility.md`, `seo.md`
- `__TODO__/_todo/OLD-NOTES.md`, `OLD-NOTES-2.md`, `OLD-LOOKUP.md`, `9999-reference.md` (research dumps, largely British news/journalism style — Economist/Guardian)

**Assessment.** Most of the reference material sits outside TS-26's stated
purpose. The three large `OLD-*` and `9999-reference.md` files are British
news/journalism style guides (Economist, Guardian, LSE) whose bulk is
honorifics, place/country names, political titles, sports terms, currency,
and an A-Z spelling word list — all out of scope for a technical-documentation
style guide. The draft `0100`–`1100` files and `copywriting.adoc` are web
copywriting/marketing material (SEO headlines, sales copy, blog strategy), also
out of scope. The O'Reilly guide is the closest match (technical books) and
supplies the majority of the genuinely missing items, concentrated in
punctuation, capitalization, and figure/list mechanics the standard doesn't
address. Net: a cluster of real missing/partial gaps around punctuation marks
the standard omits, plus scattered partials; otherwise mostly out-of-scope
reference breadth.

**Status:** First run. All gaps open. 2026-08-05.

## Missing

- [ ] O'Reilly Style Guide#Punctuation and `9999-reference.md:880-882` /
      `9999-reference.md:890-901` / `OLD-NOTES-2.md:117-131` — comma usage
      (serial/Oxford comma, comma splices, introductory phrases). TS-26
      `13-punctuation.adoc` covers only colons and semicolons; commas are not
      addressed. Recommend expanding `13-punctuation.adoc`.

- [ ] O'Reilly Style Guide#Punctuation and `9999-reference.md:3788-3795` /
      `OLD-NOTES-2.md:240-247` — quotation marks (curly vs straight, double vs
      single, placement of periods/commas relative to closing quotes). Not
      addressed anywhere in the standard. Recommend `13-punctuation.adoc` or a
      new subsection.

- [ ] `9999-reference.md:175-192` / `OLD-NOTES-2.md:201-217` /
      `OLD-NOTES.md:2407-2431` — apostrophes (singular/plural possessives,
      decades written without apostrophes, plurals of abbreviations). Not
      addressed. Recommend `13-punctuation.adoc`.

- [ ] O'Reilly Style Guide#Punctuation (em/en dash) and
      `9999-reference.md:2343-2367` / `OLD-NOTES-2.md:132-138` — em dashes
      (closed, no spaces) and en dashes for numeric ranges/negative numbers.
      TS-26 mentions em dashes only in the AI-tells context
      (`15-ai-writing-tells.adoc:148-151`); it gives no dash mechanics rule.
      Recommend `13-punctuation.adoc`.

- [ ] `9999-reference.md:2343-2367` / `0500-punctuation.md` /
      `OLD-NOTES-2.md:154-173` / O'Reilly Style Guide#Miscellaneous —
      hyphenation (compound adjectives before nouns, no hyphen after `-ly`
      adverbs, no hyphen in units of measure like "32 MB"). Not addressed
      anywhere in the standard. Recommend a new "Hyphenation" subsection of
      `13-punctuation.adoc`.

- [ ] `9999-reference.md:1473-1474` / O'Reilly Style Guide#Punctuation —
      exclamation marks and question marks (e.g. "do not use exclamation
      marks" as a default). Not addressed. Recommend `13-punctuation.adoc`.

- [ ] O'Reilly Style Guide#Dates and Numbers and `9999-reference.md:4528-4531`
      — time-of-day formatting (e.g. `1am`, `6.30pm`, when to spell out). TS-26
      `10-numbers-dates-units.adoc` covers dates and numbers but not times.
      Recommend `10-numbers-dates-units.adoc`.

- [ ] `1100-foreign.md` / `OLD-NOTES.md:2071-2133` /
      `9999-reference.md:1956-1962` — foreign words and accents (when to
      italicize, when to keep accents, anglicised forms). Not addressed.
      Recommend a new subsection of `06-emphasis.adoc` or `13-punctuation.adoc`.

- [ ] O'Reilly Style Guide#Typography and Font Conventions /
      `9999-reference.md:3062-3066` / `OLD-NOTES.md:2137-2155` — italics for
      titles of works (books, periodicals, films) vs quotation marks. TS-26
      `06-emphasis.adoc` covers italics for new terms and emphasis only.
      Recommend `06-emphasis.adoc`.

- [ ] O'Reilly Style Guide#CrossReferences and #Considering Electronic
      Formats — avoid "above"/"below" for figures/tables/examples; prefer
      "preceding"/"following" or live cross-references because layout shifts
      in reflowable formats. Not addressed. Recommend a new subsection of
      `12-referencing.adoc` or `02-headings.adoc`.

- [ ] O'Reilly Style Guide#Figures, Tables, and Examples — every numbered
      figure/table/example needs a specific in-text reference, sentence-cased
      captions, no period after captions. Not addressed. Recommend a new
      section.

- [ ] O'Reilly Style Guide#Bibliographical Entries and Citations — footnote
      mechanics (numbered per chapter, marker placed after punctuation,
      footnote must contain more than a bare URL). TS-26 `12-referencing.adoc`
      covers citation *format* but not footnote placement/mechanics.
      Recommend `12-referencing.adoc`.

- [ ] `9999-reference.md:4457-4472` / `OLD-NOTES.md:645-651` — "that"
      (restrictive) vs "which" (non-restrictive). Not addressed. Recommend
      `14-sentences-and-paragraphs.adoc`.

- [ ] `9999-reference.md:849-860` / `OLD-NOTES-2.md:1120-1131` /
      `OLD-NOTES.md:2587-2611` — collective-noun agreement (e.g. "data"
      plural/singular, companies singular, teams plural). Not addressed.
      Recommend `14-sentences-and-paragraphs.adoc`.

- [ ] O'Reilly Style Guide#Punctuation ("Lowercase the first letter after a
      colon") and `9999-reference.md` colon entries — capitalization of the
      first word after a colon. TS-26 `13-punctuation.adoc` gives colon rules
      but not the follow-on capitalization convention. Recommend
      `13-punctuation.adoc`.

- [ ] `0800-conciseness.md` ("Contractions") / `9999-reference.md:2506-2508`
      — contractions: use them but do not overdo. Not addressed. Recommend
      `14-sentences-and-paragraphs.adoc` or `01-voice-and-tense.adoc`.

- [ ] `9999-reference.md:1373-1375` / `2377-2378` — formatting of "eg"/"ie"
      (no full points, no following comma). TS-26 `04-abbreviations.adoc`
      does not address these abbreviations' punctuation. Recommend
      `04-abbreviations.adoc`.

- [ ] O'Reilly Style Guide#Code (Line Length, Syntax Highlighting,
      Formatting Code in Word) — code-block line-length limits, syntax
      highlighting, and "indent with spaces not tabs". TS-26
      `11-code-blocks.adoc` covers placeholders and CLI prompts only.
      Recommend `11-code-blocks.adoc`.

- [ ] `copywriting.adoc` ("Copywriting guidelines") — UI/short-message
      conventions: titles and short messages should not end with a full stop;
      short messages may use hyphens for readability. Not addressed (relevant
      to microcopy/UI text in documentation). Recommend a new subsection of
      `13-punctuation.adoc` or `06-emphasis.adoc`.

## Partial

- [ ] O'Reilly Style Guide#Headings — headings should contain no inline code
      font, bold, or italic, and acronyms in headings should be expanded
      unless common. TS-26 `02-headings.adoc` covers sentence case and level
      skipping but omits these. Recommend `02-headings.adoc`.

- [ ] O'Reilly Style Guide#Abbreviations & Acronyms /
      `9999-reference.md:620-656` / `OLD-NOTES.md:661-699` — abbreviation
      mechanics beyond first-use spelling-out: plural forms (CDs), "a" vs
      "an" by pronunciation, omitting periods, no "the" before pronounceable
      acronyms. TS-26 `04-abbreviations.adoc` covers only spelling-out.
      Recommend `04-abbreviations.adoc`.

- [ ] `9999-reference.md:1214-1222` / `9999-reference.md:2040-2057` /
      `OLD-NOTES.md:4243` (gender-neutral phrasing) — person-first disability
      language ("disabled people" not "the disabled"; "uses a wheelchair") and
      gender-neutral pronouns / "mankind" → "humankind". TS-26
      `05-inclusive-language.adoc` covers violent/ableist connotations and
      idioms but not pronoun strategy or person-first phrasing. Recommend
      `05-inclusive-language.adoc`.

- [ ] O'Reilly Style Guide#Dates and Numbers /
      `9999-reference.md:1600-1603` / `9999-reference.md:3339` /
      `OLD-NOTES.md:1423-1427` — ordinals (first–ninth spelled, 10th+ figures),
      hyphenated fractions, "percentage points" vs percent, and ranges.
      TS-26 `10-numbers-dates-units.adoc` covers the 0–9/10+ split, units, and
      ISO dates only. Recommend `10-numbers-dates-units.adoc`.

- [ ] O'Reilly Style Guide#Lists — list items take no periods unless one item
      is a complete sentence (then all do); "variable lists" for term/
      definition pairs; nested bullets use em dashes. TS-26 `08-lists.adoc`
      covers parallelism and nesting depth but not the period rule or
      variable lists. Recommend `08-lists.adoc`.

- [ ] O'Reilly Style Guide#Typography and Font Conventions — finer emphasis
      conventions: placeholders in constant-width italic, user-typed text in
      constant-width bold, URLs/filenames in italic (O'Reilly) vs the
      standard's monospace. TS-26 `06-emphasis.adoc` gives the high-level
      monospace/bold/italic split but not these refinements. Recommend
      `06-emphasis.adoc`.

- [ ] `OLD-NOTES.md:4243` / `9999-reference.md` (usage entries) /
      `0700-redundancy.md` — commonly confused words (fewer/less, comprise,
      affect/effect, flaunt/flout, disinterested/uninterested). TS-26
      `03-terminology.adoc` covers "one term per concept" and plain words but
      gives no commonly-confused-words guidance. Recommend
      `03-terminology.adoc` (or out-of-scope as a word list — see below).

- [ ] `0600-voice.md` / `OLD-NOTES.md:4243` — a detection heuristic for
      passive voice (be-verb forms: am/is/was/were/been; subject receives the
      action). TS-26 `01-voice-and-tense.adoc` states the preference but gives
      no way to recognize passive constructions. Recommend
      `01-voice-and-tense.adoc`.

- [ ] `0700-redundancy.md` / `0800-conciseness.md` — general redundancy and
      overused-word lists ("very", "actually", "basically", "completely") as
      plain good-writing rules. TS-26 `15-ai-writing-tells.adoc` covers much of
      this but frames it as LLM tells rather than general editing. Recommend
      cross-linking or a general note in `14-sentences-and-paragraphs.adoc`.

- [ ] `0100-forward.md` / `0300-general-style.md` (Orwell's six rules) /
      `0900-structure-pacing.md` — sentence fragments are acceptable for
      emphasis. TS-26 `14-sentences-and-paragraphs.adoc` covers sentence length
      and pace but not fragment use. Recommend `14-sentences-and-paragraphs.adoc`.

## Out-of-scope

- [ ] `OLD-NOTES.md`, `OLD-NOTES-2.md`, `9999-reference.md`, `OLD-LOOKUP.md`
      — honorifics and titles for people (Mr/Mrs/Miss/Ms/Dr, "Prime Minister
      Blair", "the Rev", knights/dames), capitalization of political offices,
      parties, acts, government departments, the Crown, etc. Flagged: this is
      news/journalism style; a technical-writing standard has no need for it.

- [ ] `OLD-NOTES.md:3385-3567`, `9999-reference.md:3405-3555`,
      `OLD-NOTES-2.md:1469-1533` — place-name and country-name conventions
      (Mumbai not Bombay, "the Netherlands", Ukraine, Côte d'Ivoire,
      transliteration of foreign personal names). Flagged: reference style for
      journalism, not technical documentation.

- [ ] `9999-reference.md`, `OLD-NOTES.md` (sports, currencies, weights/
      measures, placenames, dog breeds, wine names, fashion weeks, grand
      prix) — specialized reference word lists. Flagged: domain-specific
      journalism reference, far outside a technical-doc style guide.

- [ ] `0100-forward.md`, `0200-strategy.md`, `blogs.md`, `seo.md`,
      `reference-resources.md` — content strategy, SEO, corporate blogging,
      keyword density, page-`<title>` tag optimization, sales-copy "sizzle"
      words, calls to action. Flagged: marketing/web-strategy, not prose
      style.

- [ ] `OLD-NOTES.md:4243` / `OLD-NOTES-2.md:3-28` — web-scannability tactics
      (highlight three times as many words as print, `<strong>` over `<em>`
      for keywords, blue reserved for links, keyword density 5–8%). Flagged:
      web-design/SEO heuristics; TS-26 is format-agnostic prose style.

- [ ] O'Reilly Style Guide#Code (Line Length table by book series),
      #Considering Electronic Formats (InDesign/Atlas/DocBook/Word workflows,
      oreil.ly short links, "do not link to Amazon/Apple/Google"),
      #O'Reilly Cover Copy, #O'Reilly Word List — book-production and
      publisher-specific workflow. Flagged: tooling/publisher convention, not
      a general style rule.

- [ ] `9999-reference.md`, `OLD-NOTES.md` (long A-Z spelling and word-choice
      lists: "acknowledgment not acknowledgement", "aeroplane not airplane",
      "-ise vs -ize", British vs American spelling) — a dictionary/word-list,
      not reusable style rules. Flagged: lexicography, outside the standard's
      purpose.

- [ ] `OLD-NOTES.md:4243` / `OLD-NOTES-2.md:2001-2011` — general English
      grammar (split infinitives, dangling participles, subjunctive mood,
      gerunds take possessive adjectives, "an" before vowel sounds). Flagged:
      a general-grammar reference; TS-26 deliberately scopes itself to
      prose-level/presentational conventions, not grammar instruction.

- [ ] `OLD-NOTES.md:3347-3361` / `9999-reference.md:805-808` — Latin/biological
      nomenclature, classical-music work referencing, biblical citation
      format. Flagged: specialized referencing domains not relevant to
      technical documentation.

- [ ] `accessibility.md`, `styleguides.md`, `writing.md`,
      `reference-resources.md` — these files are lists of external URLs with
      at most a one-line gloss each; their linked content was not fetched
      (see Unresolved). Flagged: pointers, not reference content in
      themselves.

## Unresolved

- [ ] `__TODO__/_todo/Web Copy That Sells - Second Edition.pdf` — binary PDF,
      not read (no text-extraction tool available to the agent). Not included
      in the comparison.

- [ ] `__TODO__/_todo/accessibility.md`, `seo.md`, `styleguides.md`,
      `writing.md`, `reference-resources.md` contain ~40 external URLs (e.g.
      alistapart.com, nngroup.com, copyblogger.com, monzo.com/tone-of-voice).
      These are link collections; the linked pages were not individually
      fetched. Only the local file content was used.