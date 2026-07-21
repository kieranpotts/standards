# TS-61: AI Tools

Best practices for using AI tools to support software development
workflows — specifically, the generation of computer program code,
software architectural designs, and technical documentation.

In this standard, the acronyms LLM and AI are used interchangeably to
refer to AI models based on the transformer (or similar) architecture.

Topics covered: the role of human judgment in AI-assisted development;
quality assurance strategies for AI-generated code; understanding AI
model capabilities and limitations; engineering and configuring an agent
harness; tuning model behavior through inference-time parameters; prompt
and context engineering; evaluating
models and prompts (evals); cost optimization techniques; task
segmentation and workflow optimization; and security and risk
considerations.

Use this when designing, implementing, reviewing, or governing AI-assisted
or agentic software development workflows, or when authoring reusable
agent context (AGENTS.md files, skills).

Do NOT use this for general security and secrets management — see
[TS-52: Security and Secrets Management](../052/AGENTS.md). For privacy
and PII handling, see [TS-53: Privacy and Data Protection](../053/AGENTS.md).
For QA and testing practices, see [TS-12: Quality Assurance](../012/AGENTS.md)
and [TS-13: Functional Testing](../013/AGENTS.md). For version control
practices, see [TS-9: Version Control](../009/AGENTS.md). For Docker and
container isolation, see [TS-58: Docker](../058/AGENTS.md). For
application architecture, see [TS-5: Application Architecture](../005/AGENTS.md).
For general code design, see [TS-7: Code Design](../007/AGENTS.md).

## Rules

### Definitions

- **Model.** A large-language model (LLM), a type of neural network — the
  "brain" in an AI toolchain. A model only consumes tokens (decoded from
  text or images) and outputs tokens (encoded into text or images), and
  has no inherent ability to act on computer systems — for that, you
  need a harness.

- **Model runtime.** The software and infrastructure layer that executes
  a model's inference calls — loading weights, scheduling GPU/TPU
  compute, batching concurrent requests, applying serving-time
  optimizations (quantization, key-value caching). Examples: vLLM,
  llama.cpp, TensorRT-LLM, Ollama.

- **Agent harness** (formerly scaffold). A conventional computer program
  that wraps a model runtime. It mediates between the user, the model,
  and the rest of the computer environment. It constructs the system
  prompt, defines and executes tools (file reads/writes, shell commands,
  MCP server calls), feeds tool output back to the model as context,
  implements security (sandboxing, permission management), and
  proactively manages the context window (compaction, task lists).
  Examples: Claude Code, Codex, OpenCode, Pi.

- **Agent.** An instance of a model (or multiple models) running in an
  agent harness in an iterative loop (agent = model + harness). The
  model proposes an action, the harness executes it via tool calls, and
  the result goes back into the model's context via the next inference
  call. This repeats until the task is done or a stop condition is
  reached. A *coding agent* is an agent using models trained for
  programming tasks in a harness designed for software development.

- **Tool.** A function an agent harness exposes to a model and invokes on
  the model's request (a *tool call*). Examples: file edits, shell
  executions, web requests, HTTP API calls. *MCP (Model Context
  Protocol)* is the emerging industry standard protocol for serving
  tools or data to a harness.

- **Agent framework/SDK.** A library for building your own agent harness
  (not a finished product). Examples: LangGraph, Claude Agent SDK.

- **Agent orchestrator.** A layer above a harness that runs multiple
  agent sessions in parallel, often using Git worktrees. Examples:
  Claude Squad, Crystal, mux. Some harnesses are also orchestrators,
  capable of spawning and managing *subagents*.

- **Inference provider.** An organization that hosts and serves models
  via web services (self-hosted, cloud provider, or third-party vendor
  API). Distinct from the *model vendor*, though often the same company.

- **Context.** A model's "memory" — the set of tokens (instructions,
  files, conversation, tool results) made available to the model in a
  single inference call. The *system prompt* is the initial set of
  instructions injected by the harness. Different models have different
  **context window** sizes (how many tokens they can consume in one
  inference call). Context is the main supply-chain/injection surface
  for agentic workflows.

- **Prompt injection.** Adversarial instructions embedded in data the
  agent processes (files, web pages, tool results) that attempt to
  override the user's intended instructions.

- **Data exfiltration.** Transmission of sensitive material from an
  agent's context or accessible environment to an unauthorized
  destination, via tool calls or model output.

### Human-in-the-loop

- **There MUST always be a human-in-the-loop when using AI tools for
  software development.** Only the _degree_ of human involvement may
  change with the domain and risk profile. A throwaway prototype can be
  driven with a light touch; code that handles authentication, money,
  personal data, or safety-critical functions — or any change that is
  hard to reverse — warrants proportionately closer scrutiny, up to
  line-by-line review and independent verification.

- **The normal software development life cycle MUST NOT change when AIs
  are introduced.** Following rigorous development processes,
  particularly quality control and change management, becomes _more_
  important, not less.

- **As confidence in an agentic workflow's reliability grows
  (demonstrated by a track record of predictable outcomes), human
  checkpoints can be deliberately reduced.** This is the path toward
  greater autonomy — an incremental transfer of trust. Conversely, if
  testing reveals unpredictable outcomes, add more human checkpoints.

#### Success criteria

- **AI-generated code destined for production MUST be validated by a
  human against its success criteria.** Setting clear success criteria
  is the key to effective agentic workflows.

- **Concrete, executable success criteria matter more for predictable
  outcomes than the size or capability of the underlying model.**
  Acceptance tests, schemas, linters — verifiable criteria — narrow
  the gap between frontier and cheaper models, because both are steered
  by the same external check rather than by the model's unaided
  interpretation.

- **Verification of AI-generated output MUST NOT rely solely on the same
  AI session that produced it.** Wherever a rule or standard can be
  checked by a machine, it SHOULD be enforced by an independent,
  deterministic process (linter, type-checker, test suite) run outside
  the agent's own context, rather than left to the agent's
  self-assessment. Agents are not reliable judges of their own work.
  Treat agent-reported success as a claim to be verified, not a fact.

#### Software architecture

- **A clean, well-structured codebase yields better results from AI code
  generators.** Clear tiers and boundaries constrain the blast radius of
  any change. Without them, AI tools are more likely to make sweeping
  changes with unintended consequences.

### Choosing models

- **A model's knowledge of semantic associations is learned from its
  training data.** If training data is biased toward certain languages,
  frameworks, or styles, the model reflects those biases. Choose a
  model that has been trained on data relevant to the task. General-
  purpose models will be adequate for many tasks in modern programming
  languages; for specialized tasks, consider specialist models.

- **Match the model tier to the task.** Models are commonly grouped into
  tiers that trade capability against speed and cost:
  - **Frontier** models (Claude Opus, GPT flagship, Gemini Pro) are the
    state of the art — most capable, slowest, most expensive. SHOULD be
    reserved for work where their capability changes the outcome:
    planning, architecture, complex problem-solving, security analysis.
  - **Mid-tier** models (Claude Sonnet, GPT mid-tier, Llama 70B, Qwen)
    balance capability, speed, and cost. Adequate for most day-to-day
    tasks, including a large share of coding work.
  - **Light** models (Claude Haiku, Gemini Flash, GPT mini) trade
    capability for speed and cost. Suit high-volume, latency-sensitive,
    or mechanical work — classification, extraction, routing, simple
    lookups.
  - **Reasoning** models spend extra compute on an internal chain-of-
    thought before answering, at the cost of latency and token spend.
    Use for problems with a verifiable chain of logic: maths, planning,
    multi-step analysis, complex debugging.
  - **Specialist** models are fine-tuned for a narrow domain (eg. a
    search-grounded model for factual retrieval with citations, or a
    code-completion model for IDE autocomplete). Prefer a specialist
    over a general-purpose one where the task matches its specialization.
  - **Open-weight** models have publicly released weights that can be
    downloaded and run on your own hardware. Typically trail frontier
    models by some months, but eliminate per-token cost and keep data
    on infrastructure you control. RECOMMENDED for privacy-sensitive or
    offline work, and for high-volume tasks where local hardware is
    adequate.

