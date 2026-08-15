# TS-16 gap analysis

Gaps found comparing TS-16: Command line interfaces (CLIs) against the following reference
resources:

- `__TODO__/` directory (the original source draft material TS-16 was derived from):
  `README.md`, `principles.md`, `naming.md`, `distribution.md`, `interactivity.md`,
  `subcommands.md`, `output.md`, `errors.md`, `help.md`, and `options/` (`README.md`,
  `arguments-flags.md`, `configuration-files.md`, `environment-variables.md`,
  `piping.md`).

- The 10 reference URLs listed in GitHub issue #65
  (https://github.com/kieranpotts/standards/issues/65):
  - https://clig.dev/ — _Command Line Interface Guidelines_
  - https://devcenter.heroku.com/articles/cli-style-guide — Heroku CLI Style Guide
  - https://smallstep.com/blog/the-poetics-of-cli-command-names/ — _The Poetics of CLI Command Names_
  - https://unix.stackexchange.com/a/4132 — terminal/shell/tty/console definitions
  - https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f — _User Experience, CLIs, and Breaking the World_
  - https://en.wikipedia.org/wiki/The_Unix_Programming_Environment — Wikipedia
  - https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html — POSIX Utility Conventions
  - https://www.gnu.org/prep/standards/html_node/Program-Behavior.html — GNU Program Behavior
  - https://www.gnu.org/prep/standards/html_node/index.html — GNU Coding Standards (index)
  - https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 — _12 Factor CLI Apps_

**Assessment.** The `__TODO__` directory is the direct source draft TS-16 was reorganized
from, so nearly all of its content is already covered — often more thoroughly than the
source; only a few small omissions remain (carried over from the first run, all still open).
Of the external URLs, clig.dev is the foundation TS-16 explicitly builds on and is largely
covered, but it contributes concrete recommendations the standard omits (use an
argument-parsing library; an analytics/telemetry policy; the `--` end-of-options delimiter;
an "explicit actions" principle). Heroku's and 12 Factor's guidance surfaces gaps in
table output, sub-subcommand delimiters, the `--version` output format, and the XDG
data/cache directory structure. Smallstep adds naming anti-patterns (emoji, version
suffixes). POSIX reinforces the `--` delimiter and the mutually-exclusive-argument
notation. GNU adds `--version` format rules, output-via-`-o`, and detailed error-position
formatting. The UX Collective case study surfaces help-discoverability problems for CLIs
with very many commands and the "automated migration command" pattern. The Wikipedia and
Unix SE resources are background/reference rather than CLI design rules (out-of-scope).

**Status:** Fourth run, 2026-08-15. All 60 actionable gaps (10 Missing, 50 Partial)
closed. Third run (2026-08-14) closed 59 of them across every content file in the
standard — `01-principles.adoc` through `11-documentation.adoc`, plus
`03-distribution.adoc`. This run closed the remaining Missing item — the
user-authorized "Terminology" section, routed in from the Out-of-scope review. All
9 Out-of-scope items are resolved (8 confirmed, 1 overruled and actioned, 1 overruled
but left unrouted pending a separate standards decision — see below). 1 Unresolved
item (`Program-Behavior.html`) is dismissed as a persistent fetch failure whose
content was already captured elsewhere. This file is now fully resolved.

## Missing

- [x] `__TODO__/options/README.md:17` — the point that it is acceptable to have a
      group of options that can _never_ have their defaults adjusted, to keep some
      behavior consistent across all environments, is not addressed anywhere in the
      standard. Recommend placing at `04-options.adoc:19` (Defaults section) or as a
      new subsection.

      **Resolved.** Closed by a new paragraph in the "Defaults" section of
      `04-options.adoc`. States it is acceptable for a group of options to
      never have their defaults adjusted, to keep behavior consistent across
      every environment the program runs in.

- [x] `__TODO__/options/README.md:21` — the recommendation that, for local
      configuration files, it is RECOMMENDED to allow individual users to provide
      custom file names and paths via optional flags and/or environment variables,
      is not addressed anywhere in the standard. Recommend placing at
      `04-options.adoc:219` (Local configuration section).

      **Resolved.** Closed by a new paragraph in the "Local configuration"
      section of `04-options.adoc`. Recommends allowing a custom local
      configuration file name/path via an optional flag and/or environment
      variable (eg. `--config <path>` or `[APP]_CONFIG`).

- [x] `__TODO__/principles.md:96` — the distinction that human-readable output is OK
      to iterate on (it is not a stable interface) whereas machine-readable output
      (`--plain`/`--json`) should be kept stable, with the recommendation to
      encourage users to use `--plain`/`--json` in scripts to keep output stable, is
      not made anywhere in the standard. Recommend placing at `09-output.adoc:9`
      (Standard output section) or `01-principles.adoc:134` (Future proofing).

      **Resolved.** Closed by a new paragraph in the "Standard output" section
      of `09-output.adoc`. States human-readable output is not a stable
      interface and is fine to iterate on, while machine-readable output is a
      stable interface once scripts depend on it, cross-referencing "Future
      proofing", and encourages scripts to use `--plain`/`--json`.

- [x] https://clig.dev/#analytics — the standard has no guidance at all on usage
      analytics / telemetry / "phoning home". clig.dev devotes a whole section to it:
      do not phone home usage or crash data without consent; be explicit about what is
      collected, why, how anonymous, how anonymized, and retention; prefer opt-in, and
      if opt-out, clearly tell users and make it easy to disable; consider alternatives
      (instrumenting web docs or downloads, talking to users). Recommend a new
      "Analytics" section after `03-distribution.adoc` or within `01-principles.adoc`.

      **Resolved.** Closed by a new "Analytics" section in `01-principles.adoc`,
      placed after "Communicate state changes" and before "Control output".
      Requires consent before phoning home usage or crash data, requires
      transparency about what is collected/why/anonymization/retention, prefers
      opt-in, and requires an easy disable (`--no-analytics` flag or
      `[APP]_NO_ANALYTICS` env var, mirroring the `NO_COLOR` convention) where
      opt-out is used instead. Also notes non-telemetry alternatives (registry
      download counts, doc-site analytics, talking to users directly).

- [x] https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_02
      (Guideline 10), reinforced by
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor II) — the
      `--` end-of-options delimiter. The standard never mentions bare `--` to separate
      options from operands, nor its use to pass remaining args to a subprocess
      (e.g. `heroku run -a myapp -- myscript.sh -a arg1`). Recommend a new subsection in
      `04-options.adoc` (Arguments and flags).

      **Resolved.** Closed by a new "The `--` end-of-options delimiter"
      subsection in `04-options.adoc`, after the common-flags table. Covers
      both reasons for the delimiter: passing a hyphen-prefixed value
      unambiguously, and passing remaining arguments through to a subprocess,
      with the `heroku run -a myapp -- myscript.sh -a arg1` example. Source
      (POSIX Utility Conventions) already in the page's `== References`.

