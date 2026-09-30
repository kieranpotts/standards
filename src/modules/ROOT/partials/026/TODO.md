# TS-26 deep dive

Findings from a deep review of TS-26: Technical Writing Style Guide

~677 lines across 54 files (the page plus 53 partials).

Assessed against the repository [style guide](../../../../../docs/style-guide.md), [TS-26: Technical Writing Style Guide](../../pages/026.adoc) itself, [TS-27: Markdown](../../pages/027.adoc), [TS-28: AsciiDoc](../../pages/028.adoc), and the [template](../../../../../template/). Where the style guide is silent, the de-facto convention of the sibling standards was sampled.

**Assessment.** The alphabetical topic layout works, and most individual rules are sound, concrete, and illustrated. The main problem is that TS-26 does not follow itself. Its prose breaks its own rules on colons, dashes, filler words, quoted punctuation, first person, tense, units, numbers, emphasis, and reference-list order, often in the example that is meant to demonstrate the rule. Several rules also contradict each other outright, most seriously the colon rule, which forbids a construction the standard uses about 50 times. The references topic has drifted furthest. It is written in the first person, prescribes three incompatible entry formats, cites a paper with the wrong authors and title, and carries repository-specific AsciiDoc mechanics into a standard that declares itself format-agnostic.

**Status:** All four tiers are applied and verified, except S1, which waits on D3. D3 and D4 are open and need your approval, because they edit files outside TS-26. The two Tier 4 questions are settled: the rule now allows an optional publisher, and WCAG, APA, MLA, FAQ, and PR stay unexpanded. The seven unpunctuated "eg" instances elsewhere in the repository were fixed at your request.

## Priority order

1. **Correctness.** Contradictions and factual errors. A reader cannot comply with a standard that says two incompatible things.

2. **Coherence.** Structural problems. Structure must settle before content is added to it.

3. **Completeness.** Coverage gaps. Filled into a structure that has stopped moving.

4. **Conventions.** Style-guide conformance. Last, because content edits invalidate cosmetic fixes made too early.

Sections 1 and 2 below are Tier 1. Section 3 is Tier 2. Section 4 is Tier 3. Sections 5 and 6 are Tier 4.

## Decisions needed

Each decision has a recommendation. Record the user's choice and rationale here before working the dependent items.

- [x] **D1. The colon rule versus the standard's own labels.** colons.adoc:7 says "The only valid use for a colon is within a single sentence that ends with a short, comma-separated list". TS-26 itself uses a colon after "Example", "Examples", "Bad", "Good", and "Write" roughly 50 times, as well as to introduce list and code blocks (see C1–C3 and the colon items in section 5). **Recommendation:** amend the rule, not the prose. Permit a colon after a one-word label that introduces an inline example ("Example:"), keep the ban on colons introducing blocks and joining independent clauses, and drop "The only valid use". Rewriting 50 labels would make every example sentence longer to satisfy a rule that the author evidently does not hold. Decided (recommendation accepted): amend the rule, not the prose. Recorded in colons.adoc.

- [x] **D2. One convention for good and bad examples.** TS-26 uses four conventions. `.Bad style` / `.Good style` block titles (colons.adoc:19, commas.adoc:14, semicolons.adoc:7), `Bad:` / `Good:` paragraphs (language.adoc:13, significance-claims.adoc:5, terminology.adoc:15, trailing-participial-clauses.adoc:7), a `* Good:` / `* Bad:` list with the good example first (sentences-and-paragraphs.adoc:5), and ✅ / ❌ line prefixes in a listing block (quotation-marks.adoc:9). Eight sibling standards (016, 021, 022, 027, 031, 032, 061, and TS-26 itself) use ✅ / ❌, and no sibling uses the other three. **Recommendation:** convert every good/bad pair to ✅ / ❌ lines in a listing block. This also settles the inconsistent period placement between terminology.adoc:15 (outside the quote) and language.adoc:13 (inside), because the examples will no longer be quoted. Decided (recommendation accepted, ✅ / ❌ lines in a listing block). Not yet applied, because converting the examples belongs to Tier 4.

- [ ] **D3. Where the repository-specific references rules live.** citations.adoc:51-62 prescribes the `partials/NNN/99-references.adoc` file, the `{link-<slug>}` AsciiDoc attribute syntax, and the page-top attribute block. 01-introduction.adoc:7 says TS-26 "is agnostic about the source format", and the same mechanics are already in docs/style-guide.md:71-75 and TS-28 14-links.adoc:51-60. **Recommendation:** move the subsection's unique content (entry order, one work per entry, no annotations) into docs/style-guide.md, and cut the subsection. This touches a file outside TS-26, so it needs explicit approval. The alternative is to keep it and amend 01-introduction.adoc:7 to admit the exception. Open. It needs your approval because it edits a file outside TS-26.

- [ ] **D4. Unprefixed partial file names.** docs/style-guide.md:47-51 says content files MUST be named with a two-digit numeric prefix. TS-26's 50 topic partials (`a-an.adoc` … `units-of-measure.adoc`) have none, deliberately, so that the alphabetical order in 01-introduction.adoc:3 follows from the file names. **Recommendation:** keep the names, and add a documented exception for TS-26 to docs/style-guide.md (outside scope, needs approval). Renumbering would be pure churn, and every new topic would force a renumber. Open. It needs your approval because it edits a file outside TS-26.

- [x] **D5. Em dashes that join independent clauses.** sentences-and-paragraphs.adoc:3 says to avoid joining two independent clauses with a dash (it says "hyphen", see P11), and its bad example is exactly that. dashes.adoc:5 then gives as its model em-dash usage "the change is backward compatible — no client update is required", which joins two independent clauses. citations.adoc:62 and apostrophes.adoc:9 do the same. **Recommendation:** keep the sentences-and-paragraphs rule. Replace the dashes.adoc:5 example with a true parenthetical, and split the clauses at citations.adoc:62 and apostrophes.adoc:9. Decided (recommendation accepted): keep the ban on joining independent clauses with a dash, and fix the examples. The dashes.adoc example is done (C4). apostrophes.adoc:9 and citations.adoc:62 remain in Tier 4.

