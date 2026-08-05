# TS-49 gap analysis

Gaps found comparing TS-49: Cloud Platform Engineering against the following
reference resources (collected from GitHub issue
<https://github.com/kieranpotts/standards/issues/69>):

- https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/defining-needs-and-use-cases.html
- https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html
- https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-tagging
- https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview

**Assessment.** Most of the reference material falls inside TS-49's stated
scope, but is largely missing. The references cluster around three topics the
standard does not substantively address: resource tagging strategy, resource
naming conventions, and multitenancy/tenancy models. The standard mentions
"tags, IAM policies, and resource naming for separation" only in passing
(`src/049/01-multi-product-deployments.adoc:37`). Concrete per-vendor details
(specific Azure resource-type abbreviations, AWS system tag keys, vendor
tooling) are out-of-scope for a provider-agnostic standard, but the general
strategies and principles behind them are in-scope and almost entirely absent.
The multitenancy overview is SaaS-product-focused and mostly out-of-scope, but
its enterprise-shared-platform framing overlaps with the standard's
multi-product isolation content.

**Status:** Initial run, 2026-08-05. All gaps open.

## Missing

- [ ] [https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/defining-needs-and-use-cases.html]
      A tagging strategy should start by engaging the stakeholders who consume
      metadata (finance, governance/compliance, operations/development,
      security) and working backwards from their use cases via a
      cross-functional workshop. TS-49 does not address defining a tagging
      strategy at all. Recommend a new section (e.g. a new
      `03-resource-tagging.adoc`).

- [ ] [https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/defining-needs-and-use-cases.html]
      A tagging strategy must document which use cases it addresses, who is
      responsible for tagging resources, how tags are enforced (proactive vs
      reactive), how effectiveness is measured, how often the strategy is
      reviewed, and who drives improvements. TS-49 has none of this. Recommend
      the new section proposed above.

- [ ] [https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html]
      A tagging strategy must distinguish mandatory tags (every resource has
      them) from discretionary tags (defined by the strategy, applied only
      where needed), and define detection/enforcement mechanisms for
      mandatory tags. TS-49 does not address mandatory vs discretionary tags.
      Recommend the new section proposed above.

- [ ] [https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html]
      Recommended mandatory tag categories include owner, business unit,
      SDLC stage (production vs non-production), cost center, and financial
      owner; recommended discretionary categories include workload
      ID/name, compliance requirement, environment version, workload tier,
      backup, SLA level, and lifespan. TS-49 gives no recommended tag set.
      Recommend the new section proposed above.

- [ ] [https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html]
      In a multi-account environment, every account should have mandatory tags
      identifying the account's purpose and who is responsible for its
      resources. TS-49's multi-account guidance
      (`src/049/01-multi-product-deployments.adoc:1-58`) does not mention
      tagging accounts. Recommend placing at
      `src/049/01-multi-product-deployments.adoc:58` or in the new tagging
      section.

- [ ] [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tagging-governance]
      Tagging governance has two complementary modes: reactive (find
      non-compliant resources after creation, via APIs/rules/Tag Editor) and
      proactive (enforce tags at creation via IaC, service catalog, tag
      policies, IAM conditions). TS-49 does not address tagging governance.
      Recommend the new section proposed above.

- [ ] [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tags-for-cost-allocation]
      [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tags-for-automation]
      [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tags-for-access-control]
      [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tags-for-resource-organization]
      Tags serve four primary purposes — cost allocation, automation
      (e.g. opt-in/opt-out of start/stop schedules, snapshot lifecycle),
      access control (tag-based IAM conditions), and resource organization
      (grouping/filtering). TS-49 mentions tags only for "separation"
      (`src/049/01-multi-product-deployments.adoc:37`) and does not enumerate
      these use cases. Recommend the new section proposed above.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-tagging#use-foundational-tagging-categories]
      A foundational tagging schema should group tags into categories —
      functional (app, tier, environment, region), classification
      (criticality, confidentiality, SLA), accounting (department, cost
      center, budget), purpose (business process, business impact), and
      ownership (business unit, ops team). TS-49 has no tag taxonomy.
      Recommend the new section proposed above.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-tagging#implement-consistent-tagging]
      The same core tagging schema must be used for all resources across all
      regions to maintain governance, simplify automation, and avoid
      reporting inaccuracy. TS-49 has no consistency requirement for tags.
      Recommend the new section proposed above.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming#understand-resource-names-in-azure]
      A resource naming convention must respect each resource type's own
      rules for length, character set, and uniqueness scope, and should
      include only information that remains constant (most resource names
      cannot be changed after creation; put mutable attributes in tags
      instead). TS-49 does not address naming conventions. Recommend a new
      section (e.g. a new `04-resource-naming.adoc`).

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming#choose-naming-components]
      Useful naming components include a resource-type abbreviation, the
      workload/application, the environment, the region, and an instance
      number; the convention must standardize the order of these components.
      TS-49 gives no naming component guidance. Recommend the new section
      proposed above.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming#understand-azure-name-scope]
      Resource names must be unique within a defined scope (global,
      resource-group, or resource) that varies by resource type; globally
      scoped (typically PaaS) names form part of the public DNS name. TS-49
      does not address name uniqueness scopes. Recommend the new section
      proposed above.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming#develop-your-naming-convention]
      A hyphen delimiter improves readability and is recommended even though
      not every resource supports delimiters; for absolute cross-resource
      consistency, omit the hyphen. TS-49 gives no delimiter guidance. Recommend
      the new section proposed above.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming#example-azure-resource-names]
      Subscription and management-group/account identifiers should follow
      descriptive patterns (e.g. `(Business Unit) (Function) (Environment)`
      for subscriptions) and can be changed after creation. TS-49's
      multi-account guidance
      (`src/049/01-multi-product-deployments.adoc:1-58`) does not address
      naming the accounts/organizations themselves. Recommend placing at
      `src/049/01-multi-product-deployments.adoc:58` or in the new naming
      section.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-tagging#why-use-azure-resource-tags]
      A tagging strategy should build on and complement the naming
      convention, and the naming convention should be defined before the
      tagging strategy. TS-49 treats neither, and does not relate the two.
      Recommend the new naming and tagging sections, with this relationship
      stated explicitly.

## Partial

- [ ] [https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview#scope]
      covers enterprise-wide shared platform solutions (e.g. a shared
      Kubernetes cluster used by multiple business units) as a form of
      multitenancy — `src/049/01-multi-product-deployments.adoc:1-58`
      addresses multi-product isolation (multiple accounts vs VPCs) but does
      not frame it as a tenancy model or discuss the spectrum of isolation
      approaches (fully isolated per tenant, shared with per-tenant data,
      fully shared). The reference's overview page itself does not detail
      the models; the detail lives in the linked sub-page
      <https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models>,
      which was not fetched in this run.

- [ ] [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tags-for-automation]
      describes using tags to drive automated start/stop of non-production
      environments outside working hours —
      `src/049/02-development-and-testing-environments.adoc:14` recommends
      automatically terminating non-production environments outside working
      hours but does not mention tagging as the mechanism for selecting which
      resources to target. Recommend placing at
      `src/049/02-development-and-testing-environments.adoc:14`.

## Out-of-scope

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations]
      provides recommended per-resource-type abbreviations for every Azure
      resource (e.g. `srch` for AI Search, `vnet` for virtual networks,
      `sqldb` for SQL databases). Flagged for the user to confirm or
      overrule — TS-49 is explicitly provider-agnostic, so a per-resource
      abbreviation catalog for one vendor plausibly sits outside its stated
      purpose. The general principle ("use a resource-type abbreviation as a
      naming component") is captured above as a missing gap.

- [ ] [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tag-naming-best-practices]
      documents AWS system tags (`aws:ec2spot:fleet-request-id`,
      `aws:cloudformation:stack-name`, `elasticbeanstalk:environment-name`)
      and the reserved `aws:` prefix. Flagged — TS-49 is provider-agnostic,
      so AWS-internal tag namespaces plausibly sit outside its scope. The
      general tag-naming conventions (lowercase, hyphens, organization prefix)
      are provider-agnostic and captured below as out-of-scope-adjacent; see
      the next item.

- [ ] [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tag-naming-limits-and-requirements]
      documents AWS-specific tag limits (50 user tags per resource, 128-char
      keys, 256-char values, `aws:` reserved prefix, allowed character set
      varying by service). Flagged — TS-49 is provider-agnostic, so
      vendor-specific limits plausibly sit outside its scope. The general
      principle ("decide a capitalization strategy and apply it consistently")
      is provider-agnostic but is implicitly covered by the consistency gap
      above.

- [ ] [https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tagging-governance]
      names specific AWS enforcement tooling (Tag Editor, Resource Groups
      Tagging API, AWS Config Rules, CloudFormation `Resource Tags`,
      Service Catalog, AWS Organizations tag policies). Flagged — TS-49 is
      provider-agnostic; specific AWS tooling plausibly sits outside its
      scope. The general proactive/reactive governance principle is captured
      above as a missing gap.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-tagging#implement-consistent-tagging]
      names Azure Policy (built-in/custom definitions, resource selectors)
      as the enforcement mechanism for tagging. Flagged — TS-49 is
      provider-agnostic; Azure-specific tooling plausibly sits outside its
      scope. The general consistency requirement is captured above as a
      missing gap.

- [ ] [https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview]
      is primarily about designing and building multitenant SaaS solutions
      (B2B/B2C products) for external customers on Azure. Flagged — TS-49 is
      about internal self-service platform engineering, so SaaS-product
      multitenancy plausibly sits outside its stated purpose. The
      enterprise-shared-platform overlap is captured above as a partial gap.

- [ ] [https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview#whats-in-this-series]
      lists Azure-service-specific multitenancy guidance (compute,
      networking, storage, data, messaging, identity, AI/ML, IoT) and a
      multitenant-solution design checklist. Flagged — these are SaaS-on-
      Azure service-by-service recommendations, plausibly outside a
      provider-agnostic internal-platform-engineering standard.

- [ ] [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming#example-azure-resource-names]
      gives per-resource-type example name patterns for ~30 Azure resource
      types (e.g. `srch-<workload>-<environment>`, `vnet-<subscription
      purpose>-<region>-<###>`). Flagged — provider- and resource-specific
      patterns plausibly sit outside a provider-agnostic standard. The
      general naming-component principle is captured above as a missing gap.

## Unresolved

- [ ] The Azure multitenant overview links to a sub-page,
      <https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models>,
      that almost certainly contains the actual tenancy-model detail relevant
      to the partial gap above. It was not fetched in this run because it was
      not in the issue's URL list; re-running with it included would let the
      partial gap be resolved more precisely.