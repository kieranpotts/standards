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