- [x] **D6. "The following" as a positional reference.** figures-tables-and-examples.adoc:5 bans positional references. "(see below)" at citations.adoc:14 and "above" at citations.adoc:62 are clear violations. But "the following example", "An example follows.", and "the following checks" (citations.adoc:43, :47, requirements-levels.adoc:9, lists.adoc:10, :20) are borderline. **Recommendation:** permit "the following" and "follows" for content that directly follows the sentence, since the rule's rationale (reflow moving a figure away from its citation) does not apply to an adjacent example. State this explicitly in figures-tables-and-examples.adoc. Decided (recommendation accepted): "the following" and "as follows" are allowed when the example directly follows. Recorded in figures-tables-and-examples.adoc. The "see below" and "above" instances at citations.adoc:14 and :62 remain Tier 4 fixes.

- [x] **D7. The document-title case.** headings.adoc:5 says sentence case "applies equally to document titles". The standard's own title, `TS-26: Technical Writing Style Guide` (pages/026.adoc:1), and every sibling standard's title are in title case. **Recommendation:** add an explicit exception to headings.adoc treating the titles of the standards as titles of works. Retitling all the standards is a repository-wide sweep. Decided (recommendation accepted): the title of a technical standard is an exception to sentence case. Recorded in headings.adoc.

- [x] **D8. The RFC 2119 boilerplate.** requirements-levels.adoc:9 says "A document that relies on these keywords MUST state, once, near its start" that they carry RFC 2119 meanings. TS-26 does not. The collection states it once, at pages/index.adoc:15. **Recommendation:** amend requirements-levels.adoc:9 to allow the statement to appear once for a collection of documents, in its front page. Decided (recommendation accepted): a collection may state the RFC 2119 meaning once, on its front page. Recorded in requirements-levels.adoc (C15).

- [x] **D9. English spelling variety.** See G1. **Recommendation:** American English, which matches the existing spelling ("organized", "behavior", "colorful", "labeled"). Decided (recommendation accepted, American English). Not yet applied, because the rule belongs to Tier 3 (G1).

## 1. Contradictions

- [x] **C1.** colons.adoc:7 says "The only valid use for a colon is within a single sentence that ends with a short, comma-separated list", but colons.adoc:13 says to capitalize after a colon when "the colon introduces more than one complete sentence", which by :7 can never happen. Resolve with D1. Done. colons.adoc now lists the permitted uses, and the capitalization rule no longer mentions multiple sentences (D1).

- [x] **C2.** colons.adoc:5 forbids a colon between two independent clauses without exception, but sentences-and-paragraphs.adoc:8 says punctuation-joined clauses "are still appropriate" where splitting "would lose an explicit cause-and-effect or contrast", and calls the rule "a default, not an absolute prohibition". semicolons.adoc:5 makes the same allowance. Either colons.adoc:5 gains the same exception, or sentences-and-paragraphs.adoc:8 must exclude colons. Done, resolved the second way: colons.adoc stays strict, and sentences-and-paragraphs.adoc now limits the cause-and-effect exception to semicolons and dashes and points at Colons. Its "hyphen" became "dash" (also P11).

- [x] **C3.** colons.adoc:7 (only valid use is a sentence ending with a short list) conflicts with TS-28 17-lists.adoc:249-256, which prescribes `*Status:* Active` key-value lead-ins. Resolve with D1, so the rule names the key-value lead-in as a permitted use. Done. The key-value lead-in is now the third permitted use in colons.adoc, with the colon inside the bold markers.

- [x] **C4.** sentences-and-paragraphs.adoc:3-6 (avoid joining independent clauses with a dash) conflicts with the model example at dashes.adoc:5. Resolve with D5. Done. The dashes.adoc example is now a true parenthetical ("the default retry limit — three attempts — applies to every request"), "abrupt break" is gone, and the rule against joining independent clauses is stated there (D5).

- [x] **C5.** filler-words.adoc:3 bans "so" outright, but commas.adoc:12 recommends "so" as a coordinating conjunction and commas.adoc:21 uses it in the good example. Scope the filler rule to "so" as an intensifier ("so much faster"), not as a conjunction ("so the client retried it") or in "so that". Done. "so" is removed from the banned list, and the rule now bans only "so" as an intensifier, with the conjunction expressly allowed.

- [x] **C6.** language.adoc:11 says "Avoid marketing words", listing "seamless" and "robust", but terminology.adoc:11 lists the same two words and says "None is forbidden outright". Pick one strength, and hold each word in only one list (see S7). Done. "robust" and "seamless" are removed from terminology.adoc, so the words stay only in the avoid list in language.adoc.

- [x] **C7.** headings.adoc:9 says headings SHOULD NOT "ask a question", but question-marks.adoc:3 says "A valid example is a heading phrased as a question in a FAQ section". Add the FAQ exception to headings.adoc:9, or drop it from question-marks.adoc:3. Done. headings.adoc:9 now excepts FAQ entries.

- [x] **C8.** admonitions.adoc:3 defines an admonition as information "that the reader could reasonably skip", and :23 restricts them to "asides that are secondary to a linear read-through". But :13 defines IMPORTANT as "Information required to complete a task correctly", and :15 defines WARNING as risk of data loss or security exposure. Neither can be skipped. Reword :3 and :23 so that admonitions set apart information by kind (a warning, a tip), not by whether it can be skipped. Done. admonitions.adoc:3 no longer defines an admonition as skippable. :23 now limits the skippable rule to NOTE and TIP, and says IMPORTANT, WARNING, and CAUTION are for information the reader must not miss. Also fixed "panel panel" (P1).

