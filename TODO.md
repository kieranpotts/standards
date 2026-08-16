# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-16**, after the user
confirmed TS-40's last open item — the OOCSS/BEM/SMACSS/SUIT CSS
methodology-comparison gap, declined as scope creep on 2026-08-14 — should
be marked closed rather than left standing as a pending decision. TS-40 now
has 0 unchecked items of any kind and has left the table below. It is worth
noting this is a narrower kind of "resolved" than most rows that leave this
table: TS-40 still carries 10 Out-of-scope items ticked-but-held against an
unformalized scope-broadening RFC (see "Known inconsistencies" below) —
decided in direction, not yet written up. A `close-gaps` run cannot action
those; only that RFC can.

This follows two earlier batches the same day. The first: an eleventh
`close-gaps` run against TS-18 closed all 3 of its remaining Missing items
(the DOM/scripting/fetch/CORS split between TS-18 and TS-37, the Windows
app design confirmed-out-of-scope call, and the Shopify Polaris
design-token gap); that regeneration also found TS-7 and TS-16 — both
listed as having 1 open actionable item each as of the 2026-08-15
snapshot — were in fact already fully resolved as of 2026-08-15, neither
touched by that day's session, the previous snapshot simply gone stale.
The second: TS-40's 2 concrete Missing items (app-namespace prefix, `js-`
hook class), TS-25's 1 remaining Missing item (documentation review
etiquette), and TS-15's 1 deliberately-open Out-of-scope item (the
design.google fidelity-sequencing essay) were all closed. The table below
now reflects all of this plus today's final TS-40 item.

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

Forty-two standards have a `GAPS.md`. None currently carries an actionable,
scope, or unresolved open item — every one is at 0 unchecked items. TS-38
still shows `actionable=1` under the mechanical script alone, its known
false-negative (see below); reading the file confirms it is genuinely
closed.

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

No standard currently has an open actionable, scope, or unresolved item.
This table is empty for the first time since this file began being
tracked.

TS-14 (Performance testing) and TS-19 (SEO) left this table on 2026-08-15:
TS-14's 2 actionable items were both closed with new content; TS-19's 3
items were all withdrawn on inspection (see above). TS-7 (Code design) and
TS-16 (Command line interfaces) were discovered already fully resolved on
2026-08-16's regeneration — both were actually closed on 2026-08-15, but
the previous table snapshot hadn't caught up. TS-18 (Web GUIs) left the
table on 2026-08-16: its last 3 actionable items were closed by an
eleventh `close-gaps` run. TS-25 (Technical documentation) and TS-15 (User
interfaces) also left the table on 2026-08-16: TS-25's 1 remaining Missing
item (documentation review etiquette) was closed, and TS-15's 1
deliberately-open Out-of-scope item (the design.google essays) was
resolved via the fetch-and-reassess pass a prior run had deferred, finding
one genuine gap (design-process fidelity sequencing). TS-40 (CSS) left the
table last, also on 2026-08-16: its 2 concrete Missing items (app-namespace
prefix, `js-` hook class) were closed first, then its one remaining item —
the OOCSS/BEM/SMACSS/SUIT CSS methodology-comparison gap, already declined
on 2026-08-14 — was confirmed by the user as closed rather than left as a
standing decision. All seven are now fully resolved and appear in the
fully-resolved count below.

Every standard with a `GAPS.md` (all 42) is fully resolved: zero unchecked
items of any kind. TS-26 joined that list on 2026-08-15 — all of its
Missing items were either closed or routed to another standard's
`GAPS.md`, and no Out-of-scope items remain open. TS-14, TS-19, TS-7, and
TS-16 joined it the same day: TS-14 by closing its 2 remaining items with
new content; TS-19 by withdrawing all 3 of its routed-in items as not
genuinely SEO-specific; TS-7 and TS-16 by closing all of their remaining
items with new content. TS-18, TS-25, TS-15, and TS-40 joined it on
2026-08-16 (see above). TS-40's case is worth flagging on its own: it is
"fully resolved" by the flat-unchecked-count measure only — it still
carries 10 Out-of-scope items ticked-but-held against an unformalized
scope-broadening RFC (see "Known inconsistencies" below), decided in
direction but not yet actioned. Nothing in this file's counts distinguishes
that from a standard with no pending decisions at all; treat "fully
resolved" here as "no `close-gaps` work outstanding," not as "nothing left
to decide."

