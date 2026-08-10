# TS-51: Amazon Web Services (AWS)

Best practices for using AWS services.

Use this when designing, provisioning, or governing AWS resources. The
guidance is AWS-specific but many of the principles (naming conventions,
tagging strategy, environment isolation, IAM discipline) transfer to
other cloud providers.

Do NOT use this for cloud platform engineering in general — multi-account
strategies and self-service platforms — see
[TS-49: Cloud Platform Engineering](../049/AGENTS.md). For cloud economics
and dedicated-vs-cloud-native trade-offs, see
[TS-50: Cloud Economics](../050/AGENTS.md). For security and secrets
management, see [TS-52: Security and Secrets Management](../052/AGENTS.md).
For privacy and data protection, see
[TS-53: Privacy and Data Protection](../053/AGENTS.md). For release
mechanics, see [TS-10: Releasing](../010/AGENTS.md).

## Rules

### Identity and access management

- **Do not use the root user for everyday tasks.** Every AWS account has a
  root user with full access to all AWS services and resources. It is
  strongly RECOMMENDED that you do not use the root user for everyday
  tasks. Instead:
  - Create an administrative IAM user with the `AdministratorAccess`
    policy and use it to administer the account.
  - For the root user, set a very strong password and enable MFA.
  - The root user SHOULD NOT have any access keys, restricting root
    access to the web console only.
  - Set alerts for root user activity.
  - Enable IAM user and role access to billing information (via Billing
    and Cost Management) so costs can be managed by a non-root user.
  - All other AWS activities SHOULD be undertaken by non-root users.
    Only a few use cases require root (closing the account, changing the
    primary email address).

- **Prefer IAM Identity Center over plain IAM for identity management.**
  AWS *Identity and Access Management (IAM)* creates users, groups,
  roles, and policies. *IAM Identity Center* (formerly AWS Single
  Sign-On / SSO) serves the broader purpose of managing all user
  identities from a single, centralized service. AWS recommends using
  IAM Identity Center to manage all user identities. It supports
  multiple identity sources (IAM itself, or external IdPs via SAML 2.0
  such as Active Directory, Azure AD, Okta) and built-in SSO integrations
  with many business SaaS applications. IAM Identity Center integrates
  with *AWS Organizations*.

- **Use AWS Organizations for multi-account management.** It is a common
  pattern in large organizations to have multiple AWS accounts managed
  under one organization, allowing delegation of resource and permission
  control to separate business units or product divisions. Create a
  *Management Account* at the root of the account hierarchy, then create
  or invite additional accounts into the organization. Even for a simple
  organization with a single product, building infrastructure under a
  sub-account lets you more easily scale to new products while keeping
  cloud infrastructure clearly delimited by product.

- **Attach IAM policies to groups, not directly to users.** IAM policies
  MAY be attached directly to IAM users, but it is RECOMMENDED to attach
  them to groups instead. This makes it much easier to manage permissions
  across multiple users — especially important for large organizations
  where managing individual user permissions becomes impractical.

### Resource naming conventions

- **Resource names MUST follow a consistent format.** A standardized
  naming convention helps identify, sort, and filter resources and
  quickly identify characteristics such as owner, deployment environment,
  location, and the associated software component or workload. It is a
  prerequisite for cloud governance and policy enforcement automation —
  resource names need to be machine-parsable, with a consistent global
  schema shared by all resources across all your AWS accounts.

- **Identify the key pieces of information to embed in resource names.**
  Categories to consider:
  - **Account** — name of the AWS account that owns the resource.
  - **Business unit** — department that owns the workload.
  - **Workload, application, or project** — how the resource fits into
    the overall architecture.
  - **Environment** — stage of the development lifecycle.
  - **Resource type** — the type of cloud resource or asset.
  - **Region, location, or scope** — region into which the resource is
    deployed, or parent resource (eg. VPC) if not a global resource.
  - **Instance** — instance count for replicable resources (`001`,
    `002`, etc.).

  Information not embedded in resource names can be captured in
  metadata (tags). Embed only information that is most useful for
  identifying the _purpose_ of a resource.

- **List the most helpful components first.** The components most
  helpful in identifying the purpose of a resource SHOULD be listed
  first in the name.

- **Resource naming conventions SHOULD be agnostic to the cloud
  provider.** This allows the same naming convention across all cloud
  providers and on-premises resources. Some variation may be necessary
  due to provider-specific constraints.

