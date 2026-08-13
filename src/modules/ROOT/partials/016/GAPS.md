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

**Status:** Second run, 2026-08-05. All first-run gaps from `__TODO__/` remain open (the
standard's files were not modified). New gaps from the 10 issue-#65 URLs are added below.
Note: `Program-Behavior.html` could not be fetched directly from this environment
(repeated connection failures — see Unresolved); its CLI-relevant content ("Standards for
Command Line Interfaces") was captured via the GNU Coding Standards index sub-agent, so
the analysis is not materially affected.

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

- [ ] https://clig.dev/#analytics — the standard has no guidance at all on usage
      analytics / telemetry / "phoning home". clig.dev devotes a whole section to it:
      do not phone home usage or crash data without consent; be explicit about what is
      collected, why, how anonymous, how anonymized, and retention; prefer opt-in, and
      if opt-out, clearly tell users and make it easy to disable; consider alternatives
      (instrumenting web docs or downloads, talking to users). Recommend a new
      "Analytics" section after `03-distribution.adoc` or within `01-principles.adoc`.

- [ ] https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_02
      (Guideline 10), reinforced by
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor II) — the
      `--` end-of-options delimiter. The standard never mentions bare `--` to separate
      options from operands, nor its use to pass remaining args to a subprocess
      (e.g. `heroku run -a myapp -- myscript.sh -a arg1`). Recommend a new subsection in
      `04-options.adoc` (Arguments and flags).

- [ ] https://clig.dev/#output — the "explicit actions" principle: reading or writing
      files the user did not explicitly pass as arguments, and talking to a remote
      server (e.g. to download a file), should usually be explicit (unless storing
      internal program state such as a cache). Not addressed anywhere in the standard.
      Recommend adding as a new principle in `01-principles.adoc` (after "Communicate
      state changes", L66) or in `04-options.adoc` (Arguments and flags).

- [ ] https://clig.dev/#output and https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46
      (Factor I) — shell completion / autocomplete. The standard covers discoverability
      via help text and suggestions but never mentions shell completion, which both
      sources call out as a major aid to discoverability and correct flag usage (e.g.
      typing `--app <tab><tab>` makes the next value unambiguous). Recommend a new
      subsection in `11-documentation.adoc`.

- [ ] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VIII) —
      tabular output conventions. The standard discusses `--json`/`--plain` but has no
      guidance on table output: one entry per row (so output pipes cleanly to `grep`
      and `wc`), never emit table borders, and the conventional flags for tables
      (`--columns`, `--no-truncate`, `--no-headers`, `--filter`, `--sort`, CSV output).
      Recommend a new "Tables" subsection in `09-output.adoc` (Formatting, L63).

- [ ] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VI) — OS
      / desktop notifications when a very long-running task completes. Not mentioned
      anywhere in the standard. Recommend placing in `09-output.adoc` (Animations, L101)
      or `06-interactivity.adoc`.

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

- [ ] https://clig.dev/#the-basics, reinforced by
      https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html
      — use a command-line argument-parsing library (the language's built-in or a
      good third-party one; GNU names `getopt`/`getopt_long`). The standard specifies
      flag-parsing conventions but never recommends using a parsing library, which
      both sources call the easiest way to handle args, flags, help text, and
      spelling suggestions sensibly. Recommend adding to `04-options.adoc:22`
      (Arguments and flags).

