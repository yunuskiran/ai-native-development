# 10. Choosing the Right Methodology

> Author manuscript · completed 2026-11-05 · C10 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C10-S01 -->
## Describe the project before naming a method

Begin selection with a decision the team needs to make well. Describe the work before creating a shortlist.

Requirements may disappear between discussion and implementation. A maintenance queue may be burdened by documents that no one revisits. An established service may need traceable policy changes. Each hypothetical condition calls for a different evaluation question.

For the vendor-access service, our immediate question is narrow: can a selected process carry a tenant-local approval rule from agreed intent through implementation and acceptance, then preserve it during a policy change? The question does not require us to decide which framework is best for every service the organization might build.

Write down the conditions that could change the answer. Is this a new codebase or an existing one? Who can settle product ambiguity? How long must the service be maintained? What may the assistant change? Which host and runtime can the team actually use? Which obligations would make an otherwise plausible output unacceptable?

A useful project description is specific enough to disqualify an attractive candidate. “We use TypeScript” is too broad to establish compatibility. “We must retain this existing persistence and HTTP boundary, and cannot introduce another application stack during the exercise” is a real constraint. A framework with a stack-specific adapter would then need a separately assessed route.

State these conditions before reading a candidate's positioning. Otherwise it is easy to rewrite the problem in the vocabulary of the first polished workflow we encounter. The selection record should survive a change in popularity or branding because its reasons concern the team's work.

<!-- C10-S02 -->
## Identify non-negotiable decision duties

In the common case, no self-approval and tenant isolation are required behavior. A named ceremony is not. We need a way to establish the rule, implement it, check it and preserve the decision when the code changes. There may be several legitimate ways to arrange that work.

Separate these duties from preferences. The team may prefer Markdown artifacts, a particular command style or a small number of files. Those preferences can affect adoption cost. They cannot replace the obligation to show that a foreign-tenant actor cannot obtain another customer's request under the agreed interface policy.

The duties also need owners. A model can propose a policy but cannot supply missing organizational authority. A workflow can request approval, but the selected configuration and operator behavior determine what approval means in practice. An acceptance owner needs to know which decisions were actually reviewed, by whom, and against which requirement.

For a small team, ownership may overlap. Record the overlap and its limits. If the implementing engineer also prepares the only tests, call them implementation tests. Additional AI review may be helpful, but calling it independent human verification would overstate the arrangement.

Once these duties are explicit, ceremony becomes something to justify. A document earns its place when it carries a decision, supports a check or helps a later change. If it has no such role in the proposed evaluation, ask whether it belongs in that path. Equally, removing a document requires deciding where its useful information will live.

### Distinguish permission to work from permission to accept

For the common service, the product owner settles whether an old request retains its original policy. An engineer chooses how the accepted rule is represented within the agreed application boundary. An acceptance reviewer checks evidence against the rule. A release owner decides whether remaining operational limitations permit a release. One person may hold several roles, but the decisions remain different.

Write that assignment before configuring automated approvals. Permission for an assistant to edit code does not authorize it to change a product rule. Approval of a proposed plan does not establish that the implementation satisfies it. A review label should identify the decision actually made, not borrow authority from a nearby checkpoint.

Also define what happens when the responsible person is unavailable. A trial may pause, proceed only with unaffected work, or record a provisional interpretation excluded from acceptance. The operator should not infer consent from an unanswered question. For a local evaluation, the sensible action may be to stop the affected episode and retain its state.

This distinction helps diagnose an apparently slow process. Waiting for a required policy decision is different from generating an unnecessary planning artifact. Removing the checkpoint may shorten the visible workflow while transferring an unresolved decision into code. The evaluation needs to identify which duty caused the wait before recommending a smaller process.

<!-- C10-S03 -->
## Filter candidates with evidence