- **Keep resource names short and simple.** Use only lowercase ASCII
  letters and numbers for individual components. Avoid special
  characters, including underscores and periods. For delimiters, it is
  RECOMMENDED to use single hyphens (`-`) for the widest compatibility
  with all cloud providers and resource types. Hyphens SHOULD NOT appear
  in the resource name components themselves (use `webserver` not
  `web-server`).

- **Use a global naming schema as the starting point:**

  ```
  {organization}-{account}-{project}-{description}-{environment}-{resource}-{location}-{instance}-{suffix}
  ```

  | Component | Description | Required | Constraints |
  |---|---|---|---|
  | `{organization}` | Global identifier for the parent organization | RECOMMENDED | `[a-z][a-z0-9]{2,7}` |
  | `{account}` | Account identifier | REQUIRED for multi-account orgs | `[a-z][a-z0-9]{3,4}` |
  | `{project}` | Project name | REQUIRED unless account serves this purpose | `[a-z0-9]{4-12}` |
  | `{module}` | Software module or component name | OPTIONAL | `[a-z0-9]{1,20}` |
  | `{environment}` | Deployment environment | REQUIRED only for environment-specific resources | `[a-z]{3,4}` from enum |
  | `{resource}` | Resource type | REQUIRED | `[a-z]{3,4}` from enum, or CSP-specific name |
  | `{location}` | Region | OPTIONAL | Matches CSP region name + AZ |
  | `{instance}` | Instance count | OPTIONAL | `[0-9]{3}` |
  | `{suffix}` | Random hash or account ID | OPTIONAL | `[a-z0-9]{7}` or account ID |

- **Use a consistent `{organization}` identifier across all resources.**
  It is RECOMMENDED to use a registered business name or unique
  trademark, to make resource names as unique as possible across AWS.
  This mitigates conflicts when environments merge (business acquisitions,
  managed service provider engagements, etc.).

- **The `{account}` component is REQUIRED for multi-account AWS
  organizations.** It MAY be dropped for singular AWS accounts, or used
  to identify the business unit or product department when multiple
  departments share the same account. Use short abbreviations such as
  `fin`, `mktg`, `prd`, `it`, `corp`.

- **The `{project}` component MUST be included** unless `{account}`
  fulfills an equivalent purpose (one account per project). A "project"
  may reference components/subdomains within a software system, or
  identify a workload, application, team, or general usage.

- **For `{environment}`, use a common set of abbreviations** such as
  `prod`, `dev`, `qa`, `stage`, `test`. Not applicable to all resource
  types; can be dropped where other components identify the target
  environment.

- **For `{resource}`, use a custom enum of generic resource types**
  (`vpc`, `vm` for EC2, `fn` for Lambda, `cntr`, `rdb`, `obj`, etc.) or
  match the cloud provider's naming convention (the third component of
  the ARN for AWS: `ec2`, `rds`, `s3`, `lambda`, `iam`, etc.).

- **For `{location}`, use region names matching the cloud provider's
  convention, minus hyphens** (`us-east-1` → `useast1`). This MAY be
  combined with an AZ suffix (`useast1a`). For global resources such as
  S3 buckets, use an abbreviation like `gbl` or `g` or drop the
  component.

- **Use `{instance}` to identify replicated resources** (`001`, `002`,
  etc.) and `{suffix}` as a random hash where uniqueness is required. For
  global resources like S3 buckets, using your AWS account ID as the
  suffix increases the chance of a globally-unique name.

