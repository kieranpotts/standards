# TS-15 gap analysis

Gaps found comparing TS-15: *User interfaces* against the following reference
resources:

- `__TODO__/015/API Design.md` (local file)
- `__TODO__/015/guidelines.md` (link list — Atlassian, BBC GEL, CFPB, IBM,
  Microsoft Windows, Polaris, and others that failed to fetch)
- `__TODO__/015/usability.md` (link list — Nielsen Norman Group,
  usability.gov, Google Design, Usability Post)
- `__TODO__/015/laws-of-ux` → https://lawsofux.com/

**Assessment.** TS-15 is currently thin: one principles file with two sections
("Keep it tidy" and "Embrace affordances"). Its stated scope is broad — any
human-computer interface, including GUIs, TUIs, CLIs, and APIs — so almost all
of the reference material falls inside that scope. The bulk of the reference
content is missing entirely: feedback and system status, error prevention and
recovery, recognition over recall, flexibility/efficiency, help and
documentation, the Laws of UX, and API-specific design principles are all
absent. A few items (consistency, minimalism, responsive design, color
accessibility) receive partial treatment in "Keep it tidy". The platform- or
brand-specific design systems (IBM, Microsoft Windows, Polaris, Atlassian's AI
content) are flagged out-of-scope.

**Status:** Initial run, 2026-08-05. All gaps below remain open.

**Second run, 2026-08-06.** Re-run against the UK Government Design
Principles (https://www.gov.uk/guidance/government-design-principles). Three
principles were routed to TS-15: #6 ("This is for everyone"), #7
("Understand context"), and #9 ("Be consistent, not uniform"). #7 is a
new Missing gap (no context-of-use treatment exists). #6 and #9 are
Partial — existing entries already cover much of their ground
(accessibility via CFPB/usability.gov/Laws of UX; consistency via Nielsen
Heuristic 4 and Jakob's Law); the new entries capture only what those
existing entries omit (#6: sacrificing elegance, prioritising the
hardest-to-reach users; #9: the consistency-vs-uniformity distinction and
evolving/sharing patterns). All prior gaps remain open.

**Third run, 2026-08-06.** Re-run against Nelson Elhage's "Reflections on
software performance" (https://blog.nelhage.com/post/reflections-on-performance/).
One point was routed to TS-15: "performance changes how users use software"
(B). It is Missing — TS-15 has no response-time thresholds (not even the
100ms instantaneous-perception threshold) and no treatment of performance
changing interaction patterns; the existing Doherty Threshold (400ms) entry
is adjacent but distinct. One new Missing gap added; all prior gaps remain
open.

**Fifth run (`close-gaps`), 2026-08-14.** All 51 actionable items (47
Missing, 4 Partial) closed in one run, across ten new content partials
(`02-feedback-and-communication.adoc` through
`10-visual-rhythm-and-text.adoc`) plus expansions to the existing "Keep it
tidy" and "Embrace affordances" content in `01-design-principles.adoc` and
a new usability-definition paragraph on the page itself. This run was
conducted jointly with a `close-gaps` run against TS-18 (Web GUIs), on the
user's request, specifically to catch gaps that would be better routed
between the two standards; none were found — TS-18's remaining gaps are all
web-implementation-specific (HTTP/CSS/DOM mechanics) and TS-15's are all
platform-agnostic HCI/UX principles, so no items moved in either direction.
TS-15's 7 Out-of-scope items and 12 Unresolved references remain open; none
were actioned in this run. All checked items below carry a **Resolved.**
note stating what was written and where.

## Missing

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 1:
      Visibility of System Status) is not addressed anywhere in the standard.
      The standard never states that interfaces should keep users informed about
      what is going on through timely feedback. Recommend a new section
      "Feedback and system status" in `01-design-principles.adoc`.

      **Resolved.** Closed by `02-feedback-and-communication.adoc`, "Feedback
      and system status" section. Covers immediate response to input,
      progress indicators for long operations, and not showing false
      completion. Source added to the page's `== References`.

- [x] https://lawsofux.com/#doherty-threshold is not addressed anywhere in the
      standard. The Doherty Threshold states that productivity soars when
      computer and user interact at a pace under 400 ms, and that perceived
      performance and progress bars help when waits are unavoidable. Recommend
      the new "Feedback and system status" section.

      **Resolved.** Closed by the same section's response-time-thresholds
      table (100ms/400ms/1s/10s), documenting the 400ms Doherty Threshold and
      perceived-performance techniques. Source added to the page's
      `== References`.

- [x] https://lawsofux.com/#flow is not addressed anywhere in the standard.
      Flow (immersed, energized focus) is sustained by removing friction,
      giving feedback on what was done and accomplished, and making content
      discoverable. Recommend the new "Feedback and system status" section.

      **Resolved.** Closed by the same section's closing paragraph on Flow —
      friction removal, feedback on progress, and discoverable content.
      Source added to the page's `== References`.

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 2:
      Match Between System and Real World) is not addressed anywhere in the
      standard. Interfaces should speak the users' language, use familiar
      words/phrases, follow real-world conventions, and present information in a
      natural and logical order. Recommend a new section "Speak the user's
      language" in `01-design-principles.adoc`.

      **Resolved.** Closed by `02-feedback-and-communication.adoc`, "Speak
      the user's language" section. Covers familiar vocabulary, real-world
      conventions, and natural information ordering.

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 3:
      User Control and Freedom) is not addressed anywhere in the standard.
      Users need a clearly marked "emergency exit", and support for Undo and
      Redo, to back out of unwanted actions. Recommend a new section "User
      control and freedom" in `01-design-principles.adoc`.

      **Resolved.** Closed by `02-feedback-and-communication.adoc`, "User
      control and freedom" section. Covers emergency exits from flows, Undo,
      and Redo, cross-linked to the existing "Embrace affordances" section.

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 5:
      Error Prevention) is not addressed anywhere in the standard. Good designs
      either eliminate error-prone conditions or check for them and present a
      confirmation before committing; slips vs. mistakes are distinguished, and
      helpful constraints, good defaults, and warnings are recommended.
      Recommend a new section "Error prevention" in `01-design-principles.adoc`.

      **Resolved.** Closed by `03-errors.adoc`, "Error prevention" section.
      Covers eliminating error-prone conditions, the slip/mistake
      distinction, constraints and good defaults, and confirmation before
      consequential actions.

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 6:
      Recognition Rather than Recall) is not addressed anywhere in the standard.
      Minimize memory load by keeping elements, actions, and options visible
      and easily retrievable; users should not have to remember information from
      one part of the interface to another. Recommend a new section "Recognition
      over recall" in `01-design-principles.adoc`.

      **Resolved.** Closed by `04-memory-and-cognitive-load.adoc`,
      "Recognition over recall" section. Covers keeping information visible,
      differentiating visited links, and carrying critical information across
      screens.