- [ ] https://clig.dev/#arguments-and-flags — the standard's common-flags table
      (`04-options.adoc:88`) omits `-n`/`--dry-run`, which clig.dev lists as a
      standard flag ("do not run the command but describe the changes that would
      occur", e.g. `rsync`, `git add`). The standard mentions `--dry-run` in prose
      (`06-interactivity.adoc:37`) but not in the table, and gives no `-n` shorthand.

- [ ] https://clig.dev/#arguments-and-flags — the standard covers basic
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

- [ ] https://clig.dev/#robustness-1 — if a progress bar gets stuck in one place for
      a long time, the user cannot tell whether work is still happening or the
      program has crashed; show estimated time remaining or an animated component to
      reassure them. The standard says to keep the user informed of long operations
      (`01-principles.adoc:86`) but does not address the stuck-progress-bar case.

- [ ] https://clig.dev/#robustness-1 — reporting progress for parallel processes is
      much harder than for sequential; ensure output is robust and not confusingly
      interleaved (use a library for parallel progress where possible). The
      standard's Parallelism section (`01-principles.adoc:100`) says to parallelize
      only when reliable but does not address the parallel-progress-reporting
      difficulty or interleaved output.

- [ ] https://clig.dev/#robustness-1 — hiding logs behind progress bars when things
      go well makes output easier to understand, but if there is an error, print the
      logs out (otherwise it is very hard to debug). Not addressed in the standard.

- [ ] https://clig.dev/#help and https://clig.dev/#documentation — a `help` subcommand
      (e.g. `myapp help`, `myapp help subcommand`, equivalent to `myapp subcommand
      --help`), as popularized by git and npm (`npm help ls` == `man npm-ls`). The
      standard covers `--help`/`-h` flags (`11-documentation.adoc:35`) but not the
      `help` subcommand pattern.

- [ ] https://clig.dev/#documentation — tools to generate man pages from `--help`
      output (clig.dev names `ronn`; GNU names `help2man`). The standard treats man
      pages as an optional extra (`11-documentation.adoc:45`) but does not mention
      generation tooling, which both sources recommend as the low-effort path.

- [ ] https://clig.dev/#documentation — terminal-based documentation has the
      specific benefit of staying in sync with the installed version and working
      offline. The standard recommends online docs but does not articulate why
      built-in docs matter (always version-matched, offline-capable).

- [ ] https://clig.dev/#interactivity — "let the user escape; make it clear how to
      get out (don't do what vim does)." The standard's signals section
      (`06-interactivity.adoc:44`) covers `Ctrl+C` escape but not the broader
      "make the exit path obvious / don't trap the user" guidance.

- [ ] https://clig.dev/#interactivity — for wrappers around program execution where
      `Ctrl+C` cannot quit (SSH, tmux, telnet), make the escape route clear (e.g.
      SSH's `~` escape sequences). The standard covers `Ctrl+C` for normal CLIs but
      not this wrapper exception.

- [ ] https://clig.dev/#signals-and-control-characters — when the user hits `Ctrl+C`
      during clean-up that might take a long time, tell the user what will happen when
      they hit `Ctrl+C` again, in case it is a destructive action (e.g. Docker
      Compose: a second `Ctrl+C` forces containers to stop immediately). The
      standard says to cancel clean-up on a second `Ctrl+C`
      (`06-interactivity.adoc:51`) but not to warn the user what the second press
      will do.

- [ ] https://clig.dev/#environment-variables — `FORCE_COLOR` (force-enable color,
      ignoring TTY detection) is the counterpart to `NO_COLOR`. The standard
      (`09-output.adoc:69`) covers `NO_COLOR` and `[APP]_NO_COLOR` but not
      `FORCE_COLOR`.

- [ ] https://clig.dev/#environment-variables and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VI) —
      disable color when `TERM=dumb`. The standard lists `NO_COLOR` and
      `[APP]_NO_COLOR` (`09-output.adoc:74`) but never mentions the `TERM=dumb`
      convention.

- [ ] https://clig.dev/#environment-variables — `SHELL` is for opening interactive
      sessions in the user's preferred shell, but if you need to execute a shell
      script, use a specific interpreter like `/bin/sh`. The standard lists `SHELL`
      (`04-options.adoc:274`) without this caveat.

- [ ] https://clig.dev/#environment-variables — `TERM`, `TERMINFO`, and `TERMCAP`
      should be checked when using terminal-specific escape sequences. The standard
      discusses TTY checks and color but does not mention these terminal-capability
      environment variables.

- [ ] https://clig.dev/#environment-variables — secrets should be accepted only via
      credential files, pipes, `AF_UNIX` sockets, secret management services, or
      another IPC mechanism. The standard (`04-options.adoc:345`) names only files
      and stdin.

- [ ] https://clig.dev/#naming and https://smallstep.com/blog/the-poetics-of-cli-command-names/
      — do not put emoji in command names (technically possible, but a bad idea). The
      standard discusses emoji in output (`09-output.adoc:78`) but not in command
      names.

- [ ] https://smallstep.com/blog/the-poetics-of-cli-command-names/ — version numbers
      should not appear in command names (e.g. `python3.7m`), and version-suffixed
      names reveal the ecosystem's failure to support coexistence of multiple
      versions. The standard (`02-naming.adoc:15`) permits numbers but does not call
      out version-suffixed command names as an anti-pattern.

- [ ] https://clig.dev/#consistency-across-programs — consistency _across programs_
      as a design principle ("where possible, a CLI should follow patterns that
      already exist; that's what makes CLIs intuitive and guessable"), and the
      corollary that when following convention would compromise usability it may be
      time to break with it, done with care. The standard covers consistency within
      a program and conventional flag names (`04-options.adoc:85`,
      `05-subcommands.adoc:9`) but not the cross-program principle or when to break
      convention.

- [ ] https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_01
      — the standard's POSIX-notation coverage (`11-documentation.adoc:3`) omits
      the `|` notation for mutually-exclusive options and the convention of using
      multiple synopsis lines to indicate mutually-exclusive argument sets.

- [ ] https://www.gnu.org/prep/standards/html_node/_002d_002dversion.html and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor III) — the
      `--version` output format. The standard's flag table (`04-options.adoc:141`)
      lists `--version` as "Version" but specifies no output format. GNU details a
      format: a parseable first line (canonical program name — a constant string,
      not computed from `argv[0]` — followed by the version number), then a
      copyright line, then a license/no-warranty line; 12-factor adds that the
      version command is a good place for extra debugging info (and to send the
      version string as the `User-Agent` for server-side debugging). 12-factor also
      notes version should be reachable via a `version` subcommand and `-V`.

- [ ] https://www.gnu.org/prep/standards/html_node/_002d_002dversion.html — once
      `--version` is seen, other options and arguments should be ignored and the
      program should exit successfully. The standard states this for `--help`
      (`11-documentation.adoc:98`) but not for `--version`.

- [ ] https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html
      — file names given as ordinary arguments should usually be _input_ files only;
      output files should be specified via an option, preferably `-o`/`--output`,
      and even where an output file is accepted as an argument for compatibility, an
      option should also be provided. The standard's arguments section
      (`04-options.adoc:22`) does not draw this input-vs-output distinction.

- [ ] https://www.gnu.org/prep/standards/html_node/Option-Table.html — `--silent`
      should be accepted as a synonym for `--quiet` (and vice versa). The standard's
      table (`04-options.adoc:131`) lists `--quiet`/`-q` but not `--silent`.

- [ ] https://www.gnu.org/prep/standards/html_node/Errors.html — interactive
      programs (reading commands from a terminal) should not include the program
      name in error messages; identity should be conveyed via the prompt or screen
      layout; and the same program reading from a non-terminal should switch to the
      noninteractive `program: message` style. The standard's error format
      (`10-errors.adoc:11`) always uses the `<program-name>:` prefix and does not
      distinguish interactive from noninteractive contexts.

- [ ] https://www.gnu.org/prep/standards/html_node/Errors.html — detailed
      source-position formatting for error messages (column numbers calculated with
      tab stops every 8 columns and equal-width ASCII characters; Unicode character
      widths in UTF-8 locales; start-and-end position formats such as
      `file:line1.column1-line2.column2`; multi-file spans such as
      `file1:line1.column1-file2:line2.column2`). The standard's error format
      (`10-errors.adoc:11`) gives only the basic `<program>: <file>:<line>:<column>:
      <message>` shape. Most relevant to tools that report source locations.

- [ ] https://devcenter.heroku.com/articles/cli-style-guide#stdout-stderr,
      https://clig.dev/#output, and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor IV) —
      progress / spinner / "action" output is out-of-band information and should go
      to stderr (so stdout can be redirected while the user still sees progress;
      `curl` puts progress on stderr). The standard says primary output goes to
      stdout and errors to stderr (`09-output.adoc:3`, `10-errors.adoc:3`) but does
      not say where progress/spinner output should go.

- [ ] https://devcenter.heroku.com/articles/cli-style-guide#grep-parseable —
      human-readable output should remain grep-parseable (one record per line);
      avoid multi-section grouped-header formats that break `grep` filtering (a
      single tabular row per item is better). The standard mentions `--plain` for
      `grep`/`awk` (`09-output.adoc:9`) but not the one-record-per-line discipline
      or the multi-section-header anti-pattern.

- [ ] https://devcenter.heroku.com/articles/cli-style-guide#naming-the-command and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor XI) — the
      delimiter for sub-subcommands: spaces (git: `git submodule add`) vs colons
      (heroku: `heroku domains:add`). 12-factor argues colons are preferable because
      they let a topic command accept an argument while also having subcommands
      (a space-based parser cannot disambiguate), and that one should never create a
      `*:list` command (the topic root lists the nouns). The standard's subcommand
      section (`05-subcommands.adoc:19`) covers two-level noun-verb subcommands but
      not the delimiter choice or the `*:list` convention.

- [ ] https://devcenter.heroku.com/articles/cli-style-guide#description —
      description/flag-description formatting conventions: fit 80-character widths,
      begin with lowercase, do not end with a period. The standard has wording
      conventions for error messages (`10-errors.adoc:50`) but none for help-text
      descriptions.

- [ ] https://devcenter.heroku.com/articles/cli-style-guide#prompting and
      https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor VII) —
      interactive selection UIs (arrow-key prompts, checkboxes, radio buttons) for
      presenting options visually. The standard covers TTY-gated text prompts and
      the `--no-input` escape hatch (`06-interactivity.adoc:3`) but not richer
      interactive selection controls.

- [ ] https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f
      — help discoverability for CLIs with very many commands. For 100+ commands,
      listing all commands is a non-starter; the article advocates "structured help"
      / eventual disclosure (showing only the immediate subcommands, not all of them
      at once) and visually grouped commands. The standard's help guidance
      (`11-documentation.adoc:35`) does not address the scaling problem of very
      large command sets.

- [ ] https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f
      — the noun-verb vs verb-noun choice has a maintenance/scaling criterion: if the
      nouns will always support all verbs, verb-first scales easily; if the nouns
      have very different verbs, noun-first is lower-maintenance. The standard
      (`05-subcommands.adoc:22`) notes noun-verb is "more common" but gives no
      scaling/maintenance rationale for the choice.

- [ ] https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f
      — providing an automated migration command that rewrites users' shell scripts
      to use new commands (e.g. `ibmcloud ks script update`). The standard covers
      deprecation warnings (`01-principles.adoc:157`) but not the option of shipping
      an automated migration tool.

- [ ] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor V) — a
      structured error message format: error code, error title, error description
      (optional), how to fix, and a URL for more information. The standard's error
      content (`10-errors.adoc:29`) says a good error communicates "what went wrong,
      where, and what to do next" and mentions stable error-code pages
      (`10-errors.adoc:141`), but does not prescribe including an error code in the
      message itself or the structured code/title/fix/URL shape.

- [ ] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor V) — for
      unhandled errors, provide full traceback/debug output via an environment
      variable (e.g. `DEBUG`). The standard (`10-errors.adoc:91`) hides stack traces
      behind a `--verbose`/`--debug` flag but does not mention the env-var approach.

