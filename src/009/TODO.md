# TS-9 drift: commit types in `.pre-commit-config.yaml` enforcement

Findings from auditing every `.pre-commit-config.yaml` under
`~/dev/personal/kieranpotts/*` against the eleven core revision types defined
in [04-commits.adoc](./04-commits.adoc) — `feature`, `runtime`, `fix`, `step`,
`refactor`, `style`, `maintenance`, `chore`, `release`, `merge`, `revert`.

Scope: commit-*type* vocabulary only. (Version pinning, header-length
enforcement, and flag-syntax enforcement were also reviewed but are out of
scope for this note.)

## 1. `performance` vs `runtime` — shared hook is out of sync with TS-9 and with CI

`kieranpotts/pre-commit-hooks` (`hooks/validate_commit_message.py`, tag
`v0.2.0` — consumed by 28 repos) still lists `performance` in `VALID_TYPES`.
TS-9 renamed this type to `runtime` to cover the full set of dynamic quality
attributes (latency, availability, security, resilience, etc.), not just
performance. The hook's own docstring claims to implement "the allowed
revision types defined in TS-9," but doesn't.

The centrally-shared CI action, `kieranpotts/actions/validate-commit-messages`,
*was* updated and correctly enforces `runtime` (not `performance`). This means
the two enforcement points now disagree for all 28 repos that consume the
shared pre-commit hook:

- `performance: reduce query latency` — passes pre-commit, **fails CI**.
- `runtime: reduce query latency` (TS-9-correct) — **fails pre-commit**, passes CI.

**Action:** update `VALID_TYPES` in `pre-commit-hooks` to swap `performance` →
`runtime`, cut a `v0.3.0` release.

## 2. Stale `v0.1.0` pin — `ocean`, `website-ui`

Both repos are pinned two releases behind (`v0.1.0`). That version's
`VALID_TYPES` includes `format` where every other repo now has TS-9's
`style`. No `format:`/`style:` commit has landed in either repo yet, so this
hasn't caused a rejected commit — but it's the same class of problem as (1),
latent until someone makes a style-only commit.

**Action:** bump both repos to the release that fixes (1).

**Decision:** This can be ignored because ocean and website-ui are archived
repositories anyway.

## 3. Extension vocabulary added by repository-specific hooks

Ten repos bypass the shared hook with a local `repo: local` hook so they can
extend the type vocabulary with repository-specific prefixes (`garden` also
does this, but with its own gardening-metaphor verb set, and is out of scope
for this section). Deduplicated across those ten repos, the extension
vocabulary is eighteen words, and it falls into three recurring patterns
rather than being ad hoc per repo:

| Extension | Used in | Marks | Pattern |
|---|---|---|---|
| `add` | `bookmarks`, `cheats`, `standards` | new content introduced | TS-9 alternative type (content-kind) |
| `edit` | `bookmarks`, `cheats`, `standards` | existing content improved | TS-9 alternative type (content-kind) |
| `delete` | `bookmarks`, `cheats`, `standards` | content removed | TS-9 alternative type, **named `remove` in TS-9** — see note below |
| `report` | `risks` | a threat-modeling workshop report | subject-matter (document-kind) |
| `register` | `risks` | an update to the living risk register | subject-matter (document-kind) |
| `plan` | `plans` | a delivery plan document change | subject-matter (document-kind) |
| `audit` | `audits` | an architecture audit report | subject-matter (document-kind) |
| `design` | `design` | a design documentation change | subject-matter (document-kind) |
| `rfc` | `rfc` | an RFC document change | subject-matter (document-kind) |
| `epic` | `specs` | scaffolding a new epic proposal | subject-matter (document-kind) |
| `quality` | `specs` | a non-functional-requirement proposal | subject-matter (document-kind) |
| `draft` | `rfc`, `thoughts` | a document put into draft | lifecycle-stage |
| `propose` | `rfc` | a draft taken out of draft, ready for review | lifecycle-stage |
| `accept` | `rfc` | a proposal approved by stakeholders | lifecycle-stage |
| `reject` | `rfc` | a proposal not approved | lifecycle-stage |
| `implement` | `rfc` | tooling/infrastructure for an accepted RFC now built | lifecycle-stage |
| `supersede` | `rfc` | a prior decision replaced by a newer one | lifecycle-stage |
| `publish` | `thoughts` | a draft made public | lifecycle-stage |

Three patterns account for all eighteen words:

1. **`add` / `edit` / `delete`** (`bookmarks`, `cheats`, `standards`) map
   directly onto TS-9's alternative revision-type set for non-code repos
   (§Alternative revision types in [04-commits.adoc](./04-commits.adoc)) —
   except that TS-9 names the third type **`remove`**, and all three repos
   independently chose `delete` instead. This is the one place these
   extensions actually drift from TS-9's own vocabulary rather than just
   extending it.

