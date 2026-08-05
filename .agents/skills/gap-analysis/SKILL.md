---
name: gap-analysis
description: >-
  Check a technical standard in this repository for coverage gaps against one
  or more external reference resources (a URL, a file, or a directory). Use
  when asked to "do a gap analysis between TS-<N> and <url>", "analyze TS-<N>
  for gaps with <file>", or "gap-check TS-<N> against the directory of vendor
  docs in <path>."
compatibility: requires Read, Write, Edit, WebFetch, Bash (grep/find), Agent
license: CC0-1.0
---

# Gap analysis

Check a single technical standard for coverage gaps against one or more
external reference resources, producing a `GAPS.md` in the standard's
directory. You are looking for stuff the reference material covers that
the standard does not, never the reverse.

## Parameters

- **The target technical standard — REQUIRED.** A single standard, eg. TS-10,
  not multiple. If not explicitly defined by the user's prompt, try to determine
  the target from the context and environment. If the immediate context
  includes the `README.adoc` for a specific standard, or if the current working
  directory is one of the `src/<NNN>/` paths, assume that is the target.

- **Reference resources — REQUIRED.** A web URL, a local file, or a local
  directory. If a directory, recurse through every Markdown, AsciiDoc, and
  other plain-text files within it and its sub-directories. It is RECOMMENDED
  to use a shell command like `cat` to traverse directories, in case they are
  Git-ignored (which will prevent them being accessible to you via your file
  tools). Treat each found text file as a reference resource. Treat `.URL` files
  as web resources — follow their `URL=` path.

  A reference resource that is a URL to a GitHub issue under
  `https://github.com/kieranpotts/*` is never itself the resource — treat it
  as an index. Expand it into the actual reference resources listed in its
  description, comments, and sub-issues, using the `gh` commands in step 3a,
  before ingesting anything.

Prompt the user for clarification if either is ambiguous.

## Success criteria

- A `GAPS.md` MUST exist in the target standard's directory, listing every
  identified gap as a flat checklist item.

- `GAPS.md` MUST be saved to disk, but MUST NOT be staged or committed to
  version control.

- Every gap MUST cite both its reference-material source and its intended
  location in the standard.

- Every gap MUST be classified as missing, partial, or out-of-scope.

- The target standard's own files (`.adoc`, `AGENTS.md`) MUST NOT have been
  modified by you.

## Instructions

1.  Resolve the target and check for an existing analysis. Look up the standard
    in `src/README.adoc`. The directory is zero-padded to three digits, eg.
    TS-1 is `src/001/`.

    Run `ls src/<NNN>/GAPS.md`. If it exists, this is a re-run against the
    same (or an updated) set of reference resources. Read it first. Carry
    forward every unchecked gap for re-verification, and re-check any
    checked gap to confirm the standard still covers it.

2.  Read `src/<NNN>/README.adoc` and every file it pulls in via `include::`,
    including any subdirectories with their own `README.adoc`. Also read the
    standard's `AGENTS.md`, if one exists — it can reveal what the maintainers
    consider the load-bearing rules from the standard.