- **Identify the dominant capability a task demands, then choose the
  cheapest tier and capability type that satisfies it.** Reserve
  frontier and reasoning models for tasks where that capability is
  genuinely the bottleneck.

- **No model reliably beats a deterministic tool at exact computation.**
  For exact multi-step computation (arithmetic on large numbers,
  tracing algorithm execution), the right choice is a script or code
  interpreter, not a model. These tasks are *computationally
  irreducible* — the only way to know the outcome is to carry out every
  step computationally.

- **Public benchmarks are a useful first filter but no substitute for
  evaluating candidate models on your own representative tasks.** See
  the section on evaluation.

### Choosing interfaces

- **The interface through which you interact with a model matters at
  least as much as the choice of model.** General-purpose chatbot
  interfaces are flexible but blunt. Specialist interfaces (IDE
  coding assistants, agent harnesses) present AI capabilities in a form
  optimized for the task, with necessary structure, constraints, and
  affordances built into the UI.

- **When designing an AI-assisted workflow, it is RECOMMENDED to check
  whether a specialist tool exists for the job before defaulting to a
  general-purpose chatbot.**

#### Agent harnesses vs IDE coding assistants

- **IDE coding assistants** (GitHub Copilot, Cursor) are inline tools
  that observe the developer's active file and offer completions,
  explanations, or targeted edits. The developer drives the
  interaction. Best for fine-grained, interactive work.

- **Agent harnesses** (Claude Code, OpenCode, Aider) operate at a higher
  level of abstraction. The developer specifies a goal; the harness
  plans and executes a sequence of steps to reach it. The developer's
  role shifts from directing each action to supervising the outcome.
  Best for multi-file tasks defined by a goal rather than a sequence of
  steps, where the developer is comfortable reviewing outcomes.

#### Adopting a harness vs building on a framework

- **It is RECOMMENDED to default to a ready-made harness** for
  interactive and ad hoc development. Ready-made harnesses ship with a
  curated tool set, context-window management, permission system,
  memory persistence, and MCP support already wired together.

- **Reserve building on a framework for when you are shipping an agentic
  _product_, embedding agentic capability into an application, or you
  have orchestration/integration needs no available harness meets.**
  Building on a framework gives full programmatic control but costs
  engineering effort and ongoing maintenance.

- **Start with a harness and graduate to a framework only when a concrete
  limitation forces the move** — not in anticipation of one. Consistent
  with this standard's incremental philosophy.

### Harness engineering

- **Harness engineering is the work of controlling the environment in
  which a model runs.** The model is chosen from what vendors offer; the
  environment around it is built locally, against the failure modes of a
  specific codebase, and it is what determines an agent's capabilities
  and constraints. Not confined to teams building on a framework — a team
  running an off-the-shelf harness engineers one too, through
  configuration rather than code. The build-versus-buy decision
  determines the mechanism, not the discipline.

- **The dimensions of the harness surface:** the tool surface (including
  connected MCP servers), the context assembled (system prompt,
  instruction files, skills), the permissions enforced, the checks that
  fire, the models assigned to each role, and the record kept
  (transcripts and persisted artifacts). Each is covered in its own right
  elsewhere in this standard — context engineering, guides and sensors,
  least-privilege tool access, auditability.

- **The dimensions are interdependent.** Widening the tool surface raises
  the burden on permissions and checks. Adding instructions to steer
  behavior that a check could enforce mechanically spends context to buy
  a weaker guarantee.

#### Configuration is code

- **Project-level harness configuration SHOULD be committed to version
  control** alongside the code it applies to. Configuration living only
  on one developer's machine cannot be reviewed, cannot be reproduced in
  CI, and silently produces different agent behavior for different
  people.

- **Changes to harness configuration SHOULD be reviewed.** Widening a
  permission list or disabling a check changes what every subsequent
  unsupervised session may do — often more consequential than the code
  reviewed alongside it, and easy to wave through because it is short.

- **Separate project-level from personal-level configuration.** Permitted
  tools, required checks, connected servers, and project skills belong in
  the repository. Chosen model, interface options, and personal shortcuts
  do not — exclude those paths from version control.

- **Credentials MUST NOT be committed in harness configuration.**
  Reference environment variables or a secrets manager.

- **Record the rationale for each non-obvious rule.** A permission denial
  or check whose reason is unrecorded will eventually be removed by
  someone who cannot tell whether it still matters — the same failure
  mode as an undocumented test.

#### Hooks and deterministic enforcement

- **A hook is a program the harness runs automatically at a defined point
  in the agent's loop** — before a tool call, after a file write, at
  session start, when the agent believes it has finished. The harness
  executes it as an ordinary process and acts on its exit status, so its
  verdict does not depend on the model's cooperation or interpretation.
  - A hook running _before_ an action, able to block it, is an **enforced
    guide** — a programmable extension of a permission list, able to
    decide against arguments and current state rather than only whether a
    tool is allowed.
  - A hook running _after_ an action is an **enforced deterministic
    sensor** — the formatter, linter, type checker, or test suite runs
    because the harness ran it, not because the agent chose to.

- **Where a rule is mechanically checkable and expressible as a program,
  it SHOULD be enforced by a hook rather than stated as a behavioral
  instruction.** Instructions compete for the attention budget on every
  inference call and are obeyed probabilistically. A hook costs no
  context and is obeyed absolutely.

- **An instruction observed to be ignored repeatedly is a candidate for
  promotion to a hook.** Restating it more emphatically, or in more
  places, is the weaker and more expensive response.

- **A blocking hook MUST return an error message specific enough for the
  agent to self-correct**, otherwise it converts a recoverable mistake
  into a stall. Hooks SHOULD be fast — they run on every matching event
  and their latency is added to the loop. Bind expensive checks to
  infrequent events (end of task, not every file write).

#### Evolving the harness

- **Start with the minimum configuration that works**, adding only in
  response to failure modes actually observed. Configuration added in
  anticipation tends to constrain the model against its own better
  judgment.

- **Change one thing at a time and measure.** Harness configuration is
  one of the components evals exist to evaluate. A new check, narrowed
  permission, or rewritten instruction either moves pass rate, latency,
  or token cost, or it is not earning its keep.

- **Review the whole harness on a model upgrade, not just the
  instructions.** Rules written for an older model's weakness may be
  counterproductive against a newer one; tools pitched at a less-capable
  model may now be needlessly fine-grained.

- **Prune.** Stale harness configuration is worse than none, for the same
  reason stale context is worse than none.

#### Portability

- **Harness configuration is the least portable layer of an AI
  toolchain.** Reusable context has `AGENTS.md` and skills; tool
  integration has MCP; configuration has no equivalent. This creates a
  tension: the most reliable enforcement mechanisms are the least
  portable, while the most portable mechanism — written instruction — is
  the weakest.

