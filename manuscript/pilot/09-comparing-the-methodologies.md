# 9. Comparing the Methodologies

> Author manuscript · completed 2026-11-05 · C09 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C09-S01 -->
## Check what is being compared

The four deep dives describe different arrangements for making decisions, carrying context and checking work. Bringing them into one table does not make their scope equal. First identify the common business task and the selected source/profile for each arrangement.

Our documentary subjects are BMAD's inspected stable source, GSD Core's contemporary continuation, the inspected AWS workflow implementation/profiles and AIUP core with its Node-path qualifications. SDD supplies a lifecycle lens across them. Hosts, optional modules and application adapters remain dependencies of the intervention rather than additional peer methods.

The common task is the vendor-access increment and its later change/repair episodes. Requirements and intended starting conditions come from the book's case design. Native artifacts can differ. A comparison that forces AIUP use cases onto every arm or removes a required planning step to equalize file counts would change the methods being evaluated.

Record source and installed-package identities separately. A matching version string does not prove equivalent contents; the [version-provenance review](../../research/CONTESTED_CLAIMS.md) records source-versus-release differences. Until an actual environment is frozen and checked, the tables below compare inspected mechanisms only.

The same limit applies to operator and model conditions. If one arrangement receives a larger resource budget or additional manual architecture work, report it. Such an exercise can still describe a useful configured workflow, but it cannot isolate a method effect without further controls.

The instrument remains F01–F11 from chapter 3. The chapter groups related questions for readability while retaining every dimension. It asks which mechanisms are documented, which dependencies alter them and which outcomes remain unsupported. Chapter 10 owns scenario selection; this chapter supplies its evidence boundary.

### Build a comparison row that can survive a profile change

Start a row with one business obligation and one question from the comparison instrument. For example, pair the v1 preservation rule with the question of how implementation workers receive a current decision. Give each row a source identity and a scenario, then specify what observation could change the row. A source revision can support a claim about a documented mechanism. A work record from a configured run would be needed to say how that mechanism behaved in the scenario.

For the proposed E2 exercise, freeze the same starting code, fixtures and v1 behavior for each arrangement. Record the native artifacts that each approach expects the operator to create or update. Different artifact names and sequences are acceptable. Compare whether the work received the preservation rule and whether the resulting implementation honored it. The comparison should still show where each method stored the rule and how the operator found it.

If a profile changes, create a new row with its own scope. An assessment of an optional review path cannot be transferred to a default profile simply because the repository contains both. If a later release replaces a verification step, the earlier row remains interpretable with its original pin. This keeps the chapter's documentary findings usable when readers evaluate an installed version of their own.

<!-- C09-S02 -->
## Compare decision rights and planning

F01 asks who may decide and how the decision constrains the next action. F02 asks how much preparation the selected route requires for the work. A framework's most elaborate route is not automatically the right comparison for a tiny repair.

| Source scope | Documented decision/planning mechanism | Qualification |
|---|---|---|
| BMAD | Intent-sized planning and a light versus flagged-plan Build path | Approval is prompted where the selected design requires it; enforcement and cost were not tested |
| GSD Core | Discussion decisions feed bounded plans and later verification | The phase loop can be disproportionate for tiny work; a quick path is described |
| AWS workflow | Profile-specific stages, checkpoints and guard policy | Configuration and overrides are part of the intervention; oversight is not one universal setting |
| AIUP core/Node path | Owned specifications, scoped decision rights and path-specific implementation rules | Layered defaults must not be generalized to every adapter; tiny-task overhead remains unmeasured |