- [x] https://lawsofux.com/#working-memory is not addressed anywhere in the
      standard. Working memory holds only 4–7 chunks that fade in 20–30 seconds,
      so designers should keep displayed information necessary and relevant,
      differentiate visited links, and carry critical information across
      screens (e.g. comparison tables). Recommend the new "Recognition over
      recall" section.

      **Resolved.** Closed by the same section's opening paragraph, stating
      the 4-7 chunk / 20-30 second working-memory limit. Source added to the
      page's `== References`.

- [x] https://lawsofux.com/#millers-law is not addressed anywhere in the
      standard. Miller's Law (7±2 items in working memory) implies content
      should be organized into chunks; the site warns against using the
      "magical number seven" to justify arbitrary limitations. Recommend the
      new "Recognition over recall" section.

      **Resolved.** Closed by the same section's "Organize content into
      chunks" bullet, including the explicit warning against using Miller's
      Law to justify an arbitrary item-count limit.

- [x] https://lawsofux.com/#chunking is not addressed anywhere in the standard.
      Chunking (grouping information into meaningful wholes with clear
      hierarchy) lets users scan, identify, and process content faster.
      Recommend the new "Recognition over recall" section.

      **Resolved.** Closed by the same "Organize content into chunks" bullet.

- [x] https://lawsofux.com/#cognitive-load is not addressed anywhere in the
      standard. The standard does not distinguish intrinsic vs. extraneous
      cognitive load, nor warn that distracting/unnecessary elements add
      extraneous load. Recommend the new "Recognition over recall" section.

      **Resolved.** Closed by the same section's closing paragraph,
      distinguishing intrinsic from extraneous cognitive load and
      cross-linking to "Keep it tidy".

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 7:
      Flexibility and Efficiency of Use) is not addressed anywhere in the
      standard. Accelerators (keyboard shortcuts, gestures) hidden from
      novices can speed expert interaction; processes can be carried out in
      different ways; personalization and customization cater to both
      inexperienced and experienced users. Recommend a new section
      "Flexibility and efficiency" in `01-design-principles.adoc`.

      **Resolved.** Closed by `04-memory-and-cognitive-load.adoc`,
      "Flexibility and efficiency of use" section. Covers accelerators,
      multiple paths to the same outcome, and personalization/customization.

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 9:
      Help Users Recognize, Diagnose, and Recover from Errors) is not addressed
      anywhere in the standard. Error messages should use plain language (no
      error codes), precisely indicate the problem, constructively suggest a
      solution, and use recognizable visual treatments. Recommend a new
      section "Error messages" in `01-design-principles.adoc`.

      **Resolved.** Closed by `03-errors.adoc`, "Error messages" section.
      Covers plain language, precision, solution suggestions, and consistent
      visual treatment.