- **Keep enforcement where it is strongest and logic where it is
  portable.** Put the substance of a check in an ordinary repository
  script that a developer can run by hand and CI can run unchanged, and
  let harness-specific configuration be a thin binding that invokes it.
  Migrating harness then means rewriting the binding, not the check.

- **Prefer a project's existing quality gates over harness-specific
  reimplementations.** A hook running the project's lint command inherits
  every rule that command enforces, and stays correct as they change.

### Tuning model behavior

- **First try steering model behavior through the prompt, context, and
  model choice.** Reach for inference-time parameters only when you
  have a specific reason — eg. a specific failure mode the controls
  address (output too random or repetitive, responses truncated,
  reasoning too shallow or too slow).

- **Note:** Some interfaces (agent harnesses, IDE assistants) fix these
  parameters internally and do not expose them. Where a tool sets them
  for you, it is usually because the maintainers have tuned them for
  that tool's specialist workload.

#### Temperature and sampling

- **Temperature** controls the randomness of token selection. Match
  temperature to the task:
  - Low (0–0.3): Focused, near-deterministic. Code generation, data
    extraction, classification, structured output, factual answers.
  - Medium (0.4–0.7): Balanced. General conversation, drafting,
    summarization.
  - High (0.8+): Varied, exploratory. Creative writing, brainstorming,
    generating diverse options.

  Higher temperature does not make a model "more intelligent" — it
  makes the model sample less-probable tokens, trading coherence for
  diversity. Past a point, this produces incoherent output.

- **Top-p (nucleus sampling)** restricts sampling to the smallest set
  of tokens whose cumulative probability meets threshold _p_. **Top-k**
  caps the candidate set at the _k_ most likely tokens. It is
  RECOMMENDED to tune temperature _or_ top-p, but not both at once —
  their interaction is hard to reason about.

#### Reasoning: thinking and effort

- **Reasoning models expose controls over how much compute the model
  spends "thinking"** (internal chain of thought). Two related but
  separate dials:
  - **Thinking** governs _whether and when_ the model produces an
    internal chain of thought before committing to an answer. Typically
    adaptive — the model decides per request whether a step warrants
    extended reasoning. Can also be turned fully off.
  - **Effort** governs _how hard the model works_ overall — thoroughness
    of surrounding actions: how much it explores, how many tool calls it
    makes, how much it verifies its own work, how much preamble it
    produces. Usually exposed as discrete levels (low, medium, high).

- **Both SHOULD be scaled to the task, not defaulted to maximum:**
  - Turn reasoning *up* (adaptive thinking, higher effort) for problems
    with a verifiable chain of logic — maths, planning, multi-step
    analysis, complex code, debugging — and for long-horizon agentic
    work.
  - Turn reasoning *down*, or thinking fully off, for prose,
    summarization, translation, simple lookups, and high-volume or
    latency-sensitive work. On language tasks, extended thinking can
    actively degrade output by pushing the model to over-edit.

- **Raise effort before reaching for a larger model.** A smaller model
  at high effort is often a better trade than a larger model at low
  effort. Thinking tokens are billed and higher effort consumes more
  tokens and more time — both dials are a direct cost/quality/latency
  tradeoff.

#### Output controls and determinism

- **Maximum output tokens** caps response length. A sensible cap SHOULD
  be set to bound cost and prevent runaway generation, but MUST be
  large enough to accommodate the expected output. Truncation partway
  through a response is a common, easily-missed failure mode,
  particularly with reasoning models whose thinking tokens count against
  the budget.

- **Stop sequences** terminate generation when the model emits a
  specified delimiter. Useful for enforcing structured output and
  controlling tool-call loops in agentic workflows.

- **For repeatable output, set temperature to 0 (or near it) and supply
  a fixed seed where supported.** However, bit-for-bit determinism is
  generally NOT guaranteed, even at temperature 0. Evals and
  reproducibility checks SHOULD account for residual non-determinism —
  eg. run several samples and assert against properties of the output,
  rather than assuming a single exact string.

#### Penalties

- **Frequency penalty** and **presence penalty** reduce repetition by
  down-weighting tokens the model has already produced. Use sparingly,
  with small values. Large penalties degrade coherence. It is
  RECOMMENDED to address repetition first through clearer prompting and
  temperature, reaching for penalties only when those prove
  insufficient.

### Context engineering

- **Context engineering is a superset of prompt engineering.** It
  encompasses the entire set of tokens passed to an LLM during
  inference — system prompts, examples, message history, and any other
  data in the context window. The guiding principle: find the smallest
  set of high-signal tokens that maximizes the likelihood of the desired
  outcome.

- **Treat context as a finite resource.** As context size increases, a
  model's ability to accurately recall information decreases —
  *context rot*. This is a performance gradient, not a hard cut-off.
  Every token added depletes the model's finite *attention budget*. At
  some point, adding more tokens actively worsens performance.

- **Context engineering is particularly critical for tools used by AI
  agents.** Because agents run autonomously with minimal oversight,
  their tools must be programmed to manage context effectively —
  through compaction of long-horizon tasks, token-efficient tool design,
  and just-in-time data retrieval.

#### System prompts

- **System prompts SHOULD be clear and direct, using simple, plain
  language.**

- **Pitch system prompts at the optimum level of specificity.** Too
  specific hardcodes brittle logic and increases maintenance; too
  general fails to give the model strong signals. Strike a balance:
  specific enough to guide behavior, flexible enough to provide strong
  heuristics.

- **Prompts MUST be token-efficient.** Skills, rules, instructions, and
  other reusable prompt components SHOULD be concise and focused on the
  most critical information. Start with the minimum prompt needed, add
  instructions only to address specific failure modes observed in
  testing.

- **Long prompts MUST be well structured.** RECOMMENDED to organize
  into distinct sections (background information, instructions, success
  criteria). Use a structured language like YAML or Markdown to
  delineate sections.

#### Specialized tools

- **Tools SHOULD be small, self-contained, and focused on specific
  capabilities** (Unix philosophy). Complex tasks SHOULD be decomposed
  into multiple tools that can be orchestrated together. Each tool
  SHOULD have clear boundaries, with no overlapping functionality.
  Input parameters MUST be descriptive and unambiguous. Bloated tools
  create ambiguous decision points and bloat context with redundant
  information.

- **Few-shot prompting (curated examples of tool usage) is
  RECOMMENDED.** Curate a set of diverse, canonical examples, but do
  not overload the context with exhaustive edge cases.

- **Match the tool's abstraction level to how the agent naturally
  reasons about the task.** A single composite operation (retrieve,
  filter, format in one call) is typically better than three separate
  low-level calls. Fine-grained interfaces force the agent to manage
  implementation details, multiply turns, and consume context with
  intermediate state.

#### Just-in-time retrieval

- **Dynamically extend context with new information only when needed.**
  Rather than preloading all context, instruct agents to load
  additional instructions at runtime. Lightweight references (file
  paths, stored queries, web links) are ideal.

- **Treat session-wide context** (product taxonomy, critical
  constraints, syntax rules, project-wide conventions) **as a candidate
  for persistent loading. Treat everything else as a candidate for
  just-in-time retrieval.**

- **Trade-off:** Runtime exploration is slower than precomputed data,
  and agents can waste time chasing dead-ends. This technique requires
  careful design of the agent's information landscape and the
  tools/heuristics it uses to navigate it.

#### Context history