- **Define resource-specific subsets of the global schema.** Deviate
  where additional information is needed. Some AWS resource types have
  unique conventions (eg. IAM resources generally use `PascalCase`).
  Greater variability in naming increases the difficulty of
  implementing automation and governance.

  Examples of AWS resource-specific naming conventions:

  | Resource type | Schema | Example |
  |---|---|---|
  | VPCs | `{org}-{project}-{module}-{env}-vpc-{region}` | `hackscorp-arundel-authapi-prod-vpc-useast1` |
  | Subnets | `{org}-{project}-{module}-{env}-vpc-{region}-subnet-{scope}` | `hackscorp-arundel-authapi-prod-vpc-useast1-subnet-public` |
  | Route tables | `{org}-{project}-{module}-{env}-vpc-{region}-rt-{scope}` | `hackscorp-arundel-authapi-prod-vpc-useast1-rt-public` |
  | NAT gateways | `{org}-{project}-{module}-{env}-vpc-{region}-nat` | `hackscorp-arundel-authapi-prod-vpc-useast1-nat` |
  | NACLs | `{org}-{project}-{module}-{env}-vpc-{region}-nacl` | `hackscorp-arundel-authapi-prod-vpc-useast1-nacl` |
  | EC2 instances | `{org}-{project}-{module}-{env}-vm-{location}-{instance}` | `hackscorp-arundel-authapi-prod-vm-useast1-001` |
  | Load balancers | `{org}-{project}-{module}-{env}-lb-{location}-{instance}` | `hackscorp-arundel-authapi-prod-lb-useast1-001` |
  | Auto-scaling groups | `{org}-{project}-{module}-{env}-asg-{location}` | `hackscorp-arundel-authapi-prod-asg-useast1` |
  | Security Groups | `{org}-{project}-sg-{description}` | `hackscorp-arundel-sg-public` |
  | IAM roles (EC2) | `{org}-{project}-{module}-{env}-role` | `hackscorp-arundel-authapi-prod-role` |
  | RDS instances | `{org}-{project}-{module}-{env}-rdb-{engine}-{master\|slave}-{location}-{instance}` | `hackscorp-arundel-authapi-prod-rdb-mysql-slave-useast1-001` |
  | Lambda functions | `{org}-{project}-{module}-{env}-fn` | `hackscorp-arundel-reportbatch-prod-fn` |
  | S3 buckets | `{org}-{project}-{module}-{env}-obj-{accountid}` | `hackscorp-arundel-logos-prod-obj-123456789012` |

### Resource tagging strategy

- **Use tags for supplementary metadata not embedded in resource
  names.** A good tagging strategy complements a naming convention and
  improves governance and management of AWS resources. Tags are used
  for billing/cost allocation, filtering resources in automation,
  tag-based IAM policy conditions, and Resource Groups views in the
  AWS Management Console.

- **Tag consistency matters more than tag definition.** If a portion of
  resources are missing tags for cost allocation, cost analysis becomes
  more time consuming and/or less accurate. If you are missing tags to
  identify resources that contain sensitive data, you may need to
  assume all resources contain sensitive data — increasing your costs.
  The _management_ of tags — how you enforce and audit their use — is
  arguably more important than how you _define_ them.

- **Identify stakeholders and assign tag owners.** Stakeholders who may
  need to manage tags include cloud administrators, software developers
  / application owners, infosec, finance, and legal/compliance. Each
  group is responsible for managing different groups of tags, by use
  case. Tag owners have the responsibility to articulate the value
  proposition of the tags they manage.

- **Identify use cases for tags.** Use cases vary by organization. Have
  different groups of tags for different use cases. Common use cases:
  - **Resource management** — grouping resources in the AWS Management
    Console (by project, application, team, department).
  - **Cost allocation** — breaking down costs for analysis and
    reporting.
  - **Compliance** — identifying resources that store PII or other
    sensitive data.
  - **Automation** — driving automated processes (patching, backup and
    restore, monitoring, job scheduling, disaster recovery).

  Be aware that monthly cost allocation reports are calculated based on
  the tags assigned to resources over the whole reporting period. Cost
  allocation reports are not recalculated when cost allocation tags are
  changed; new cost allocation tags apply only from the point in time
  they are applied.

- **Identify required, conditionally-required, and optional tags.**
  Conditionally-required tags are only mandatory under certain
  circumstances (eg. if an application processes sensitive data, you may
  require a data-classification tag). Focus on required and
  conditionally-required tags. Start with a small set of known-needed
  tags and create new tags as new needs emerge — preferable to
  specifying an exhaustive list at the outset.

- **Use a consistent prefix in tag names that identifies your business
  and account.** This distinguishes your tag schema from AWS's built-in
  tags and reduces the risks associated with merged AWS accounts.
  AWS-defined tags use lowercase ASCII letters, hyphen-separated words,
  and colon-delimited prefixes (eg. `aws:cloudformation:stack-name`,
  `aws:ec2spot:fleet-request-id`, `lambda-console:blueprint`). A simple
  starter template:

  ```
  {organization}:{key}:{value}
  ```

  Example use cases:

  | Use case | Tag schema | Description | Example values |
  |---|---|---|---|
  | Data classification | `hackscorp:data:{classification}` | Infosec-defined data classifications | `sensitive`, `confidential`, `personal` |
  | Environments | `hackscorp:env:{environment}` | Tag resources as belonging to a specific environment | `development`, `staging`, `qa`, `production` |
  | Disaster recovery | `hackscorp:dr:rpo` | Define the recovery point objective (RPO) | `6h`, `24h` |
  | Cost allocation | `hackscorp:fin:{cost-allocation}` | Finance teams implement cost reporting on each team's usage | `corporate`, `recruitment`, `support`, `engineering` |

