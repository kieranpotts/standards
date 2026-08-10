# TS-31: Unix Shells and POSIX Standards

This is a compact version of technical standard TS-31 for AI agents.

Use this when authoring or modifying shell scripts that must be POSIX-compliant
and run across multiple shells (sh, bash, zsh, dash, etc.) and platforms (Linux,
macOS, WSL2, and Git Bash for Windows).

Do NOT use this skill for Bash-specific scripts, Python scripts, or shell
configuration files (`.bashrc`, `.zshrc`). For scripts that target Bash
specifically, these POSIX standards apply but are extended by
[Bash standards](../032/AGENTS.md)

Use project-specific shell skills if available.

## Rules

- **Use POSIX-compliant syntax.**

  Use `#!/usr/bin/env sh` (not `#!/bin/sh` or `#!/bin/bash`). This form looks up
  `sh` via `PATH`, making it more portable across environments.

  No Bashisms (`[[`, `=~`, `${var^}`, etc.). Scripts must work in `sh`, `bash`,
  `zsh`, and `dash`.

  Do not use the `function` keyword in function declarations – it is not POSIX:

  ```sh
  # ❌
  function my_func() { : ; }

  # ✅
  my_func() { : ; }
  ```

- **Trap errors.**

  Use `set -eu` at the top of most scripts. `-e` exits immediately when any
  command returns a non-zero status. `-u` treats references to undefined
  variables as errors. Both SHOULD be set before any other logic.

  `set -x` MAY be added temporarily for debugging but MUST NOT be committed.

  `set -o pipefail` is not POSIX – do not use it.

  ```sh
  #!/bin/sh

  set -eu

  # Start of script...
  ```

- **Follow this source order.**

  Structure script files in this order:

  1. Shebang and `set` operations
  2. File-level comment block
  3. Variables
  4. Functions
  5. Main program (`main "$@"`)

  Keep all function definitions together. Do not interleave executable code
  between function definitions.

- **Wrap non-trivial scripts in `main()`.**

  For any script longer than a few lines, define a `main()` function as the
  entry point and call it at the end of the script:

  ```sh
  main() {
    # Script logic here.
  }

  main "$@"
  ```

  This keeps executable code out of the global scope and away from function
  definitions.

- **Return explicit exit codes.**

  Use `return <number>` in functions and `exit <number>` in scripts. 0 =
  success, non-zero = failure. Avoid implicit status from the last command.

- **Prefer built-ins over external commands.**

  Shell built-ins run in the shell's own process. External commands spawn a new
  process.

  Prefer built-in parameter expansion over `sed`, `awk`, etc., for simple text
  manipulation. It is faster and has no external dependency.

  When external commands are unavoidable, prefer POSIX-standard utilities:
  `grep`, `sed`, `awk`, `find`, `xargs`, `cut`, `sort`, `uniq`, `tr`, etc. For
  anything else, eg. non-POSIX utilities for JSON parsing and HTTP requests,
  document the dependency explicitly.

- **Use lowercase_snake_case for variable and function names.**

  Do not use `UPPER_SNAKE_CASE` for script variables – it risks collision with
  shell and environment variables. Use only for variables that are explicitly
  exported to the environment:

  ```sh
  # ❌ No:
  readonly OUTPUT_DIR="/tmp/out"

  # ✅ Yes:
  readonly output_dir="/tmp/out"

  # ✅ Yes:
  export MY_APP_LOG_LEVEL="info"
  ```

- **Err on the side of clarity over brevity.**

  Prefer descriptive names over terse abbreviations: `input_file` over `f`,
  `exit_code` over `rc`.

- **Declare variables `readonly` by default.**

  Variables SHOULD be `readonly` unless the logic requires reassignment. Apply
  `readonly` immediately after assignment:

  ```sh
  # ❌ No:
  readonly config_file="/etc/app/config"

  # ✅ Yes:
  result="$(some_command)"
  readonly result
  ```

- **Quote all variables.**

  Always write `"${var}"`. This is easier to read than `"$var"`, and more
  reliable than `$var`.

  Quoting prevents word-splitting and glob expansion.

  Exception: intentional word-splitting must have a comment explaining why.

- **Use bracketed variable syntax.**

  Prefer `${var}` over `$var`. The brackets clearly delimit the variable name,
  prevent ambiguity in concatenation, and enable extended parameter expansion
  forms (`${#var}`, `${var:0:1}`, `${var:-default}`, etc.):

  ```sh
  var="foo"

  # Looks for a variable named 'varbar' (likely undefined).
  echo "$varbar"

  # Correctly expands to 'foobar'.
  echo "${var}bar"
  ```

  Brackets MAY be omitted from positional parameters (`$1`, `$@`, etc.) and
  other special variables.

