# TS-26 gap analysis

Gaps found comparing TS-26: Technical writing style guide against the following
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
and an A-Z spelling word list. Four of these categories were originally
flagged out-of-scope, then reversed on 2026-08-14 at the user's explicit
direction and imported in full as a new glossary partial — see the Status
line and the individual resolution notes under Out-of-scope below. The
draft `0100`–`1100` files and `copywriting.adoc` are web copywriting/
marketing material (SEO headlines, sales copy, blog strategy) and remain
out of scope, along with general-grammar reference and specialized
referencing domains (Latin nomenclature, biblical citation). The O'Reilly
guide is the closest match to TS-26's stated technical-book purpose and fed
the majority of the originally-missing items, concentrated in punctuation,
capitalization, and figure/list mechanics.

**Status:** All 32 actionable items resolved (the 29 original plus the one
routed in from TS-21 on 2026-08-15, plus one found while resolving the
Unresolved link-collection triage on 2026-08-15 and closed the same batch
on 2026-08-15), plus 4 of the original 9 out-of-scope items (2026-08-14),
across five `close-gaps` batches — the first closed the comma/quotation-
mark/apostrophe/dash/hyphenation/exclamation-question-mark/colon-
capitalization cluster in `13-punctuation.adoc` plus abbreviation
mechanics, dates/numbers, code-block formatting, emphasis/typography, and
referencing mechanics; the second closed that/which, collective nouns,
overused words, sentence fragments, and contractions/passive-voice
detection in `14-sentences-and-paragraphs.adoc` and
`01-voice-and-tense.adoc`, and heading formatting plus nested/variable
lists in `02-headings.adoc` and `08-lists.adoc`; the third closed the two
remaining Partial items (commonly-confused words, person-first/gender-
neutral language) and, at the user's explicit direction, reversed and
closed four Out-of-scope items (honorifics/titles, place/country names,
sports/currencies/measures, and the A-Z spelling list itself) by importing
the full ~1,373-entry A-Z word list as a new `16-glossary.adoc` partial —
see that item's resolution note for what the import contains and the two
corrections made to the source along the way. One further Out-of-scope
item (`copywriting.adoc`'s UI/short-message conventions) was confirmed
out-of-scope for TS-26 and routed to TS-15 (User interfaces) instead, at
the user's direction. Both previously-Unresolved resources (the PDF and
the link collections) were resolved on 2026-08-15 — see below — surfacing
one new Missing item (procedural/instructional phrasing), closed the same
day by a fifth `close-gaps` batch: a new "Instructional steps" section in
`14-sentences-and-paragraphs.adoc`, requiring chronological sequencing
over spatial reference and device-agnostic action verbs. This file has 0
actionable items remaining. 5 out-of-scope items remain unticked, awaiting
the user's confirm/overrule decision — this file is not yet fully resolved
on the "zero unchecked items of any kind" standard.

**2026-08-14 addendum.** One new Missing item was added, routed here from
TS-21 (HTTP APIs) at the user's direction while confirming TS-21's own
out-of-scope items: `api-style-guide.md`'s document-level conventions
(RFC 2119 rendering, all-caps REST/JSON, fixed-width machine-readable text,
URI Template syntax). Closed 2026-08-15 — see below.

**2026-08-15 addendum.** The two remaining Unresolved items were resolved:
the PDF (`Web Copy That Sells - Second Edition.pdf`) was extracted with
`pdftotext` and confirmed out-of-scope (direct-response sales copywriting,
the same register as the already-out-of-scope `copywriting.adoc`), and the
five link-collection files were read in full and their ~77 URLs triaged,
with 8 of the most promising fetched. One genuine new Missing item was
found — procedural/instructional phrasing (chronological sequencing,
device-agnostic action verbs) — and is recorded below, not yet actioned.

## Missing

- [x] O'Reilly Style Guide#Punctuation and `9999-reference.md:880-882` /
      `9999-reference.md:890-901` / `OLD-NOTES-2.md:117-131` — comma usage
      (serial/Oxford comma, comma splices, introductory phrases). TS-26
      `13-punctuation.adoc` covers only colons and semicolons; commas are not
      addressed. Recommend expanding `13-punctuation.adoc`.

      **Resolved.** Closed by a new "Commas" section in `13-punctuation.adoc`.
      Requires the serial (Oxford) comma, requires a comma after an
      introductory phrase or clause longer than three words, and prohibits
      comma splices, with a bad/good example pair. Source added to the
      page's `== References`.

- [x] O'Reilly Style Guide#Punctuation and `9999-reference.md:3788-3795` /
      `OLD-NOTES-2.md:240-247` — quotation marks (curly vs straight, double vs
      single, placement of periods/commas relative to closing quotes). Not
      addressed anywhere in the standard. Recommend `13-punctuation.adoc` or a
      new subsection.

      **Resolved.** Closed by a new "Quotation marks" section in
      `13-punctuation.adoc`. Requires plain straight double quotes (cross-
      referencing the existing style-guide rule), reserves single quotes for
      nesting, and states the American convention of periods/commas inside
      the closing quote versus other punctuation outside it.