- [x] https://clig.dev/#output — the "explicit actions" principle: reading or writing
      files the user did not explicitly pass as arguments, and talking to a remote
      server (e.g. to download a file), should usually be explicit (unless storing
      internal program state such as a cache). Not addressed anywhere in the standard.
      Recommend adding as a new principle in `01-principles.adoc` (after "Communicate
      state changes", L66) or in `04-options.adoc` (Arguments and flags).

      **Resolved.** Closed by a new "Prefer explicit actions" section in
      `01-principles.adoc`, immediately after "Communicate state changes".
      States that reading/writing files not explicitly passed as arguments, and
      talking to a remote server, should usually be an explicit action, and
      carves out the exception for internal program state such as a cache,
      cross-referencing the new Analytics section.

- [x] https://clig.dev/#output and https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46
      (Factor I) — shell completion / autocomplete. The standard covers discoverability
      via help text and suggestions but never mentions shell completion, which both
      sources call out as a major aid to discoverability and correct flag usage (e.g.
      typing `--app <tab><tab>` makes the next value unambiguous). Recommend a new
      subsection in `11-documentation.adoc`.

      **Resolved.** Closed by a new "Shell completion" section in
      `11-documentation.adoc`, after "Help text". Recommends providing
      completion scripts for common shells, with the `--app <tab><tab>`
      example, and documenting installation.

- [x] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VIII) —
      tabular output conventions. The standard discusses `--json`/`--plain` but has no
      guidance on table output: one entry per row (so output pipes cleanly to `grep`
      and `wc`), never emit table borders, and the conventional flags for tables
      (`--columns`, `--no-truncate`, `--no-headers`, `--filter`, `--sort`, CSV output).
      Recommend a new "Tables" subsection in `09-output.adoc` (Formatting, L63).

      **Resolved.** Closed by a new "Tables" section in `09-output.adoc`,
      placed after "Standard output" and before "Pagers" (a top-level section
      rather than a Formatting subsection, since it groups a full set of
      conventions of its own). Covers one-record-per-row, no table borders,
      and the `--columns`/`--no-truncate`/`--no-headers`/`--filter`/`--sort`/
      `--csv` flags.

- [x] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VI) — OS
      / desktop notifications when a very long-running task completes. Not mentioned
      anywhere in the standard. Recommend placing in `09-output.adoc` (Animations, L101)
      or `06-interactivity.adoc`.

      **Resolved.** Closed by a new paragraph at the end of the "Animations"
      section of `09-output.adoc`. Recommends triggering an OS-level desktop
      notification for long tasks a user is likely to switch away from,
      alongside terminal output.

- [x] https://unix.stackexchange.com/a/4132 (routed in from the
      Out-of-scope review, 2026-08-15) — definitions of terminal, shell,
      tty, console, pseudo-ttys, terminal emulators, and the division of
      labor between terminal and shell. The user explicitly asked for a
      new "Terminology" section covering this, overruling the original
      out-of-scope classification. Not yet written into any partial.

      **Resolved.** Closed by a new "Terminology" section opening
      `01-principles.adoc`, before "Simplicity". Defines shell (the
      command-line interpreter), terminal/tty (the Unix text I/O
      environment, a device file supporting `ioctl`-based control beyond
      plain read/write), terminal emulator (the program providing a
      pseudo-tty and rendering it — Xterm, `screen`, `tmux`, SSH), and
      console (the primary terminal physically/directly connected to a
      machine). Closes with a note that a CLI's own I/O model — stdin/
      stdout/stderr, tty detection — is the same regardless of which of
      these sits behind it, cross-referencing the "Piping" section for
      where that matters in practice. The direct `unix.stackexchange.com`
      fetch failed with HTTP 403 again this run, as it did previously; the
      content was retrieved via a Wayback Machine snapshot instead, which
      returned HTTP 200 with the full accepted answer. Source added to the
      page's `== References`.

## Partial

- [x] `__TODO__/principles.md:82` covers the "make it feel robust" framing more
      thoroughly than `01-principles.adoc:3-10` — specifically, the source's point that
      "above all, robustness is achieved by keeping it simple" and that complex code
      and special/edge cases make a program fragile and unpredictable. The standard's
      intro mirrors the attention-to-detail framing but omits the simplicity
      principle entirely.

      **Resolved.** Closed by a new "Simplicity" section in `01-principles.adoc`,
      as the first principle before "Composability". States that robustness is
      achieved above all by keeping the program simple, that complexity and
      special-case handling make a program fragile and unpredictable, and
      recommends rejecting rare input combinations outright with a clear error
      rather than special-casing them.