- **Compaction** summarizes a conversation nearing the context window
  threshold and re-initiates a new context with that summary. The art
  is in selecting what to keep vs. discard — overly aggressive
  compaction can lose subtle but critical context. The first lever in
  context engineering for long-horizon tasks.

- **Structured note-taking (agentic memory)** persists notes outside
  the context window that can be pulled back in when needed. Commonly
  used to manage task lists in a session. Excels at incremental tasks
  that can be planned up-front.

- **Sub-agent architectures** delegate focused tasks to specialized
  sub-agents with clean context windows. The main agent follows a
  high-level plan but delegates discrete steps. Ideal for complex
  research and analysis where synthesis from multiple specialist models
  is beneficial.

### Reusable context

- **Reusable context consumes tokens, depleting a model's attention
  budget and competing with the user's actual prompt.** The same core
  principles of context engineering apply.

#### General best practices

- **Reusable context MUST be token-efficient.** Start with the minimum
  content needed to elicit the desired behavior, and grow it only in
  response to observed failure modes.

- **A bundle of reusable context SHOULD be narrowly scoped.** Where an
  agent harness supports it, use scoping mechanisms (directory-specific
  or pattern-matching rules) to load content only when relevant.

- **Prefer just-in-time retrieval over always-on loading.** Rather than
  embedding a full coding standard in a context bundle, provide a
  pointer and let the agent load it on-demand.

- **Reusable units of context SHOULD be reviewed and pruned regularly.**
  Instructions that were once useful can become stale, redundant, or
  contradictory. Stale context is worse than no context — it actively
  misleads the model.

- **With capable, frontier coding models, you will get little value
  from context bundles that specify universal best practices** like
  "never commit secrets" or "match the prevailing code style". Such
  knowledge is already embedded in the model. Use context bundles to
  capture guidelines, standards, and requirements specific to your
  project.

#### Conventions

- **As of 2026, AI tool makers have not converged on where reusable
  context should live, what to call it, or how to load it.** If you use
  multiple agent harnesses, you may end up maintaining the same bundles
  in `CLAUDE.md`, `.cursorrules`,
  `.github/copilot-instructions.md`, etc. Duplication will lead to
  drift.

- **It is RECOMMENDED to maintain a single source-of-truth collection
  of reusable context bundles**, and transform this source material
  into distributable artifacts in formats tailored for different agent
  harnesses.

- **The industry is slowly converging on two standards: `AGENTS.md`
  and skills files.** It is RECOMMENDED to adopt these standards for
  your source files.

#### The AGENTS.md standard

