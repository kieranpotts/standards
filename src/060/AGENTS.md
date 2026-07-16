# TS-60: GitHub Actions

Best practices for using (and making) GitHub Actions — authoring
workflows, designing actions, optimizing performance, and securing
CI/CD pipelines.

Use this when designing, authoring, reviewing, or securing GitHub
Actions workflows or custom actions.

Do NOT use this for general YAML syntax and conventions — see
[TS-30: YAML](../030/AGENTS.md). For general security and secrets
management, see [TS-52: Security and Secrets Management](../052/AGENTS.md).
For version control practices, see [TS-9: Version Control](../009/AGENTS.md).
For general code design, see [TS-7: Code Design](../007/AGENTS.md).

## Rules

### YAML syntax

- **Write YAML primarily with readability in mind.** Actions and
  workflows are defined in YAML files, which SHOULD be written primarily
  with readability in mind.

- **Consider maintenance and diffs.** Because Git is line-based, it is
  RECOMMENDED to use YAML's multi-line syntax for lists, so that adding
  or removing items produces clean diffs:

  ```yaml
  # Prefer:
  on:
    push:
      branches:
        - main

  # Over:
  on:
    push:
      branches: [ "main" ]
  ```

- **Use YAML comments to document anything not intuitively understood**
  from the YAML data structure and the workflow/action schema.

### Designing workflows and actions

#### General guidelines

- **Compose workflows from modules.** Encourage reuse by breaking out
  discrete parts of pipelines into actions, reusable workflows, or
  workflow templates.

- **Break down workflows into small, discrete jobs and steps.** This
  makes it easier to manage conditions and dependencies.

- **Choose descriptive and meaningful names for secrets and variables.**
  It SHOULD NOT be necessary to consult out-of-band documentation to
  understand the purpose of a secret or variable referenced in a
  workflow. If the meaning cannot be easily deduced from the name and
  context, include an adjacent comment.

- **Names for workflows, jobs, and steps SHOULD be clear and
  consistent.**

- **Test workflows thoroughly.** Ensure that conditional logic and job
  dependencies work as expected by testing all possible scenarios that
  could trigger each workflow.

#### Events

- **Be explicit about the specific event types that trigger your
  workflows.** For event types such as `pull_request`, if you do not
  specify the _types_ of events, GitHub will assume default activity
  types. Use event filters and activity types to refine triggers:

  ```yaml
  on:
    pull_request:
      types:
        - opened
        - synchronize
      branches:
        - main
        - dev
  ```

#### Jobs

- **Each job definition SHOULD be responsible for a single concern.**
  Although a single job may compile, test, _and_ deploy an application,
  it is best practice for complex workflows to be composed from
  multiple single-responsibility jobs. This makes workflows easier to
  extend and maintain, and logging output easier to analyze.

#### Steps

- **All steps SHOULD be given a unique name.** This helps identify the
  output of each step in the logs, making it easier to debug failed
  workflows.

  ```yaml
  steps:
    - name: Say hello
      run: echo "Hello, world!"
  ```

#### Expressions

- **Expressions are commonly used in `if` attributes** to make execution
  of a step or job conditional. The value of the `if` attribute is
  treated as a JavaScript expression, not a string value. Expressions
  can be used in other attributes (which assume string values by
  default) using the `${{ <expression> }}` notation.

- **If an expression starts with `!`, it MUST be encapsulated in
  `${{ }}`** syntax, or escaped with `''`, `""`, or `()`, because the
  exclamation mark is reserved notation in YAML.

- **For consistency, it is RECOMMENDED to use the `${{ <expression> }}`
  syntax to wrap _all_ expressions**, even those in `if` values where
  this syntax is not required:

  ```yaml
  jobs:
    production-deploy:
      if: ${{ github.repository == 'owner/repo' && github.ref == 'refs/heads/main' }}
  ```

#### Repository and environment variables

- **Workflows SHOULD include fallback values for variables** that are
  supposed to be configured via the repository, to protect the workflow
  from those variables being accidentally deleted from the repository's
  configuration:

  ```yaml
  env:
    MY_ENV_VAR: ${{ vars.MY_ENV_VAR || 'default value' }}
  ```

- **For secrets, workflow scripts MUST check for a valid value and fail
  the step if a secret is missing.**

### Performance optimization

#### Minimalism

- **Keep individual workflows and reusable actions as minimal as
  possible.** The more time something takes to set up and run, the
  higher the costs of running your CI/CD infrastructure. Even shaving a
  few seconds off can add up to significant cost savings.

