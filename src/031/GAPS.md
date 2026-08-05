# TS-31 gap analysis

Gaps found comparing TS-31: Unix Shells and POSIX Standards against the following
reference resources:

- `src/031/__TODO__/shell/unix/input.md` (and its parent navigation files
  `src/031/__TODO__/shell/README.md`, `src/031/__TODO__/shell/unix/README.md`)
- `src/031/__TODO__/shell1/...` — a byte-for-byte duplicate of the `shell/`
  tree (identical content; not cited separately below).

**Assessment.** The reference material is narrow: it covers a single topic —
accepting interactive user input via the `read` built-in. TS-31 names `read` as
an example shell built-in (`12-miscellaneous-shell-built-ins.adoc:4`) but never
documents it, and has no coverage of interactive input anywhere. Every
substantive point in the reference is therefore a **missing** gap. Note that the
reference recommends the `-p` (prompt) and `-s` (silent) options to `read`, both
of which are Bashisms and not POSIX; TS-31 is explicitly a POSIX standard, so a
POSIX-compliant equivalent (`printf` prompt + `read`; `stty -echo` for hidden
input) would need to be documented rather than the reference's specific
mechanisms. Interactive prompting sits at the edge of TS-31's stated
"system administration, batch processing, and low-level automation" scope but is
plausibly in scope for sysadmin scripts that confirm destructive operations or
prompt for credentials.

**Status:** Initial run. All gaps open. Last run: 2026-08-05.

## Missing

- [ ] `src/031/__TODO__/shell/unix/input.md:3-5` — the `read` built-in for
      capturing interactive user input into a variable is not addressed anywhere
      in the standard. `read` is named as an example built-in at
      `12-miscellaneous-shell-built-ins.adoc:4` but never documented. Recommend
      placing at a new `== read` section in
      `12-miscellaneous-shell-built-ins.adoc` (after the existing `== eval`
      section, ending at line 37).

- [ ] `src/031/__TODO__/shell/unix/input.md:7-9` — the basic `read my_var` form
      (no prompt; prints a blank line and waits for input) is not addressed.
      Recommend placing at the new `== read` section in
      `12-miscellaneous-shell-built-ins.adoc`.

- [ ] `src/031/__TODO__/shell/unix/input.md:11-19` — prompting the user with an
      inline message before reading input is not addressed. The reference
      recommends `read -p`, which is a Bashism and not POSIX; TS-31 would need to
      document the POSIX-compliant equivalent (`printf` prompt to stderr + bare
      `read`). Recommend placing at the new `== read` section in
      `12-miscellaneous-shell-built-ins.adoc`.

- [ ] `src/031/__TODO__/shell/unix/input.md:21-29` — the alternative pattern of
      pre-printing the prompt with `echo`/`printf` on its own line, then
      `read` (useful for multi-line instructions) is not addressed. This is in
      fact the POSIX-compliant prompting approach. Recommend placing at the new
      `== read` section in `12-miscellaneous-shell-built-ins.adoc`.

- [ ] `src/031/__TODO__/shell/unix/input.md:31-37` — UX guidance on prompt
      placement (inline prompt vs. separate-line prompt; inline RECOMMENDED) is
      not addressed. Recommend placing at the new `== read` section in
      `12-miscellaneous-shell-built-ins.adoc`.

- [ ] `src/031/__TODO__/shell/unix/input.md:39-43` — hidden/silent input for
      passwords is not addressed. The reference uses `read -s`, which is a
      Bashism and not POSIX; TS-31 would need to document the POSIX-compliant
      approach (`stty -echo` before `read` and `stty echo` after). Recommend
      placing at the new `== read` section in
      `12-miscellaneous-shell-built-ins.adoc`.

## Partial

- (none — TS-31 does not cover `read` beyond naming it, so no point of
  comparison rises to "partial".)

## Out-of-scope

- (none — interactive input prompting is plausibly in scope for TS-31's
  system-administration audience, even though it is less central to the
  "batch processing / automation" framing. Flagged in the assessment for the
  user to confirm.)

## Unresolved

- (none — all reference files were read successfully. The `shell/` and `shell1/`
  trees are identical duplicates; only `shell/` is cited above.)