- **`AGENTS.md` is an open convention** designed to give coding agents a
  predictable way to understand and operate on software projects,
  jointly launched by Google, OpenAI, Factory, Sourcegraph, and Cursor
  to replace tool-specific instructions. Canonical specification:
  [agents.md](https://agents.md).

- **`AGENTS.md` is a loose convention, not a strict standard.** Any
  Markdown is supported; suggested sections (project overview, dev
  environment, build/test commands, code style, security) are not
  required. Agents parse `AGENTS.md` if it exists in the current
  working directory, else the nearest parent directory.

- **The "repository structure" section is RECOMMENDED** — one of the
  highest-leverage things you can give an agent, sparing it from wasting
  tokens grepping around the project's directory tree.

- **Start with a minimum baseline then extend your agent instructions
  incrementally** to improve output.

#### Agent skills

- **Skills are a complementary open convention** for packaging reusable
  bundles of context that agents can load on demand. Skills complement
  `AGENTS.md`: whereas `AGENTS.md` provides a static, always-loaded
  orientation to the project, skills encapsulate specific procedures,
  standards, runbooks, or playbooks loaded dynamically when relevant.
  Canonical specification: [agentskills.io/specification](https://agentskills.io/specification).

- **Use skills to define a small set of common workflow steps**, while
  keeping knowledge (standards, policies, constraints, domain models)
  as separate reference documents loaded on-demand. Workflow skills
  should be step-by-step, deterministic, free of domain-specific facts,
  so they rarely change between projects and domains. This separation
  makes workflow skills more reusable and helps debugging:
  - "Did the workflow break?" → Skill issue.
  - "Did the knowledge change?" → Retrieval issue.

- **A skill SHOULD have exactly one responsibility** — a single step in
  a workflow — and stop at a well-defined boundary. A skill SHOULD NOT
  combine _evaluation_ and _implementation_ in one responsibility. A
  skill that analyzes and reports findings should be distinct from a
  skill that enacts a change. The decision of whether, when, and how
  to act on findings belongs to whoever is orchestrating the workflow.

- **Where multiple skills are composed into a workflow, they SHOULD be
  loosely coupled.** A skill SHOULD NOT directly invoke, refer to, or
  hand off to another skill by name. Each skill does its one job,
  reports its result, and stops. Composition is the responsibility of
  the orchestrator, not the skills.

- **A skill SHOULD be explicit about its inputs and outputs** — what
  input it consumes (and whether OPTIONAL or REQUIRED), whether it can
  run non-interactively to completion or is necessarily interactive,
  what output it produces in what format and where, and what success
  criteria the output should be checked against.

- **Non-interactive skills SHOULD be preferred by default**, as they
  are inherently more reusable (can be run unattended, including by
  parallel sub-agents). Reserve interactive skills for cases where
  human interaction _is_ the value the skill provides. This reflects
  the _specs-to-code_ movement: push interactive work upstream into
  requirements-gathering, so downstream delivery runs non-interactively
  from executable acceptance criteria.

- **Skill discovery:** The formal specification defines the path as
  `.agents/skills/`, relative to the project root, but not all
  harnesses support this out-of-the-box. Some harnesses also look for
  global skills in the user's home directory. Until universal standards
  converge, tailor location and naming to your chosen harness. One
  option is to use `AGENTS.md` to reference skill locations and provide
  instructions to load them just-in-time.

- **A skill is a directory containing, at minimum, a `SKILL.md` file.**
  The directory MAY also contain `scripts/`, `references/`, and
  `assets/` subdirectories (executable code, supplementary docs, static
  resources). This standard RECOMMENDS including a `README.md` for
  human maintainers.

  ```
  skill-name/
  ├── SKILL.md          # REQUIRED: metadata + instructions/rules.
  ├── README.md         # RECOMMENDED: for human maintainers.
  ├── scripts/          # OPTIONAL: executable code.
  ├── references/       # OPTIONAL: extended documentation.
  ├── assets/           # OPTIONAL: templates, schemas, other resources.
  ```

- **The `SKILL.md` file MUST contain YAML front-matter followed by a
  Markdown body.** Two front-matter fields are REQUIRED:
  - `name`: 1-64 characters of lowercase alphanumerics and hyphens (no
    spaces or punctuation). SHOULD match the parent directory name.
  - `description`: 1-1024 characters describing both _what_ the skill
    does and _when_ to use it. This is the most important part of a
    skill — it defines the conditions under which agents should
    automatically load the rest of the skill into context.

  OPTIONAL fields: `license`, `compatibility` (environment
  requirements), `metadata` (arbitrary key-value pairs), `allowed-tools`
  (pre-approved tools — experimental).

- **Effective skill descriptions:**
  - Use imperative phrasing. "Use this skill when…" rather than "This
    skill does…".
  - Focus on user intent, not implementation detail.
  - Err on the side of explicitness. List every context where the skill
    applies, including cases where the user may not name the domain
    directly.
  - Stay under the 1024-character hard limit (content beyond it may be
    silently truncated).

- **Skill content (the Markdown body) has no required structure.**
  Freeform Markdown is supported. A useful test for every instruction:
  "Would the agent get this wrong without this instruction?" If not,
  cut it.

- **Skills are just guidelines.** Agents may activate skills only for
  tasks where they require specialized knowledge. Agents may ignore
  skills for simple requests they can handle unaided — even when the
  description semantically matches — unless you explicitly invoke the
  skill.

- **Effective instruction patterns:**
  - *Give the agent freedom* when multiple approaches are valid.
    Explaining _why_ is often more effective than specifying exact
    steps.
  - *Be prescriptive* when operations are fragile, consistency is
    critical, or a specific sequence must be followed.
  - *Provide defaults, not menus.* Pick one default and mention
    alternatives as escape hatches.
  - *Favor procedures over declarations.* Teach the agent _how to
    approach_ a class of problems, not what to produce for a specific
    instance.
  - *Step-by-step instructions.* For multi-step workflows, an explicit
    `- [ ] Step N` checklist helps the agent track progress and avoid
    skipping steps.
  - *Output format templates.* Provide a concrete template rather than
    a prose description; agents pattern-match against structure more
    reliably.
  - *Validation loops.* Instruct the agent to run a validator after
    completing work, fix failures, and repeat until validation passes.
  - *Plan-validate-execute.* For batch or destructive operations, have
    the agent produce an intermediate plan, validate against a source
    of truth, and only then execute. The key is a validation step that
    produces error messages specific enough for the agent to
    self-correct.
  - *Bundle reusable scripts.* If the agent reinvents the same logic
    across runs, write it once as a tested script in `scripts/` and
    reference it.
  - *Gotchas.* A dedicated section listing environment-specific facts
    that defy reasonable assumptions is often the highest-value content.
    Keep gotchas in `SKILL.md` itself — the agent needs them before
    encountering the situation. When an agent makes a mistake you
    correct, add the correction to the edge cases section.

- **Creating skills — two RECOMMENDED approaches:**
  - *Extract knowledge from a hands-on task.* Complete a real task with
    an agent, providing context, corrections, and preferences. Then
    crystallize that experience into a new skill.
  - *Synthesize from project artifacts.* Feed existing knowledge
    (internal docs, runbooks, style guides, API specs, code review
    comments, issue trackers, version control history, real-world
    failure cases) into an LLM and ask it to synthesize a skill.

  A skill synthesized from your team's actual incident reports will
  outperform one generated from a generic "best practices" article.

- **Have the agent draft its own skill** at the end of a session —
  distilling what it learned into a new or updated skill. Treat
  agent-drafted skills as a first draft, not a finished artifact.
  Models tend to over-specify; proofreading and editing down is where
  most of the value is added.

- **Progressive disclosure.** Once an agent activates a skill, the full
  body of `SKILL.md` loads into context. Keep `SKILL.md` under 500
  lines, and push extended material into three OPTIONAL directories
  (siblings of `SKILL.md`): `references/`, `assets/`, `scripts/`.
  - *References:* Documentation the agent reads only when needed. Link
    with an explicit trigger condition rather than a generic pointer.
  - *Assets:* Static resources (templates, images, data files).
  - *Scripts:* Executable code. Follow the script guidelines below.

- **Script guidelines (for the `scripts/` directory):**
  - **No interactive prompts.** All input MUST be supplied via CLI
    flags, environment variables, or stdin — a script that blocks on
    input will hang indefinitely in a non-interactive shell.
  - **`--help` as the interface.** Keep it concise (it enters the
    context window) and cover description, all flags, and a usage
    example.
  - **Self-contained dependencies.** Use PEP 723 inline metadata (with
    `uv run`), Deno, or Bun inline specifiers where possible. Where a
    script can't be self-contained, document its dependencies at the
    top of the file.
  - **One-off commands.** For simple tasks, `uvx`, `npx`, and `bunx`
    can invoke packages directly from `SKILL.md` without a `scripts/`
    directory. Pin versions for reproducibility.
  - **Stdout/stderr separation.** Structured output to stdout;
    progress, diagnostics, and warnings to stderr.
  - **Idempotency.** Scripts SHOULD be idempotent (agents may retry).
  - **Output size management.** Harnesses often truncate tool output
    past 10–30K characters. Scripts with large output SHOULD default to
    a summary view and support `--limit`/`--offset` or `--output FILE`.
  - Scripts MUST handle edge cases gracefully. Prefer a widely-
    supported language (Bash, Python, JavaScript).

- **Sharing skills publicly.** The
  [Agent Skills Directory](https://www.skills.sh/) (skills.sh) is the
  primary public registry. When designing a skill for public sharing:
  - Avoid project-specific assumptions. Shared skills must teach a
    pattern that transfers across projects.
  - Document prerequisites clearly via the `compatibility` field.
  - Provide working examples.
  - Keep skills current. Record `last_updated` in metadata and review
    shared skills whenever underlying tools or APIs change.

  Before publishing, validate configuration with the
  [`skills-ref`](https://github.com/agentskills/agentskills/tree/main/skills-ref)
  package.

### AI-assisted development workflows

- **There are two approaches to incorporating AI-based coding tools:**
  - **AI-assisted development workflows:** humans synchronously
    interact with AI tools to assist with current development
    challenges.
  - **Agentic workflows:** harnesses orchestrate one or more AI agents
    to perform development tasks with high autonomy, supporting
    asynchronous/parallel workflows. (Agentic workflows require
    additional guardrails — see below.)

- **The most effective approach is to split complex tasks into
  distinct planning and implementation phases, matching model
  capabilities to each.** Use premium, frontier models for planning and
  architecture decisions, complex problem-solving, security analysis,
  and architectural compliance. Use cheap, efficient models for code
  construction from pre-approved plans, small-scale refactoring, and
  routine chores.

- **It is RECOMMENDED to follow this planning-implementation cycle for
  all but the simplest and quickest of tasks.**

#### Planning phase

- **Provide comprehensive context** including requirements, constraints,
  and existing architectural patterns.
- **Request structured, verifiable outputs** — diagrams, pseudocode, or
  API specifications.
- **Provide sufficient context in initial prompts** to minimize
  clarification rounds. Provide code examples as context to improve
  output quality.
- **Validate architectural decisions against project standards _before_
  implementing them.**
- **For large-scale or complex changes, document AI-assisted design
  decisions for team review before proceeding with implementation.**

#### Implementation phase

- **Provide clear, specific prompts based on pre-approved execution
  plans.**
- **Define coding standards, style guides, and architectural conventions
  as concise, reusable prompt inputs.**
- **Ask the AI to implement execution plans incrementally** — small,
  stable, independently-deployable increments. Easier to review and
  test than a single "big bang" changeset.
- **Small increments also bound the context window.** A session asked
  to plan, implement, and verify a large feature end-to-end will
  eventually suffer *context rot*. A session scoped to one small
  increment starts with a clean context window and loads only what
  that increment needs.
- **Batching similar tasks can help reduce token consumption, but do
  this sparingly.** Better to have a few smaller changesets than one
  large one to review.
- **Use version control to track changes to AI-generated code** and
  provide a robust "undo" operation. Avoid making manual and automated
  changes to code in the same revision.
- **When an agent gets stuck, avoid contaminating the context with
  irrelevant information.** Instead, ask directly: "What information do
  you need that would let you implement this perfectly right now?"

#### Testing phase

- **All normal developer review and approval processes MUST remain in
  place for AI-generated code.**
- **For every incremental step, conduct manual review** of the
  AI-generated code and verify adherence to coding standards and style
  guides. Manually test AI-generated code, as well as running automated
  tests and static analysis tools, before committing.
- **Do not rely on AI-generated tests to verify the correctness of
  AI-generated code.** Review all AI-generated tests — this is more
  important than reviewing AI-generated code.
- **Do not allow AI agents to modify your existing test suite without
  your explicit prompt and oversight.**
- **A test-driven approach to AI-assisted development is RECOMMENDED
  where feasible.** Write your own tests, then ask the AI to implement
  the changes necessary to make the tests pass.
- **Prefer high-level tests** (end-to-end system tests and integration
  tests) over unit tests alone. More robust and supports AI-assisted
  refactoring better.

#### Retrospective phase

- **After implementing a new feature or fixing a bug, ask the AI to
  update its own knowledgebase of the changes** — to maintain context
  for future AI coding sessions. Agents cannot reliably learn from
  experience across sessions unless learning is explicitly documented.
- **Best practice is to have an `AGENTS.md` file in the project root**,
  linked to all files that document context the agent should have
  access to: solutions to previously encountered problems, technical
  decisions and rationale, patterns that work well for your project,
  examples of correct implementations for common tasks.

### Agentic workflows

- **Agentic workflows are about using agents for _delegation_**, where
  the human shifts from primary implementer to supervisor. The agent is
  tasked with a high-level goal and empowered to manage its own
  internal loop — planning, executing, observing results, correcting
  course autonomously. The human intervenes to provide steering,
  constraints, and final approval. Interaction is more asynchronous.

  AI-assisted workflows are about _augmentation_ — the human remains
  the primary driver, using AI for specific sub-tasks. Interaction is
  synchronous.

- **Agentic versus automated:** Automation is deterministic, rules-based
  — ideal for repetitive, predictable tasks where the environment is
  stable. Agentic workflows are dynamic and reasoning-based — they
  handle ambiguity, adapt to unexpected outputs, and devise new
  strategies. Reserve agentic approaches for tasks involving genuine
  ambiguity, adaptive reasoning, or recovery from unexpected states.
  Agentic systems carry higher operational complexity and cost;
  traditional automation is preferable when the task is deterministic.

- **Computationally irreducible tasks MUST be delegated to a tool that
  executes the steps** (code interpreter, script, calculator) rather
  than left to a model to guess token-by-token. No model reliably
  shortcuts exact multi-step computation.

#### Agentic architectures

- **Single-agent systems** (`TASK → AGENT → SOLUTION`): A single agent
  handles the entire lifecycle — planning, execution, verification.
  RECOMMENDED starting point for most tasks with well-defined goals and
  limited scope.

- **Multi-agent systems** (`TASK → SUPERVISOR AGENT → SUB-AGENTS →
  SOLUTION`): A supervisor (orchestrator) decomposes the high-level task
  into specialized sub-tasks and delegates to sub-agents. The supervisor
  never sees the sub-agents' context but captures their responses,
  aggregates results, ensures cohesion, and verifies the outcome.
  Models real-world organizational structures and reduces the
  likelihood of a single agent becoming overwhelmed.

- **Upgrade from single-agent to multi-agent as a deliberate response
  to a specific limitation, not a default posture.** Reasons to
  upgrade:
  - *Context management:* Splitting work keeps each agent's context
    focused.
  - *Parallelism:* Independent sub-tasks execute concurrently.
  - *Specialization:* Different sub-tasks benefit from different models
    or tool access.
  - *Fault isolation:* A sub-agent that goes off track is contained;
    retried or discarded without corrupting the overall task.
  - *Independent verification:* An agent reviewing another's output
    needs fresh context to judge fairly rather than sycophantically.
  - *Reusability:* A well-scoped sub-agent becomes a composable unit
    other workflows can invoke.

#### Model tiering

- **Use a tiered model strategy.** A hybrid approach using a mix of
  frontier and efficient models is RECOMMENDED. Use frontier models
  for the supervisor role (complex planning, architectural decisions,
  high-level QA). Use smaller, faster, or locally-hosted models for
  sub-agents that execute pre-approved plans.

#### Guides and sensors

- **Guardrails are critical in agentic workflows** (where humans are
  less in the loop). Two categories of control:
  - **Guides** (feed-forward, steer _before_ acting):
    - *Behavioral instructions* (advisory): Rules in system prompts,
      `AGENTS.md`, skills, etc. — direct how the agent should approach
      tasks.
    - *Permission constraints* (enforced): Explicit allow/deny lists
      controlling which tools, shell commands, file paths, or network
      endpoints an agent may access — configured in the harness, not
      relied on via context/prompts. The most reliable form of guide
      because enforced by the runtime.
  - **Sensors** (feedback, check _after_ acting): Validation gates an
    agent must satisfy before proceeding — eg. running tests before
    committing, or requesting human approval before irreversible
    actions. Work best distributed across every step of the pipeline,
    not concentrated in a single end gate.
    - *Deterministic sensors:* Scripts/tools giving the same verdict on
      the same input (linters, type checkers, tests). Strongest signal.
      Wherever a rule is mechanically checkable, prefer enforcing it
      with a deterministic sensor over stating it as guidance.
    - *Inferential sensors:* A second agent judging the output of the
      first. Bring a fresh perspective but MUST NOT be treated as a
      substitute for deterministic checks — their judgment is
      probabilistic.

- **A good harness consists of a mix of both guides and sensors, and
  both deterministic and inferential kinds.** An agent steered only by
  guides repeats the same undetected mistakes. An agent checked only
  by sensors runs an expensive trial-and-error loop with no steering.

- **Where an inferential sensor is used, the reviewing agent MUST NOT
  be the same agent, in the same session, that produced the output.**
  Models exhibit sycophancy. Invoke inferential sensors as distinct
  sessions, and frame the evaluating agent adversarially — instructed
  to assume the work is broken and verify that claim, rather than to
  assume it is correct and check for obvious problems.

#### Guarding against agent loops

- **A recurring failure mode is the agent loop:** an agent gets stuck
  repeating the same action without progress, burning tokens and time
  until it exhausts its context window. Guard against this with both a
  hard guide and a soft guide, working together:
  - **Tool quotas (enforced):** A hard cap, configured in the harness,
    on how many times a given tool may be called within an agent run.
    A reliable backstop regardless of what the model does.
  - **Budget awareness (advisory):** A behavioral instruction telling
    the agent what quotas apply (eg. "you have 15 web searches
    available"). An agent that knows its budget can plan and ration its
    tool use.

  Hard quotas alone are not enough (an agent that doesn't know its
  budget cannot plan around it). Soft budgets alone are not enough
  (advisory limits can be ignored or miscounted). The two layers
  address different failure modes and SHOULD be used together.

- **Start with the minimum constraints necessary and add guides only in
  response to observed failure modes.** Guides SHOULD be reviewed when
  switching model versions — one written to correct a failure mode in
  an older model may become unnecessary or counterproductive.

#### Composable pipelines

- **An effective agentic workflow is a pipeline of agentic steps plus
  scripted steps, each narrowly scoped, where the output of one step is
  the input to the next.** Agentic steps do the reasoning-heavy work;
  scripted steps (deterministic sensors) catch failure modes and feed
  back to an earlier step or escalate to a human.

- **Work can enter at different points** depending on what triggered it:
  proactive (new requirements), reactive (bugs/incidents), or scheduled
  (periodic audits). Individual steps SHOULD be composable so they can
  be sequenced differently into different workflows.

- **Each step needs to be a small, sharp tool with well-defined input
  and output.** Rather than steps explicitly handing off to other
  steps (which produces tight coupling), the input/output becomes the
  contract between steps. The orchestrator determines the order.

#### Persistence

- **For one step to hand off to the next, the step's output MUST be
  persisted to a durable store, not merely held in the conversation.**
  An agent that finishes a planning step and writes its decisions to a
  plan document has produced something the next agent, in a fresh
  session, can read and act on. Persisting output to disk also keeps
  the context window clean.

- **A version control system like Git is the preferred substrate for
  this persistence layer.** Artifacts (requirements, decisions, designs,
  plans) can be persisted the same way as code — branched, committed,
  reviewed, merged with the same workflow, with durability, diff-
  ability, and an audit trail for free. Existing automation (CI)
  integrates easily.

#### Isolated environments

- **Wherever a workflow runs multiple agents or scripts against a
  single repository at once, each MUST be given its own isolated
  working copy of the repository.** Two processes writing to the same
  working tree concurrently may corrupt each other's work (build
  artifacts, lockfiles may collide).

- **A Git worktree** — a second working directory checked out from the
  same repository, on its own branch, without the overhead of a full
  clone — is the appropriate mechanism. It lets an orchestrator give
  each parallel agent its own isolated copy, reconciling branches only
  at integration time.

- **CI systems typically provide isolation already** by cloning the
  repository fresh into an ephemeral environment for every job. Whether
  isolation is needed, and which mechanism provides it, is a decision
  for whoever is orchestrating the workflow.

### Evaluation

- **Evals (evaluations) are structured tests that measure how well an
  LLM, agent, skill, prompt, or AI-assisted workflow performs on a
  defined set of tasks.** They are the AI equivalent of unit and
  regression tests, and the most important — yet most often skipped —
  practice in building reliable AI systems.

- **Without evals, every change to your model, prompt, skill, or harness
  is made blind.** Evals answer: did a change actually improve
  outcomes, or quietly regress them?

- **Evals can be applied to any component:** model selection, context
  (prompts, skills, rules), harness configuration, and generated
  outputs (code, designs, documentation judged against acceptance
  criteria).

- **A test case has three parts:** a realistic input, a description of
  what success looks like, and any fixtures it needs.

- **Eval suites SHOULD live in version control alongside the code or
  prompts they exercise**, so the two evolve together. Start with a
  small suite covering most common and most failure-prone cases, and
  grow from real failures rather than speculation.

- **Beyond a handful of ad-hoc evals, it is RECOMMENDED to use an
  established eval framework** — such as
  [OpenAI Evals](https://github.com/openai/evals). For evaluating
  skills, Anthropic's
  [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
  skill automates much of the evaluation and iteration loop.

- **The central mechanism of evaluation is comparison.** Run the same
  eval in two configurations — with and without a change, or against
  the previous version — and look at the delta in pass rate, latency,
  and token cost. A change that does not move the pass rate is not
  earning its keep.

- **For mechanically verifiable properties** (regex matches, passing
  tests), make objective assertions. **For qualitative properties**
  (clarity, tone), use an LLM as the judge (the evaluating model MUST
  be run in a distinct session from the one that generated the output)
  or apply human judgment.

- **Avoid over-specifying assertions up front.** Observe what the
  system actually produces, then write checks against those outputs.
  Account for non-determinism by running several samples rather than
  asserting on a single exact output.

### Model Context Protocol

- **When connecting an agent to external tools or data, it is
  RECOMMENDED to use an open protocol, and specifically MCP**, rather
  than writing custom point-to-point integrations. Benefits:
  interoperability (any client works with any server), composability
  (one agent can draw on many servers), portability (integrations
  survive a change of harness or model), and reduced maintenance.

- **MCP is a client-server protocol.** An *MCP server* exposes tools
  and resources. An *MCP client* (typically an agent harness) connects
  to one or more MCP servers and uses their tools. A single client can
  connect to many servers at once.

- **Treat MCP servers as dependencies.** An MCP server is third-party
  code that runs with access to your tools, data, and actions. It MUST
  be treated with the same scrutiny as any other software dependency.
  A malicious or compromised MCP server could exfiltrate any data the
  agent can reach, and take any action its tools permit.
  - Prefer official or well-known MCP servers. Review the source of
    community-provided servers before connecting them.
  - Pin MCP server versions where possible, and review changes before
    upgrading.
  - Test unfamiliar MCP servers in an isolated environment before
    introducing them to regular workflows.

- **Apply least privilege at two levels:**
  - *Connection scope:* Connect only the MCP servers and tools the
    current task actually needs. Do not connect "just in case."
  - *Credential scope:* Scope each server's credentials to the minimum
    required (eg. read-only database access where writes are not
    needed).
  - Review connected servers and enabled tools before starting a task,
    not only when first configuring the harness.

- **Tool results are untrusted input.** Data returned by an MCP server
  is external content and a vector for indirect prompt injection. An
  agent cannot reliably distinguish data it should process from
  instructions it should follow. Therefore:
  - Treat all tool output as data, not instructions.
  - Prefer human confirmation before irreversible actions taken
    through MCP tools — especially when the agent has just processed
    external content.
  - Audit agent execution traces when tasks involve servers that fetch
    untrusted data.

- **Tool definitions are an attack surface.** An MCP server's tool
  definitions (names and descriptions) are injected into the context
  window and can steer the agent. Two attacks identified in 2025:
  - *Tool poisoning:* Embedding malicious instructions in a tool's
    description.
  - *Lookalike (shadowing) tools:* Tools whose names/descriptions
    impersonate a trusted tool, routing calls to the attacker's server.
  Mitigations:
  - Review an MCP server's tool definitions, not just its results,
    before connecting. Re-review after an upgrade (descriptions can
    change without observable behavior changes — this is why versions
    SHOULD be pinned).
  - Prefer official or well-known MCP servers. Be wary of connecting
    multiple servers whose tools share names or overlapping
    responsibilities.
  - Combined with least-privilege access, a poisoned or lookalike tool
    can still only reach what the agent's credentials and connected
    tools permit.

- **Transport and network exposure:**
  - Local MCP servers (over stdio) avoid network exposure entirely and
    SHOULD be preferred where the tool can run on the same host.
  - Remote MCP servers MUST authenticate their clients and MUST use
    encrypted transport. An unauthenticated MCP server MUST NOT be
    exposed on a public network interface.
  - Run MCP servers only while needed, rather than as always-on
    services.

- **Mind the context cost of connected servers.** Every connected MCP
  server injects its tool definitions into the context window,
  consuming tokens and attention budget on every inference call — not
  just when its tools are used. Indiscriminately connecting many
  servers degrades performance (context rot) and increases cost.

### Cost optimization

- **Most hosted model services are metered per token**, charging
  separately for input and output (output typically costs several times
  more than input). Reasoning ("thinking") tokens are treated as
  output. Cached input tokens, where supported, are billed at a steep
  discount (often roughly an order of magnitude cheaper than uncached
  input).

  ```
  cost = (input tokens × input price)
       + (cached input tokens × cached input price)
       + (output tokens × output price)
  ```

- **The overarching principle: spend tokens and model capability where
  they change the outcome, and economize everywhere else.**

- **Right-size the model.** The largest cost lever. Defaulting to the
  biggest model for every task is wasteful; defaulting to the cheapest
  is unreliable and may cost more due to rework. Use frontier models
  where their capability changes the result; cheaper, efficient models
  for everything else. In agentic workflows, reserve frontier models
  for the supervisor and delegate execution to efficient sub-agents.

- **Economize on context.** Every token in the context window is
  billed on every inference call and depletes the attention budget. The
  smallest high-signal context is both the most effective and the
  cheapest. Context engineering best practices are also cost-reducing:
  keep reusable context token-efficient, prefer just-in-time retrieval,
  prune stale context, use compaction on long-horizon tasks.

- **Exploit prompt caching.** Where supported, place stable content
  (system prompt, skills, large reference documents, codebase context)
  at the start of the prompt and variable content (user's current
  query) at the end. Keep that prefix byte-stable across calls — even a
  small edit near the top invalidates the cache for everything after
  it.

- **Control output and reasoning length.** Output and thinking tokens
  are the expensive ones. Set a sensible maximum output token cap
  (large enough to avoid truncation). Request concise or structured
  output where prose adds no value. Scale the reasoning/thinking budget
  to task complexity rather than defaulting to maximum.

- **Batch where latency allows.** Batching similar tasks amortizes
  shared context. Do this sparingly — the trade-off is large diffs to
  review. For high-volume, non-latency-sensitive work, asynchronous
  batch APIs are commonly offered at a significant discount and are
  RECOMMENDED for bulk jobs.

- **Choose cost-effective access.** A single gateway subscription
  (OpenRouter, Perplexity Pro) can be more economical than separate lab
  subscriptions, and lets you route each task to the cheapest adequate
  model. For high-volume, repetitive, or privacy-sensitive work,
  locally-run open-weight models eliminate per-token API costs entirely
  (marginal cost becomes hardware and electricity).

- **Measure before optimizing.** Cost decisions SHOULD be grounded in
  measurement. Track token consumption per task. When evaluating a
  skill, rule, or prompt change, measure the token-cost delta
  alongside the quality delta. Re-measure when switching models or
  model versions — relative pricing and token efficiency vary.

### Security

- **Apply the same security principles to AI tools as to any other
  development dependency.** AI tools introduce security considerations
  at several levels: the services that run models, the data submitted,
  the permissions granted to agents, and the code they produce.

#### Isolation

- **If possible, run AI models and tools in containers or virtual
  machines.** This provides an isolation boundary between models,
  files, runtime processes, and the host system.
- **Do not run containerized model services as root.**
- **Keep model services running only when actively needed.** Treat
  them as development dependencies, not always-on services.
- **For AI-assisted development in an IDE, it is RECOMMENDED to develop
  inside a [devcontainer](https://containers.dev/)** rather than
  directly on the host. Both the editor and the agent harness run
  inside the container, with project files bind-mounted.

#### Network exposure

- **Local model servers (such as Ollama) listen on `localhost` by
  default.** Do not change this unless remote access is explicitly
  required. Prefer binding to `127.0.0.1` (loopback only).
- **If LAN access is required, binding to `0.0.0.0` is necessary but
  MUST be protected with a local firewall rule.** Never expose model
  server ports on a public interface.
- **For remote access, use an SSH tunnel or VPN**, rather than
  exposing the service directly.

#### Model trust

- **Models are large binary files that encode learned behaviors.**
  Treat them with the same scrutiny as any third-party dependency.
- **Only download models from official or well-known repositories.**
  Do not use untrusted models to process sensitive data. Test
  unfamiliar models in an isolated environment before introducing them
  to regular workflows.

#### Data confidentiality

- **Be careful about submitting proprietary code, credentials, or
  sensitive data to public AI services.** Use enterprise AI solutions
  with appropriate data handling agreements for commercial projects.

#### Prompt injection

- **Prompt injection is an attack in which malicious instructions
  embedded in data cause an agent to take unintended actions.** Two
  forms:
  - *Direct injection:* A user or caller crafts input designed to
    override the agent's system prompt or behavioral instructions.
  - *Indirect injection:* The agent autonomously reads external content
    (file, web page, API response, code comment) that contains
    embedded instructions. Because the agent cannot reliably
    distinguish between data it is processing and instructions it should
    follow, such content can redirect behavior without the user's
    knowledge. More dangerous in agentic workflows, where the agent may
    encounter malicious content deep in an autonomous task chain.

- **Mitigations:**
  - Treat all external content as data, not instructions. Where
    possible, pass it in a clearly delimited structure that separates
    it from the system prompt.
  - Grant agents only the tool permissions they need for the current
    task. A compromised agent can still only do what its connected
    tools allow.
  - Prefer human confirmation before irreversible actions — file
    deletion, network requests, code execution — especially when the
    agent has processed external content.
  - Audit agent execution traces when tasks involve untrusted sources.

#### The lethal trifecta

- **Prompt injection becomes catastrophic when an agent simultaneously
  has all three of:** (1) access to private data, (2) exposure to
  untrusted content, (3) the ability to communicate externally. The
  underlying reason: an LLM cannot reliably distinguish between data it
  is meant to process and instructions it is meant to follow — both
  arrive as tokens in the same context. Untrusted content that looks
  like an instruction may be acted upon, reading private data and
  leaking it via the exfiltration channel.

- **The practical defense is to break the trifecta** rather than try to
  make prompt injection impossible (assume it will always be a risk).
  Do one of: withhold access to sensitive data; isolate the agent from
  untrusted input; or cut off external communication. Any one or two
  parts in isolation is comparatively safe; the co-occurrence of all
  three is the most dangerous.

#### Least-privilege tool access

- **Limit the blast radius by applying the principle of least privilege
  to tool permissions.** Grant read-only access where write access is
  not needed. Scope filesystem access to specific paths. Restrict shell
  access to allow-listed commands. Disable network egress entirely for
  agents that do not need it.
- **Review agent permissions before starting a task**, not just when
  configuring a harness for the first time. A permission set appropriate
  for one task may be excessive for the next.

#### Reviewing agent output

- **Keep tasks small.** Break work into small, reviewable steps rather
  than large, open-ended tasks. Small diffs are easier to review, and
  you catch problems early.
- **Treat agent output with the same scrutiny as a human contributor's
  changes.** Models are trained on enormous bodies of existing code,
  which includes code with vulnerabilities. Models are capable of
  reproducing insecure patterns — hardcoded credentials, injection
  sinks, insecure defaults, missing input validation — learned from
  training data.
- **Pay particular attention to areas that handle authentication,
  authorization, cryptography, external input, and similar sensitive
  concerns.**

## References

- [TS-61: AI Tools (source)](README.adoc)
- [TS-5: Application Architecture](../005/AGENTS.md)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-9: Version Control](../009/AGENTS.md)
- [TS-12: Quality Assurance](../012/AGENTS.md)
- [TS-13: Functional Testing](../013/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [TS-58: Docker](../058/AGENTS.md)
- [AGENTS.md specification](https://agents.md)
- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills Directory](https://www.skills.sh/)
- [Anthropic Engineering blog](https://www.anthropic.com/engineering)
- [Invariant Labs: MCP Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices)
- [Agent Skills: Optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)
- [Agent Skills: Evaluating skills](https://agentskills.io/skill-creation/evaluating-skills)
- [Agent Skills: Using scripts](https://agentskills.io/skill-creation/using-scripts)