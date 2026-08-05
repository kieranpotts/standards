# TS-16 gap analysis

Gaps found comparing TS-16: Command Line Interfaces (CLIs) against the following reference
resources:

- `__TODO__/` directory (the original source draft material TS-16 was derived from):
  `README.md`, `principles.md`, `naming.md`, `distribution.md`, `interactivity.md`,
  `subcommands.md`, `output.md`, `errors.md`, `help.md`, and `options/` (`README.md`,
  `arguments-flags.md`, `configuration-files.md`, `environment-variables.md`,
  `piping.md`).

**Assessment.** The `__TODO__` directory is the direct source material that TS-16 was
reorganized and polished from, so nearly all of its content is already covered —
often more thoroughly than the source. The remaining gaps are a small number of
specific points the draft made that the standard dropped or softened: mostly
partial omissions in the principles and options sections, plus a couple of missing
recommendations.

**Status:** First run, 2026-08-05. All gaps below are open.

## Missing

- [ ] `__TODO__/options/README.md:17` — the point that it is acceptable to have a
      group of options that can _never_ have their defaults adjusted, to keep some
      behavior consistent across all environments, is not addressed anywhere in the
      standard. Recommend placing at `04-options.adoc:19` (Defaults section) or as a
      new subsection.

- [ ] `__TODO__/options/README.md:21` — the recommendation that, for local
      configuration files, it is RECOMMENDED to allow individual users to provide
      custom file names and paths via optional flags and/or environment variables,
      is not addressed anywhere in the standard. Recommend placing at
      `04-options.adoc:219` (Local configuration section).

- [ ] `__TODO__/principles.md:96` — the distinction that human-readable output is OK
      to iterate on (it is not a stable interface) whereas machine-readable output
      (`--plain`/`--json`) should be kept stable, with the recommendation to
      encourage users to use `--plain`/`--json` in scripts to keep output stable, is
      not made anywhere in the standard. Recommend placing at `09-output.adoc:9`
      (Standard output section) or `01-principles.adoc:134` (Future proofing).

## Partial

- [ ] `__TODO__/principles.md:82` covers the "make it feel robust" framing more
      thoroughly than `01-principles.adoc:3-10` — specifically, the source's point that
      "above all, robustness is achieved by keeping it simple" and that complex code
      and special/edge cases make a program fragile and unpredictable. The standard's
      intro mirrors the attention-to-detail framing but omits the simplicity
      principle entirely.

- [ ] `__TODO__/principles.md:90` covers future-proofing more thoroughly than
      `01-principles.adoc:134` — specifically, the source's explicit statement that
      "we use Semantic Version for our CLI utilities." The standard discusses major
      versions enduring but never names Semantic Versioning as the versioning
      convention.

- [ ] `__TODO__/principles.md:94` covers deprecation warnings more thoroughly than
      `01-principles.adoc:157` — specifically, the source's guidance to tell the user
      the flag is going to change when they pass it, to show them a future-proof
      alternative, and (where possible) to detect when they have updated their usage
      and stop showing the warning. The standard only says to "warn your users about
      deprecated operations."

- [ ] `__TODO__/principles.md:114` covers time-bombs more thoroughly than
      `01-principles.adoc:160` — specifically, the concrete example "Don't build in a
      blocking call to Google Analytics either." The standard makes the general
      time-bomb point without any illustrative example.

- [ ] `__TODO__/options/README.md:29` covers defaults more thoroughly than
      `04-options.adoc:19` — specifically, the `ls` example illustrating that you
      can't always predict how programs will be used (`ls` was designed for terse
      scripting output but is most commonly run as `ls -lhF`). The standard states
      the "good defaults" principle without this illustrative example.

- [ ] `__TODO__/help.md:3` covers online documentation more thoroughly than
      `11-documentation.adoc:42` — specifically, the requirement that, for public
      applications, online documentation MUST be indexable by public search engines.
      The standard only says publishing extended documentation online is
      RECOMMENDED.

- [ ] `__TODO__/help.md:173` covers help-text scope more thoroughly than
      `11-documentation.adoc:40` — specifically, the guidance that common options like
      `--version` and `--help` can be documented elsewhere, with just a link to the
      "full documentation" in the help text. The standard says only the most useful
      options need appear in the signature, but does not call out deferring common
      options with a link.

## Out-of-scope

- [ ] `__TODO__/principles.md` cross-references companion programming-principle
      standards (`crash-only.md`, `defensive-programming.md`, `simplicity.md`,
      `programming/principles/README.md`) and `__TODO__/options/README.md` references
      `delivery/versioning.md`. These are cross-links to a broader standards system
      on general programming principles, not CLI-specific guidance. They plausibly
      sit outside TS-16's stated purpose — flagged for the user to confirm whether
      TS-16 should add cross-references to companion standards on simplicity,
      defensive programming, crash-only design, and versioning.

## Unresolved

- (none — all reference files were read successfully.)