- [x] **C9.** emphasis.adoc:9 says "Italics may also be used for foreign words", which is optional, but foreign-words.adoc:3 says "Italicize a foreign word", which is mandatory. The example in emphasis.adoc:9, "_ad hoc_", is itself an absorbed loanword that foreign-words.adoc:5 says to write in roman type. Make emphasis.adoc:9 defer to foreign-words.adoc, with a different example. Done. emphasis.adoc now defers to Foreign words, and the "_ad hoc_" example is gone.

- [x] **C10.** foreign-words.adoc:3 gives "the API uses a _naïve_ Bayes classifier" as the model for italicizing a foreign word, but "naive" is standard English vocabulary, listed without italics or diaeresis in English dictionaries, and "naive Bayes" is the standard technical term. By foreign-words.adoc:5 and :7 it should be roman and unaccented. Replace the example with an unabsorbed phrase. Done. The example is now "the patch delivers the _coup de grâce_ to the legacy parser", which shows both the italics and the preserved diacritic.

- [x] **C11.** instructional-steps.adoc:5 says to prefer "view" over "see", but TS-26 uses "See" for every cross-reference (01-introduction.adoc:5, :7, admonitions.adoc:19, citations.adoc:14, :53, :62). Scope instructional-steps.adoc:5 to verbs that describe an action in a user interface. Done. The verb rule is scoped to steps that describe a user interface, and cross-reference "see" is expressly exempt.

- [x] **C12.** requirements-levels.adoc:3 lists SHALL and SHALL NOT among the keywords, but its own example boilerplate at :13 omits them, as does pages/index.adoc:15. Either drop SHALL from :3 (RECOMMENDED, since the collection does not use it) or add it to the boilerplate. Done. SHALL and SHALL NOT are removed from requirements-levels.adoc:3, matching the boilerplate and pages/index.adoc.

- [x] **C13.** citations.adoc prescribes three incompatible entry formats. :20 is `<author> (<year>). _<title>_. <publication>`, with no final period. :57 is `<author> (<year>). {link-<slug>}[_<title>_].`, with a final period, and :62 says "omit the publisher". :39-41 adds volume, issue, and page range. Settle on one format for body citations and state where the reference-list format differs. Done, in part. The entry format in "References sections in the technical standards" is now stated to be a reduced form of the general one, and "Johnson, M (2020)" became "Johnson, M. (2020)" to match the no-year variant. The general format still has no final period while the reduced form has one, and that is now stated. The separate "et al" period is left for Tier 4.

- [x] **C14.** emphasis.adoc:3-7 allows bold only for UI elements and newly defined terms, and forbids it for emphasis. TS-28 17-lists.adoc:221 and the template's 04-best-practices.adoc use bold lead-in terms in list items, and admonitions.adoc:9-17 does too. Add the bold lead-in as a third permitted use. Done. emphasis.adoc now permits a bold lead-in term in a list item, terminated by a full stop. The colon-terminated lead-ins in admonitions.adoc:9-17 remain a Tier 4 item.

- [x] **C15.** requirements-levels.adoc:9 (D8). The standard relies on RFC 2119 keywords without stating so near its start. Done, with D8. requirements-levels.adoc:9 now lets a collection state the RFC 2119 meaning once, on its front page.

## 2. Factual errors

- [x] **F1.** dashes.adoc:3 prescribes an en dash for a negative number, but the typographically correct character is U+2212 MINUS SIGN, and an en dash is only a common substitute. The example "a range of -5 to 5" uses neither. It is an ASCII hyphen-minus (U+002D), so the example breaks the rule it illustrates. The clause "where a hyphen could be misread as a minus sign" is also muddled for a negative number, where the minus sign is the intended reading. Done. dashes.adoc now prescribes an en dash for ranges and a minus sign (U+2212) for negative numbers, and the example uses the real minus sign.

- [x] **F2.** gerunds.adoc:5 says "A gerund takes a possessive adjective when it is the true subject of the clause". "Priya's" is a possessive noun, not a possessive adjective, and in the example the gerund "explaining" is the object of "appreciated", not the subject. The traditional guidance is to use the possessive when the action, not the actor, is the focus. Reword, and cite a published grammar for it. Done. Corrected to "noun or pronoun that modifies a gerund ... possessive case", and the "-ing" wording (P8) was fixed in the same file. No published grammar is cited, because I did not verify one against a primary source, so add one if you want the rule sourced.

- [x] **F3.** collective-nouns.adoc:3 names "data" as a collective noun. It is a mass (non-count) noun in technical usage, historically the Latin plural of "datum". It is not a noun for a group of members. Move the "data" guidance under its own heading, or reword it as a mass-noun note. Done. "data" is now described as a mass noun, and dropped from the collective-noun list. I also cut "some style guides still require the Latin plural", which was an unnamed authority (attributions.adoc:3).

- [x] **F4.** a-an.adoc:3 says "Use "an" before a vowel sound, not before a written vowel". Read literally, this forbids "an" before any written vowel ("an apple"). The intended rule is "Choose "a" or "an" by the sound that follows, not the letter". Done. a-an.adoc now reads "Choose "a" or "an" by the sound that follows, not by the letter."

- [x] **F5.** citations.adoc:41 cites "DeLorne and Fedler (2003). _Journalists' Hostility Toward Public Relations: An Historical Perspective_". Crossref (DOI 10.1016/S0363-8111(03)00019-5) gives the authors as Denise E. DeLorme and Fred Fedler, and the title as "Journalists' hostility toward public relations: an historical analysis". Fix to "DeLorme" and "An Historical Analysis". Done. Now "DeLorme and Fedler (2003)" and "An Historical Analysis", per Crossref (DOI 10.1016/S0363-8111(03)00019-5). ScienceDirect returned 403, so Crossref was the source.

- [x] **F6.** citations.adoc:45 cites "Cision (2016). _Inside PR 2026_". The year and title disagree, and the URL slug is `2026-inside-pr-report`. The year is probably 2026. Not verified against the source. The preceding sentence (:43) also introduces it as "a company's annual report" straight after listing press releases, news stories, and blog posts, so the example does not match its lead-in. Done, differently from how it was written. The page for the Cision report gives no date, so per the rule in the same file the year is omitted rather than guessed. The entry now uses the full title, and the lead-in says "industry report" and explains the omission.

