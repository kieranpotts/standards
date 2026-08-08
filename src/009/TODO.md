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

## 3. Repository-specific hooks: coverage against the 11 core types

Eleven repos bypass the shared hook with a local `repo: local` hook so they
can extend the type vocabulary with repository-specific prefixes. Each is
internally consistent (local pre-commit hook and local CI workflow override
agree with each other), but each also narrows or renames TS-9's core set.

| Repository | Core types kept | Extensions added | Core types NOT covered |
|---|---|---|---|
| `risks` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style` | `report`, `register` | `feature`, `runtime`, `step`, `release`, `merge` |
| `plans` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style` | `plan` | `feature`, `runtime`, `step`, `release`, `merge` |
| `garden` | `chore`, `maintenance`, `style` | `sow`, `water`, `tend`, `fertilize`, `prune`, `graft`, `split`, `entwine`, `cultivate`, `trim`, `weed` (replaces `fix`), `uproot` (replaces `revert`), `landscape` (replaces `refactor`) | `feature`, `runtime`, `step`, `release`, `merge` — plus `fix`, `refactor`, `revert` exist only under renamed aliases, not TS-9's own words |
| `bookmarks` | `chore`, `maintenance`, `style` | `add`, `edit`, `delete` | `feature`, `runtime`, `fix`, `step`, `refactor`, `release`, `merge`, `revert` |
| `audits` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style` | `audit` | `feature`, `runtime`, `step`, `release`, `merge` |
| `design` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style` | `design` | `feature`, `runtime`, `step`, `release`, `merge` |
| `rfc` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style` | `rfc`, `draft`, `propose`, `accept`, `implement`, `reject`, `supersede` | `feature`, `runtime`, `step`, `release`, `merge` |
| `thoughts` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style` | `draft`, `publish` | `feature`, `runtime`, `step`, `release`, `merge` |
| `cheats` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style` | `add`, `edit`, `delete` | `feature`, `runtime`, `step`, `release`, `merge` |
| `specs` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style`, `feature` | `epic`, `quality` (`feature` is listed as "repository-specific" in the comment, but it's actually already a core TS-9 type — redundant, not a gap) | `runtime`, `step`, `release`, `merge` |
| `standards` | `chore`, `fix`, `maintenance`, `refactor`, `revert`, `style` | `add`, `edit`, `delete` | `feature`, `runtime`, `step`, `release`, `merge` |

Observations:

- `step`, `release`, and `merge` are excluded by **all eleven** local hooks.
  `runtime` is excluded by all eleven too — consistent with these being
  non-code, documentation-style repositories where dynamic quality attributes
  and pre-planned partial-work steps rarely apply, and releases/merges are
  either automated or not versioned the same way. Likely intentional, not a
  gap to close — but worth confirming with whoever owns each repo.
- `bookmarks`, `cheats`, and `standards` all use `delete` as their
  repository-specific "removal" type. TS-9's alternative revision-type set
  (for non-code repos, also in [04-commits.adoc](./04-commits.adoc)) names
  this type **`remove`**, not `delete`. Three-way naming drift from the
  standard's own vocabulary — either rename to `remove` for consistency, or
  record `delete` as a deliberate house synonym in TS-9 itself.
- `garden`'s `weed`/`uproot`/`landscape` are explicitly documented in-file as
  replacements for `fix`/`revert`/`refactor`, so the concepts are covered,
  just not under TS-9's own type names. Intentional per its own comments —
  flagged here for completeness, not as a defect.

## Suggested next steps

1. Fix `pre-commit-hooks` (`performance` → `runtime`), release `v0.3.0`.
2. Bump `ocean` and `website-ui` off the stale `v0.1.0` pin.
3. Decide whether `delete` (bookmarks, cheats, standards) should become
   `remove`, or whether TS-9 should document `delete` as an accepted
   synonym for repositories using its alternative revision-type set.