## Standards with neither a stub nor a GAPS.md

TS-1, TS-17, TS-22, TS-24, TS-28, TS-30, TS-32, TS-34, TS-35, TS-42, TS-45,
TS-47, TS-51, TS-53, TS-55, TS-56, TS-58, TS-59, TS-60, TS-62, and TS-63 all
have substantive content and no recorded gap analysis. A gap analysis
(`/gap-analysis`) could be run against any standard on this list; none is
known to be missing content today.

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

- **DECLINED, now closed — TS-40's methodology-comparison gap.** A
  `close-gaps` run on 2026-08-14 closed 16 of TS-40's 17 actionable items,
  declining the 17th — expanding `01-overview.adoc` into a comparative
  summary of OOCSS/BEM/SMACSS/SUIT CSS — as borderline scope creep, and
  left it unticked with a dated rationale note. A further run on
  2026-08-16 closed 2 more concrete, user-directed items filed by the
  2026-08-15 Out-of-scope sweep (app-namespace prefix, `js-` hook class).
  The same day, the user confirmed the declined item's checkbox should be
  ticked — the decision itself was never in question, only whether it
  counted as "closed" — so TS-40's `GAPS.md` now has 0 unchecked items.
  No content changed as a result; `01-overview.adoc` still just names the
  methodologies and links them in References. This item is superseded in
  practice by TS-40's broader pending scope-broadening decision (see the
  next entry), which would touch the same overview section if formalized —
  that decision remains unformalized and is tracked separately via the 10
  ticked-but-held Out-of-scope items, not this one.

- **UNFORMALIZED — TS-40's scope-broadening decision.** On 2026-08-15 the
  user directed TS-40 (CSS) to broaden beyond its stated three concerns
  (architecture/naming methodology, excluding syntax formatting,
  performance/tooling, and workflow) to also cover CSS syntax formatting
  and act as a general property/technique reference — a redefinition of a
  published standard's scope that would normally go through an RFC. The
  decision was recorded rather than formalized: 10 items in TS-40's
  `GAPS.md` `## Out-of-scope` section are ticked `[x]` with a
  "**Overruled, pending a scope-broadening RFC**" note apiece, but no RFC
  has been drafted and `01-overview.adoc`'s stated scope is unchanged.
  Because those items are ticked, TS-40's `GAPS.md` reads as fully
  resolved by the flat-unchecked-count measure (see above) — this entry is
  the record that "fully resolved" here means "no `close-gaps` work
  outstanding," not "no decision outstanding." Drafting the RFC (`/rfc`)
  is the next step if this is to be formalized; until then, treat TS-40's
  syntax-formatting/property-reference expansion as decided-but-inert.

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
failed to apply**. Trust the grep over any standard's own narrative Status
line, and re-run the grep after every batch of edits, not just once at the
end.

Note that a standard can show `scope > 0` while its flat unchecked-count is
`0` — TS-43 is the current example. Its 6 held Out-of-scope items (pending a
possible new DBA/database-administration standard) are ticked `[x]` with a
note explaining the hold, per the "held pending a possible new standard"
disposition from the 2026-08-15 Out-of-scope sweep: decided, but not yet
actionable anywhere. That is different from a *genuinely* unticked
Out-of-scope item, still awaiting a decision — TS-15's one item was the
example of this until it was resolved on 2026-08-16 (see above). Only a
genuinely unticked item belongs in the open-items table for the "scope"
reason; a ticked-but-held item does not, since the per-heading `awk` script
above only counts `- [ ]` lines regardless of which disposition ticked the
others. No standard currently has a genuinely-unticked Out-of-scope item;
watch for the next one to use as the live example here.

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
items. TS-15 was the example that made this distinction matter until
2026-08-16: for a time it had 0 actionable items and 1 deliberately-open
Out-of-scope item, so it still belonged in the open-items table despite
having no content work left, until that one item was itself resolved (see
above). Watch for a standard in the equivalent state to use as the live
example here.

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
every time, rather than trusting the previous run's list by hand.

**Do not conclude a local `__TODO__/` reference is permanently gone from a
Git-scoped search alone.** `~/local.gitignore` (a global, machine-level
gitignore) hides the entire `__TODO__/` tree from `git status`, `git log
--all`, and any other Git-aware search, even though the tree is fully
present and readable on disk. Always additionally check with a plain
filesystem `find` (not `git`-scoped) before recording a local reference as
unrecoverable.
