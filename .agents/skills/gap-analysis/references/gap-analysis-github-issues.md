# Expanding a GitHub issue into reference resources

Read this when a reference resource is a URL matching
`https://github.com/kieranpotts/<repo>/issues/<number>`.

An issue under `kieranpotts/*` SHOULD NOT itself be treated as reference material,
but rather as an index of reference material. The real resources are the URLs
and attachments named in the issue's description, its comments, and its
sub-issues.

Follow the below steps to extract information from a GitHub issue.

Extract the issue's title and body:

```sh
gh issue view <url> --json title,body
```

Extract comments, in full:

```sh
gh issue view <url> --json comments --jq '.comments[].body'
```

Extract sub-issues (number, state, title, URL):

```sh
gh api repos/kieranpotts/<repo>/issues/<number>/sub_issues \
  --jq '.[] | "\(.number)\t\(.state)\t\(.title)\t\(.html_url)"'
```

If the `sub_issues` endpoint returns 404, fall back to GraphQL:

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

Next capture every URL mentioned across the title, body, and comments, in one
pass. Dedupe.

```sh
gh issue view <url> --json body,comments \
  --jq '[.body, (.comments[].body)] | join("\n")' \
  | grep -oE 'https?://[^ )>"'"'"']+' | sort -u
```

Where a sub-issue is itself under `kieranpotts/*`, apply the same expansion
steps as above.

Where the issue and its sub-issues yield no discoverable resources at all,
report that and ask the user for clarification.
