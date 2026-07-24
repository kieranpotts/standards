# TS-61: AI Tools

Best practices for using AI tools to support software development
workflows — specifically, the generation of computer program code,
software architectural designs, and technical documentation.

Use this when designing, implementing, reviewing, or governing AI-assisted
or agentic software development workflows, or when authoring reusable
agent context (AGENTS.md files, agent skills).

## Rules

### Model choice

- **Match the model tier to the task.** Identify the dominant capability a
  task demands, then choose the cheapest tier and capability type that
  satisfies it.

  - **Frontier** models (Claude Opus, GPT flagship, Gemini Pro) are the
    state of the art — most capable, slowest, most expensive. SHOULD be
    reserved for work where their capability changes the outcome:
    planning, architecture, complex problem-solving, security analysis.

  - **Mid-tier** models (Claude Sonnet, GPT mid-tier, Llama 70B, Qwen)
    balance capability, speed, and cost. RECOMMENDED for most day-to-day
    tasks, including a large share of coding work.

  - **Light** models (Claude Haiku, Gemini Flash, GPT mini) trade
    capability for speed and cost. RECOMMENDED for high-volume,
    latency-sensitive, or mechanical work — classification, extraction,
    routing, simple lookups.

  - **Reasoning** models spend extra compute on an internal chain-of-
    thought before answering, at the cost of latency and token spend.
    RECOMMENDED for problems with a verifiable chain of logic: maths,
    planning, multi-step analysis, complex debugging.

  - **Specialist** models are fine-tuned for a narrow domain, eg. a
    search-grounded model for factual retrieval with citations, or a
    code-completion model for IDE autocomplete. RECOMMENDED over general-purpose
    models where the task matches the model's specialization.

  - **Open-weight** are RECOMMENDED for privacy-sensitive or offline work,
    and for high-volume tasks where local hardware is adequate.

- **Public benchmarks are a first filter, not a substitute** for
  evaluating candidate models on your own representative tasks.

- **No model reliably beats a deterministic tool at exact computation.**
  For exact multi-step computation (arithmetic on large numbers,
  tracing algorithm execution), the right choice is a script or code
  interpreter, not a model.

## Inference parameters

- **Reach for inference-time parameters only for a specific failure mode**
  they address: output too random or repetitive, responses truncated,
  reasoning too shallow or too slow).

- **Match temperature to the task.** Temperature controls the randomness
  of token selection. Higher temperature samples less-probable tokens,
  trading coherence for diversity.

  - **Low (0–0.3):** Focused, near-deterministic. Code generation, data
    extraction, classification, structured output, factual answers.

  - **Medium (0.4–0.7):** Balanced. General conversation, drafting,
    summarization.

  - **High (0.8+):** Varied, exploratory. Creative writing, brainstorming,
    generating diverse options.

- **Tune temperature _or_ top-p, but not both at once.** Their
  interaction is hard to reason about. Top-p (nucleus sampling) restricts
  sampling to the smallest set of tokens whose cumulative probability
  meets threshold _p_; top-k caps the candidate set at the _k_ most
  likely tokens.

- **Scale reasoning to the task, not defaulted to maximum.** Reasoning
  models expose two dials: *thinking* (whether and when the model
  produces an internal chain of thought before answering) and *effort*
  (how hard it works overall — exploration, tool calls, self-verification).

  - Turn reasoning *up* for problems with a verifiable chain of logic —
    maths, planning, multi-step analysis, complex code, debugging — and
    for long-horizon agentic work.

  - Turn reasoning *down*, or thinking off, for prose, summarization,
    translation, simple lookups, and high-volume or latency-sensitive
    work. On language tasks, extended thinking can degrade output by
    pushing the model to over-edit.

- **Raise effort before reaching for a larger model.** A smaller model at
  high effort is often a better trade than a larger model at low effort.

- **Set a maximum output token cap** large enough to accommodate the
  expected output — SHOULD bound cost and prevent runaway generation, but
  MUST NOT truncate. Truncation partway through a response is a common,
  easily-missed failure mode, particularly with reasoning models whose
  thinking tokens count against the budget.

