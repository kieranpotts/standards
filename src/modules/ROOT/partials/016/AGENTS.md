# TS-16: Command Line Interfaces (CLIs)

This is a compact version of technical standard TS-16 for AI agents.

Use this when designing, writing, or reviewing command line interfaces —
principles, naming, distribution, options (arguments/flags/config/env vars),
subcommands, interactivity, piping, exit codes, output, errors, and
documentation. Focused on Unix-based environments but applicable to CLIs in all
environments (Windows, Node.js, Python, Java, etc.). Builds on the
[Command Line Interface Guidelines](https://clig.dev/).

Do NOT use this for terminal user interfaces (TUIs — full-screen terminal
programs like Vim and Emacs); this standard covers interactive command-oriented
CLI utilities only. CLIs are a type of UI — see
[TS-15: User Interfaces](../015/AGENTS.md) for broader UI guidance.

## Rules

### Principles

- **Design CLIs to be composable.**

  Each program and subcommand should do a small amount of work independently,
  but combine with others to compose more complex operations — they may be
  used in ways you did not anticipate. A key tenet of the Unix philosophy, as
  relevant as ever in the age of CI/CD pipelines and container orchestration.
  Achieved by following standard conventions for inputs and outputs: standard
  in/out/err, signals, exit codes, arguments and flags, environment variables.

- **Design CLIs as conversations with human users.**

  Even programs intended for automation have client programs developed by real
  people — those people are the users. The UX should be like a conversation:
  the output of one command should guide the user to their next command. When
  the user inputs invalid data or an unsupported subcommand, provide helpful
  suggestions. If the user enters an invalid command name, the program SHOULD
  suggest valid commands with similar spellings or semantics (eg. `ststus` →
  suggest `status`). But MUST NOT run the alternative operation without the
  user's explicit approval, unless it is a documented alias — assumptions about
  intention can be dangerous, especially where operations modify state.

- **Make CLIs discoverable and self-documenting.**

  Good help texts with lots of examples, suggestions on what commands the user
  might like to run next, and how to fix errors — all help users _discover_ a
  program for themselves.

- **Communicate state changes; make state easy to inspect.**

  If the program changes state, inform the user — especially when entering
  intermediate state while waiting for input, or when a failure puts the system
  into an invalid state. Make it easy to inspect current state (`git status` is
  a good model).

- **Let users control output amount and format.**

  The optimum balance between too much and too little output varies by use case.
  Users SHOULD be able to control the amount (`--quiet` / `--verbose` flags)
  and MAY be able to control the format (`--plain`, `--json`).

- **Be responsive.**

  Respond to user input in under 100ms and keep the user informed of long
  operations (eg. progress bars). For network requests, try non-blocking; if
  not possible, print something before initializing the request so the UI
  doesn't hang and look broken if it times out. Set sensible default network
  timeouts and allow the user to override them. A responsive program _feels_
  robust and dependable.

- **Do stuff in parallel where reliable; prioritize responsiveness and
  robustness over speed.**

  Only parallelize if it can be done reliably.

- **Design as "crash-only".**

  The program should exit immediately on failure or user interruption
  (`Ctrl+C`). Safer, and makes programs _feel_ more responsive and robust.

- **Make requests idempotent where possible.**

  If a command fails, the user should be able to retry by pressing `Up` and
  `Enter` without causing unintended side effects.

- **Practice defensive programming.**

  Think through all the ways users could misuse it: used in a script; bad
  network connection; multiple instances at once; unsupported environments.
  Plan and test for these scenarios. Fail gracefully whenever the program
  cannot handle input or cannot guarantee correct operation.

- **Future-proof: keep interfaces stable; keep changes additive.**

  Subcommands, arguments, flags, configuration files, environment variables —
  these are all interfaces, and once you start using them you are committing to
  keeping them stable. CLIs are commonly dependencies of other programs. Major
  versions SHOULD endure with non-breaking changes for as long as possible —
  preferably indefinitely, for the whole lifespan of the program ("We do not
  break userspace." — Linus Torvalds). Keep changes additive: rather than
  modifying a flag's behavior (backwards-incompatible), add a new flag. To
  avoid bloating the interface, mark the old flag as deprecated — but do not
  remove it until the next major version bump. Warn users about deprecated
  operations so they can update clients before being broken. Avoid time-bombs;
  think about how the program might work 5, 10, 20 years from now. If you
  cannot guarantee stability (due to external dependencies), clearly document
  the reasons.

### Naming

- **Follow naming guidelines for commands, subcommands, and options.**

  Make the name memorable and easy to type. Keep it short, but not too generic
  (to avoid conflicts). Reserve the shortest, most generic names for standard
  tools. Avoid superfluous words ("tool", "util", "kit"). Don't name commands
  after any standard, protocol, or file format ("openssl", "ffmpeg"). The more
  niche the command, the longer its name should be.

- **Follow target-runtime naming conventions.**

  For Unix-based systems: only lowercase ASCII letters, words delimited by
  single dashes. The user SHOULD NOT need to press `Shift` to type your commands
  (`VirtualBox` and `easy_install` break this rule). Numbers MAY be included
  but SHOULD NOT be the first character of a command name.

- **Don't pollute the global namespace; use subcommands.**

  If your package consists of a suite of utilities, consider implementing them
  as subcommands of a single program namespace (Git does this brilliantly:
  `git [subcmd]`). Subcommands can be generic words ("update", "status"), but
  globally-scoped program names MUST NOT be — to avoid conflicts (ImageMagick
  and Windows both used `convert` — oops!).

### Distribution

- **CLI programs MUST be easy to uninstall.**

  Where possible, distribute CLIs as either binaries or via the platform's
  native package management system. Binaries and native packages can be
  easily removed.

### Options

- **Follow the order of precedence for option mechanisms
  (highest → lowest): arguments and flags → local configuration files →
  environment variables → user-level configuration files → system-wide
  configuration files.**

  Different classes of options are suited to different mechanisms.

- **Have good defaults.**

  Most users crave convenience above all. The most commonly-used options SHOULD
  form the basis of a command's default configuration.

- **Arguments and flags MUST override all other input mechanisms.**

  Only options most likely to vary between invocations should be implemented
  as arguments/flags. Arguments (args) are positional parameters whose order
  is significant (`cp foo bar` ≠ `cp bar foo`). Flags are named parameters
  whose order should not affect behavior. In Unix-like systems, flags take two
  formats: `--<name>` (eg. `--recursive`, `--no-recursive`) and `-<x>` (single-
  letter abbreviation, eg. `-r`). Arguments and subcommands are distinct — a
  command cannot have both.

- **Prefer flags over arguments where either could work; use arguments only for
  tightly-scoped, single-purpose, frequently-run, stable operations.**

  Flags take more typing but make for a clearer self-documenting API, are more
  flexible (any order), and are more future-proof (new flags added
  backwards-compatibly). Arguments SHOULD be used only for tightly-scoped,
  single-purpose operations likely to be frequently run and unlikely ever to
  change (`cp [source] [destination]`, `rm [file1] [file2] ...`). As a general
  rule, arguments for required options and flags for optional ones — but there
  are exceptions (optional arguments, mandatory flags). Use flags for safe
  mode, dry run, and forcing destructive operations without confirmation (to
  support non-interactive environments); these options SHOULD only be inputted
  via flags, not configuration files.

- **Implement all flags using the long-form notation; short-form is optional
  shorthand.**

  All flags MUST use the long form (eg. `--help`); err on the side of clarity
  over brevity. Short-form flags MAY be implemented as shorthand aliases.
  RECOMMENDED to reserve short-form aliases for the subset most useful to human
  users (eg. `-h` for `--help`). There should not be too many — the one-letter
  namespace is finite. Flags normally behave as boolean toggles but MAY take an
  input value (`--flag value` or `--flag=value`); design flags taking a value
  so the value is optional with a sensible default (a special word like "none"
  may refer to no value at all, eg. `ssh -F none`).

- **Follow existing patterns and conventional flag names.**

  Common flags: `--all`/`-a`, `--debug`/`-d`, `--force`/`-f`, `--json`,
  `--help`/`-h`, `--no-input`, `--output`/`-o`, `--port`/`-p`, `--quiet`/`-q`,
  `--user`/`-u`, `--version`, `--verbose`. Note `-v` is varyingly used for
  "version" and "verbose" — to avoid confusion, best not to use this short
  form at all; when used, suggest what other flags the user can try.

- **SHOULD NOT read secrets from arguments or flags (eg. `--password`).**

  In Unix, secrets passed as arguments/flags leak into `ps` output and
  potentially the shell history. Best practice: accept secrets only via files
  or stdin. `--password-file` (a local file path) is better than `--password`
  — no leak into command history, and the user controls file permissions.
  (In Unix shells, `--password $(< password.txt)` has the same security
  concerns as typing the password directly.) It is also safe to prompt users
  for passwords and capture from stdin; to support non-interactive environments
  you SHOULD provide an alternative non-interactive means.

- **Configuration files can exist at three levels: local (directory-scoped),
  user-level, system-wide (global); precedence in that order, highest to
  lowest.**

  User-level config (normally in the home directory) tends to be for
  preferences/requirements of individual users (color usage, non-default paths,
  HTTP proxy). For both system-wide and user-level on Unix-like systems, it is
  RECOMMENDED to follow the
  [XDG Base Directory specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
  (limits dotfile proliferation via a general-purpose `~/.config` folder;
  supported by `yarn`, `fish`, `wireshark`, `emacs`, `neovim`, `tmux`). Local
  config files (`Makefile`, `package.json`, `docker-compose.yml`, `.env`)
  control behavior within a particular directory and are commonly committed to
  version control so configurations can be shared consistently across
  environments; they typically override env vars, user-level, and system-wide
  configs.

- **Options likely to stay consistent across invocations on the same computer
  SHOULD be configurable via centralized user-level or system-wide
  configuration files.**

- **If your program needs to modify a configuration file that does not belong to
  your program, it MUST ask for the user's consent.**

  Prefer creating a new config file (eg. `/etc/cron.d/my-app`) rather than
  appending to an existing one (eg. `/etc/crontab`).

- **Environment variables SHOULD be used to vary behavior based on the context
  in which commands are run (in Unix, the terminal session).**

  For maximum portability, env var identifiers MUST contain only uppercase
  ASCII letters with underscores delimiting words; numbers MAY be included but
  identifiers MUST start with a letter. RECOMMENDED to repurpose standard,
  general-purpose env vars where appropriate: `NO_COLOR`, `DEBUG`, `EDITOR`,
  `HTTP(S)_PROXY` / `ALL_PROXY` / `NO_PROXY`, `SHELL`, `TMPDIR`, `HOME`,
  `PAGER`, `LINES`, `COLUMNS`. For program-specific env vars, RECOMMENDED to
  prefix with a unique identifier to avoid conflicts (especially with
  [POSIX-standard env vars](https://pubs.opengroup.org/onlinepubs/009695399/basedefs/xbd_chap08.html)).
  Env vars are limited to one data type (string); aim for configurations of
  single-line string values — multi-line strings create interoperability and
  usability problems.

- **`.env` files are a convention for declaring env vars via local
  configuration files; widely supported, normally not committed to version
  control.**

  Where there are valid use cases for directory-by-directory config
  (project-specific), you SHOULD make the tool recognize `.env` files. All
  options settable in a `.env` file MUST also be settable via conventional env
  vars. When a `.env` file is loaded, its settings SHOULD override actual env
  vars with the same identifiers, but only within the scope of the `.env`
  file's directory path. MUST NOT use `.env` files as a substitute for proper
  configuration files (more versatile, more secure — eg. storable outside
  version-controlled directories).

- **MUST NOT design CLI programs to read secrets from environment variables
  (for widely distributed CLIs).**

  Env vars are prone to leakage: exported vars are sent to every process and
  can leak into logs; shell substitutions like `curl -H "Authorization: Bearer
  $BEARER_TOKEN"` leak into globally-readable process state; Docker container
  env vars can be viewed by anyone with Docker daemon access via `docker
  inspect`; env vars in systemd units are globally readable via `systemctl
  show`. Best practice: accept secrets only via files and stdin. (Exception:
  env vars are a great way of injecting secrets into applications at runtime
  when deployed to environments you control.)

### Subcommands

- **Combine closely related tools under a single command namespace.**

  Reduces overall complexity — a single program can share configuration,
  storage, flags and arguments, and help text (Git does this well). Be
  consistent: use the same arguments and flags across all subcommands; similar
  output formatting and error handling; prompt for input the same way.
  Subcommands SHOULD feel like parts of a cohesive program, not standalone
  programs under a common namespace.

- **Avoid ambiguous subcommands and subcommands with similar names.**

  Avoid both `update` and `upgrade` — quite confusing. Disambiguate with extra
  words (`update-dependencies`, `upgrade-latest`). In complex programs with
  many objects and operations, a common pattern is two levels of subcommands —
  one a noun (the object), one a verb (the operation). You can use `noun verb`
  or `verb noun`; the first seems more common (eg. `docker container create`),
  but either is fine as long as consistent.

- **Flag positioning within the subcommand structure SHOULD NOT be
  significant.**

  `my-tool --flag subcmd` and `my-tool subcmd --flag` SHOULD be equivalent
  (acknowledged this is not always possible — constrained by runtime
  environment or argument-parser capabilities).

- **Do NOT design default or "catch-all" subcommands; do NOT allow arbitrary
  abbreviations.**

  If `mycmd run echo "hello world"` lets users omit `run` (`mycmd echo "hello
  world"`), you can never add a subcommand named `echo` — or anything at all —
  without risking breaking existing usages. Require all subcommands to be
  explicitly invoked. Similarly, arbitrary prefix abbreviations (`mycmd ins`
  for `install`) lock you out of adding commands with the same starting letter.
  Aliases are fine — saving typing is good — but they should be explicit and
  remain stable.

### Interactivity

- **CLIs MUST be runnable non-interactively.**

  Never build CLI commands that _require_ the user be prompted for input. It
  MUST be possible to input all invocation-specific parameters via arguments or
  flags.

- **Prompts and interactive elements MUST be enabled only if stdin is an
  interactive terminal (a TTY).**

  If not running in an interactive terminal, prompts MUST NOT be used; the
  program MUST return errors when required input parameters are missing. (In
  Unix, check `[ -t 0 ]` for stdin TTY.) Consider designing in the `--no-input`
  flag to disable prompts — it MUST force non-interactive mode. In interactive
  mode, when a user does not pass a required argument or flag, the program
  SHOULD prompt for the missing input (in most cases a better experience than
  an error).

- **In interactive mode, always prompt for confirmation before dangerous or
  highly destructive operations.**

  A common convention is requiring `y` or `yes`. In non-interactive
  environments, confirmation SHOULD be done by passing `--force`/`-f`. Consider
  offering `--dry-run` to show consequences before committing. When prompting
  for passwords, don't print the password as the user types (turn off echo in
  the terminal in Unix-like systems).

- **Let users escape with `Ctrl+C` (the INT signal); exit promptly.**

  Return a confirmation of the exit before starting clean-up. Add a timeout to
  any clean-up operation so it doesn't hang forever. If the user types `Ctrl+C`
  again during clean-up, cancel the clean-up. Design programs to start in
  situations where clean-up of prior operations has not been completed.

### Piping

- **If either input or output is a file, the CLI SHOULD support `-` to read
  from stdin or write to stdout (piping).**

  Lets the output of another command be the input to yours, and vice versa,
  without redirecting through a temporary file (eg.
  `curl https://example.com/something.tar.gz | tar xvf -`). If your command
  expects piped input when stdin is an interactive terminal and none is
  provided: either display help text and quit immediately, or print an error
  message to stderr. Don't do nothing — don't let the operation hang like
  `cat` does.

### Exit codes

- **You MUST report exit codes correctly.**

  Return zero on success and any non-zero on failure. Error codes SHOULD be
  positive integers of 1 or greater. Reserve 1 for a general, undocumented
  error. Map other codes (2 or higher) to the various failure modes and
  document them. There SHOULD be a unique exit code for each type of failed
  operation; each failure mode MUST be documented. At minimum: 0 for success,
  1 for general failure, 2 for usage errors, 130 when interrupted by Ctrl-C
  (128 + SIGINT). The BSD `sysexits.h` conventions assign meanings to codes
  64–78 (EX_USAGE=64, EX_DATAERR=65, EX_NOINPUT=66, etc.). Scripts depend on
  exit codes — be deliberate and document thoroughly. Error messages SHOULD be
  written to stderr when a command returns non-zero.

### Output

- **Primary output goes to stdout; human-readable by default.**

  Since stdout is what is piped to the next command, it is RECOMMENDED to
  support flags toggling output to alternative machine-readable formats
  (`--plain` for piping into `grep`/`awk`, `--json` for `jq`). If the program is
  used mostly in automation, the default may be machine-readable; you can still
  auto-switch to human-readable by checking if stdout is a TTY (`[ -t 1 ]`).

- **Something SHOULD be sent to stdout on success.**

  Even a simple confirmation that the operation finished. Some commands like
  `cp` print nothing, which has come to be regarded as bad practice — the user
  SHOULD get explicit feedback on all operations, and there should be something
  to pipe into the next program. ("Expect the output of every program to become
  the input to another, as yet unknown, program." — Doug McIlroy.) Provide a
  `--quiet`/`-q` flag to suppress non-essential output for automation and to
  avoid clumsy `/dev/null` redirection.

- **Use a pager for lots of text, but carefully.**

  Pagers can cause unexpected behaviors and, implemented badly, worsen the UX.
  MUST NOT use a pager if stdin or stdout is not an interactive terminal. A
  sensible set of options for `less` is `-FIRX` (does not page if output fits
  one screen, leaves output on screen when quitting, ignores case in search,
  enables colors/formatting).

- **Use color and symbols judiciously; provide a way to disable color.**

  If _everything_ is colorful, the benefits are lost. SHOULD provide a flag to
  disable color (`--no-color` recommended). Color formatting SHOULD be disabled
  by default when: stdout is not a TTY; an env var named `NO_COLOR` exists; or
  an env var named `[APP]_NO_COLOR` exists (`[APP]` identifying your program).
  Restrained use of symbols and emoji can be beneficial (✅/❌ for
  successes/failures). Focus on good formatting over symbols and colors —
  increase information density while decreasing visual noise (`ls` is a good
  example). Don't display animations if stdout is not a TTY (stops progress
  bars becoming Christmas trees in log files).

### Errors

- **Errors SHOULD go to stderr.**

  When commands are piped, error messages get displayed to the user while
  stdout gets piped to the next command. Error messages MUST be sent to stderr
  whenever a command returns non-zero. The error message MUST provide
  sufficient information to help the user fix the problem identified by the
  exit code.

- **Follow platform error formatting conventions; keep the format predictable.**

  RECOMMENDED to follow the prevailing conventions of the platform. In Unix
  shells the classic shape is `<program-name>: <error message>`, or
  `<program-name>: <file>:<line>:<column>: <error message>` when location
  matters. Keeping the format predictable matters more than the exact
  punctuation.

- **A good error message communicates what went wrong, where, and what to do
  next.**

  `permission denied: cannot write to /etc/foo - try running with sudo or use
  --output to choose a writable path` is better than `permission denied`. Do
  not treat stderr like a log file — don't print log-level labels ("ERROR",
  "WARN") or extraneous contextual information unless explicitly invoked in
  verbose mode. Wording conventions: start with lowercase (unless starting
  with a proper name); no trailing period or exclamation marks; one sentence
  per error so messages compose cleanly when wrapped.

- **Suggest valid commands for invalid command names (popularized by Git).**

  `unknown command "buidl" — did you mean "build"?`

- **Optimize signal-to-noise ratio.**

  The more irrelevant output, the longer it takes the user to figure out what
  went wrong. If producing multiple errors of the same type, consider grouping
  them under a single explanatory header instead of many similar-looking lines.
  Put the most important information at the end of the error output, not the
  start. The eye is drawn to red text — use it intentionally and sparingly. For
  unexpected or unexplainable errors, provide debug and traceback information
  and instructions on how to submit a bug — but mind the signal-to-noise ratio
  (not all users are developers). Hide stack traces and internal details behind
  a `--verbose` or `--debug` flag; consider writing scary-looking stack traces
  to a debug log instead of the terminal.

- **Distinguish user errors from internal errors.**

  User errors (bad flags, missing files) vs. internal errors ("this shouldn't
  happen, please report at ...") — so people know whether to fix their command
  or file a bug. Exit codes play an important role.

- **Use limited color in stderr; use red for errors.**

  RECOMMENDED to use only a limited amount of color in stderr, or none at all;
  prefer indentation and plain-text formatting for structure. When using
  colors and symbols: only when stderr is an interactive terminal (TTY);
  disable in the same circumstances as stdout (not a TTY, `NO_COLOR`,
  `[APP]_NO_COLOR`); do not emit progress bars, spinners, or other animations
  to stderr if the output is being piped or logged.

- **Make bug reporting effortless.**

  Provide a URL where users can report issues, with the submission form
  pre-populated with as much information as possible. Consider linking to a
  stable error code page (eg. `https://example.com/errors/E042`) to keep the
  in-terminal message short while still being thorough.

### Documentation

- **Use POSIX notation to document CLI APIs.**

  The [POSIX specification](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html)
  defines a notation for describing the APIs (subcommands, arguments, flags)
  of command line utilities; most CLI environments adopt it for documentation.
  Use an ellipsis `...` for repetition: `<arg>...` (one or more arguments);
  `[--flag <value>]...` (option can be repeated). A convention (not POSIX) is
  `[options...]` to indicate multiple unspecified options can be passed. This
  notation MUST be used to document CLI APIs whether outputted from
  `--help`/`-h`, man pages, Markdown/AsciiDoc files, or published online.

- **User documentation MUST be built-in to all CLI apps, triggered through
  `--help`/`-h`.**

  Help text need not document every option, only the most useful and widely
  used; extended documentation SHOULD be published online. Consider also
  providing help via man pages (Unix's original documentation system), but man
  pages are an optional extra — all important documentation MUST be accessible
  via the tool directly.

- **Commands requiring arguments/flags SHOULD return abbreviated help text by
  default when none are provided.**

  `my-tool cmd` would produce an abbreviated version of `my-tool cmd --help`.
  Not possible for simple commands that do exactly one operation or programs
  that read input interactively (eg. `cat`). The abbreviated help SHOULD
  include: a description of what the program/command does; the API signature or
  one or two usage examples; descriptions of the most useful flags; and
  instructions to use `--help`/`-h` for more detail.

- **When `--help`/`-h` is passed, ignore all other flags/arguments and output
  extended help text.**

  Extended help SHOULD include: a more detailed description of what the
  program/command does; the API signature; OPTIONALLY example invocations of
  common use cases (print these early — users tend to use examples over other
  documentation; include expected output if useful); descriptions of all
  available subcommands; descriptions of all available flags (if too many, list
  the most useful and provide a link to online documentation of the rest);
  OPTIONALLY a link to a versioned online documentation page (corresponding to
  the installed version); OPTIONALLY a link to provide feedback, log issues, or
  request support. Help texts MAY be formatted (eg. bold headings) so the text
  is easier to scan, but only if done in a terminal-independent way (no user
  should see escape characters).

## References

- [TS-16 source](../../pages/016-command-line-interfaces-clis.adoc)
- [TS-15: User Interfaces](../015/AGENTS.md)
- [Command Line Interface Guidelines](https://clig.dev/)
- [POSIX utility conventions](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html)
- [XDG Base Directory specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)