# TS-11 gap analysis

Gaps found comparing TS-11: Versioning against the following reference
resources:

- https://docs.gitlab.com/ee/development/deprecation_guidelines/ (GitLab Deprecation guidelines, fetched from `__TODO__/Deprecation guidelines GitLab.URL`)
- `__TODO__/versioning/` (empty directory — no reference files to compare)

**Assessment.** The single retrievable reference is GitLab's internal
"Deprecating GitLab features" page, which is almost entirely about the
deprecation/breaking-change *management process* (approval workflows,
communication plans, documentation tooling, and API-specific stability
policies). That is release-process territory — TS-11's own
`AGENTS.md` routes release cadence/rollout strategy to TS-10 and
version-control mechanics to TS-9. Consequently the large majority of the
reference plausibly sits outside TS-11's stated purpose (versioning
schemes), and is flagged out-of-scope below for the user to confirm or
overrule. Two items plausibly fall within TS-11's scope: the standard
addresses "breaking change" only from the API-contract angle (partial), and
it does not address deprecation as a versioning event at all (missing).
The `__TODO__/versioning/` directory is empty and contributed nothing.

**Status:** First run (2026-08-05). No prior `GAPS.md` existed. All gaps
below are open.

## Missing

- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/
      (whole page — deprecation as a first-class lifecycle stage: announce
      deprecation, give notice, then remove) is not addressed anywhere in
      the standard. TS-11 has no guidance on how deprecation interacts with
      versioning — e.g. that announcing a deprecation is a user-facing
      non-breaking change (SemVer minor) while the eventual removal is a
      breaking change (SemVer major). The closest analogues,
      `src/011/02-semantic-versioning.adoc:62-73` (experimental features)
      and `src/011/05-version-zero.adoc` (version zero), cover when a major
      bump is *not* required, not deprecation. Recommend a new section
      (e.g. `10-deprecation.adoc`, or a "Deprecation" subsection in
      `02-semantic-versioning.adoc` after the Experimental features block).

## Partial

- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#breaking-change-policy
      covers the definition of a breaking change more thoroughly than
      `src/011/02-semantic-versioning.adoc:11-14` — specifically, the
      reference frames a breaking change as "any change [where] customers
      need to take action to ensure their workflows aren't disrupted"
      (including configuration updates and third-party deprecations, not
      just API changes), whereas TS-11 defines breaking change only from
      the API-contract / GUI-behavior angle. TS-11 itself notes the "public
      API" surface can be fuzzy for GUIs (`src/011/01-choosing-a-versioning-scheme.adoc:17-19`),
      so a customer-impact/action-required framing would help decide major
      vs. minor for non-API software.

## Out-of-scope

- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#breaking-change-policy
      ("We aim to eliminate all breaking changes from GitLab"; "the burden
      is on GitLab, not the customer, to own change management") covers a
      release-strategy principle, but it plausibly sits outside this
      standard's stated purpose because it is a release-cadence/rollout
      concern routed to TS-10. Flagged for the user to confirm or overrule.
- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#how-do-i-get-approval-to-move-forward-with-a-breaking-change
      (Breaking Change Exception approval process, six-month lead time,
      favorable criteria such as automated migration / negligible impact /
      Severity 1-2 security risk) covers a release-governance process, but
      it plausibly sits outside this standard's stated purpose because it
      is release-process/rollout strategy (TS-10), not versioning-scheme
      guidance. Flagged for the user to confirm or overrule.
- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#what-details-are-part-of-the-request-template
      (request template fields: Executive Summary, Impact Assessment,
      Rollout & Communication Plan, Internal Communication, Customer
      Communication) covers approval-process artifacts, but it plausibly
      sits outside this standard's stated purpose because it is
      release-process documentation, not versioning. Flagged for the user
      to confirm or overrule.
- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#after-you-have-an-approved-breaking-change-what-s-next
      (public deprecation issue as source of truth, deprecations-docs
      update, follow approved rollout plan) covers post-approval process
      steps, but it plausibly sits outside this standard's stated purpose
      because it is release-process (TS-10). Flagged for the user to
      confirm or overrule.
- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#update-the-deprecations-and-removals-documentation
      and #update-the-breaking-change-windows-documentation (YAML files in
      `gitlab/data/deprecations`, `rake gitlab:docs:compile_deprecations` /
      `compile_windows`, breaking-change-window YAML fields such as
      `removal_milestone`, `breaking_change`, `gitlab_com`, `window`,
      `impact`, `scope`, `check_impact`, primary vs. contingency windows)
      covers GitLab-specific documentation tooling, but it plausibly sits
      outside this standard's stated purpose because it is
      vendor-internal tooling, not versioning-scheme guidance. Flagged for
      the user to confirm or overrule.
- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#api-deprecations-and-breaking-changes
      (REST API v4: no breaking changes unless previously marked
      experimental or beta; GraphQL API: longer deprecation cycle required;
      webhook payloads: no breaking changes allowed) covers
      API-surface-specific stability policies, but it plausibly sits
      outside this standard's stated purpose because it is a per-API
      stability contract / release-process concern, not version-string
      guidance. (TS-11's experimental-feature rule in
      `src/011/02-semantic-versioning.adoc:62-73` is the adjacent
      versioning concept.) Flagged for the user to confirm or overrule.
- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#how-are-community-contributions-to-a-deprecated-feature-handled
      (community contributions to deprecated features restricted to
      Priority 1 / Severity 1 bug fixes) covers a contribution-triage
      policy, but it plausibly sits outside this standard's stated purpose
      because it is project-governance policy, not versioning. Flagged for
      the user to confirm or overrule.
- [ ] https://docs.gitlab.com/ee/development/deprecation_guidelines/#other-guidelines
      (Omnibus deprecation policy for configuration removals; Release and
      Maintenance policy for versioning/upgrade details) covers
      GitLab-internal adjacent policies, but it plausibly sits outside this
      standard's stated purpose because these are vendor-specific
      release/maintenance policies. Flagged for the user to confirm or
      overrule.

## Unresolved

- [ ] `__TODO__/versioning/` is an empty directory — no reference files
      were available to compare. Not included in the comparison above.