- [x] https://www.bbc.co.uk/gel/guidelines/how-to-write-useful-error-messages
      is not addressed anywhere in the standard. It adds systematic guidance for
      error messages: enumerate and group errors by cause, rank by severity,
      give messages a consistent structure (e.g. [Explain][Instruct] or
      [Apologise][Explain][Resolve]), use active voice, trim "please", avoid
      blaming the user, and vary tone by severity (casual for minor, sincere
      for severe). Recommend the new "Error messages" section.

      **Resolved.** Closed by the same section's remaining bullets: message
      structure (Explain/Instruct or Apologize/Explain/Resolve), active
      voice, trimming "please", not blaming the user, tone-by-severity, and
      grouping/ranking by cause. Tone-by-severity cross-links to the new
      "Voice and tone" section. Source added to the page's `== References`.

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 10:
      Help and Documentation) is not addressed anywhere in the standard. Even
      ideal designs may need help; documentation should be easy to search,
      focused on the user's task, concise, list concrete steps, and be
      presented in context when needed. Recommend a new section "Help and
      documentation" in `01-design-principles.adoc`.

      **Resolved.** Closed by `04-memory-and-cognitive-load.adoc`, "Help and
      documentation" section. Covers searchability, task focus, concision,
      and cross-references TS-25 (Technical documentation) and TS-26
      (Technical writing style guide) for documentation content itself.

- [x] https://lawsofux.com/#paradox-of-the-active-user is not addressed anywhere
      in the standard. Users skip manuals and start using software immediately,
      so guidance should be accessible in context (e.g. tooltips) along
      whatever path they take. Recommend the new "Help and documentation"
      section.

      **Resolved.** Closed by the same section's "Present help in context"
      bullet.

- [x] https://lawsofux.com/#jakobs-law is not addressed directly in the
      standard. Jakob's Law says users prefer your interface to work like others
      they already know; they transfer expectations between similar products,
      and breaking conventions should be minimized (with a familiar-version
      transition when changes are made). Recommend a new section "Respect
      conventions and mental models" in `01-design-principles.adoc`.

      **Resolved.** Closed by `04-memory-and-cognitive-load.adoc`, "Respect
      conventions and mental models" section, and cross-linked from the
      expanded consistency bullet in "Keep it tidy". Source added to the
      page's `== References`.

- [x] https://lawsofux.com/#mental-model is not addressed anywhere in the
      standard. Designs should match users' mental models so users can transfer
      knowledge from one product to another; user research (interviews,
      personas, journey maps, empathy maps) shrinks the gap between designer
      and user mental models. Recommend the new "Respect conventions and
      mental models" section.

      **Resolved.** Closed by the same section's "Design to match users'
      mental models" bullet, naming interviews, personas, journey maps, and
      empathy maps as the research tools that narrow the gap.

- [x] https://lawsofux.com/#hicks-law is not addressed anywhere in the
      standard. Hick's Law (decision time grows with the number and complexity
      of choices) implies minimizing choices when response time is critical,
      breaking complex tasks into smaller steps, highlighting recommended
      options, and using progressive onboarding — while avoiding
      over-abstraction. Recommend a new section "Manage choice and complexity"
      in `01-design-principles.adoc`.

      **Resolved.** Closed by `05-choice-and-complexity.adoc`, "Manage choice
      and complexity" section. Covers minimizing choices under time pressure,
      breaking tasks into steps, highlighting recommended options, and
      progressive onboarding without over-abstraction. Source added to the
      page's `== References`.

- [x] https://lawsofux.com/#choice-overload is not addressed anywhere in the
      standard. Too many options overwhelms users and degrades decision-making;
      mitigate with side-by-side comparison, prioritized/featured content,
      and up-front search and filtering. Recommend the new "Manage choice and
      complexity" section.

      **Resolved.** Closed by the same section's "Prevent choice overload"
      bullet: side-by-side comparison, prioritized/featured content, and
      up-front search and filtering.

- [x] https://lawsofux.com/#teslers-law is not addressed anywhere in the
      standard. Tesler's Law (conservation of complexity) states every process
      has irreducible core complexity that must be borne by either the system
      or the user — designers should absorb as much of that burden as possible,
      and not design for an idealized rational user. Recommend the new "Manage
      choice and complexity" section.

      **Resolved.** Closed by the same section's "Absorb complexity" bullet,
      stating the system-should-absorb-it principle and the caution against
      designing for an idealized rational user.

- [x] https://lawsofux.com/#occams-razor is not addressed anywhere in the
      standard. Occam's Razor says the simplest competing hypothesis should be
      selected; reduce complexity by removing as many elements as possible
      without compromising function. Recommend the new "Manage choice and
      complexity" section.

      **Resolved.** Closed by the same section's "Prefer the simplest
      solution that works" bullet, cross-linked to the expanded Occam's
      Razor mention in "Keep it tidy".

