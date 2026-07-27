# TS-1 review and remediation plan

Findings from a deep review of TS-1: Software Requirements Specification
(~1,550 lines across 13 files), assessed against the repository
[style guide](../../docs/style-guide.md),
[TS-26: Technical Writing Style Guide](../026/README.adoc), the
[template](../../template/), and sibling standards.

**Assessment.** Structurally sound and unusually well-argued for a requirements
standard — the context/requirements split, the two-artifact model, and the
proposal state machine are the strongest parts. But there are seven outright
contradictions, several factual errors in the Gherkin material, significant
duplication across §01a/§07/§10, and the compact `AGENTS.md` has drifted from
the standard it summarizes, including one rule it invents outright.

**Status:** tier 1 (correctness) applied — see
[Changelog](#changelog). Tiers 2-4 are open.

---

## Priority order

1. ~~**Correctness**~~ — **done.**
   [1.1](#11-privilege-inheritance-direction--stated-both-ways),
   [1.2](#12-spec-merge-timing--three-mutually-incompatible-rules),
   [2.1](#21-scenario-outline-expansion-uses-the-wrong-keyword),
   [2.2](#22-gherkin-uses-indentation-to-define-structure-is-wrong),
   [1.5](#15-the-when-examples-model-the-anti-pattern-the-standard-forbids),
   [§7](#7-agentsmd-has-drifted-from-the-standard) (invented big-design-up-front
   rule + typos).
   [2.3](#23-both-templates-misalign-step-indentation) was pulled forward from
   tier 2 — see the changelog note.

2. **Coherence** — [1.3](#13-qualities-must-measurable-vs-acknowledged-subjective-nfrs),
   [1.4](#14-feature-file-scope-must-vs-should-different-rules),
   [1.6](#16-success-metrics-assigned-to-both-artifacts),
   [1.7](#17-state-machine-has-no-rework-or-abandonment-path),
   [4.1](#41-10-has-become-a-catch-all),
   [4.2](#42-the-version-control-argument-is-made-twice-at-length),
   [4.4](#44-the-directory-tree-is-reproduced-three-times-and-has-already-drifted),
   terminology collisions on "features" and "journey".

3. **Completeness** — [5.1](#5-genuine-coverage-gaps) (identifier scheme —
   unblocks three existing rules),
   [2.4](#24-missing-core-gherkin-constructs),
   [2.5](#25-feature-files-have-no-stated-home),
   [4.6](#46-9s-ordering-contradicts-its-own-stated-pipeline)/[4.7](#47-coverage-imbalance).

4. **Conventions** — the [`99-references.adoc` decision](#6-convention-conformance),
   quote and dash normalization, bold lead-in forms, README related-standard
   links, `01a-` naming.

---

## 1. Contradictions

### 1.1 Privilege inheritance direction — stated both ways

- [x] Resolve the direction and state it once. **Done** — §06 corrected to
      "down" in both places, each now xref'ing `<<Actors>>` so §05 is the single
      authoritative statement.

[06-behaviors.adoc:47](./06-behaviors.adoc#L47) says privileges are inherited
**up** the actor hierarchy. Two other places say **down**:

- [05-context.adoc:91](./05-context.adoc#L91) — "Privileges are inherited down
  the hierarchy."
- [06-behaviors.adoc:117](./06-behaviors.adoc#L117) — "Since permissions are
  inherited down the actor hierarchy…"

Same file, contradicting itself 70 lines apart. Both conclusions ("specify
against the lowest-privileged actor") are identical, so it is the direction word
that is wrong — but a reader building an access matrix has to guess. Fix: state
it once in §05, and xref it from §06.

### 1.2 Spec-merge timing — three mutually incompatible rules

- [x] Pick one rule, state it once, delete the other two. **Done** — resolved
      in favor of **same change-set as the behavior change** (decision by
      Kieran, 2026-07-27). §01a states the rule; §10 "Binding the specification
      to production" is rewritten to match and now carries the batched-release
      caveat; §10's colocation paragraph xrefs it instead of restating it; the
      `Released` and `Accepted` state definitions were corrected to match.

| Location | Rule |
|---|---|
| [01a-persistence.adoc:10-12](./01a-persistence.adoc#L10-L12) | Spec change made **at the same time as** code is released |
| [10-proposal-lifecycle.adoc:93-94](./10-proposal-lifecycle.adoc#L93-L94) | Proposal MUST NOT be merged **until** code is released |
| [10-proposal-lifecycle.adoc:44-47](./10-proposal-lifecycle.adoc#L44-L47) | A PR that changes behavior "can be required to touch the specification **in the same commit**" |

These cannot all hold. If the spec edit ships in the same commit as the behavior
change, it is merged *before* release, not after. §10's own "making drift a
merge-time concern" argument directly undercuts §10's release gate two sections
earlier. This is the load-bearing rule of the whole standard and it is specified
three ways.

### 1.3 Qualities: MUST measurable vs. acknowledged subjective NFRs

- [ ] Reconcile §07 and §10 (resolved for free by [4.1](#41-10-has-become-a-catch-all)).

[10-proposal-lifecycle.adoc:216-217](./10-proposal-lifecycle.adoc#L216-L217)
— "Qualities **MUST** be specified as concrete, testable thresholds."

[07-qualities.adoc:43](./07-qualities.adoc#L43) uses **SHOULD**, and
[07-qualities.adoc:73-79](./07-qualities.adoc#L73-L79) explicitly carves out UX
as "entirely subjective, difficult to specify and measure in quantifiable
terms." §10's MUST forbids what §07 permits.

### 1.4 `.feature` file scope: MUST vs. SHOULD, different rules

- [ ] Choose one strength and one rule.

[08-executable-specifications.adoc:36](./08-executable-specifications.adoc#L36) —
"Each discrete feature **MUST** be described in a single plain text file."

[08-executable-specifications.adoc:95](./08-executable-specifications.adoc#L95) —
"A `.feature` file **SHOULD** describe a single feature… **or a particular
aspect of a feature.**"

Different strength *and* different content, 60 lines apart in one file.

### 1.5 The `When` examples model the anti-pattern the standard forbids

- [x] Replace the five UI/CLI step examples with business-language equivalents.
      **Done** — both the `When` block and the `Given` block above it (which had
      the same first-person problem) rewritten in third-person business
      register. Added a paragraph stating the underlying rule, xref'ing
      `<<Implementation>>`.

[08-executable-specifications.adoc:213-217](./08-executable-specifications.adoc#L213-L217):

```
When I am on "/some/page"
When I fill "username" with "admin"
When I press "login"
When I run "ls -la"
```

These are UI/CLI automation steps. They contradict:

- [03-acceptance-criteria.adoc:11-12](./03-acceptance-criteria.adoc#L11-L12) —
  ACs "SHOULD NOT include technical implementation details, or even make
  reference to software"
- [08-executable-specifications.adoc:229-230](./08-executable-specifications.adoc#L229-L230)
  — "Assertions about the system's internal state or implementation details
  SHOULD be avoided"
- [08-executable-specifications.adoc:328-334](./08-executable-specifications.adoc#L328-L334)
  — don't automate through the UI; go close to the business rule

The good examples elsewhere in the same file ("a customer returns a faulty
microwave") show exactly the right register. These five lines teach the
opposite. They also switch to first-person "I" with no stated convention, while
every other example uses third person.

### 1.6 Success metrics assigned to both artifacts

- [ ] Assign success metrics to one artifact only.

[01-scope.adoc:89](./01-scope.adoc#L89) lists "success metrics" under **PRD**
contents. The comparison table at [01-scope.adoc:136](./01-scope.adoc#L136)
lists "success metrics and KPIs" under **SRS** typical contents. Given the
section's entire purpose is to separate the two artifacts, this undermines it.

### 1.7 State machine has no rework or abandonment path

- [ ] Add `Proposed → Draft` (rework) and a terminal path from `Accepted`, or
      state explicitly why neither is permitted.

[10-proposal-lifecycle.adoc:170](./10-proposal-lifecycle.adoc#L170) — "A
proposal MUST NOT move backwards… and MUST NOT skip states."

But [10-proposal-lifecycle.adoc:176-182](./10-proposal-lifecycle.adoc#L176-L182)
mandates cross-functional review of a `PROPOSED` proposal to catch ambiguity.
When review sends it back for rework, the only legal moves are `Accepted` or
`Rejected` — no `Proposed → Draft`. Likewise, a proposal that is `Accepted` but
abandoned before release (priorities change, the feature is descoped) has no
terminal state; `Superseded` is reachable only from `Released`. The mermaid
diagram at [10-proposal-lifecycle.adoc:60-71](./10-proposal-lifecycle.adoc#L60-L71)
confirms both gaps.

---

## 2. Factual errors in the Gherkin material

### 2.1 Scenario outline expansion uses the wrong keyword

- [x] Change the two expanded blocks to `Scenario:`. **Done** — also clarified
      the lead-in sentence ("one per row of the `Examples` table… the following
      ordinary scenarios"). The outline definition itself correctly retains
      `Scenario Outline:`.

[08-executable-specifications.adoc:290-301](./08-executable-specifications.adoc#L290-L301)
shows what a scenario outline is "the equivalent of writing" — but writes both
expansions as `Scenario Outline:`. Expansion produces `Scenario:` blocks. As
written, the example is not valid Gherkin (a `Scenario Outline` without
`Examples` is an error in Cucumber), and it teaches the wrong mental model of
what expansion does.

### 2.2 "Gherkin uses indentation to define structure" is wrong

- [x] Rewrite the claim and drop the derived spaces-vs-tabs advice. **Done** —
      now states that structure comes from keywords, that parsers ignore leading
      whitespace outside doc strings, and that the two-space layout is a
      readability convention that SHOULD be followed.

[08-executable-specifications.adoc:37-41](./08-executable-specifications.adoc#L37-L41)
— "Like YAML, Gherkin is line-oriented and uses indentation to define structure…
Either spaces or tabs MAY be used for indentation, though spaces SHOULD be
preferred for portability."

Gherkin structure is determined by **keywords**, not indentation. Indentation is
purely cosmetic outside doc strings. The spaces-vs-tabs portability advice is
derived from a false premise — there is no portability hazard, because parsers
ignore the leading whitespace entirely.

### 2.3 Both templates misalign step indentation

- [x] Align `When`/`Then` with `Given` in both templates. **Done** — pulled
      forward from tier 2, because
      [2.2](#22-gherkin-uses-indentation-to-define-structure-is-wrong) now
      states the two-space convention normatively, which the misaligned
      templates would have contradicted on the same page.

[08-executable-specifications.adoc:61-66](./08-executable-specifications.adoc#L61-L66)
and [08-executable-specifications.adoc:150-154](./08-executable-specifications.adoc#L150-L154)
indent `When` and `Then` one space deeper than `Given`:

```
    Given {state or precondition}
     (And {state or precondition})
     When {event or action}
     Then {expected outcome}
```

The extra space belongs to the `(And …)` optional-marker convention but has bled
onto `When`/`Then`. Since [2.2](#22-gherkin-uses-indentation-to-define-structure-is-wrong)
(incorrectly) tells readers indentation is structural, a reader may take this
alignment as meaningful. The "Simple example" at
[08-executable-specifications.adoc:86-90](./08-executable-specifications.adoc#L86-L90)
gets it right — the templates should match.

### 2.4 Missing core Gherkin constructs

- [ ] Add `Rule:`, tags, doc strings, and step data tables — or state
      explicitly that they are out of the recommended baseline and why.

[08-executable-specifications.adoc:182-188](./08-executable-specifications.adoc#L182-L188)
lists the step keywords but omits `*` (the generic bullet step). More
significantly, the section never covers:

- **`Rule:`** — part of core Gherkin since v6 and supported by Cucumber. This is
  a notable omission given
  [06-behaviors.adoc:74-100](./06-behaviors.adoc#L74-L100) makes "Rules" a
  first-class section of the taxonomy. The standard tells you to keep rules in a
  separate central place with IDs (`R1`), while Gherkin has a native construct
  for binding scenarios to rules that goes unmentioned.
- **Tags (`@…`)** — the standard mechanism for slicing/filtering suites,
  directly relevant to §10's CI-enforcement rule.
- **Doc strings (`"""`) and step data tables** — routinely needed for realistic
  scenarios.

The section claims to define "the RECOMMENDED baseline syntax"
([08-executable-specifications.adoc:31](./08-executable-specifications.adoc#L31)),
so these omissions read as prohibitions rather than gaps.

### 2.5 `.feature` files have no stated home

- [ ] Link §08 to the taxonomy, and state how a scenario cross-references a rule
      ID.

[04-structure.adoc:24](./04-structure.adoc#L24) puts Gherkin scenarios in
`requirements/behaviors/features/`. §08 — 334 lines on Gherkin — never
references the taxonomy, never says where `.feature` files live, and never
explains how a scenario cross-references a rule ID. The two sections do not know
about each other.

---

## 3. Technical accuracy elsewhere

- [ ] [07-qualities.adoc:55](./07-qualities.adoc#L55) — "256-bit SSL/TLS
  encryption (for data in transit)". SSL has been deprecated for a decade
  (RFC 7568/8996), and "256-bit SSL/TLS" conflates cipher key length with
  protocol version. As a *conformance target*, which is what this paragraph is
  offering, it is not specifiable. Suggest "TLS 1.3 (or TLS 1.2 restricted to
  AEAD cipher suites)".

- [ ] [07-qualities.adoc:56](./07-qualities.adoc#L56) — "Web Content
  Accessibility Guidelines (for usability)". WCAG is an accessibility standard,
  not a usability one — and the very next section
  ([07-qualities.adoc:73-79](./07-qualities.adoc#L73-L79)) makes the point that
  usability/UX is the *subjective* quality that cannot be pinned to a published
  standard. Mislabeling WCAG as usability contradicts that argument.

- [ ] [07-qualities.adoc:57-58](./07-qualities.adoc#L57-L58) — "EU General Data
  Protection Regulations" — singular: *Regulation*.

- [ ] [02-responsibility.adoc:11-14](./02-responsibility.adoc#L11-L14) — the
  password-strength example prescribes minimum 8 characters, mandatory special
  character, and "no dictionary words". NIST SP 800-63B has recommended
  *against* composition rules and dictionary-word bans since 2017 (they
  measurably reduce entropy by pushing users to predictable substitutions), in
  favor of length minimums plus a breach-corpus check. It is only an
  illustration of "business requirement vs. technical design", but in a
  standards repository an illustration is read as endorsement, and a reader
  could lift it verbatim into a spec. Either swap it for current guidance or
  pick a domain-neutral example.

---

## 4. Structural problems

### 4.1 §10 has become a catch-all

**Renamed 2026-07-27** to `10-proposal-lifecycle.adoc` / "= Proposal lifecycle"
(decision by Kieran). The old title, "Managing requirements", was broad enough
to invite the drift catalogued here. The rename does not by itself fix the
misfiling — it sharpens it, since four sections now sit under a title that
plainly excludes them.

**Destination map — awaiting approval before any section is moved.**

| Section (current line) | Verdict | Destination |
|---|---|---|
| Two artifacts ([14](./10-proposal-lifecycle.adoc#L14)) | Stays | — |
| Version control as the substrate ([31](./10-proposal-lifecycle.adoc#L31)) | **Moves** | Merge into §01a Persistence — this is [4.2](#42-the-version-control-argument-is-made-twice-at-length) |
| Lifecycle states ([53](./10-proposal-lifecycle.adoc#L53)) | Stays | — |
| Binding the specification to production ([96](./10-proposal-lifecycle.adoc#L96)) | Stays | — |
| Recording decisions ([123](./10-proposal-lifecycle.adoc#L123)) | Stays | — |
| Atomic proposals and epics ([135](./10-proposal-lifecycle.adoc#L135)) | Stays | — |
| Separation of feedback from record ([147](./10-proposal-lifecycle.adoc#L147)) | Stays | — |
| Specify the end state, not a changelog ([158](./10-proposal-lifecycle.adoc#L158)) | Stays | — |
| Keep description and reasoning in their proper homes ([172](./10-proposal-lifecycle.adoc#L172)) | Stays | — |
| Enforce the state machine strictly ([183](./10-proposal-lifecycle.adoc#L183)) | Stays | — |
| Review proposals cross-functionally ([191](./10-proposal-lifecycle.adoc#L191)) | Stays | — |
| Record rejections as carefully as acceptances ([199](./10-proposal-lifecycle.adoc#L199)) | Stays | — |
| Write functional requirements as testable scenarios ([208](./10-proposal-lifecycle.adoc#L208)) | **Moves** | §06 Behaviors (Features) |
| State qualities as measurable thresholds ([229](./10-proposal-lifecycle.adoc#L229)) | **Moves** | §07 Qualities — resolves [1.3](#13-qualities-must-measurable-vs-acknowledged-subjective-nfrs) |
| Trace requirements to their implementation ([243](./10-proposal-lifecycle.adoc#L243)) | **Moves** | Consolidate with §01/§07 — this is [4.3](#43-traceability-stated-three-times) |
| Enforce specs in continuous integration ([254](./10-proposal-lifecycle.adoc#L254)) | Open | Neither proposals nor authoring; see note below |
| Definition of Ready ([262](./10-proposal-lifecycle.adoc#L262)) | **Moves** | A delivery gate — new file, or drop from TS-1 |

Two open questions for the extraction pass:

1. **"Enforce specs in continuous integration"** — it is about verification
   infrastructure, not the proposal lifecycle and not authoring. Candidates: a
   new short section of its own, folding into §08 (executable specifications),
   or folding into the traceability consolidation.

2. **"Definition of Ready"** — a delivery-process gate, not a property of the
   specification. It could become its own numbered section, move to a delivery
   standard outside TS-1, or be cut. Note the DoR is also summarized in
   [AGENTS.md](./AGENTS.md), which would need to follow whatever is decided.

Moving "State qualities as measurable thresholds" into §07 removes the
contradiction in
[1.3](#13-qualities-must-measurable-vs-acknowledged-subjective-nfrs) for free,
since it exists only because the rule is stated twice.

### 4.2 The version-control argument is made twice, at length

- [ ] Merge §01a and §10's version-control material into one section.

[01a-persistence.adoc](./01a-persistence.adoc) (82 lines) and
[10-proposal-lifecycle.adoc:27-47](./10-proposal-lifecycle.adoc#L27-L47)
both argue that specs belong in VCS alongside code, both list the benefits
(history, diffs, blame, low friction), and both state the bind-to-production
rule. §01a's "Requirements documents have a tendency to rot" opening and §10's
"A specification is only as valuable as it is trustworthy" opening are the same
thesis.

### 4.3 Traceability stated three times

- [ ] Consolidate to one location, xref'd from the others.

[01-scope.adoc:148-159](./01-scope.adoc#L148-L159) ("Executable tests"),
[07-qualities.adoc:107-116](./07-qualities.adoc#L107-L116) ("Verification"), and
[10-proposal-lifecycle.adoc:228-237](./10-proposal-lifecycle.adoc#L228-L237)
("Trace requirements to their implementation") all make the same two-way
cross-reference argument.

### 4.4 The directory tree is reproduced three times, and has already drifted

- [ ] Show the tree once in §04; xref it from §05 and §06.
- [ ] Add `proposals/` to the §04 taxonomy.

[04-structure.adoc:9-29](./04-structure.adoc#L9-L29),
[05-context.adoc:10-21](./05-context.adoc#L10-L21),
[06-behaviors.adoc:25-40](./06-behaviors.adoc#L25-L40). Divergences already
present:

- `features/` — "Gherkin scenarios" (§04) vs "Scenarios" (§06)
- `journeys/` — "Wireframes and/or call-sequences" (§04) vs "Wireframes or
  call-sequences" (§06)
- `access/` — "Permission matrix — which actors may exercise which capabilities"
  (§04) vs "Actor-permissions matrix" (§06)

Exactly the drift the standard warns about at
[06-behaviors.adoc:76-83](./06-behaviors.adoc#L76-L83).

Additionally, §04's tree omits `proposals/`, which
[01a-persistence.adoc:68](./01a-persistence.adoc#L68) shows and
[10-proposal-lifecycle.adoc:12-20](./10-proposal-lifecycle.adoc#L12-L20)
mandates as one of two required artifacts. §04 claims to be the taxonomy where
"every category of requirement has a single, unambiguous home" — the decision
log has no home in it.

### 4.5 Tree order ≠ section order

- [ ] Reorder the trees to match the prose in §05 and §06.

- **§05**: tree lists overview, constraints, glossary, model, actors; prose
  sections run Overview → Constraints → **Model → Actors → Glossary**.
- **§06**: tree lists access, rules, features, journeys, interfaces; the intro
  bullet list and the prose sections both run Features → Rules → Access →
  Interfaces → Journeys.

In both files the tree is the odd one out.

### 4.6 §09's ordering contradicts its own stated pipeline

- [ ] Reorder to use cases → event storming → story mapping → example mapping.

The section presents use cases → event storming → **example mapping** → **story
mapping**. But it also says:

- [09-requirements-elicitation.adoc:86-88](./09-requirements-elicitation.adoc#L86-L88)
  — example mapping is "the RECOMMENDED technique for the **final step** of
  requirements elicitation"
- [09-requirements-elicitation.adoc:130-133](./09-requirements-elicitation.adoc#L130-L133)
  — story mapping "sequenc[es] and prioritiz[es] the scope identified through
  use case analysis or event storming"

So the funnel is: use cases / event storming → story mapping → example mapping →
Gherkin. The last two sections are in the wrong order relative to the argument
the section makes about them.

### 4.7 Coverage imbalance

- [ ] **Use cases** get 8 lines
  ([09-requirements-elicitation.adoc:12-22](./09-requirements-elicitation.adoc#L12-L22))
  with no guidance on how to write one (actor, goal, preconditions, main success
  scenario, extensions) — versus 40 lines for event storming and 44 for story
  mapping, both of which get full procedural detail. A reader can run an
  event-storming workshop from this text; they cannot write a use case from it.

- [ ] **Impact mapping** is absent, despite being part of the project's own
  `discover` workflow.

- [ ] **NPS** gets ~30 lines
  ([07-qualities.adoc:81-105](./07-qualities.adoc#L81-L105)) explaining the
  survey question, the 0-10 bands, and the arithmetic. The style guide states
  the audience is experienced engineers and "foundational concepts do not need
  to be explained." One sentence plus a link would carry the same weight.

- [ ] **§08** is 334 lines — 21% of the standard — much of it explaining what
  `Given`/`When`/`Then` mean. Same audience-level concern; it reads as a Gherkin
  tutorial rather than a normative standard.

- [ ] **§02 Responsibility** (22 lines) says only "write in business language,
  collaborate with the customer, technical teams own it" — the first two of
  which §03 repeats at
  [03-acceptance-criteria.adoc:14-16](./03-acceptance-criteria.adoc#L14-L16).
  Only the ownership sentence is unique. Merge candidate.

---

## 5. Genuine coverage gaps

- [ ] **5.1 No requirement identifier scheme.** Rules get stable IDs (`R1`,
  `R2`) at [06-behaviors.adoc:83-84](./06-behaviors.adoc#L83-L84), but features,
  scenarios, and qualities get none. Yet
  [10-proposal-lifecycle.adoc:228-237](./10-proposal-lifecycle.adoc#L228-L237)
  requires each requirement to be linked to its component, test suite, and
  ticket, and [07-qualities.adoc:109-112](./07-qualities.adoc#L109-L112)
  requires two-way cross-referencing between qualities and their checks.
  Cross-reference *by what handle?* This is the missing mechanism under three
  separate rules.

- [ ] **5.2 `qualities/` has no internal structure.** §04 gives `behaviors/`
  five subdirectories and leaves `qualities/` flat, with no guidance on
  organizing NFRs (by attribute? by component? by SLA?). §07 does not fill the
  gap either.

- [ ] **5.3 Single-production-deployment assumption.** "The main line MUST
  describe the as-is production system"
  ([10-proposal-lifecycle.adoc:4-5](./10-proposal-lifecycle.adoc#L4-L5),
  [01-scope.adoc:5](./01-scope.adoc#L5)) is undefined for products with
  concurrently supported versions — on-prem installs, LTS branches, staged
  multi-region rollouts. Nothing addresses how the spec branches or is versioned
  in that case, and it is a common situation.

- [ ] **5.4 No prioritization guidance.** MoSCoW, weighted shortest job first,
  or any means of expressing relative importance of requirements.
  [09-requirements-elicitation.adoc:94-96](./09-requirements-elicitation.adoc#L94-L96)
  mentions stories "ordered by priority" without saying by what scheme.

- [ ] **5.5 No procedure for removing a requirement.** `Superseded` is a
  *proposal* state
  ([10-proposal-lifecycle.adoc:88-89](./10-proposal-lifecycle.adoc#L88-L89)).
  Nothing says what happens to the *specification* text when a feature is
  deprecated and removed from production — deleted outright, or marked? Given
  the spec describes only the present, deletion is implied, but a normative
  standard should say so.

---

## 6. Convention conformance

The repo [style guide](../../docs/style-guide.md) is normative for `src/`. TS-1
diverges in several places.

- [ ] **File naming.** [01a-persistence.adoc](./01a-persistence.adoc) violates
  "Content files MUST be named with a two-digit numeric prefix"
  ([style-guide.md:75-76](../../docs/style-guide.md#L75-L76)). TS-61 does the
  same (`05b-`, `09b-`), so there is a de-facto convention for inserted
  sections — but it is not sanctioned by the style guide. Either legitimize
  `NN[a-z]-` there or renumber.

- [ ] **References file.** TS-1 is the **only** standard of 61 that uses a
  separate `99-references.adoc`; all nine others with references put
  `== References` in `README.adoc` after `''''`, per
  [style-guide.md:96-99](../../docs/style-guide.md#L96-L99). Commit
  `eaab29b "edit: ts-1 move references out"` shows this was deliberate — so the
  style guide should be updated, or the file folded back. Right now TS-1 is
  silently non-conforming.

- [ ] **Reference entry format.** [99-references.adoc](./99-references.adoc)
  uses a period and a new sentence, violating the style guide's "hyperlink
  followed by a **colon** and a short descriptive annotation". A third format is
  specified in [TS-26 §12](../026/12-referencing.adoc#L27-L30)
  (`<author> (<year>). _<title>_. <publication>`). Three conventions, none of
  which TS-1 follows.

- [ ] **Quote marks — split convention.** AsciiDoc curly-quote syntax
  ``"`…`"`` appears 10 times, plain `"` about 25 times. Worst inside one file:
  [10-proposal-lifecycle.adoc:147-148](./10-proposal-lifecycle.adoc#L147-L148)
  uses plain quotes for a specification-phrasing example, while
  [10-proposal-lifecycle.adoc:199-200](./10-proposal-lifecycle.adoc#L199-L200)
  uses curly quotes for exactly the same kind of example.

- [ ] **Dashes — split convention.** 73 em dashes (—) vs 10 en dashes (–) used
  for the identical parenthetical function, concentrated in
  [08-executable-specifications.adoc:227-242](./08-executable-specifications.adoc#L227-L242),
  [03-acceptance-criteria.adoc:4](./03-acceptance-criteria.adoc#L4), and
  [07-qualities.adoc:3](./07-qualities.adoc#L3).

- [ ] **Bold lead-ins — three competing forms.** The style guide mandates
  `* *Label.* Description.` and explicitly forbids alternatives
  ([style-guide.md:66-71](../../docs/style-guide.md#L66-L71)). TS-1 uses:

  - ✅ `* *Draft.* The proposal is…` — §09, §10, §06
  - ❌ `* *Framing:* authors, purpose…` — [01-scope.adoc:76](./01-scope.adoc#L76),
    81, 87, 89 (colon inside bold, lowercase continuation)
  - ❌ `* *Branching and review*, so a proposal…` —
    [10-proposal-lifecycle.adoc:32-41](./10-proposal-lifecycle.adoc#L32-L41)

  [05-context.adoc:43-51](./05-context.adoc#L43-L51) mixes two forms **within a
  single list** — three items in the inline-bold form, then
  `* *Dependencies.* External systems…` in the mandated form.

- [ ] **README missing related-standard links.**
  [style-guide.md:92-94](../../docs/style-guide.md#L92-L94) says the intro
  SHOULD link to related standards. [README.adoc](./README.adoc) links only to
  the external reference implementation, despite the body linking to TS-2, TS-3,
  TS-4, TS-7, TS-13, and TS-14. Compare [TS-3](../003/README.adoc), which does
  this well.

- [ ] **Prose cross-reference instead of an xref.**
  [06-behaviors.adoc:72](./06-behaviors.adoc#L72) — "covered in-depth in the
  section on executable specifications" should be
  `<<Executable specifications>>`, since the files merge into one document via
  `include::`.

- [ ] **Inconsistent listing blocks.**
  [01a-persistence.adoc:61](./01a-persistence.adoc#L61) titles its block
  (`.Example repository structure`); the equivalent trees in §04/§05/§06 are
  untitled. [07-qualities.adoc:67-71](./07-qualities.adoc#L67-L71) puts a user
  story in a bare `----` block while §08 uses `[source,feature]` for comparable
  content.

- [ ] **Mermaid rendering.**
  [10-proposal-lifecycle.adoc:60-71](./10-proposal-lifecycle.adoc#L60-L71)
  uses a `[mermaid]` block. The repo README states GitHub is the render target
  and there is no build tooling — confirm this actually renders through GitHub's
  AsciiDoc pipeline rather than falling back to a literal block, since the state
  machine is one of the standard's key diagrams.

---

## 7. `AGENTS.md` has drifted from the standard

[AGENTS.md](./AGENTS.md) is meant to be a faithful compaction. It is not.

- [x] **Invents a rule not in the standard.** **Done** — the "Avoid iterating on
  NFRs / Big-design-up-front is preferred" sentences are deleted. Replaced with
  the standard's actual §07 reasoning (architecturally significant, harder to
  change than FRs) plus the SLA point.

  Original defect: [AGENTS.md:123](./AGENTS.md#L123) asserted a
  big-design-up-front preference appearing nowhere in
  [07-qualities.adoc](./07-qualities.adoc), which sat badly with the standard's
  own incremental proposal machinery in §10.

- [x] **Typos in a file that agents act on.** **Done** — "product product" →
  "a product"; "PRF" → "PRD"; "tht" → "that".

- [x] **Internal MAY/SHOULD mismatch.** **Done** — heading promoted to "Some
  NFRs SHOULD be expressed as user stories", matching the rule beneath it and
  §07's own wording.

- [x] **Merge rule contradicted the standard.** **Done** — AGENTS.md carried the
  old "MUST NOT be merged until it is live in production" rule, which
  [1.2](#12-spec-merge-timing--three-mutually-incompatible-rules) replaced.
  Updated to the same-change-set rule.

- [x] **DoR checklist truncated.** **Done** — restored "Is it clear who the
  stakeholders are?" and "Can the design be iterated based on feedback?", giving
  6 of the standard's 7 criteria. (The standard splits independence and small
  increments into two items; AGENTS.md keeps them combined as one.)

- [ ] **Omits the taxonomy the standard is built on.** AGENTS.md gives the
  context/requirements split but never mentions `rules`, `access`, `interfaces`,
  or `journeys` — four of the five behavior sections. An agent asked to
  structure a spec from AGENTS.md alone would produce features-and-qualities
  only.

- [ ] **Also absent:** persistence/placement options (§01a), requirements
  elicitation (§09 entirely), traceability, CI enforcement, cross-functional
  review, and recording rejections. Some trimming is expected in a compact
  version, but these are omissions worth a deliberate decision rather than
  drift.

**Verified sound:** links to `../013/AGENTS.md` and `../014/AGENTS.md` resolve.
All six standard cross-references in the body (TS-2, TS-3, TS-4, TS-7, TS-13,
TS-14) resolve with correct titles.

---

## 8. Typos and grammar

| Location | Issue |
|---|---|
| [01-scope.adoc:13](./01-scope.adoc#L13) | "A software requirements is a living document" → *requirements specification* |
| [01-scope.adoc:156](./01-scope.adoc#L156) | "cross-reference **that** test(s) that verify it" → *the*; also lowercase "should" beside a SHOULD in the same sentence |
| [01a-persistence.adoc:20](./01a-persistence.adoc#L20) | "the same version control **systems** as used to" → *system* |
| [05-context.adoc:78](./05-context.adoc#L78) | "**They** may be a lot of necessary overlap" → *There* |
| [05-context.adoc:98](./05-context.adoc#L98) | "who are the **participates**" → *who the participants are* |
| [06-behaviors.adoc:71](./06-behaviors.adoc#L71) | "**RECOMMENDEDs**" → *RECOMMENDS* |
| [08-executable-specifications.adoc:20](./08-executable-specifications.adoc#L20) | "One of the **objective's** of the language's design" → *objectives* |
| [08-executable-specifications.adoc:266](./08-executable-specifications.adoc#L266) | "with **severable** variable inputs" → *several* |
| [09-requirements-elicitation.adoc:133](./09-requirements-elicitation.adoc#L133) | "closer to implementation planning **that** it is" → *than* |
| [10-proposal-lifecycle.adoc:94](./10-proposal-lifecycle.adoc#L94) | "code and configuration **is** merged" → *are* |
| [99-references.adoc:5](./99-references.adoc#L5) vs [09:26](./09-requirements-elicitation.adoc#L26) | Same Brandolini post cited as `.blogspot.co.uk` and `.blogspot.com` |

### Other prose issues

- [ ] [03-acceptance-criteria.adoc:3](./03-acceptance-criteria.adoc#L3) —
  "**Most** requirements specifications **SHOULD** be written as acceptance
  criteria" — double-hedged; the style guide says avoid hedging. Either they
  SHOULD be, or state the exception.

- [ ] [07-qualities.adoc:33-35](./07-qualities.adoc#L33-L35) — "all NFRs
  **MUST** be identified… **as early as possible**" — an unfalsifiable MUST.
  Nobody can demonstrate a violation. SHOULD, or tie it to a gate ("before the
  first release increment is designed").

- [ ] [06-behaviors.adoc:44](./06-behaviors.adoc#L44) — "The **all-important**
  features…" — editorializing filler.

- [ ] [05-context.adoc:58-61](./05-context.adoc#L58-L61) — "…so the constraint
  itself is purely a statement of the boundary. **The constraint remains purely
  descriptive.**" The second sentence restates the first.

- [ ] [06-behaviors.adoc:78-79](./06-behaviors.adoc#L78-L79) — "if **we**
  specified policies… **we'd** get duplication" —
  [TS-26 §01](../026/01-voice-and-tense.adoc#L18-L20) reserves "we" for genuine
  statements of the author's position.

- [ ] **Terminology collision on "features".**
  [03-acceptance-criteria.adoc:34](./03-acceptance-criteria.adoc#L34) defines
  "features" as functional + non-functional requirements combined.
  [06-behaviors.adoc:12](./06-behaviors.adoc#L12) defines "Features" as
  scenario-level behaviors under `behaviors/`. Two meanings for a term the
  standard makes structural — a direct violation of
  [TS-26 §03](../026/03-terminology.adoc) ("use one term per concept").

- [ ] **Terminology collision on "journey".**
  [08-executable-specifications.adoc:136](./08-executable-specifications.adoc#L136)
  — a scenario "describes a **journey**" collides with §06's `journeys/`
  section.

- [ ] [01-scope.adoc:139](./01-scope.adoc#L139) — section titled "Executable
  tests" but argues about executable *specifications*, which is §08's title.
  Align.

- [ ] [06-behaviors.adoc:108-115](./06-behaviors.adoc#L108-L115) — the access
  table renders a full matrix with explicit `—` for Anonymous, while
  [06-behaviors.adoc:117-120](./06-behaviors.adoc#L117-L120) says "it is
  sufficient to state each capability once, against the lowest-privileged actor
  that holds it." The example does not demonstrate the rule it precedes.

- [ ] [08-executable-specifications.adoc:168-173](./08-executable-specifications.adoc#L168-L173)
  — the scheduling scenario publishes the post, *then* sets the future
  publication date. Reversed causally.

- [ ] **Line length.** The [style guide](../../docs/style-guide.md) implies
  80-column wrapping and most of the repo honors it. ~30 prose lines in TS-1 run
  to 81-84 chars; [99-references.adoc](./99-references.adoc) runs to 150. Prose
  overruns are trivial to fix; the reference file needs a wrapping decision
  (long URLs may justify an exemption — worth stating one).

---

## Changelog

### §10 rename (2026-07-27)

Uncommitted. `10-managing-requirements.adoc` → `10-proposal-lifecycle.adoc`
(via `git mv`, so history follows), title "= Managing requirements" →
"= Proposal lifecycle". Kieran's call: the section is about the proposal
lifecycle, and the old broad title invited the drift catalogued in
[4.1](#41-10-has-become-a-catch-all).

Consequential edits:

- The intro paragraph was extended to introduce proposals, since the section
  now opens on that concept rather than on "managing requirements" generally.
- The `== The proposal lifecycle` subsection was retitled `== Lifecycle states`.
  A subsection sharing its parent document's title would have made the
  `<<The proposal lifecycle>>` xref ambiguous, and the subsection's actual
  content is the state machine.
- `README.adoc` include directive updated.
- Filename references throughout this plan updated.

No section contents were moved. The destination map in
[4.1](#41-10-has-become-a-catch-all) is proposed and awaiting approval.

### Tier 1 — correctness (2026-07-27)

Committed by Kieran across five commits (`d6f4c47`…`a8588c6`, plan at
`b147b48`), with edits of their own on top — see
[Kieran's amendments](#kierans-amendments-to-tier-1) below. Five files touched:
`01a-persistence.adoc`, `06-behaviors.adoc`,
`08-executable-specifications.adoc`, `10-proposal-lifecycle.adoc`,
`AGENTS.md`.

**Decision taken.** The §01a/§10 merge-timing conflict
([1.2](#12-spec-merge-timing--three-mutually-incompatible-rules)) was resolved
in favor of **specification edits merging in the same change-set as the code
that implements them**. Kieran chose this over the alternative (hold the spec
edit on a branch until the code is live), which would have kept the main line
strictly true of production at the cost of long-lived proposal branches. The
accepted rule allows the main line to briefly lead production between merge and
deploy; §10 now states that window explicitly and assigns closing it to the
release pipeline.

**Consequential edits beyond the literal findings:**

- The `Accepted` and `Released` state definitions in §10 were reworded — the old
  `Released` text defined release as the merge event, which the new rule
  separates into merge and deploy.
- §10's colocation paragraph was trimmed to an xref rather than restating the
  merge rule, so the rule now has exactly one statement.
- [2.3](#23-both-templates-misalign-step-indentation) was pulled forward from
  tier 2 (rationale recorded at that item).
- The `Given` example block in §08 was rewritten alongside the `When` block; it
  had the same first-person / UI-flavored problem but was not called out
  separately in the original review.
- Three `<<…>>` internal xrefs were introduced (`<<Actors>>`,
  `<<Binding the specification to production>>`, `<<Implementation>>`); all
  three verified to resolve against existing section titles.

**Not addressed in this tier.** Two §7 items are scope decisions rather than
defects, and remain open for tier 3: AGENTS.md omitting the
rules/access/interfaces/journeys taxonomy, and its omission of §01a, §09,
traceability, CI enforcement, cross-functional review, and rejection recording.

**Verification performed.** Grep confirmed no stale wording survived (old merge
phrasing, "inherited up", "uses indentation", the invented big-design-up-front
rule, the three typos, first-person Gherkin steps). All xref targets checked
against the set of section titles. New lines checked against the 80-column
convention. No rendering check was possible — the repo has no build tooling, so
the AsciiDoc output has not been visually confirmed.

#### Kieran's amendments to tier 1

Applied during commit, on top of the changes above:

- **Gherkin template placeholders `{…}` → `<…>`** throughout §08, conforming to
  [TS-26 §11](../026/11-code-blocks.adoc#L5-L7), which mandates angle brackets
  for placeholder text.

  Side effect worth tracking: §08 now uses `<…>` for two different things —
  template placeholders, and genuine Gherkin scenario-outline variables
  ([08:284-286](./08-executable-specifications.adoc#L284-L286)). The sentence
  "Variables in the scenario outline steps are marked up with `<` and `>`" no
  longer distinguishes the two. Accepted as the cost of TS-26 conformance; if
  it proves confusing, the fix is a sentence noting the distinction, not a
  revert.

- **§08 em-dash for colon** — "Gherkin is line-oriented — one statement per
  line", conforming to [TS-26 §13](../026/13-punctuation.adoc#L5-L7), which
  restricts colons to introducing lists.

- **AGENTS.md trimmed** — the sentence "Acceptance authorizes the work; it does
  not license the spec to describe behavior that does not yet exist" was
  dropped, keeping the compact version terser than the standard.
