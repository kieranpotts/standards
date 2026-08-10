# TS-9: Version Control

This is a compact version of technical standard TS-9 for AI agents.

Use this when working with Git: organizing repositories, writing commits and
commit messages, branching and merging, integrating changes, cutting releases,
or configuring Git/PR/CI tooling. Defines an opinionated trunk-based workflow
(`dev` → `test` → `ready` → `release`) rooted in continuous integration and
delivery. Workflows are Git-specific but portable to other decentralized VCS
(Mercurial, Fossil); centralized systems (SVN) are NOT RECOMMENDED.

Do NOT use this for release-cadence/rollout strategy decisions — those are
covered by [TS-10: Releasing](../010/AGENTS.md). For issue tracking see
[TS-8: Issue Tracking](../008/AGENTS.md); for version-numbering see
[TS-11: Versioning](../011/AGENTS.md). The workflow is intentionally a template
to adapt, not a rigid framework.

## Rules

### Repositories

- **Each repository MUST have a single centralized reference repository that is
  the source of truth.**

  All contributors implement changes in local clones. External contributors
  without write access use the fork-and-clone workflow (fork the reference
  repository, clone the fork, add an `upstream` remote pointing at the
  reference repository). Cloning SHOULD use SSH (stronger security profile
  than HTTPS).

- **Repository boundaries SHOULD reflect component boundaries and team
  ownership.**

  A repository encapsulates all code, config, tests, requirements, docs, and
  infra config for a discrete software component. Each repository SHOULD be
  owned by exactly one team; one team MAY own multiple closely-related repos.
  Repositories SHOULD be self-contained: a checkout plus scripts in the repo
  produce a working application, relying only on dependencies configured in the
  repo and installable automatically. Developers SHOULD be able to check out
  _any prior version_ and build, run, test, and deploy it without external
  state not pinned at that revision.

- **Mono-repos MAY encapsulate tightly-coupled components; they are REQUIRED
  where components must always coexist.**

  All components in a mono-repo SHOULD share version numbers and be taggable at
  repository level (rather than versioning components in-repo). It SHOULD be
  possible to run a complete deployment from a single repo without coordinating
  other repos.

- **Dependencies SHOULD NOT be committed to version control.**

  Use a binary repository manager (Artifactory, Nexus, CodeArtifact) plus
  package lock files (`package-lock.json`, `poetry.lock`, `Cargo.lock`), which
  MUST be committed. This guarantees reproducible builds and protects against
  upstream registries changing or disappearing.

- **Follow the repository naming convention.**

  ```
  <project>__<component>[-<version>][--<subcomponent>]
  ```

  Prefix with team/subdomain/project codename; use `global__`/`shared__`/
  `org-name` for org-wide repos; suffix with `--app`/`--db`/`--infra`/`--lib`
  etc. for subcomponents; append `-legacy`/`-next` for versioned variants.
  Lowercase US-ASCII only, hyphens between words, no numbers or special
  characters. Names SHOULD be short, domain-descriptive, and MUST NOT reference
  the technology stack. Internal codenames are RECOMMENDED so external brand
  changes don't force renames.

- **Every repository SHOULD include a `.gitignore`, and SHOULD include an
  `AUTHORS` file.**

  `.gitignore` excludes editor/OS metadata, build outputs, dependency dirs,
  env files. Take particular care to exclude secrets (`.env`, `.env.local`,
  credentials, key files) — `.gitignore` is the first line of defence even with
  secret-scanning hooks. `AUTHORS` (or `AUTHORS.md`) lists contributors as
  credit/attribution; it is distinct from `CODEOWNERS` (review routing /
  governance). A repo MAY have both.

- **Default branch SHOULD be `dev` (or `latest/dev` for LTS).**

  Initialize new repos with `git init`, rename the default branch with
  `git branch -m dev`, push with `--set-upstream`. Configure `init.defaultBranch
  = dev`. See LTS section below for the `latest/` prefix.

- **Retired repositories SHOULD be archived, not deleted.**

  Archiving (a hosting-provider feature) freezes contents read-only, preserving
  source for historical reference. Before archiving, update the README to
  explain why and point to any successor. Delete only when there is a positive
  reason (created in error, legal/regulatory removal).

### Commits