2. **Subject-matter types** (`report`, `register`, `plan`, `audit`, `design`,
   `rfc`, `epic`, `quality`) each name the *kind of document* a commit
   touches, rather than the *kind of change* TS-9's core types describe. Each
   is scoped to exactly one repo and doesn't overlap with any other
   repository's vocabulary — no cross-repo drift here, just eight
   repo-local nouns standing in for a generic `feature`/`add`-style commit.

3. **Lifecycle-stage types** (`draft`, `propose`, `accept`, `reject`,
   `implement`, `supersede`, `publish`) mark a document's progress through a
   workflow rather than a change to its content. Six of the seven live in
   `rfc` alone, mirroring that repo's `draft-rfc` → `propose-rfc` →
   `accept-rfc`/`reject-rfc` → `implement-rfc` → `supersede-rfc` skill
   sequence one-for-one. `thoughts` reuses `draft` and adds its own
   `publish` for the same kind of stage-marking. These are the extension
   type with the least resemblance to anything in TS-9's core or
   alternative type lists — TS-9 has no concept of a lifecycle-stage commit
   type at all, only content-kind ones.

## Suggested next steps

1. Fix `pre-commit-hooks` (`performance` → `runtime`), release `v0.3.0`.
2. Rename `delete` → `remove` in `bookmarks`, `cheats`, and `standards` to
   match TS-9's alternative-type vocabulary — or document `delete` as an
   accepted house synonym in TS-9 itself.
3. Consider whether the lifecycle-stage pattern (`draft`/`propose`/`accept`/
   `reject`/`implement`/`supersede`/`publish`) is common enough across repos
   to warrant its own note in TS-9, given it's a distinct, recurring idiom
   that TS-9 doesn't currently describe.

## 4. Proposal: extend TS-9 with governance-document lifecycle types

The variation catalogued in §3 creates real development/operations friction —
every governance-style repo has independently invented its own commit-type
vocabulary, so the meaning of a `git log --oneline` prefix isn't portable
between repos the way TS-9 intends. The eighteen extension words split into
two problems that need different fixes, not one:

### 4.1 Subject-matter nouns should NOT become new TS-9 types

`report`, `register`, `plan`, `audit`, `design`, `rfc`, `epic`, `quality` each
name *what kind of document* changed, not *what kind of change* happened —
a different axis from every type TS-9 already defines. `feature`/`fix`/
`refactor`/etc. all describe the change; the artifact is inferred from the
diff, the repo, or a footer. If TS-9 grows a new type every time a repo
introduces a new document kind, the vocabulary never stops growing — that's
the friction this proposal is meant to eliminate, not encode. Recommendation:
retire these eight in favor of TS-9's existing generic types — mostly `add`/
`edit` — with the document kind left to context (repo identity, path,
`Refs:` footer). `risks`' `update-register` skill already models this
correctly in spirit: "mark TA1 mitigated" is just an edit; it doesn't need
its own type.

### 4.2 Lifecycle-stage words are a genuine gap, worth adding

`draft`, `propose`, `accept`, `reject`, `implement`, `supersede`, `publish`
describe a governance state-transition — independent of diff content — that
TS-9 has no vocabulary for at all today. This isn't only visible in the
pre-commit hooks: the repository's own skill set already encodes a consistent
six-stage lifecycle across six document families (rfc, spec, design, plan,
report, audit) — draft → propose → accept/reject → complete/implement/release
→ supersede, with `plan` adding an `abandon` off-ramp. The hooks simply
haven't caught up to what the skills already assume.

Proposed minimal set — six new types, following the vocabulary the skills
already converged on independently:

| New type | Marks | Precedent in skills |
|---|---|---|
| `draft` | a new proposal/document opened, not yet ready for review | `draft-rfc`, `draft-spec`, `draft-design`, `draft-plan`, `draft-report`, `draft-audit` |
| `propose` | draft taken out of draft, ready for stakeholder review | `propose-rfc`, `propose-spec`, `propose-plan` |
| `accept` | reviewers approve the proposal | `accept-rfc`, `accept-spec` |
| `reject` | reviewers do not approve it | `reject-rfc`, `reject-spec` |
| `complete` | the decision has been realized and the record lands in `main` | `complete-audit`, `complete-design`, `complete-plan`, `complete-report`, `complete-rfc`, `release-spec` |
| `supersede` | a previously-completed decision is retired in favor of a newer one | `supersede-rfc`, `supersede-spec` |

Two folding decisions still open:

- **`publish` (thoughts) → `complete`.** A lightweight, blog-style repo
  collapses draft→review→ship into draft→publish; `complete` already means
  "this document's content is now live/real" for every other repo, so
  `publish` doesn't need to survive as its own word.