- [x] **F7.** citations.adoc:39 "including the https:// schema". The URI component is the scheme (RFC 3986 §3.1), not "schema". Done. "schema" is now "scheme".

- [x] **F8.** 99-references.adoc:7 titles the Google source "Google Developer Documentation Style Guide: In-page style guide". The linked page (google.github.io/styleguide/docguide/style.html) is titled "Markdown style guide". The Google developer documentation style guide is a different publication at developers.google.com/style. Verified by fetch. Retitle the entry, or relink it if the developer guide was the intended source. Done. Retitled to "Markdown style guide", the title of the linked page, verified by fetch. The link attribute name `link-google-docguide-capitalization` still says "docguide", which is the URL path segment, so it is accurate and left alone.

- [x] **F9.** 99-references.adoc:15 renders the Wikipedia page title as "Signs of AI Writing". The published title is "Wikipedia:Signs of AI writing", in sentence case (verified by fetch), while :17 keeps "List of style guides" in its published sentence case. titles-of-works.adoc:5 and :9 allow one treatment or the other, not both. Pick one and apply it to both entries. Done. Both Wikipedia titles now appear as published, in sentence case, under the "as published" exception in titles-of-works.adoc:9.

## 3. Structural problems

- [ ] **S1.** citations.adoc:51-62, repository-specific mechanics in a format-agnostic standard. Resolve with D3. Not worked. It waits on D3, which needs your approval because the recommended fix edits docs/style-guide.md.

- [x] **S2.** citations.adoc:1 and 99-references.adoc:1 are both headed "References", so the rendered page has two sections with the same title, one a topic and one the bibliography. Rename the topic to "Citations" (file `citations.adoc`, moving it in the alphabetical include order), which also describes it better. Done. `git mv references.adoc citations.adoc`, retitled "Citations", and moved to its alphabetical place in the include list in pages/026.adoc. The 99-references.adoc partial keeps the title "References". All partials are included exactly once, in order.

- [x] **S3.** code-blocks.adoc:44-49 repeats placeholders.adoc:3-8 verbatim, including the example. The code-blocks copy adds only "Adopt sensible variations…", which placeholders.adoc:12 already states precisely. Cut the code-blocks copy and cross-reference Placeholders. Done. code-blocks.adoc now ends with "For the conventions on placeholders in code blocks, see Placeholders." The duplicated paragraph and example are gone. placeholders.adoc:12 already carries the "vary this rule" exception, so nothing was lost.

- [x] **S4.** abbreviations.adoc:13 restates a-an.adoc:3 (article by pronunciation), and abbreviations.adoc:11 restates apostrophes.adoc:5 with identical examples ("three APIs", "two CDNs"). Keep each rule in one topic and cross-reference it from the other. Done. Each rule now lives in one place. Apostrophes holds the plural of an abbreviation, and I moved the "lowercase s" wording there so nothing was lost. "a", "an" holds the article rule. Abbreviations cross-references both.

- [x] **S5.** dashes.adoc:3 and numbers.adoc:7 both state the numeric-range rule, and have drifted. numbers.adoc adds "no surrounding spaces", which dashes.adoc lacks. Keep one statement, in Dashes, and cross-reference it. Done. Dashes holds the range rule, with "no surrounding spaces" moved there from Numbers, and Numbers now says "For a numeric range, see Dashes."

- [x] **S6.** headings.adoc:7 restates titles-of-works.adoc:7 (title case for cited works as an exception to sentence case). Cut headings.adoc:7 down to a cross-reference. Done. headings.adoc now says a cited work "follows a different rule" and points at Titles of works.

- [x] **S7.** "Technical documentation states facts / does not sell" is said four times: tone.adoc:3, language.adoc:11, exclamation-marks.adoc:3, and significance-claims.adoc:3. The word lists are split between language.adoc:11 (marketing words) and terminology.adoc:11-13 (weighty words), and overlap (C6). tone.adoc is a one-paragraph stub, while the substance is scattered. Make Tone the home of the register rule and the word lists, and point the others at it. Done. Tone now holds the register rule, the marketing-word list with its Bad/Good pair, and the weighty-word list, moved verbatim from language.adoc and terminology.adoc, minus the duplicated "states facts, does not sell" sentence. Language, Terminology, and Exclamation marks now point at Tone. The stray "— , eg." moved with the text, so it is now at tone.adoc, and the Tier 4 dash and colon items that cited language.adoc:11 apply there.

- [x] **S8.** sentences-and-paragraphs.adoc:3-8 restates the clause-joining rules of colons.adoc:5 and semicolons.adoc:3-5, and has drifted from them (C2). Keep the rule in Sentences and paragraphs, and reduce the colon and semicolon entries to what is specific to each mark. Done. semicolons.adoc now points at the exception in Sentences and paragraphs instead of restating it. colons.adoc already points there since Tier 1. Each topic keeps its own Bad/Good example.

- [x] **S9.** colons.adoc:15-17 repeats the example at :9-11 verbatim. Cut the repetition, or replace it with an example that shows the lowercase-after-colon rule it follows. Done. Cut the duplicated example. The first example, after the list of permitted uses, still demonstrates the lowercase-after-colon rule.

## 4. Coverage gaps

- [x] **G1.** No rule states which variety of English to use. TS-26 writes "organized", "behavior", "colorful", and "labeled" (American) but also "full stop" (British) at lists.adoc:7 and semicolons.adoc:3. Resolve with D9, and place it in a new `spelling.adoc` topic or in language.adoc. Done, with D9. language.adoc now requires American English, with one variety per document and original spelling kept in quotations and names. I added it to Language, not a new topic. The "full stop" instances remain Tier 4 terminology items.