- **Use stop sequences to enforce structured output** and control
  tool-call loops in agentic workflows.

- **For repeatable output, set temperature to 0 (or near it)** and supply a
  fixed seed where supported. Bit-for-bit determinism is generally NOT
  guaranteed even at temperature 0.

- **Address repetition through clearer prompting and temperature** before
  reaching for penalties. Frequency and presence penalties reduce
  repetition by down-weighting already-produced tokens. Use sparingly,
  with small values, as large penalties degrade coherence.

### Harness engineering

- **Start with the minimum harness configuration that works**, adding
  only in response to failure modes actually observed.

- **Change one thing at a time and measure.** A new check, narrowed
  permission, or rewritten instruction either moves pass rate, latency,
  or token cost, or it is not earning its keep.

- **Review the whole harness on a model upgrade**, not just the
  instructions. Rules written for an older model's weakness may be
  counterproductive against a newer one.

- **Prune stale harness configuration.** It is worse than none, for the
  same reason stale context is worse than none.

- **Separate project-level from personal-level configuration.** Permitted
  tools, required checks, connected servers, and project skills belong in
  the repository. Chosen model, interface options, and personal shortcuts
  do not — exclude those paths from version control.

- **Harness configuration SHOULD be committed to version control** alongside
  the code it applies to.

- **Credentials MUST NOT be committed in harness configuration.**
  Reference environment variables or a secrets manager.

## Prompt engineering and context engineering

- **Treat context as a finite resource.** As context size increases, a
  model's ability to accurately recall information decreases —
  *context rot*, a performance gradient, not a hard cut-off. Every token
  added depletes the model's finite *attention budget*. Past a point,
  adding more tokens actively worsens performance.

- **Find the smallest set of high-signal tokens** that maximizes the
  likelihood of the desired outcome.

- **System prompts SHOULD be clear and direct**, in simple, plain
  language, pitched at the optimum level of specificity — specific
  enough to guide behavior, flexible enough to provide strong heuristics.

- **Prompts MUST be token-efficient.** Start with the minimum prompt
  needed, adding instructions only to address specific failure modes
  observed in testing.

- **Long prompts MUST be well structured.** RECOMMENDED to organize into
  distinct sections (background, instructions, success criteria) using a
  structured language like YAML or Markdown.

- **Manage context history on long-horizon tasks** through three levers:

  - **Compaction** summarizes a conversation nearing the context window
    threshold and re-initiates a new context with that summary. Overly
    aggressive compaction loses subtle but critical context.

  - **Structured note-taking (agentic memory)** persists notes outside the
    context window, pulled back in when needed. Commonly used for task
    lists; excels at incremental tasks planned up-front.

  - **Sub-agent architectures** delegate focused tasks to sub-agents with
    clean context windows. Ideal for complex research and analysis.

## Reusable context and just-in-time retrieval

- **Use agent skills to define project-specific workflow steps** rather than
  to encode knowledge, standards, etc.

- **Prefer just-in-time retrieval over always-on loading** for knowledge,
  standards, etc. Rather than embedding a full coding standard in a skill or
  other context bundle, provide a pointer and let the agent load
  it on-demand.

- **Use lightweight references** such as file paths and web links for pointers
  to dynamically-loaded information.

- **Skills SHOULD be narrowly scoped.** Where the harness supports it, use
  scoping mechanisms (directory-specific or pattern-matching rules) to load
  skills only when relevant.

- **A skill SHOULD have exactly one responsibility** — a single step in a
  workflow — and stop at a well-defined boundary. A skill SHOULD NOT
  combine _evaluation_ and _implementation_: a skill that analyzes and
  reports findings should be distinct from one that enacts a change.

- **Composed skills SHOULD be loosely coupled.** A skill SHOULD NOT
  invoke, refer to, or hand off to another skill by name. Each does its
  one job, reports its result, and stops; composition is the
  orchestrator's responsibility, not the skills'.

- **A skill SHOULD be explicit about its inputs and outputs** — what it
  consumes (OPTIONAL or REQUIRED), whether it runs non-interactively or is
  necessarily interactive, what output it produces in what format and
  where, and what success criteria to check against.

