# TS-48 gap analysis

Gaps found comparing TS-48: *Environment variables* against the following
reference resource:

- https://12factor.net/config (Factor III: Config, "The Twelve-Factor App",
  Adam Wiggins, 2017)

**Assessment.** TS-48 is a short standard (one page, no subsections) and
already states the reference's central claim — config MUST live in environment
variables, not in code — as its opening sentence. But the reference contains
several supporting principles that TS-48 does not carry: the "could this
codebase be open-sourced right now without leaking credentials" litmus test,
the distinction between deploy-varying config and internal-to-code
configuration, the specific reasons environment variables are the right
mechanism (as opposed to config files or language constants), and — the
largest cluster — the granularity principle that env vars should be
independent, orthogonal controls rather than grouped into named "environments."
This last point is a genuine tension worth flagging: TS-9's branch-to-
environment model (`../009/07-environments.adoc`) is built around named
environments (dev, test, staging, production), which the reference explicitly
argues against as a config-management pattern. The two are not actually in
conflict — named *deployment environments* and named *config-var groupings*
are different things — but TS-48 does not draw this distinction, so a reader
could plausibly conflate them.

**Status:** All 4 actionable gaps closed (2026-08-13). The page was
restructured from a single flat body into three numbered partials
(`01-what-counts-as-config.adoc`, `02-core-requirements.adoc`,
`03-granularity.adoc`), wired into the page via `include::`. Nothing remains
open in this file.

## Missing

- [x] https://12factor.net/config ("A litmus test for whether an app has all
      config correctly factored out of the code is whether the codebase could
      be made open source at any moment, without compromising any
      credentials") is not addressed. TS-48 states the separation requirement
      but gives no way to verify it has been achieved. Recommend adding this
      as a practical test after the opening paragraph.

      **Resolved.** Closed by `02-core-requirements.adoc`, "Verifying correct
      separation" section. States the open-source litmus test as the
      practical check for whether config has been correctly separated from
      code, and names the corrective action (move the value into an
      environment variable) when the test fails. Source added to the page's
      `== References`.

- [x] https://12factor.net/config ("This is not the same as config files [...]
      This includes: [...] internal application config, such as [...] config
      that does not vary between deploys, such as [...] routing [...] should
      not be extracted [...] since it does not vary between deploys") is not
      addressed. TS-48 does not scope what counts as "config" — a reader could
      over-apply the standard and try to externalize settings that are
      properly part of the code because they never vary by deployment.
      Recommend a short "What counts as config" clarification.

      **Resolved.** Closed by a new `01-what-counts-as-config.adoc` partial,
      "What counts as config" section. Defines config as anything likely to
      vary between deploys, gives examples (database URLs, credentials,
      per-deploy hostnames), and explicitly excludes internal settings that
      never vary between deploys (routing rules, templating engine choice,
      module wiring), stating that such settings SHOULD NOT be externalized.
      Also restates the open-source litmus test from the first item as the
      dividing line between the two categories. Source added to the page's
      `== References`.

- [x] https://12factor.net/config ("Env vars are easy to change between
      deploys without changing any code; unlike config files, there is little
      chance of them being checked into the code repo accidentally; unlike
      custom config files [...] they are a language- and OS-agnostic
      standard") is only partially implied by TS-48's requirement, not stated
      as reasoning. Recommend adding these three justifications so the
      MUST-store-in-env-vars rule reads as a decision with rationale rather
      than an assertion.

      **Resolved.** Closed by a new paragraph in `02-core-requirements.adoc`,
      "Core requirements" section, immediately after the existing MUST-store
      rule. States the three justifications from the source: env vars change
      between deploys without a code change, they carry little risk of being
      committed to the repository by accident, and they are a language- and
      OS-agnostic mechanism understood by every runtime and deployment
      platform. Source added to the page's `== References`.

- [x] https://12factor.net/config ("The twelve-factor app stores config in
      environment variables (often shortened to env vars or env). Env vars are
      easy to change [...] granular controls, each fully orthogonal to other
      env vars. They are never grouped together as 'environments', but instead
      are independently managed for each deploy. This is a model that scales
      up smoothly as the app naturally expands into more deploys over its
      lifetime") is not addressed. TS-48 has no guidance at all on how
      individual variables should be organized or named, nor the
      recommendation against combinatorial "environment name" schemes (eg.
      `STAGING_DATABASE_URL` vs a plain `DATABASE_URL` whose value differs per
      deploy). Recommend a new "Granularity" section. Note the interaction
      with TS-9's named-environment branch model
      (`../009/07-environments.adoc:1-31`) flagged in the Assessment above —
      the new section should clarify that this principle concerns how
      individual variables are scoped and named, not TS-9's separate concern
      of which branches deploy to which environments.

      **Resolved.** Closed by a new `03-granularity.adoc` partial,
      "Granularity" section. Requires environment variables to be managed as
      independent, orthogonal, per-concern controls rather than grouped into
      named collections such as `STAGING_DATABASE_URL`, and requires a single
      plainly-named variable (`DATABASE_URL`) whose value differs per deploy
      instead. Explicitly distinguishes this from TS-9 (Version control)'s
      named-environment branch-to-deployment model, clarifying the two are
      complementary rather than in conflict — TS-9 governs which branches
      deploy where, this section governs how individual variables are scoped
      and named within any one deploy. Cross-references TS-9 (Version
      control) by xref. Source added to the page's `== References`.

## Partial

(None — the remaining reference claims are covered above as Missing.)

## Out-of-scope

(None identified in this run.)

## Unresolved

(None.)