Chapter 9's comparison supplies mechanisms and gaps, not a league table. Selection should use those findings as constraints and questions. A supported documentary capability may justify investigating a profile. A demonstrated incompatibility may rule out that profile under current constraints. An unknown should remain an unknown until the team obtains the evidence it needs.

For example, the inspected GSD Core installation guide says Node 18 or later, while the same-pin package manifest declares Node 24 or later and npm 10 or later. That discrepancy does not establish that installation will fail. It does establish that the prose requirement alone is insufficient for an installation decision. A candidate environment must be tested and the actual package identity recorded. [Installation guide](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/install-on-your-runtime.md#L1-L10), [package engines](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/package.json#L68-L74)

The inspected AWS workflow implementation makes profile choice consequential. Its Classic and Express descriptions differ in stages, artifacts, reviewer behavior and guard settings; some human-presence or approval duties remain even where particular guards stand aside. “Uses AI-DLC” therefore leaves too much unspecified for selection or reproduction. [Pinned workflow profiles, lines 45–95](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/workflow-profiles.md#L45-L95)

AIUP supplies another kind of boundary. The inspected combined Node adapter targets NestJS, Drizzle, PostgreSQL and a Next.js frontend. Its workflow also says this adapter does not yet supply an equivalent of the coverage auditor described for certain other adapters. That is an adapter-specific qualification, not evidence that specifications cannot be reviewed in a Node project. [Node adapter scope](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/README.md#L9-L26), [coverage-auditor boundary](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L388-L417)

These examples show why a weighted total would be premature. A high score for documentation cannot cancel an incompatible mandatory stack. A low-confidence portability judgment should not become a numerical penalty for a capability we did not test. Record the constraint, the relevant evidence and what would resolve the uncertainty.

A useful candidate disposition has four possible states: investigate, conditionally retain, exclude for a stated constraint, or insufficient evidence. An unknown can matter differently for different duties. Unmeasured long-term benefit may be acceptable during exploration; an unknown mandatory runtime may block an executable pilot. Name the profile, the affected decision and the evidence needed to proceed.

### Reject a candidate for a stated local reason

A team can remove an arrangement from its immediate shortlist when an essential dependency is unavailable in the authorized environment. Record the dependency, the attempted setup or documentary conflict and the duty it prevents the team from fulfilling. Keep the reason tied to that environment.

If the dependency later becomes available, the decision record gives the team a precise reason to reopen the candidate. The earlier exclusion remains an account of the conditions at the time. This makes shortlist decisions easier to maintain as hosts, integrations and team responsibilities change.

<!-- C10-S04 -->
## Work through contrasting scenarios

The following scenarios are editorial decision exercises. Their project conditions are invented and explicit; no successful adoption or performance result is implied. They show how a team can make a provisional choice from documented mechanisms without pretending to know its later outcomes.

### A tiny, well-understood repair

Assume one developer understands a small presentation defect, the relevant code and accepted behavior are available, and the change does not alter policy, routes, authorization or persistent data. There is no demonstrated handoff problem to solve and the existing review record is current.

Our provisional decision is ordinary bounded change work with the compact record from chapter 2. We would not introduce a named full-process adoption for this task. The reason is the absence of a new coordination or specification-maintenance duty, not a general belief that small changes are harmless.

BMAD's inspected guidance permits a trivial direct edit and describes a bounded Build route for other small changes. This is evidence against forcing its full planning inventory onto every repair. It does not tell us how much effort our repair will take. [Small-change guidance, lines 15–23](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L15-L23)

Retain the constrained diff and meaningful navigation/regression evidence. If inspection reveals a shared permission change or a stale requirement, reopen the sizing decision. That observation would invalidate the conditions under which the small path was chosen. The exit criterion is therefore concrete: stop treating it as a presentation-only repair when the work changes a protected behavior.

### Defined intent with reviewable story checkpoints

Assume a small team has agreed the vendor-approval rules, wants a compact named specification, and needs a human checkpoint before implementing the first foundational slice. Team members are already familiar with the inspected BMAD path. Application constraints and an external acceptance inventory are available, while no project duty requires a permanent use-case catalog.

We would choose BMAD's specification/story/Build arrangement for a bounded evaluation, with optional modules stated explicitly. The documented story breakdown lets the operator choose checkpoints, and specification updates have a designated route. Those mechanisms match the declared work arrangement. This is not evidence that Core or AIUP could not address the same task. [Specification and checkpoint guidance](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/define-requirements-and-a-specification.md#L97-L124)

The selection record would name the capability/constraint trail to inspect, a first-story review decision and the external checks that must remain independent. Built-in QA would not be described as comprehensive acceptance. Enabling a larger testing module would change the evaluated configuration and its preparation cost.

Revisit the choice if the first checkpoint exposes undefined product intent, if maintaining the record creates unresolved contradictions, or if the actual host cannot support the review arrangement. The team should then fix the premise or compare another route, rather than keep generating stories to preserve the original selection.

### Multi-session work with phase continuity

Assume the main difficulty is recovering decisions and unfinished work across sessions. The team wants bounded plans, durable summaries and a verification record whose freshness can be checked. It has no fixed requirement to make a use-case catalog the enduring product record. For this exercise, assume the chosen Core package/runtime conflict has been resolved through actual environment checks; that premise is not a result from our book case.

We would choose the inspected Core phase loop as the first bounded trial. Its context/plan/summary arrangement and documented staleness policy address the declared continuity problem. The trial question is whether an interrupted episode can be resumed with the right current decisions, including the policy exception, and with stale verdicts rejected appropriately. [Phase loop](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L25-L59), [verification freshness](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/verify-and-ship.md#L106-L115)

The operator would retain the actual handoff inputs and the interruption/recovery point. Code review would be an explicit selected duty rather than assumed part of shipping. A summary-derived UAT list would coexist with independent CS checks, so omitted deliverables cannot define the whole oracle.

Revisit the choice if the recovered record requires substantial undocumented interpretation, if workers miss material constraints or if the required host behavior is unavailable. Those observations concern the scenario's reason for adopting the loop. A successful code-generation step alone would not answer the continuity question.

### Lifecycle coordination with explicit stage authority

Assume an organization needs one visible route from intent through construction into operational preparation, with different people owning consequential decisions. It can resource those handoffs and wants to inspect stage/unit authority explicitly. A local coding-only route would leave important duties outside the chosen arrangement.

We would start a documentary/configuration evaluation with the AWS workflow's Feature candidate, which the inspected chooser describes as a complete-lifecycle route. We would record active guard/reviewer settings and actual ownership rather than infer them from the profile name. The chooser's static stage counts do not establish elapsed effort or operational readiness. [Pinned profile chooser](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/workflow-profiles.md#L24-L43)

The first evaluation deliverable is a route/authority map: which person reviews which decision, which evidence reaches them and what constrains the next action. Operational exclusions or placeholders would be retained as open work. A route labeled Enterprise would not, by its label, establish compliance or better acceptance for this scenario.

Revisit the choice if the named owners cannot perform their duties, if local substitutions remove a mandatory operational check, or if the configured enforcement differs from what the decision record assumed. A solo simulation cannot establish that this organization will coordinate effectively.

### A maintained behavioral catalog in a compatible existing stack

Assume the organization already maintains requirements and use cases as a product record. Its application boundary is NestJS/Next.js with PostgreSQL, and it accepts the inspected Node adapter's construction assumptions. The team has explicit specification owners and resources for a manual coverage review where equivalent automation is absent. These are scenario premises, not technology selections for our common SaaS.

We would choose AIUP core plus the matching Node path as the first bounded evaluation. The documented artifact/change flow fits the desired maintenance duty, while the existing stack removes one obvious adapter mismatch. It does not prove compatibility of actual package versions or establish that the record will stay aligned. [Adapter scope](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/README.md#L9-L26)

The evaluation would follow one policy change from accepted requirements through affected use cases, implementation and checks. It would measure the real work of semantic review and reconciliation rather than count markers. The Node coverage-auditor limitation stays in the record; an explicitly resourced manual route is part of the arrangement.

Revisit the choice if maintaining the catalog creates unresolved duplicate rules, if adapter constraints force unaccepted architecture changes, or if coverage cannot be assessed under the available review capacity. The same principle would permit another framework to be investigated if it met the constraints more convincingly.

### Uncertain intent is an earlier decision

These selections assume enough agreed intent to define the evaluation question. If the team has not decided who may approve or how old requests behave, first produce a bounded decision record that exposes those choices. A detailed implementation plan cannot supply missing organizational authority. Progress in that stage is an agreed rule and visible uncertainty, not a completed application.

The examples deliberately make different decisions from different premises: use a compact ordinary path, trial a named specification/story route, trial phase continuity, inspect lifecycle authority or trial a maintained use-case flow. They are not a hidden ranking. Change a mandatory premise and the same procedure may produce a different next commitment.

<!-- C10-S05 -->
## Adapt practices without losing ownership

A team may want the planning path from one framework and a specification practice discussed elsewhere. That is a possible process design, but it creates new ownership questions. Which artifact is authoritative? Who may change it? What happens when the story and specification disagree? Which check establishes that downstream work has caught up?

BMAD's selected specification guidance designates `bmad-spec` as the writer of `SPEC.md` and directs updates through that skill. Adding a second workflow that edits the file directly would conflict with the documented maintenance rule. An adaptation must resolve that conflict rather than describe both policies as simultaneously in force. [Specification ownership, lines 112–116](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/define-requirements-and-a-specification.md#L112-L116)

Begin an adaptation by naming the problem it solves. Then assign one authoritative location for each decision and define the handoff. Preserve the native artifacts needed to understand the original process, or document exactly what has been replaced. If the adaptation changes mandatory behavior, describe the evaluated process as an adaptation; results from it should not automatically become claims about the unmodified framework.

Spec-Driven Development belongs in this discussion as an approach to organizing intent and change. Giving it a chapter does not require a fifth experimental arm. The relevant selection question is which specification policy the team needs and how that policy interacts with the chosen framework's lifecycle.

### A worked adaptation boundary

Suppose the team retains BMAD's named specification route and adds an external change-request queue used by its existing maintenance process. The queue entry describes the proposed v2 rule and affected customer behavior. It is an input to the specification owner; it does not become a second authoritative specification simply because another assistant created it.

The proposed handoff records the queue entry, the accepted policy decision, the specification revision and the downstream implementation/check references. A rejected request remains visible without changing accepted intent. If implementation reveals an ambiguity, the question returns through the same ownership route rather than being settled by an unreviewed edit to the specification.

The adaptation record must say which native duties remain and which have changed. It should identify any new manual work and any automated behavior the arrangement no longer uses. Merely retaining a familiar command or filename is insufficient to claim that the unmodified framework was evaluated.

Before adoption, review a change in each direction: an accepted policy change moving toward implementation, and an implementation discovery returning to the policy owner. The aim is to inspect the handoff, not to generate two independent documents that happen to agree initially. Their first disagreement is exactly the event the ownership rule should handle.

This is an original process-design example, not a tested integration. The narrower adoption decision is whether the proposed ownership boundary is understandable and feasible for the team. Later execution would need to establish whether people and tools actually follow it.

### Define an interface between a new workflow and the team's existing controls

A team may want to adopt the planning part of a workflow while keeping its current release review. Start by specifying what the existing reviewer needs to receive. For a stateful policy change, that might be the accepted behavior, a migration decision, the candidate revision and evidence about older requests. An integration can translate native records into that packet as long as each item retains its origin and scope.

Suppose the planning record marks all stories complete while the release review awaits a rehearsal. The integration should carry both statuses and attach them to their decisions. If it maps them to a single “complete,” the release owner loses information. If the process requires the reviewer to reconstruct every native artifact, the integration has transferred the manual work to the wrong person. A short record that points to the actual decision and observation often suffices.

Try this interface on one bounded change and inspect what happens when an observation is stale. The team should be able to replace that observation and retain the historical record. If each refresh requires copying entire reports, narrow the interface. If essential policy details are lost in the translation, add the missing reference before expanding adoption. Record the adapted arrangement as the object of evaluation.

<!-- C10-S06 -->
## Pilot, measure learning and define an exit

A reversible pilot should answer one bounded question. For the common case, one candidate question is: can the selected path carry CS-04 and CS-05 into a reviewable decision implementation while retaining CS-03's tenant boundary? The full case contains additional obligations; this question defines a smaller learning scope, not permission to omit them from final acceptance.

Before a run, record the exact profile, baseline, host/model settings, permitted interventions, independent checks and resource ceiling. If a field is unresolved, the trial is not reproducible yet. Setup and adaptation effort belong in the record alongside active implementation effort. Human waiting, agent work and elapsed duration are different observations; combining them into an unexplained speed number hides the allocation of work.

Define exit conditions in advance. Stop the trial if the environment cannot be reproduced, required checks cannot be executed, an unresolved product decision would change the task, or the agreed resource ceiling is reached. Preserve the partial output and the reason. A stopped run can reveal an adoption obstacle; it should not quietly disappear from the comparison.

Success criteria should concern the question. The trial might establish that required artifacts can be linked and the independent checks executed under the selected configuration. It would not, by itself, establish a long-term maintenance benefit or predict another team's productivity. The team should name the additional observation that would justify expanding the evaluation.

This book has not executed that pilot. The companion [case walkthrough](case-walkthrough.md) describes the proposed evidence boundary. The readiness checklist and later run records must supply the execution evidence.

### Budget the investigation before estimating a return

A useful pilot budget separates the effort of making a candidate evaluable from the effort of completing the business episode. Installing a host, resolving package requirements, learning the native path and preparing an adapter can all consume real capacity. Whether they are inside or outside the episode's timed interval must be stated before work begins; neither choice makes them disappear from adoption cost.

Use a blank effort ledger with activity, responsible role, start/stop rule, evidence locator and accounting category. Categories can include preparation, native planning, implementation, review, policy clarification, waiting and recovery. Overlapping agent and human activity needs a declared counting rule. Adding their durations as if all work were sequential would answer a different question from wall-clock completion time.

Do not convert this ledger into a return estimate without a meaningful comparator. A pilot can establish the effort observed for its own arrangement. It cannot show time saved against an unobserved alternative. Likewise, an operator's familiarity is a condition to record, not a reason to assume that every future team will incur the same learning cost.

Include stopped attempts in the investigation account. A blocked installation may leave application correctness unassessed while still revealing an adoption obstacle. An unavailable reviewer may make a particular process arrangement infeasible under the team's staffing conditions without proving a defect in its written method. Keep the observations and their interpretation separate.

The next commitment can be deliberately small: retain one useful record, investigate a different profile, repeat with an independently reviewed contract, or return to the existing process. Before leaving a trial, identify any accepted decisions that must be transferred, preserve the native evidence and remove reliance on temporary automation. Reversibility is a procedure for recovering ordinary work, not simply a promise that the team can stop.

A longer adoption should need an additional learning question. For example, does the same ownership arrangement remain understandable during a later policy change performed by someone else? That question requires new observations. It cannot be answered by extending the interpretation of a single successful feature episode.

### Specify what would cause you to end the pilot

A team choosing a workflow for multi-session maintenance can set a stop condition around handoff. After the first bounded change, ask a second operator to find the accepted policy, distinguish current from stale verification, and complete the next authorized step. If they need an undocumented assumption from the first operator, record where the handoff failed. The team can try a bounded correction and repeat the same exercise on a fresh change.

Set a separate exit condition for setup. If the chosen host cannot provide the necessary review or permission boundary under the agreed configuration, the pilot can end with a compatibility finding. Record work completed before the stop and preserve any useful artifact. A later configuration change can justify a new attempt with its own baseline.

<!-- C10-S07 -->
## Write and revisit the decision

The selection deliverable is a short decision record that another engineer can challenge. Use the following original template:

| Field | Required entry |
|---|---|
| Decision question | One bounded problem the evaluation is intended to resolve |
| Context and constraints | Codebase, ownership, lifespan, application/host constraints and required acceptance duties |
| Candidates | Exact source/package/profile/module scope; tool context recorded separately |
| Evidence | Source passages or run records, each with its limited interpretation |
| Disposition | Investigate, retain conditionally, exclude for a specific constraint, or insufficient evidence |
| Costs and uncertainties | Known adaptation work and unmeasured effort; unresolved compatibility or review limits |
| Pilot contract | Baseline, checks, resource ceiling, permitted interventions and stop conditions |
| Owner and revisit trigger | Who decides; which observation or changed constraint reopens the choice |

For our book, the present disposition is to retain four framework subjects for documentary comparison and possible later controlled evaluation, with SDD treated across them. Contemporary Core is the explicit working GSD prose scope. BMAD's pinned source supplied the earlier method pilot prose; that writing choice does not appoint it as the production process for the SaaS or freeze installed packages, host or stack.

Here is a populated example for the policy-change episode. It is an editorial decision exercise, not an approved run contract:

| Field | Example entry |
|---|---|
| Decision question | Which profile should enter a bounded evaluation of the high-risk approval-policy change? |
| Fixed intent | New high-risk v2 requests need two distinct eligible approvers; existing v1 requests keep v1 semantics; tenant isolation and no self-approval remain required |
| Starting condition | The same externally prepared baseline for every arm; TypeScript / Node.js family only, with exact stack and host still open |
| BMAD candidate | Investigate the inspected specification/Build path; check whether the version-binding rule reaches the implementation record and acceptance evidence |
| GSD candidate | Contemporary Core for the prose; confirm the installed edition/package and resolve the guide/manifest runtime discrepancy before an install-based trial |
| AWS AI-DLC candidate | Retain for investigation; name the implementation, profile and guard configuration rather than treat the lifecycle label as the complete intervention |
| AIUP candidate | Retain for investigation; verify whether the selected adapter fits the common stack and assign an explicit coverage-review route |
| Current decision | Prepare comparable profiles and checks; do not name a winner or start measured runs while the mandatory inputs remain unresolved |
| Revisit trigger | A reviewed environment and acceptance contract, or evidence that a candidate cannot satisfy a fixed constraint without changing the experiment |

The table turns uncertainty into work. GSD needs a compatibility answer, AWS needs a configuration identity, AIUP needs an adapter/review route, and BMAD needs a checkable artifact path. These are different questions, not equal numerical penalties. A team with already fixed constraints could reach a different shortlist; this example preserves the choices the book has actually made.

A later decision can change without invalidating this record. A resolved compatibility conflict, a different application constraint or an actual pilot observation may alter the choice. Record the new evidence and preserve the earlier reasoning. The purpose of selection is to make a defensible next commitment with a clear way to learn from it.

### Leave a decision that can be revisited without reopening the whole selection

A completed selection record can name the local need, chosen arrangement, configuration and reason for accepting its dependencies. It should also name the next observation. For example, after choosing a persistent-context workflow for interrupted maintenance, observe whether the next operator can recover the accepted rule and the current verification boundary.

Give reevaluation a trigger. A failed handoff, changed host capability or new release responsibility can reopen the relevant part of the decision. The original choice remains understandable with its earlier conditions. The team can then revise the configuration or choose another arrangement with a clear account of what changed.