- [x] `__TODO__/principles.md:90` covers future-proofing more thoroughly than
      `01-principles.adoc:134` — specifically, the source's explicit statement that
      "we use Semantic Version for our CLI utilities." The standard discusses major
      versions enduring but never names Semantic Versioning as the versioning
      convention.

      **Resolved.** Closed by a new paragraph in the "Future proofing" section
      of `01-principles.adoc`, immediately after the existing "Major versions
      SHOULD endure..." paragraph. Names Semantic Versioning as the convention,
      links to semver.org, and states that major bumps are reserved for
      breaking interface changes (removed/renamed subcommands, flags, env
      vars; changed defaults; changed exit codes).

- [x] `__TODO__/principles.md:94` covers deprecation warnings more thoroughly than
      `01-principles.adoc:157` — specifically, the source's guidance to tell the user
      the flag is going to change when they pass it, to show them a future-proof
      alternative, and (where possible) to detect when they have updated their usage
      and stop showing the warning. The standard only says to "warn your users about
      deprecated operations."

      **Resolved.** Closed by expanding the deprecation-warning sentence in the
      "Future proofing" section of `01-principles.adoc` into a full paragraph:
      warn at the moment of use, show the future-proof alternative, and detect
      (where possible) when the user has already migrated so the warning stops
      nagging them.

- [x] `__TODO__/principles.md:114` covers time-bombs more thoroughly than
      `01-principles.adoc:160` — specifically, the concrete example "Don't build in a
      blocking call to Google Analytics either." The standard makes the general
      time-bomb point without any illustrative example.

      **Resolved.** Closed by extending the "Avoid creating time-bombs" paragraph
      in `01-principles.adoc` with an illustrative example: don't build in a
      blocking call to a third-party analytics service, since a discontinued or
      blocking service should not hang or fail the program. Generalized from
      "Google Analytics" to "a third-party analytics service" to avoid pinning
      the example to one vendor, consistent with the new Analytics section this
      run also added.

- [x] `__TODO__/options/README.md:29` covers defaults more thoroughly than
      `04-options.adoc:19` — specifically, the `ls` example illustrating that you
      can't always predict how programs will be used (`ls` was designed for terse
      scripting output but is most commonly run as `ls -lhF`). The standard states
      the "good defaults" principle without this illustrative example.

      **Resolved.** Closed by a new paragraph in the "Defaults" section of
      `04-options.adoc`, using the `ls`/`ls -lhF` example and generalizing it
      into a rule: let evidence about actual usage override assumptions about
      what the default should be.

- [x] `__TODO__/help.md:3` covers online documentation more thoroughly than
      `11-documentation.adoc:42` — specifically, the requirement that, for public
      applications, online documentation MUST be indexable by public search engines.
      The standard only says publishing extended documentation online is
      RECOMMENDED.

      **Resolved.** Closed by extending the online-documentation sentence in
      the "Help text" section of `11-documentation.adoc`: for public
      applications, online documentation MUST be indexable by public search
      engines.

- [x] `__TODO__/help.md:173` covers help-text scope more thoroughly than
      `11-documentation.adoc:40` — specifically, the guidance that common options like
      `--version` and `--help` can be documented elsewhere, with just a link to the
      "full documentation" in the help text. The standard says only the most useful
      options need appear in the signature, but does not call out deferring common
      options with a link.

      **Resolved.** Closed by extending the "not necessary to document every
      option" sentence in the "Help text" section of `11-documentation.adoc`
      to call out that common cross-cutting options like `--version` and
      `--help` can be documented once elsewhere, with help text linking to
      the full documentation instead of repeating them.

- [x] https://clig.dev/#the-basics, reinforced by
      https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html
      — use a command-line argument-parsing library (the language's built-in or a
      good third-party one; GNU names `getopt`/`getopt_long`). The standard specifies
      flag-parsing conventions but never recommends using a parsing library, which
      both sources call the easiest way to handle args, flags, help text, and
      spelling suggestions sensibly. Recommend adding to `04-options.adoc:22`
      (Arguments and flags).

      **Resolved.** Closed by a new paragraph at the top of the "Arguments and
      flags" section of `04-options.adoc`. Recommends using a language-native
      or well-established third-party argument-parsing library rather than
      hand-rolling parsing, naming the classes of behavior it handles
      consistently (flag forms, help-text generation, spelling suggestions).

- [x] https://clig.dev/#arguments-and-flags — the standard's common-flags table
      (`04-options.adoc:88`) omits `-n`/`--dry-run`, which clig.dev lists as a
      standard flag ("do not run the command but describe the changes that would
      occur", e.g. `rsync`, `git add`). The standard mentions `--dry-run` in prose
      (`06-interactivity.adoc:37`) but not in the table, and gives no `-n` shorthand.

      **Resolved.** Closed by adding a `--dry-run`/`-n` row to the common-flags
      table in `04-options.adoc`, with the `rsync`/`git add` examples.

- [x] https://clig.dev/#arguments-and-flags — the standard covers basic
      confirmation (`y`/`yes`, `--force`) at `06-interactivity.adoc:33` but omits
      clig.dev's gradation of danger: _mild_ (small local change — may not need
      prompting if the user explicitly ran a "delete" command), _moderate_ (deleting a
      directory, remote change, bulk modification that can't be easily undone —
      usually prompt; consider a dry-run), and _severe_ (deleting something complex
      like an entire remote app — make confirmation hard to do by accident; ask the
      user to type something non-trivial like the name of the thing being deleted;
      allow a `--confirm="name"` flag so it is still scriptable). Also reinforced by
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VII, type
      the app name to confirm destroying a Heroku app).

      **Resolved.** Closed by a new paragraph and bulleted list in the
      "Prompts" section of `06-interactivity.adoc`, after the existing
      confirmation paragraph. Covers the mild/moderate/severe gradation, the
      "type the name to confirm" pattern for severe operations, and the
      `--confirm=<name>` scriptable escape hatch (12-factor's Heroku example
      folded into the severe case rather than kept as a separate mention).