- [x] `9999-reference.md:175-192` / `OLD-NOTES-2.md:201-217` /
      `OLD-NOTES.md:2407-2431` — apostrophes (singular/plural possessives,
      decades written without apostrophes, plurals of abbreviations). Not
      addressed. Recommend `13-punctuation.adoc`.

      **Resolved.** Closed by a new "Apostrophes" section in
      `13-punctuation.adoc`. Covers singular possessive (including names
      ending in "s") and plural possessive formation, and requires decades
      and plural abbreviations to be written without an apostrophe.

- [x] O'Reilly Style Guide#Punctuation (em/en dash) and
      `9999-reference.md:2343-2367` / `OLD-NOTES-2.md:132-138` — em dashes
      (closed, no spaces) and en dashes for numeric ranges/negative numbers.
      TS-26 mentions em dashes only in the AI-tells context
      (`15-ai-writing-tells.adoc:148-151`); it gives no dash mechanics rule.
      Recommend `13-punctuation.adoc`.

      **Resolved.** Closed by a new "Dashes" section in `13-punctuation.adoc`.
      Requires the em dash closed up with no surrounding spaces, cross-
      references the existing "Stacked em dashes and bold" AI-tells guidance
      so the overuse warning and the mechanics sit side by side, and requires
      the en dash (not a hyphen) for numeric ranges and negative numbers.

- [x] `9999-reference.md:2343-2367` / `0500-punctuation.md` /
      `OLD-NOTES-2.md:154-173` / O'Reilly Style Guide#Miscellaneous —
      hyphenation (compound adjectives before nouns, no hyphen after `-ly`
      adverbs, no hyphen in units of measure like "32 MB"). Not addressed
      anywhere in the standard. Recommend a new "Hyphenation" subsection of
      `13-punctuation.adoc`.

      **Resolved.** Closed by a new "Hyphenation" section in
      `13-punctuation.adoc`. Requires hyphenating a compound modifier before
      the noun it modifies where omitting it would misparse, prohibits
      hyphenating the same compound after the noun, prohibits a hyphen after
      an `-ly` adverb, and prohibits hyphenating a numeral-unit pair such as
      "32 MB" even when used as a modifier.