- **`abandon` (plans) → `reject`.** Both mean "this doesn't happen," just at
  different points in the timeline (reject = at the review gate, abandon =
  mid-flight after acceptance). Folding keeps the set at six instead of
  seven; keeping them separate preserves the timing distinction. Judgment
  call, no strong preference either way yet.

### 4.3 Net effect on the eighteen words

- `add` / `edit` / `delete` — kept, as TS-9's existing alternative types
  (fixing `delete` → `remove` per §3.1).
- `report`, `register`, `plan`, `audit`, `design`, `rfc`, `epic`, `quality` —
  retired, replaced by `add`/`edit` + context.
- `draft`, `propose`, `accept`, `reject`, `implement`, `supersede`, `publish`
  — consolidated into six new types (`draft`, `propose`, `accept`, `reject`,
  `complete`, `supersede`).

### 4.4 Where this lives in TS-9

Frame the six new types as a **third revision-type list** in
[04-commits.adoc](./04-commits.adoc), alongside the existing "core" (code
repos) and "alternative" (generic content repos) lists — scoped specifically
to governance/decision documents (RFCs, specs, design docs, plans, workshop
reports, audits). They wouldn't make sense applied to, say, `bookmarks` or
`garden`, so they shouldn't be folded into either existing list.

**Status:** proposal for discussion — not yet drafted into
`04-commits.adoc`. Superseded by the decision in §5, below.

## 5. Decision: consolidate on `create` / `update` / `delete`

Rather than the six-type lifecycle list proposed in §4, the call is to go
smaller: three CRUD types, replacing TS-9's existing alternative-type triad
(`add`/`edit`/`remove`) rather than sitting alongside it. Lifecycle *stage*
(draft/proposed/accepted/rejected/shipped) is left to structural state that
GitHub already tracks — draft PR, requested reviewers, merged vs.
closed-unmerged — and to the document's own front matter/status field,
rather than being re-encoded a second time in the commit type. The commit
type answers one question only: was a document created, changed, or
removed.

This also resolves the `delete`-vs-`remove` naming drift flagged in §3.1 for
free: the new canonical word is `delete`, which is what three of the repos
were already using.

`garden` remains excluded from this exercise, per the original scoping —
its gardening-metaphor verbs aren't part of this consolidation.

### 5.1 Mapping: old types → new types

| Old type(s) | Used in | New type | Why |
|---|---|---|---|
| `add` | `bookmarks`, `cheats`, `standards` | `create` | direct CRUD equivalent |
| `edit` | `bookmarks`, `cheats`, `standards` | `update` | direct CRUD equivalent |
| `delete` | `bookmarks`, `cheats`, `standards` | `delete` | already the canonical word |
| `report` | `risks` | `create` / `update` | new workshop report → `create`; amendments → `update` |
| `register` | `risks` | `update` | almost always an edit to the existing living register |
| `plan` | `plans` | `create` / `update` | new plan → `create`; revisions → `update` |
| `audit` | `audits` | `create` / `update` | new audit report → `create`; revisions → `update` |
| `design` | `design` | `create` / `update` | new design doc → `create`; revisions → `update` |
| `rfc` | `rfc` | `create` / `update` | new RFC → `create`; revisions → `update` |
| `epic` | `specs` | `create` | scaffolds a new proposal document |
| `quality` | `specs` | `create` | scaffolds a new proposal document |
| `draft` | `rfc`, `thoughts` | `create` | the document starts existing |
| `propose` | `rfc` | `update` | status change on an existing document |
| `accept` | `rfc` | `update` | status change on an existing document |
| `reject` | `rfc` | `update` | status change on an existing document (doc is kept, marked rejected) |
| `implement` | `rfc` | `update` | status change on an existing document |
| `supersede` | `rfc` | `update` | status change on an existing document |
| `publish` | `thoughts` | `update` | status change on an existing document |
| `abandon` | `plans` (skill-level, not yet in a hook) | `update` | status change; the plan document is kept as a record, not deleted |

Net result: TS-9's alternative revision-type list becomes `create` /
`update` / `delete` (three words, same size as today's `add`/`edit`/
`remove`), and every repo currently using a `repo: local` hook — `risks`,
`plans`, `bookmarks`, `audits`, `design`, `rfc`, `thoughts`, `cheats`,
`specs`, `standards` — can drop its local hook and local CI workflow
override entirely, going back to consuming the shared `pre-commit-hooks`
hook and the shared `validate-commit-messages` CI action like every other
repo in §1.

**Status:** decided direction. Next steps: update
[04-commits.adoc](./04-commits.adoc)'s alternative revision-type list, then
retire the eleven local hooks/workflow overrides listed in §3 in favor of
the shared ones (once §1's `performance`→`runtime` fix has also landed).