- [x] **G2.** No rule covers words cited as words, or suffixes. TS-26 puts cited words in double quotes ("very", "an") but sets some fragments in monospace (`-ly` at hyphenation.adoc:7, `'s` at apostrophes.adoc:3). It writes one suffix three ways, "ing" (gerunds.adoc:3), "-ing" in quotes (trailing-participial-clauses.adoc:3), and `-ly` in monospace. quotation-marks.adoc:3 covers only "quoted prose". Recommend quotes for words as words, including suffixes, and place the rule in quotation-marks.adoc. Done. quotation-marks.adoc now sets words and suffixes mentioned as words in double quotes, and reserves monospace for typed or output text. gerunds.adoc already follows it after the Tier 1 fix. The rest of the inconsistent suffixes are a new Tier 4 item below.

- [x] **G3.** No rule covers how to present good and bad examples, and TS-26 uses four conventions (D2). Place the chosen convention in figures-tables-and-examples.adoc, which also has an open `// TODO` at :3. Done, with D2. figures-tables-and-examples.adoc now states the ✅ / ❌ convention with a worked pair, and the open `// TODO` there is resolved and removed. Converting the existing examples is still a Tier 4 item.

- [x] **G4.** lists.adoc:7 says when to punctuate items as sentences, but not what to do when no item is a full sentence. The example at :19-27 implies "no terminal period", but TS-26 itself ends fragment items with periods at admonitions.adoc:9-17 and citations.adoc:5-6. State the rule for fragments. Done. lists.adoc now says to capitalize the first word of a fragment item and omit its period.

- [x] **G5.** citations.adoc:60 orders entries alphabetically by author or organization, but does not say how to treat a leading article. 99-references.adoc:13 sorts "The Economist" under T. State the rule. Library convention ignores a leading article. Done. citations.adoc now says to ignore a leading article. I also reordered 99-references.adoc to follow the rule, which also settles the two Wikipedia entries (title order), so that Tier 4 ordering item is done too.

- [x] **G6.** No guidance on gendered pronouns for unspecified people. The only examples (quotation-marks.adoc:21-22) use "She said" and "he replied". inclusive-language.adoc is the natural home for singular "they". Done. inclusive-language.adoc now covers singular "they", using a person's own pronouns, and not inferring pronouns from a name.

- [x] **G7.** requirements-levels.adoc does not mention RFC 8174, which clarifies that the keywords carry their RFC 2119 meaning only when written in capitals. :5 and :13 already gesture at this ("written in their full uppercase forms"). Citing BCP 14 (RFC 2119 and RFC 8174) would ground it. Done, and verified against the RFC (it updates RFC 2119, both form BCP 14, and only capitals carry the special meaning). requirements-levels.adoc cites RFC 8174, and I declared both RFC links as attributes in 00-attributes.adoc, which also clears the requirements-levels.adoc half of the Tier 4 inline-URL item.

- [x] **G8.** language.adoc:5 carries an open `// TODO: Add Oscar Wilde quote.`, and language.adoc:3 ("Use plain language.") is a bare instruction with no rationale. Done, in part. language.adoc:3 now has a rationale. You have since replaced the `// TODO` with a sidebar quoting George Orwell's six rules from "Politics and the English Language" (1946), and I checked that the summary matches those rules.

## 5. Convention conformance

Items where TS-26's own prose breaks a TS-26 rule, the repository style guide, or TS-28. Items that depend on a decision name it.

- [x] colons.adoc:3 (no colon before a list or code block). A colon introduces a list block at admonitions.adoc:7 and citations.adoc:3, and a code block at citations.adoc:16 and :53. These stand whatever D1 decides. Done. The lead-ins to the lists and code blocks in admonitions.adoc and citations.adoc now end in a period ("are as follows.").

- [x] colons.adoc:7 (D1). A colon introduces a free-standing example paragraph at citations.adoc:10, :23, :27, :39, and :43, and a clause or quoted example at titles-of-works.adoc:3 (twice), titles-of-works.adoc:5, dangling-participles.adoc:3 ("Write:"), placeholders.adoc:10, citations.adoc:31, citations.adoc:35, and dashes.adoc:7 ("avoid:", "Prefer:", "Or:"). Done. Every clause-ending colon in TS-26 was rewritten, or replaced with an "Example:" label or a ✅ / ❌ block, in citations, titles-of-works, dangling-participles, placeholders, hyphenation, and dashes. I then reviewed every remaining colon in prose by eye. All are labels, inline lists ending a sentence, or part of a cited title.

- [x] admonitions.adoc:9-17 bold lead-ins end in a colon (`*NOTE*:`). TS-28 17-lists.adoc:221 says a lead-in term "is terminated by a full-stop, rather than by a colon". The same list also uses `-` markers, which TS-28 17-lists.adoc:207 says SHOULD NOT be used in AsciiDoc. Done. The admonition types are now `* *NOTE.* …` with the `*` marker and a full stop after the bold term.

- [x] quotation-marks.adoc:7 (punctuation outside the quote). dangling-participles.adoc:3 puts the periods of both suggested rewrites inside the quotes. titles-of-works.adoc:3 ends "'Falsehoods Programmers Believe About Time.'" with the sentence's period inside the nested quote. Done. dangling-participles.adoc and titles-of-works.adoc now comply. I also converted the other quoted full sentences that ended in a period inside the quote (gerunds, emphasis, sentences-and-paragraphs) to ✅ / ❌ lines, and moved the period outside the quote in subjunctive-mood.adoc and standards.adoc. The periods left inside quotes belong to the quoted text, as in "eg.", "et al.", and "A.P.I.".

- [x] dashes.adoc:3 (en dash for ranges). citations.adoc:41 writes "pages 99-124" with a hyphen. Done. "pages 99–124" now uses an en dash.

- [x] dashes.adoc:5 (em dash for a parenthetical). inclusive-language.adoc:3 sets off "– for example, …" with a spaced en dash. Done. inclusive-language.adoc:3 now says "Examples:" with the terms written as separate quoted words, so no dash is needed.