- [x] https://clig.dev/#robustness-1 — if a progress bar gets stuck in one place for
      a long time, the user cannot tell whether work is still happening or the
      program has crashed; show estimated time remaining or an animated component to
      reassure them. The standard says to keep the user informed of long operations
      (`01-principles.adoc:86`) but does not address the stuck-progress-bar case.

      **Resolved.** Closed by a new paragraph in the "Animations" section of
      `09-output.adoc`. Addresses the stuck-progress-bar problem and
      recommends showing estimated time remaining or keeping some part of the
      display animated.

- [x] https://clig.dev/#robustness-1 — reporting progress for parallel processes is
      much harder than for sequential; ensure output is robust and not confusingly
      interleaved (use a library for parallel progress where possible). The
      standard's Parallelism section (`01-principles.adoc:100`) says to parallelize
      only when reliable but does not address the parallel-progress-reporting
      difficulty or interleaved output.

      **Resolved.** Closed by a new paragraph in the "Animations" section of
      `09-output.adoc`, addressing progress reporting for parallel work
      specifically (rather than the Parallelism section in `01-principles.adoc`,
      which is about when to parallelize, not how to report on it). Warns
      against naive interleaved output and recommends a purpose-built library.

- [x] https://clig.dev/#robustness-1 — hiding logs behind progress bars when things
      go well makes output easier to understand, but if there is an error, print the
      logs out (otherwise it is very hard to debug). Not addressed in the standard.

      **Resolved.** Closed by a new paragraph in the "Animations" section of
      `09-output.adoc`. States that hiding logs behind a progress bar is fine
      when things go well, but the hidden logs must be printed on error.

- [x] https://clig.dev/#help and https://clig.dev/#documentation — a `help` subcommand
      (e.g. `myapp help`, `myapp help subcommand`, equivalent to `myapp subcommand
      --help`), as popularized by git and npm (`npm help ls` == `man npm-ls`). The
      standard covers `--help`/`-h` flags (`11-documentation.adoc:35`) but not the
      `help` subcommand pattern.

      **Resolved.** Closed by a new paragraph in the "Help text" section of
      `11-documentation.adoc`, after the formatting-and-heroku-example
      paragraph. Recommends offering a `help` subcommand alongside
      `--help`/`-h`, with the git/npm precedent.

- [x] https://clig.dev/#documentation — tools to generate man pages from `--help`
      output (clig.dev names `ronn`; GNU names `help2man`). The standard treats man
      pages as an optional extra (`11-documentation.adoc:45`) but does not mention
      generation tooling, which both sources recommend as the low-effort path.

      **Resolved.** Closed by extending the man-pages paragraph in the "Help
      text" section of `11-documentation.adoc` with a sentence naming
      `help2man` and `ronn` as low-effort generation tools.

- [x] https://clig.dev/#documentation — terminal-based documentation has the
      specific benefit of staying in sync with the installed version and working
      offline. The standard recommends online docs but does not articulate why
      built-in docs matter (always version-matched, offline-capable).

      **Resolved.** Closed by a new paragraph in the "Help text" section of
      `11-documentation.adoc`, between the online-docs paragraph and the
      man-pages paragraph. States built-in documentation's two advantages:
      always matches the installed version, and works offline.