- **Make atomic commits.**

  Each commit is small, self-contained, stable (compiles, static and runtime
  tests pass — the golden rule is _don't break the build_), and self-contained
  (revertable independently). Application code changes SHOULD be committed with
  the tests that verify them. Prefer many small, discrete commits over a few
  large ones; if commits are too granular you can squash, but splitting a large
  commit is harder. Ideally a commit is scoped to a single concern and
  technology layer, but prefer larger cross-layer commits over breaking the
  build.

- **Stage deliberately; separate renames from edits.**

  Avoid `git add -A` and `git commit -a` for routine work — they bundle
  unrelated changes. Prefer `git add <path>` or `git add -p` (hunk-level
  staging). Commit a file rename in one revision and edits to that file in a
  separate revision, so Git detects the rename via content similarity (mixing
  rename and edit shows as delete-plus-add, breaking `git log --follow`).

- **Each commit MUST be scoped to exactly one of eleven revision types.**

  For software repositories: `behavior`, `quality`, `fix`, `step`, `refactor`,
  `style`, `maintenance`, `chore`, `release`, `merge`, `revert`.

  - **behavior** — change in user-facing operation (new, changed, deprecated,
    removed). Maps to functional requirements ("behaviors" in
    [TS-1](../001/AGENTS.md)).
  - **quality** — implementation of non-functional/dynamic quality attributes
    ("qualities" in [TS-1](../001/AGENTS.md)): latency, throughput,
    availability, security, resilience. Observable and measurable externally
    at runtime. Distinct from `refactor` (internal, static qualities for
    developers).
  - **fix** — resolves a defect: bug, regression, vulnerability, or incident.
  - **step** — incremental building block toward a larger behavior/quality/fix
    that does not itself change user-facing behavior. Enables CI of large
    changes.
  - **refactor** — improves internal design/structure without changing
    behaviors or degrading qualities (includes test/build-script/data-structure
    changes).
  - **style** — presentation-only changes (whitespace, indentation, wrapping,
    formatter runs like `prettier`/`black`/`gofmt`). Distinct from `refactor`.
  - **maintenance** — upkeep: dependency updates, test improvements, CI
    reconfig, doc extensions. May be recurring or triggered by external events.
  - **chore** — small, insignificant housekeeping not worth tracking in the
    issue tracker; typically doesn't touch code/config, may skip review and
    commit directly to trunks.
  - **release** — prepares a new software release.
  - **merge** / **revert** — capture the corresponding Git operations.

  For non-executable content repositories (docs, specs, handbooks), the
  RECOMMENDED extended types are: `create`, `update`, `delete`. (`create`
  introduces new content — new documents, sections, or substantial new
  material; `update` edits existing content; `delete` removes outdated or
  redundant content.) These extend, rather than replace, the standard set
  above — eg. `style` still applies to markup/formatting updates.

  Commit types map loosely to issue types in
  [TS-8](../008/AGENTS.md) but a one-to-one mapping is NOT mandated (a
  `refactor` commit may be associated with a "feature" issue, etc. — TS-8's
  issue-type vocabulary is separate from TS-9's commit-type vocabulary and is
  not renamed by this change).

- **Format commit messages as header, optional body, optional footers,
  separated by single blank lines.**

  ```
  <header>

  [<body>]

  [<footers>]
  ```

  Messages SHOULD be American English, US-ASCII only.

- **Header format: `<type>: <description> - <flag>`.**

  `<type>` MUST be one of the revision-type words above. `<description>` is
  REQUIRED, lowercase, no terminating period or other punctuation; multiple
  distinct changes in one commit are comma-separated. SHOULD be imperative
  present tense ("change" not "changed") — completes the sentence "If applied,
  this commit will <description>." Generally start with a verb describing the
  action; bug fixes need only describe the problem; release commits can give
  just the version number.

  ```
  chore: initial commit, add readme
  step: add openapi specification
  fix: invalid yaml formatting
  behavior: enable route to openapi spec
  release: v0.0.0-beta
  ```

- **Use flags to signpost special commits.**

  Flags are a single capitalized word, demarcated from the description by a
  spaced hyphen: `BREAKING`, `INCOMPAT`, `WIP`, `EXPERIMENT`, `TEMPORARY`
  (additional flags MAY be added per project).

  - **BREAKING** — MUST be used for changes incompatible with external clients
    (API changes that must be communicated via release notes). MAY drive
    automated major-version bumps and changelog generation (see
    [TS-11](../011/AGENTS.md)).
  - **INCOMPAT** — internal breaking changes (function signature changes,
    data/schema/facade changes that affect calling code or parallel work).
    Keep the build stable by refactoring in the same revision.
  - **WIP** — work-in-progress. MUST be used when the build is broken or tests
    fail. WIP commits MUST NOT be pushed to trunks (`dev`, `test`, `ready`);
    only permitted on `temp/*` or `epic/*`, and MUST be cleaned up (rebased,
    squashed, amended) before integration into `dev`.
  - **EXPERIMENT** — experimental changes not intended to be permanent,
    expected to be rolled back (eg. testing a library or design pattern). MUST
    NOT be integrated into `dev`, even via squash-merge.
  - **TEMPORARY** — commits that will be removed before `dev` integration (eg.
    debug logging). Author fully intends to revert.

- **Header line SHOULD NOT exceed 50 characters and MUST NOT exceed 72.**

  (Only automated `merge` and `revert` commits are exempt.)

- **Body explains the _why_, not the _what_.**

  Use the body for motivation, context, alternatives considered, and knowledge
  that can't be intuited from the diff. Do NOT duplicate information extractable
  from the commit (eg. list of changed files). Full sentences, periods, may be
  multi-paragraph (single blank lines between) and MAY include Markdown-style
  bullet lists with hanging indents. Lines SHOULD NOT exceed 72 characters.

- **Footers are `key: value` pairs for automation.**

  Block separated from body/header by a single blank line; entries delimited by
  single line breaks. Keys are hyphen-delimited contiguous strings, case
  insensitive (RECOMMENDED capital-case only the first word, eg. `Reviewed-by`;
  parsers MUST be case-insensitive). Values are freeform text; a continuation
  line indented by at least one space continues the previous value. Keys need
  not be unique. `git interpret-trailers` can read/add them.

  - `Closes: #123` (or `Fixes`/`Resolves`) — RECOMMENDED for cross-referencing
    issues; auto-closes issues on the default branch in integrated hosting
    providers. Use `Refs: #123` to reference without auto-closing.
  - Issue numbers SHOULD NOT be encoded in the subject line; use footers
    instead. Temporary branches, however, SHOULD be cross-referenced with the
    issue tracker (eg. `temp/123-add-feature`).
  - `Signed-off-by` — added via `git commit -s`; used for DCO opt-in.
  - Other common footers: `Co-authored-by`, `Reviewed-by`, `Tested-by`.

- **For merge commits, edit the header to conform; for revert commits, use the
  `revert:` prefix and a `Reverts:` footer.**

  Merge commits: use `--edit` (default since Git v1.7.10), keep Git's default
  body (parent hashes), and prefix the header with the change type (`behavior:`,
  `refactor:`, etc.) rather than a generic `merge:` when an explicit merge
  commit is necessary. Prefer fast-forward-only merging to avoid merge commits
  entirely. Revert commits: `revert: "<original header>"`, no body, footer
  `Reverts: <hash>`.

- **Do not rewrite history that has been pushed to a shared branch.**

  Rebasing, amending, squashing, or force-pushing a commit others may have
  pulled breaks downstream references. By branch type:

  - **Trunks** (`dev`, `test`, `ready`, release branches): history MUST NOT be
    rewritten under any circumstances. Force-push MUST be disabled in repo
    config.
  - **Temporary branches** (`temp/*`): single-owner, so rewriting pushed
    history is technically safe. Cleanup via interactive rebase, amend, or
    squash before integration is RECOMMENDED.
  - **Epic branches** (`epic/*`): shared between multiple developers; rewriting
    pushed history MUST be coordinated with all contributors. The merge-down
    sync strategy avoids the need for rebases.

### Branches

The workflow recommends seven branch types:

| Type | Naming | Lifespan | Protected | Mutable | Stable | Level |
| --- | --- | --- | --- | --- | --- | --- |
| Dev | `dev` | Permanent | No | No | No | REQUIRED |
| Test | `test` | Permanent | Yes | No | No | OPTIONAL |
| Ready | `ready` | Permanent | Yes | No | Yes | RECOMMENDED |
| Release | `release` / `release/<version>` | Perm./Temp | Yes | No | Yes | OPTIONAL |
| Temporary | `temp/[<id>-]<desc>` | Temporary | No | Yes | No | OPTIONAL |
| Epic | `epic/[<id>-]<desc>` | Long-lived temp | No | Yes | No | OPTIONAL |
| Spike | `spike/[<id>-]<desc>` | Temporary | No | Yes | No | OPTIONAL |

"Protected" means commits cannot be made directly — only fast-forward from
other branches' tips.

- **Trunks are append-only and immutable; fix forward only.**

  `dev`, `test`, and `ready` share exactly the same linear commit history (most
  of the time their tips differ). They MUST NOT ever be deleted. Trunks MUST be
  treated as append-only stacks: once a commit lands on a trunk it MUST NOT be
  dropped or amended — it can only be reverted via `git revert`. All changes —
  including hotfixes — MUST originate on `dev` and propagate forward through
  `test`, `ready`, and `release`. The GitFlow "hotfix" pattern (direct commits
  to release branches, then back-merges) is forbidden. The correct response to
  "the pipeline is too slow for hotfixes" is to make the pipeline fast, not to
  bypass it. No commits — not even hotfixes — are made directly on `test`,
  `ready`, or release branches.

- **All working branches MUST be cut from `dev`; new work originates only on
  `dev`.**

  `temp/*`, `epic/*`, and `spike/*` MUST be cut from `dev`, never from `test`,
  `ready`, or any release branch. Revisions are continuously integrated into
  `dev` either via direct commits or via `temp/*`/`epic/*` subsequently
  integrated back. The end result SHOULD be as though all changes were
  committed directly to `dev`, preserving a clean linear history.

- **`dev` is the integration branch; integrate multiple times per day.**

  `dev` is the only REQUIRED branch, equivalent to GitFlow's `develop` or
  trunk-based's `main`; RECOMMENDED as the default branch in the reference
  repository. The objective is to integrate into `dev` as soon as possible
  (ideally multiple times per day, per developer) to minimize merge conflicts.
  Run fast checks (linting, unit tests) on `dev`; longer checks belong on
  `test`. All tests that run against `dev` SHOULD pass on every commit;
  instability is fixed forward by pushing new fixes. `dev` is RECOMMENDED to
  be configured as the default branch.

- **Prefix trunks and branches with `latest/` from the outset, even for
  single-pipeline projects.**

  So the default branch is `latest/dev` rather than `dev`. The cost is
  negligible and reserves the option to run a future major version in parallel
  (big-bang rewrite, framework migration) without renaming established trunks.
  See LTS section below.

- **`test` is a permanent, protected QA trunk; `ready` is a permanent,
  protected, pristine trunk.**

  `test` is fast-forwarded to stable commits on `dev`, then more extensive
  long-running checks (integration, system, performance, expensive static
  analysis) run against it. When all tests pass, `ready` is fast-forwarded to
  the passing commit on `test`. Every commit on `ready` MUST have passed all QA
  checks; `ready` MUST NOT carry unverified work. The tip of `ready` always
  references shippable, production-grade code — a release candidate. If you
  have no expensive tests, `test` MAY be dropped and `ready` synced directly to
  `dev`. Multiple testing trunks MAY exist (eg. `perf`, `uat`, `smoke`).

- **Temporary branches (`temp/*`) are short-lived, single-owner, cut from
  `dev`, integrated via rebase + fast-forward.**

  Reserved for short-lived feature dev and bug fixes — not exploratory work
  (use `spike/*`). Valid uses: major refactors/rewrites, disruptive changes,
  long-running features that can't complete in a day, WIP backup, open-source
  contributions without write access. Ephemeral: SHOULD be deleted after
  integration (history is preserved in `dev`). Naming: `temp/[<id>-]<desc>`
  (`<id>` OPTIONAL, usually an issue number; `<desc>` REQUIRED,
  hyphen-delimited). Each temp branch SHOULD be scoped to a single focused
  change (typically one issue); orthogonal changes MUST NOT be combined even
  if they touch overlapping files. Sync strategy: rebase the temp branch onto
  `dev` at least daily; do NOT merge `dev` into temp branches (can introduce
  regressions).

- **Epic branches (`epic/*`) are long-lived, shared, cut from `dev`,
  synchronized via merge-down, integrated via squash-merge.**

  For complex big-bang integrations spanning weeks/months with multiple
  contributors. Valid uses: large coordinated features, major refactors,
  cross-cutting concerns, release preparation. MUST be cut from `dev`. Key
  difference from temp branches: sync via merge-down (merge `dev` _into_ the
  epic branch, creating explicit merge commits that preserve lineage) — never
  rebase shared history. Integrate back into `dev` via squash-merge,
  typically through a PR. Naming: `epic/[<id>-]<desc>`. SHOULD be deleted once
  integrated.

- **Spike branches (`spike/*`) isolate exploratory work that is never
  merged.**

  Time-boxed investigations whose deliverable is knowledge, not shippable
  code. MUST be cut from `dev`. MUST NOT be integrated back into `dev` (or any
  trunk) — this is the defining characteristic. If you want to keep the code,
  start a fresh `temp/*` or `epic/*` branch and reimplement to integration
  standard. Two acceptable end states: delete the branch once learnings are
  captured elsewhere, or retain it as an archived record (clearly marked via
  the `spike/` prefix). Naming: `spike/[<id>-]<desc>`.

- **Periodically review and clean up stale branches.**

  A `temp/*` or `epic/*` branch with no commits in (eg.) 90 days SHOULD be
  reviewed and either revived or deleted. Intentionally retained `spike/*`
  branches are exempt (they are archived records, not work awaiting
  integration).

### Integrations

- **Trunk-to-trunk: fast-forward-only merging.**

  Maintains a clean linear history so `git log` serves as a useful changelog.
  Use for `test` catching up with `dev` and `ready` catching up with `test`:

  ```
  git checkout test && git merge --ff-only dev
  git checkout ready && git merge --ff-only test
  ```

  Works only if no commits are ever made directly to trunks except `dev`.

- **Temporary branches into `dev`: rebase, then fast-forward merge.**

  Stage 1: rebase the temp branch onto the latest `dev` (resolves conflicts in
  the source branch, not the shared trunk). Stage 2: `git checkout dev && git
  merge --ff-only temp/*`. Alternative for larger integrations where you want
  single-operation undo: `git merge --no-ff temp/*` (creates an explicit merge
  commit recording the integration point; less linear but revertable as one
  `git revert`). Rebase temp branches on `dev` at least daily; do NOT merge
  `dev` into them.

- **Epic branches into `dev`: squash-merge, typically via pull request.**

  Epic branches accumulate noisy history (intermediate WIP, merge-down
  commits). Squash-merge consolidates the entire epic into a single
  well-described commit on `dev`. After squash-merging, delete the source
  branch immediately — the squashed commit is not linked to the originals, so
  a future merge would reintroduce the same changes and conflict.

- **Cherry-picking is a targeted, exceptional tool, not a routine strategy.**

  Useful for backporting fixes or selectively promoting commits. Cherry-picked
  commits are copies not linked to their origin, so a later full merge will
  not recognize them as already applied and may conflict.

- **Patching (`git format-patch` / `git am`) is the only strategy that doesn't
  require a shared remote.**

  Useful for air-gapped systems or external contributions where direct repo
  access isn't possible. Rarely encountered outside the Linux kernel
  ecosystem; modern PR-based workflows have made it largely redundant.

### Releases

- **Continuous delivery is REQUIRED; continuous deployment is OPTIONAL.**

  Every change is automatically built, tested, and prepared for release as
  part of the normal workflow. Every commit on `ready` is a release candidate,
  but deployment cadence is flexible. Two workflows are RECOMMENDED:

  - **Release trunk** (`release`, permanent, protected, immutable, stable;
    OPTIONAL): supports continuous deployment. Every change passing automated
    verification on `ready` is promoted to `release` for immediate production
    deployment. References compiled artifacts in an external artifact
    repository indexed by commit SHA or tag; you MUST be able to deploy
    immediately without waiting for builds.

  - **Release branches** (`release/<version>`, temporary, protected, immutable,
    stable; OPTIONAL): support release trains and big bangs. Cut one per
    release from `ready`. A placeholder `release/next` MAY be used if the
    version isn't decided yet. Release preparation does NOT block `dev` —
    release-time code freezes are not needed. Release branches MUST contain
    only release-preparation commits (version bumps, changelog, release
    config); code/config fixes MUST NOT be committed to them and instead flow
    through `dev` → `test` → `ready`. After tagging, delete the branch; the
    version tag is permanent.

  Release cadence (big bang / release trains / continuous deployment) and
  rollout strategy (rolling / canary / blue-green / feature flags) are covered
  by [TS-10: Releasing](../010/AGENTS.md).

- **Compiled artifacts MUST NOT be stored in version control.**

  Binaries, packages, container images, and other build outputs belong in
  registries (Docker Hub, ECR, Maven Central, npm, PyPI), object storage (S3,
  GCS, Azure Blob), or generic artifact repos (Artifactory, Nexus,
  CodeArtifact). Anti-patterns: Git LFS for release artifacts, orphaned
  artifact-storing branches. Release metadata (tags, changelogs, notes,
  secrets/flag config) MAY live in version control via release branches.
  Best practice: create a two-way binding between VCS and artifact repo via
  version numbers (tag `v1.2.3` ↔ artifact `v1.2.3`).

### Long-term support (LTS)

- **To support multiple major versions in parallel, prefix branches with the
  version and run one pipeline per version.**

  `latest/*` (current major version), `v2/*`, `v1/*`, etc., each with their own
  `dev`/`test`/`ready`/`release`/`temp/*`. To start a new major version, create
  new branches from each `latest/*` (eg. `latest/dev` → `v3/dev`) and promote
  the new version to `latest/*`. LTS branches MAY be deleted once a major
  version reaches end-of-life (release tags persist).

- **Patch upstream-first: fix the latest version, then backport.**

  When a bug affects multiple maintained versions, introduce the fix to
  `latest/dev` first, then cherry-pick backwards to older versions. This
  prevents the same bug resurfacing in future releases and keeps fixes
  traceable to their origin. Diverged versions may need extra conflict-resolution
  commits, or separate patches per version. Limit the total number of parallel
  legacy versions — each multiplies coordination overhead.

- **Use `/` as the LTS delimiter.**

  Many Git GUIs collapse branch lists into a tree based on `/`. Naming
  variations are acceptable: `latest/`, explicit version (`v4/`), `next/` (the
  upcoming version, distinct from `latest/` = current), date-based
  (`2026-spring/`), codenames (`alpine/`). `latest/` avoids renaming the
  default branch on each major bump; explicit version numbers give immutability
  and reduce CI reconfiguration. Don't confuse release branches
  (`release/**`, prepare point releases like v1.2.3) with LTS pipelines
  (groupings of trunks/branches supporting multiple major versions like v1/v2).

### Workflows

Five workflows introduce revisions to `dev`, all supporting continuous
integration:

- **Trunk workflow** — atomic commits pushed directly to `dev`. For
  contributors with write access who prefer CI over branches. Pull with
  `--rebase` before pushing; push after every atomic commit.

- **Branch workflow** — atomic commits on a `temp/*` branch, integrated by
  fast-forwarding `dev` to the temp branch tip. For contributors with write
  access who prefer isolation. Optionally push the temp branch as a remote
  backup (use `--force-with-lease`, never plain `--force`, after rebasing —
  safer because it refuses if the remote has moved).

- **Pull request workflow** — branch workflow plus peer review via a PR
  system. PRs SHOULD target `dev` (or `<version>/dev`). Use draft/WIP PR status
  for in-progress work seeking early feedback. PR systems SHOULD be configured
  to auto-delete source branches after merge.

- **Fork workflow** — for external contributors without write access. Same as
  the branch workflow but temp branches are pushed to a fork; PRs go from the
  fork's temp branch (head) to the reference repo's `dev` (base). Add an
  `upstream` remote for synchronization.

- **Epic workflow** — for long-lived, team-coordinated work. Sync the epic
  branch with `dev` via merge-down (`git fetch origin && git merge
  origin/dev`), NOT rebase. Integrate via squash-merge, typically through a
  PR. Communicate before force-pushing; coordinate with all contributors.

### Work-in-progress commits

- **WIP commits MUST NOT be integrated into `dev`; clean up before
  integrating.**

  WIP commits (build broken or tests failing) MUST be flagged `WIP` and MUST
  NOT be pushed to trunks. They MAY exist only on `temp/*` or `epic/*`. Before
  merging into `dev`, ensure the branch tip is stable and passes tests.
  Cleanup options: soft reset (`git reset --soft <hash>` then commit),
  amend (`git commit --amend`), interactive rebase (`git rebase -i`), or
  squash-merge. All history rewriting is limited to temp/epic branches before
  push, or after push only with `--force-with-lease` and (for epics) team
  coordination. Once commits reach `dev` they are immutable. EXPERIMENT-flagged
  commits MUST NOT be integrated into `dev`, even via squash-merge.

### Pull request configuration

- **Prioritize continuous integration over PR-gated review.**

  PR-gated workflows impose real costs: blocked progress, context switching,
  slow integration. The trunk and branch workflows allow CI without PR gates;
  quality is maintained by pair/mob programming and strong automated checks.
  PRs SHOULD be reserved for the fork workflow (external contributions) and
  epic-branch integration. Minimizing epic branches in favor of small
  continuously-integrated changes is itself a goal.

- **All PRs MUST target `dev` (or `<version>/dev`); PRs to downstream branches
  MUST be rejected by repo configuration.**

  `test`, `ready`, and release branches are populated only via automated
  promotion.

- **PR merge configuration on `dev`: rebase + fast-forward for `temp/*`;
  squash-merge for `epic/*`.**

  Basic merge and rebase-with-merge-commit are NOT RECOMMENDED (non-linear or
  noisy histories undermine provenance). The strategy is driven by source
  branch type, not by whether integration is local or via PR. No merge
  configuration applies to `spike/*` (never integrated); a spike MAY have a
  draft PR as a discussion forum, but it's closed not merged.

- **Repositories SHOULD include a `CODEOWNERS` file.**

  Maps paths to teams/individuals responsible for reviewing changes to those
  paths; PR systems auto-request reviews and MAY gate merge on owner approval.
  Owners SHOULD be teams (not individuals) where possible, for coverage when
  individuals are unavailable.

- **PR titles SHOULD follow commit header conventions; PR descriptions SHOULD
  use task lists for non-trivial changes.**

  PR titles become the commit message when squash-merged: lowercase type
  prefix, optional scope, `BREAKING`/`INCOMPAT` flag where applicable, concise
  imperative subject (eg. `behavior(auth): add OAuth device flow`). Task lists
  (Markdown checkboxes) give the author a self-checklist, reviewers a quick
  view of progress, and make cross-PR dependencies explicit.

- **Draft PRs are a review forum, not a license to keep work isolated.**

  Useful for long-running features, spike discussion, and cross-team
  coordination. Work MUST still land on `dev` as soon as it is complete and
  stable.

### Environments

- **Map branch types to deployment environments.**

  Local dev (`dev`, `temp/*`) → dev integration (`dev`) → testing (`test`) →
  staging/pre-production (`ready`) → production (`release`). Minimal setups
  may collapse some. Ephemeral preview environments (auto-provisioned on push
  to `temp/*` or on PR open, destroyed on merge/delete) complement but don't
  replace trunk environments.

- **Preview environments MUST use environment-scoped secrets, never production
  secrets; SHOULD use synthetic/anonymized/scrubbed data.**

  Most CI/CD platforms support environment-specific secret stores — treat this
  as a hard requirement. Budget infrastructure for concurrent previews and
  configure automatic teardown on inactivity. Preview URLs are often
  guessable — gate behind authentication or assume they are public.

- **Environment-specific configuration SHOULD NOT be committed to version
  control.**

  Inject at runtime via environment variables, config files, or secrets
  management systems (Vault, AWS Secrets Manager). Use feature flags to
  enable/disable features per environment without code changes. Keep
  infrastructure-as-code (Terraform, CloudFormation) in version control but
  separate from application code. For LTS, create a parallel set of
  environments per supported version (`latest/dev`, `v2/dev`, `v1/dev`), each
  with its own CI/CD pipeline.

### Continuous integration and delivery

- **Break work into increments completable in one to two days.**

  Features that can't be completed in that timeframe SHOULD still integrate
  into `dev` in a disabled/inactive state, exercised against the latest
  mainline without exposing to users. Two techniques: feature flags
  (conditional statements controlled at runtime, eg. via a config service —
  see [TS-10](../010/AGENTS.md)) and branch by abstraction (refactor under an
  abstraction layer; both implementations coexist; switching is a small
  controllable change). For genuinely indivisible work, epic branches are the
  exception, not the norm.

- **Prioritize and expedite code review; automate quality checks on every
  commit and every promotion.**

  Integration velocity is limited by review latency. Small frequent commits
  yield smaller, faster-to-review PRs. Automated checks (linting, testing,
  builds, deployments) run on every commit to `dev` and every promotion
  through `test`/`ready`.

- **Use the reverse-merge strategy: pull mainline changes into your branch,
  don't push WIP to the mainline.**

  Continuously pull `dev` into your work-in-progress branch to test against
  the full current codebase, detect integration issues early, and reduce merge
  complexity at integration time. Only completed, releasable work is merged to
  trunks.

- **Beware semantic conflicts; mitigate via frequent integration, strong
  automated trunk checks, coordination, and merge queues.**

  Semantic conflicts (eg. one PR renames a function, another parallel PR calls
  it by the old name) are not detectable by `git merge` textual diffs. Both
  PRs pass in isolation but the build breaks when both land. Mitigations:
  multi-times-per-day integration, strong automated checks on the trunk,
  coordination (pair programming, design notes, `INCOMPAT`-flagged commits), and
  merge queues that test each change against the latest trunk before
  integration.

- **Keep the mainline (`dev`, especially `ready`) always releasable.**

  Do not use code freezes, all-hands swarms, or back-outs to clean up before
  releases — those are symptoms of poor integration discipline. If stories
  and fixes need to be held and coordinated before release, you are not
  practicing continuous delivery.

### Security

- **Secrets and PII MUST NOT be committed to version control.**

  Use a dedicated secrets management system (Vault, AWS Secrets Manager, Azure
  Key Vault, 1Password) and inject at runtime (typically as environment
  variables resolved by the deployment pipeline). See
  [TS-52](../052/AGENTS.md) and [TS-48](../048/AGENTS.md). Integrate static
  analysis (TruffleHog, detect-secrets) at multiple layers: as a pre-commit
  hook (most valuable — catches before history), in the CI pipeline on every
  push, and as a merge gate on protected branches. Pre-commit hook config
  SHOULD live in the repo. Once a secret reaches even a local commit the only
  remedy is to rotate/invalidate it — removing it from history is
  insufficient, especially on immutable trunks.

- **Commit signing is RECOMMENDED, especially for open source and critical
  infrastructure.**

  Without signing, `user.name`/`user.email` are unverified and trivially
  forged. Git supports GPG, SSH (simplest if you already use SSH keys), and
  X.509 signing. RECOMMENDED to require signed commits on protected branches
  via the hosting provider. Less critical for closed-source where push access
  is already authentication-gated, but still useful for audit and compliance.

- **Control access via authentication and RBAC; protect branches; audit
  access.**

  Developers SHOULD authenticate with SSH keys or personal access tokens (not
  passwords); SSH keys passphrase-protected; tokens minimal-permission with
  short expirations; inactive accounts removed promptly. Use RBAC tiers
  (read-only, developer, maintainer, owner/admin). Regularly audit access
  logs. Branch protection on all protected branches (especially trunks)
  SHOULD require PR reviews, status checks, up-to-date branches, signed
  commits, dismiss stale approvals, restrict push, and prevent force
  pushes/deletions. `dev` is typically permissive to enable CI; restrict it
  only for very large teams, open-source, or strict governance.

- **Maintain repository backups in a geographically distinct location and test
  them periodically.**

  Protects against accidental/malicious deletion, hosting-provider
  corruption, and account compromise. Git's distributed nature (every clone
  is a full copy) helps but is not sufficient.