3.  Ingest every reference resource in full.

    - If a web URL, fetch it. If it fails or is paywalled/blocked, report the
      failure against that resource and continue with the rest.

    - If a local file, read it in full.

    - If a local directory, recurse through every Markdown, AsciiDoc, and
      plain-text file within it. Skip binary files silently.

    Note the resource's own scope and audience as you read it. A broad
    external resource (eg. a general industry style guide) will likely cover
    more ground than the technical standard.

    Where a resource is large — a directory with more than about 15 files,
    or several sizeable URLs — do not read it all directly into your own
    context. Instead, fan the extraction out. Spawn one sub-agent per
    resource (or per batch of ~10-15 files, for a large directory), each
    with a narrow task. Read the assigned material and return a flat list
    of atomic claims, rules, or topics, each with a precise citation
    (URL#section, or `<file>:<line>`).

3a. Before ingesting a reference resource matching
    `https://github.com/kieranpotts/<repo>/issues/<number>`, run these `gh`
    commands to pull the candidate resources out of it, then treat each
    discovered URL (or attached file) as its own reference resource.

    - Issue title and body:

      ```sh
      gh issue view <url> --json title,body
      ```

    - Comments, in full:

      ```sh
      gh issue view <url> --json comments --jq '.comments[].body'
      ```

    - Sub-issues (title, state, URL):

      ```sh
      gh api repos/kieranpotts/<repo>/issues/<number>/sub_issues \
        --jq '.[] | "\(.number)\t\(.state)\t\(.title)\t\(.html_url)"'
      ```

      If the `sub_issues` endpoint 404s (older `gh`/API version), fall back
      to GraphQL:

      ```sh
      gh api graphql -f query='
        query($owner:String!, $repo:String!, $number:Int!) {
          repository(owner:$owner, name:$repo) {
            issue(number:$number) {
              subIssues(first: 100) {
                nodes { number title url state }
              }
            }
          }
        }' -f owner=kieranpotts -f repo=<repo> -F number=<number>
      ```

    - Extract every URL mentioned across the title, body, and comments in one
      pass (dedupe, then drop the issue's own URL and any sub-issue URLs
      already captured above — those are handled separately, not as
      resources in their own right):

      ```sh
      gh issue view <url> --json body,comments \
        --jq '[.body, (.comments[].body)] | join("\n")' \
        | grep -oE 'https?://[^ )>"'"'"']+' | sort -u
      ```

    If a sub-issue is itself under `kieranpotts/*`, apply this same expansion
    to it rather than treating the sub-issue as a resource. Ingest each
    _discovered_ URL/file per the normal rules in step 3 above. If the
    issue (and its sub-issues) yield no discoverable resources at all, report
    that and ask the user for clarification rather than guessing.

3b. Before ingesting a reference resource that is a YouTube URL
    (`https://www.youtube.com/watch?v=<id>` or `https://youtu.be/<id>`),
    note that the video itself cannot be fetched — YouTube watch pages are
    JavaScript-rendered, and a plain web fetch returns only page chrome with
    no video content or transcript. Do not report the URL as a simple fetch
    failure; the creator's own summary of the video's argument is available
    without any API key.

    Run the helper script to extract the video's title, author, length,
    keywords, and full description:

    ```sh
    python3 .agents/skills/gap-analysis/scripts/youtube_description.py <video-id-or-url>
    ```

    The argument may be a bare 11-character video id, a watch URL, or a
    `youtu.be` short URL. The script reads YouTube's public oEmbed endpoint
    (title, author) and the `ytInitialPlayerResponse` blob embedded in the raw
    watch-page HTML (full description, keywords, length) and prints them as
    plain text. It uses only the Python 3 standard library.

    Treat the returned description as the creator's own summary of the
    video's thesis and key claims, and compare the standard against that. Be
    transparent that the comparison is against the description, not a full
    transcript: note this in the `GAPS.md` Unresolved section (or alongside
    any gap it produces), since claims present only in the spoken audio could
    not be verified.

    If the description links to a full transcript on another page (some
    creators host one), fetch that transcript per the normal rules in step 3
    and use it as the primary source, with the description as a fallback.

    If the script fails (eg. the video is private, age-restricted, or
    removed, or YouTube changes its page structure), report that against the
    resource and continue with the rest.

4.  Compare coverage, point by point. Break each reference resource down into
    its atomic claims, rules, or topics. For each one, check whether the target
    standard addresses it, and classify it as one of:

    - **Missing.** The standard does not address it at all, and it falls
      within the standard's own stated scope.

    - **Partial.** The standard touches on it, but more shallowly than the
      reference, eg. the reference gives a worked exception the standard
      omits.

    - **Out-of-scope.** The reference covers it, but it plausibly sits
      outside this standard's stated purpose or audience. Note these
      rather than silently dropping them (the user may disagree with
      your scope call).

    Only missing and partial items are gaps. Do not manufacture a gap
    from a point the reference makes only in passing, or restate something
    the standard already covers using different words.

5.  Write or update `GAPS.md`. Use the structure in `./assets/GAPS.md`. Every
    individual gap MUST have:

    - A checkbox (`- [ ]`), so implementation status is visible at a glance.

    - The reference source it derives from (a URL with section/anchor
      where possible, or `<file>:<line>`).

    - Where in the standard it would fit — an existing `<file>:<line>`, or
      "new section" if nothing in the current structure holds it.

    - Whether it is missing, partial, or out-of-scope.

    Keep gaps as flat bullets. Do not introduce sub-headings, tables, or
    per-gap subsections.

6.  Report the gap count by category and anything you could not verify
    (a fetch failure, an ambiguous scope call). Stop there.

## Rules

- You MUST NOT edit the target standard's `.adoc` files, its `AGENTS.md`, or
  any file beyond `GAPS.md` itself.

- You MUST NOT stage or commit your changes to `GAPS.md`.

- You SHOULD NOT report gaps in the reference material that are covered by
  the technical standard, unless you have a good reason to do so. Your gap
  analysis MUST be focused on topics missing from the technical standard.

- You MUST NOT fabricate reference content. If a URL cannot be fetched, or a
  file cannot be read, report exactly that. Do not infer or recall it from
  your memory.

- Sub-agents, if used, MUST only be used to extract content from reference
  materials, and MUST NOT be used to analyze and classify gaps. A sub-agent
  spawned to extract claims from a reference resource MUST return only
  citation-tagged claims, never a missing/partial/out-of-scope verdict.

- You MUST preserve prior findings across re-runs. Where `GAPS.md` already
  exists, do not discard its history. A gap that is still open stays open with
  its original citation. A gap now covered gets checked off, not deleted.

- Every gap MUST cite a concrete source location and a concrete target
  location. A gap that cannot be tied to a specific place in the reference
  material and a specific place (or "new section") in the standard is not
  actionable.

## Edge cases

- **Stub standards.** A standard with only a placeholder has essentially
  unbounded scope for comparison. Report this and ask the user whether to
  proceed, since almost anything in the reference material could be
  called a gap.

- **Unreachable or partial reference resources.** If some URLs succeed and
  others fail, proceed with what was retrieved and list the failures
  separately in the report, rather than aborting the whole analysis.

- **Reference material broader than the standard.** Where an external
  resource is a comprehensive general reference (eg. an industry style
  guide covering many languages) and the standard is narrow (eg. one
  language), most of its content will be out-of-scope. Say so plainly
  rather than forcing a long "missing" list.

- **Reference material narrower than the standard.** Where the reference
  covers only a slice of what the standard addresses, most of the standard
  will simply have nothing to compare against. This is not itself a
  finding and should not be reported.

- **YouTube videos.** A YouTube URL is a reference resource whose primary
  content (spoken audio) cannot be fetched. Use the helper script in step 3b
  to extract the creator-supplied description and keywords, and compare
  against that — it is the author's own summary of the video's argument, not
  a full transcript. Say so plainly in `GAPS.md` so the user knows the depth
  of the comparison. If a full transcript is linked from the description,
  prefer that.

## Assets

- [GAPS.md template](./assets/GAPS.md): The structure to follow when
  writing or updating the report in step 5.

- [YouTube description extractor](./scripts/youtube_description.py): The
  helper script used in step 3b. Reads a video's title, author, length,
  keywords, and full description from YouTube's public oEmbed endpoint and the
  `ytInitialPlayerResponse` blob embedded in the watch page, with no API
  key. Run as `python3 .agents/skills/gap-analysis/scripts/youtube_description.py
  <video-id-or-url>`.
