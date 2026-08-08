---
name: gap-analysis
description: >-
  Check one technical standard in this repository for coverage gaps against
  external reference resources — a URL, a file, or a directory — and record
  them in a GAPS.md beside the standard. Use when the user says "do a gap
  analysis between TS-<N> and <url>", "analyze TS-<N> for gaps with <file>", or
  "gap-check TS-<N> against the vendor docs in <path>". Do not use it to close
  the gaps it finds.
compatibility: >-
  requires Read, Write, Edit, Glob, Grep, WebFetch, Agent, Bash (gh, python3)
license: CC0-1.0
---

# Gap analysis

Check a single technical standard for coverage gaps against one or more
external reference resources, and write what you find to a `GAPS.md` in the
standard's directory. You are looking for what the reference material covers
and the standard does not — never the reverse — and you stop at the report.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **The target standard — REQUIRED.** One technical standard, identified as
  `TS-<N>`, not several. Its directory is that number zero-padded to three
  digits, so TS-1 is `src/001/`. If the user does not name one, and the
  context or the working directory already establishes a `src/<NNN>/`
  standard, treat that as the target.

- **The reference resources — REQUIRED.** A web URL, a local file, or a local
  directory. For a directory, recurse through every Markdown, AsciiDoc, and
  other plain-text file within it and its subdirectories, and treat each as
  its own resource. Read directories with a shell command such as `cat`
  rather than your file tools, in case they are Git-ignored and therefore
  invisible to those tools. Follow the `URL=` path of any `.URL` file.

## Success criteria

- `src/<NNN>/GAPS.md` MUST exist, MUST follow the bundled template, and MUST
  list every gap as a flat checklist bullet — no sub-headings, tables, or
  per-gap subsections.

- Every gap MUST cite both a concrete source location in the reference
  material — a URL with a section anchor where possible, or
  `<file>:<line>` — and a concrete destination in the standard, either an
  existing `<file>:<line>` or "new section". A gap that cannot be tied to
  both is not actionable.

- Every gap MUST be classified as missing, partial, or out-of-scope.

- Where a `GAPS.md` already existed, every prior finding MUST still be
  present: a gap that is still open keeps its original citation, and a gap now
  covered by the standard is checked off rather than deleted.

- Every reference resource that could not be retrieved or read MUST be named
  in the report and in the Unresolved section, with the actual error.

- The standard's `.adoc` files and its `AGENTS.md` MUST be unchanged, no file
  other than `GAPS.md` MUST have been written, and nothing MUST be staged or
  committed. This skill finds gaps; it does not close them.

## Instructions

1.  Resolve the target directory from the standards index at
    `src/README.adoc`, then check for `src/<NNN>/GAPS.md`. If it exists, this
    is a re-run against the same or an updated set of resources. Read it
    first, carry every unchecked gap forward for re-verification, and re-check
    every checked gap to confirm the standard still covers it.

2.  Read the standard in full: `src/<NNN>/README.adoc`, every file it pulls in
    via `include::`, and any subdirectory carrying its own `README.adoc`. Read
    its `AGENTS.md` too, if it has one — that file reveals which rules the
    maintainers consider load-bearing.

3.  Ingest every reference resource in full, noting its own scope and audience
    as you read. A broad external resource, such as a general industry style
    guide, will cover far more ground than a narrow standard.

    - A web URL: fetch it. If the fetch fails, or the page is paywalled or
      blocked, record the failure against that resource and continue with the
      rest.
    - A local file: read it in full.
    - A local directory: recurse through its Markdown, AsciiDoc, and
      plain-text files. Skip binary files silently.

    Two kinds of URL need handling before they can be ingested at all — a
    `kieranpotts/*` GitHub issue, which is an index of resources rather than a
    resource, and a YouTube video, whose content cannot be fetched. See the
    references below.

4.  Where the material is large — a directory of more than about 15 files, or
    several sizeable URLs — do not read it all into your own context. Fan the
    extraction out: spawn one sub-agent per resource, or per batch of ten to
    fifteen files, each tasked narrowly with reading its assigned material and
    returning a flat list of atomic claims, rules, or topics, every one
    carrying a precise citation.

5.  Compare coverage point by point. Break each resource down into its atomic
    claims, rules, or topics, and classify each against the standard:

    - Missing. The standard does not address it at all, and it falls within
      the standard's own stated scope.
    - Partial. The standard touches on it, but more shallowly than the
      reference — the reference gives a worked exception the standard omits,
      say.
    - Out-of-scope. The reference covers it, but it plausibly sits outside
      this standard's stated purpose or audience. Note these rather than
      dropping them silently; the user may disagree with your scope call.

    Only missing and partial items are gaps. Do not manufacture one from a
    point the reference makes in passing, and do not restate something the
    standard already covers in different words.

6.  Write or update `GAPS.md` from the bundled template, giving every gap a
    checkbox, its source citation, its destination in the standard, and its
    classification.

7.  Report the gap count by category, plus anything you could not verify — a
    fetch failure, an ambiguous scope call. Stop there.

## Rules

- You MUST NOT edit the target standard's `.adoc` files, its `AGENTS.md`, or
  any file other than `GAPS.md`, and MUST NOT stage or commit that file.

- You MUST NOT fabricate reference content. Where a URL cannot be fetched or a
  file cannot be read, report exactly that. Do not infer the content, and do
  not recall it from memory.

- Your analysis MUST stay focused on what is missing from the standard. You
  SHOULD NOT report material in the reference that the standard already
  covers, unless you have a specific reason to.

- Sub-agents MUST only extract content from reference material, and MUST NOT
  classify gaps. A sub-agent MUST return citation-tagged claims and never a
  missing, partial, or out-of-scope verdict, because the classification
  depends on the whole standard, which only you have read.

## Edge cases

- The standard is a stub, holding only a heading and a placeholder.

  Its scope for comparison is effectively unbounded, so almost anything in the
  reference material could be called a gap. Report this and ask the user
  whether to proceed.

- Some resources were retrieved and others were not.

  Proceed with what you have and list the failures separately in the report,
  rather than abandoning the whole analysis.

- The reference material is far broader than the standard.

  Where a comprehensive general reference meets a narrow standard, most of the
  reference will be out-of-scope. Say so plainly, rather than forcing out a
  long "missing" list.

- The reference material is far narrower than the standard.

  Most of the standard will then have nothing to compare against. That is not
  itself a finding, and should not be reported as one.

## Assets

- [GAPS.md template](./assets/gap-analysis/GAPS.md) \
  The structure to follow when writing or updating the report in step 6.

## References

- [Expanding a GitHub issue](./references/gap-analysis-github-issues.md) \
  Read before ingesting any reference resource under
  `https://github.com/kieranpotts/*/issues/`. Such a URL is an index of
  resources, not a resource; this explains how to expand it into the real
  ones.

- [Extracting a YouTube resource](./references/gap-analysis-youtube.md) \
  Read before ingesting any `youtube.com/watch` or `youtu.be` URL. The video
  cannot be fetched, and this explains how to get the creator's own summary
  instead, using the bundled script at
  `scripts/gap-analysis/youtube_description.py`.
