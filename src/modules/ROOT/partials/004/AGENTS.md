# TS-4: Modeling

This is a compact version of technical standard TS-4 for AI agents.

Use this when defining architectural views or choosing tools for system
modeling.

## Rules

- **Use the following RECOMMENDED architectural views**, arranged from most
  abstract to most concrete:

  - **Conceptual.** High-level strategic overview of major components and
    interactions; readable by non-technical stakeholders.

  - **Logical.** Functional decomposition and logical information flows,
    abstracting implementation details.

  - **Development.** Static organization of implementation (modules, layers,
    repositories, build artifacts) and their dependencies.

  - **Process.** Runtime structure (processes, threads, services),
    communication, synchronization, and concurrency.

  - **Physical.** Deployment topology mapping software to infrastructure
    (hosts, networks, data stores, devices).

  - **Technical.** Concrete technology stack (languages, runtime environments,
    system software).

  - **Scenarios.** Architecturally significant end-to-end flows used as a
    consistency check to ensure other perspectives agree.

- **Prefer text-to-diagram tools** (eg. PlantUML, Mermaid, Graphviz) over
  graphical drawing tools. Diagrams SHOULD be defined using human-readable
  markup to ensure they are version-controllable and integrate with code review
  workflows.

## References

- Source: [TS-4: Modeling](../../pages/004-modeling.adoc)
- [TS-3: Design Docs](../003/AGENTS.md) applies these modeling perspectives
  as the organizing structure for architectural documentation.
- [TS-54: Threat Modeling](../054/AGENTS.md) covers a related modeling activity
  focused on identifying security and privacy vulnerabilities.
