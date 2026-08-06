# TS-2: Software Design Qualities

This is a compact version of technical standard TS-2 for AI agents. Use this to
evaluate software designs and guide architectural decisions.

## Rules

- **Prioritize changeability.** The ultimate objective of software design is to
  ensure the system is changeable—capable of responding to new requirements,
  market shifts, and technical evolution with minimal cost, risk, and disruption.

- **Target MVP for completeness.** Do not aim for absolute completeness up-front.
  Target a minimal viable product (MVP) focusing on a critical subset of
  functionality, then iterate and increment the design based on real user
  feedback.

- **Ensure absolute correctness.** A system MUST reliably perform its functional
  requirements. Actual behaviors MUST match expected behaviors, and all state
  MUST remain valid and consistent, including following error conditions.
  Correctness should generally not be sacrificed for any other quality.

- **Specify non-functional requirements up-front.** Performance, security, and
  regulatory compliance are "architecturally significant" and difficult to
  retrofit. These MUST be clearly specified in acceptance criteria and built
  into the architecture from the start.

- **Design for failure (reliability).** Assume failures will happen. Implement
  explicit recovery logic to ensure fault tolerance and high availability. In
  distributed systems, employ redundancy, replication, caching, retries with
  timeouts, and asynchronous messaging to isolate failures.

- **Treat responsiveness as a first-class concern (experience).** Focus on how
  the software *feels* to the user. Ensure the system provides immediate and
  clear feedback for actions to maintain perceived reliability and user
  confidence.

- **Optimize for habitability.** Design code for human understanding. Maintain
  a habitable codebase through consistent conceptual application, appropriately
  sized abstractions, and regular refactoring to combat entropy.

- **Maintain conceptual integrity (cohesiveness).** Ensure the design forms a
  unified, consistent whole. Limit the vocabulary of languages, infrastructure,
  and design patterns. Use a rigorous, shared domain model to unify the system's
  design.

- **Use simplicity as the foundation.**

  - **Interface simplicity**: Manage essential complexity by exposing only the
    minimum set of concepts and behaviors users genuinely need.

  - **Implementation simplicity**: Minimize accidental complexity by
    prioritizing loose coupling.

  - **Alignment**: Align the interface and implementation through the shared
    domain model to reduce cognitive load.

- **Resolve quality conflicts deliberately, and record them.** The qualities
  mostly reinforce one another, but some pairs pull against each other directly:
  security vs. experience (MFA, session timeouts, rate limits), performance vs.
  simplicity (caching, denormalization), performance vs. portability,
  correctness vs. performance (eventual consistency), completeness vs.
  simplicity.

  Three rules: (1) try to dissolve the conflict before accepting it — many
  apparent trade-offs are artifacts of a particular design; (2) defer to the
  priority order set by the requirements, and escalate rather than silently
  overriding a stated priority; (3) record what was given up, for what, and
  under which constraints — in a design doc.

  A compromise is decided under the constraints of its moment, and those move.
  The reasoning is worth more in the record than the decision is.

## References

- Related: [TS-1: Software Requirements Specification](../001/AGENTS.md), [TS-3: Design Docs](../003/AGENTS.md), [TS-5: Application Architecture](../005/AGENTS.md), [TS-7: Code Design](../007/AGENTS.md)