- **Tags are case-sensitive.** In AWS, `costCenter` and `costcenter`
  are treated as different tag keys. American English SHOULD be used
  for consistent spelling (eg. "center", not "centre").

### Environment isolation

- **Isolate resources by environment.** This is particularly important
  for security and compliance. It stops production data leaking into
  pre-production environments, and vice versa — it stops dummy data from
  contaminating production environments. It also helps reduce the risk of
  accidental changes to production services, and supports strategies
  such as blue-green deployments.

- **Two common approaches: separate AWS accounts, or separate VPCs
  within the same account.** Using separate AWS accounts under a single
  AWS Organization is probably the simplest solution — create a separate
  account for each environment (`dev`, `staging`, `prod`), each managed
  independently with its own IAM users, roles, and policies. Risks of
  cross-environment contamination are minimized. Alternatively, scope
  each AWS account to a particular project or business unit and use
  separate VPCs within the same account to isolate environments — more
  involving to set up but affords more flexibility (eg. easier to share
  resources between environments, such as a centralized logging system).

- **Create distinct IAM roles for production and pre-production within a
  product account.** It is RECOMMENDED to create distinct IAM roles
  within a product account for production and pre-production
  environments and workloads. Use tags to identify the environment of
  each resource, and use IAM policies to restrict access based on those
  environment tags. This ensures both users and services/resources can
  access resources only in their designated environment.

- **Deploy production and pre-production in completely separate VPCs,
  with no peering connections.** This creates a hard network boundary
  between the environments.

- **Use environment-specific resources and secrets.** Use private subnets
  for data storage and processing, with environment-specific NAT
  gateways and routing tables. Use completely separate RDS instances,
  DynamoDB tables, and S3 buckets for each environment. Use different
  KMS keys for each environment to ensure encrypted data cannot be
  decrypted in another environment in the event it does accidentally
  leak. Use different parameter paths (`/prod/`, `/test/`) in Systems
  Manager Parameter Store, and separate secrets in AWS Secrets Manager.

- **Use different Terraform state files for each environment** when
  building infrastructure from code, stored in separate S3 buckets with
  different access policies.

### Virtual Private Clouds (VPCs)

- **Choose VPC CIDR blocks from RFC 1918 private IP address ranges:**
  - `10.0.0.0/8` (`10.0.0.0` - `10.255.255.255`)
  - `172.16.0.0/12` (`172.16.0.0` - `172.31.255.255`)
  - `192.168.0.0/16` (`192.168.0.0` - `192.168.255.255`)

  These are reserved for private networks and not routable on the public
  internet. The allowed size for a VPC CIDR block is between `/16`
  (65,536 IP addresses) and `/28` (16 IP addresses).

- **Avoid `172.17.0.0/16`.** Some AWS services (Cloud9, SageMaker AI)
  use this CIDR range. Avoiding it prevents IP address conflicts with
  these services.

- **Subnets MUST NOT have overlapping IP ranges within the same VPC.**
  Subnets should have smaller CIDR ranges than their VPC. A common
  practice is to use a `/16` CIDR block for the VPC (eg. `10.0.0.0/16`)
  and create subnets with smaller blocks like `/24` or `/28` (eg.
  `10.0.1.0/24` for web servers, `10.0.2.0/24` for application servers,
  `10.0.3.0/24` for database servers — about 200 possible private IPs
  per subnet).

- **Standardize subnet sizing by subnet type.** Use the subnet
  allocation feature in a multi-VPC architecture to mandate a smaller
  CIDR size (eg. `/27`) for public subnets and a larger CIDR size (eg.
  `/24`) for private subnets.

- **Plan IP addressing for future growth.** Plan each subnet to have
  enough addresses not only for resources you intend to deploy
  immediately, but also to allow room for future growth. Keep in mind
  that the first four IP addresses and the last IP address in each
  subnet CIDR block are not available for your use and cannot be
  assigned to a resource.

## References

- [TS-51: Amazon Web Services (AWS) (source)](../../pages/051-amazon-web-services-aws.adoc)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-49: Cloud Platform Engineering](../049/AGENTS.md)
- [TS-50: Cloud Economics](../050/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [AWS tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)
- [Microsoft Cloud Adoption Framework: resource naming](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)
- [Stepan Stipl's cloud naming convention](https://stepan.wtf/cloud-naming-convention/)
- [Anthony Wat's AWS naming scheme](https://blog.avangards.io/my-quest-to-finding-the-perfect-aws-resource-naming-scheme)
- [Terraform null-label module](https://registry.terraform.io/modules/cloudposse/label/null/latest)