- **Non-interactive skills SHOULD be preferred by default**, as they are
  more reusable (can run unattended, including by parallel sub-agents).
  Reserve interactive skills for cases where human interaction _is_ the
  value the skill provides.

- **Skills and references MUST be token-efficient.** They consume tokens,
  depleting the attention budget and competing with the user's actual
  prompt. Start with the minimum content needed to elicit the desired
  behavior, and grow it only in response to observed failure modes.

- **Skills and references SHOULD be reviewed and pruned regularly.**
  Stale context is worse than none — it actively misleads the model.

- **With capable frontier models, do not encode universal best practices**
  like "never commit secrets" or "match the prevailing code style" — that
  knowledge is already embedded in the model. Use context bundles for
  guidelines, standards, and requirements specific to your project.

## Tools

- **Tools SHOULD be small, self-contained**, and focused on specific
  capabilities, with clear boundaries and no overlapping functionality.
  Decompose complex tasks into multiple tools that can be orchestrated
  together. Bloated tools create ambiguous decision points and bloat
  context.

- **Input parameters MUST be descriptive and unambiguous.**

- **Few-shot prompting (curated examples of tool usage) is RECOMMENDED.**
  Curate diverse, canonical examples. Do not overload the context with
  exhaustive edge cases.

## AI-assisted and agentic workflows

- **Split complex tasks into distinct planning and implementation**
  phases, matching model capability to each — RECOMMENDED for all but
  the simplest tasks. Use frontier models for planning, architecture,
  complex problem-solving, and security analysis; cheap, efficient models
  for code construction from pre-approved plans, small refactoring, and
  routine chores.

- **Fully agentic workflows require additional guardrails.**

- **Ask the AI to implement pre-approved plans incrementally** — small,
  stable, independently-deployable increments, easier to review and test
  than a "big bang" changeset. Small increments also bound the context
  window: a session scoped to one increment starts clean and avoids
  *context rot*. Define coding standards and conventions as concise,
  reusable prompt inputs. Batch similar tasks only sparingly — better a
  few small changesets than one large one to review.

- **Use version control to track AI-generated code** and provide a robust
  "undo". Avoid mixing manual and automated changes in the same revision.

### Verification of AI-generated code

- **AI-generated code destined for production MUST be validated** by a
  human against its success criteria.

- **Concrete, executable success criteria** matter more for predictable
  outcomes than the size or capability of the underlying model.
  Acceptance tests, schemas, linters — verifiable criteria — narrow
  the gap between frontier and cheaper models.

- **Verification of AI-generated output MUST NOT rely on the same AI session**
  that produced it. Wherever a rule or standard can be checked by a machine, it
  SHOULD be enforced by an independent, deterministic process (linter,
  type-checker, test suite) run outside the agent's own context, rather
  than left to the agent's self-assessment.

- **Do not treat your own generated tests as verification** of your own
  generated code. Both share the same blind spots. Surface the tests you
  write for explicit human review, and flag that reviewing them matters
  more than reviewing the code. MUST NOT modify the existing test suite
  without an explicit instruction to do so.

- **A test-driven approach is RECOMMENDED where feasible.** Write your own
  tests, then ask the AI to make them pass. Prefer high-level tests
  (end-to-end and integration) over unit tests alone — more robust, and
  better support for AI-assisted refactoring.

- **After a feature or fix, ask the AI to update its own knowledgebase.**
  Agents cannot reliably learn across sessions unless learning is
  explicitly documented. Keep an `AGENTS.md` in the project root linked to
  files documenting solutions to past problems, technical decisions and
  rationale, patterns that work well, and examples of correct
  implementations.

- **Reserve agentic approaches for genuine ambiguity, adaptive reasoning,
  or recovery from unexpected states.** Automation is deterministic and
  rules-based — preferable when the task is stable and predictable.
  Agentic systems are dynamic and reasoning-based but carry higher
  operational complexity and cost. Computationally irreducible tasks MUST
  be delegated to a tool that executes the steps (code interpreter,
  script, calculator), never left to a model to guess token-by-token.

