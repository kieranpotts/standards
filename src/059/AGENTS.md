# TS-59: Terraform

Best practices for working with Terraform, HCL, and related technologies.

Focused on the Community Edition of Terraform (the Terraform CLI) and
its drop-in fork OpenTofu, rather than commercial services such as HCP
Terraform (formerly Terraform Cloud) and Terraform Enterprise.

Use this when authoring Terraform/HCL configurations, organizing
Terraform projects, or managing infrastructure-as-code lifecycles.

Do NOT use this for general version control practices — see
[TS-9: Version Control](../009/AGENTS.md). For versioning practices, see
[TS-11: Versioning](../011/AGENTS.md). For security and secrets
management (referenced by the secrets-in-state rules), see
[TS-52: Security and Secrets Management](../052/AGENTS.md). For privacy
and PII handling, see [TS-53: Privacy and Data Protection](../053/AGENTS.md).
For cloud platform engineering, see
[TS-49: Cloud Platform Engineering](../049/AGENTS.md). For AWS-specific
resource patterns, see [TS-51: Amazon Web Services (AWS)](../051/AGENTS.md).
For QA and testing practices, see [TS-12: Quality Assurance](../012/AGENTS.md)
and [TS-13: Functional Testing](../013/AGENTS.md). For release mechanics,
see [TS-10: Releasing](../010/AGENTS.md). For general code design, see
[TS-7: Code Design](../007/AGENTS.md).

## Rules

### HCL style guide

- **Use HCL for all Terraform configuration files.** HCL is generally
  preferred over JSON (which Terraform supports via `.tf.json` files)
  because it is more concise, easier to read, and a better fit for
  Terraform's use case.

