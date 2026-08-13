# TS-11: Versioning

This is a compact version of technical standard TS-11 for AI agents.

Use this when choosing a versioning scheme, formatting version strings, tagging
releases in version control, applying SemVer bumps from commit history, or
handling pre-release / build-metadata / LTS / named-release identifiers. Covers
semantic versioning (SemVer) and calendar versioning (CalVer).

Do NOT use this for release cadence/rollout strategy (see
[TS-10: Releasing](../010/AGENTS.md)) or for the version-control mechanics of
tagging and artifact binding (see [TS-9: Version Control](../009/AGENTS.md)) —
though this standard references both.

## Rules

- **Released software components SHOULD use a consistent versioning scheme.**

  This applies to libraries, web services, end-user applications, command-line
  tools, and infrastructure modules — anything released, distributed, or
  consumed by other parties. A consistent scheme makes it easier to manage
  compatibility between components and to communicate changes to consumers.

### Choosing a scheme

- **SemVer is RECOMMENDED for software with a stable, contractual interface
  that consumers depend on: libraries, public APIs, SDKs.**

  The semantic increments (major, minor, patch) communicate compatibility
  precisely.

- **CalVer is RECOMMENDED where time-of-release is the most meaningful
  identifier and backwards-compatibility commitments are softer: end-user
  applications, internal services, infrastructure modules, CLI tools, and
  continuously-deployed software (see [TS-10](../010/AGENTS.md)).**

  Common CalVer formats: `YYYY.MM.DD`, `YYYY.MM`, `YY.0M.MICRO`,
  `YYYY.MINOR.PATCH` (eg. `2025.07.14`, `25.07`, `2026.0.1`). Choice of
  granularity depends on release frequency. Appropriate for continuous
  deployment (where SemVer increments are too granular to be informative),
  time-boxed releases where the date itself is the identifier (Ubuntu's
  `YY.MM`), and internal/OS-style projects without a consumer-facing API
  contract. When SemVer would technically apply but the "public API" surface
  is fuzzy or shifting (eg. end-user GUIs where "breaking change" is hard to
  define), prefer CalVer.

- **A single version string SHOULD use one scheme consistently; the two MAY be
  layered for different audiences.**

  CalVer SHOULD NOT be combined with SemVer increments in the same string (eg.
  `1.2.3-2025.07`) — that defeats the purpose of both schemes; pick one and
  apply it consistently. Layering is permitted: eg. SemVer for internal
  versioning (developers, dependency managers) and CalVer for public release
  identifiers (marketing, end-user communication). Where layered, both
  identifiers MUST be unambiguously mapped to the same source-control tag and
  artifact so the binding remains traceable. All other guidance in this
  standard (tagging, `v` prefix, build metadata, pre-release suffixes) applies
  equally to CalVer.

### Semantic versioning

