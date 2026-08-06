# TS-50: Cloud Economics

Financial decision-making for cloud deployments. Addresses how cloud
costs are structured, how to avoid unexpected expenditure, and how to
choose between cloud-native and dedicated server architectures.

Managing costs is a critical aspect of cloud operations. Organizations
need a clear understanding of business-as-usual usage patterns and
associated costs, plus the potential risks of "exploding costs" due to
unexpected changes in throughput, storage, or other resource usage.

Use this when making strategic or architectural decisions about cloud
spending, auto-scaling cost controls, or dedicated-server vs. cloud-native
trade-offs.

Do NOT use this for cloud platform engineering — multi-account strategies
and environment management — see
[TS-49: Cloud Platform Engineering](../049/AGENTS.md). For application
architecture concerns, see [TS-5: Application Architecture](../005/AGENTS.md).
For distributed system design, see
[TS-6: Distributed System Design](../006/AGENTS.md). For caching and
distributed data, see [TS-46: Distributed Data and Caching](../046/AGENTS.md).

## Rules

### Auto-scaling surge costs

- **The greater the auto-scaling, the greater the risk of unexpected
  costs.** Platform-as-a-Service (PaaS) solutions, which tend to have
  uncapped auto-scaling by default, are particularly vulnerable. Costs
  can explode from seemingly negligible charges — for example, $0.023
  per GB per month for hot storage becomes $115k/month at 10M users × 100
  images × 5MB (= 5PB).

- **Set limits on auto-scaling.** Set concurrency limits (eg. for AWS
  Lambda) or instance limits (eg. for EC2 auto-scaling groups). Accept
  that some users may experience service unavailability during peak
  times, and communicate these limitations transparently (eg. via SLAs
  and status pages).

  This is a quality trade-off, not just a configuration value. The cap MUST
  be set consistently with any specified availability threshold; a cap that
  cannot be reconciled with it is a requirements problem to escalate, not a
  value to tune. See [TS-1: Software Requirements Specification](../001/AGENTS.md)
  for specifying and costing availability, and
  [TS-2: Software Design Qualities](../002/AGENTS.md) for resolving the
  availability-vs-cost conflict.

- **Match revenue-per-user to costs-per-user before fully opening up
  auto-scaling.** Do not enable auto-scaling until you have set up a
  paywall, subscription model, or other monetization strategy that
  scales with usage. Prioritize availability for paying customers over
  free-tier users.

- **Use inexpensive storage tiers.** Archive or delete data that no
  longer needs to be retained in a user-facing storage system.

- **Use caching and compression for frequently-accessed data.** Caching
  layers reduce the number of requests to the underlying storage system.
  Implement compression on both data-at-rest and data-in-transit wherever
  possible.

- **Avoid excessive logging, especially in production.** Use feature
  flags to dynamically restrict logging to only the most important
  events. Consider request sampling in tracing systems.

- **Prepare for denial-of-service (DoS and DDoS) attacks.** Use services
  such as Azure Front Door, AWS Shield, or Cloudflare.

### Dedicated servers vs. cloud-native architectures

- **Do not reach for distributed, cloud-native architecture before it is
  actually needed.** Cloud-native architectures carry a significant
  baseline cost premium over running equivalent workloads on dedicated
  servers — typically 5–30x compared to renting a dedicated server from a
  hosting provider. Serverless compute (eg. AWS Lambda) is approximately
  5–6x more expensive than an equivalent large cloud VM instance, and
  approximately 25x more expensive than an equivalent dedicated server
  from a budget hosting provider. These premiums exist because cloud
  providers build in spare capacity to handle peak loads, and that cost
  is passed on.

- **The burstier the workload, the more justified cloud-native
  architecture becomes.** If a workload is highly unpredictable — long
  periods of idleness punctuated by sudden large surges — serverless or
  auto-scaling architectures can be cost-effective, since you only pay
  for what you use. For workloads with relatively steady, predictable
  traffic, paying the cloud premium provides little benefit. Heuristic:
  if a dedicated server would be kept above approximately 5% utilization
  almost all the time, it will likely be cheaper than equivalent
  serverless compute.

- **Prefer vertical scaling before horizontal scaling or cloud-native
  distributed architectures.** Organizations SHOULD consider vertical
  scaling (moving to a larger server) before adopting horizontal scaling
  or cloud-native distributed architectures. It is RECOMMENDED to scale
  vertically first, then horizontally.

- **Use a small number of large servers rather than a large fleet of
  small machines.** When horizontal scaling becomes necessary, a small
  number of large servers will generally be more efficient, because
  there is a non-trivial coordination overhead associated with each node
  in a cluster.

- **Most web services fit on a single large server.** Modern servers are
  substantially more powerful than when distributed computing patterns
  became fashionable in the early 2010s. For most web services with under
  10,000 queries per second (QPS), a single large server is sufficient.

- **Mitigate the availability drawback of single-server architecture
  with redundancy.** The main drawback of single-server architecture
  compared to cloud-native is availability. To mitigate, it is
  RECOMMENDED to run a primary and a backup server in separate
  datacenters or cloud regions. For higher redundancy, a 2x2
  configuration (two servers in a primary datacenter, two in a secondary)
  is sufficient for most services.

- **Avoid correlated hardware failures.** Primary and backup servers
  SHOULD use hardware from different manufacturing batches, and ideally
  from different models or vendors. This is especially important for
  storage devices.

- **Cost savings is unlikely to be a justification for cloud-native
  architecture.** Unless traffic patterns are really bursty, the
  economic justifications for investing in auto-scaling will be, at
  best, weak. There may be other rational justifications for adopting
  cloud-native architecture (fault tolerance, managed security patching,
  DDoS protection, data replication), but cost savings is unlikely to be
  one of them.

## References

- [TS-50: Cloud Economics (source)](README.adoc)
- [TS-1: Software Requirements Specification](../001/AGENTS.md)
- [TS-2: Software Design Qualities](../002/AGENTS.md)
- [TS-5: Application Architecture](../005/AGENTS.md)
- [TS-6: Distributed System Design](../006/AGENTS.md)
- [TS-46: Distributed Data and Caching](../046/AGENTS.md)
- [TS-49: Cloud Platform Engineering](../049/AGENTS.md)
- [Use One Big Server (Nima Badizadegan)](https://specbranch.com/posts/one-big-server/)