- [x] dashes.adoc:7 (use em dashes sparingly). titles-of-works.adoc:3 has four em dashes in one paragraph, headings.adoc:3 three, and citations.adoc:62 three. Rewrite the asides with commas or parentheses. language.adoc:11 has a stray "— , eg.". Done. The dash-heavy sentences in titles-of-works, headings, and citations now use parentheses, commas, and full stops. I also removed the single dashes in that-and-which.adoc, figures-tables-and-examples.adoc, and apostrophes.adoc, and the stray "— , eg." in tone.adoc. The em-dash pairs left (active-voice, contractions, numbers, requirements-levels, quotation-marks, figures :5) are one parenthetical each.

- [x] units-of-measure.adoc:3 (space between numeral and unit). trailing-participial-clauses.adoc:9 writes "a 200ms backoff" in its good example. Should be "200 ms". Done. The good example now reads "200 ms".

- [x] numbers.adoc:3 and :5 (spell out zero to nine, "the third retry"). numbers.adoc:9 gives "`3 retries`" as an example of numerals with a unit. "Retries" is not a unit. Replace it with a real unit, eg. "`3 s`". Done. "`3 retries`" became "3 s", since "retries" is not a unit. "Figures" for numerals became "numerals" in numbers.adoc.

- [x] monospace.adoc:3 (monospace for what a reader types or a system outputs). Prose examples are set in monospace at numbers.adoc:7, numbers.adoc:9, units-of-measure.adoc:3, and abbreviations.adoc:7, while the same kind of example is in quotes at hyphenation.adoc:9 ("32 MB") and dashes.adoc:3 ("pages 12–20"). Use quotes for prose examples. Done. The prose examples in numbers, units-of-measure, and abbreviations are now in double quotes. I kept monospace for the ISO date and time formats in dates-and-times.adoc, because they are literal strings a reader would write.

- [x] emphasis.adoc:7 (no bold for emphasis). active-voice.adoc:3 bolds "*active voice*", which is not being defined. Done. The bold on "active voice" is removed.

- [x] emphasis.adoc:5 (bold a new term at its point of definition). Terms defined but not bolded: "admonition" (admonitions.adoc:3), "gerund" (gerunds.adoc:3), "dangling participle" (dangling-participles.adoc:3). Done. "admonition", "gerund", and "dangling participle" are bold at their definitions.

- [x] emphasis.adoc:3 (bold UI elements). instructional-steps.adoc:3 writes "select Save" and "click the Save button" without bold on "Save". Done. "*Save*" is bold in both quoted examples.

- [x] active-voice.adoc:3 (prefer active voice). The good examples at semicolons.adoc:14 and sentences-and-paragraphs.adoc:5 ("The cache is invalidated on write") and the recommended rewrite at dangling-participles.adoc:3 ("After the server was configured") are passive. Rewrite them in active voice, eg. "A write invalidates the cache.", so the examples do not model the construction another topic discourages. Done. The examples now read "A write invalidates the cache." Commas.adoc:8 and the dangling-participle rewrites are active too.

- [x] grammatical-person.adoc and tone.adoc. citations.adoc:8, :10, :16, :27, and :31 are in the first person singular ("My preference", "I will use", "I use", "I write", "I will truncate"), the only first-person passages in TS-26. Rewrite as imperatives. dangling-participles.adoc:3 models "we sent the request". Prefer "you" per grammatical-person.adoc:3. Done. The citations topic is rewritten as imperatives ("Prefer", "use", "write"). The "we sent the request" example is gone with the dangling-participle rewrite.

- [x] tense.adoc:3 (present tense for current behavior). code-blocks.adoc:7 "some rendering systems will provide functionality", and citations.adoc:10 and :31 "I will use", "I will truncate". Done. code-blocks.adoc:7 is rewritten in the present tense ("Many rendering systems let readers…"), and the "I will" forms are gone.

- [x] trailing-participial-clauses.adoc:3. code-blocks.adoc:7 ends "…invalidates the commands, making for a poor user experience", and sentences-and-paragraphs.adoc:16 ends "…for pace or emphasis, landing a short point after a longer sentence has built up to it". Both restate the sentence in vaguer terms. Cut them. Done. Both trailing clauses are cut.

- [x] filler-words.adoc:3. "very short" (commas.adoc:5), "not just" (headings.adoc:5, subjunctive-mood.adoc:3), "actually" (headings.adoc:13), and "a number of" (citations.adoc:3). Done. "very short" became "short", "not just" became "as well as" or "not only", "actually" is gone, and "a number of" became "several".

- [x] attributions.adoc:3 (no unnamed authorities). collective-nouns.adoc:5 "some style guides still require", code-blocks.adoc:7 "as is common in many technical documents", and citations.adoc:39 "it is common practice". Name the source or state the claim directly. Done. code-blocks.adoc:7 is cut, and citations now tells the reader to include the issue number and page range instead of asserting that it is "common practice".

- [x] commas.adoc:5 (comma after an introductory phrase of more than three words). citations.adoc:43 "However, as a general rule it is preferable" and headings.adoc:13 "as deeply as the content actually warrants up to a maximum". Done. citations.adoc now reads "As a general rule, cite…", and headings.adoc:13 is rewritten.

- [x] figures-tables-and-examples.adoc:5 (no positional references). citations.adoc:14 "(see below)" and citations.adoc:62 "the press-release and news-story guidance above". See D6 for "the following". Done. "(see below)" and "above" are removed from citations. "The following" stays, per D6.

- [x] placeholders.adoc:3 and :10 (angle brackets for placeholders in prose too). citations.adoc:53 writes `partials/NNN/99-references.adoc`. Should be `partials/<NNN>/99-references.adoc`, or moot under D3. Done. It is now `partials/<NNN>/99-references.adoc`. "Command-line argument" is hyphenated, and "prefer to use" became "use".

