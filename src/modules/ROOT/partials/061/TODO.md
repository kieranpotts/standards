# TS-61 deep dive

Findings from a deep review of TS-61: AI Tools

~2,350 lines (about 39,400 words) across 25 files.

Assessed against the repository [style guide](../../../../../docs/style-guide.md), [TS-26: Technical Writing Style Guide](../../pages/026.adoc), [TS-27: Markdown](../../pages/027.adoc), [TS-28: AsciiDoc](../../pages/028.adoc), and the [template](../../../../../template/).

**Assessment.** The sections on agentic workflows, skills, harness engineering, and loop engineering are sound, specific, and mostly consistent with each other, and every in-page cross-reference resolves to exactly one explicit anchor. The problems number 111. They concentrate in `04-ai-use-cases.adoc` and `05-benefits-and-costs.adoc`, which are written as an essay in a different voice from the rest and account for most of the convention and prose findings. Structural problems dominate in effect: the same material is stated up to four times, and six of the 12 contradictions are restatements that have drifted apart.

**Status:** Tiers 1 and 2 applied (sections 1 to 3). Tiers 3 and 4 are open. Two items in tier 4 still need a user decision, each marked **Decision needed**. Tier 2 left `GARDEN.md` in this directory, holding text cut from `04-ai-use-cases.adoc`, for you to move to the garden and delete.

## Priority order

1. **Correctness.** Contradictions and factual errors (sections 1 and 2). A reader cannot comply with a standard that says two incompatible things.

2. **Coherence.** Structural problems (section 3). Structure must settle before content is added to it.

3. **Completeness.** Coverage gaps (section 4). Filled into a structure that has stopped moving.

4. **Conventions.** Style-guide conformance and prose defects (sections 5 and 6). Last, because content edits invalidate cosmetic fixes made too early.

Every finding belongs to the tier of the section it sits in. No finding is assigned outside that mapping.

## Verification notes

Factual findings were checked against primary sources on 2026-10-09 where one could be reached.

- **Checked.** The Agent Skills specification (agentskills.io/specification), skills.sh, agents.md, the harness engineering article on martinfowler.com, and the hyper.ai page for the loop engineering paper.

- **Checked against secondary sources only.** The DORA 2024 and 2025 findings, and the formation of the Agentic AI Foundation. Confirm exact figures at dora.dev before citing them.

- **Not verifiable.** The BBC article behind `{link-mcmahon-2026}` could not be fetched, so every claim in `22-security.adoc:89-109` that rests on it is unverified. No source was found for the "27-fold" figure at `05-benefits-and-costs.adoc:41`.

## 1. Contradictions

- [x] `03-human-in-the-loop.adoc:46` says "There MUST always be a human-in-the-loop", but `04-ai-use-cases.adoc:102` defines an *automated* task as one with "no human checkpoint at all", and `16-loop-engineering.adoc:20` says a loop "removes the human from that inner cycle". A reader cannot tell whether an unattended loop is permitted. The term is never defined, so "in the loop" means an accountable human in one place and a per-run checkpoint in another. **Decision needed:** recommend defining the term in `03` as accountability plus a defined point of intervention, and rewording `04:102` and `16:20` to match, so that removing a per-run checkpoint is distinct from removing the human.

- [x] `04-ai-use-cases.adoc:59` says "a model essentially never answers 'I don't know'" and has "no reliable signal for its own uncertainty" (`04:47`), but `03-human-in-the-loop.adoc:32` says providers are "making genuine progress" on models that "express calibrated uncertainty, ask clarifying questions rather than guess", and `10-prompt-engineering.adoc:34` says frontier models ask "a clarifying question where the request is ambiguous rather than guessing". The absolute form in `04` is the outlier.

- [x] `07-choosing-models.adoc:59` lists *Reasoning* as a fourth capability tier beside Frontier, Mid-tier, and Light, but `09-tuning-model-behavior.adoc:60` says reasoning controls "are orthogonal both to temperature and to model tier". A tier cannot be orthogonal to the tiers.

- [x] `18-ai-assisted-workflows.adoc:5` says "Premium, specialist models tend to plan code changes better than cheaper, general-purpose models", but `07-choosing-models.adoc:42` says "A specialist model may be small and cheap" and `07:53` assigns planning to frontier models, which are general-purpose. "Specialist" is used in two opposed senses.

- [x] `02-definitions.adoc:72` and `19-agentic-workflows.adoc:139` define an *inferential* sensor as "a second agent tasked with judging the output of the first", but `15-harness-engineering.adoc:78` defines *inferential controls* as controls "written in ordinary prose — system prompts, `AGENTS.md`, skills". `19:143` then refers to guides "of both the deterministic and inferential kinds", a split that `19:121-125` names advisory and enforced instead. Two taxonomies share one word.

- [x] `18-ai-assisted-workflows.adoc:54` says "Do not rely on AI-generated tests to verify the correctness of AI-generated code", but `15-harness-engineering.adoc:86` says "LLMs are the fastest way to build a large library of such sensors". Nothing reconciles the two, such as a requirement that an LLM-authored sensor is human-reviewed before it gates anything.

- [x] `20-evaluation.adoc:42` says "A change that does not move the pass rate is not earning its keep", but `20:38` tells the reader to look at "the delta in pass rate, latency, and token cost", and `15-harness-engineering.adoc:96` accepts a change that "moves the pass rate, latency, or token cost". A change that halves cost at an equal pass rate fails the first rule and passes the other two.

- [x] `10-prompt-engineering.adoc:34` says "do not over-invest in upfront prompt design", but `18-ai-assisted-workflows.adoc:15` says "Put enough context in the initial prompt to minimize rounds of clarification", and `08-choosing-interfaces.adoc:41` requires up-front investment for asynchronous work. The standard never says that the first applies to interactive sessions and the others to unattended ones.