- [ ] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor V) — error
      log files for post-mortem debugging must have timestamps, be truncated
      occasionally so they do not eat disk space, and must not contain ANSI color
      codes. The standard says not to treat stderr like a log file (`10-errors.adoc:46`)
      but does not address error log files.

- [ ] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor IX) — CLI
      startup-time benchmarks: <100ms very fast, 100–500ms the target, 500ms–2s
      usable, 2s+ languid (users will avoid the CLI). The standard's responsiveness
      rule (`01-principles.adoc:86`) covers in-interaction latency (<100ms to
      feedback) but not cold-start / startup-time latency.

- [ ] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor XII) — the
      XDG directory structure beyond config: `~/.local/share/myapp` for data files
      and `~/.cache/myapp` for cache files, with cross-platform cache locations
      (`~/Library/Caches/myapp` on macOS, `%LOCALAPPDATA%\myapp` on Windows). The
      standard (`04-options.adoc:208`) references the XDG Base Directory spec only
      for config files and does not mention data or cache directories or the
      non-Linux equivalents.

- [ ] https://smallstep.com/blog/the-poetics-of-cli-command-names/ — it is
      acceptable to signal the solution domain in a command name when the name is
      both literal and niche (e.g. `mkfs`), and conversely a deliberately
      meaningless but easy-to-type name (e.g. `emacs`, `step`) is a sound choice
      when the solution domain is expected to evolve. The standard's naming rules
      (`02-naming.adoc:9`, "don't name after a standard, protocol, or file format")
      do not acknowledge these exceptions.