- [x] hyphenation.adoc:5 (no hyphen after the noun). headings.adoc:13 "a maximum of level-4" and "in level-1". Should be "level 4" and "level 1". hyphenation.adoc:3 (hyphenate a compound modifier before its noun). code-blocks.adoc:44 and placeholders.adoc:3 "command line argument". Should be "command-line argument". Done. The headings.adoc text now says "level 4" and "level 1", and "command-line" is hyphenated.

- [x] terminology.adoc:3 (one term per concept). "full stop" (lists.adoc:7, semicolons.adoc:3) against "period" everywhere else. "exclamation points" (quotation-marks.adoc:7) against the topic title "Exclamation marks". "screenreaders" (instructional-steps.adoc:3) against "screen readers" (links.adoc:3). "figures" for numerals (numbers.adoc:5), where "figure" elsewhere means a diagram. "section headings" (headings.adoc:5) against "subsection headings" (headings.adoc:7) for the same thing. Done. "Full stop" became "period" in lists, semicolons, and emphasis. "Exclamation points" became "exclamation marks", "screenreaders" became "screen readers", "figures" became "numerals", and "subsection headings" became "section headings".

- [x] requirements-levels.adoc:3 and :7 (RFC 2119 keywords in capitals, not softer phrasing). Normative lowercase "should" at lists.adoc:5, terminology.adoc:5, citations.adoc:39, and citations.adoc:43. Normative lowercase "may" at emphasis.adoc:9, eg-and-ie.adoc:5, and citations.adoc:39. Hedged "prefer to" at code-blocks.adoc:44, placeholders.adoc:3, and standards.adoc:3. Use the capitalized keyword or a plain imperative. Descriptive "may" (language.adoc:7, terminology.adoc:5, instructional-steps.adoc:3) is fine. Done. Lowercase normative words became SHOULD in lists.adoc, SHOULD NOT in terminology.adoc, MAY and SHOULD in citations.adoc, and MAY in eg-and-ie.adoc. "Prefer to" was dropped in placeholders.adoc and standards.adoc. I also reworded descriptive "must" in admonitions, emphasis, and dates-and-times. Lowercase keywords inside quoted examples are deliberate and were left.

- [x] standards.adoc:3 (cite a standard with its version). dates-and-times.adoc:3 cites "ISO 8601" without its edition (ISO 8601-1:2019). Done. dates-and-times.adoc now cites "ISO 8601-1:2019", confirmed as Part 1 of the current edition (the ISO site returned 403, so Wikipedia was the source).

- [x] links.adoc:3 and docs/style-guide.md:26. 01-introduction.adoc:5 and :7 link as `xref:025.adoc[TS-25]`. The style guide requires `xref:NNN.adoc[*TS-N: Title*]`, and "TS-25" alone does not describe the destination. admonitions.adoc:19 already uses the correct form. Done. The introduction now uses `xref:025.adoc[*TS-25: Technical Documentation*]`, and the same form for TS-27 and TS-28.

- [x] TS-28 14-links.adoc:51 (every external URL declared as a `:link-*:` attribute). requirements-levels.adoc:9 and placeholders.adoc:12 inline raw `https://…[…]` macros. Declare them in 00-attributes.adoc. The requirements-levels.adoc link is now an attribute (Tier 3, G7). Only the RFC 6570 link in placeholders.adoc remains. Done. RFC 6570 is now the attribute `link-ietf-rfc6570`. The other inline URL was done in Tier 3.

- [x] citations.adoc:60 (same-author entries ordered by title). 99-references.adoc:15-17 lists "Signs of AI Writing" before "List of style guides". Done in Tier 3 (G5).

- [x] citations.adoc:62 (omit any annotation). 99-references.adoc:11 carries "(community fork)". 99-references.adoc:3 gives the author as "A List Apart / Aimee Gonzalez-Santos", a form the entry format does not define. Partly done. "(community fork)" is removed. The A List Apart entry is your own edit, so I left it. It now carries the publisher ("A List Apart.") at the end, which contradicts the rule in citations.adoc ("Omit the publisher"). Resolved: you chose to change the rule. citations.adoc now allows an optional publisher after the linked title, with the A List Apart entry as the worked example, and 99-references.adoc is unchanged. I only reordered the entry, because sorting by surname puts Gonzalez-Santos before Google.

- [x] citations.adoc:37 and titles-of-works.adoc:5 (titles in title case). citations.adoc:29's own template entry is "_Title of the work_". See also F8 and F9. Done. The template entry is now "Title of the Work". The Wikipedia titles are handled under the "as published" exception (Tier 1).

- [x] citations.adoc internal consistency. :25 writes "Johnson, M" and :35 writes "Johnson, M.". :31 writes "et al" without a period, while eg-and-ie.adoc:3 keeps the period on Latin abbreviations. Done. "Johnson, M." is consistent, and "et al" is now "et al.".

- [x] code-blocks.adoc:3 (code blocks SHOULD specify their language). The CLI-output example at code-blocks.adoc:18 has no language. TS-28 07-code-blocks.adoc:187 says a block with prompts uses `console`. Its lines 27 (87 characters) and 30 (84) also break the "narrow enough to avoid horizontal scrolling" rule at code-blocks.adoc:5 that sits above them. Done. The CLI-output example is now `[source,console]`, and I truncated the two over-long Heroku lines to fit the width, by dropping the "(such as …)" parentheticals.

- [x] abbreviations.adoc:3 (spell out on first use). "IETF" (requirements-levels.adoc:3), "WCAG" (standards.adoc:3), "APA" and "MLA" (citations.adoc:3), "FAQ" (question-marks.adoc:3), and "PR" (apostrophes.adoc:3, where it means "pull request"). Judgment call against the "so common to the audience" exception at :5. IETF and WCAG are the likeliest to need it. Not changed, deliberately. IETF is now spelled out at its first use in requirements-levels.adoc. WCAG, APA, MLA, FAQ, and PR are left under the "so common to the audience" exception, and you decided to leave them.