- **Use `$()` for command substitution.**

  Prefer `$(command)` over backtick syntax. Backticks require escaping when
  nested; `$()` nests cleanly:

  ```sh
  # ❌ No:
  result=`outer \`inner\``

  # ✅ Yes:
  result="$(outer "$(inner)")"
  ```

- **Use `"$@"` to forward all arguments.**

  When passing all arguments to another function or command (eg. from a script
  to `main()`), use `"$@"` (quoted). The alternatives lose arguments that
  contain spaces or are empty strings:

  - `"$@"` — each argument preserved as-is (correct)
  - `$@` and `$*` (unquoted) — split on spaces, dropping empty-string arguments
  - `"$*"` — all arguments collapsed into one string

- **Separate data output from messaging.**

  Reserve plain `echo` / `printf` for script _output_ (the data the caller
  expects).

  Send status, errors, and debug info to stderr.

  ```sh
  # Data output:
  echo "result: $value"

  # Status/error messages:
  printf "Processing file: %s\n" "$file" >&2
  ```

  If using a project-specific output library, follow its conventions.

- **Use `printf` over `echo -e`.**

  The `-e` flag for `echo` is not POSIX. Its handling of backslash escape
  sequences is implementation-defined and so varies between shells.

  Use `printf` for any output that requires escape interpretation:

  ```sh
  # ❌ No:
  echo -e "Done.\nSee log for details."

  # ✅ Yes:
  printf "Done.\nSee log for details.\n"
  ```

  Plain `echo` (without `-e`) is fine for simple string output with no escape
  sequences.

- **Use `; then` and `; do` on the same line as the opening keyword.**

  `else`, `fi`, and `done` go on their own lines, vertically aligned with the
  opening statement:

  ```sh
  # ✅
  if [ "${count}" -eq 100 ]; then
    echo "Count is 100"
  else
    echo "Count is not 100"
  fi

  # ❌
  if [ "${count}" -eq 100 ]
  then
    echo "Count is 100"
  fi
  ```

  Flatten nested conditionals where possible using `&&` and `||`:

  ```sh
  # Instead of:
  if sudo apt-get update; then
    sudo apt-get install pyrenamer
  fi

  # Prefer:
  sudo apt-get update && sudo apt-get install pyrenamer
  ```

  For `case` statements, put the pattern and closing `;;` each on their own
  lines. Simple single-command cases MAY be written on one line:

  ```sh
  # Multi-command case:
  case expression in
    case1)
      operation1
    ;;
    case2)
      operation2
      operation3
    ;;
  esac

  # Simple single-command case (one-liner form):
  case "${flag}" in
    a) aflag='true' ;;
    b) bflag='true' ;;
    *) error "Unexpected option ${flag}" ;;
  esac
  ```

  Do not precede patterns with an open parenthesis. Avoid `;&` and `;;&`
  notations.

- **Choose argument-handling pattern by scope.**

  _No-argument scripts_ validate and reject any input:

  ```sh
  if [ $# -gt 0 ]; then
    printf "Error: script does not accept arguments\n" >&2
    return 1
  fi
  ```

  _Single-option scripts_ use a simple case:

  ```sh
  case "${1:-}" in
    --help)  show_help; return 0 ;;
    -*)      printf "Error: unknown option '%s'\n" "$1" >&2; return 1 ;;
    *)       : ;;
  esac
  ```

  _Multi-option scripts_ use a loop:

  ```sh
  while [ $# -gt 0 ]; do
    case "$1" in
      --name)  name="$2"; shift 2 ;;
      --file)  file="$2"; shift 2 ;;
      -*)      printf "Error: unknown option '%s'\n" "$1" >&2; return 1 ;;
      *)       break ;;
    esac
  done
  ```

- **Add defensive checks before destructive operations.**

  Verify assumptions before modifying files, deleting paths, or overwriting
  data. Handle edge cases - empty strings, missing files, unset variables, or
  multiple spaces in data:

  ```sh
  # Verify a required external tool is available.
  if ! command -v jq >/dev/null 2>&1; then
    printf "Error: 'jq' is required but not installed\n" >&2
    exit 1
  fi

  # Verify a file exists before operating on it.
  if [ ! -f "${target_file}" ]; then
    printf "Error: file not found: %s\n" "${target_file}" >&2
    exit 1
  fi

  # Dry-run a command before committing to it.
  if ! some_command >/dev/null 2>&1; then
    printf "Error: precondition check failed\n" >&2
    exit 1
  fi
  ```

- **Follow code style conventions.**

  - **Indentation**: two spaces. Never use tabs, except in the body of `<<-`
    here-documents.

  - **Line length**: keep most lines under 80 characters. Use continuation lines
    (`\`) to wrap long commands; indent them by four spaces (double indent).
    Break before operators, not after.

  - **Blank lines**: insert between discrete blocks of code to improve
    readability.

  ```sh
  # Continuation lines, broken before the operator:
  command1 \
      && command2 \
      && command3
  ```

- **Set executable permissions correctly.**

  Scripts intended to be executed directly MUST be executable (`chmod +x`).
  Library scripts intended only to be sourced SHOULD NOT be executable
  (`chmod -x`).

  SUID and SGID MUST NOT be applied to any shell scripts. Remove them explicitly
  if present:

  ```sh
  chmod u-s filename   # Remove SUID.
  chmod g-s filename   # Remove SGID.
  ```

- **Delimit sections with banner comments.**

  Longer scripts SHOULD be divided into clearly delimited sections. Use a
  consistent two-level hierarchy of banner-style delimiters so the structure
  is visible at a glance:

  - **Major sections** — a banner of equals signs:

    ```sh
    # ==============================================================================
    # Section Title
    # ==============================================================================
    ```

  - **Subsections** — a banner of hyphens:

    ```sh
    # ------------------------------------------------------------------------------
    # Subsection Title
    # ------------------------------------------------------------------------------
    ```

  Banners SHOULD be 80 characters wide (`#` plus 78 delimiter characters).
  A banner SHOULD be followed by ordinary comment lines summarizing the
  section's purpose. Ordinary single-line explanations use a plain `#` with
  no banner. A script that needs more than two levels of banners is probably
  too long and SHOULD be split into separate files.