- [x] https://lawsofux.com/#fittss-law is not addressed anywhere in the
      standard. Fitts's Law (time to acquire a target is a function of distance
      and size) implies touch targets should be large, well-spaced, placed near
      the user's attention area, and that fast movements + small targets cause
      errors. Recommend a new section "Targeting and reachability" in
      `01-design-principles.adoc`.

      **Resolved.** Closed by `05-choice-and-complexity.adoc`, "Targeting and
      reachability" section. Covers target size, spacing, placement near the
      user's attention area, and the fast-movement/small-target error
      trade-off.

- [x] https://lawsofux.com/#aesthetic-usability-effect is not addressed
      anywhere in the standard. Users perceive aesthetically pleasing designs
      as more usable, are more tolerant of minor usability issues when designs
      are attractive, and visually pleasing design can mask usability problems
      during testing. Recommend a new section "Aesthetics and perceived
      usability" in `01-design-principles.adoc`.

      **Resolved.** Closed by `06-visual-perception.adoc`, "Aesthetics and
      perceived usability" section. Covers both the tolerance effect and the
      usability-testing risk of masked problems, with a requirement that
      testing not rely on subjective ratings alone.

- [x] https://lawsofux.com/#serial-position-effect is not addressed anywhere in
      the standard. Users best remember the first and last items in a series
      (primacy and recency effects), so place key actions at the far left and
      right of navigation and least important items in the middle. Recommend a
      new section "Ordering and emphasis" in `01-design-principles.adoc`.

      **Resolved.** Closed by `06-visual-perception.adoc`, "Ordering and
      emphasis" section, "Place key actions at the ends of a sequence"
      bullet.

- [x] https://lawsofux.com/#von-restorff-effect is not addressed anywhere in the
      standard. The Von Restorff (Isolation) Effect predicts the visually
      distinctive item in a group is most remembered; make important info or
      key actions visually distinctive, use restraint so emphasized items
      don't compete or look like ads, and don't rely on color or motion alone
      (color-vision deficiency, motion sensitivity). Recommend the new
      "Ordering and emphasis" section.

      **Resolved.** Closed by the same section's "Make the important item
      visually distinctive — with restraint" bullet, cross-linked from the
      expanded color-accessibility paragraph in "Keep it tidy".

- [x] https://lawsofux.com/#selective-attention is not addressed anywhere in
      the standard. Selective attention means people filter out irrelevant
      stimuli; banner blindness (users ignore ad-like content) and change
      blindness (significant changes go unnoticed without strong cues) are
      consequences designers must counter. Recommend the new "Ordering and
      emphasis" section.

      **Resolved.** Closed by the same section's "Counter banner blindness"
      and "Counter change blindness" bullets.

- [x] https://lawsofux.com/#law-of-common-region,
      https://lawsofux.com/#law-of-proximity,
      https://lawsofux.com/#law-of-pragnanz,
      https://lawsofux.com/#law-of-similarity, and
      https://lawsofux.com/#law-of-uniform-connectedness are not addressed
      anywhere in the standard. These Gestalt grouping principles describe how
      users perceive structure: common region (borders/backgrounds group
      elements), proximity (near elements group), Prägnanz (ambiguous shapes
      read as simplest form), similarity (visually similar elements seem
      related — keep links differentiated from body text), and uniform
      connectedness (visually connected elements seem most related).
      Recommend a new section "Grouping and structure" in
      `01-design-principles.adoc`.

      **Resolved.** Closed by `06-visual-perception.adoc`, "Grouping and
      structure" section, covering all five Gestalt principles named:
      common region, proximity, Prägnanz, similarity (including the
      link-vs-body-text distinction), and uniform connectedness.

- [x] https://lawsofux.com/#goal-gradient-effect and
      https://lawsofux.com/#zeigarnik-effect are not addressed anywhere in the
      standard. Both note that visible progress toward a goal (even artificial
      progress) motivates users to complete tasks; the Zeigarnik Effect adds
      that people remember uncompleted tasks better, so clear signifiers of
      additional content invite discovery. Recommend a new section "Progress
      and completion" in `01-design-principles.adoc`.

      **Resolved.** Closed by `07-motivation-and-pacing.adoc`, "Progress and
      completion" section, covering both effects and the caveat that
      artificial progress must not be misleading about genuine remaining
      effort.

- [x] https://lawsofux.com/#peak-end-rule is not addressed anywhere in the
      standard. People judge an experience by its most intense point and its
      end rather than the average of every moment, and recall negative
      experiences more vividly than positive ones — design the peaks, ends, and
      recovery from low points deliberately. Recommend a new section
      "Experience peaks and endings" in `01-design-principles.adoc`.

      **Resolved.** Closed by `07-motivation-and-pacing.adoc`, "Experience
      peaks and endings" section, covering deliberate design of peaks,
      endings, and recovery from low points.