- [x] `18-ai-assisted-workflows.adoc:64-68` tells the reader to have the agent "update its own knowledgebase" after every change and to link "every file" of such context from `AGENTS.md`, but `12-reusable-context.adoc:12-18` says reusable context MUST be token-efficient, minimal, and pruned, and "Stale context is worse than no context". An ever-growing log linked from an always-loaded file is the pattern `12` warns against.

- [x] `16-loop-engineering.adoc:20` says loop engineering "is the fourth layer above harness engineering", but the stack in `06-ai-engineering-stack.adoc:11-16` has it as the fourth layer above the model and the layer directly above harness engineering.

- [x] `08-choosing-interfaces.adoc:58` says harness engineering "is the subject of the next section", but the next section is `09-tuning-model-behavior.adoc` and harness engineering is five sections later. `15-harness-engineering.adoc:118` likewise calls `08` "the previous section", and `05-benefits-and-costs.adoc:4` and `18-ai-assisted-workflows.adoc:3` use the same device. The prose describes an ordering the document does not have.

- [x] `01-introduction.adoc:5` says the scope "runs from choosing a model and an interface, through harness and context engineering and the design of AI-assisted and agentic workflows, to evaluation", but the includes in `pages/061.adoc:6-25` put workflows (`18`, `19`) before model and interface choice (`07`, `08`), and context engineering before harness engineering.

## 2. Factual errors

- [x] `13-agent-skills.adoc:99` claims the `name` field "SHOULD match the parent directory name, though the standard does not require it". The specification says the name "Must match the parent directory name". It also forbids a leading, trailing, or consecutive hyphen, which the standard omits (agentskills.io/specification). **Done.** Fixed: the name field MUST match the parent directory and MUST NOT start, end, or double a hyphen.

- [x] `13-agent-skills.adoc:69` claims "The formal specification defines the discovery path as `.agents/skills/`". The specification page defines no discovery path. If the path comes from another page of the Agent Skills documentation, cite that page. Otherwise describe it as a convention. **Done.** Fixed: now says the specification defines no discovery path and calls `.agents/skills/` an emerging convention. I did not find a primary page that defines it, so no citation was added.

- [x] `13-agent-skills.adoc:369` gives the install command as `npx skillsadd <owner/repo>`. The command is `npx skills add <owner/repo>`. The skills.sh home page renders it without the space, which is the likely origin of the error. **Done.** Fixed: `npx skills add`.

- [x] `13-agent-skills.adoc:125` gives `allowed-tools: Bash(git:*) Zsh(git:*)` as an example. `Zsh` is not a tool name in any harness the standard names. The specification's own example is `Bash(git:*) Bash(jq:*) Read`. **Done.** Fixed: example now `Bash(git:*) Bash(jq:*) Read`.

- [x] `13-agent-skills.adoc:308` gives the shebang `#!/bin/env sh` in the script template. `env` is at `/usr/bin/env` on Linux and macOS, so the template script fails to start on most systems. **Done.** Fixed: `#!/usr/bin/env sh`.

- [x] `04-ai-use-cases.adoc:61` claims a model "trained to stay close to the statistical patterns in its training data is *overfitted*" and that sampling randomness "is one of the countermeasures". Overfitting is a training-time failure to generalize, and it is addressed in training. Sampling temperature is an inference-time control on output diversity and does not change how well a model generalizes. `09-tuning-model-behavior.adoc:53` repeats the claim that sampling "is what lets a model generalize past its training data". **Done.** Fixed in `04`: overfitting is now described as a training-time defect, and sampling as an inference-time control on variety. Also fixed the repeat in `09-tuning-model-behavior.adoc`.

- [x] `14-model-context-protocol.adoc:14` calls Google's A2A "an alternative" to MCP. A2A connects agents to each other and MCP connects an agent to tools, as the same sentence concedes. They are complementary, and both are now Linux Foundation projects. **Done.** Fixed: A2A is described as complementary, and a Linux Foundation project.

- [x] `14-model-context-protocol.adoc:6` and `02-definitions.adoc:46` describe MCP as an Anthropic protocol and an "emerging" standard. MCP was donated to the Agentic AI Foundation under the Linux Foundation in December 2025. The governance matters to a reader weighing lock-in. **Done.** Fixed: MCP's donation to the Agentic AI Foundation is stated in `14`, and `02` now says "open" rather than "emerging". The donation date comes from this plan's own notes and was not re-checked at a primary source.

- [x] `12-reusable-context.adoc:36` says `AGENTS.md` "was jointly launched by Google, OpenAI, Factory, Sourcegraph, and Cursor". This is accurate as history, but it omits that the convention is now stewarded by the Agentic AI Foundation (agents.md). **Done.** Fixed: stewardship by the Agentic AI Foundation added.

- [x] `12-reusable-context.adoc:42` claims "Claude Code also supports it alongside `CLAUDE.md`". Claude Code is not on the agents.md list of supporting tools, and this repository's own `CLAUDE.md` is a one-line `@AGENTS.md` import, which would be unnecessary if the claim were true. The list of supporting tools in the same paragraph has also drifted from the agents.md list. Verify against the Claude Code documentation. **Done.** Fixed: confirmed against agents.md that Claude Code is not listed. Replaced the claim with a note that it reads `CLAUDE.md`, and that `@AGENTS.md` imports the shared file. Supporting-tool list replaced with names from agents.md. The Claude Code documentation itself was not consulted.

