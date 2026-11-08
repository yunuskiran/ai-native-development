# 3. Understanding AI-Driven Methodologies

> Author manuscript · completed 2026-11-05 · C03 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C03-S01 -->
## The comparison unit

“We used the same AI method” is an incomplete description of an engineering exercise. One team may have enabled optional test architecture, another may have used a short repair path, and a third may have followed a different generation of the documentation. Their work can share a name while involving different instructions, artifacts and decision rights.

The comparison unit in this book is a **named source snapshot and implementation profile, applied under stated operating conditions**. A profile identifies the relevant route, required activities, optional modules and settings. Operating conditions identify the task, starting repository, host, model access, operator and resource limits. Together they describe what was actually available to influence the work.

Start with a source identity. A repository commit gives a fixed documentary reference. A package version names a distributed artifact, whose contents still need to be checked for an executable exercise. A branch name can move. A product version may bundle process instructions with host behavior. Record these identities at the level needed to understand and reproduce the intervention.

Then describe configuration. An approval requested in a prompt, a hook that blocks an operation and a human review outside the tool are different mechanisms. A profile may enable one and omit another. The evaluation must identify the actual arrangement before interpreting a completed stage or a green status.

The following record defines the unit without prescribing a particular methodology:

| Field | What the reader needs |
|---|---|
| Method/source identity | Name, repository or publication, exact source revision and relevant passages |
| Installed implementation | Package/plugin identity and contents used, if execution occurs |
| Profile and modules | Selected route, required steps, enabled add-ons and material overrides |
| Host/model conditions | Execution surface, model identification available to the operator, worker/tool permissions and relevant settings |
| Business task | Accepted requirements, exclusions and the specific episode being attempted |
| Starting state | Baseline revision, fixtures, existing application behavior and reset procedure |
| People and resources | Operator familiarity, decision owners, reviewer arrangements and resource ceiling |
| Evidence boundary | Documentary walkthrough or actual execution; which conclusions the records can support |

These fields also help separate a concept from one implementation. AWS's July 2025 introduction describes inception, construction and operations. The pinned workflow implementation examined for this book includes initialization and ideation as well. The names therefore need source qualifiers; the difference does not establish that one source is defective. [Original AI-DLC account](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/), [inspected implementation phases](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/04-phases-and-stages.md#L18-L45)

A similar caution applies to a host change. If the model, available tools and reviewer dispatch all change with the workflow, a different outcome cannot be attributed to the method alone. We may still learn something about that configured arrangement. The report must identify the combined intervention and preserve the limitation.

The source snapshots used here are research references, not a completed installation freeze. The GSD chapter retains the author's requested title while contemporary Core sources provide a dated implementation reference. The final edition/lineage choice and exact run packages remain open. This visible boundary is preferable to silently applying one generation's behavior to every use of a name.

<!-- C03-S02 -->
## Methods, approaches and tools

For this book, a method or process framework arranges decisions, roles, artifacts and feedback across development work. An approach describes a way to organize some of that work. An execution tool supplies capabilities through which the work happens. These are working distinctions for comparison, not universal labels that every project must adopt.

A single package can contain substantial process guidance and executable tooling. An editor can supply specification workflows. A framework can be distributed as skills or templates. We therefore need to inspect what each component does rather than classify it by its installation format.

The accepted coverage has four framework chapters and a cross-cutting approach:

| Coverage | Role in the book | Question the classification helps answer |
|---|---|---|
| BMAD Method | Framework deep dive, chapter 4 | How does a selected path size planning, carry intent and organize implementation/review? |
| GSD framework lineage | Framework deep dive, chapter 5 | How does the selected implementation organize phases, context and verification? |
| AWS AI-DLC | Lifecycle/framework deep dive, chapter 6 | How do concept, implementation and configured profile assign work and authority? |
| AI Unified Process (AIUP) | Framework deep dive, chapter 7 | How do specifications, use cases and selected construction paths govern implementation and change? |
| Spec-Driven Development (SDD) | Cross-cutting approach, chapter 8 | What role do specifications play before, during and after implementation? |
| Coding hosts, IDEs and implementation toolkits | Execution and process context | Which capabilities, dependencies and constraints belong to the selected arrangement? |