- [x] https://lawsofux.com/#parkinsons-law is not addressed anywhere in the
      standard. Parkinson's Law (work expands to fill available time) implies
      limiting task duration to user expectations and using autofill to prevent
      task inflation in forms, purchases, and bookings. Recommend a new
      section "Task duration and pacing" in `01-design-principles.adoc`.

      **Resolved.** Closed by `07-motivation-and-pacing.adoc`, "Task duration
      and pacing" section, covering both bullets: setting duration
      expectations and using autofill against task inflation.

- [x] https://lawsofux.com/#pareto-principle is not addressed anywhere in the
      standard. Roughly 80% of effects come from 20% of causes, so focus
      design effort on the areas that bring the largest benefits to the most
      users. Recommend a new section "Prioritization" in
      `01-design-principles.adoc`.

      **Resolved.** Closed by `07-motivation-and-pacing.adoc`,
      "Prioritization" section.

- [x] https://lawsofux.com/#postels-law is not addressed anywhere in the
      standard. Postel's Law ("be liberal in what you accept, conservative in
      what you send") counsels tolerance and flexibility for user input,
      anticipating variable input, defining boundaries, and providing clear
      feedback — equally relevant to UIs and APIs. Recommend a new section
      "Tolerance of input" in `01-design-principles.adoc`.

      **Resolved.** Closed by `08-inputs-context-and-bias.adoc`, "Tolerance
      of input" section, including the explicit note that the principle
      applies equally to GUIs and APIs, cross-linking to the new
      "API design principles" section. Source added to the page's
      `== References`.

- [x] https://lawsofux.com/#cognitive-bias is not addressed anywhere in the
      standard. Cognitive biases (incl. confirmation bias) systematically skew
      user judgment; awareness helps designers avoid fallacious reasoning and
      unintentional discrimination. Recommend a new section "Bias awareness" in
      `01-design-principles.adoc`.

      **Resolved.** Closed by `08-inputs-context-and-bias.adoc`, "Bias
      awareness" section, covering confirmation bias and the link to
      unintentional discrimination via unexamined designer assumptions.

- [x] `__TODO__/015/API Design.md` (lines 1–13) frames API design as
      developer UX — "an application's API is developer UX" — and asserts APIs
      should be evaluated for utility, simplicity, and elegance. The standard
      declares APIs are user interfaces (`README.adoc:18-19`) but gives no
      API-specific guidance. Recommend a new section "API-specific principles"
      in `01-design-principles.adoc`, or a dedicated file
      `02-api-design-principles.adoc`.

      **Resolved.** Closed by a new `09-api-design-principles.adoc` partial,
      "API design principles" section — a dedicated file, since the topic
      warranted more than a subsection. States the developer-as-user framing
      and cross-references TS-21 (HTTP APIs) for transport-specific guidance.
      (Note: `README.adoc` in the original item text refers to what is now
      the page `pages/015.adoc`, following this repository's move to a
      native Antora module.)

- [x] `__TODO__/015/API Design.md` (lines 21–44, "Simplicity") is not
      addressed anywhere in the standard. APIs should be simple and have a low
      barrier to entry for new users, but simplicity must not violate the
      single-responsibility principle (the jQuery `$` overload is given as a
      cautionary example of one method doing many unrelated jobs, raising
      cyclomatic complexity and harming testability/maintainability).
      Recommend the new "API-specific principles" section.

      **Resolved.** Closed by the same section's "barrier to entry" and
      "single-responsibility" bullets, including the jQuery `$` example.

- [x] `__TODO__/015/API Design.md` (lines 46–67) is not addressed anywhere
      in the standard. Repurposing one method as both getter and setter (e.g.
      `.height(50)` vs `.height()`) is a common anti-pattern because reading
      and mutating are fundamentally different actions and should have
      distinct names; property-assignment syntax with getters/setters makes
      mutation explicit. Recommend the new "API-specific principles" section.

      **Resolved.** Closed by the same section's getter/setter bullet.

- [x] https://www.usability.gov/ (Usability — definition) is not addressed
      anywhere in the standard. The standard never defines usability nor how it
      relates to the broader UX umbrella, nor that it is measurable through
      success rates and customer satisfaction. Recommend adding a short
      "What is usability?" subsection to `README.adoc`.

      **Resolved.** Closed by a new paragraph on the page (`pages/015.adoc`)
      immediately after the standard's scope paragraph, defining usability,
      relating it to the UX umbrella, and stating it is measurable through
      success rates, time on task, error rates, and satisfaction. Source
      added to the page's `== References`.

- [x] https://www.bbc.co.uk/gel/guidelines/spacing-units is not addressed
      anywhere in the standard. Predefined spacing scales create consistency
      and let designers and developers share a vocabulary; spacing units
      define only space between elements (not sizes), should be flexed at
      breakpoints, and exception units are for component-level spacing only.
      Recommend a new section "Spacing and rhythm" in
      `01-design-principles.adoc`.

      **Resolved.** Closed by `10-visual-rhythm-and-text.adoc`, "Spacing and
      rhythm" section, covering the scale concept, the space-not-size
      distinction, breakpoint flexing, and component-scoped exceptions.

