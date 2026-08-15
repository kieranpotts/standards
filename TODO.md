# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-15**, immediately after a
full user-driven decision sweep worked through every one of the 79
`## Out-of-scope` items that were awaiting a human confirm/overrule decision
across TS-39, TS-16, TS-43, TS-27, TS-33, TS-26, TS-40, TS-15, and TS-18 (see
the previous regeneration's total). Every item was individually confirmed or
overruled by the user; **none remain undecided.** The sweep's decisions
substantially changed the shape of what's open in this repository — several
confirmed exclusions were routed as new Missing items into other standards
(some into a brand-new TS-19 `GAPS.md`, since TS-19 had none before today),
a handful of overrules were concrete enough to file as ready-to-action
Missing items, and several broader overrules were recorded as pending
scope-broadening decisions for their standard (not yet formalized via RFC or
written into any overview text), and two overrules were held pending
possible brand-new standards not yet created. See
[Out-of-scope sweep, 2026-08-15](#out-of-scope-sweep-2026-08-15) for the full
account.

Re-derive the counts with the script in
[Regenerating this file](#regenerating-this-file) before trusting them after
any content work.

## Stub standards

These pages have no substantive content yet — just a heading, `// TODO`
placeholder(s), and no `include::partial$NNN/...[]` includes.

No standard is currently in this state. TS-39 (HTML) was the last remaining
stub, authored from scratch on 2026-08-14. This table has been empty since
that run.

TS-47 (Dates and times) also has no `include::partial$` directive, but is not
a stub: its page carries the standard's content directly, monolithically,
rather than via the `partials/NNN/` pattern. The mechanical check in
[Regenerating this file](#regenerating-this-file) flags it as a false
positive — verify by reading the page before trusting the grep alone.

## Open gap analyses

TS-19 (SEO) gained a `GAPS.md` for the first time today, created purely to
receive items routed in from other standards' Out-of-scope reviews — it has
not had a `gap-analysis` run of its own. Forty-two standards now have a
`GAPS.md`.

### The two GAPS.md formats

The files are in two formats, and the columns mean different things in each.

- **Template format** (39 files). Follows the `gap-analysis` skill's bundled
  template: flat `- [ ]` checklists under `## Missing`, `## Partial`,
  `## Out-of-scope`, and `## Unresolved` headings.

- **Legacy format** (3 files: TS-6, TS-38, TS-44, all fully resolved). One
  `## <gap title>` subsection per gap, with `**Source**` /
  `**What the source says**` / `**Coverage check**` / `**Gap**` bullets,
  closed by appending a `**RESOLVED**` (or, in TS-38's case,
  `**RESOLVED.**` — the mechanical script only matches the bare form; see
  [Regenerating this file](#regenerating-this-file)) bullet. Some also carry
  a `**Cross-references**` field naming other standards the gap touches; the
  template format has no equivalent.

Legacy-format files are converted to the template format as they are worked,
not in a separate sweep.

### What the columns mean

- **Actionable** — `## Missing` plus `## Partial` items. Content that needs
  writing. This is the number to plan against. For legacy-format files it is
  every unresolved `## <gap title>` subsection, which mixes both kinds.

- **Scope** — `## Out-of-scope` items. Not authoring work: each is flagged
  for a human to confirm the exclusion or overrule it.

- **Unresolved** — `## Unresolved` items. Reference resources that could not
  be retrieved when the analysis ran, or open scope questions not yet
  settled by the user.

### Standards, ordered by actionable count

All nine standards worked in today's sweep now have actionable (Missing/
Partial) items, mostly from overrules that got routed in or written up. Two
other standards (TS-7, TS-14) also gained a new actionable item each, as the
destination of a routed overrule. TS-15 is the only standard with a
remaining open `## Out-of-scope` item — deliberately left undecided, not
overlooked (see the sweep account below).

| TS | Title | Actionable | Scope | Unresolved | Notes |
| --- | --- | ---: | ---: | ---: | --- |
| [TS-18](src/modules/ROOT/partials/018/GAPS.md) | Web GUIs | 11 | 0 | 0 | All 26 Out-of-scope items decided 2026-08-15. 11 new Missing items: 4 bundled as a pending security-pillar scope-broadening decision (XSRF/MITM/XSS/Bearer auth), 4 bundled as a pending architecture scope-broadening decision (client architecture/SPA frameworks/PWA/microfrontends), 1 with its TS-18-vs-TS-37 placement still undecided (DOM/scripting/fetch), and 4 concrete write-ups (push notifications, responsive design, browser support policy, feature detection/polyfilling, DevTools profiling — see per-item detail in `GAPS.md`). 1 item reframed rather than simply accepted (WCAG AA restated as a floor, with 3 AAA items added as stretch goals). 5 items routed out to TS-19, TS-14 (×1, joining an earlier TS-39 routing), and TS-15 (×2). 1 item held pending a possible new internationalization standard. 1 item held pending a possible TS-19 content-strategy expansion. |
| [TS-26](src/modules/ROOT/partials/026/GAPS.md) | Technical writing style guide | 5 | 0 | 0 | All 5 Out-of-scope items decided 2026-08-15. 3 routed in from TS-27 (Google Developer Documentation Style Guide capitalization/process items). 2 overruled and written up directly (general English grammar; Latin/biological/music/biblical referencing conventions). 2 of TS-26's own original items routed out to TS-19 (content strategy, web-scannability/SEO heuristics); 1 confirmed out-of-scope with no routing target (O'Reilly publisher-specific workflow). |
| [TS-19](src/modules/ROOT/partials/019/GAPS.md) | SEO | 3 | 0 | 0 | New `GAPS.md`, created 2026-08-15 purely to receive routed items — no `gap-analysis` run of its own yet. 2 items from TS-26 (content strategy/SEO material, web-scannability tactics), 1 from TS-18 (SEO). |
| [TS-15](src/modules/ROOT/partials/015/GAPS.md) | User interfaces | 5 | 1 | 0 | 6 of 7 Out-of-scope items decided 2026-08-15; the 7th (design.google project-narrative essays) deliberately left open pending a future fetch-and-assess pass — not overlooked. 3 items overruled and written up directly (trust/relationship principle from IBM's "Build Bonds"; AI-experience design section; a full "User research" section). 2 items routed in from TS-18 (website-audit checklists; neurodivergent-persona UX research). 2 of TS-15's own original items routed out to TS-18 (Windows-specific app design; Shopify Polaris design-system mechanics). |
| [TS-40](src/modules/ROOT/partials/040/GAPS.md) | CSS | 3 | 0 | 0 | All 12 Out-of-scope items decided 2026-08-15. 8 bundled as a pending scope-broadening decision (would add CSS syntax formatting, comment/documentation conventions, property/technique reference material, performance/tooling, and legacy-IE content — all currently excluded by `01-overview.adoc`'s explicit stated scope). 2 overruled and written up directly (an app-namespace class-prefix heuristic; a `js-` JS-hook-class prefix convention). 1 confirmed and routed out to TS-18 (living style guides/pattern libraries). 1 confirmed plain (Painless CSS's SEO/learning-advice mistakes). |
| [TS-14](src/modules/ROOT/partials/014/GAPS.md) | Performance testing | 2 | — | — | Was fully resolved (0/0/0/0) before today. Gained 2 new Missing items, both routed in from other standards' Out-of-scope reviews: CI/Axe accessibility-testing tooling (from TS-39) and the assistive-technology test matrix/audit process (from TS-18) — both fit TS-14's existing `06-accessibility-testing.adoc`. |
| [TS-16](src/modules/ROOT/partials/016/GAPS.md) | Command line interfaces (CLIs) | 1 | 0 | 0 | All 9 Out-of-scope items decided 2026-08-15. 1 overruled and written up directly (a new "Terminology" section for terminal/shell/tty/console definitions). 1 overruled but left unrouted — the user floated that open-source project process (licensing, contribution guidelines, code of conduct, plugin systems) may need a whole new standard, not yet created. 7 confirmed plain. |
| [TS-7](src/modules/ROOT/partials/007/GAPS.md) | Code design | 1 | — | — | Was fully resolved before today. Gained 1 new Missing item, routed in from TS-33's Out-of-scope review: design-level thread-safety guidance, matching TS-33's own documented deferral of concurrency to TS-7. |
| [TS-43](src/modules/ROOT/partials/043/GAPS.md) | Relational databases and SQL | 0 | 6 | 0 | All 6 Out-of-scope items decided 2026-08-15. 5 overruled but held — the user decided DBA/database-administration operations (MySQL installation, user/permission administration, table maintenance, backup/restore, client CLI operation) warrant a dedicated new standard, not yet created; these stay unticked in `GAPS.md` pending that. 1 confirmed plain (the empty schema-less stub). |
| [TS-27](src/modules/ROOT/partials/027/GAPS.md) | Markdown | 0 | 0 | 0 | All 6 Out-of-scope items decided 2026-08-15 — fully resolved. 3 confirmed and routed out to TS-26 (Google Developer Documentation Style Guide process/capitalization material). 3 confirmed plain (document-layout/`[TOC]` scope disagreements; the original 2004 Markdown.pl spec). |
| [TS-33](src/modules/ROOT/partials/033/GAPS.md) | Java | 0 | 0 | 0 | All 3 Out-of-scope items decided 2026-08-15 — fully resolved. 1 overruled but held (Kotlin nullability comparison — the user does not want it folded directly into TS-33, and no Kotlin/JVM-ecosystem standard exists yet to route it to). 1 confirmed and routed out to TS-7 (thread-safety design guidance, matching TS-33's documented deferral). 1 confirmed plain (Oracle Code Conventions' contextual introduction; citation kept as-is). |
| [TS-39](src/modules/ROOT/partials/039/GAPS.md) | HTML | 0 | 0 | 0 | All 5 Out-of-scope items decided 2026-08-15 — fully resolved. 2 confirmed and routed out (Semantic Web/RDFa background to TS-18, with a TS-19 cross-reference noted; CI/Axe accessibility-testing tooling to TS-14). 3 confirmed plain. |
| | **Total** | **30** | **7** | **0** | |

Every other standard with a `GAPS.md` (30 of the 42) is fully resolved: zero
unchecked items of any kind. That list is unchanged by today's sweep except
where noted above — see [Regenerating this file](#regenerating-this-file) to
re-derive it.

## Out-of-scope sweep, 2026-08-15

At the user's request, every one of the 79 `## Out-of-scope` items open
across TS-39, TS-16, TS-43, TS-27, TS-33, TS-26, TS-40, TS-15, and TS-18 (as
tallied by the previous regeneration of this file) was walked through
individually — one item at a time, each requiring an explicit confirm-the-
exclusion or overrule-it decision from the user. All 79 are now decided; the
per-standard "Notes" column above summarizes each standard's outcome, and
each standard's own `GAPS.md` carries a dated resolution note against every
item. No item was left ambiguous, though a deliberate minority were left
*open* by design — see the four dispositions below.

Four kinds of disposition came out of the sweep, beyond plain confirm/deny:

- **Concrete overrules, written up as new Missing items.** Where the
  overrule was a specific, scoped piece of content (e.g. TS-16's new
  Terminology section, TS-40's app-namespace and `js-` prefix conventions,
  TS-15's trust/relationship principle and AI-experience section, TS-26's
  general-grammar and specialized-referencing content, TS-18's push-
  notifications/responsive-design/browser-support-policy/feature-detection/
  DevTools-profiling sections), it was filed directly as a new `## Missing`
  item in the standard's own `GAPS.md`, ready for a future `close-gaps` run.

- **Routed overrules, filed against a different standard.** Where the user
  agreed content didn't belong in the standard that flagged it but did
  belong somewhere else, it was filed as a new `## Missing` item in the
  *other* standard's `GAPS.md`, with a note explaining where it came from
  and why. This is how TS-19 gained its first-ever `GAPS.md` today (2 items
  from TS-26, 1 from TS-18), and how TS-7 and TS-14 — both previously fully
  resolved — each gained a new item from TS-33 and from TS-39/TS-18
  respectively.

- **Pending scope-broadening decisions, held without formalizing.** Several
  overrules amounted to redefining a published standard's stated scope —
  TS-40 covering CSS syntax formatting/tooling/property-reference material
  it currently explicitly excludes, and TS-18 gaining a fourth "security"
  pillar plus reversing its documented deferral of application architecture
  to TS-5. In both cases the user confirmed the direction but explicitly
  asked to record the decision *without* yet formalizing it — no RFC drafted,
  no `01-overview.adoc` edited. These items are ticked `[x]` in `GAPS.md`
  (the confirm/overrule decision is made) but their content is not written,
  and each carries a note flagging it as part of a pending bundle. Treat
  these as decided-but-not-yet-actioned, distinct from a normal open Missing
  item — the standard's own overview text still says the old thing until a
  deliberate follow-up (likely via `draft-rfc`) changes it.

- **Held pending a possible new standard, not yet created.** Three overrules
  concluded that no existing standard is a good home for the content, and
  that a brand-new standard might be warranted: DBA/database-administration
  operations (5 items, from TS-43), open-source project process — licensing,
  contribution guidelines, code of conduct, plugin systems (1 item, from
  TS-16), and internationalization (1 item, from TS-18). None of these three
  candidate standards has been created. The items stay ticked `[x]` in their
  originating `GAPS.md` with a note explaining the hold, but are not filed
  as Missing items anywhere, since there is nowhere to file them yet.

One item was deliberately left **undecided** rather than forced into any of
the above: TS-15's design.google project-narrative essays. The user judged
that the homepage blurbs alone don't carry enough to extract a principle
from, and asked for the actual linked essays to be fetched and reassessed in
a future pass before a real decision is made. This is the one remaining
open `## Out-of-scope` item in the repository (see the table above) — a
conscious placeholder, not an oversight.

One further item (TS-18's WCAG Level AAA material) was **reframed** rather
than simply confirmed or overruled: instead of choosing between "TS-18 stays
AA-only" and "TS-18 becomes AAA", the user asked for TS-18 to state AA as a
*minimum*, with the three AAA items added as stretch guidance above that
floor — filed as a single concrete Missing item accordingly.

## Standards with neither a stub nor a GAPS.md

TS-1, TS-17, TS-22, TS-24, TS-28, TS-30, TS-32, TS-34, TS-35, TS-42, TS-45,
TS-47, TS-51, TS-53, TS-55, TS-56, TS-58, TS-59, TS-60, TS-62, and TS-63 all
have substantive content and no recorded gap analysis. TS-19 has dropped off
this list as of 2026-08-15's sweep, since it now has a `GAPS.md` (see above)
— though that file exists only to receive routed items, not because a
`gap-analysis` was run against TS-19 itself. A gap analysis (`/gap-analysis`)
could be run against any standard on this list; none is known to be missing
content today.

## Known inconsistencies

Surfaced on 2026-08-13 while writing the `close-gaps` skill, and added to
since. These are repo-level decisions and defects, not gap-closing work, but
the first two govern how all new content should be written.

- **The stub-detection script has a false positive.** `grep -L
  'include::partial\$'` also matches TS-47 (Dates and times), whose page
  carries its content monolithically rather than via `partials/NNN/`
  includes. TS-47 is complete, not a stub. Re-verify by reading the page,
  not just the grep result, whenever this script's stub list changes.

- **Reference lists in a trailing partial.** `docs/style-guide.md` (lines
  150–153) says a reference list MUST NOT be split into a separate partial.
  Eight standards do exactly that: TS-17, TS-18, TS-21, TS-23, TS-29, TS-31,
  TS-32, and TS-33. Twenty-three pages carry a `== References` section.

- **DECLINED — TS-40's methodology-comparison gap.** A `close-gaps` run on
  2026-08-14 closed 16 of TS-40's 17 actionable items. The remaining one
  proposed expanding `01-overview.adoc` into a comparative summary of
  OOCSS/BEM/SMACSS/SUIT CSS; declined as borderline and left open with a
  dated rationale note. Superseded in practice by 2026-08-15's broader
  pending scope-broadening decision for TS-40 (see the sweep account above),
  which would touch the same overview section if formalized.

- **The legacy-format script has one known false negative.** It matches the
  literal string `**RESOLVED**`, but TS-38's `GAPS.md` closes its one gap
  with `**RESOLVED.**` (the period sits inside the bold markup, not after
  it) — the only file in the repository written that way. The script
  reports TS-38 as `actionable=1` even though the gap is genuinely closed;
  verify any legacy file the script reports as non-zero by reading it
  before trusting the count.

- **Do not conclude a local `__TODO__/` reference is permanently gone from a
  Git-scoped search alone.** `~/local.gitignore` (a global, machine-level
  gitignore) hides the entire `__TODO__/` tree from `git status`, `git log
  --all`, and any other Git-aware search, even though the tree is fully
  present and readable on disk. Always additionally check with a plain
  filesystem `find` (not `git`-scoped) before recording a local reference as
  unrecoverable. Discovered 2026-08-15; see this file's own version history
  for the full account of standards affected.

Earlier entries in this section — covering broken cross-references, dropped
`include::` directives, markdown-vs-AsciiDoc bold-markup cleanup,
self-referencing xrefs, comma-in-heading xref parsing, TS-9's formatting
defects, and TS-16/TS-27/TS-33/TS-37/TS-38/TS-43/TS-44's individual
`close-gaps` histories — are resolved and have been trimmed from this file;
consult Git history or each standard's own `GAPS.md` for the detail.

## Regenerating this file

Run from `src/modules/ROOT/partials/`:

```sh
for d in $(ls -d [0-9][0-9][0-9]/ | sort); do
  n="${d%/}"; g="$n/GAPS.md"; [ -f "$g" ] || continue
  if grep -q '^## Missing$' "$g"; then
    awk -v n="$n" '
      /^## /   { s = substr($0, 4) }
      /^- \[ \]/ { c[s]++ }
      END { printf "%s template actionable=%d scope=%d unresolved=%d\n",
              n, c["Missing"] + c["Partial"], c["Out-of-scope"],
              c["Unresolved"] }' "$g"
  else
    awk -v n="$n" '
      /^## /            { total++; resolved_here = 0 }
      /\*\*RESOLVED\*\*/ { if (!resolved_here) { done++; resolved_here = 1 } }
      END { printf "%s legacy actionable=%d\n", n, total - done }' "$g"
  fi
done
```

**Do not stop at the per-standard `actionable=`/`scope=`/`unresolved=`
breakdown above.** Also run a plain total-unchecked count per file —
`grep -c '^- \[ \]' <NNN>/GAPS.md` — and compare it against
`actionable + scope + unresolved` for that same file. A mismatch means the
per-heading `awk` count and the flat count disagree, which usually means a
checklist item exists outside the four recognized `## ` headings, or that a
heading name was typo'd, **or that an edit intended to tick an item silently
failed to apply** — this is exactly how a stray unticked pair of TS-39
Out-of-scope items was caught during this file's 2026-08-15 regeneration,
after being missed by an editing pass that believed it had ticked them.
Trust the grep over any standard's own narrative Status line, and re-run the
grep after every batch of edits, not just once at the end.

Stub standards are those whose page has no `include::partial$` directive:

```sh
grep -L 'include::partial\$' src/modules/ROOT/pages/[0-9][0-9][0-9].adoc
```

This grep has one known false positive — TS-47, whose content is written
directly on the page rather than via partials. Verify each hit by reading the
page before adding it to the stub table: a stub has a `// TODO` placeholder
and essentially no prose; a false positive like TS-47 has complete sections.

A standard is "fully resolved" when its `GAPS.md` has zero unchecked items of
*any* kind — `grep -c '^- \[ \]'` returns 0 — not merely zero actionable
items. TS-15 is the current example that makes this distinction matter: it
has 5 actionable items and 1 deliberately-open Out-of-scope item, so it
belongs in the open-items table for both reasons.

The legacy-format script also has one known false negative: it matches the
literal string `**RESOLVED**`, but TS-38's `GAPS.md` closes its one gap with
`**RESOLVED.**` (the period sits inside the bold markup, not after it) — the
only file in the repository written that way. The script reports TS-38 as
`actionable=1` even though the gap is genuinely closed; verify any legacy
file the script reports as non-zero by reading it before trusting the count,
the same caution the script's template branch already needs for its
Out-of-scope/Unresolved blind spots.

**To find standards with substantive content but no gap analysis**, diff the
standards that have a page against the standards that have a `GAPS.md`:

```sh
ls src/modules/ROOT/pages/[0-9][0-9][0-9].adoc | xargs -n1 basename | sed 's/\.adoc//' | sort > /tmp/all_ts.txt
ls src/modules/ROOT/partials/*/GAPS.md | sed -E 's#.*partials/([0-9]+)/GAPS.md#\1#' | sort > /tmp/gaps_ts.txt
comm -23 /tmp/all_ts.txt /tmp/gaps_ts.txt
```

Cross-check the result against the stub list — a standard in both is a stub
awaiting authorship, not a candidate for `gap-analysis`. Re-run this diff
every time, rather than trusting the previous run's list by hand — TS-19
dropped off it today only because a `GAPS.md` was created to receive routed
items, not because a real gap analysis was run against TS-19 itself; don't
mistake the file's existence for that having happened.

**Do not conclude a local `__TODO__/` reference is permanently gone from a
Git-scoped search alone.** `~/local.gitignore` (a global, machine-level
gitignore) hides the entire `__TODO__/` tree from `git status`, `git log
--all`, and any other Git-aware search, even though the tree is fully
present and readable on disk. Always additionally check with a plain
filesystem `find` (not `git`-scoped) before recording a local reference as
unrecoverable.