- **Keep dependencies up-to-date; integrate dependency scanning; commit lock
  files; review updates before merging to protected branches.**

  Enable hosting-provider security alerts (Dependabot, GitLab security
  dashboards). Lock files MUST be committed to version control.

### Git configuration

- **Configure Git for the workflow.**

  - `init.defaultBranch = dev` (or `latest/dev`).
  - `merge.ff = only` — fast-forward-only as the default merge (override with
    `--no-ff` for epic merge-down sync, or use a conditional include scoped to
    `epic/` branches: `[includeIf "onbranch:epic/"] path = ~/.gitconfig-epic`
    with `[merge] ff = true`).
  - `pull.rebase = true` OR `pull.ff = only` — both produce linear history;
    `pull.rebase` automates the rebase step, `pull.ff` requires manual rebase.
  - `push.autoSetupRemote = true` — auto-creates same-named remote branch and
    tracking on first push (forces identical local/remote branch names).
  - `commit.gpgSign = true`, `tag.gpgSign = true`, `gpg.format = ssh`,
    `user.signingKey = ~/.ssh/...` for SSH commit signing (register the same
    key as a signing key with your hosting provider, separately from auth).
  - `core.autocrlf = false`, `core.eol = lf` — normalize to Unix line endings;
    enforce via EditorConfig.
  - RECOMMENDED aliases: `rb = rebase --committer-date-is-author-date`
    (preserve author dates), `puff = push --force-with-lease` (safe force
    push), `ff = merge --ff-only`, `sync = pull --rebase` (or `pull --ff-only`).