- [x] https://www.bbc.co.uk/gel/guidelines/how-to-write-useful-error-messages
      ("Using your voice" / "Striking the right tone") is not addressed anywhere
      in the standard. A product should have a consistent Voice (personality)
      while Tone adapts to the situation; minor errors can be casual and warm,
      severe errors should be sincere and direct. Recommend the new "Error
      messages" section, or a new section "Voice and tone".

      **Resolved.** Closed by a new "Voice and tone" section in
      `10-visual-rhythm-and-text.adoc`, cross-linked from "Error messages"
      rather than merged into it, since voice/tone applies to all interface
      text, not only errors.

- [x] https://www.gov.uk/guidance/government-design-principles (Principle 7,
      "Understand context") is not addressed anywhere in the standard. The
      principle holds that we design for people, not screens, and must
      consider the context of use — where the user is (a library, a public
      space), the device (a phone), their familiarity with the web or
      specific products ("only really familiar with Facebook"), and
      first-time/no-prior-web users. TS-15 acknowledges only device screen
      size via responsive design (`01-design-principles.adoc:25-26`) and
      touches users' prior software exposure (`:51-53`) and physical-world
      knowledge (`:55-60`), but never frames design as context-of-use
      analysis and has no section on user research, personas, or
      situational context. Recommend a new "Understand context" / "Context
      of use" section in `01-design-principles.adoc`, possibly alongside a
      user-research/personas treatment.

      **Resolved.** Closed by `08-inputs-context-and-bias.adoc`, "Understand
      context" section — where the user is, what device they have, and their
      prior familiarity — plus the research-methods paragraph (interviews,
      personas, journey maps, empathy maps) and the accessibility-first
      posture, cross-linked from the expanded "Keep it tidy" accessibility
      paragraph. Source added to the page's `== References`.

- [x] https://blog.nelhage.com/post/reflections-on-performance/ ("Performance
      changes how users use software") is not addressed anywhere in the
      standard. The reference argues that fast tools don't just let users
      accomplish tasks faster — they enable entirely new types of tasks and
      new ways of working, and users choose faster tools more frequently:
      Sorbet became the fastest code-feedback loop (typecheck in 10-20s vs
      a 10-15min CI suite) so users reached for it first and tolerated its
      false errors; livegrep responds inside 100ms — the well-documented
      threshold at which a response appears "instantaneous" — so users use
      it *interactively*, entering a query then refining/iterating against
      the result list in real time, which adds power and approachability.
      TS-15 has no response-time/responsiveness thresholds at all (no 100ms
      instantaneous threshold) and never addresses performance changing
      *how* users use a tool. The existing Doherty Threshold entry
      (`GAPS.md:47-51`) is a 400ms productivity threshold, distinct from
      the 100ms instantaneous-perception threshold and from the
      "performance changes usage patterns" thesis. Recommend a new
      "Responsiveness and response-time thresholds" section in
      `01-design-principles.adoc` stating the 100ms/400ms/1s thresholds and
      how performance enables new interaction patterns (interactive
      iteration, new task types).

      **Resolved.** Closed by `02-feedback-and-communication.adoc`,
      "Feedback and system status" section: the response-time-thresholds
      table states the 100ms instantaneous / 400ms Doherty / 1s / 10s
      thresholds together (rather than as a separate section, since they
      share one table with the existing Doherty Threshold gap above), and a
      following paragraph states the "performance changes how users use
      software" thesis, citing the interactive-iteration pattern and users
      routing around latency. Source added to the page's `== References`.

**Fourth run, 2026-08-14.** One item routed in from TS-26 (Technical writing
style guide)'s gap analysis, whose `copywriting.adoc` source item was
confirmed out-of-scope for TS-26 on the grounds that UI microcopy is a
different register from documentation prose — the user asked that it be
captured here instead. One new Missing gap added; all prior gaps remain
open.

- [x] `copywriting.adoc` ("Copywriting guidelines") — UI/short-message text
      conventions: titles and short messages take no full stop; short
      messages should use hyphens for readability; longer, multi-sentence
      descriptions are written as full prose with terminal full stops.
      TS-15 `01-design-principles.adoc` has no microcopy or UI-text
      conventions of any kind. Recommend a new section, or a new partial if
      the topic grows beyond a section's worth of content.

      **Resolved.** Closed by `10-visual-rhythm-and-text.adoc`, "Microcopy
      and UI text" section, covering all three conventions and
      cross-referencing TS-26 (Technical writing style guide) for the
      longer-form prose register.