- **Start with a single-agent system** (`TASK → AGENT → SOLUTION`) —
  RECOMMENDED for most tasks with well-defined goals and limited scope.
  Upgrade to multi-agent (`TASK → SUPERVISOR → SUB-AGENTS → SOLUTION`) as
  a deliberate response to a specific limitation, not a default posture.
  Reasons to upgrade: context management (focused per-agent context),
  parallelism, specialization (different models/tools per sub-task), fault
  isolation, independent verification (fresh context judges fairly), and
  reusability.

- **Use a tiered model strategy in agentic workflows** — RECOMMENDED.
  Frontier models for the supervisor role (complex planning, architectural
  decisions, high-level QA); smaller, faster, or locally-hosted models for
  sub-agents executing pre-approved plans.

- **A good harness mixes guides and sensors, both deterministic and
  inferential.** An agent steered only by guides repeats undetected
  mistakes; one checked only by sensors runs an expensive trial-and-error
  loop with no steering. Guardrails are critical where humans are less in
  the loop.
  - *Guides* steer _before_ acting: behavioral instructions (advisory —
    system prompts, `AGENTS.md`, skills) and permission constraints
    (enforced allow/deny lists in the harness — the most reliable guide
    because enforced by the runtime).
  - *Sensors* check _after_ acting, distributed across every step rather
    than a single end gate: deterministic sensors (linters, type checkers,
    tests — same verdict on the same input, the strongest signal) and
    inferential sensors (a second agent judging output — a fresh
    perspective, but MUST NOT substitute for deterministic checks).

- **An inferential sensor MUST NOT be the same agent, in the same session,
  that produced the output.** Models exhibit sycophancy. Invoke the
  reviewer as a distinct session, framed adversarially — instructed to
  assume the work is broken and verify that claim.

- **Guard against the agent loop with both a hard and a soft guide.** An
  agent stuck repeating an action burns tokens until it exhausts its
  context. Combine tool quotas (enforced hard cap on tool calls per run —
  a reliable backstop) with budget awareness (an advisory instruction
  telling the agent its quotas so it can ration). Neither alone suffices:
  an agent that doesn't know its budget cannot plan around it, and
  advisory limits can be ignored or miscounted. Start with minimum
  constraints and add guides only for observed failure modes, reviewing
  them on model upgrades.

- **Build agentic workflows as pipelines of narrowly-scoped agentic and
  scripted steps**, where the output of one is the input to the next.
  Agentic steps do the reasoning-heavy work; scripted steps (deterministic
  sensors) catch failure modes and feed back or escalate. Each step is a
  small, sharp tool with well-defined input/output — the input/output is
  the contract between steps, not explicit hand-offs (which produce tight
  coupling). The orchestrator determines the order, so steps stay
  composable across proactive, reactive, and scheduled entry points.

- **For one step to hand off to the next, its output MUST be persisted to
  a durable store**, not merely held in the conversation. Git is the
  preferred substrate: artifacts (requirements, decisions, designs, plans)
  branch, commit, review, and merge like code, with durability,
  diffability, and an audit trail for free. Persisting to disk also keeps
  the context window clean.

- **Where a workflow runs multiple agents or scripts against one
  repository at once, each MUST get its own isolated working copy.** Two
  processes writing to the same working tree concurrently may corrupt each
  other's work. A Git worktree is the appropriate mechanism; CI systems
  typically provide isolation already by cloning fresh per job.

- **Use evals to measure whether a change improved outcomes or quietly
  regressed them.** Evals are structured tests measuring how well an LLM,
  agent, skill, prompt, or workflow performs on a defined set of tasks —
  the AI equivalent of unit and regression tests, and the most important
  yet most often skipped practice. Without them, every change to model,
  prompt, skill, or harness is made blind. A test case has three parts: a
  realistic input, a description of success, and any fixtures it needs.