- [x] https://clig.dev/#interactivity — "let the user escape; make it clear how to
      get out (don't do what vim does)." The standard's signals section
      (`06-interactivity.adoc:44`) covers `Ctrl+C` escape but not the broader
      "make the exit path obvious / don't trap the user" guidance.

      **Resolved.** Closed by a new sentence in the "Signals" section of
      `06-interactivity.adoc`, appended to the opening paragraph: make the
      exit path obvious, and don't trap the user in a mode with no visible
      way back to the shell.

- [x] https://clig.dev/#interactivity — for wrappers around program execution where
      `Ctrl+C` cannot quit (SSH, tmux, telnet), make the escape route clear (e.g.
      SSH's `~` escape sequences). The standard covers `Ctrl+C` for normal CLIs but
      not this wrapper exception.

      **Resolved.** Closed by a new paragraph in the "Signals" section of
      `06-interactivity.adoc`. Covers the wrapper exception (SSH, tmux,
      telnet) and the SSH `~` escape-sequence precedent.

- [x] https://clig.dev/#signals-and-control-characters — when the user hits `Ctrl+C`
      during clean-up that might take a long time, tell the user what will happen when
      they hit `Ctrl+C` again, in case it is a destructive action (e.g. Docker
      Compose: a second `Ctrl+C` forces containers to stop immediately). The
      standard says to cancel clean-up on a second `Ctrl+C`
      (`06-interactivity.adoc:51`) but not to warn the user what the second press
      will do.

      **Resolved.** Closed by a new paragraph at the end of the "Signals"
      section of `06-interactivity.adoc`, after the existing clean-up
      paragraph. Uses the Docker Compose example and requires warning the
      user what a second `Ctrl+C` will do where it is destructive.

- [x] https://clig.dev/#environment-variables — `FORCE_COLOR` (force-enable color,
      ignoring TTY detection) is the counterpart to `NO_COLOR`. The standard
      (`09-output.adoc:69`) covers `NO_COLOR` and `[APP]_NO_COLOR` but not
      `FORCE_COLOR`.

      **Resolved.** Closed by a new paragraph in the "Formatting" section of
      `09-output.adoc`, after the color-disabling bullet list. Recommends
      supporting `FORCE_COLOR` as the counterpart to `NO_COLOR`, with the
      piped-into-a-pager example.

- [x] https://clig.dev/#environment-variables and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VI) —
      disable color when `TERM=dumb`. The standard lists `NO_COLOR` and
      `[APP]_NO_COLOR` (`09-output.adoc:74`) but never mentions the `TERM=dumb`
      convention.

      **Resolved.** Closed by a new bullet in the color-disabling list in the
      "Formatting" section of `09-output.adoc`: disable color when `TERM` is
      `dumb`.

- [x] https://clig.dev/#environment-variables — `SHELL` is for opening interactive
      sessions in the user's preferred shell, but if you need to execute a shell
      script, use a specific interpreter like `/bin/sh`. The standard lists `SHELL`
      (`04-options.adoc:274`) without this caveat.

      **Resolved.** Closed by a new paragraph after the environment-variables
      table in `04-options.adoc`. States `SHELL` is for opening interactive
      sessions, and that executing a script or one-off command should use a
      specific interpreter such as `/bin/sh` instead.

- [x] https://clig.dev/#environment-variables — `TERM`, `TERMINFO`, and `TERMCAP`
      should be checked when using terminal-specific escape sequences. The standard
      discusses TTY checks and color but does not mention these terminal-capability
      environment variables.

      **Resolved.** Closed by a new `TERM`, `TERMINFO`, `TERMCAP` row in the
      environment-variables table in `04-options.adoc`.

- [x] https://clig.dev/#environment-variables — secrets should be accepted only via
      credential files, pipes, `AF_UNIX` sockets, secret management services, or
      another IPC mechanism. The standard (`04-options.adoc:345`) names only files
      and stdin.

      **Resolved.** Closed by expanding the closing sentence of "Inputting
      secrets via environment variables" in `04-options.adoc` to list
      credential files, pipes (stdin), `AF_UNIX` sockets, and secret-management
      services or other IPC mechanisms, rather than only "files and stdin".

- [x] https://clig.dev/#naming and https://smallstep.com/blog/the-poetics-of-cli-command-names/
      — do not put emoji in command names (technically possible, but a bad idea). The
      standard discusses emoji in output (`09-output.adoc:78`) but not in command
      names.

      **Resolved.** Closed by a new bullet in the naming-guidelines list of
      `02-naming.adoc`: don't put emoji in a command name, cross-referencing
      the "Formatting" section where emoji in output is discussed.

- [x] https://smallstep.com/blog/the-poetics-of-cli-command-names/ — version numbers
      should not appear in command names (e.g. `python3.7m`), and version-suffixed
      names reveal the ecosystem's failure to support coexistence of multiple
      versions. The standard (`02-naming.adoc:15`) permits numbers but does not call
      out version-suffixed command names as an anti-pattern.

      **Resolved.** Closed by a new bullet in the naming-guidelines list of
      `02-naming.adoc`: don't version-suffix a command name, with the
      `python3.7m` example and the ecosystem-failure framing.

- [x] https://clig.dev/#consistency-across-programs — consistency _across programs_
      as a design principle ("where possible, a CLI should follow patterns that
      already exist; that's what makes CLIs intuitive and guessable"), and the
      corollary that when following convention would compromise usability it may be
      time to break with it, done with care. The standard covers consistency within
      a program and conventional flag names (`04-options.adoc:85`,
      `05-subcommands.adoc:9`) but not the cross-program principle or when to break
      convention.

      **Resolved.** Closed by a new "Consistency across programs" section in
      `02-naming.adoc`, after the `curl` example. States the cross-program
      consistency principle and the corollary for breaking convention
      deliberately when it would compromise usability.

- [x] https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_01
      — the standard's POSIX-notation coverage (`11-documentation.adoc:3`) omits
      the `|` notation for mutually-exclusive options and the convention of using
      multiple synopsis lines to indicate mutually-exclusive argument sets.

      **Resolved.** Closed by a new paragraph in the "CLI API signature
      notation" section of `11-documentation.adoc`, using the Git example's
      own `[-p | --paginate | -P | --no-pager]` to illustrate `|`, and covering
      the multiple-synopsis-line convention for argument sets that can't be
      expressed with `|`/`[]` alone.

- [x] https://www.gnu.org/prep/standards/html_node/_002d_002dversion.html and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor III) — the
      `--version` output format. The standard's flag table (`04-options.adoc:141`)
      lists `--version` as "Version" but specifies no output format. GNU details a
      format: a parseable first line (canonical program name — a constant string,
      not computed from `argv[0]` — followed by the version number), then a
      copyright line, then a license/no-warranty line; 12-factor adds that the
      version command is a good place for extra debugging info (and to send the
      version string as the `User-Agent` for server-side debugging). 12-factor also
      notes version should be reachable via a `version` subcommand and `-V`.

      **Resolved.** Closed by a new "`--version` output" subsection in
      `04-options.adoc`, after the common-flags table, plus a `-V` shorthand
      added to the `--version` table row. Covers the parseable-first-line
      format (constant program name, not `argv[0]`), the optional copyright/
      license lines, the debugging-info and `User-Agent` uses, and the
      `version` subcommand. GNU Coding Standards is already in the page's
      `== References` (as the index page, which covers this sub-page too);
      12-factor is already cited elsewhere in the page.

- [x] https://www.gnu.org/prep/standards/html_node/_002d_002dversion.html — once
      `--version` is seen, other options and arguments should be ignored and the
      program should exit successfully. The standard states this for `--help`
      (`11-documentation.adoc:98`) but not for `--version`.

      **Resolved.** Closed by the closing sentence of the new "`--version`
      output" subsection in `04-options.adoc`, cross-referencing the parallel
      `--help` rule in "Help text" rather than duplicating it.

- [x] https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html
      — file names given as ordinary arguments should usually be _input_ files only;
      output files should be specified via an option, preferably `-o`/`--output`,
      and even where an output file is accepted as an argument for compatibility, an
      option should also be provided. The standard's arguments section
      (`04-options.adoc:22`) does not draw this input-vs-output distinction.

      **Resolved.** Closed by a new paragraph in the "Arguments and flags"
      section of `04-options.adoc`. States ordinary file-path arguments should
      usually be treated as input only, and output files should be specified
      via an option (preferably `-o`/`--output`), with that option still
      provided even where an output-file argument is kept for compatibility.

- [x] https://www.gnu.org/prep/standards/html_node/Option-Table.html — `--silent`
      should be accepted as a synonym for `--quiet` (and vice versa). The standard's
      table (`04-options.adoc:131`) lists `--quiet`/`-q` but not `--silent`.

      **Resolved.** Closed by updating the `--quiet`/`-q` row in the
      common-flags table in `04-options.adoc` to `--quiet`, `--silent`.

- [x] https://www.gnu.org/prep/standards/html_node/Errors.html — interactive
      programs (reading commands from a terminal) should not include the program
      name in error messages; identity should be conveyed via the prompt or screen
      layout; and the same program reading from a non-terminal should switch to the
      noninteractive `program: message` style. The standard's error format
      (`10-errors.adoc:11`) always uses the `<program-name>:` prefix and does not
      distinguish interactive from noninteractive contexts.

      **Resolved.** Closed by a new paragraph in the "Error formatting"
      section of `10-errors.adoc`. Distinguishes interactive programs (REPL-style,
      no program name needed – the prompt conveys identity) from the same
      program reading from a non-terminal (switches to the `<program-name>:`
      style).

- [x] https://www.gnu.org/prep/standards/html_node/Errors.html — detailed
      source-position formatting for error messages (column numbers calculated with
      tab stops every 8 columns and equal-width ASCII characters; Unicode character
      widths in UTF-8 locales; start-and-end position formats such as
      `file:line1.column1-line2.column2`; multi-file spans such as
      `file1:line1.column1-file2:line2.column2`). The standard's error format
      (`10-errors.adoc:11`) gives only the basic `<program>: <file>:<line>:<column>:
      <message>` shape. Most relevant to tools that report source locations.

      **Resolved.** Closed by a new paragraph in the "Error formatting" section
      of `10-errors.adoc`, scoped explicitly to tools that report source
      locations. Covers tab-stop column calculation, UTF-8 character widths,
      and the start-and-end and multi-file span formats.

- [x] https://devcenter.heroku.com/articles/cli-style-guide#stdout-stderr,
      https://clig.dev/#output, and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor IV) —
      progress / spinner / "action" output is out-of-band information and should go
      to stderr (so stdout can be redirected while the user still sees progress;
      `curl` puts progress on stderr). The standard says primary output goes to
      stdout and errors to stderr (`09-output.adoc:3`, `10-errors.adoc:3`) but does
      not say where progress/spinner output should go.

      **Resolved.** Closed by a new paragraph in the "Animations" section of
      `09-output.adoc`. States progress/spinner/action output is out-of-band
      and belongs on stderr, not stdout, with the `curl` example.

- [x] https://devcenter.heroku.com/articles/cli-style-guide#grep-parseable —
      human-readable output should remain grep-parseable (one record per line);
      avoid multi-section grouped-header formats that break `grep` filtering (a
      single tabular row per item is better). The standard mentions `--plain` for
      `grep`/`awk` (`09-output.adoc:9`) but not the one-record-per-line discipline
      or the multi-section-header anti-pattern.

      **Resolved.** Closed by a new paragraph in the "Standard output" section
      of `09-output.adoc`, alongside the machine-readable-stability paragraph.
      States the one-record-per-line discipline and warns against
      multi-section grouped-header formats, cross-referencing the new Tables
      section.

- [x] https://devcenter.heroku.com/articles/cli-style-guide#naming-the-command and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor XI) — the
      delimiter for sub-subcommands: spaces (git: `git submodule add`) vs colons
      (heroku: `heroku domains:add`). 12-factor argues colons are preferable because
      they let a topic command accept an argument while also having subcommands
      (a space-based parser cannot disambiguate), and that one should never create a
      `*:list` command (the topic root lists the nouns). The standard's subcommand
      section (`05-subcommands.adoc:19`) covers two-level noun-verb subcommands but
      not the delimiter choice or the `*:list` convention.

      **Resolved.** Closed by a new paragraph in `05-subcommands.adoc`, after
      the noun-verb/verb-noun paragraph. Covers the space vs colon delimiter
      choice with the `heroku domains:add` example, the argument-plus-subcommand
      disambiguation rationale, and the `*:list` anti-pattern.

- [x] https://devcenter.heroku.com/articles/cli-style-guide#description —
      description/flag-description formatting conventions: fit 80-character widths,
      begin with lowercase, do not end with a period. The standard has wording
      conventions for error messages (`10-errors.adoc:50`) but none for help-text
      descriptions.

      **Resolved.** Closed by a sentence appended to the flags-description
      bullet in the "extended help text" list of `11-documentation.adoc`,
      cross-referencing the wording conventions in "Error message content"
      rather than duplicating them.

- [x] https://devcenter.heroku.com/articles/cli-style-guide#prompting and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VII) —
      interactive selection UIs (arrow-key prompts, checkboxes, radio buttons) for
      presenting options visually. The standard covers TTY-gated text prompts and
      the `--no-input` escape hatch (`06-interactivity.adoc:3`) but not richer
      interactive selection controls.

      **Resolved.** Closed by a new paragraph in the "Prompts" section of
      `06-interactivity.adoc`, after the password-prompting paragraph.
      Recommends arrow-key/checkbox/radio-button selection UIs for choosing
      between options, and requires the same TTY-gating and non-interactive
      flag equivalent as other prompts.

- [x] https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f
      — help discoverability for CLIs with very many commands. For 100+ commands,
      listing all commands is a non-starter; the article advocates "structured help"
      / eventual disclosure (showing only the immediate subcommands, not all of them
      at once) and visually grouped commands. The standard's help guidance
      (`11-documentation.adoc:35`) does not address the scaling problem of very
      large command sets.

      **Resolved.** Closed by a new paragraph in the "Help text" section of
      `11-documentation.adoc`, after the new `help`-subcommand paragraph.
      Recommends structured help / eventual disclosure for CLIs with very
      many commands, pointing at the `heroku --help` example already on the
      page as an existing illustration of grouped, topic-level display.

- [x] https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f
      — the noun-verb vs verb-noun choice has a maintenance/scaling criterion: if the
      nouns will always support all verbs, verb-first scales easily; if the nouns
      have very different verbs, noun-first is lower-maintenance. The standard
      (`05-subcommands.adoc:22`) notes noun-verb is "more common" but gives no
      scaling/maintenance rationale for the choice.

      **Resolved.** Closed by a new paragraph in `05-subcommands.adoc`,
      immediately after the existing noun-verb/verb-noun paragraph. States
      the scaling criterion: verb-first when every noun supports the same
      verbs, noun-first when verb sets differ per noun.

- [x] https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f
      — providing an automated migration command that rewrites users' shell scripts
      to use new commands (e.g. `ibmcloud ks script update`). The standard covers
      deprecation warnings (`01-principles.adoc:157`) but not the option of shipping
      an automated migration tool.

      **Resolved.** Closed by a new paragraph at the end of `05-subcommands.adoc`,
      after the abbreviations/aliases paragraph. Recommends an automated
      migration command for script rewrites, cross-referencing the
      deprecation-warning guidance in "Future proofing" as the lighter-weight
      alternative.

- [x] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor V) — a
      structured error message format: error code, error title, error description
      (optional), how to fix, and a URL for more information. The standard's error
      content (`10-errors.adoc:29`) says a good error communicates "what went wrong,
      where, and what to do next" and mentions stable error-code pages
      (`10-errors.adoc:141`), but does not prescribe including an error code in the
      message itself or the structured code/title/fix/URL shape.

      **Resolved.** Closed by a new paragraph in the "Error message content"
      section of `10-errors.adoc`. Recommends structuring complex error
      messages around error code, title, optional description, and how to
      fix, cross-referencing "Supporting bug reporting" for the stable
      error-code page URL rather than duplicating that guidance.

- [x] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor V) — for
      unhandled errors, provide full traceback/debug output via an environment
      variable (e.g. `DEBUG`). The standard (`10-errors.adoc:91`) hides stack traces
      behind a `--verbose`/`--debug` flag but does not mention the env-var approach.

      **Resolved.** Closed by extending the "Signal-to-noise ratio" section's
      sentence on hiding stack traces in `10-errors.adoc` to also name a
      `DEBUG` environment variable as an equivalent to the `--verbose`/`--debug`
      flags.