Primary support: [BMAD routing](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L62-L92), [Core sizing](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L77-L90), [AWS profiles](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/workflow-profiles.md#L45-L95), [AIUP scoped rights](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L319-L357).

The table supports conditional questions, not effort rankings. BMAD and Core explicitly allow smaller routes, but we have not measured their use. AIUP's durable artifact structure does not prove that every task requires rewriting every artifact. AWS profile reduction changes coverage and must be evaluated against the scenario's actual duties.

For the two-approval change, the decisive product question is creation-time policy binding. The decision owner must settle it before an implementation silently chooses retroactivity. Each method provides a different place to record that answer. The evaluation should ask whether it remained available and constrained later work.

Human gates also differ in strength. An instruction to ask, a recorded approval and a mechanically enforced boundary require different evidence. The AWS hook's inspected disable branch is one concrete reminder that source configuration matters; it is not a comparative security audit. [Selected static branch](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/core/hooks/aidlc-plan-approval-guard.ts#L2391-L2397)

Planning cost should include relevant setup, review and repair. A route that quickly generates code but needs extensive policy correction may compare differently from one that front-loads the decision. Without actual observations and a declared accounting policy, that remains a question rather than a result.

### Compare the decision an operator has to make

Imagine giving each arrangement the same request to support dual approval. The first comparable moment is when the operator decides the work is ready to move into implementation. The reviewer can inspect what the proposed plan says about existing requests, who supplied that answer, and what records the implementer receives. A conditional approval that asks for a missing v1 fixture has a different meaning from an approval with no stated conditions. Preserve the condition and check whether it survived handoff.

The next comparable moment is a late policy question. Suppose an implementer notices that one actor can hold two approver roles. The accepted requirement counts distinct actors, so role count cannot satisfy it. A useful handoff lets that implementer find the rule and update the plan without requesting a new product decision. If the rule is absent, record the clarification, the operator's intervention and where it entered the remaining work.

| Observation sought | Record to inspect | What remains unresolved |
|---|---|---|
| Decision was available at handoff | Accepted decision and actual worker inputs | Whether the implementation followed it |
| Approval constrained execution | Reproduction of a blocked unapproved action under the frozen configuration | Whether other execution paths enforce the same boundary |
| Planning effort was incurred | Defined record of operator actions and time categories | Whether the effort generalizes to another team or task |

These are proposed observation rows. A documentary review can point to where an operator should look, while a trial has to retain what actually happened at each moment. Keeping the levels distinct also allows an investigator to report a useful mechanism whose enforcement remains untested.

### Compare review authority under the same interruption

A useful future exercise stops each configured workflow after an owner has accepted a policy clarification and before all implementation tasks consume it. Give the next operator access to the same repository and its native records. Ask them to find the accepted decision, identify which tasks have consumed it and decide whether the next action is authorized. The interruption should preserve the same business state in all arms while allowing each arrangement to persist its own artifacts.

A comparison record can distinguish three observations. First, can the operator find the accepted rule? Second, can they identify the revision it governs? Third, does the arrangement expose which work remains blocked or stale? Finding the rule is weaker than showing it constrained the next action. An attempt that resumes correctly only after the prior operator supplies missing context should record that intervention.

The evaluator should decide how to handle operator familiarity. A person who wrote the first plan can sometimes infer missing context from memory. A second operator can expose handoff gaps but also introduces different experience. One proposed design gives each operator the same familiarization task and repeats the exercise across several arrangements in varied order. Report the preparation and order so the reader can inspect their possible influence. A small trial can still describe a failure mechanism without estimating a general effect.

<!-- C09-S03 -->
## Compare artifacts, context and change

F03–F05 examine artifact lifecycle, traceability and context. F07/F11 extend those questions into existing systems and maintenance. These dimensions converge when a policy changes: which record owns the new intent, which work receives it and what proves reconciliation?

| Source scope | Persistent structure to inspect | Change/context question |
|---|---|---|
| BMAD | Named specification, linked stories/implementation records and current project context | Do skill-mediated updates preserve the right constraints while stale greenfield material is kept out of ordinary changes? |
| GSD Core | Phase decisions, research/plans, summaries, state and verification | Do bounded workers receive complete current decisions, and can the next session reconstruct unfinished work? |
| AWS workflow | Intent, workflow state, audit and boundary-verification records, with transient engine state distinguished | Which evidence survives a handoff, and which profile/route produced it? |
| AIUP | Requirements, use cases, domain/architecture context and downstream implementation/test links | Are applicable constraints linked and reconciled through the selected construction path? |

Primary support: [BMAD specification policy](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/define-requirements-and-a-specification.md#L97-L124), [Core record flow](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L25-L59), [AWS retained/transient records](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/14-artifacts-reference.md#L25-L54), [AIUP inputs/change](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L475-L494).

Durability has several meanings. A phase archive preserves process history. A behavioral specification is intended to guide future changes. A local engine cache supports execution. Treating all three as equivalent documentation would obscure the maintenance policy.

Traceability also needs three questions: are links present, do they cover the relevant obligations, and do the linked checks actually exercise those obligations? A plan, code marker and passing assertion can share CS-05 while testing an already terminal request. Their agreement would leave the self-approval rule unestablished.

For E2, inspect the same semantic probes across native artifacts: new high-risk v2 threshold, distinct approvers, preserved v1 semantics, unchanged tenant/self-approval constraints, and refreshed acceptance. An artifact count cannot answer those questions. Neither can a generated summary that merely declares completeness.

Brownfield guidance must distinguish observed from intended behavior. A reverse-engineered record can accurately describe a defect. An existing-code-first route can preserve an undesirable pattern. A specification-led route can impose stale behavior. The evaluation needs the accepted change contract and repository evidence together.

The sources give us different mechanisms for this work. They do not establish long-term maintenance benefit. That would require multiple changes, meaningful follow-up, contradictory artifacts and the effort needed to repair them. The current synthetic case has no such observations.

### Evaluate recovery after a contradiction

Use a controlled discrepancy to see what the records make visible. In a future experiment, the operator could compare a plan saying “v1 requests keep their policy” with an implementation summary that implies the current setting governs all pending requests. Before changing either, determine whether the summary describes observed code, a proposed change or an unverified interpretation. An accurate summary of a defect should remain available as evidence while the intended rule guides the repair.

A reviewer can inspect four handoff properties. Find the accepted decision without relying on chat history. Identify the exact implementation revision the summary describes. Follow the rule to an acceptance example that exercises a pre-existing request. Identify who can resolve the contradiction. Record the steps needed in each native arrangement and any extra interpretation supplied by the operator.

The comparison remains sensitive to starting conditions. An arrangement beginning with a curated behavioral contract has a different context advantage from one beginning with an incomplete issue. Give all arms the same business decision and repository baseline. Allow the native arrangement to organize those inputs, then record any manual translation. The translation can be legitimate preparation and still matters when estimating adoption work.

### Compare maintenance records by the question they let a reader answer

An artifact can be useful even when it is short. Ask a future maintainer to explain why the request keeps a stored version. A decision record with the accepted behavior and rationale can answer that question. A detailed task log can explain which files changed. A verification result can show what was observed. Give each record the job its evidence supports.

A future evaluation can supply the same maintenance question to each configured arrangement and retain the reader's path to an answer. Record which native artifact they opened, whether it identified the accepted decision and whether they needed additional help. Then ask them to locate the implementation and observation affected by a proposed change. This second task exposes whether discoverability extends beyond a single well-written note.

Avoid rewarding artifacts merely for being numerous or penalizing them for being specialized. A workflow may keep a useful decision in one record and a useful check in another. The relevant question is whether their relationship is inspectable when it matters. If an operator has to manually assemble that relationship, retain the effort as part of the configured workflow.

This exercise also needs a stable task. A record for a large architectural change may naturally contain more context than one for a bounded bugfix. Hold the business question and starting state constant while allowing native representation. If a method requires a broader preparation step, record what it contributed and how much work it added before interpreting the result.

<!-- C09-S04 -->
## Compare verification, operations and portability

F06 and F08–F10 address people, acceptance, operations and dependencies. These are especially easy to overstate when a workflow includes named review roles or a delivery stage.

| Source scope | Verification mechanism or boundary | Operational/dependency limit |
|---|---|---|
| BMAD | Built-in generated QA differs from optional TEA and has explicit coverage limits | Host capabilities affect reviewer dispatch; comprehensive operations were not established in this inspection |
| GSD Core | Summary-derived UAT, gap closure and stale-verdict handling; code review is separate/optional | Shipping a PR does not establish production operation; runtime prerequisites conflict in the inspected source |
| AWS workflow | Profile-specific checks, reviewer behavior and gates | Operations can be reduced/placeholder; team and guard configuration change the intervention |
| AIUP core/Node | Deterministic spec lint, semantic advice, tests and human acceptance records | Node stack assumptions and the equivalent-auditor limitation must remain explicit |

Primary support: [BMAD QA limits](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/test-completed-work.md#L76-L105), [Core verification/shipping](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/verify-and-ship.md#L9-L89), [AWS profiles](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/workflow-profiles.md#L45-L95), [AIUP auditor boundary](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L388-L417).

No cell is a test result. The book has not installed the four arrangements, run a common oracle or observed a human team. Where a mechanism is documented, its actual use and efficacy remain separate questions.

A local exercise can establish selected behavior under synthetic conditions when executed. It cannot establish a team's coordination benefit, enterprise suitability or production resilience. A process may integrate with existing organizational practices; those practices and their effort belong in the evaluated arrangement.

Portability has the same evidential boundary. A host adapter or stack plugin demonstrates an intended integration path. It does not prove equivalent hooks, permissions, reviewer dispatch or generated application behavior on another environment. A migration/smoke exercise needs its own inputs and records.

The TypeScript/Node case exposes this issue directly. The AIUP adapter's framework/database assumptions and Core's runtime discrepancy affect setup. Choosing a common stack could advantage or constrain particular integrations. The design must disclose that choice and count adaptation rather than silently make portability free.

### Read a verification record at the right boundary

Suppose a native status reports completion for E2. Ask for the observations underneath it. A status backed by a reviewed plan, a compilation log and two policy-function checks may be accurate according to the workflow's own rules. Acceptance of the common business increment still needs a pre-existing v1 request and a high-risk v2 request exercised through the relevant service boundary. Count the status once as workflow evidence, and use the underlying observations only for the claims they support.

The same separation applies to approval enforcement. A transcript showing a prompt and a human answer documents one interaction. A controlled attempt to proceed without the answer can inspect enforcement on the selected path. Record the actual environment and settings before interpreting either. A capability supplied by the host, such as an approval dialog or process isolation, belongs in that environment record rather than being attributed automatically to the methodology.

For an existing repository, include recovery from a stopped or expired session in the evaluation. Ask a different operator to identify unfinished work from the retained records, with the same authorized repository access. Record which decision or check needed help, and whether native records were current. This proposed exercise addresses handoff. A delivery claim also needs observations about the actual release boundary and about how people respond when that boundary fails.

### Record adaptation where it happens

Suppose a native workflow assumes a certain way to dispatch independent work, and the selected host exposes a different set of capabilities. An operator can adopt a manual handoff that preserves the intended division of responsibility. The resulting trial should identify that change. An evaluator who calls the setup stock would attribute part of the outcome to the wrong component.

Describe the adaptation at the affected step. Include the expected behavior, the constraint that required a change, the replacement action and the artifact it produced. If the operator manually copies an accepted decision into a work packet, record whether they merely transfer the decision or also interpret and expand it. The latter can change which business context the implementer receives. It may be appropriate in practice and still matters for comparison.

A similar issue arises when an organization adds its ordinary deployment process to each arrangement. Record which controls are shared and which controls come from the selected configuration. A common independent acceptance check can be a deliberate constant. Different amounts of manual setup or repair belong in the account of each attempt. Keep a clean distinction between evidence that an arrangement can be made to work and evidence about how much work that took.

A reviewer can use a short adaptation log during analysis. If one result depends on an unusual recovery procedure, describe the procedure and its scope before comparing it with other outcomes. If the procedure will be available to all future users, include it in the reproducibility packet. If only one operator knows how to perform it, the result may still be informative while remaining dependent on that operator.

<!-- C09-S05 -->
## Read gaps, conflicts and observations

Missing evidence does not have one meaning. We have documentary support for some mechanisms, an explicit source conflict for Core installation requirements and no execution outcomes. Preserve those states rather than turn them into a numerical scale.

The comparative preprint reviewed for this book provides useful prior documentary work, but its dimensional scoring is single-rater judgment with disclosed limitations. Such scores are not framework-effectiveness measurements. We do not import them or claim to be the first comparison. [Prior taxonomy/comparison paper, method and limitations](https://arxiv.org/html/2606.04967v1)

Source confidence is also claim-specific. Confidence that a pinned file contains an instruction does not transfer to confidence that the instruction succeeds. A maintainer's exact terminology may be well established while an outcome claim remains interested-party evidence. A field account can expose a particular failure without establishing its frequency.

Our current outcome disposition is deliberately simple:

| Outcome | Current book evidence |
|---|---|
| Implementation acceptance under the common oracle | Not run |
| Human effort or elapsed-time advantage | Not assessed |
| Defect detection or repair advantage | Not assessed |
| Human-team coordination | Not observed |
| Production operation/recovery | Not exercised |
| Long-term artifact/code alignment | Not assessed |

Those entries describe the project, not an absence of all evidence everywhere. The literature search was directed and bounded. A new well-described study could change the assessment, provided its task, versions and conditions match the claim being considered.

The separate local policy-model checks described in chapter 11 do not fill this table. They exercise an author-written sequential function, not four installed processes against the common application oracle. Their passing result is useful executable teaching evidence with a much narrower scope.

If later trials occur, retain failures and deviations. Installation failure leaves business behavior unassessed; a failed acceptance assertion addresses behavior under its fixture. A run completed after large human redesign must include that intervention. Missing attempts should not disappear from a favorable summary.

When sources conflict, keep the conflict visible and define what would resolve it. The Core guide/manifest discrepancy calls for installed-artifact and compatibility checks, not averaging runtime requirements. A profile-specific AWS statement calls for configuration identification, not a global verdict about all AI-DLC work.

### Keep denominators visible when work stops early

Consider four hypothetical attempts in a future evaluation. One stops at installation, one builds and fails an acceptance check, one passes after manual redesign, and one is interrupted by an unrelated outage. Give each attempt a row and record the stopping condition. The installation result informs compatibility under the selected setup. The acceptance failure informs the behavior of the built revision. The manually repaired pass is a result for the configured workflow with the repair included. The outage leaves the interrupted outcome unresolved.

An effort comparison across only the finished attempts would lose both the setup burden and the interrupted work. Report the population for every statistic or qualitative claim. If setup was shared, say how it was accounted for. If a single operator gained experience between attempts, keep the ordering and familiarization history visible. Reusing an accepted baseline for E2 can reduce carryover from E1, while operator learning still needs attention.

The book's present documentary exercise has no such attempt rows. Readers can use the distinctions to review other reports. Ask what was eligible to enter the study, how incomplete attempts were treated, and whether a result depends on help that another team would need to reproduce. An apparent performance advantage can become a narrower statement about a particular team, version and starting point once those conditions are recorded.

### Give uncertainty a consequence in the report

An unresolved source conflict should change what the reader can act on. If a runtime requirement differs between a guide and an installed manifest, the report can describe the conflict and withhold an installation recipe until a smoke exercise resolves it. A claim about a configured approval guard can be supported for a named path while the report leaves other hosts open. Assigning both situations a generic low-confidence badge hides the next action.

For a documentary comparison, pair each important gap with an evidence request. A missing package identity needs the installed artifact and its provenance. A missing enforcement observation needs a controlled attempt with and without the prerequisite on the same path. A missing maintenance outcome needs another change and a way to inspect whether decisions remained discoverable after it. None of these requests needs a universal numerical confidence scale.

Then ask which decisions can proceed. A team can shortlist a method because its documented records are relevant to a handoff problem, while keeping installation and continued use conditional on its own pilot. A book can describe the documented mechanism and refrain from publishing comparative outcome claims. This makes uncertainty part of the decision record.

### Compare the evidence before comparing the apparent result

Imagine two proposed reports on the same change. The first names the selected configuration, the revision, and the accepted criterion, and says the acceptance check could not be run. The second says the change passed, but provides only an aggregated green status. The first report supports a clear statement about where the attempt stopped. The second requires more information before a reviewer can decide what passed.

A reusable comparison record separates a method claim, a local observation and an interpretation. For example, the method claim describes a documented place for persistent decisions. The local observation identifies whether a second operator found the governing rule after interruption. The interpretation explains whether any missing context affected the next action. Each entry has its own evidence and can be revised when new material appears.

Ask how the reported finding could be wrong. An operator may already know the expected policy and find it faster than a new contributor. A seeded record may sidestep the path that introduced the defect. A report may capture an approved plan while omitting a later manual change. The comparison can retain these alternatives and propose follow-up observations without forcing every outcome into a shared numerical ranking.

<!-- C09-S06 -->
## Tradeoffs the evidence supports

The strongest current finding is that the selected arrangements expose different structures for the same engineering duties. BMAD makes planning-path choice and a named specification/Build trail explicit. Core emphasizes persistent phase decisions and bounded context/workers. AWS makes lifecycle routing and configuration a large part of the intervention. AIUP emphasizes maintained behavioral artifacts and scoped construction/review paths.

These are documentary differences, not benefit scores. They suggest questions about adoption and maintenance cost. A small route can be appropriate for a clear repair; a durable specification can help inspect a policy change; a configured lifecycle can expose wider duties. Which arrangement fits depends on the actual constraints and on evidence that its mechanisms work there.

All four need an external interpretation of accepted behavior. Generating a plan, test suite or review report does not establish its correctness. The common CS contract and eventual independent checks exist to keep the comparison's target stable while native work differs.

The SDD lens adds policy questions without a fifth arm. Which specifications persist, what do humans edit, and how is disagreement resolved? Answers can differ by artifact within one framework. Strictness of edit policy is not an effectiveness ranking.

### Form a conclusion someone can challenge

A defensible documentary conclusion names a mechanism, its scope and what would overturn the interpretation. For example, a team can treat a maintained behavioral artifact as a candidate source of context for future changes. To evaluate it, give a later contributor a versioned policy change and ask them to find the governing rule, update its dependents and expose stale evidence. If they need an undocumented decision from the original operator, the result identifies a handoff gap under the tested conditions.

Use the same standard for light routes. A smaller procedure looks appropriate for a well-understood repair when it preserves the relevant decision and produces adequate verification. A later evaluation can compare the amount of preparation with the completeness of the repair record. If the work depends on an unresolved tenant contract, the smallest route might reasonably pause at clarification. That pause belongs in the report and can be the correct outcome for the scenario.

The selection record in chapter 10 can carry the resulting conditions forward. State the local need, choose an arrangement whose documented mechanism addresses it, and name the observation that would justify keeping or revisiting the choice. For an organization, the useful decision is often about one workflow and one environment. That level allows the team to learn from the evaluation and allows another reader to decide which parts apply to their own setting.

### Read a mixed outcome without compressing it into a winner

Consider a hypothetical exercise in which one configured arrangement makes the policy decision easy to find but needs manual work to refresh evidence. Another makes the review report easy to regenerate but requires a conversation to recover which version rule applies. These are distinct observations about handoff and verification. Reporting them side by side preserves the information a team needs to choose.

A maintenance team with frequent interruptions may prioritize recovery of accepted intent and accept some manual verification work. A team with a stable owner but frequent releases may prioritize evidence freshness and add an explicit decision record to the second arrangement. Either team needs to check its adaptation on a subsequent change. A favorable observation about the original arrangement cannot by itself establish the effects of the adaptation.

The report can carry forward conditions for transfer. Identify the repository shape, the selected scope, the available integrations and the duties supplied by the team. If a reader wants to apply the result to a regulated release or an architecture with different data ownership, those differences become part of a new evaluation. The documentary comparison can suggest which native mechanism to inspect without guessing how it will behave under those conditions.

Chapter 10 turns this evidence into scenario-based choices and a reversible evaluation record. Chapter 11 presents the full qualitative case and its missing execution controls. A later measured study would add observations to these mechanisms; it must not be invented to make the table look complete.

### Carry a qualitative finding into a local decision

A comparison can finish with several findings whose conditions differ. One arrangement may make an accepted decision easy to locate. Another may supply a more useful verification handoff. A third may require setup work that the team's environment cannot currently support. Write each finding with its task, configuration, observation and unresolved alternatives.

A local decision can then select one finding to investigate. For an interrupted maintenance workflow, the team might prioritize discovery of accepted intent. It can shortlist arrangements with relevant persistent records and plan a recovery exercise. For a release workflow, the team might prioritize the relationship between candidate identity and evidence. It can inspect that handoff using a stale observation and a revised candidate.

The comparison supplies reasons to choose an exercise and a candidate. The local exercise supplies observations for a decision under the team's conditions. Keeping that sequence visible gives another reader a way to challenge a premise or repeat a bounded check.

For a report, use one row per conclusion and include an evidence request beside any unresolved claim. If the configuration changes, revisit the affected row. This preserves useful distinctions without making the entire comparison depend on a single aggregate verdict.
