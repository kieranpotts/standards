---
name: unwrap-prose
description: >-
  Remove soft line wraps from the prose of one technical standard in this
  repository, so each paragraph, list item, and table cell sits on a single
  source line as TS-28 requires. Use when the user says "unwrap TS-<N>",
  "remove the soft wraps from TS-<N>", "convert TS-<N> to one line per
  paragraph", or asks for the next standard to be unwrapped. Do not use it to
  reword, restructure, or otherwise edit a standard's content.
compatibility: requires Read, Edit, Bash (git, python3, node)
license: CC0-1.0
---

# Unwrap prose

> [!NOTE]
> This is a temporary skill. It exists to migrate the standards, one at a
> time, from soft-wrapped prose to one line per paragraph, following the
> change to TS-28 § Line length and wrapping. Delete it once every standard
> has been converted.

Rewrite one standard's AsciiDoc source so that no paragraph, list item,
admonition, description-list entry, or table cell is soft wrapped across
several source lines. The conversion is mechanical, and a script does it. The
agent's job is to run the script, then deal with the handful of lines the
script deliberately leaves for a human to judge.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **The target standard — REQUIRED.** One technical standard, identified as
  `TS-<N>`. Its number zero-padded to three digits identifies its files, so
  TS-1 is the page `src/modules/ROOT/pages/001.adoc` plus every `.adoc` file
  under `src/modules/ROOT/partials/001/`. Convert one standard per run, never
  several, so each diff stays reviewable on its own.

  If the user asks for "the next one", pick the lowest-numbered standard for
  which `unwrap.py <N> --check` still reports joins.

## Success criteria

- `unwrap.py <N> --check` MUST report `would join 0 lines`.

- No line in the diff MUST differ from the original other than by
  whitespace — the script refuses to write a file that fails this — and any
  file the script rejected for a rendering difference MUST have been either
  forced, with the reason stated, or left alone and reported.

- Every note the script printed MUST have been judged, and each fix, or the
  reason for leaving a line as it is, MUST be in the report back to the user.

- AsciiDoc markup examples inside verbatim blocks in the target standard MUST
  have been unwrapped by hand (see step 4).

- Only the target standard's page and partials MUST have been modified.
  Nothing MUST be staged or committed.

## Steps

1. **Check the starting state.** Run `git status --short` on the target
   standard's page and partials directory. If there are uncommitted changes
   there, stop and ask the user whether to proceed; mixing them into this
   diff makes it unreviewable.

2. **Run the script.**

   ```sh
   python3 .agents/skills/unwrap-prose/scripts/unwrap.py TS-<N>
   ```

   The script needs Node.js and the `@asciidoctor/core` package. By default it
   uses the website repository's copy, at
   `../../website/default/node_modules/@asciidoctor/core` relative to this
   repository. If that is missing, ask the user to run `npm install` in the
   website repository, or pass `--core <path>`. Do not skip the render check.

   For each file, the script joins every soft-wrapped line onto the one
   before it, then checks two invariants before writing the file:

   - The text is identical apart from whitespace. A failure here is a bug in
     the script. It aborts without writing anything. Report it to the user;
     do not work around it.

   - Asciidoctor.js renders the file to the same HTML, apart from whitespace
     outside `<pre>` elements. A file that fails is reported as `REJECTED`
     with an HTML diff, and is not written.

3. **Judge rejected files.** A rendering difference is usually one of two
   things:

   - **A fix.** A wrap had split an inline construct — a bold span, a link
     macro, an `xref:` — so it did not render, and now it does. This is the
     point of the exercise. Rerun with
     `--force <path-to-the-file>` to accept it, and tell the user which
     construct now renders.

   - **A regression.** The join changed the meaning of the markup (a block
     that was a separate paragraph is now part of the one before, for
     instance). Leave the file unwritten, fix the lines by hand if the fix is
     obvious, and rerun the script. Otherwise report the file.

4. **Judge the notes.** The script never joins a line that could be the start
   of a new block, even when it's probably a wrapped continuation. It reports
   these as `not joined; looks structural mid-paragraph`. Typical cases:

   - A wrap that happens to start with `- `, `... `, `2024. `, or `.`, which
     look like list markers or block titles. If the line is plainly a
     continuation of the sentence before, join it by hand with the Edit tool.

   - A genuine list, block title, or admonition that follows a paragraph
     without a blank line. Leave it on its own line.

   Lines not joined across a `//` line comment should stay as they are,
   unless the comment is obviously stale — in which case, flag it for the
   user rather than removing it.

5. **Unwrap AsciiDoc examples.** The script never touches verbatim blocks,
   because their line structure usually matters. But a listing that
   demonstrates AsciiDoc markup should itself follow the one-line rule, so it
   doesn't teach the old style. Find them with:

   ```sh
   grep -nE -A1 '^\[source, ?(asciidoc|adoc)' src/modules/ROOT/partials/<NNN> -r
   ```

   Also skim any unlabeled ```` ``` ```` or `----` blocks whose content is
   AsciiDoc. Join wrapped prose lines in these examples by hand. Leave code,
   config, and command-line examples alone.

6. **Verify.**

   ```sh
   python3 .agents/skills/unwrap-prose/scripts/unwrap.py TS-<N> --check
   git diff --stat -- src/modules/ROOT/pages/<NNN>.adoc src/modules/ROOT/partials/<NNN>/
   git diff --word-diff=porcelain -- src/modules/ROOT/pages/<NNN>.adoc src/modules/ROOT/partials/<NNN>/ | grep -E '^[-+][^-+]' | head
   ```

   The first MUST report `would join 0 lines`. The last prints words that
   were added or removed; it should print nothing except for any hand edits
   from steps 3 to 5, which you should be able to account for.

7. **Report back.** Tell the user the number of lines joined and files
   changed, each forced file and why, each note and how it was resolved, and
   any examples unwrapped by hand. Suggest a commit message in the style of
   the TS-33 conversion, eg. `style: ts-<n> revert to non-soft wrapped text`,
   but do not commit.