- [x] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor V) — error
      log files for post-mortem debugging must have timestamps, be truncated
      occasionally so they do not eat disk space, and must not contain ANSI color
      codes. The standard says not to treat stderr like a log file (`10-errors.adoc:46`)
      but does not address error log files.

      **Resolved.** Closed by a new paragraph immediately after "Do not treat
      stderr like a log file" in `10-errors.adoc`. Requires timestamps,
      truncation/rotation, and no ANSI color codes in error log files.

- [x] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor IX) — CLI
      startup-time benchmarks: <100ms very fast, 100–500ms the target, 500ms–2s
      usable, 2s+ languid (users will avoid the CLI). The standard's responsiveness
      rule (`01-principles.adoc:86`) covers in-interaction latency (<100ms to
      feedback) but not cold-start / startup-time latency.

      **Resolved.** Closed by a new paragraph in the "Be responsive" section of
      `01-principles.adoc`, after the existing "A responsive program _feels_
      robust..." sentence. States the same benchmark bands (under 100ms
      instant, 100–500ms target, 500ms–2s usable but noticeable, beyond 2s
      users avoid the tool) and notes startup time matters most for
      frequently-invoked CLIs (shell prompts, git hooks, editor integrations).

- [x] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor XII) — the
      XDG directory structure beyond config: `~/.local/share/myapp` for data files
      and `~/.cache/myapp` for cache files, with cross-platform cache locations
      (`~/Library/Caches/myapp` on macOS, `%LOCALAPPDATA%\myapp` on Windows). The
      standard (`04-options.adoc:208`) references the XDG Base Directory spec only
      for config files and does not mention data or cache directories or the
      non-Linux equivalents.

      **Resolved.** Closed by a new paragraph after the XDG links in the
      "User-level and system-wide configuration" section of `04-options.adoc`.
      Covers `~/.local/share/<app>` for data and `~/.cache/<app>` for cache,
      the "safe to delete" framing for cache, and the macOS/Windows
      equivalents for platforms that don't follow the XDG specification.