- [ ] https://clig.dev/#distribution — the single-binary distribution ideal, the
      use of bundlers like PyInstaller for languages that do not compile to
      binaries, and the exception that language-specific tools (e.g. a code linter)
      need not follow the single-binary rule (the user can be assumed to have the
      interpreter). The standard (`03-distribution.adoc:5`) says distribute as
      binaries or via the native package manager but does not articulate the
      single-binary ideal, the bundler fallback, or the language-tool exception.

- [ ] https://clig.dev/#distribution — if uninstall needs instructions, put them at
      the bottom of the install instructions (one of the most common times people
      want to uninstall is right after installing). The standard says CLIs must be
      easy to uninstall (`03-distribution.adoc:3`) but gives no placement guidance
      for uninstall instructions.

## Out-of-scope

- [ ] `__TODO__/principles.md` cross-references companion programming-principle
      standards (`crash-only.md`, `defensive-programming.md`, `simplicity.md`,
      `programming/principles/README.md`) and `__TODO__/options/README.md` references
      `delivery/versioning.md`. These are cross-links to a broader standards system
      on general programming principles, not CLI-specific guidance. They plausibly
      sit outside TS-16's stated purpose — flagged for the user to confirm whether
      TS-16 should add cross-references to companion standards on simplicity,
      defensive programming, crash-only design, and versioning.