### Worktrees

- **It is RECOMMENDED to check out repositories as worktrees (necessary for
  parallelism in agentic workflows).**

  Clone bare (`git clone --bare`), add worktrees with `git worktree add`. The
  only constraint: the same branch can't be checked out in more than one
  worktree at a time. Best practice: put the bare repo in a hidden `.bare`
  directory with a `.git` pointer file (`echo "gitdir: ./.bare" > .git`) so all
  `git` commands work from the project root, and place worktrees as siblings
  (eg. `main/`, `feature-x/`). Fix the fetch refspec manually after a bare
  clone: `git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'`.
  The adjacent-sibling pattern keeps working files separate from Git
  internals and prevents editors/search tools/watchers from descending into
  `.bare`.

### Miscellaneous

- **Committed symlinks MUST NOT point outside the repository and MUST be
  relative paths.**

  `../config/prod.yaml` travels better than
  `/home/user/project/config/prod.yaml`. Even so, symlinks can cause
  cross-environment incompatibilities (Windows `core.symlinks` defaults to
  false in some installs, checking out symlinks as plain text). Best to avoid
  committing symlinks at all.

## References

- [TS-9 source](../../pages/009-version-control.adoc)
- [TS-8: Issue Tracking](../008/AGENTS.md)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-11: Versioning](../011/AGENTS.md)
- [TS-48: Environment Variables](../048/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-60: GitHub Actions](../060/AGENTS.md)