- [x] `05-benefits-and-costs.adoc:60` claims DORA's 2024 research found "an estimated 1.5% decrease in delivery throughput and a 7.2% reduction in delivery stability". The figures are per 25% increase in AI adoption, which the sentence drops. The 2025 report found the throughput association had turned positive while stability stayed negative, so the bullet's heading, "Delivery throughput and stability decline", is out of date for throughput. **Done.** Fixed: the "per 25% increase in AI adoption" qualifier added, the 2025 reversal on throughput added, the bullet retitled "Delivery stability declines", and DORA expanded (this also closes the section 5 abbreviation item). The 2025 detail is from secondary sources, so confirm at dora.dev.

- [x] `05-benefits-and-costs.adoc:60` says "See xref:012.adoc[TS-12] for how delivery stability is measured". TS-12 (Quality Assurance) contains no mention of delivery stability, DORA, or change failure rate. The reference promises content that does not exist. **Done.** Fixed: removed the sentence. No standard here covers delivery stability (grep found none), so the promised content is a coverage gap, not recorded separately.

- [x] `05-benefits-and-costs.adoc:41` claims "one recent study found the productivity gap between developers in the top and bottom quartiles by some measures of code quality is now as much as 27-fold". No source for this figure could be found. Cite it or remove it. **Done.** Fixed: removed the unsourced 27-fold clause, and kept the surrounding claim, which no longer rests on a figure.

- [x] `22-security.adoc:89` dates the OpenAI sandbox incident to "In 2025", but the only source is cited as McMahon, 2026, and `22:91` says the other incidents followed "Within the following month". The article could not be fetched. Confirm the year against the source. **Done.** Partly fixed: the BBC article cannot be fetched from here, so the year could not be confirmed. "In 2025" is now "In an incident reported in 2026", which is what the citation supports. Confirm manually.

- [x] `99-references.adoc:7` attributes _Harness Engineering_ to "Fowler, M." with no year. The article is "Harness engineering for coding agent users" by Birgitta Böckeler, published on martinfowler.com on 2026-04-02. The article's terms are also "computational" and "inferential", where the standard says "deterministic" and "inferential" (`15-harness-engineering.adoc:74-88`). **Done.** Fixed: attributed to Böckeler (2026) with the real title, attribute renamed `link-bockeler-2026`, and `15-harness-engineering.adoc` now notes the article's "computational" term.

- [x] `00-attributes.adoc:8` names the loop engineering link `Loop-Engineering-IEEE`, and the paper is hosted on hyper.ai. The page names no venue and does not confirm IEEE publication. Do not imply IEEE provenance unless a primary record of it exists. **Done.** No change needed: `Loop-Engineering-IEEE` is the literal URL slug on hyper.ai, not a claim made by the standard, and no "IEEE" appears in the body text. It cannot be renamed without breaking the link.

- [x] `02-definitions.adoc:38` defines a coding agent as one that "uses models trained specifically for computer programming tasks", and `07-choosing-models.adoc:10` describes "coding-flavored LLMs" produced by fine-tuning. The harnesses the standard names (Claude Code, Codex, OpenCode, Pi) run general-purpose frontier models. `07-choosing-models.adoc:53` itself lists those models as the frontier tier. **Done.** Fixed in `02` and `07`: coding agents use general-purpose frontier models, possibly fine-tuned.

- [x] `21-cost-optimization.adoc:72` gives Perplexity Pro as an example of "A single gateway subscription" that "lets you route each task to the cheapest model adequate for it". Perplexity Pro is a consumer subscription to a search product, not an inference gateway. **Done.** Fixed: Perplexity Pro removed from the example.

- [x] `04-ai-use-cases.adoc:24` says agent-level unreliability "never will" change, and `04:18` says a model "has no processes to reflect on". Both are stated as settled fact. Neither is checkable, and the second is contested by published interpretability research. A standard cannot require a reader to accept a prediction. Restate both as the current position, as `03-human-in-the-loop.adoc:6` does with "at least in their 2026 frontier form". **Done.** Fixed: "never will" now "at least with the frontier models of 2026", and the "no processes to reflect on" claim restated as an inability to report reliably on its own processes.

- [x] `11-context-engineering.adoc:29` says compaction techniques "accentuate" context rot. Compaction reduces the context, which mitigates context rot at the cost of losing detail, as `11:94-98` says. `11:73` also says few-shot examples "train agents", but examples in context do not train anything, as `02-definitions.adoc:18` makes clear. **Done.** Fixed: compaction "mitigates" context rot, and few-shot examples "teach agents, within a single session" instead of training them.

## 3. Structural problems

