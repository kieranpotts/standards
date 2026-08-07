# Expanding a GitHub issue into reference resources

Read this when a reference resource is a URL matching
`https://github.com/kieranpotts/<repo>/issues/<number>`.

An issue under `kieranpotts/*` is never itself the reference material. It is an
index of material: the real resources are the URLs and attachments named in its
description, its comments, and its sub-issues. Expand it first, then ingest
whatever it yields under the normal rules.

## Pull the issue apart

Title and body:

```sh
gh issue view <url> --json title,body
```

Comments, in full:

```sh
gh issue view <url> --json comments --jq '.comments[].body'
```

Sub-issues (number, state, title, URL):

```sh
gh api repos/kieranpotts/<repo>/issues/<number>/sub_issues \
  --jq '.[] | "\(.number)\t\(.state)\t\(.title)\t\(.html_url)"'
```

If the `sub_issues` endpoint returns 404 — an older `gh` or API version —
fall back to GraphQL:

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

Every URL mentioned across the title, body, and comments, in one pass. Dedupe,
then drop the issue's own URL and any sub-issue URLs already captured above —
those are handled separately, not as resources in their own right:

```sh
gh issue view <url> --json body,comments \
  --jq '[.body, (.comments[].body)] | join("\n")' \
  | grep -oE 'https?://[^ )>"'"'"']+' | sort -u
```

## Then

Where a sub-issue is itself under `kieranpotts/*`, apply this same expansion to
it rather than treating the sub-issue as a resource.

Where the issue and its sub-issues yield no discoverable resources at all,
report that and ask the user for clarification rather than guessing at what
was meant.