- [x] https://smallstep.com/blog/the-poetics-of-cli-command-names/ — it is
      acceptable to signal the solution domain in a command name when the name is
      both literal and niche (e.g. `mkfs`), and conversely a deliberately
      meaningless but easy-to-type name (e.g. `emacs`, `step`) is a sound choice
      when the solution domain is expected to evolve. The standard's naming rules
      (`02-naming.adoc:9`, "don't name after a standard, protocol, or file format")
      do not acknowledge these exceptions.

      **Resolved.** Closed by extending the "don't name after a standard,
      protocol, or file format" bullet in `02-naming.adoc` with the two
      exceptions: a literal-and-niche name (`mkfs`), and a deliberately
      meaningless, easy-to-type name (`emacs`) when the solution domain is
      expected to evolve.

- [x] https://clig.dev/#distribution — the single-binary distribution ideal, the
      use of bundlers like PyInstaller for languages that do not compile to
      binaries, and the exception that language-specific tools (e.g. a code linter)
      need not follow the single-binary rule (the user can be assumed to have the
      interpreter). The standard (`03-distribution.adoc:5`) says distribute as
      binaries or via the native package manager but does not articulate the
      single-binary ideal, the bundler fallback, or the language-tool exception.

      **Resolved.** Closed by two new paragraphs in `03-distribution.adoc`,
      after the existing binaries/native-package-manager paragraph. States the
      single-binary ideal, the PyInstaller-style bundler fallback for
      non-compiled languages, and the language-specific-tool exception (eg.
      npm/pip distribution for a linter).