- **Use the [Semantic Versioning 2.0.0](https://semver.org/) format:
  `v{major}.{minor}.{patch}`.**

  - **{major}**: increment by 1 for incompatible/breaking API changes. For
    user-facing GUIs, a breaking change could be a change in behavior of an
    existing UI control or removal of existing controls.
  - **{minor}**: increment by 1 for user-facing changes that do not break
    backwards compatibility — new features, bug fixes, runtime-quality
    improvements.
  - **{patch}**: increment by 1 for internal changes that do not affect the
    user-visible contract — refactors, formatting, maintenance, chores.

  Representative chronology: `v1.0.0` → `v1.1.0` → `v1.2.0` → `v1.2.1` →
  `v2.0.0` → `v2.0.1` → `v2.0.2` → `v2.1.0`.

- **Bump versions from commit history per this mapping (see
  [TS-9](../009/AGENTS.md) for commit conventions).**

  - Commits flagged `BREAKING` → **major** bump.
  - Commits of type `feature`, `fix`, or `runtime` (without `BREAKING`) →
    **minor** bump.
  - Commits of type `refactor`, `format`, `maintenance`, or `chore` (without
    `BREAKING`) → **patch** bump.
  - Commits flagged `INCOMPAT` (internal-only breaking changes) MUST NOT, on
    their own, trigger a major bump — they affect internal callers but not the
    public API contract, so they bump patch like any other internal change.
  - Commits of type `step`, `version`, `merge`, and `revert` are
    version-neutral; they do not trigger bumps.

  When a release accumulates multiple commits, the highest applicable bump
  wins: `BREAKING` beats `feature`/`fix`/`runtime` beats
  `refactor`/`format`/`maintenance`/`chore`. Tools like `semantic-release` and
  `release-please` can automate this; manual version selection MUST follow the
  same rules.

- **Experimental features MAY change or be removed in a breaking way without a
  major bump, provided the experimental status is clearly communicated.**

  Experimental features MUST be clearly marked, require users to explicitly
  opt-in, be documented as experimental visible to anyone who discovers them,
  and have their unstable status communicated in release notes. Once an
  experimental feature becomes stable, the usual SemVer rules apply — breaking
  changes to it then require a major version bump.

### Version zero

- **`v0.x.x` releases are NOT REQUIRED to comply with SemVer rules.**

  Version zero SHOULD be used for preview, pre-release, or prototype builds of
  new software — considered unstable and not production-grade. Breaking changes
  MAY be introduced to `v0.x.x` releases without bumping the major version
  number.

### Pre-release versions

- **Pre-release versions follow `v{major}.{minor}.{patch}-{stage}.{inc}`.**

  A hyphen, then a stage identifier, a dot, and a zero-indexed incrementing
  integer. Common stage identifiers:

  - `alpha` — early, unstable, feature-incomplete builds.
  - `beta` — feature-complete but possibly buggy preview builds.
  - `rc` — release candidates expected to be stable and unlikely to change
    before final release.
  - `canary` — automated nightly or per-commit builds for early integration
    testing.
  - `dev` — single-revision builds used for testing through the registry.
  - `next` — sometimes used in place of `beta` or `rc` to identify the upcoming
    version.

  Release-order example:

  ```
  v1.0.0-alpha.0
  v1.0.0-alpha.1
  v1.0.0-beta.0
  v1.0.0-beta.1
  v1.0.0
  v1.1.0-alpha.0
  ```

  This convention extends SemVer and is based on the NPM registry convention;
  adapt for other package managers/ecosystems as needed. Distribution channel
  tags (`latest`, `stable`, `next`, `lts` assigned by package managers) are a
  related but distinct concept — registry metadata, not part of the version
  string.

### Build metadata

- **SemVer supports an OPTIONAL `+{build-metadata}` suffix.**

  ```
  v{major}.{minor}.{patch}[-{prerelease}][+{build-metadata}]
  ```

  Examples: `v1.2.3+sha.5114f85`, `v1.0.0-rc.1+20251201`. Build metadata MUST
  NOT affect version precedence — `1.2.3+a` and `1.2.3+b` are the same version.
  Intended for embedding non-version-determining build context (commit SHAs,
  build numbers, build dates, CI run identifiers). RECOMMENDED where the
  source-tag-to-artifact binding needs to be made explicit in the version
  string itself — eg. continuous deployment pipelines where artifact
  identifiers are not separately tracked.

### Tagging

- **Each release MUST be marked in version control by an annotated Git tag
  whose name is the version string prefixed with `v`.**

  Version `1.2.3` is tagged `v1.2.3`. The `v` prefix is part of the _tag_
  convention, not the version string itself — published version strings
  (package metadata, release notes, etc.) MAY omit it. Tags MUST be annotated
  (`git tag -a`) so they carry a tagger, timestamp, and message. Tags SHOULD
  be signed (`git tag -s`) where commit signing is in use (see
  [TS-9](../009/AGENTS.md)).

- **Tags MUST be permanent.**

  Once pushed to the reference repository, a tag MUST NOT be deleted, moved, or
  recreated against a different commit. If a release is botched, cut a new
  release with a new version number rather than retagging.

- **The tag and the artifacts produced from it MUST share the same identifier.**

  If `v1.2.3` is the tag, `v1.2.3` is also the identifier under which the
  corresponding compiled artifacts are stored in the artifact repository (see
  [TS-9](../009/AGENTS.md)). Tag a release as soon as possible after the
  integration that completes it, ideally as part of the automated pipeline that
  promotes commits to the `release` trunk. Tags are the canonical record of
  versioned releases — merge commits indicate _when_ changes were integrated,
  but only tags identify _which version_ corresponds to a given commit. Use
  `git tag -a v1.2.3 -F RELEASE_NOTES.md` for longer notes; `git push
  --follow-tags` pushes commits and annotated tags reachable from them in one
  operation.

### LTS releases

- **For long-term support releases, " LTS" MAY be appended to the version
  number.**

  Eg. `v1.3.0 LTS`, `v2.1.0 LTS`. Used alongside the regular version progression
  to designate which releases receive long-term support.

### Named releases

- **Consumer-friendly release names (eg. "Autumn 2025") MAY be used in
  addition to a version number for user-facing software applications.**

## References

- [TS-11 source](../../pages/011.adoc)
- [TS-9: Version Control](../009/AGENTS.md)
- [TS-10: Releasing](../010/AGENTS.md)
- [Semantic Versioning 2.0.0](https://semver.org/)