- [x] `9999-reference.md:1473-1474` / O'Reilly Style Guide#Punctuation —
      exclamation marks and question marks (e.g. "do not use exclamation
      marks" as a default). Not addressed. Recommend `13-punctuation.adoc`.

      **Resolved.** Closed by a new "Exclamation and question marks" section
      in `13-punctuation.adoc`. Prohibits exclamation marks outright,
      cross-referencing the existing "Promotional language" AI-tells section
      as the same underlying failure mode, and restricts question marks to
      genuine questions directed at the reader, prohibiting the rhetorical-
      question device.

- [x] O'Reilly Style Guide#Dates and Numbers and `9999-reference.md:4528-4531`
      — time-of-day formatting (e.g. `1am`, `6.30pm`, when to spell out). TS-26
      `10-numbers-dates-units.adoc` covers dates and numbers but not times.
      Recommend `10-numbers-dates-units.adoc`.

      **Resolved.** Closed by a new paragraph in `10-numbers-dates-units.adoc`.
      Requires 24-hour format for the same locale-unambiguity reason as ISO
      dates, with a 12-hour fallback format specified for non-technical
      audiences.

- [x] `1100-foreign.md` / `OLD-NOTES.md:2071-2133` /
      `9999-reference.md:1956-1962` — foreign words and accents (when to
      italicize, when to keep accents, anglicised forms). Not addressed.
      Recommend a new subsection of `06-emphasis.adoc` or `13-punctuation.adoc`.

      **Resolved.** Closed by a new "Foreign words" section in
      `06-emphasis.adoc`. Requires italicizing an unabsorbed foreign word or
      phrase with its native accents preserved, exempts loanwords that have
      become standard English vocabulary, and defers ambiguous cases to an
      authoritative English dictionary.

- [x] O'Reilly Style Guide#Typography and Font Conventions /
      `9999-reference.md:3062-3066` / `OLD-NOTES.md:2137-2155` — italics for
      titles of works (books, periodicals, films) vs quotation marks. TS-26
      `06-emphasis.adoc` covers italics for new terms and emphasis only.
      Recommend `06-emphasis.adoc`.

      **Resolved.** Closed by a new "Titles of works" section in
      `06-emphasis.adoc`. Requires italics for a standalone work and
      quotation marks for a work that is part of a larger publication,
      cross-referencing the parallel rule for citation titles in
      `12-referencing.adoc`.

- [x] O'Reilly Style Guide#CrossReferences and #Considering Electronic
      Formats — avoid "above"/"below" for figures/tables/examples; prefer
      "preceding"/"following" or live cross-references because layout shifts
      in reflowable formats. Not addressed. Recommend a new subsection of
      `12-referencing.adoc` or `02-headings.adoc`.

      **Resolved.** Closed by a new "Referring to figures, tables, and
      examples" section in `12-referencing.adoc`. Prohibits "above"/"below"
      positional references, requires numbered or cross-referenced pointers
      instead, and restricts "preceding"/"following" to cases with no live
      cross-reference available.

- [x] O'Reilly Style Guide#Figures, Tables, and Examples — every numbered
      figure/table/example needs a specific in-text reference, sentence-cased
      captions, no period after captions. Not addressed. Recommend a new
      section.

      **Resolved.** Closed by the same new "Referring to figures, tables, and
      examples" section in `12-referencing.adoc` as the above/below item.
      Requires a sentence-case caption with no trailing period and a specific
      in-text reference to every numbered figure, table, and example.

- [x] O'Reilly Style Guide#Bibliographical Entries and Citations — footnote
      mechanics (numbered per chapter, marker placed after punctuation,
      footnote must contain more than a bare URL). TS-26 `12-referencing.adoc`
      covers citation *format* but not footnote placement/mechanics.
      Recommend `12-referencing.adoc`.

      **Resolved.** Closed by a new "Footnote and endnote mechanics" section
      in `12-referencing.adoc`. Requires per-document (not per-chapter)
      numbering — adapted from the source's per-chapter convention, since a
      merged single-page standard has no chapter boundary — marker placement
      after adjacent punctuation, and a footnote that is more than a bare
      URL.

- [x] `9999-reference.md:4457-4472` / `OLD-NOTES.md:645-651` — "that"
      (restrictive) vs "which" (non-restrictive). Not addressed. Recommend
      `14-sentences-and-paragraphs.adoc`.

      **Resolved.** Closed by a new "'That' and 'which'" section in
      `14-sentences-and-paragraphs.adoc`. Requires "that" for a restrictive
      clause the sentence's meaning depends on, and comma-set-off "which" for
      a non-restrictive clause the sentence would still make sense without.

- [x] `9999-reference.md:849-860` / `OLD-NOTES-2.md:1120-1131` /
      `OLD-NOTES.md:2587-2611` — collective-noun agreement (e.g. "data"
      plural/singular, companies singular, teams plural). Not addressed.
      Recommend `14-sentences-and-paragraphs.adoc`.

      **Resolved.** Closed by a new "Collective nouns" section in
      `14-sentences-and-paragraphs.adoc`. Requires singular agreement when a
      collective noun refers to the group as a unit and plural only when the
      sentence is explicitly about individual members, and fixes "data" as
      singular in this standard's technical-writing context. The source's
      journalism-specific rulings on company and country names (Tesco,
      "the Netherlands," sports-team names) were left out as out of scope for
      a technical-documentation standard.

- [x] O'Reilly Style Guide#Punctuation ("Lowercase the first letter after a
      colon") and `9999-reference.md` colon entries — capitalization of the
      first word after a colon. TS-26 `13-punctuation.adoc` gives colon rules
      but not the follow-on capitalization convention. Recommend
      `13-punctuation.adoc`.

      **Resolved.** Closed by a new paragraph and example appended to the
      existing "Colons" section in `13-punctuation.adoc`. Requires
      lowercasing the first word after a colon unless it is a proper noun or
      the colon introduces more than one complete sentence.

- [x] `0800-conciseness.md` ("Contractions") / `9999-reference.md:2506-2508`
      — contractions: use them but do not overdo. Not addressed. Recommend
      `14-sentences-and-paragraphs.adoc` or `01-voice-and-tense.adoc`.

      **Resolved.** Closed by a new paragraph in `01-voice-and-tense.adoc`,
      placed there rather than `14-sentences-and-paragraphs.adoc` since the
      file already covers register-level voice choices. Permits contractions
      for natural phrasing and requires stopping short of a conversational
      register.

- [x] `9999-reference.md:1373-1375` / `2377-2378` — formatting of "eg"/"ie"
      (no full points, no following comma). TS-26 `04-abbreviations.adoc`
      does not address these abbreviations' punctuation. Recommend
      `04-abbreviations.adoc`.

      **Resolved.** Closed by a new paragraph in `04-abbreviations.adoc`.
      Requires "eg"/"ie" without periods and without a following comma, and
      recommends spelling out the full phrase where the document is not
      already abbreviation-dense.

- [x] O'Reilly Style Guide#Code (Line Length, Syntax Highlighting,
      Formatting Code in Word) — code-block line-length limits, syntax
      highlighting, and "indent with spaces not tabs". TS-26
      `11-code-blocks.adoc` covers placeholders and CLI prompts only.
      Recommend `11-code-blocks.adoc`.

      **Resolved.** Closed by a new "Formatting" section in
      `11-code-blocks.adoc`. Requires the `[source,<language>]` language tag
      (cross-referencing the repository style guide's existing rule), spaces
      over tabs, and keeping example lines narrow enough to avoid horizontal
      scroll — the book-series-specific line-length table itself was left as
      out-of-scope publisher tooling (already recorded under Out-of-scope).

## Partial

- [x] O'Reilly Style Guide#Headings — headings should contain no inline code
      font, bold, or italic, and acronyms in headings should be expanded
      unless common. TS-26 `02-headings.adoc` covers sentence case and level
      skipping but omits these. Recommend `02-headings.adoc`.

      **Resolved.** Closed by two new paragraphs in `02-headings.adoc`.
      Prohibits monospace, bold, or italic formatting within a heading, and
      requires expanding an acronym in a heading unless it is common enough
      for the audience to recognize unexpanded, cross-referencing the
      existing first-use spelling-out rule in "Abbreviations and acronyms".

- [x] O'Reilly Style Guide#Abbreviations & Acronyms /
      `9999-reference.md:620-656` / `OLD-NOTES.md:661-699` — abbreviation
      mechanics beyond first-use spelling-out: plural forms (CDs), "a" vs
      "an" by pronunciation, omitting periods, no "the" before pronounceable
      acronyms. TS-26 `04-abbreviations.adoc` covers only spelling-out.
      Recommend `04-abbreviations.adoc`.

      **Resolved.** Closed by the same new paragraph in
      `04-abbreviations.adoc` as the eg/ie item above. Requires plural
      abbreviations formed with a lowercase "s" and no apostrophe (cross-
      referencing the "Apostrophes" section), "a"/"an" chosen by
      pronunciation, periods omitted from all-caps abbreviations, and "the"
      omitted before a pronounceable acronym functioning as the noun itself.

- [x] `9999-reference.md:1214-1222` / `9999-reference.md:2040-2057` /
      `OLD-NOTES.md:4243` (gender-neutral phrasing) — person-first disability
      language ("disabled people" not "the disabled"; "uses a wheelchair") and
      gender-neutral pronouns / "mankind" → "humankind". TS-26
      `05-inclusive-language.adoc` covers violent/ableist connotations and
      idioms but not pronoun strategy or person-first phrasing. Recommend
      `05-inclusive-language.adoc`.

      **Resolved.** Closed by the "disabled people, disabled persons" entry
      in the new glossary (`16-glossary.adoc`), added as part of the
      2026-08-14 full-glossary batch (see the Missing-list A-Z-spelling-list
      item below). Requires person-first phrasing for disability ("disabled
      people," not "the disabled"; "uses a wheelchair," not "wheelchair
      bound"), and extends the same principle to gender-neutral language:
      "humankind" over "mankind," and a gender-neutral construction over
      "he"/"his" for a person of unspecified gender. Placed in the glossary
      rather than `05-inclusive-language.adoc` because it is a word/phrase-
      level ruling consistent with the rest of that new section, with the
      existing `05-inclusive-language.adoc` file left as the place for the
      higher-level principle it already states.

- [x] O'Reilly Style Guide#Dates and Numbers /
      `9999-reference.md:1600-1603` / `9999-reference.md:3339` /
      `OLD-NOTES.md:1423-1427` — ordinals (first–ninth spelled, 10th+ figures),
      hyphenated fractions, "percentage points" vs percent, and ranges.
      TS-26 `10-numbers-dates-units.adoc` covers the 0–9/10+ split, units, and
      ISO dates only. Recommend `10-numbers-dates-units.adoc`.

      **Resolved.** Closed by the same new paragraph in
      `10-numbers-dates-units.adoc` as the time-of-day item above. Requires
      spelled ordinals first–ninth and figure ordinals from 10th, hyphenated
      spelled-out fractions used as modifiers, "percentage points" for a
      difference between two percentages (with a worked example showing why
      "percent" would be wrong), and en-dash numeric ranges.

- [x] O'Reilly Style Guide#Lists — list items take no periods unless one item
      is a complete sentence (then all do); "variable lists" for term/
      definition pairs; nested bullets use em dashes. TS-26 `08-lists.adoc`
      covers parallelism and nesting depth but not the period rule or
      variable lists. Recommend `08-lists.adoc`.

      **No change needed** for the period rule: `08-lists.adoc:10-11` already
      requires punctuating list items as sentences when any item is a full
      sentence, matching the source. **Resolved** for the rest, by two new
      paragraphs in `08-lists.adoc`. Requires an em dash (not a repeated
      bullet character) to mark a nested list level, and requires converting
      a bulleted list of short term/definition pairs into an AsciiDoc
      description list (`Term:: Definition`) instead.

- [x] O'Reilly Style Guide#Typography and Font Conventions — finer emphasis
      conventions: placeholders in constant-width italic, user-typed text in
      constant-width bold, URLs/filenames in italic (O'Reilly) vs the
      standard's monospace. TS-26 `06-emphasis.adoc` gives the high-level
      monospace/bold/italic split but not these refinements. Recommend
      `06-emphasis.adoc`.

      **Resolved.** Closed by a new paragraph in `06-emphasis.adoc`. Requires
      italic monospace for a placeholder within a monospace span (cross-
      referencing the existing `13-punctuation.adoc` "Placeholders" rule) and
      regular monospace for literal typed/output text. Deliberately keeps
      URLs and file names in monospace rather than adopting O'Reilly's italic
      convention, since TS-26 already normatively assigns monospace to that
      category — reconciling the two would contradict existing content, not
      close a gap.

- [x] `OLD-NOTES.md:4243` / `9999-reference.md` (usage entries) /
      `0700-redundancy.md` — commonly confused words (fewer/less, comprise,
      affect/effect, flaunt/flout, disinterested/uninterested). TS-26
      `03-terminology.adoc` covers "one term per concept" and plain words but
      gives no commonly-confused-words guidance. Recommend
      `03-terminology.adoc` (or out-of-scope as a word list — see below).

      **Resolved.** Closed by a new "Commonly confused words" section in the
      new glossary (`16-glossary.adoc`), sourced from `9999-reference.md`'s
      full homophones list (found at `9999-reference.md:2270-2299` while
      transcribing letter H's "homophones" entry). Covers 17 word pairs
      (accept/except, affect/effect, biannual/biennial, canon/cannon,
      discrete/discreet, and others), and is cross-referenced from every
      individual glossary entry for an affected word. Placed in the
      glossary rather than `03-terminology.adoc` because it is dictionary-
      style word-pair content consistent with the rest of the new section,
      not the terminology-consistency guidance `03-terminology.adoc`
      already covers.

- [x] `0600-voice.md` / `OLD-NOTES.md:4243` — a detection heuristic for
      passive voice (be-verb forms: am/is/was/were/been; subject receives the
      action). TS-26 `01-voice-and-tense.adoc` states the preference but gives
      no way to recognize passive constructions. Recommend
      `01-voice-and-tense.adoc`.

      **Resolved.** Closed by a new paragraph in `01-voice-and-tense.adoc`.
      Requires recognizing passive voice by its be-verb-plus-past-participle
      form and the subject receiving rather than performing the action,
      states the "by <actor>" insertion test, and gives a be-verb-but-active
      counterexample (past progressive) so the heuristic isn't
      over-applied.

- [x] `0700-redundancy.md` / `0800-conciseness.md` — general redundancy and
      overused-word lists ("very", "actually", "basically", "completely") as
      plain good-writing rules. TS-26 `15-ai-writing-tells.adoc` covers much of
      this but frames it as LLM tells rather than general editing. Recommend
      cross-linking or a general note in `14-sentences-and-paragraphs.adoc`.

      **Resolved.** Closed by a new "Overused words" section in
      `14-sentences-and-paragraphs.adoc`. Gives a shorter, representative
      subset of the source's word list plus a removal test for spotting
      others, and cross-references the LLM-associated vocabulary list in
      `15-ai-writing-tells.adoc` as a related but distinct concern rather
      than duplicating that list.

- [x] `0100-forward.md` / `0300-general-style.md` (Orwell's six rules) /
      `0900-structure-pacing.md` — sentence fragments are acceptable for
      emphasis. TS-26 `14-sentences-and-paragraphs.adoc` covers sentence length
      and pace but not fragment use. Recommend `14-sentences-and-paragraphs.adoc`.

      **Resolved.** Closed by a new paragraph in
      `14-sentences-and-paragraphs.adoc`, appended to the existing pacing
      guidance. Permits a fragment as a deliberate pacing device and
      restricts it to a clause a reader could not mistake for an
      accidentally incomplete sentence.

## Missing

- [x] `api-style-guide.md:27-44` (surfaced while gap-closing TS-21, HTTP APIs,
      2026-08-14) — document-level convention: RFC 2119 keyword
      interpretation, all-caps rendering of "REST"/"JSON", fixed-width
      rendering of machine-readable text, and URI Template (RFC 6570) syntax
      for variable blocks in prose/URL templates. TS-21 confirmed this as
      out-of-scope for itself — it is a cross-cutting authoring convention,
      not HTTP-API-specific content — and the user asked that it be routed
      here instead, since these are exactly the kind of document-level
      conventions this standard's style guide governs. Not yet checked
      against TS-26's current content; needs its own coverage check before
      being actioned. Recommend a new section, or extending an existing one
      on abbreviation/keyword conventions, once reviewed.

      **Resolved.** Re-checked against TS-26's current content: two of the
      four sub-items were already covered — fixed-width rendering of
      machine-readable text (`06-emphasis.adoc`, "Use monospace formatting
      for anything a reader might type or that the system might output
      literally") and all-caps rendering of acronyms like REST/JSON
      (`04-abbreviations.adoc`, "Omit periods from an abbreviation written in
      capitals") — so no change was needed for either. The remaining two were
      genuinely missing. RFC 2119 keyword interpretation is closed by a new
      "Normative language" section in `01-voice-and-tense.adoc`, requiring
      capitalized keyword rendering and a stated interpretation declaration
      before a document may rely on the keywords carrying RFC 2119 weight.
      URI Template (RFC 6570) syntax for variable blocks in prose is closed
      by extending the existing "Placeholders" section in
      `11-code-blocks.adoc`, which already established the standard's own
      `<placeholder>` angle-bracket convention — added the inline-prose case
      (a URL with a variable segment) and the exception for a formal grammar
      like URI Template that uses curly braces instead. Source added to the
      page's `== References`, cited by its canonical GitHub location
      (`levid-gc/paypal-api-standards`), matching how TS-21 already cites the
      same source elsewhere in this repository.

- [x] `alistapart.com/article/standards-for-writing-accessibly/` (fetched
      2026-08-15, routed in from the Unresolved link-collection triage) —
      procedural/instructional phrasing for accessibility: prefer
      chronological sequencing over spatial references when describing UI
      interactions (e.g. "next, select OK to continue" over "click the OK
      button below," since position is not stable for a screen-reader or
      voice-interface user), and prefer device-agnostic action verbs
      ("select," "choose," "view") over device-specific ones ("click,"
      "tap," "press," "see") in procedural steps. TS-26 has no
      instructional-step-writing guidance at all — the closest existing
      content is `09-links.adoc`'s descriptive-link-text rule and
      `12-referencing.adoc`'s prohibition on "above"/"below" for figures,
      neither of which covers UI-interaction verbs or step sequencing.
      Recommend a new section, most likely in `14-sentences-and-
      paragraphs.adoc` or as a new numbered partial, since this is
      procedural prose rather than punctuation, emphasis, or referencing.

      **Resolved.** Closed by a new "Instructional steps" section in
      `14-sentences-and-paragraphs.adoc`. Requires chronological sequencing
      over spatial reference for describing UI interactions, and requires
      a device-agnostic action verb ("select," "choose," "view") over a
      device-specific one ("click," "tap," "press," "see"). Source added
      to the page's `== References`.

## Out-of-scope

- [x] `copywriting.adoc` ("Copywriting guidelines") — UI/short-message
      conventions: titles and short messages should not end with a full stop;
      short messages may use hyphens for readability. Not addressed
      (relevant to microcopy/UI text in documentation). Recommend a new
      subsection of `13-punctuation.adoc` or `06-emphasis.adoc`.

      **Confirmed out-of-scope.** 2026-08-14. UI microcopy (button labels,
      toast messages, short-message text) is a different register and
      audience from the documentation prose TS-26 covers. Per the user's
      instruction, the gap was not dropped: it was routed to TS-15
      (User interfaces), the general-purpose UI standard, as a new Missing
      item in its own `GAPS.md` — see that file's "Fourth run, 2026-08-14"
      entry.

- [x] `OLD-NOTES.md`, `OLD-NOTES-2.md`, `9999-reference.md`, `OLD-LOOKUP.md`
      — honorifics and titles for people (Mr/Mrs/Miss/Ms/Dr, "Prime Minister
      Blair", "the Rev", knights/dames), capitalization of political offices,
      parties, acts, government departments, the Crown, etc. Flagged: this is
      news/journalism style; a technical-writing standard has no need for it.

      **Overruled and resolved, 2026-08-14.** The user asked for a full,
      unfiltered import of the A-Z word list rather than accepting this
      exclusion. Closed by a new "Honorifics and personal titles" section in
      the new glossary (`16-glossary.adoc`), adapted from `OLD-NOTES.md`'s
      "Titles" section (found around line 4133). Political-office
      capitalization is covered inline in the A-Z entries for "capital
      letters" and "president." Moved here from Out-of-scope rather than
      Missing/Partial, per the original classification.

- [x] `OLD-NOTES.md:3385-3567`, `9999-reference.md:3405-3555`,
      `OLD-NOTES-2.md:1469-1533` — place-name and country-name conventions
      (Mumbai not Bombay, "the Netherlands", Ukraine, Côte d'Ivoire,
      transliteration of foreign personal names). Flagged: reference style for
      journalism, not technical documentation.

      **Overruled and resolved, 2026-08-14.** Closed by a new "Countries and
      nationalities" section and a new "Transliteration of foreign names"
      section in the glossary (`16-glossary.adoc`), merged from the
      near-identical content duplicated across `OLD-NOTES.md:3385-3567` and
      `OLD-NOTES-2.md:1469-1533`. Individual place names (Mumbai, the
      Netherlands, Ukraine) are covered inline in the A-Z "placenames and
      venues" entry under P.

- [x] `9999-reference.md`, `OLD-NOTES.md` (sports, currencies, weights/
      measures, placenames, dog breeds, wine names, fashion weeks, grand
      prix) — specialized reference word lists. Flagged: domain-specific
      journalism reference, far outside a technical-doc style guide.

      **Overruled and resolved, 2026-08-14.** This item's premise was that a
      dedicated sports/currency/measures list existed separately; on
      re-verification, `9999-reference.md` has no such standalone list —
      this content is scattered through individual A-Z entries (currencies,
      cricket terms, golf, grand prix, wines, measurements and quantities),
      all of which are already transcribed in the glossary's A-Z as part of
      the full import. No separate section was needed.

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

- [x] `9999-reference.md`, `OLD-NOTES.md` (long A-Z spelling and word-choice
      lists: "acknowledgment not acknowledgement", "aeroplane not airplane",
      "-ise vs -ize", British vs American spelling) — a dictionary/word-list,
      not reusable style rules. Flagged: lexicography, outside the standard's
      purpose.

      **Overruled and resolved, 2026-08-14.** The user explicitly asked for
      the full A-Z list to be imported as a glossary, reversing this
      exclusion. Closed by a new `16-glossary.adoc` partial: a full A-Z
      transcription of `9999-reference.md`'s roughly 1,373 dictionary
      entries (all 26 letters), merged with a "Commonly confused words"
      section (from the same source's separate homophones list), a
      "Countries and nationalities" section, a "Transliteration of foreign
      names" section, and an "Honorifics and personal titles" section (all
      from `OLD-NOTES.md`/`OLD-NOTES-2.md`, which duplicate the same content
      — see the honorifics and place-name Out-of-scope items above, both
      also overruled and closed by this same partial), plus a supplementary
      "Food and drink terms" A-Z embedded in the source's letter F. Two
      corrections were made to the source during transcription: `9999-
      reference.md`'s "affect, effect" entry (line 51-52) was garbled with a
      different word pair's definition — the correct definition, found
      elsewhere in the same file at line 2274, was used instead; and the
      "Americanisms"/"-ise"/"metric system"/"times" entries, which assume a
      British-house-style default the source's publication used, are
      annotated in place to note they differ from this standard's own
      American-English and 24-hour-time defaults, rather than silently
      presented as this standard's rule. `08-lists.adoc`'s existing
      "Referring to figures, tables, and examples" rule does not apply to a
      glossary entry, so no cross-reference conflict was introduced. Nothing
      was dropped except one entry (a publication-specific spelling note
      with no transferable content) and a handful of items whose content
      already appears verbatim in another A-Z entry.

- [ ] `OLD-NOTES.md:4243` / `OLD-NOTES-2.md:2001-2011` — general English
      grammar (split infinitives, dangling participles, subjunctive mood,
      gerunds take possessive adjectives, "an" before vowel sounds). Flagged:
      a general-grammar reference; TS-26 deliberately scopes itself to
      prose-level/presentational conventions, not grammar instruction.

- [ ] `OLD-NOTES.md:3347-3361` / `9999-reference.md:805-808` — Latin/biological
      nomenclature, classical-music work referencing, biblical citation
      format. Flagged: specialized referencing domains not relevant to
      technical documentation.

- [x] `accessibility.md`, `styleguides.md`, `writing.md`,
      `reference-resources.md` — these files are lists of external URLs with
      at most a one-line gloss each; their linked content was not fetched
      (see Unresolved). Flagged: pointers, not reference content in
      themselves.

      **Resolved, 2026-08-15.** Superseded by the Unresolved-section
      resolution below, which read these files (plus `seo.md`) in full and
      fetched the most promising of their ~77 URLs. Confirmed out-of-scope
      overall — see that resolution note for the per-URL findings and the
      one genuine gap it surfaced (procedural/instructional phrasing, in
      Missing above).

## Unresolved

- [x] `__TODO__/_todo/Web Copy That Sells - Second Edition.pdf` — binary PDF,
      not read (no text-extraction tool available to the agent). Not included
      in the comparison.

      **Resolved, 2026-08-15.** `pdftotext` (now available at
      `/usr/bin/pdftotext`) was used to extract the full text (`-layout`
      mode; the PDF logged benign `Dictionary key must be a name object`
      warnings from a malformed embedded object but extracted cleanly
      otherwise). Skimmed the front-matter praise, and read a full
      chapter-length sample from "Crafting Your Copy," including the
      book's "Selling Quotient" scoring formula. **Confirmed out-of-scope
      for TS-26.** The book is exclusively direct-response sales
      copywriting: headline formulas designed to "stop readers dead in
      their tracks," emotional/psychological persuasion tactics (fear,
      greed, guilt, curiosity as "proven emotional drivers"), embedded
      commands in link text, and a scoring rubric for a website's
      "selling quotient." None of this is documentation prose guidance —
      it is marketing copy for driving purchase decisions, the same
      register as `copywriting.adoc`'s UI/short-message conventions,
      which this file's Out-of-scope section already confirmed
      out-of-scope for TS-26 and routed to TS-15 instead. This PDF sits
      even further from TS-26's purpose than `copywriting.adoc` did (that
      file was at least about short UI microcopy mechanics; this book is
      about sales-page rhetoric), so no routing target applies here —
      it is simply not a technical-writing-adjacent resource at all, for
      any standard in this repository.

- [x] `__TODO__/_todo/accessibility.md`, `seo.md`, `styleguides.md`,
      `writing.md`, `reference-resources.md` contain ~40 external URLs (e.g.
      alistapart.com, nngroup.com, copyblogger.com, monzo.com/tone-of-voice).
      These are link collections; the linked pages were not individually
      fetched. Only the local file content was used.

      **Resolved, 2026-08-15.** Read all five files directly; they total
      77 URLs (`accessibility.md`: 1, `seo.md`: 1, `styleguides.md`: 1,
      `writing.md`: 4, `reference-resources.md`: 70). The great majority,
      concentrated in `reference-resources.md`, are early-2010s web-design/
      content-strategy/SEO/blogging posts (webdesignerdepot.com,
      copyblogger.com, smashingmagazine.com, problogger.com, etc.) —
      already covered by this file's existing Out-of-scope items for
      content strategy, SEO, and marketing/web-strategy, so the bulk was
      triaged out without fetching. 8 of the most promising
      writing-prose-relevant URLs from reputable sources were fetched:

      - `alistapart.com/article/standards-for-writing-accessibly/` — UI
        microcopy/accessibility phrasing (chronological over spatial
        references, device-agnostic action verbs, critical info before
        action points). Its "click here" point duplicates the existing
        `09-links.adoc` descriptive-link-text rule; its "above/below"
        point duplicates the existing `12-referencing.adoc` figure-
        reference rule. Yielded one genuine new item — see Missing below.
      - `monzo.com/tone-of-voice/` — brand tone-of-voice guide. Confirmed
        out-of-scope: the source's own text scopes its distinctive
        "everyday magic" and "warm wit" principles to "brand and
        marketing writing" specifically; only its generic "clear,
        inclusive, reader-focused" principle would transfer, and that is
        already TS-26's baseline throughout. No actionable gap.
      - `nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/`
        — validates conciseness/scannability/objectivity principles TS-26
        already states via headings, lists, and `14-sentences-and-
        paragraphs.adoc`'s plain-sentence guidance. No new rule; the
        article is usability-research support for existing content, not
        a gap.
      - `nngroup.com/articles/microcontent-how-to-write-headlines-page-titles-and-subject-lines/`
        — confirmed out-of-scope: explicitly about web microcontent
        (search-result snippets, social posts, email subject lines), not
        document headings or technical prose.
      - `nicolefenton.com/interface-writing/` — confirmed out-of-scope:
        explicitly about UI/product microcopy (buttons, error messages,
        tooltips), the same register already routed to TS-15.
      - `gov.uk/guidance/content-design/writing-for-gov-uk` — redirects
        (301) to `guidance.publishing.service.gov.uk/writing-to-gov-uk-
        standards/tone-of-voice/`, which itself redirects again to a
        `writing-guidelines/` page; the content could not be reached
        through two redirect hops in the time available. Left unfetched;
        not actioned.
      - `plainenglish.co.uk/how-to-write-in-plain-english.html` — dead
        link (HTTP 404). Not actioned.
      - `orwell.ru/library/essays/politics/english/e_polit/` (Orwell's
        "Politics and the English Language," linked from `writing.md`)
        — the source is already cited in TS-26's `== References` (the
        Wikipedia "Signs of AI writing" entry draws on the same
        tradition), and its six numbered rules (avoid stale metaphors,
        prefer short words, cut unnecessary words, prefer active voice,
        avoid jargon/foreign phrases with a plain equivalent) are all
        already independently covered by existing TS-26 content: active
        voice (`01-voice-and-tense.adoc`), plain terminology
        (`03-terminology.adoc`, `05-inclusive-language.adoc`), and
        conciseness (`14-sentences-and-paragraphs.adoc`'s "Overused
        words" section). No new rule.

      The remaining ~69 URLs were not individually fetched: triage by
      title/domain against this file's existing Out-of-scope categories
      (content strategy, SEO, marketing copy, UI microcopy) placed all of
      them in an already-flagged out-of-scope bucket with high confidence
      — titles like "5 tips on how to write a killer slogan,"
      "copywriting A to Z," "magnetic headlines," and "the 10 commandments
      of PageRank sculpting" are unambiguously sales-copy or SEO content,
      consistent with the pattern already established across this file's
      Out-of-scope section.