The four frameworks are included because they are the book's chosen subjects, not because every other toolkit lacks a methodology. Excluding a toolkit from peer coverage is an editorial scope decision. When a toolkit contains planning or change rules, acknowledge those rules rather than reduce the toolkit to a command-line interface.

The source material gives us concrete reasons to inspect each framework. BMAD's planning guide distinguishes defined intent from work that needs further planning and provides different paths according to that need. That is a process choice, not merely an editor feature. [BMAD planning-path guidance](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/choose-a-planning-path.md#L8-L65)

The inspected GSD Core guide describes discussion decisions carried in phase context, plans, execution, verification and shipment. Its artifacts connect activities across sessions. This supports examining the selected process design; it does not establish its claims about reduced rework or context quality. [GSD Core phase loop](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L25-L59)

AWS's implementation makes configured routes consequential: its Classic and Express descriptions differ in stage selection, artifacts, reviews and guard behavior. The lifecycle concept and a particular route through that implementation should therefore be recorded separately. [Inspected workflow profiles](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/workflow-profiles.md#L45-L95)

AIUP's workflow maps requirements, use cases, architecture decisions, test journeys and acceptance records to their producers and consumers. That artifact flow supplies a process subject for analysis, while construction adapters introduce further scope and dependencies. [AIUP artifact flow](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L48-L66)

These descriptions establish the presence of process mechanisms in the selected sources. They do not establish equivalent lifecycle coverage, equal effort or effectiveness. One framework's phase may encompass work that another splits across stories or use cases. Comparing the count of those units would answer a naming question rather than an engineering one.

The implementation layer still matters. A process that expects worker dispatch depends on a host's relevant capabilities. A stack-specific construction adapter may constrain the application architecture. Those dependencies belong in the comparison record. They should not quietly become universal properties of the method, or disappear because the method describes itself as portable.

<!-- C03-S03 -->
## A short specification primer

In this book, a specification is an identified description of required behavior or constraints, with a known scope and change policy. It may be concise and written in natural language. Its engineering role depends on what decisions it carries, who maintains it and how it relates to implementation and acceptance.

A long prompt does not acquire that role through length. A short issue can serve as a useful behavioral contract if it identifies the requirement, preserves material constraints and has a clear disposition. Conversely, an extensive document can remain ambiguous about who may approve a change or which behavior should prevail on conflict.