- [x] lists.adoc:7 (punctuate as sentences only when an item is a sentence) and TS-28 17-lists.adoc:260 (blank line between numbered items). citations.adoc:5-6 are fragments ending in periods, with no blank line between them. Done. The two numbered-list items in citations.adoc are now fragments without periods, with a blank line between them.

- [x] standards.adoc:3 has no terminal period. Done. standards.adoc now ends in a period.

- [x] quotation-marks.adoc (words as words, added in Tier 3, G2). hyphenation.adoc:7 sets `-ly` in monospace, and apostrophes.adoc:3 and :7 set `'s` and `s` in monospace. Set each mentioned suffix in double quotes, keeping monospace only where the text is literal syntax. trailing-participial-clauses.adoc:3 already quotes "-ing", and gerunds.adoc:3 was fixed in Tier 1. Done. hyphenation.adoc and apostrophes.adoc now quote the suffixes ("-ly", "'s", "s").

## 6. Prose defects

- [x] **P1.** admonitions.adoc:3 "a labeled box or panel panel" → "a labeled box or panel" Done in Tier 1.

- [x] **P2.** code-blocks.adoc:5 "Try to keep code examples narrow enough avoid horizontal scrolling" → "Keep code examples narrow enough to avoid horizontal scrolling". This drops the hedge and adds the missing "to". Done. "Keep code examples narrow enough to avoid horizontal scrolling…"

- [x] **P3.** instructional-steps.adoc:3 "a fixed visual layout that a may not be applicable to all UI views" → "a fixed visual layout that not every view shares" Done. "…a fixed visual layout, which does not hold in every view (eg. screen readers, mobile views)."

- [x] **P4.** headings.adoc:13 "Nest headings only as deeply as the content actually warrants up to a maximum of level-4 (where the document title in level-1)." → "Nest headings no deeper than level 4, where the document title is level 1." Done. "Nest headings no deeper than level 4, where the document title is level 1."

- [x] **P5.** headings.adoc:15 "inline formatting on top of that can confuse rendering issues in some cases" → "inline formatting on top of that can cause rendering errors" Done. "…can cause rendering errors."

- [x] **P6.** numbers.adoc:5 "Exaples" → "Examples" Done.

- [x] **P7.** subjunctive-mood.adoc:3 "wished- for" → "wished-for" Done.

- [x] **P8.** gerunds.adoc:3 "a verb form ending "ing"" → "a verb form ending in "-ing"" (see G2) Done in Tier 1.

- [x] **P9.** dashes.adoc:5 "surrounded on each side by a single empty space" → "with a space on each side" Done. "…with a space on each side…"

- [x] **P10.** requirements-levels.adoc:5 "Do not use the mixed-case spelling, eg. "Must", "should not"" says mixed case, but "should not" is lowercase. → "Do not write a keyword in lowercase or mixed case, eg. "should not", "Must"." Done. "Do not write a keyword in lowercase or mixed case, eg. "should not" or "Must"."

- [x] **P11.** sentences-and-paragraphs.adoc:3 "with a hyphen, colon, or semicolon" → "with a dash, colon, or semicolon". dashes.adoc:3 draws the hyphen/dash distinction, and this sentence ignores it. Done in Tier 1 (sentences-and-paragraphs.adoc now says "dash").

- [x] **P12.** standards.adoc:3 ""WCAG 2.2 Level AA", not "accessible"" contrasts a standard with a vague adjective, which does not show the version rule. → ""WCAG 2.2 Level AA", not "WCAG"". :5 "A standard named without a version is not a testable threshold" is also too broad, since an RFC is immutable and needs no version. Done. Now "WCAG 2.2 Level AA", not "WCAG", and "TLS 1.3", not "TLS". I also gave the second sentence its reason (requirements change between versions), because "not a testable threshold" was too broad.

- [x] **P13.** question-marks.adoc:5 labels a prohibited rhetorical question "Example:" without saying it is the thing to avoid. Resolve with D2 (❌). Done. It is now a ✅ / ❌ pair.

- [x] **P14.** lists.adoc:29-38 says to avoid nesting more than two levels, then shows a two-level list with no indication whether it is the good or the bad case. The example does not show the rule. Show a three-level list restructured into subsections, or cut the example. Done. The nesting example is now a ✅ two-level list against a ❌ three-level one.

- [x] **P15.** code-blocks.adoc:44 "Adopt sensible variations where these characters have special meaning" is unfalsifiable. Moot if S3 cuts it, since placeholders.adoc:12 states the concrete rule. Done by S3 (Tier 2). The sentence is gone.

- [x] **P16.** "genuine" and "genuinely" appear six times as intensifiers (emphasis.adoc:9, foreign-words.adoc:7, grammatical-person.adoc:7, question-marks.adoc:3, requirements-levels.adoc:3, sentences-and-paragraphs.adoc:8). They serve the same function as the words filler-words.adoc:3 bans. Cut most of them. Done. I removed "genuine" and "genuinely" in all six places.

- [x] **P17.** citations.adoc:43-49 draws its examples from the public-relations trade (Cision, PR Week, a PR journal at :41). They are off-domain for a technical writing standard. Replace them with technical sources, eg. a vendor engineering blog post. Done. The PR Week and Cision examples are replaced with a blog post (Cognitect, Michael Nygard, 2011) and a standards document (RFC 9110, IETF, 2022), both verified by fetch. I kept the DeLorme and Fedler journal example, which is verified and is there to show the journal format.

- [x] **P18.** abbreviations.adoc:15 "not "the JSON is a text format"" is a strawman that no writer produces. The distinction worth drawing is "JSON is a text format" against "the JSON payload", where "the" belongs to "payload". Done. The example now states the distinction: "The JSON payload" is correct, because "payload" is the noun.

- [x] **P19.** code-blocks.adoc:7 is a 495-character paragraph that gives four separate reasons against `$` prompts, and hedges ("It can also be confusing…", "some rendering systems"). Cut it to the copy-paste reason, which is the one that decides the rule. Done. It is cut to the one reason that decides the rule, the copy-and-paste one.