## Partial

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 4:
      Consistency and Standards) covers consistency more thoroughly than
      `01-design-principles.adoc:14` ("Use a consistent layout and design
      language throughout the application") — specifically, the reference
      requires both internal consistency (within a product family) and
      external consistency (established industry/platform conventions), cites
      Jakob's Law to explain why, and warns that inconsistency raises
      cognitive load.

      **Resolved.** Closed by expanding the "Use a consistent layout" bullet
      in `01-design-principles.adoc`, "Keep it tidy" section: internal vs.
      external consistency, Jakob's Law (cross-linked to
      "Respect conventions and mental models"), and the cognitive-load cost
      of inconsistency.

- [x] https://www.nngroup.com/articles/ten-usability-heuristics/ (Heuristic 8:
      Aesthetic and Minimalist Design) covers minimalism more thoroughly than
      `01-design-principles.adoc:5-26` ("Keep it tidy") — specifically, the
      reference states that every extra unit of information competes with
      relevant units and diminishes their visibility, and that the goal is to
      prioritize content and features that support primary goals (not merely
      "avoid clutter").

      **Resolved.** Closed by expanding the whitespace bullet in "Keep it
      tidy": every extra element competes with relevant ones, and the goal is
      prioritizing content/features that support primary goals, not merely
      avoiding clutter.

- [x] https://lawsofux.com/#occams-razor partially overlaps with
      `01-design-principles.adoc:5-9` (eliminate unnecessary animations) but
      adds the explicit principle that the best way to reduce complexity is to
      avoid it in the first place, and that completion is reached only when no
      more items can be removed without compromising function.

      **Resolved.** Closed by expanding the animations bullet in "Keep it
      tidy" with the Occam's Razor principle, cross-linked to the fuller
      treatment in "Manage choice and complexity".

- [x] https://lawsofux.com/#von-restorff-effect partially overlaps with
      `01-design-principles.adoc:33-36` (colors as accents for emphasis) but
      adds that emphasized items should not compete with one another or be
      mistaken for ads, and that emphasis must not rely on color alone (color
      vision deficiency) or motion alone (motion sensitivity).

      **Resolved.** Closed by expanding the color-accents paragraph in "Keep
      it tidy" with a cross-link to "Ordering and emphasis", where the full
      Von Restorff Effect treatment (including the not-competing and
      not-color/motion-alone caveats) lives.

- [x] https://cfpb.github.io/design-system/ ("About the CFPB Design System")
      partially overlaps with `01-design-principles.adoc:25-26` (responsive
      design) but adds an explicit mobile-first responsive approach and a
      general accessibility-best-practices commitment, which the standard
      mentions only for color (`01-design-principles.adoc:33-36`).

      **Resolved.** Closed by the new accessibility paragraph in "Keep it
      tidy", stating the mobile-first responsive approach and broadening
      accessibility beyond the color caveat. Source added to the page's
      `== References`.

- [x] https://www.usability.gov/ (News: Designing for people with disabilities)
      partially overlaps with `01-design-principles.adoc:33-36` (information
      conveyed by color must be accessible without color) but adds broader
      accessibility guidance: clear headings and action-oriented descriptions
      aid assistive-technology users, carousels can be difficult for them, and
      accessibility testing is required to ensure equal access.

      **Resolved.** Closed by the same new accessibility paragraph: clear
      headings and action-oriented descriptions, carousel caution, and the
      requirement for accessibility testing with real assistive technology.
      Source added to the page's `== References`.

- [x] https://www.gov.uk/guidance/government-design-principles (Principle 6,
      "This is for everyone") covers inclusive-design posture more directly
      than `01-design-principles.adoc:33-36` (color must not be the sole
      carrier of information) — specifically, the principle states that
      accessible design is good design and everything should be "as
      inclusive, legible and readable as possible"; that "if we have to
      sacrifice elegance - so be it"; and that "the people who most need
      our services are often the people who find them hardest to use," so
      the hardest-to-reach users should be considered from the start.
      TS-15's existing accessibility treatment is a single color caveat; the
      broader assistive-technology/motor/cognitive/auditory coverage is
      already captured by the CFPB and usability.gov entries above, but the
      prioritise-the-hardest-to-reach-users-first posture and the
      willingness-to-sacrifice-elegance principle are not. Recommend
      strengthening `01-design-principles.adoc:33-36` into a first-class
      "Accessibility and inclusivity" section that states these as
      objectives, not a color caveat.

      **Resolved.** Closed by a third new paragraph in "Keep it tidy":
      accessible design as good design, the willingness to sacrifice
      elegance, and prioritizing the hardest-to-reach users from the start,
      cross-linked to "Understand context". Written as an expansion of the
      existing color-caveat paragraph rather than a new top-level section,
      since "Keep it tidy" was judged the right home for it alongside the
      related consistency and minimalism expansions above. Source added to
      the page's `== References`.