Birgitta Böckeler's 2025 analysis distinguishes spec-first, spec-anchored and spec-as-source patterns: respectively, specifications used before implementation, retained for later evolution, and treated as the human-edited source from which implementation is produced. We use the vocabulary with attribution as a lifecycle lens, not an effectiveness ranking. [Böckeler's SDD analysis](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

For the deep dives, four practical questions are enough to begin:

| Policy question | Why the answer matters for a change |
|---|---|
| Who owns the specification? | Identifies who may change the accepted behavior and by which route |
| What is retained? | Distinguishes a temporary implementation instruction from a maintained product record |
| What happens on disagreement? | Identifies whether the intent, specification, code or check needs correction |
| How is alignment assessed? | Separates links and assertions from observations that address the required behavior |

Consider the proposed approval-policy change. “High-risk requests need two approvals” leaves the treatment of existing requests unresolved. The case's agreed direction binds requests to the policy active at creation. A useful specification change needs to carry that decision as well as the new count. Otherwise two implementations could follow the short sentence and disagree materially about existing v1 requests.

Ownership is equally concrete. BMAD's inspected specification guide directs updates to its named `SPEC.md` through `bmad-spec`, preserving capability identifiers. That policy concerns a particular artifact; it does not tell us that every specification in every framework has the same writer. [BMAD specification ownership](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/define-requirements-and-a-specification.md#L112-L116)

AIUP's inspected change guidance starts with changed intent or requirements, then reconciles related specifications and implementation/tests through the selected construction path. This is a documented maintenance policy. Its existence does not prove that every later implementation stays aligned. [AIUP change guidance](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L475-L494)

The phrase “source of truth” needs the same precision. Truth for which decision? If a business rule and generated endpoint disagree, who resolves the conflict? If an implementation exposes a previously unknown constraint, how does that finding change the specification? A declaration of authority supplies no synchronization mechanism by itself.

We also reserve **executable specification** for an artifact with an identified mechanical execution or validation path. A natural-language instruction that an agent interprets is not enough to establish that property. Nor does generation imply deterministic output: a reproducible exercise needs inputs, configuration and observations, even when repeated outputs differ.

Chapter 8 examines specification policies in depth. For now, retain the distinction between using a specification at the start, maintaining it through change and governing how implementation may be edited. A framework can combine these policies in different ways across artifacts. We will inspect the actual rules before applying a broad label.

<!-- C03-S04 -->
## The common SaaS problem

The common case is a synthetic B2B service for recording vendor-access requests and their decisions. A requester asks for temporary access for a vendor. Eligible approvers in the same customer tenant decide the request. The service preserves decision history; it does not provision access in an external system. This boundary keeps the business problem meaningful without requiring live vendor accounts or infrastructure.

A **tenant** is the customer-organization boundary in the exercise. Tenant A's membership, requests and history must not become available to a tenant B actor through the business interface. The test fixtures will contain both tenants so the boundary can be examined. No real customer or vendor data are needed.

An actor may hold more than one role. A requester with approver or administrator privileges remains disqualified from approving their own request. Approval also requires current eligible membership in the request's tenant. A role label alone therefore does not settle a decision; actor identity, target request and current membership all matter to the agreed behavior.

Under the base policy, one eligible distinct approver can complete a pending request. A permitted rejection is terminal. Repeated decision requests need a defined idempotency contract, and concurrent decisions must preserve the policy and one valid terminal outcome. Successful transitions need durable, tenant-scoped audit history. The detailed requirements and unresolved interface choices are in the [case specification](../../CASE_STUDY_SPEC.md).

The shared increment can be expressed without selecting a framework's native artifacts:

| Neutral business brief | Agreed direction |
|---|---|
| Useful behavior | Create a valid request, obtain an eligible decision, inspect the permitted request/history |
| Important boundaries | Identity and current membership, tenant isolation, no self-approval and consistent terminal behavior |
| State/evidence obligations | Defined retries and concurrency; durable business state and audit history |
| Technology family | TypeScript / Node.js; exact framework, database, compiler and runtime versions remain open |
| Exclusions | External provisioning, billing, outbound email, production federation and regulatory certification |
| Acceptance status | Requirements are design obligations; no application or independent executable checks have been completed |

The actors and rules are common; native planning artifacts remain different. BMAD may carry the intent in its specification/story arrangement. A GSD path may use phase decisions and plans. AIUP may organize behavior through use-case artifacts. Requiring every arm to use one of these structures would impose part of that framework on the others.

We plan three episodes. **E1** implements the base increment from the same neutral scaffold. **E2** changes the policy for newly created high-risk requests to require two distinct eligible approvers, while existing v1 requests keep their bound policy and standard-risk v2 requests still need one. **E3** repairs a predetermined tenant-boundary defect in a shared prepared baseline. They examine creation, change and repair rather than repeatedly scoring a greenfield demonstration.

Each episode needs its own matched starting condition. In particular, E2 should not begin from each framework's different E1 output if we intend to compare the change procedure under the same baseline. Those prior outputs could differ in structure, defects and decisions. A longitudinal study of maintaining each output would be a different design and should be reported separately.

The external acceptance boundary should also remain common. A method may generate its own checks and reviews, but the independent case obligations still ask whether the same business behavior holds. Preserve the native artifacts alongside the common requirement/check mapping. That lets us inspect how each process carries the work without demanding identical prose or code.

This design is proposed, not executed. Choosing a common application stack may expose adapter constraints; choosing a host may alter reviewer or worker capabilities. Those issues need explicit disposition before runs. Chapter 11 owns the complete contract, baselines, commands and observations if execution occurs. The short case here supplies the business vocabulary needed to understand the four deep dives.

<!-- C03-S05 -->
## Questions applied to every framework

The comparison instrument contains eleven dimensions, F01–F11. They organize questions about mechanisms and outcomes. They are not eleven scores, and a strong answer in one dimension cannot silently compensate for an unacceptable boundary in another.

Use the same questions while preserving native terminology. A framework may call an acceptance activity verification, review or a gate. The relevant question is who makes which decision, using what evidence, under which configuration. Names and counts are starting points for investigation.

| ID | Dimension | Common question | Evidence that would strengthen an outcome claim |
|---|---|---|---|
| F01 | Decision rights | Who can propose, approve, change scope or stop work, and how does the selected gate operate? | Recorded approvals, bypass behavior, interventions and unresolved decisions |
| F02 | Planning overhead and scale | What work is required for a repair, feature or uncertain initiative? | Setup, planning, review and relevant rework under stated scope |
| F03 | Artifact lifecycle | What is created, retained, retired and reconciled; who owns it? | Artifact changes and disagreements through a maintenance episode |
| F04 | Requirements traceability | How do requirements reach plans, implementation, checks and acceptance? | Inspected valid, missing and semantically incorrect links |
| F05 | Context management | What information reaches each session or worker, and what survives interruption? | Recorded inputs, omissions, recovery and resulting corrections |
| F06 | Solo/team operation | How are business, design, implementation and review duties assigned and handed off? | Observed human coordination under disclosed team conditions |
| F07 | Brownfield suitability | How is existing behavior discovered and the intended change bounded? | Shared change/repair baselines and regression observations |
| F08 | Testing and acceptance | Which checks are prescribed, who owns the oracle and how is disagreement handled? | Independently reviewed checks and actual command/output records |
| F09 | Deployment governance and operations | Which release, observability, recovery and service-ownership duties are covered? | Environment-specific operational evidence and reviewed limits |
| F10 | Portability and dependencies | What depends on a host, model, adapter, stack or service? | Defined compatibility/migration observations and disclosed workarounds |
| F11 | Maintainability | Who keeps specifications, code and generated assets aligned after change? | Follow-up changes, drift findings and repair effort over time |

The dimensions overlap where the underlying work overlaps. An outdated specification concerns artifact lifecycle, traceability and maintenance. Record the event once, then explain its relevance to each question. Repeating the event in several columns does not create several independent observations.

Required and optional mechanisms need separate treatment. A mandatory review contributes to the selected route's work. An optional module contributes only when enabled. An external reviewer or tool may be necessary to satisfy the book's acceptance boundary without being part of the framework core. Describe that arrangement rather than attributing all resulting coverage to the method.

Take F04 as a worked example. Suppose a hypothetical plan links a capability to CS-05. The implementation contains a corresponding marker, and a test cites the same identifier. The references establish presence. They do not establish that the test prevents self-approval. If it targets a completed request, it could succeed through the wrong rule. Completeness and semantic correctness require further inspection.

F01 presents a different distinction. A document that asks an operator to approve a plan supports a claim that approval is prescribed. A recorded pause and response can show that approval occurred in a run. A configured block with bypass tests can establish something about enforcement in that environment. These are progressively different questions; no adjective in the workflow name answers them all.

For F02, report what effort includes. Installation, familiarization, artifact preparation, active human work, waiting and repair may be allocated differently. Agent duration and wall-clock duration can overlap. A single unexplained completion time would make comparisons hard to interpret. The future run protocol must define these observations before measurement, not after a favorable result appears.

For F06 and F09, respect the scale of the exercise. One author playing several roles can demonstrate a proposed handoff but cannot establish a human team's coordination benefit. A local service can expose useful behavior but does not supply evidence of real incident response, recovery practice or production ownership. Those dimensions may remain unassessed even when the local exercise succeeds.

An unanswered dimension is not an automatic failure. A process could be suitable for a bounded task while leaving an operational duty to the organization's existing practice. The comparison must identify that dependency and decide whether it is acceptable for the scenario. Conversely, a documented feature should not receive an effectiveness rating merely because it is relevant.

Chapter 9 will synthesize findings under these questions. Here, their role is to make the deep dives inspectable. The research [comparison framework](../../COMPARISON_FRAMEWORK.md) retains the full instrument, evidence categories and reporting rules.

### Apply the instrument in a consistent order

Begin an inspection with the selected method identity, then the task and its accepted boundary. Ask how the workflow obtains decisions, carries them into work and interprets the resulting checks. Finish with the dependencies and duties supplied by the surrounding organization. That order reduces the chance of praising a verification mechanism before establishing what it was supposed to verify.

For a small existing-code repair, some lifecycle questions may have little work behind them. Record the reason. An operating environment supplied by an organization can remain outside the repair while still constraining release. A larger feature may need explicit design and operational preparation. The same instrument can describe both arrangements while preserving the difference in scope.

Keep the completed instrument with the source revision and scenario. Another reviewer can then dispute a particular interpretation and identify the evidence that would resolve it. Updating one assessment becomes possible without rewriting the framework's identity or importing a conclusion from an unrelated task.

<!-- C03-S06 -->
## Reading claims and observations

Every substantive statement in a comparison needs an evidence type. This is especially important when documentation mixes an instruction with an expected benefit. “Use a fresh session” describes a mechanism. “Fresh sessions prevent relevant errors” is an effectiveness claim. The first does not establish the second.

The inspected GSD Core phase-loop guide provides a concrete example: it describes fresh executor contexts, names a 200k-token window and attributes benefits to that arrangement. Our documentary conclusion is that this source prescribes a context strategy. Actual window availability depends on the selected host/model arrangement, and effectiveness requires observations of what context arrived and what errors occurred. We do not turn the documentation's number into a portable capacity guarantee. [GSD Core context description within the phase loop](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L25-L59)

This is the reading discipline we apply to favorable and unfavorable claims alike. Preserve the mechanism, identify its dependencies, and ask what additional evidence would establish the stated consequence. A source-reported limitation also needs its exact version and scope before it can rule out another configuration.

We distinguish the following categories:

| Evidence type | What it can establish within its scope | Question to retain |
|---|---|---|
| Documented design | A selected source prescribes a workflow, artifact or dependency | Which version/profile, and was actual behavior checked? |
| Source-reported outcome | A maintainer or vendor reports a result | Under what conditions, with what records and interests? |
| Field observation | A practitioner reports what happened in a particular setting | Which task/configuration, what failures, and how transferable is it? |
| Controlled observation | An executed comparison records outcomes under a disclosed design | What was held constant, what varied, and which confounders remain? |
| Editorial analysis | A reasoned interpretation or conditional recommendation | Which premises and evidence would change the conclusion? |

An illustrative walkthrough is a separate presentation mode. It can explain a procedure or expose a design ambiguity. It does not become a field observation because the story uses names and realistic business rules. Our unexecuted vendor-access examples remain in that mode until actual records exist.

The categories are not a simple quality ladder. Primary documentation is often the best evidence for a prescribed writer policy. A controlled experiment may be more relevant to an effect under its tested conditions, while telling us little about another release. A field report can reveal a concrete failure that a broader study did not examine. Match the evidence to the claim.

Interests also need disclosure. A maintainer may understand an implementation deeply and still benefit from its adoption. A practitioner may have invested in a particular workflow. An external analysis may use a judgment-based rubric rather than measure outcomes. These conditions affect interpretation; they do not justify ignoring the source or treating its assertions as independently established.

The same precision applies to absence and uncertainty:

| Statement | Appropriate interpretation |
|---|---|
| Not assessed | The current work does not establish an answer |
| Not found in inspected scope | The bounded inspection did not locate the mechanism; wider coverage may differ |
| Outside the selected profile | The described capability is not part of the configuration being evaluated |
| Absent in a defined scope | A sufficiently complete check supports a missing-capability claim for that scope |

Do not convert those states into a common zero. A missing test result differs from an executed failed test. An unreviewed adapter differs from a demonstrated incompatibility. A documented optional capability differs from something the base route produces. Preserving those distinctions makes a later decision more defensible than filling a table with intuitive ratings.

Version qualifiers need to survive paraphrase. If a source describes a particular adapter, a summary that drops the adapter can overstate the method. If an original article describes a concept, a current implementation's phase count should not be substituted without explanation. Trace the claim back to the source and record the exact scope it supports.

For outcomes, preserve failures, deviations and stopping conditions. A trial that stops during installation has not tested the business behavior. A successful run after substantial manual redesign is evidence about the assisted arrangement, including that intervention. Removing inconvenient attempts or omitting the redesign would alter the apparent result.

Reproducibility also has a bounded meaning here. The record should permit another person to recover the starting conditions, follow the procedure and compare observations. It need not promise identical model output. When model identity, access or behavior cannot be fully fixed, disclose that limit rather than claim exact repeatability.

These rules let a reader challenge the argument at the appropriate point: source interpretation, design, execution, inference or recommendation. The book's [research protocol](../../RESEARCH_PROTOCOL.md) records the corresponding source, interest, rights and claim-handling duties.

### Give each claim the evidence it asks for

A maintainer may document a route for small changes. Reading the relevant revision can support a statement about that route. To say a team used it on the tenant repair, the investigator needs records of the configured workflow and the repair. To say the route reduced effort, the investigator needs an accounting policy and a comparison design. A reader should be able to tell when an author moves between these levels.

One practical reading habit is to underline the verb in a claim. “Describes,” “requires,” “blocked” and “improved” demand different observations. A written requirement can be inspected in the document. A blocked action needs an executed attempt and a record of what prevented it. An improvement needs an explicit reference point and a way to handle changes in task difficulty or operator experience. Keep the claim local when the available evidence is local.

A source locator is an inspection aid. Open the cited revision and read the passage around the claim. Check whether the prose describes a requirement, an optional path or an observed result. If the claim depends on a selected adapter or setting, keep that condition in the assessment. This makes source review repeatable at the level of an individual statement.

<!-- C03-S07 -->
## How to read the four deep dives

Read each framework chapter as an examination of a selected arrangement. Begin with its scope note, then follow the common business intent through its native decisions and artifacts. The chapter should make clear what the source prescribes, what the teaching example proposes and what has actually been observed.

Use five questions as a reading guide:

1. What intervention is being described: source, profile, modules and host assumptions?
2. Which unresolved decisions must be settled before implementation, and who settles them?
3. What carries those decisions into work and through a later change?
4. Which checks support acceptance, and what do they leave unresolved?
5. Under which conditions would this arrangement merit investigation, adaptation or rejection?

The native artifact trail should differ. A BMAD specification is not automatically an AIUP use case under another filename. A GSD phase is not an AWS lifecycle phase of equal size. Preserve what makes the mechanism distinct, then use the common questions to examine its role.

The chapters should also give small changes a fair treatment. A minimal route must retain its relevant obligations; a larger route should be used when the selected process and task call for it. The comparison should not force every framework through its longest demonstration or silently omit a required step. Optional enhancements remain visible configuration choices.

Source caveats are part of the explanation. A framework can change while the reviewed source stays fixed. A host can add capabilities while an older adapter remains limited. The useful question is which statement holds for the arrangement under discussion. Edition notes and exact references let the reader distinguish a documented historical design from a current environment they may later evaluate.

After the four deep dives, chapter 8 expands specification lifecycle policies. Chapter 9 brings the evidence together; chapter 10 turns supported constraints and uncertainties into conditional choices. Chapter 11 owns the complete case records. This order gives the reader a common vocabulary before asking for a comparative judgment.

The result should be a comparison a reader can inspect and disagree with constructively. A missing observation stays visible. A claimed advantage has a source and scope. A recommendation names its premises. With that contract in place, we can begin BMAD's deep dive without treating its vocabulary as the default for every method that follows.

Before moving to chapter 4, choose one maintenance task from a project you know. Describe its accepted behavior, who can settle ambiguity and one observation that would change your decision about completion. Keep the description method-neutral. As you read each account, identify where those three items would live and which dependencies the proposed arrangement would add. This exercise produces a local comparison question that can survive differences in vocabulary.