- **Document all functions with a structured comment block.**

  All functions SHOULD have a comment block immediately above the declaration
  covering: description, globals used, arguments, stdout/stderr output, and
  return values (non-zero exit codes).

  ```sh
  # function_name - <Short description.>
  #
  # <Optional longer description.>
  #
  # Globals:
  #   $<VAR> - <Description.>
  #
  # Arguments:
  #   $1 - <Description.>
  #
  # Output:
  #   stdout - <Description.>
  #   stderr - <Description.>
  #
  # Returns:
  #   1 - <Description of error condition.>
  #
  function_name() {
    # ...
  }
  ```

  The description MUST note any surprising side effects: changes to the working
  directory, filesystem modifications, or calls to `exit`.

- **Do not use `eval` or aliases.**

  `eval` executes arbitrary strings as shell code, making it impossible to
  reason about what variables were set or whether commands succeeded. Use
  explicit commands instead.

  Aliases are unreliable in scripts. They are not always expanded and behave
  differently between interactive and non-interactive shells. Define functions
  instead.

- **Beware `rm` with wildcard expansion.**

  Filenames beginning with `-` can be misinterpreted as flags when a glob
  expands. Always use `--` or a `./` prefix with `rm *`:

  ```sh
  # ❌ If a file named `-r` exists, this deletes recursively.
  rm -v *

  # ✅
  rm -v -- *

  # ✅
  rm -v ./*
  ```

- **Validate with ShellCheck.**

  Run this before committing:

  ```sh
  shellcheck --severity=style <script.sh>
  ```

  Address all warnings before committing changes.

  Use ShellCheck's "source" directive to point it to the real path of sourced
  files (relative to the current file):

  ```sh
  # shellcheck source=./lib/helpers.sh
  . "$(dirname "$0")/lib/helpers.sh"
  ```

  Use ShellCheck's "disable" directive (`# shellcheck disable=SC2086`) sparingly
  and only with clear justification (which MUST be explained in an adjacent
  comment).

## Examples

Basic script with argument parsing:

```sh
#!/bin/sh

set -eu

main() {
  action="${1:-}"

  case "$action" in
    start)   start_service; return 0 ;;
    stop)    stop_service; return 0 ;;
    status)  check_status; return 0 ;;
    *)       printf "Error: unknown action '%s'\n" "$action" >&2; return 1 ;;
  esac
}

start_service() {
  if [ -f "$service_pid" ]; then
    printf "Error: service already running\n" >&2
    return 1
  fi
  printf "Starting service...\n" >&2
}

stop_service() {
  printf "Stopping service...\n" >&2
}

check_status() {
  echo "Service is running"
}

main "$@"
```

Defensive checks before file operations:

```sh
#!/bin/sh

set -eu

backup_file() {
  src="$1"
  dst="$2"

  if [ ! -f "$src" ]; then
    printf "Error: source file not found: %s\n" "$src" >&2
    return 1
  fi

  if [ -f "$dst" ]; then
    printf "Error: destination already exists: %s\n" "$dst" >&2
    return 1
  fi

  cp "$src" "$dst" || {
    printf "Error: copy failed\n" >&2
    return 1
  }
}

backup_file "$@"
```