- [x] https://www.gov.uk/guidance/government-design-principles (Principle 9,
      "Be consistent, not uniform") covers the consistency-vs-uniformity
      distinction more directly than `01-design-principles.adoc:14` ("Use a
      consistent layout and design language throughout the application") —
      specifically, the principle states consistency is "not a straitjacket
      or a rule book," that when patterns that work are found they should
      be shared and the reasons talked about, and that patterns should be
      improved or changed when better ways are found or user needs change.
      The existing Nielsen Heuristic 4 entry above covers internal +
      external consistency and Jakob's Law, but not the explicit licence
      to diverge from uniformity, the practice of sharing patterns across
      teams and explaining why, or the evolution of patterns over time.
      Recommend expanding `01-design-principles.adoc:14` to address when
      to diverge and how shared patterns evolve.

      **Resolved.** Closed by the same consistency-bullet expansion as the
      Nielsen Heuristic 4 item above: consistency is not a straitjacket,
      patterns that work should be shared with reasons, and patterns should
      evolve as better ways are found or needs change.

## Out-of-scope

- [ ] https://www.ibm.com/design/language/ ("Build Bonds" philosophy) covers
      IBM-specific brand ethos. Flagged out-of-scope because it is a corporate
      brand statement rather than a general interface principle.

- [ ] https://developer.microsoft.com/en-us/windows/apps/design covers
      Windows-specific app design (UWP/WinUI foundations, input types, form
      factors). Flagged out-of-scope because it is platform-specific guidance;
      any general principle it implies (intuitive, accessible, delightful) is
      already vague enough not to constitute a gap.

- [ ] https://polaris.shopify.com/ (Polaris homepage: Foundations, Components,
      Tokens, Icons) covers Shopify's commerce-domain design system mechanics
      (tokens, coded component packaging, commerce-domain iconography).
      Flagged out-of-scope as design-system implementation detail rather than
      general interface design guidance.

- [ ] https://atlassian.design/ ("Design for AI") covers designing AI
      experiences specifically. Flagged out-of-scope as a narrower topic than
      general user-interface design.

- [ ] https://www.bbc.co.uk/gel/guidelines/category/foundations lists BBC GEL's
      foundational categories (icons, grid, motion, spacing, typography).
      Flagged out-of-scope as a design-system inventory; only the spacing-units
      guidance was extracted as a substantive in-scope gap above.

- [ ] https://design.google/ homepage article blurbs (e.g. "Illustrating the
      Gemini App", "Refreshing Chrome", "UX Design as Dance Theater") are
      individual essays on specific projects. Flagged out-of-scope as
      project-specific narratives rather than general principles.

- [ ] https://www.usability.gov/ resource items (how to write a research plan,
      how to conduct a usability test, interview debriefs, participant
      agreements) cover user-research methodology. Flagged out-of-scope because
      TS-15 is about designing and implementing interfaces, not research
      methods — though the standard could usefully cross-reference TS-12
      (Quality assurance) or a future research standard.

## Unresolved

- [ ] https://airbnb.design/the-way-we-build/ returned 404 (and the alternative
      `https://airbnb.design/building-a-visual-language/` also 404). The Airbnb
      Design Language System series could not be retrieved and is not included
      in the comparison.

- [ ] https://developer.apple.com/ios/human-interface-guidelines/overview/design-principles/
      fetched but returned no extractable text (Apple's HIG is a
      JavaScript-rendered SPA). iOS design principles are not included in the
      comparison.

- [ ] https://www.lightningdesignsystem.com/guidelines/overview/ requires
      JavaScript and returned only "This website requires JavaScript."
      Salesforce Lightning design principles are not included in the
      comparison.

- [ ] https://material.io/guidelines/ redirects to m3.material.io, a
      JavaScript-rendered SPA; `https://m3.material.io/foundations/design-principles`
      returned 404 with boilerplate HTML. Material Design principles are not
      included in the comparison.

- [ ] https://www.nordnet.se/brand/ redirected to a Swedish marketing site
      rather than brand guidelines. Nordnet brand guidance is not included in
      the comparison.

- [ ] https://weconnect.github.io/plasma/docs/ returned 404 (GitHub Pages site
      not published). WeWork Plasma design system is not included in the
      comparison.

- [ ] https://design.ubuntu.com/apps/get-started/overview returned HTTP 525
      (SSL/connection failure). Ubuntu design guidelines are not included in
      the comparison.

- [ ] https://designguidelines.co/ returned a 404 "not found" page. The
      Design Guidelines.co curation site is no longer hosting content and is
      not included in the comparison.

- [ ] https://usabilitypost.com/archive/ returned an index of article titles
      but individual article URLs returned only a "blog is in hiatus" notice
      with no body. Usability Post claims could not be extracted.

- [ ] https://www.usability.gov/ legacy deep URLs (e.g.
      `/what-and-why/usability.html`, method pages) all redirect to the single
      homepage; only homepage content was retrievable.

- [ ] https://design.google/library/ returned an empty page and several
      article URLs returned 404; only the homepage feed of one-line article
      blurbs was retrievable.

- [ ] `__TODO__/015/ui/` and `__TODO__/015/ui2/` are empty directories;
      nothing to extract.