- [x] https://clig.dev/#distribution — if uninstall needs instructions, put them at
      the bottom of the install instructions (one of the most common times people
      want to uninstall is right after installing). The standard says CLIs must be
      easy to uninstall (`03-distribution.adoc:3`) but gives no placement guidance
      for uninstall instructions.

      **Resolved.** Closed by extending the opening sentence of
      `03-distribution.adoc` with placement guidance: put uninstall
      instructions at the bottom of the install instructions.

## Out-of-scope

- [x] `__TODO__/principles.md` cross-references companion programming-principle
      standards (`crash-only.md`, `defensive-programming.md`, `simplicity.md`,
      `programming/principles/README.md`) and `__TODO__/options/README.md` references
      `delivery/versioning.md`. These are cross-links to a broader standards system
      on general programming principles, not CLI-specific guidance. They plausibly
      sit outside TS-16's stated purpose — flagged for the user to confirm whether
      TS-16 should add cross-references to companion standards on simplicity,
      defensive programming, crash-only design, and versioning.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://en.wikipedia.org/wiki/The_Unix_Programming_Environment — this is a
      Wikipedia article about a 1984 book (its contents, historical context, C
      programming style, critical reception, editions), not CLI design guidance.
      Its one in-scope essence — the Unix philosophy of small cooperating tools with
      standardized I/O, and power coming from relationships among programs — is
      already covered by the standard's Composability principle
      (`01-principles.adoc:12`). The rest is background/reference.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://unix.stackexchange.com/a/4132 — definitions of terminal, shell, tty,
      console, pseudo-ttys, terminal emulators, and the division of labor between
      terminal and shell. This is foundational background the standard assumes its
      technical audience already knows; it is not CLI interface design guidance.
      Flagged for the user to confirm whether TS-16 should add a "Terminology"
      section.

      **Overruled, 2026-08-15.** The user asked for a new "Terminology"
      section to be added. Filed as a new Missing item below, to be
      written up via `close-gaps`.

- [x] https://devcenter.heroku.com/articles/cli-style-guide#dependency-guidelines
      — Node/oclif dependency-management guidance (native dependencies,
      judiciousness, dev dependencies, discouraged packages like `request`/
      `underscore`). This is implementation/library guidance, not CLI interface
      design.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor X,
      "Encourage contributions") — open-sourcing the CLI, picking a license,
      hosting on GitHub/GitLab, contribution guidelines, code of conduct, plugin
      systems. This is project/community process, not CLI interface design.

      **Overruled, 2026-08-15 — not yet routed.** The user agreed this
      doesn't belong in TS-16, but felt existing standards may not have a
      good home for open-source project process (licensing, contribution
      guidelines, code of conduct, plugin systems) either, and floated
      that a new standard might be needed. Left unrouted pending that
      decision — not filed against any other standard's `GAPS.md` yet.

- [x] https://www.gnu.org/prep/standards/html_node/Names.html — naming of C source
      variables, functions, and files (underscores, lower case, `enum` vs `#define`,
      14-char file-name limits, `doschk`). This is internal code naming, not CLI
      command/interface naming.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://www.gnu.org/prep/standards/html_node/Using-Extensions.html — when to
      use GNU/C language extensions vs portable constructs. C/GNU-extension usage
      policy, not CLI design.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://www.gnu.org/prep/standards/html_node/_002d_002dversion.html — the
      exhaustive table of license abbreviations (`GPL`, `LGPL`, `Apache`, `MPL`,
      etc.) and the legal rules for `--version` copyright notices (the word
      "Copyright" must be in English per international treaty, `(C)` vs `©`). Legal
     /licensing specifics; the standard would only need the high-level
      `--version` format (captured as a partial gap above), not the license
      taxonomy.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f
      — case-study-specific details (the IBM Cloud Kubernetes Service CLI's beta
      environment variable, code-churn statistics, Slack channels, contributor
      names) and the "always run user tests / provide tools / leave plenty of time"
      process advice. Project-specific or process guidance, not CLI interface
      rules.

      **Confirmed out-of-scope.** 2026-08-15.

## Unresolved

- [x] https://www.gnu.org/prep/standards/html_node/Program-Behavior.html could not
      be fetched directly from this environment (the `fetch` tool returned a send
      error; repeated `curl` attempts returned HTTP 000 — connection failure). It
      is a table-of-contents node for §4.5 "Program Behavior for All Programs"; its
      CLI-relevant content ("Standards for Command Line Interfaces") was captured
      via the GNU Coding Standards index sub-agent, so the analysis is not
      materially affected. If a future run can fetch it directly, re-verify there
      is no unique content missed.

      **Dismissed.** 2026-08-15. Re-attempted three times via WebFetch (429
      Too Many Requests each time, including after 5s, 15s, and 20s backoffs)
      and once via direct `curl` with a browser User-Agent (403 Forbidden).
      This confirms the failure is persistent from this environment, not
      transient — matching the original finding. Since the page's
      CLI-relevant content was already captured via the GNU Coding Standards
      index sub-agent in an earlier run, no gap is left unaddressed.