# TS-49: Cloud Platform Engineering

Broad principles and best practices for cloud platform engineering. Not
specific to any particular cloud service provider — applicable to any
cloud platform.

Platform engineering is a subset of cloud engineering. The focus is on
building **self-service platforms** that enable development teams to
deliver applications and services more efficiently. Platform engineering
creates a standard set of tools, processes, and best practices within an
organization so development teams can build, test, deploy, and manage
their applications themselves, with minimal ops support.

Specific technologies that support cloud platform engineering
(infrastructure-as-code, CI/CD pipelines, monitoring and observability
tools) are covered in other technical standards.

Use this when designing or building self-service internal platforms for
development teams.

Do NOT use this for cloud cost management or the tradeoffs between
dedicated servers and cloud-native architectures — see
[TS-50: Cloud Economics](../050/AGENTS.md). For release mechanics, see
[TS-10: Releasing](../010/AGENTS.md). For application architecture, see
[TS-5: Application Architecture](../005/AGENTS.md). For observability,
see [TS-57: Logging, Monitoring, Observability](../057/AGENTS.md).

## Rules

### Guiding principles

- **Maximize both autonomy and alignment — they are not a trade-off.**
  The overarching goal of platform engineering is to accelerate delivery
  without adding to the workload of development teams. The aim is not a
  midpoint between autonomy and alignment but to maximize both. This is
  the principle of **aligned autonomy**: teams are free to make their own
  decisions, but always within well-defined global constraints, and
  always working in the same direction of travel. Alignment is expressed
  as _context_, not command-and-control — teams are given the context they
  need to make good technical decisions and are then trusted to make
  them.

- **Avoid technology autocracy (too much alignment, too little
  autonomy).** Rigid, iron-clad rules on technology with a small number
  of technical leaders approving every decision results in slow
  delivery. Platform engineering can be misused to enforce this kind of
  autocracy — centrally controlling languages, frameworks, build tools,
  third-party dependencies.

- **Avoid technology anarchy (too much autonomy, too little
  alignment).** The cost of anarchy is the loss of economies of scale. A
  platform that tries to be everything to everyone — supporting too many
  technology stacks — ends up maintaining multiple deployment pipelines,
  testing environments, observability dashboards and alerting
  configurations. The burden surfaces most painfully during large,
  cross-cutting changes.

- **A platform SHOULD NOT attempt to support an unbounded range of
  technology choices.** Some decisions MUST be made centrally, taking
  that responsibility away from individual teams. This is not a
  constraint on autonomy so much as a precondition for it — it frees teams
  to spend time on the product rather than on maintaining bespoke
  delivery infrastructure.

- **Build technical alignment into paved roads.** The way to resolve
  technology anarchy is an opinionated platform that makes the
  well-aligned path the easy path. Teams remain free to make their own
  decisions, but the platform encodes the organization's accumulated
  context so the default choices are also the right ones.

- **Capture leadership guidance in decision records.** To establish
  contextual alignment, ask technology leaders for three things:
  1. Their guidance on technology stack and architecture.
  2. Their expectations about how that guidance will be followed.
  3. The business consequences they anticipate — for the organization as
     a whole — if those expectations are not met.

  This guidance SHOULD be captured in decision records. Platform
  capabilities are then built on the foundation of those records, baking
  the technical alignment directly into the platform.

### Multi-product deployments

- **Use multiple cloud accounts for product isolation.** The RECOMMENDED
  approach for organizations supporting multiple products and services is
  to use multiple accounts with the cloud service provider, one for each
  discrete product. In AWS, the *AWS Organizations* feature allows
  multiple independent AWS accounts to be managed under one root
  organization.

  ```
  Root Organization
  ├── Management Account
  ├── Shared Services Account (networking, DNS, logging)
  ├── Product A - Test Account
  ├── Product A - Prod Account
  ├── Product B - Test Account
  ├── Product B - Prod Account
  └── Security/Audit Account
  ```

- **Use VPCs for a simpler, weaker-isolation alternative.** VPCs under
  the same account provide isolation with easier cross-product
  communication (via VPC peering or transit gateways, with IAM policies
  for access control). But this does not scale as well, isolation is
  weaker, and it is harder to track costs on a per-product basis.

  ```
  Single AWS Account
  ├── Product A VPC
  ├── Product B VPC
  ├── Shared Services VPC
  └── Use tags, IAM policies, and resource naming for separation
  ```

- **A hybrid approach is most common.** Products are isolated at the
  account level, with an additional account that manages centralized
  infrastructure shared by all accounts.

  ```
  Organization
  ├── Shared Infrastructure Account
  │   ├── Shared VPC
  │   ├── Transit Gateway
  │   ├── Route53 Hosted Zones
  │   └── Shared databases/caches
  ├── Product A Account
  └── Product B Account
  ```

### Development and testing environments

- **Use zero-touch ephemeral environments.** Development and testing
  environments SHOULD be zero-touch ephemeral environments — isolated
  environments automatically created and destroyed as needed, without
  manual intervention.

- **Use infrastructure-as-code (IaC) tools.** It is RECOMMENDED to use IaC
  tools to manage these environments. This allows consistent and
  repeatable environment creation on-demand, and rollback is more easily
  automated.

- **Automatically terminate non-production environments outside working
  hours.** Ephemeral environments are cost-effective because they can be
  spun down when no longer needed, so the organization only pays for
  resources actively in use.

- **Non-production environments MUST be close replicas of production.**
  Development and testing environments MUST be close replicas of
  production environments, with essentially the same underlying
  infrastructure and configuration. This ensures issues are more likely
  to be caught early. The only differentiating factors SHOULD be the use
  of dummy data in non-production environments, and pre-production
  environments would typically have fewer resources than production.

## References

- [TS-49: Cloud Platform Engineering (source)](../../pages/049.adoc)
- [TS-5: Application Architecture](../005/AGENTS.md)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-50: Cloud Economics](../050/AGENTS.md)
- [TS-57: Logging, Monitoring, Observability](../057/AGENTS.md)