- **Follow Terraform's own style guide.** HCL code SHOULD be formatted in
  a consistent style following the conventions in
  [Terraform's style guide](https://developer.hashicorp.com/terraform/language/style).

- **Use `terraform fmt` to auto-format.** It is RECOMMENDED to use
  `terraform fmt` to format configuration files to Terraform's canonical
  style. Pre-commit hooks SHOULD run `terraform fmt` automatically at
  check-in. (By default `terraform fmt` runs on `.tf` files in the
  current working directory; add `-recursive` to include subdirectories.)

- **A linter such as [TFLint](https://github.com/terraform-linters/tflint)
  MAY be used** to enforce an organization's own coding standards that
  extend the Terraform canonical style.

- **Run `terraform validate` before committing** (RECOMMENDED). This
  checks that configuration is syntactically valid and internally
  consistent. It is RECOMMENDED to configure text editors to run this
  command as a post-save check, and to configure Git to run it via the
  pre-commit hook.

#### Character encoding and line endings

- Terraform requires configuration files to be UTF-8 encoded. Both
  Unix-style (LF) and Windows-style (CRLF) line endings are supported.
  The idiomatic style is Unix (LF). Formatting tools SHOULD be
  configured to automatically fix line endings to the Unix style.

#### Indentation

- Block contents SHOULD be indented with two spaces from the parent
  block.

#### Line lengths

- Except for `variable` and `output` blocks (where single-line strings
  are preferred), most HCL code SHOULD follow a 120-column line-length
  limit.

#### Comments

- Use `#` for all comments (both block-level and inline) — this is the
  canonical style RECOMMENDED by Terraform's style guide. The `//`
  notation MAY be used to temporarily comment-out code. The
  `/* ... */` notation SHOULD NOT be used.

- Comments SHOULD be written on the line(s) immediately preceding the
  code they refer to. Short end-of-line comments MAY be used where doing
  so improves readability; readability can be improved further by
  vertically aligning adjacent end-of-line comments.

- Comments SHOULD be written in full, proper American English sentences.

#### Naming conventions

- **Block labels, variables, and outputs SHOULD be named using lower
  snake case:** `example_instance`, not `ExampleInstance`,
  `exampleInstance`, or `example-instance`.

  ```hcl
  resource "aws_instance" "example_instance" {}
  variable "vpc_id" {}
  output "instance_name" {}
  ```

- Wrap the resource type and name in double quotes in resource
  definitions. Use singular nouns for resource names. Do not repeat the
  resource type in the name.

#### Blocks

- All blocks (top-level and nested) SHOULD be separated from one
  another by a single blank line. MAY have exceptions (eg. grouping
  multiple `provisioner` sub-blocks).

#### Arguments

- When multiple arguments with single-line values appear on consecutive
  lines at the same indentation level, align their assignment operators:

  ```hcl
  ami           = "abc123"
  instance_type = "t2.micro"
  ```

- Use empty lines to separate logical groups of arguments within a
  block.

- When both arguments and blocks appear together inside a block body,
  place all arguments at the top and nested blocks below them, with one
  blank line separating arguments from blocks.

- For blocks that contain both arguments and meta-arguments, list
  meta-arguments first and separate them from other arguments with one
  blank line. Place meta-argument blocks last and separate them from
  other blocks with one blank line.

  ```hcl
  resource "aws_instance" "example" {
    # Meta (Terraform-specific) arguments:
    count = 2

    # Regular (provider-specific) arguments:
    ami           = "abc123"
    instance_type = "t2.micro"

    # Regular blocks (provider-specific):
    network_interface {
      # ...
    }

    # Meta-argument blocks (Terraform-specific):
    lifecycle {
      create_before_destroy = true
    }
  }
  ```

#### Heredocs

- Multi-line string values MAY be inputted using
  [heredoc syntax](https://developer.hashicorp.com/terraform/language/expressions/strings#heredoc-strings)
  (opened with `<<`). Terraform also supports indented heredocs (opened
  with `<<-`), which allow the heredoc's string content to be indented
  to match the outer HCL code.

- **For complex user scripts and other long string values, prefer to
  import from separate files** rather than using heredocs inline. This
  improves readability and avoids breaking syntax highlighting in code
  editors:

  ```hcl
  resource "aws_instance" "web_server" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t3.micro"

    user_data                   = file("scripts/user_data.sh")
    user_data_replace_on_change = true
  }
  ```

- Imported files SHOULD be kept in a `scripts/*` or `files/*`
  directory.

### Version control

- **Keep Terraform configurations under version control** (RECOMMENDED)
  to support versioning of infrastructure changes. For collaboration,
  there SHOULD be a single centralized reference repository that
  contains the source-of-truth for a project's infrastructure
  configuration.

- **Hosted repositories MUST be private** (not publicly accessible
  except to authorized users).

#### Excluded files

- **The following files and directories MUST NOT be committed to source
  control:**
  - `.terraform/` — auto-generated working files.
  - `terraform.tfstate` — the state file. Plain text, likely to contain
    access keys and other secrets. Backups (`*.tfstate.backup`) MUST
    also be excluded.

- **`terraform.tfvars` MAY be excluded** if it includes sensitive data.
  If excluded, a `terraform.tfvars.example` (keys but no values) SHOULD
  be committed for reference.

- **RECOMMENDED baseline `.gitignore`:**

  ```
  .terraform/
  *.tfstate
  *.tfstate.backup
  *.local.hcl
  terraform.tfvars
  *.auto.tfvars
  *.auto.tfvars.json
  ```

- **The `.terraform.lock.hcl` file SHOULD be committed to version
  control.** It is machine-generated (created on `terraform init`) and
  guarantees that everyone installs the exact same provider versions.
  The file SHOULD NOT be edited directly; use `terraform init -upgrade`
  to update dependencies.

- **Always run `terraform init` after pulling changes** (RECOMMENDED)
  and before running any additional `terraform` commands, to update
  local dependencies to match those specified in
  `.terraform.lock.hcl`.

### Secrets

#### Secrets in configuration files

- **Secrets MUST NOT be hard-coded in Terraform configuration files** —
  even if those files are committed to private version control
  repositories.

- **Access credentials MUST be retrieved either from the environment or a
  secure remote vault.** The AWS provider allows importing credentials
  from the AWS CLI's `~/.aws/credentials` file by profile name.

- **For other secrets, the RECOMMENDED approach is to pass them in from
  environment variables.** Variables with the `TF_VAR_` prefix are
  automatically picked up by Terraform and auto-filled into variables:

  ```
  export TF_VAR_password=abcdefghik
  ```

#### Secrets in outputs

- **Secrets MUST NOT be exposed in output from `terraform apply`
  commands.** Secret values are given the `sensitive = true` argument in
  output blocks. This means the value will not be displayed in console
  output, so secrets will not leak into log files in automation
  pipelines.

  ```hcl
  output "rds_password" {
    value     = data.aws_ssm_parameter.rds_password.value
    sensitive = true
  }
  ```

#### Secrets in state files

- **Secrets (passwords, etc.) _will_ be printed in `terraform.tfstate`,
  whether or not those secrets are marked as sensitive.** Therefore, the
  state file MUST be stored securely and access restricted to only
  authorized personnel.

- **It is RECOMMENDED to use encryption at rest for the state file.**
  State files MAY be encrypted in private Git repositories using tools
  such as [git-secret](https://git-secret.io/),
  [transcrypt](https://github.com/elasticdog/transcrypt), or
  [SOPS](https://github.com/mozilla/sops). But it is best practice to
  exclude state files from version control entirely and instead store
  them in a secure back-end (eg. an S3 bucket with server-side
  encryption). See *Remote state and back-ends* below.

See [TS-52: Security and Secrets Management](../052/AGENTS.md).

### Remote state and back-ends

- **Use secure back-ends to store Terraform state remotely**
  (RECOMMENDED). Terraform's default behavior is to store state locally
  in `terraform.tfstate`. State can be moved to a remote back-end by
  configuring the `terraform.backend` block:

  ```hcl
  terraform {
    backend "s3" {
      bucket = "terraform-remote-state-abcdef"
      key    = "dev/network/terraform.tfstate"
      region = "us-west-2"
    }
  }
  ```

  Remote back-ends are more secure, allow team collaboration, and make
  infrastructure automation easier (eg. running Terraform in CI/CD
  pipelines).

- **Remote storage systems MUST be private and the state files MUST be
  encrypted at rest.** For object storage systems, it is sufficient to
  enable filesystem encryption on the bucket. (Secrets are stored in
  state files in plain text.)

- **Remote state back-ends MUST enable the `use_lockfile` option.** This
  applies a lock to the remote state while a `terraform apply` operation
  is in progress, preventing concurrent state changes from corrupting
  the infrastructure. (Users can still override this with
  `terraform apply -lock=false`, so strong governance and well-designed
  change management procedures are the only true protection against
  concurrent state changes.)

  ```hcl
  terraform {
    backend "s3" {
      bucket       = "terraform-remote-state-abcdef"
      key          = "network/terraform.tfstate"
      region       = "us-west-2"
      use_lockfile = true
    }
  }
  ```

- **Use multiple state files to split infrastructure into components**
  that can be managed independently — particularly useful for
  enterprise-scale infrastructure, or where different teams manage
  different bits of the infrastructure. Alternatively, split state by
  layers (eg. separating networking configuration from the application
  layer).

### Provisioners

- **Custom scripts called by Terraform SHOULD be kept separate from the
  main infrastructure configuration files.** It is RECOMMENDED to use a
  `scripts/` directory for this purpose.

- **Usage of custom scripts should be kept to a minimum.** The state of
  resources created through scripts is not accounted for or managed by
  Terraform. Use custom scripts only when Terraform doesn't support the
  desired behavior. Custom scripts MUST have a clearly documented
  reason for existing, and ideally a deprecation plan.

### Organizing Terraform code

How you organize Terraform code is important for maintainability. It
should be immediately clear, from the filesystem design, where a
maintainer can find a specific resource or data source definition.

#### Filesystem design

- **RECOMMENDED starting-point files for a new infrastructure-as-code
  project:**
  - `terraform.tf` — single `terraform` block defining
    `required_version` and `required_providers`.
  - `backend.tf` — back-end configuration for remote state storage.
  - `providers.tf` — cloud provider configuration.
  - `main.tf` — main resources and data source blocks.
  - `variables.tf` — variable blocks, in alphabetical order.
  - `locals.tf` — local values.
  - `outputs.tf` — output definitions, in alphabetical order.
  - `override.tf` or `*_override.tf` — override definitions.

- **For large-scale projects, refactor the filesystem to represent a
  higher level of granularity.** RECOMMENDED baseline directory
  structure supports multiple projects, organized by environment
  (dev/staging/prod), with each environment a root Terraform module
  (own state files and back-end). Resources within an environment MAY be
  further organized by resource type:

  ```
  .
  ├── modules/
  │   ├── aws_network/
  │   └── aws_database/
  ├── projects/
  │   └── <project-a>/
  │       ├── modules/
  │       ├── environments/
  │       │   ├── dev/   (kms/, network/, route53/, s3/, vpc/{applications, databases, ecs_cluster, vpn}/, main.tf)
  │       │   ├── prod/  (same layout)
  │       │   └── staging/ (same layout)
  │       └── shared/ (locals.tf, data.tf)
  ├── shared/ (locals.tf, data.tf)
  ├── scripts/
  ├── helpers/
  └── files/
  ```

- **Each environment is managed and deployed independently.** Each
  environment subdirectory is a root Terraform module with its own state
  files and back-end configuration. If necessary, state can be shared
  between projects using the `terraform_remote_state` data source.

- **All components of the infrastructure configuration are abstracted
  into environment-agnostic, reusable modules** that accept input
  variables for environment-specific customization. An environment's
  `main.tf` imports configurations from resource subdirectories using
  module declarations; resources are defined by composing modules with
  environment-specific variables, rather than declaring resources
  directly.

- **Environment-specific `.tfvars` files MAY be included within
  projects** for easy environment-specific customization. Complex
  variable types (eg. `map(object({...}))`) MAY be used to manage
  environment differences. Dynamic blocks can also be used for
  environment-specific configuration.

- **Use variable validation to enforce environment-specific variables
  being set correctly:**

  ```hcl
  variable "environment" {
    type = string
    validation {
      condition     = contains(["development", "staging", "production"], var.environment)
      error_message = "Environment must be development, staging, or production."
    }
  }
  ```

- **Terraform-specific code SHOULD be kept isolated** from other
  scripts, binaries, and files not directly related to infrastructure
  configuration. Scripts executed by `local-exec` or `remote-exec`
  provisioners SHOULD be placed in a `scripts/` directory. Custom helper
  scripts run independently of Terraform SHOULD be put in a `helpers/`
  directory. Static files referenced by `file()` or `templatefile()`
  SHOULD be put in a `files/` directory.

- **Terraform workspaces are meant only for testing production
  configurations** by pre-deploying to isolated, ephemeral environments.
  Workspaces do not allow variation in configuration of each environment
  (eg. you can't define a VPN and load balancer only for production).
  [Terragrunt](https://terragrunt.gruntwork.io/),
  [Terraspace](https://terraspace.cloud/), and
  [Terramate](https://terramate.io/) are meta-frameworks that simplify
  multi-environment configurations.

### Workspaces and state scope

- **Each deployment environment SHOULD have its own state.** State
  MUST NOT be shared between production and pre-production
  environments. The RECOMMENDED way to separate state per environment is
  a separate root module per environment, each with its own back-end
  configuration pointing to a distinct state path or workspace.

- **Terraform workspaces allow a single root module to maintain multiple
  named states against the same configuration.** They are best suited
  to ephemeral, short-lived deployments that share an identical
  configuration (eg. a temporary copy of production for testing). They
  SHOULD NOT be used to manage long-lived environments that differ in
  their resource configuration, because the configuration cannot vary
  per workspace without awkward `terraform.workspace` checks.

- **In HCP Terraform, a _workspace_ is a different concept:** a named
  object holding a configuration, its variables, its state, and its run
  settings — corresponding to a single state and a single root module.
  HCP Terraform's
  [best practices](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/best-practices#workspace-structure)
  recommend scoping each workspace to a single, cohesive set of
  resources. The same principle applies to the Community Edition: keep
  each state focused on one logical unit.

- **Limit the blast radius of a single state.** A state SHOULD contain
  only the resources that are deployed and lifecycle-managed together.
  Resources with independent lifecycles SHOULD be split into separate
  states and composed with `terraform_remote_state` or module outputs.

#### Providers

- **A single default provider configuration MUST be included for every
  project.** The default provider is the block without an `alias`
  argument. Additional aliased providers MAY be added for multi-region
  or multi-account configurations.

#### Logical grouping of resources

- **Avoid giving each resource its own file.** Create logical groupings
  of resources within their own files with descriptive names (eg. all
  DNS resources in `route53.tf`, or a group of `.tf` files under a
  `dns/` directory).

- **Avoid grouping multiple blocks of the same type with other blocks
  of different types**, unless the mixed block types form a semantic
  family (eg. `root_block_device`, `ebs_block_device`, and
  `ephemeral_block_device` on `aws_instance`).

- **In any one `.tf` file, the configuration SHOULD build on itself, top
  to bottom.** Dependent resources SHOULD be defined _after_ the
  resources they reference.

#### Loops

- **Use `count` and `for_each` sparingly.** Use loops to define
  resources that are _genuine_ replicas (eg. for redundancy). Resources
  that _coincidentally_ share the same configuration SHOULD be defined
  separately. Sometimes reducing duplication helps maintainability;
  sometimes duplication actually makes it easier to maintain things.

#### Data sources

- **[Data sources](https://developer.hashicorp.com/terraform/language/data-sources)
  SHOULD be declared next to the resources that reference them.** For
  example, if fetching an image to launch an instance, place it
  alongside the instance instead of collecting data resources in their
  own file. However, if the number of data sources becomes large, they
  MAY be extracted to a dedicated `data.tf` file.

#### Descriptions

- **It is RECOMMENDED to provide descriptions for all resources,
  variables, outputs, and other block types that support descriptions.**
  This reduces the need for inline comments and is displayed alongside
  resources in the cloud provider's web console. Descriptions can be
  useful for auditing purposes too.

#### Variables

- **It is RECOMMENDED to define variables for all values that are likely
  to change between environments, or between deployments to the same
  environment.** Good candidates: resource names, CIDR ranges, tags,
  instance types, AMI IDs, environment names, environment variables.

- **All variables MUST be declared in `variables.tf`.** Include a type
  and a description for every variable. Give variables descriptive names
  relevant to their usage or purpose.

- **Numeric values MUST be named with units**, such as `ram_size_gb`.
  To simplify conditional logic, give boolean variables positive names,
  eg. `enable_external_access`.

- **Variables MUST have descriptions.** Descriptions are automatically
  included in a published module's auto-generated documentation.

##### Default values

- For root projects, it is RECOMMENDED that all variables have default
  values — this allows configuration to be applied without user input,
  supporting automation via CI/CD.

- For modules, some input variables MAY omit default values, so calling
  code is required to provide meaningful values.

##### Validation

- **Use validation blocks wherever practical** (RECOMMENDED). Each
  validation block defines a condition that assigned values must meet;
  if the condition is not met, an error message is displayed and
  `terraform apply` will not run.

  ```hcl
  variable "password" {
    description = "Password input"
    type        = string
    sensitive   = true
    validation {
      condition     = length(var.password) == 10
      error_message = "Your password must be 10 characters exactly"
    }
  }
  ```

#### Local values

- Local values assign a value to a variable used only within the scope
  of the module it is defined in — useful for generating values from an
  expression that is referenced from multiple points in the
  configuration.

- If you reference a local value in multiple files, define it in a file
  named `locals.tf` within the root project or module. If the local
  value is specific to a particular file, define it at the top of that
  file.

- **Avoid overuse of local values.** They increase the cognitive
  overhead required to understand a configuration. Oftentimes it is
  better to just repeat an expression wherever it is needed.

#### Overrides

- **Use overrides sparingly.** They make it harder to reason about the
  configuration — it becomes less clear where changes should be made.

- **Where overrides are used, there MUST be prominent comments
  adjacent to the original resource definitions** declaring that
  overrides exist for those definitions.

- For small projects, all overrides MAY be grouped into a single
  root-level `overrides.tf` file. For large projects, it is RECOMMENDED
  to add overrides in files named `[file]_override.tf`, where `[file]`
  is the name of the file (in the same directory) that contains the
  original definitions.

#### Modules

- **A good module should raise the level of abstraction** by
  introducing a new concept to your architecture (such as the idea of a
  "web server" or "document store"), hiding the particular resource
  types and configuration details used to implement those concepts.

- **Avoid writing modules that are merely thin wrappers around existing
  resource types.** If you want low-level modules like that, there
  probably already exist public open-source ones you can reuse. For AWS,
  check out the [Terraform AWS modules](https://github.com/terraform-aws-modules)
  project.

- **Maintain a flat module tree, rather than a hierarchy of nested
  modules** (RECOMMENDED). This design constraint emphasizes
  composition of infrastructure from loosely-coupled, highly-reusable
  components.

- **Modules sufficiently generic to be reusable in different projects
  MAY be extracted to shared upstream code repositories or module
  registries.**

##### Module files

- **A module MUST have the following files as a minimum:**
  - `README` — basic documentation (inputs, required/optional, outputs).
  - `variables.tf` — input variables.
  - `main.tf` — main resources and data sources.
  - `outputs.tf` — outputs the calling module can capture.

- **Complex modules SHOULD include an `examples/` directory**, with a
  separate subdirectory for each example. Include a `README` for each
  example. Each example should be a self-contained Terraform project
  that uses the module.

- **Each module SHOULD be entirely self-contained; there SHOULD NOT be
  any shared globals** (such as local values or data sources).

- **Each module MUST have its own `README`.** In large organizations,
  an `OWNERS` (or `CODEOWNERS` for GitHub) file SHOULD document the
  teams or individuals responsible for maintaining the module.

##### Module input variables

- **Modules MAY have input variables that omit default values**, so
  calling code is required to provide meaningful values. (Root projects
  SHOULD try to have default values for all their variables.)

- **Modules SHOULD allow their consumers to fully configure the labels
  and tags** applied to all resources the module creates. Consider
  providing a labels variable with a default value of an empty map.

- **Be judicious in your use of input variables within modules.** Only
  parameterize values that must vary for each instance or environment.
  Ensure you have a concrete use case for changing that variable.

- **Adding a variable with a default value is backwards-compatible.
  Removing a module variable is not**, so do this only if you can
  update all the calling code simultaneously.

- **Projects SHOULD always import external modules at a fixed
  revision** (preferably a release tag). This protects against
  unexpected breaking changes in imported modules.

##### Module outputs

- **Organize all module outputs in `outputs.tf`.** Provide meaningful
  descriptions for all outputs, and document all of them in the
  module's `README`.

- **Expose outputs for all resources created by the module.** Without
  outputs, users cannot properly order your module in relation to
  their Terraform configurations.

- **Do not pass outputs directly through input variables**, because
  doing so prevents them from being properly added to the dependency
  graph. Have all outputs reference attributes from resources.

  ```hcl
  # Not recommended:
  output "name" {
    value = var.name
  }

  # Recommended:
  output "name" {
    description = "Name of instance"
    value       = google_compute_instance.main.name
  }
  ```

##### Providers and back-ends

- **Modules MUST NOT configure providers or back-ends.** These MUST be
  configured in a Terraform project root.

- **Modules SHOULD define their minimum required provider versions**
  via a `terraform.required_providers` block in a file named
  `terraform.tf`.

  ```hcl
  terraform {
    required_providers {
      google = {
        source  = "hashicorp/google"
        version = ">= 4.0.0"
      }
    }
  }
  ```

##### Module documentation

- While a module's `README` should provide an at-a-glance reference,
  more extensive documentation is RECOMMENDED for complex modules.
  Authors MAY use tools such as
  [terraform-docs](https://github.com/terraform-docs/terraform-docs) to
  auto-generate module documentation. Otherwise, documentation MAY be
  manually maintained in a `docs/` directory.

##### Refactoring code into modules

- **Terraform doesn't track refactored resources.** If you start with
  several resources in the top-level module and then push them into
  submodules, Terraform will try to recreate all the refactored
  resources on the next `apply`. **Use `moved` blocks when
  refactoring** to mitigate this behavior.

### Testing

- **Before dynamic testing, static analysis of Terraform configuration
  files is RECOMMENDED.** `terraform validate` and `terraform fmt`
  provide a baseline. Linters such as
  [TFLint](https://github.com/terraform-linters/tflint) can enforce
  additional coding standards. Other useful static analysis tools:
  - [Checkov](https://www.checkov.io/) — scans IaC files for
    misconfigurations.
  - [tfsec](https://aquasecurity.github.io/tfsec/v1.20.0/) — checks for
    security issues.

  These tools can help catch common mistakes and enforce best practices
  before the infrastructure is deployed. However, they do not guarantee
  that the configuration is correct or that it will work as intended once
  deployed. That is the purpose of dynamic testing.

- **Dynamic testing requires deployments to pre-production environments
  prior to production.** This is because dynamic testing requires the
  infrastructure to actually exist. A multi-environment deployment
  strategy is REQUIRED to implement dynamic testing of infrastructure
  configuration.

- **A branch-based deployment strategy MAY be used:**
  - Feature branches deploy to ephemeral dev environments.
  - The main branch deploys to a staging environment.
  - Tagged commits deploy to production.

- **Keep pre-production and production environments as similar as
  possible**, to ensure that dynamic tests are valid. Balance this
  against costs by using smaller instance sizes and/or reduced
  redundancy in pre-production. Feature flags can disable non-critical
  (or particularly expensive) infrastructure components in
  pre-production.

- **Deployed infrastructure can be validated using automated
  infrastructure testing tools** such as
  [Terratest](https://terratest.gruntwork.io/),
  [Kitchen-Terraform](https://newcontext-oss.github.io/kitchen-terraform/),
  or [Testinfra](https://testinfra.readthedocs.io/en/latest/). You may
  use a combination. As well as verifying the _existence_ of resources,
  test their _behavior_ — for example, that a web server is running and
  serving expected content, or that a database is accessible from the
  expected IP addresses.

- **Related best practices:**
  - **Staged rollouts** — Deploy changes incrementally. Implement and
    test changes to individual modules or components before making
    wider changes that depend on those components. Deploy network
    layer changes ahead of application layer changes.
  - **Rollback strategy** — Have a rollback strategy in place, using
    version control or previous Terraform state snapshots. Ideally,
    rollbacks should be automated. Failed post-deployment tests or
    monitoring checks should trigger an automatic rollback to the
    previous version.
  - **Blue-green deployments** — For critical infrastructure, run two
    identical production environments (one live, one idle). Deploy the
    new version to the idle environment, then switch traffic once
    deployment is verified via automated tests. This minimizes downtime
    and supports quick rollbacks.
  - **Plan review** — Integrate an execution plan review into your
    workflow, similar to code review for software changes. This can be
    implemented in standard pull request systems (eg. GitHub).
    [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs)
    and [Atlantis](https://www.runatlantis.io/) offer bespoke tooling
    for infrastructure planning and review.
  - **Drift detection** — Regularly run `terraform plan` against
    existing infrastructure to detect configuration drift.
  - **Data isolation** — Use separate accounts or projects in your
    cloud service provider to isolate production data from
    pre-production dummy data. Particularly important for sensitive
    data (PII, financial data).

#### Native testing with `terraform test`

- **Terraform includes a built-in test framework**, invoked with
  [`terraform test`](https://developer.hashicorp.com/terraform/cli/commands/test).
  It runs `.tftest.hcl` files in the `tests/` directory against the
  module in the current working directory, executing real Terraform
  operations (plan, apply, destroy) in isolated, temporary state. This
  complements static analysis — `terraform test` verifies the behavior
  of a configuration, not just its syntax.

- **Test files live in a `tests/` directory alongside the module they
  test**, using the `.tftest.hcl` extension. Each test file declares
  variables, runs the module with a `run` block, and asserts on the
  resulting plan or state.

- **Each `run` block executes a Terraform command** (`plan` or `apply`)
  and makes the plan or state available for `assert` blocks. Multiple
  `run` blocks MAY be combined in a single test file and share state
  within that file.

- **`terraform test` supports
  [mocking](https://developer.hashicorp.com/terraform/language/tests/mocking)**
  of providers and resources, so tests can run without real cloud
  credentials. Mocking is RECOMMENDED for unit-style tests of module
  logic; `apply` runs against a real provider are better suited to
  integration tests.

- **`terraform test` is RECOMMENDED for testing reusable modules** —
  verifying that input variables produce the expected resource
  configuration, catching regressions during refactors, and documenting
  intended behavior through executable examples. For testing the
  behavior of deployed infrastructure, continue to use the dynamic
  testing tools above.

## References

- [TS-59: Terraform (source)](README.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-9: Version Control](../009/AGENTS.md)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-11: Versioning](../011/AGENTS.md)
- [TS-12: Quality Assurance](../012/AGENTS.md)
- [TS-13: Functional Testing](../013/AGENTS.md)
- [TS-49: Cloud Platform Engineering](../049/AGENTS.md)
- [TS-51: Amazon Web Services (AWS)](../051/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [Terraform style guide](https://developer.hashicorp.com/terraform/language/style)
- [Google Cloud — Root module best practices](https://cloud.google.com/docs/terraform/best-practices/root-modules)
- [Gruntwork — Terraform style guide](https://docs.gruntwork.io/guides/style/terraform-style-guide/)
- [TFLint](https://github.com/terraform-linters/tflint)
- [Checkov](https://www.checkov.io/)
- [tfsec](https://aquasecurity.github.io/tfsec/v1.20.0/)
- [Terratest](https://terratest.gruntwork.io/)
- [Kitchen-Terraform](https://newcontext-oss.github.io/kitchen-terraform/)
- [Terragrunt](https://terragrunt.gruntwork.io/)
- [terraform-docs](https://github.com/terraform-docs/terraform-docs)
- [Atlantis](https://www.runatlantis.io/)
- [`terraform test` command reference](https://developer.hashicorp.com/terraform/cli/commands/test)
- [Terraform test files](https://developer.hashicorp.com/terraform/language/tests)
- [HCP Terraform workspace best practices](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/best-practices)
- [Terraform Well-Architected Framework — Enterprise reference architecture](https://developer.hashicorp.com/well-architected-framework/terraform/enterprise-reference-architecture)