- [x] `04-ai-use-cases.adoc:6-38` ("The inherent nature of the technology") is about 4,000 words in 16 paragraphs of up to 342 words each, covering the Turing test, consumer-choice economics, moral judgment studies, and the Alternative Uses Test. `AGENTS.md` describes the standards as "reference material, not tutorials". The section states one rule (verify, do not trust) at least eight times. **Decision needed:** recommend cutting it to the three properties and their consequences, in roughly a quarter of the length, and moving the essay material to the garden. **Done.** Decision (user): cut. The section is now about 800 words in three properties, a consequences subsection, and a short "where the technology shines" subsection (the plan's 4,000-word estimate was high; the original was about 2,700 words). The Turing test, consumer-choice, moral-judgment, noughts-and-crosses and "human-likeness" paragraphs are saved verbatim in `GARDEN.md` for you to move to the garden. Delete that file once done. The `the-inherent-nature-of-the-technology` anchor is kept.

- [x] `04-ai-use-cases.adoc:40-65` ("Hallucination") repeats `02-definitions.adoc:22` almost word for word, including its MUST NOT, and the same rule appears again at `04:22`, `04:57`, `04:154`, and `22-security.adoc:144`. One normative statement with cross-references would serve. **Done.** The single normative statement now lives in `04-ai-use-cases.adoc` under "Hallucination". `02-definitions.adoc` is a definition with a pointer, and `22-security.adoc` cross-references it. The cut of the "inherent nature" section removed the other repeats, though its "Consequences" paragraph still states the related rule that correctness must be established by something that does not share the model's flaws.

- [x] Model tiering is stated in full four times: `18-ai-assisted-workflows.adoc:5-7`, `19-agentic-workflows.adoc:90-112`, `07-choosing-models.adoc:46-63`, and `21-cost-optimization.adoc:20-26`. The lists of what frontier models are for differ slightly in each. Keep the rule in `07` and reference it. **Done.** The rule is stated once, in `07-choosing-models.adoc` under "Assigning tiers to workflow roles" (`[#tiers-in-a-workflow]`). `18-ai-assisted-workflows.adoc`, `19-agentic-workflows.adoc` (which keeps its diagram) and `21-cost-optimization.adoc` reference it. The task lists differed in two places, and I merged them (the union is in `07`, including architectural compliance review).

- [x] The guides and sensors taxonomy is defined three times: `02-definitions.adoc:70-74`, `19-agentic-workflows.adoc:114-147`, and `15-harness-engineering.adoc:53-88`. The third has drifted (see section 1). Keep one definition. **Done.** The definition lives in `15-harness-engineering.adoc` under "Guides and sensors" (`[#guides-and-sensors]`), beside the existing "Inferential and deterministic controls" subsection. `19-agentic-workflows.adoc` keeps only workflow practice, under "Sensors in the pipeline" (`[#sensors-in-the-pipeline]`). `02-definitions.adoc` keeps terse glossary entries with a pointer, and its normative "MUST NOT substitute" was removed (`15` and `19` carry that rule).

- [x] `02-definitions.adoc:80` and `17-ways-of-working-with-ai.adoc:6-10` define the vibe coding, AI-assisted, and agentic triad in the same words. `02-definitions.adoc:58-62` likewise duplicates the openings of `11`, `15`, and `16`. **Done.** Per the decision on the glossary item below, only the duplicates were removed. The triad entry is now a pointer to `17-ways-of-working-with-ai.adoc`, and the prompt, context, harness and loop engineering entries are one compact entry pointing to the stack in `06-ai-engineering-stack.adoc`.

- [x] `05-benefits-and-costs.adoc:41` restates the "AI-augmented software development" paragraph of `03-human-in-the-loop.adoc:39` nearly verbatim, and `05:37` restates the "thinking companion" passage of `04-ai-use-cases.adoc:88-90`. **Done.** The "thinking companion" passage is cut to one sentence plus a pointer, and the augmentation paragraph's restatement of the objective now points to `03-human-in-the-loop.adoc`.

- [x] The five-layer stack diagram is drawn five times: `06-ai-engineering-stack.adoc:8-19`, `09-tuning-model-behavior.adoc:4-17`, `11-context-engineering.adoc:4-17`, `15-harness-engineering.adoc:4-17`, and `16-loop-engineering.adoc:3-16`. The base node is labeled "Model selection" in the first and "Model" in the others. **Done.** The diagram remains only in `06-ai-engineering-stack.adoc`. `09`, `11`, `15` and `16` open with one sentence pointing to it, and the base-label mismatch no longer applies.

- [x] `pages/061.adoc:8-9` places the workflow sections (`18`, `19`) before the sections that define what they depend on: capability tiers (`07`), context rot (`11`), and the stack (`06`). `18-ai-assisted-workflows.adoc:30` has to explain context rot inline as a result. **Decision needed:** recommend the order foundations (`04`, `05`), stack and choices (`06` to `09`), context (`10` to `13`, `14`), harness and loop (`15`, `16`), workflows (`17` to `19`), then evaluation, cost, and security. This requires renumbering with `git mv`. **Done.** Decision (user): reorder as recommended. New order: `04` use cases, `05` benefits and costs, `06` stack, `07` models, `08` interfaces, `09` tuning, `10` prompts, `11` context, `12` reusable context, `13` skills, `14` MCP, `15` harness, `16` loop, `17` ways of working, `18` AI-assisted workflows, `19` agentic workflows, `20` evaluation, `21` cost, `22` security. Files were renamed with `git mv` through temporary names, since the mapping is a permutation with no free slot. `pages/061.adoc` includes were rebuilt, `01-introduction.adoc` scope sentence reordered to match, three ordering phrases in the prose adjusted, and this file's file references were remapped. Every `<<xref>>` resolves to exactly one explicit anchor.

- [x] `06-ai-engineering-stack.adoc` presents a five-layer stack as the organizing frame, but seven sections have no place in it: `10` (prompt engineering), `12` (reusable context), `13` (agent skills), `20` (evaluation), `14` (MCP), `21` (cost), and `22` (security). `13` and `14` are the two longest practical sections. Either show where they sit or drop the claim at `06:31` that the rest of the standard "works through the whole toolchain in turn". **Done.** Rather than dropping the claim, the closing paragraph now says where each section sits: models and interfaces at the base, prompts, reusable context, skills and MCP within context engineering, and evaluation, cost and security across all layers. Added anchors `ai-engineering-stack`, `choosing-interfaces`, `security`, `prompt-engineering` (this closes part of the tier 4 anchor item).

- [x] `10-prompt-engineering.adoc:2` is titled "Prompt engineering: roles and personas" and covers only personas, while general prompt guidance sits under "System prompts" at `11-context-engineering.adoc:43-65`. The vagueness test at `11:65` is about a user's prompt, not a system prompt. Planning-prompt advice is also in `18-ai-assisted-workflows.adoc:13-15`. **Done.** `10-prompt-engineering.adoc` is now "Prompt engineering", with "Writing effective prompts" (moved from `11-context-engineering.adoc`) ahead of "Roles and personas" (old anchor kept). The planning-prompt advice in `18-ai-assisted-workflows.adoc` stays, because it is workflow-specific, and now points to `10`. The vagueness test was moved unchanged, so its pass/fail wording is still open under section 6.

- [x] `02-definitions.adoc` is a 2,700-word glossary of 39 terms in undifferentiated bullets, each up to 160 words, with a `TODO` at `02:4` to move it to the garden. Eleven terms already link to garden entries. Several bullets carry normative rules (`02:22`, `02:72`) that a reader would not look for in a glossary. **Decision needed:** recommend keeping one-sentence definitions here, in a description list as TS-28 prescribes for glossaries, and moving the rest to the sections that own each term. **Done, no restructuring.** Decision (user): leave the long entries. Only the duplicated entries were de-duplicated (see the two items above and the hallucination entry). The `TODO` comment at the top of `02-definitions.adoc` is untouched and remains in the tier 4 comment item.

- [x] `22-security.adoc:85-109` ("Testing autonomous agents") is 700 words of narrative about red-teaming frontier models, resting on one news article. The standard's stated audience at `01-introduction.adoc:7` uses AI tools to build software and does not evaluate model containment. **Decision needed:** recommend reducing it to the bulleted guidance at `22:97-107`, or moving it to the garden. **Done.** Decision (user): reduce to the bullets. The narrative and all six McMahon citations are gone, and the bullets are kept with the citations and the one-hour claim removed. With no remaining citation, the McMahon entry in `99-references.adoc` and its attribute were removed. This also dissolves the McMahon items in section 5 and the unverified claims noted at the top of this file.

- [x] `22-security.adoc:111-146` ("Goals without judgment") sits between "Testing autonomous agents" and "Least-privilege tool access", but its rules at `22:138-146` are authorization rules that depend on least privilege, which is defined after it at `22:148`. **Done.** "Goals without judgment" now follows "Least-privilege tool access". One sentence that depended on the removed incident narrative was replaced, and the hallucination cross-reference now points to `04-ai-use-cases.adoc`.

- [x] `19-agentic-workflows.adoc:164-168` discusses relaxing prescriptive guides as models improve, under the heading "Guarding against runaway loops". It belongs with "Guides and sensors" at `19:114`, or with "Evolving the harness" at `15-harness-engineering.adoc:90`, which says the same thing. **Done.** Deleted from the runaway-loops section. "Evolving the harness" in `15-harness-engineering.adoc` already says the same thing, so no text was moved.

- [x] `04-ai-use-cases.adoc:96-102` ("Delegated versus automated tasks") defines degrees of human involvement, which is the subject of `03-human-in-the-loop.adoc:43-56`. It also uses "automated" for a model acting unchecked, while `19-agentic-workflows.adoc:30-49` uses "automated" for deterministic scripts. **Done.** Moved to `03-human-in-the-loop.adoc` as "Delegated versus unattended tasks". The model-driven no-checkpoint case is renamed *unattended*, which also matches `03`'s existing wording, and the section says that *automated* is reserved for deterministic scripts.

- [x] `07-choosing-models.adoc:85-90` ("When not to use a model at all") is a two-sentence stub pointing at `19-agentic-workflows.adoc:30`, and `04-ai-use-cases.adoc:152` makes the same point a third time. **Done.** Removed. The point is made in `04-ai-use-cases.adoc` ("When not to use AI") and `19-agentic-workflows.adoc` ("Agentic versus automated"), and nothing referenced the removed anchor.

- [x] `08-choosing-interfaces.adoc:15-21` lists three Google products for design, marketing, and research. `01-introduction.adoc:7` scopes the standard to software development. **Done.** The three Google products were removed, leaving the sentence that equivalent tools exist outside software development.

## 4. Coverage gaps

- [ ] Evaluation is cited from about ten sections as the way to justify any change, but `20-evaluation.adoc` is 460 words. It does not cover grader types, how many samples a comparison needs, calibrating an LLM judge against human labels, evaluating a trajectory as against an outcome, held-out cases, or running evals in CI. Recommend expanding `20-evaluation.adoc:22-46`.

- [ ] Data confidentiality is two sentences at `22-security.adoc:37-39`, though `04-ai-use-cases.adoc:164`, `05-benefits-and-costs.adoc:48`, and `07-choosing-models.adoc:74` all defer to it as the control. A reader needs to know what to check: provider retention and training terms, zero-retention options, data residency, and which classes of data may go to which class of service. Recommend expanding at `22-security.adoc:37` and referencing TS-53.

- [ ] Nothing covers secrets reaching a model's context. An agent with file and shell access reads `.env` files, credential stores, and environment variables unless denied. Recommend placing at `22-security.adoc:148` under least-privilege tool access, with a reference to TS-52.

- [ ] Nothing covers skills as a supply-chain risk. `13-agent-skills.adoc:367-381` recommends installing public skills, and `13:226` says skills carry scripts "the agent is allowed to run", but only MCP servers get the dependency treatment (`14-model-context-protocol.adoc:16-24`). The same applies to rules files and plugins. Recommend placing after `13-agent-skills.adoc:381` and in `22-security.adoc`.

- [ ] Nothing covers hallucinated dependencies. A model can name a package that does not exist, and attackers register such names. `04-ai-use-cases.adoc:43` mentions "non-existent APIs" as an example but states no rule. Recommend placing at `22-security.adoc:157` under reviewing agent output.

- [ ] Nothing covers approval modes. Every harness the standard names has a mode that skips permission prompts, and `22-security.adoc:148-155` does not say when it may be used. Recommend a rule tying unattended approval to sandboxing and the lethal trifecta, at `22-security.adoc:148`.

- [ ] `22-security.adoc:9-17` recommends containers and devcontainers but does not say what they do not isolate: a bind-mounted project, forwarded SSH agents and Git credentials, and unrestricted network egress. A reader could take a devcontainer as breaking the lethal trifecta when it breaks none of the three legs.

- [ ] `17-ways-of-working-with-ai.adoc:29` says AI-assisted development "scales to the volume of code that can be reviewed, and no further", and `05-benefits-and-costs.adoc:60` names batch size as the cause of instability. Nothing says what to do about review load: batch-size limits, who may approve AI-authored changes, or how review differs for them. Recommend placing at `18-ai-assisted-workflows.adoc:48`.

- [ ] Nothing covers team policy. A reader adopting the standard needs rules on which tools are approved, whether AI authorship is disclosed in commits and pull requests, and who is accountable for an agent's change. `03-human-in-the-loop.adoc:28` asserts accountability but assigns it to no one. Recommend a short section after `05-benefits-and-costs.adoc`.

- [ ] Specification-driven development is named as "The long-term goal" at `19-agentic-workflows.adoc:28` and as an industry movement at `13-agent-skills.adoc:65`, but it is never described. A reader is told where the practice is heading and not how to do it. Recommend placing at `19-agentic-workflows.adoc:262` with success criteria.

- [ ] `21-cost-optimization.adoc:4-16` models cost as per-token billing only. Most developers pay for harnesses through flat-rate subscriptions with usage limits, which changes the optimization. The section also omits that cache writes cost more than uncached input and that a cache entry expires, both of which decide whether caching pays. `21:16` mentions "a multiplier" without saying which providers or why.

- [ ] `14-model-context-protocol.adoc:66-72` requires remote servers to authenticate clients but names no mechanism, though the protocol specifies one. `14:74-78` states the context cost of connected servers and offers no mitigation beyond connecting fewer. The section also gives no guidance on choosing between an MCP server, a skill with a script, and a plain CLI tool, which `11-context-engineering.adoc:67-75` and `13-agent-skills.adoc:226-242` each cover without reference to the others.

- [ ] `09-tuning-model-behavior.adoc:28-55` gives temperature ranges without saying that several current reasoning models fix or ignore sampling parameters when thinking is enabled. `09:23` covers harnesses fixing them but not providers.

- [ ] Nothing covers observability of agent runs beyond the transcript. `22-security.adoc:167-186` covers audit, and `21-cost-optimization.adoc:80` mentions usage data, but there is no guidance on tracing or metrics for agentic workflows and loops. Recommend a reference to TS-57 from `16-loop-engineering.adoc:71`.

- [ ] `01-introduction.adoc` links to no related standard. The style guide says the introduction SHOULD. Candidates are TS-9 (Version Control), TS-12 (Quality Assurance), TS-13 (Functional Testing), TS-52 (Security and Secrets Management), TS-53 (Privacy and Data Protection), TS-54 (Threat Modeling), and TS-57 (Logging, Monitoring, Observability). The body references only TS-12, once.

- [ ] The standard has no summary of its normative requirements. It contains about 115 RFC 2119 keywords spread through 39,000 words, so a reader cannot find what compliance requires without reading all of it. Recommend a checklist section before `99-references.adoc`.

## 5. Convention conformance

- [ ] Empirical claims are credited to unnamed authorities, which TS-26 (Attributions) prohibits: `04-ai-use-cases.adoc:32` ("Studies now find", "Studies in moral judgment and in game theory report"), `04:92` ("Some early reporting has even suggested"), `05-benefits-and-costs.adoc:41` ("Early academic research", "one recent study"), `05:58` ("Studies have repeatedly shown"), `08-choosing-interfaces.adoc:5` ("Recent research suggests"), `20-evaluation.adoc:4` ("widely cited"), and `14-model-context-protocol.adoc:52` ("Security research published in 2025"). The last has its source in the references list (Invariant Labs) but does not cite it.

- [ ] `99-references.adoc:3-19` lists nine works, and only McMahon is cited in the body. TS-26 (Citations) pairs each reference with a Harvard inline citation. Sources the body does rely on are missing from the list: DORA (`05-benefits-and-costs.adoc:60`), Willison (`22-security.adoc:65`), Gosling (`22:116`), Turing (`04-ai-use-cases.adoc:36`), and the Agent Skills and AGENTS.md specifications (`13-agent-skills.adoc:8`, `12-reusable-context.adoc:38`). **Tier 2 note.** McMahon is no longer in the list, because the section that cited it was cut, so the list now has eight works and none of them is cited in the body.

- [ ] `99-references.adoc:11` cites a BBC news story as "McMahon, L (2026)". TS-26 (Citations) says to cite the publisher of a news story as the author even where there is a byline. The six inline citations at `22-security.adoc:91-109` must change with it. **Tier 2 note.** Moot. The McMahon reference and its six inline citations were removed with "Testing autonomous agents". Tick as no change needed when working tier 4.

- [ ] `99-references.adoc:11`, `:13`, and `:19` write "McMahon, L", "Mollick, E", and "Vaswani et al". TS-26 (Citations) writes an initial with a period ("Johnson, M.") and the truncation as "et al.". Entries at `:5`, `:7`, and `:15` omit a year that their sources state. **Tier 2 note.** The McMahon part is moot (entry removed). The Mollick and Vaswani forms remain.

- [ ] `05-benefits-and-costs.adoc:60` writes `xref:012.adoc[TS-12]`. The style guide requires the form `xref:012.adoc[*TS-12: Quality Assurance*]`.

- [ ] `13-agent-skills.adoc:228-240` writes a list with `-` markers and `**bold**` markup. TS-28 (Native syntax) requires `*` markers, and bold is single asterisks.

- [ ] `19-agentic-workflows.adoc:78-88`, `:123-125`, `:156-158`, and `13-agent-skills.adoc:248-250` terminate a bold lead-in term with a colon outside the bold. TS-26 (Lists) requires a period inside the bold. `19:24` puts the period outside the bold, after an xref.

- [ ] `19-agentic-workflows.adoc:121`, `13-agent-skills.adoc:193`, and `13:226` end the lead-in to a list with a colon. TS-26 (Colons) requires a period.

- [ ] `20-evaluation.adoc:26-28` writes list items in lowercase with semicolons and "and". `18-ai-assisted-workflows.adoc:70-73` ends noun-phrase items with periods. `16-loop-engineering.adoc:46-49` runs full-sentence items together without blank lines. Each diverges from TS-26 (Lists) or TS-28 (Spacing between items).

- [ ] `04-ai-use-cases.adoc` joins independent clauses with a colon about 42 times and a semicolon 13 times, and uses 112 em dashes, many to join clauses. TS-26 (Colons, Semicolons, Dashes) prohibits the colon join, discourages the semicolon, and says to use em dashes sparingly. `05-benefits-and-costs.adoc` has the same pattern at lower density (12 colon joins, 35 em dashes). Do this item after the tier 2 cuts, since most of the affected text is recommended for removal.

- [ ] First-person "we", "us", and "our" appear at `02-definitions.adoc:48`, `03-human-in-the-loop.adoc:6`, `:39`, `:41`, `04-ai-use-cases.adoc:12`, `:26`, `:30`, `:34`, `05-benefits-and-costs.adoc:29`, and `11-context-engineering.adoc:27`, `:31`. TS-26 (Grammatical person) reserves "we" for a statement of the author's position.

- [ ] Positional references, which TS-26 (Figures, tables, and examples) prohibits because position is not stable: "above" at `19-agentic-workflows.adoc:225`, `04-ai-use-cases.adoc:26`, `:32`, `:34`, `:36`, `:43`, `:63`, `:139`, `05-benefits-and-costs.adoc:68`, `:70`, `13-agent-skills.adoc:184`, `22-security.adoc:109`, `:116`, and "below" at `04:16`, `04:26`, `11-context-engineering.adoc:41`.

- [ ] RFC 2119 keywords are capitalized in sentences that state no requirement: `18-ai-assisted-workflows.adoc:68`, `19-agentic-workflows.adoc:123`, `12-reusable-context.adoc:25`, `14-model-context-protocol.adoc:42` (twice), `22-security.adoc:48`, `:91` ("internet access it SHOULD NOT have had"), and `:97` ("the agent MAY be able to escape"). RFC 8174 gives the capitalized form its special meaning, so each of these reads as a rule.

- [ ] American English is required by TS-26 (Language). `04-ai-use-cases.adoc:28` has "noughts-and-crosses", `07-choosing-models.adoc:59` and `:61` have "maths", and `05-benefits-and-costs.adoc:41` has "levelling".

- [ ] Idioms that TS-26 (Language) says may not translate: "earning its keep" (`04-ai-use-cases.adoc:111`, `15-harness-engineering.adoc:96`, `20-evaluation.adoc:42`), "force multiplier" (`04:166`, `05-benefits-and-costs.adoc:74`), "raise the floor" (`19-agentic-workflows.adoc:18`, `04:24`, `05:41`), "batteries included" (`08-choosing-interfaces.adoc:50`), "blunt instruments" (`08:5`), "wave it through" (`16-loop-engineering.adoc:34`), and "flailing blindly" (`18-ai-assisted-workflows.adoc:42`).

- [ ] Rhetorical questions, which TS-26 (Question marks) prohibits: `17-ways-of-working-with-ai.adoc:12` and `20-evaluation.adoc:6`.

- [ ] Backticks inside quoted strings, which TS-26 (Quotation marks) prohibits: `13-agent-skills.adoc:222` (twice) and `14-model-context-protocol.adoc:54`.

- [ ] `13-agent-skills.adoc:297` prefixes a command with `$`, against TS-26 (Code blocks). Listing blocks at `11-context-engineering.adoc:55`, `13-agent-skills.adoc:85`, and `21-cost-optimization.adoc:8` specify no language.

- [ ] One term per concept is required by TS-26 (Terminology). The standard varies: "agent harness", "coding assistant", "AI coding tool", and "AI code generator" (`19-agentic-workflows.adoc:285`); "supervisor agent", "main agent", and "lead orchestration agent" (`11-context-engineering.adoc:102`); "reusable context", "context bundle", and "reusable prompt components" (`11:51`); "inference provider" (`02-definitions.adoc:14`) and "hosting provider" (`21-cost-optimization.adoc:16`, `:44`); "light" (`07-choosing-models.adoc:57`), "efficient" (`19:95`), and "cheap" models; "guardrails" and "guards" (`19:18`); "kill switch" and "kill-switch" (`22-security.adoc:103`, `:107`); "front-matter" (`13-agent-skills.adoc:95`) where TS-27 writes "frontmatter".

- [ ] `05-benefits-and-costs.adoc:60` uses "DORA" without expansion, against TS-26 (Abbreviations).

- [ ] Explicit anchors mix cases: `[#Definitions]`, `[#Human-in-the-loop]`, `[#Persistence]`, `[#Evaluation]`, and `[#Auditability]`, beside lowercase kebab-case elsewhere in the same standard. TS-28 and the template show lowercase only. Sibling standards are 88% lowercase (406 of 461 anchors). **Decision needed:** recommend lowercasing the five and their references, in one sweep.

- [ ] Six section files have no explicit anchor on their title: `18-ai-assisted-workflows.adoc:1`, `04-ai-use-cases.adoc:1`, `06-ai-engineering-stack.adoc:1`, `08-choosing-interfaces.adoc:1`, `16-loop-engineering.adoc:1`, and `22-security.adoc:1`. Nothing references them today, so this is consistency with the other 16 only. **Tier 2 note.** Anchors were added to `06-ai-engineering-stack.adoc`, `08-choosing-interfaces.adoc` and `22-security.adoc` (needed by new cross-references). Two remain: `04-ai-use-cases.adoc` and `16-loop-engineering.adoc`. `18-ai-assisted-workflows.adoc` already had one, so the finding was partly wrong.

- [ ] `05-benefits-and-costs.adoc:6-23` is an 18-line commented-out quotation, attributed to a fictional "assembly programmer, 1980", and soft wrapped against the style guide. `02-definitions.adoc:4` is a `TODO` comment. **Decision needed:** recommend deleting the quotation, since a fabricated attribution cannot be published, and resolving the `TODO` with the glossary item in section 3.

- [ ] `13-agent-skills.adoc:256-365` presents a Markdown `SKILL.md` template that contains AsciiDoc source-block syntax (`[source,sh]` with `----` delimiters at `:295-298`, `:306-312`, and `:319-329`). A reader who copies it gets invalid Markdown. Use fenced code blocks, and lengthen the outer AsciiDoc delimiter as TS-28 (Delimited blocks) describes. `13:343` also ends with a stray `]`.

## 6. Prose defects

- [ ] `01-introduction.adoc:9` "large language models models that are themselves based on" → "large language models, which are themselves based on"

- [ ] `01-introduction.adoc:7` "Out-of-scope is the integration of AI into software applications." → "The integration of AI into software applications is out of scope."

- [ ] `02-definitions.adoc:8` "large-language model (LLM)" → "large language model (LLM)", as at `01-introduction.adoc:3`

- [ ] `02-definitions.adoc:18` "A model's *parameters* (which are called *weights*), are" → "A model's *parameters*, also called *weights*, are"

- [ ] `02-definitions.adoc:28` "most the text a user types" → "most often the text a user types"

- [ ] `02-definitions.adoc:32` "Agent harness are programmed" → "Agent harnesses are programmed"

- [ ] `02-definitions.adoc:48` "we can assume that the word orchestrator is used is contexts where" → "the word orchestrator is used in contexts where"

- [ ] `18-ai-assisted-workflows.adoc:68` "including but not limited to." → "including the following."

- [ ] `07-choosing-models.adoc:20` "will give the model material to work. Extend these guides with external verification checks — eg. a compiler, automated tests — will improve outcomes" → "give the model material to work with. Extending these guides with external verification checks, eg. a compiler or automated tests, improves outcomes"

- [ ] `07-choosing-models.adoc:22` "The more expensive, more ultimately more effective, option" → "The more expensive, but ultimately more effective, option"

- [ ] `22-security.adoc:87` "(that's the role its given in the test)" → "(that is the role it is given in the test)"

- [ ] `22-security.adoc:103` "Monitor for and have a kill switch ready to halt unexpected autonomous behavior" → "Monitor for unexpected autonomous behavior, and have a kill switch ready to halt it"

- [ ] `04-ai-use-cases.adoc:26` "We MUST NOT treat a model as though it were genuinely intelligent in the human sense" is unfalsifiable. No reader can demonstrate compliance with a rule about belief. State the behavior the rule protects, which `04:22` already does. **Tier 2 note.** The sentence was removed with the cut of the "inherent nature" section. Tick as resolved when working tier 4.

- [ ] `03-human-in-the-loop.adoc:41` "the one a team MUST keep sharp" and `11-context-engineering.adoc:51` "Prompts MUST be token-efficient" are unfalsifiable. Neither says what would count as failing. `12-reusable-context.adoc:12` repeats the second.

- [ ] `19-agentic-workflows.adoc:218` "Different steps in a pipeline SHOULD be assigned to different models" is stated without the cost it imposes. It conflicts in practice with data-confidentiality limits on which providers may see the code, which the sentence does not acknowledge. Soften to MAY, or state the condition.

- [ ] Filler words that TS-26 (Filler words) lists appear 66 times, with "genuinely", "precisely", "merely", and "simply" the most frequent. They concentrate in `04-ai-use-cases.adoc`. Sweep after the tier 2 cuts.

- [ ] Significance is asserted without the fact behind it, against TS-26 (Significance claims): `04-ai-use-cases.adoc:30` ("That is the essence of the paradigm shift", "what makes the technology transformative"), `08-choosing-interfaces.adoc:27` ("They represent a qualitative shift"), `11-context-engineering.adoc:19` ("Context engineering is a key skill"), and `19-agentic-workflows.adoc:265` ("Setting clear success criteria is the key").

- [ ] `08-choosing-interfaces.adoc:27` "They represent a qualitative shift" and `19-agentic-workflows.adoc:256` "Together they compose the infrastructure" use inflated verbs where TS-26 (Terminology) asks for "is" or "are".

- [ ] `13-agent-skills.adoc:20-23` illustrates the separation of workflow and knowledge with two quoted questions and arrows ("→ Skill issue"). The example does not show how a reader would tell the two apart, which is the rule it illustrates.

- [ ] `11-context-engineering.adoc:65` says a vague prompt "passes that test" and a specific one "does not pass", then "Failing the test is a reliable signal to add context". Passing is the bad outcome in the first two sentences and failing is the bad outcome in the third.

- [ ] `19-agentic-workflows.adoc:57` and `:64` write flows as `TASK → AGENT → SOLUTION` in monospace capitals. These are neither something a reader types nor system output, which is what TS-26 (Monospace) reserves monospace for.

- [ ] Volatile detail is written into the body as timeless fact: "As of 2026" (`12-reusable-context.adoc:25`, `13-agent-skills.adoc:71`), named products and model sizes (`02-definitions.adoc:50`, `07-choosing-models.adoc:53-57`, `08-choosing-interfaces.adoc:46`), and the tool-support list at `12:42`. Each will be wrong within months and nothing marks it for review. Write the date in ISO 8601 form as TS-26 (Dates and times) requires, or move the detail to a dated table.