- **Eval suites SHOULD live in version control** alongside the code or
  prompts they exercise. Start small — most common and most failure-prone
  cases — and grow from real failures, not speculation. Beyond a handful,
  it is RECOMMENDED to use an established framework (eg. OpenAI Evals).

- **The central mechanism of evaluation is comparison.** Run the same eval
  with and without a change (or against the previous version) and look at
  the delta in pass rate, latency, and token cost. A change that does not
  move the pass rate is not earning its keep.

- **Assert objectively on mechanically verifiable properties** (regex
  matches, passing tests). **For qualitative properties** (clarity, tone),
  use an LLM as judge — run in a distinct session from the one that
  generated the output — or apply human judgment. Avoid over-specifying
  assertions up front: observe what the system produces, then write checks
  against those outputs, running several samples to account for
  non-determinism.

- **Use an open protocol, specifically MCP, to connect an agent to
  external tools or data** — RECOMMENDED over custom point-to-point
  integrations. Benefits: interoperability, composability, portability
  across harness/model changes, and reduced maintenance. MCP is
  client-server: a server exposes tools and resources; a client (typically
  a harness) connects to one or more servers.

- **Treat MCP servers as dependencies.** A server is third-party code
  running with access to your tools, data, and actions, and MUST get the
  same scrutiny as any dependency — a compromised server could exfiltrate
  any data the agent can reach and take any action its tools permit.
  Prefer official or well-known servers and review community-provided
  ones; pin versions and review changes before upgrading; test unfamiliar
  servers in isolation first.

- **Apply least privilege to MCP at two levels.** *Connection scope:*
  connect only the servers and tools the current task needs, not "just in
  case." *Credential scope:* scope each server's credentials to the
  minimum required (eg. read-only where writes are not needed). Review
  connected servers and enabled tools before starting a task, not only at
  first configuration.

- **Treat all MCP tool results as untrusted input** — external content and
  a vector for indirect prompt injection. Treat tool output as data, not
  instructions; prefer human confirmation before irreversible actions
  taken through MCP tools, especially just after processing external
  content; audit execution traces when tasks involve servers that fetch
  untrusted data.

- **Treat MCP tool definitions as an attack surface.** Names and
  descriptions are injected into the context and can steer the agent. Two
  2025 attacks: *tool poisoning* (malicious instructions in a tool's
  description) and *lookalike/shadowing tools* (impersonating a trusted
  tool to route calls to the attacker). Review tool definitions, not just
  results, before connecting and after any upgrade (descriptions can
  change without behavior changes — why versions SHOULD be pinned). Be
  wary of connecting multiple servers whose tools share names.

- **Prefer local MCP servers (over stdio)** where the tool can run on the
  same host — they avoid network exposure entirely. Remote servers MUST
  authenticate clients and MUST use encrypted transport; an
  unauthenticated server MUST NOT be exposed on a public interface. Run
  servers only while needed.

- **Mind the context cost of connected servers.** Every connected server
  injects its tool definitions into the context on every inference call —
  not just when used. Indiscriminately connecting many servers degrades
  performance (context rot) and increases cost.

- **Spend tokens and model capability where they change the outcome, and
  economize everywhere else.** Most services meter per token, charging
  separately for input and output (output typically several times more),
  with reasoning tokens billed as output and cached input billed at a
  steep discount.

  ```
  cost = (input tokens × input price)
       + (cached input tokens × cached input price)
       + (output tokens × output price)
  ```

- **Right-size the model — the largest cost lever.** Defaulting to the
  biggest model is wasteful; defaulting to the cheapest is unreliable and
  may cost more in rework. In agentic workflows, reserve frontier models
  for the supervisor and delegate execution to efficient sub-agents.

- **Economize on context.** Every token is billed on every inference call
  and depletes the attention budget. The context-engineering practices are
  also cost-reducing: keep reusable context token-efficient, prefer
  just-in-time retrieval, prune stale context, use compaction on
  long-horizon tasks.