- [ ] https://en.wikipedia.org/wiki/The_Unix_Programming_Environment — this is a
      Wikipedia article about a 1984 book (its contents, historical context, C
      programming style, critical reception, editions), not CLI design guidance.
      Its one in-scope essence — the Unix philosophy of small cooperating tools with
      standardized I/O, and power coming from relationships among programs — is
      already covered by the standard's Composability principle
      (`01-principles.adoc:12`). The rest is background/reference.

- [ ] https://unix.stackexchange.com/a/4132 — definitions of terminal, shell, tty,
      console, pseudo-ttys, terminal emulators, and the division of labor between
      terminal and shell. This is foundational background the standard assumes its
      technical audience already knows; it is not CLI interface design guidance.
      Flagged for the user to confirm whether TS-16 should add a "Terminology"
      section.

- [ ] https://devcenter.heroku.com/articles/cli-style-guide#dependency-guidelines
      — Node/oclif dependency-management guidance (native dependencies,
      judiciousness, dev dependencies, discouraged packages like `request`/
      `underscore`). This is implementation/library guidance, not CLI interface
      design.

- [ ] https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46 (Factor X,
      "Encourage contributions") — open-sourcing the CLI, picking a license,
      hosting on GitHub/GitLab, contribution guidelines, code of conduct, plugin
      systems. This is project/community process, not CLI interface design.

- [ ] https://www.gnu.org/prep/standards/html_node/Names.html — naming of C source
      variables, functions, and files (underscores, lower case, `enum` vs `#define`,
      14-char file-name limits, `doschk`). This is internal code naming, not CLI
      command/interface naming.

- [ ] https://www.gnu.org/prep/standards/html_node/Using-Extensions.html — when to
      use GNU/C language extensions vs portable constructs. C/GNU-extension usage
      policy, not CLI design.

- [ ] https://www.gnu.org/prep/standards/html_node/_002d_002dversion.html — the
      exhaustive table of license abbreviations (`GPL`, `LGPL`, `Apache`, `MPL`,
      etc.) and the legal rules for `--version` copyright notices (the word
      "Copyright" must be in English per international treaty, `(C)` vs `©`). Legal
     /licensing specifics; the standard would only need the high-level
      `--version` format (captured as a partial gap above), not the license
      taxonomy.

- [ ] https://uxdesign.cc/user-experience-clis-and-breaking-the-world-baed8709244f
      — case-study-specific details (the IBM Cloud Kubernetes Service CLI's beta
      environment variable, code-churn statistics, Slack channels, contributor
      names) and the "always run user tests / provide tools / leave plenty of time"
      process advice. Project-specific or process guidance, not CLI interface
      rules.

## Unresolved

- [ ] https://www.gnu.org/prep/standards/html_node/Program-Behavior.html could not
      be fetched directly from this environment (the `fetch` tool returned a send
      error; repeated `curl` attempts returned HTTP 000 — connection failure). It
      is a table-of-contents node for §4.5 "Program Behavior for All Programs"; its
      CLI-relevant content ("Standards for Command Line Interfaces") was captured
      via the GNU Coding Standards index sub-agent, so the analysis is not
      materially affected. If a future run can fetch it directly, re-verify there
      is no unique content missed.