- **Prefer lightweight actions over heavyweight ones.** Prefer
  JavaScript actions over container actions, and best of all are
  composite actions consisting of simple shell scripts. Where container
  actions are essential (eg. requiring a specific toolchain), prefer
  light images such as alpine or alpine-node over heavy ones.

- **Don't install unnecessary dependencies.**

#### Caching

- **Use caching wherever possible.** Have package managers cache
  dependencies, and cache any generated artifacts that can be reused
  between jobs or workflow runs.

#### Timeouts

- **It is RECOMMENDED to specify shorter timeouts, appropriate for each
  job.** By default, GitHub kills jobs after 6 hours. Many jobs don't
  need nearly that much time, but sometimes jobs can hang and consume
  unnecessary minutes. Specify via `jobs.<job_id>.timeout-minutes`:

  ```yaml
  jobs:
    set_config:
      timeout-minutes: 30
      runs-on: ubuntu-latest
  ```

#### Concurrency

- **It is RECOMMENDED to implement a concurrency strategy for
  workflows**, especially long-running, resource-intensive ones. This
  cancels running workflows in the same group when an event triggers a
  new run — for example, automatically canceling intermediate builds on
  a PR when a newer commit gets pushed:

  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: ${{ startsWith(github.ref, 'refs/pull/') }}
  ```

### Security

#### Secrets

- **Do not hard-code secrets in workflow files, even in private
  repositories.** All sensitive data MUST be managed via GitHub Secrets.

- **Secrets SHOULD be regularly rotated, and unused ones deleted.**
  Restrict who has permissions to create and update secrets.

- **Secrets SHOULD be primitive values** such as strings or numbers, not
  complex data types:

  ```txt
  # Good
  SENSITIVE_VALUE1 = "abcdef"
  SENSITIVE_VALUE2 = 123456

  # Bad
  {
    "sensitiveValue1": "abcdef",
    "sensitiveValue2": 123456
  }
  ```

- **Mask any generated sensitive values in log output.** Audit the
  source code of third-party actions to make sure they do the same:

  ```yaml
  echo "::add-mask::$GENERATED_SENSITIVE_VALUE"
  ```

- CI workflows are also a good place to implement secrets detection
  using tools like
  [GitGuardian](https://github.com/GitGuardian/ggshield-action).

#### Tokens

- **Avoid storing tokens and other long-lived secrets where possible.**
  For example, rather than using API keys to authenticate with
  infrastructure providers, prefer using OpenID Connect (OIDC). With
  OIDC, you exchange GitHub's OIDC token for short-lived cloud
  credentials that are valid only for a single job and automatically
  expire after that.

- **DO NOT use classic Personal Access Tokens (PATs) to grant workflow
  access to code from another repository.** Ideally, create a GitHub App
  and use its short-term credentials. If needed, use a fine-grained PAT
  with as few permissions as necessary (eg. only read access to the
  required repositories).

- **Rotate fine-grained PATs regularly.** PATs are bound to specific
  GitHub users, so it is RECOMMENDED to create a generic shared user
  account against which to create your PATs.

#### `GITHUB_TOKEN` permissions

- **Apply the principle of least privilege to `GITHUB_TOKEN`.** By
  default, the auto-generated `GITHUB_TOKEN` is given wide-ranging
  permissions. Permissions SHOULD be explicitly restricted on a
  per-workflow or per-job basis using the `permissions` attribute:

  ```yaml
  permissions:
    contents: read

  jobs:
    open-issue:
      runs-on: ubuntu-latest
      permissions:
        contents: read
        issues: write
  ```

- **Workflows MUST NOT pass the `$GITHUB_TOKEN` value to untrusted
  third-party software**, including actions from untrusted sources.

- **The same practices apply for all kinds of tokens** you create to
  authenticate with any service and store in GitHub Secrets: always
  restrict permissions to the bare essentials, and rotate tokens
  regularly.

#### Environment variable scope

- **Declare environment variables at the step level wherever possible.**
  Elevate them to the job or (rarely) workflow level only to solve the
  problem of sharing data between steps within a job, or between jobs
  within a workflow.

#### Untrusted input

- **Don't directly reference values you don't control.** The following
  context data cannot be trusted: `github.event.issue.title`,
  `github.event.issue.body`, `github.event.pull_request.title`,
  `github.event.pull_request.body`, `github.event.comment.body`,
  `github.event.review.body`, `github.event.pages.*.page_name`,
  `github.event.commits.*.message`, `github.event.head_commit.message`,
  `github.event.head_commit.author.email`,
  `github.event.head_commit.author.name`,
  `github.event.commits.*.author.email`,
  `github.event.commits.*.author.name`,
  `github.event.pull_request.head.ref`,
  `github.event.pull_request.head.label`,
  `github.event.pull_request.head.repo.default_branch`,
  `github.head_ref`.

- **The RECOMMENDED solution is to extract scripts to custom actions**
  that accept inputs via their arguments. These SHOULD be JavaScript or
  container actions, which run in an isolated environment rather than
  directly in the runner:

  ```yaml
  uses: ./.github/actions/print
  with:
    text: ${{ github.event.pull_request.title }}
  ```

- **A second option is to bind the input value to an intermediate
  environment variable**, then print from that variable. This is not
  proper input sanitization and is not as robust, but may be adequate
  for private repositories where you trust contributors:

  ```yaml
  - name: Print title
    env:
      PR_TITLE: ${{ github.event.pull_request.title }}
    run: |
      echo "$PR_TITLE"
  ```

  Double-quote shell variables to avoid word splitting.

- **It is RECOMMENDED to use code scanning tools** to help detect
  potential exploits in your workflow code.

#### Consuming open source actions

- **Open source actions MUST be carefully audited** before integrating
  them into your development toolchain. The risks are similar to using
  package managers to integrate third-party components.

- **RECOMMENDED steps when using third-party actions:**
  - Use only actions that are actively maintained (bugs triaged and
    fixed, security vulnerabilities quickly patched).
  - Use only actions published to the GitHub Marketplace and verified
    by GitHub.
  - Review the action's `action.yml` file for inputs and outputs, and
    check that the code does what it says it does.
  - **Pin to a specific audited version — best practice is to specify a
    commit SHA, rather than a branch or version tag.** This locks the
    action's code down and protects against unexpected supply-chain
    compromises:

    ```yaml
    - name: Checkout code
      uses: actions/checkout@a12a3943b4bdde767164f792f33f40b04645d846
    ```

#### PRs from forks

- **It is RECOMMENDED to disable automatic workflow runs from events
  triggered from forks.** Workflows on PRs from _first-time_ outside
  contributors do not run automatically by default, but it is
  RECOMMENDED to disable automatic runs from external contributors
  _all of the time_.

- **Project maintainers MUST review code coming from external PRs
  before triggering the CI to run** on those changes.

- **When adding workflows to public repositories, consider:**
  - What events could trigger a run?
  - What code will be executed in the runner? Can it be trusted?
  - What inputs are given to the workflow? Can _that_ be trusted?
  - What data, secrets, and services does that code access?

- **Use of `pull_request_target` is especially dangerous and MUST be
  restricted to specific use cases.** When workflows are triggered by
  this event, the runner is given the _base_ repository's secrets and
  `GITHUB_TOKEN` is granted write permissions on the PR's base
  repository — more potential attack vectors than the conventional
  `pull_request` event. The `pull_request_target` event was introduced
  "to enable workflows to label PRs (eg. needs review) or to comment on
  the PR" and is not intended for any kind of building, running, or
  other processing of the PR's changeset. **Workflows triggered by
  `pull_request_target` MUST NOT check out, build, or run the
  repository's code.** Such workflows SHOULD NOT save any caches (to
  prevent cache poisoning).

#### Self-hosted runners

- **Use self-hosted runners only for workflows defined in private
  repositories.** Any code that `runs-on: self-hosted` runners MUST be
  kept private. In public repositories, third parties could run
  malicious code on your self-hosted runners by forking the repository
  and opening a PR that triggers a workflow to run on _their_ code in
  the head branch of their fork.

- **If using self-hosted runners, you are fully responsible for
  hardening your infrastructure**, for example by:
  - Configuring a dedicated low-privilege user.
  - Using isolated and ephemeral workloads to execute the jobs.
  - Implementing logging and monitoring to ensure visibility.

  The ultimate security is ensuring self-hosted runners can only be
  used by trusted users inside your organization — keeping private the
  workflows and actions that run on them.

#### GitHub-hosted runners

- **Pin workflows to specific runner versions**, such as
  `ubuntu-22.04` rather than `ubuntu-latest`. You must manually update
  workflow configurations when old runner versions are deprecated, but
  the tradeoff is more stable workflows. (This is more a maintenance
  issue than a security one.)

  ```yaml
  # Prefer:
  runs-on: ubuntu-22.04

  # To:
  runs-on: ubuntu-latest
  ```

## References

- [TS-60: GitHub Actions (source)](README.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-9: Version Control](../009/AGENTS.md)
- [TS-30: YAML](../030/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [GitHub: Security Hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [GitHub Security Lab: Preventing pwn requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)
- [GitHub Docs: Workflow syntax — concurrency](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#concurrency)
- [GitHub Docs: Workflow syntax — permissions](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#permissions)
- [GitGuardian](https://github.com/GitGuardian/ggshield-action)