- **Exploit prompt caching.** Where supported, place stable content
  (system prompt, skills, large reference documents, codebase context) at
  the start of the prompt and variable content (the user's query) at the
  end. Keep that prefix byte-stable — even a small edit near the top
  invalidates the cache for everything after it.

- **Control output and reasoning length** — the expensive tokens. Set a
  sensible maximum output cap (large enough to avoid truncation), request
  concise or structured output where prose adds no value, and scale the
  reasoning budget to complexity rather than defaulting to maximum.

- **Batch where latency allows** — batching amortizes shared context, but
  sparingly, as the trade-off is large diffs to review. For high-volume,
  non-latency-sensitive work, asynchronous batch APIs at a discount are
  RECOMMENDED.

- **Choose cost-effective access.** A single gateway subscription
  (OpenRouter, Perplexity Pro) can beat separate lab subscriptions and
  lets you route each task to the cheapest adequate model. For high-volume,
  repetitive, or privacy-sensitive work, locally-run open-weight models
  eliminate per-token costs entirely.

- **Measure before optimizing.** Track token consumption per task. When
  evaluating a skill, rule, or prompt change, measure the token-cost delta
  alongside the quality delta. Re-measure when switching models — relative
  pricing and token efficiency vary.

- **Apply the same security principles to AI tools as to any development
  dependency** — across the services that run models, the data submitted,
  the permissions granted to agents, and the code produced.

- **Run AI models and tools in containers or virtual machines** where
  possible, for an isolation boundary between models, files, runtime
  processes, and the host. Do not run containerized model services as
  root, and keep them running only while actively needed. For IDE
  development it is RECOMMENDED to work inside a
  [devcontainer](https://containers.dev/), with both editor and harness in
  the container and project files bind-mounted.

- **Local model servers (eg. Ollama) MUST bind to loopback (`127.0.0.1`)
  unless remote access is explicitly required.** If LAN access is needed,
  binding to `0.0.0.0` MUST be protected with a local firewall rule; never
  expose model-server ports on a public interface. For remote access, use
  an SSH tunnel or VPN rather than exposing the service directly.

- **Treat models as third-party dependencies.** They are large binary
  files encoding learned behaviors. Only download from official or
  well-known repositories, do not use untrusted models on sensitive data,
  and test unfamiliar models in isolation first.

- **Be careful submitting proprietary code, credentials, or sensitive data
  to public AI services.** Use enterprise AI solutions with appropriate
  data-handling agreements for commercial projects.

- **Prompt injection is an attack in which malicious instructions embedded
  in data cause an agent to take unintended actions.** *Direct injection:*
  crafted input overrides the system prompt. *Indirect injection:* the
  agent autonomously reads external content (file, web page, API response,
  code comment) containing embedded instructions — more dangerous in
  agentic workflows, where malicious content may sit deep in an autonomous
  task chain. Mitigate: treat external content as data in a clearly
  delimited structure; grant only the tool permissions the task needs;
  prefer human confirmation before irreversible actions after processing
  external content; audit execution traces on untrusted sources.

- **Break the lethal trifecta.** Prompt injection becomes catastrophic
  when an agent simultaneously has all three of: (1) access to private
  data, (2) exposure to untrusted content, (3) the ability to communicate
  externally — the conditions to read private data and leak it. Assume
  injection will always be a risk and remove one leg: withhold sensitive
  data, isolate from untrusted input, or cut off external communication.
  Any one or two parts in isolation is comparatively safe.

- **Apply least privilege to tool permissions to limit the blast radius.**
  Grant read-only where writes are not needed, scope filesystem access to
  specific paths, restrict shell access to allow-listed commands, and
  disable network egress for agents that do not need it. Review agent
  permissions before starting a task — a set appropriate for one task may
  be excessive for the next.

- **Review agent output with the same scrutiny as a human contributor's.**
  Keep tasks small so diffs are reviewable and problems surface early.
  Models reproduce insecure patterns learned from training data —
  hardcoded credentials, injection sinks, insecure defaults, missing input
  validation — so pay particular attention to authentication,
  authorization, cryptography, and external input.

## References

- [AGENTS.md specification](https://agents.md):
  Read this when authoring `AGENTS.md` files.

- [Agent Skills specification](https://agentskills.io/specification):
  Read this when authoring agent skills.
