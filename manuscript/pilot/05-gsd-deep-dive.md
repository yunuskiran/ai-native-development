# 5. GSD — Deep Dive

> Author manuscript · completed 2026-11-05 · C05 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C05-S01 -->
## Name the lineage and snapshot

GSD's role in this book is the process layer: how decisions, plans, work and verification are organized. A coding-agent product sharing related naming is outside the peer-method comparison. The distinction matters because an interface feature, model integration or product subscription is not automatically part of the process being examined.

The inspected former repository directs readers to `open-gsd/gsd-core`. That notice establishes a declared continuation, not a complete founding or ownership history. We use a pinned Core source for the contemporary workflow discussion and retain the requested chapter title. [Inspected migration notice](https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/README.md#L1-L12)

The intervention we can examine is therefore specific: the phase-loop design and related verification guidance at `72c4e14…`. We have not installed that source or established that a published package delivers identical instructions. The chapter asks what the source prescribes, then designs a way to inspect its consequences for the common task.

One compatibility discrepancy illustrates why the pin matters. The same source's installation guide says Node 18 or later, while the package manifest declares Node 24 or later and npm 10 or later. A prose prerequisite is not sufficient to freeze an environment when its manifest disagrees. This is a documentary conflict, not an observed failed installation. [Guide](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/install-on-your-runtime.md#L1-L10), [manifest](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/package.json#L68-L74)

For the SaaS example, the chosen language family remains TypeScript / Node.js. That does not resolve the discrepancy or select a web framework. A future executable profile must identify both the workflow's installation environment and the application's runtime. Those may impose different dependencies.

The distinctive design question is continuity: can bounded workers act on explicit decisions while persistent records make the larger work resumable? File-based continuity is a mechanism to investigate. Its existence does not establish that workers received the right information or that a later session interpreted it correctly.

<!-- C05-S02 -->
## Discuss decisions before decomposition

The phase-loop guide places discussion before planning. Discussion records implementation decisions in `CONTEXT.md`; the subsequent planning activity reads those decisions alongside research. The purpose described by the source is to make preferences and constraints available before an executor chooses a plausible alternative. [Discussion and planning](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L25-L59)

For the approval increment, distinguish three kinds of input. Business behavior includes current same-tenant eligibility and no self-approval. Project constraints include the existing application boundary and conventions. Unresolved implementation decisions include the exact persistence/interface design where the shared contract has not settled it. A discussion should not make the third category override the first.

Suppose an operator says, “Administrators normally approve requests.” That preference must be reconciled with CS-05 before plans are written. In our case, an administrator who requested the item is still disqualified. Recording the preference without its exception could give a planner a coherent but incorrect rule.

The useful discussion result is therefore a set of decisions with boundaries. The following is an original content sketch, not a generated Core file:

| Decision to carry | Proposed case content | What remains unresolved |
|---|---|---|
| Approval eligibility | Current approver membership in the request's tenant; requester excluded | Exact identity fixture and interface contract |
| Existing behavior | Preserve valid pending/terminal rules and tenant-local reads | Baseline implementation has not been prepared |
| Retry semantics | Apply the frozen identical-key/payload contract when one exists | Scope, retention and conflict response of the key |
| Policy transition | Bind a request to its creation-time policy | Technical representation and migration procedure |

These entries keep an answered business question from being reopened accidentally and an unanswered technical question from looking settled. A future record should also identify who supplied each consequential answer. A conversation that contains the answer is useful; a persistent summary must preserve its meaning.

Discussion has a stopping point. It should resolve the decisions needed for bounded planning, not become an indefinite interview about every possible product feature. If an uncertainty does not affect this increment, record its exclusion. If it affects acceptance, resolve it or explicitly stop the affected work. The question is whether the planner has enough agreed information to avoid inventing business policy.

For an established application, answers may come from repository evidence. A current route, accepted decision record or maintained convention can settle an implementation choice. The source of that answer matters: matching current code is appropriate only where the intended change does not correct that code's behavior.

### Make a decision recoverable outside the conversation

A decision record needs its scope as well as its answer. For E2, two approvals is incomplete. The recoverable decision is that newly created high-risk v2 requests need two distinct eligible contributors, while standard-risk v2 and existing v1 requests retain their defined thresholds. Attach the authority and applicable requirement version so a later planner can distinguish a product rule from an implementation suggestion.

Separate mandatory behavior, permitted technical choices and unresolved questions. The no-self-approval rule is mandatory. A particular repository abstraction may be a technical choice within the application boundary. The response to a retried key after authority changes remains unfrozen. Recording all three in the same confident tone would give a worker no basis for deciding what it may change.

An original context audit can therefore ask what an executor could reasonably infer from each entry. Could it infer that current administrator status overrides requester exclusion? Could it infer that v2 changes old requests? Could it mistake an example storage field for the required public interface? Fix the entry's meaning before decomposing work around it.

This inspection differs from adding more context indiscriminately. An obsolete design can be more harmful than a missing optional note when it appears authoritative. Keep the active decision linked to its evidence and identify superseded alternatives. The aim is a recoverable choice, not a transcript of every possibility considered.

### Turn discussion into a dependency a planner can use

A discussion about request policy can end with an apparently complete sentence that still leaves planning difficult. “Keep old requests working” needs a definition of old, a source for the version and an owner for records whose origin is unclear. Ask the discussion record to resolve the part that constrains decomposition. A worker can choose an internal function name later. It cannot safely choose which existing customers receive a different threshold.

A useful decision record for the case names the selected behavior, its rationale and an example that crosses the policy switch. It also lists any unresolved questions that do not block that behavior. The planner can then create work for version assignment, resolution and the integrated observation. If historical records cannot be classified, the record should expose that dependency and identify the work that remains possible while the owner investigates it.

The distinction between a decision and a preference also matters. A preferred layout for a summary may be adaptable. A preserved v1 promise constrains implementation. Mark that difference in the work packet so a worker can make routine choices without reopening accepted behavior. If a technical discovery contradicts a decision's premise, return the observation to its owner and record the revision before continuing dependent work.

A later reader should be able to recover the discussion's result without reproducing its entire conversational path. Retain rejected alternatives where they explain a consequential tradeoff. Keep the actual accepted condition easy to find. For example, the reason for saving a policy identifier may be that pending requests outlive tenant settings. That rationale helps a maintainer resist replacing the identifier with a current-settings lookup during a future cleanup.

This is a proposed inspection of the discussion-to-plan boundary. A local exercise could ask another operator to plan the same bounded change using only the retained decision. Their questions would reveal which premises still depend on the original operator's memory.

<!-- C05-S03 -->
## Plan bounded work with persistent state

The inspected loop describes a research/planning/checking sequence, bounded `PLAN.md` files and dependency waves. Each plan identifies a work unit, relevant files, changes and acceptance criteria. Execution summaries, verification and state records connect the activity to later closure. These are prescribed structures, not artifacts produced in this project. [Core phase loop](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L25-L59)

A plan boundary should make the decision path easier to inspect. “Implement approvals” hides several business obligations. “Implement an eligible decision transition while retaining tenant isolation and its audit event” identifies a more specific unit, but it still needs an agreed contract and a prepared baseline before it can become an executable plan.

Do not decompose away a shared invariant. A request reader, decision path and history reader all carry tenant scope. If isolation appears only in a final cleanup plan, earlier work may be treated as complete before the relevant obligation is satisfied. Native plans can differ in size while retaining a common external acceptance boundary.

For a documentary walkthrough, preserve the role of each native record:

| Record described in the loop | Question we would ask of its case content |
|---|---|
| Phase goal | Does the goal identify the bounded business outcome? |
| `CONTEXT.md` | Are the agreed actor, tenant and policy decisions still explicit? |
| `RESEARCH.md` | Does each technical recommendation distinguish evidence from an assumption? |
| `PLAN.md` | Are dependencies, change scope and acceptance criteria inspectable? |
| Execution summary | Does it identify actual changes, deviations and unexecuted work? |
| Verification record | Does it relate requirements and decisions to inspected evidence? |
| State/roadmap records | Do they reflect the same completion state and unresolved gaps? |

A durable file is useful only if it remains relevant and recoverable. A new session that loads a phase goal but misses the policy exception still has incomplete context. A summary that reports “all checks passed” without the checked revision or outputs remains insufficient for our acceptance question.

The dependency graph also needs semantic review. Two plans may touch different files yet depend on the same policy interpretation or shared data contract. Non-overlapping edits do not prove independent work. For the two-approval change, the decision writer and reader must agree about policy binding even if their files differ.

We would preserve both declared dependencies and discoveries during execution. If a worker finds that the baseline does not expose the assumed repository operation, the plan needs correction or a visible deviation. Editing around the assumption and reporting completion would hide the cost of reconciling the design with the actual application.

Persistent state makes this reconciliation inspectable in principle. A future exercise must show whether its records actually supported recovery, how much human interpretation they required and what information was lost. The documentation alone does not supply those outcomes.

### Examine the dependency behind the file list

For an original E2 planning exercise, consider these proposed units. Their labels are teaching references, not generated plan identifiers:

| Proposed unit | Necessary input | Dependency to inspect |
|---|---|---|
| A — establish policy interpretation | Accepted v1/v2 transition and baseline evidence | Binding semantics must be agreed before consumers are changed |
| B — reconcile creation and decision paths | The same version/threshold contract | A request's recorded policy must agree with the decision reader |
| C — reconcile permitted reads/history | The same state and contribution meaning | Partial approval must not be presented as terminal completion |
| D — assemble acceptance observations | Reviewed fixtures and resulting implementation | Earlier regression and new behavior both need actual checks |

Some work within B and C may be parallel after the shared contract is established. That possibility is a design question, not evidence that every file-separated task is independent. If one worker invents a representation and another assumes a different one, their eventual integration requires reconciliation even when neither edit conflicts textually.

The plan checker should be examined against those semantic dependencies. A plan can name a file and a check while lacking the accepted rule that gives the check its expectation. Conversely, one plan may legitimately carry several tightly related operations when splitting them would obscure a shared invariant. Granularity earns its place through clarity and executable boundaries.

Preserve any dependency discovered later. If the baseline does not contain the assumed policy source, record the correction, affected plans and manual work. The final arrangement may still be useful, but the evaluation should distinguish following a well-founded plan from repairing an inadequate one during execution.

### Plan around the point where independent work stops being independent

Consider two workers with different tasks. One adds a migration and creation behavior. The other changes decision evaluation. Both need a policy identifier, but each may be tempted to create its own vocabulary while the other is working. Name the shared concept in the accepted plan and identify who owns the interface. An agreed identifier plus a provisional fixture may let the decision worker proceed. Mark that fixture explicitly and schedule a later exercise that uses the completed creation path.

Parallel work has a boundary beyond source file overlap. Two edits can touch different files while disagreeing about whether an absent identifier means v1, an invalid record or a request awaiting repair. The plan should distinguish a choice settled by the owner from one a worker is free to make. An accepted historical-data rule constrains both tasks. If nobody can establish the provenance of a historical record, pause the dependent transition design and keep unrelated work moving.

A summary is useful when it says what inputs it consumed. A decision worker can record the agreed interface revision, the provisional fixture and the checks performed against it. The integration worker can compare those inputs with the actual migration and creation change. If the interface changed, identify which earlier observation still applies to the policy function and which service-level check must run again.

A phase can close with evidence for the work actually delivered. If the integrated path is still open, record that state directly. The next operator should be able to see the accepted decision, the implemented pieces, the mismatch if one exists and the action needed to complete the phase. The exercise tests the continuity of the proposed work record in addition to its decomposition.

<!-- C05-S04 -->
## Execute with explicit context boundaries

The guide describes fresh executor contexts loaded with selected project, phase, research and plan information. It also gives a specific window size and strong claims about avoiding context degradation. We can establish the prescribed strategy from the source. We cannot generalize its capacity or effectiveness to every host/model configuration. [Execution-context description](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L25-L59)

Treat a worker handoff as an input contract. What is the worker expected to know, which decisions may it make, and where should it send an unresolved issue? The goal is not to maximize loaded material. It is to make the information required by the bounded task available without allowing stale or irrelevant material to settle current decisions.

For our decision-transition worker, the minimum relevant business context includes the pending-state precondition, current membership rule, no-self-approval rule, policy threshold and durable audit obligation. Technical context includes the selected baseline conventions and the frozen interface contract. The context record should point to their authoritative locations rather than silently restate a different version.

An original handoff inspection could ask:

1. Does the plan link to the actual requirement version?
2. Can the worker identify which request policy governs this transition?
3. Is the retry contract available, or is the worker expected to guess it?
4. Which existing behavior must survive the change?
5. Where is a discovered contradiction recorded before the scope changes?

These questions require the actual inputs or an auditable reconstruction during an executed trial. A worker summary saying that it considered security is not equivalent evidence. Nor can a new worker's clean context establish that it received a complete decision record.

Concurrency in orchestration needs its own scope. The source's waves coordinate plans. The application also has concurrent business decisions. Successfully dispatching workers would not establish correctness when two approvers act at once. The first concerns process execution; CS-09 concerns application behavior under competing decisions.

Record operator intervention as part of the arrangement. If a person supplies a missing policy exception halfway through execution, retain the correction and affected work. The resulting implementation may be acceptable, but its record should show that the initial handoff was incomplete. This is information for the context-management dimension, not an embarrassment to remove.

For a host migration, inspect which parts of the same handoff and reviewer arrangement remain available. Multiple supported installation paths do not establish identical hooks, permissions or worker behavior. A portability claim needs a defined migration exercise, with all compensating manual work included.

### Inspect a handoff before interpreting worker behavior

Suppose a future decision-path worker receives the phase goal, its own bounded plan and a link to the policy decision. A useful handoff inspection follows the link and verifies that the available version includes creation-time binding and requester exclusion. Merely listing a filename in a prompt does not establish that the content was readable or that the executor used it.

Record the actual input selection at the point of execution where the host permits it. If only a reconstruction is possible, state that limitation. Keep retrieved authoritative context separate from an operator's later explanation of what the worker should have known. The difference matters when diagnosing an omission.

An executor's new question can reveal an incomplete plan, a genuinely new discovery or an ignored available answer. Those explanations have different implications. Preserve the question, the input it had and the response rather than counting every clarification as the same kind of human intervention.

The application contract remains external to this process analysis. A worker can complete its bounded implementation yet leave a cross-unit history or tenant obligation unassessed. The phase-level evidence needs to reconnect the bounded outputs before claiming that the business increment is accepted.

### Design a resumability probe without changing the task

A proposed continuity exercise can stop after decisions and plans have been recorded, then resume with the declared retained state in a fresh session. Another can stop during the acceptance conversation. Specify the interruption point and retained artifacts before an attempt, rather than choose whichever interruption makes recovery look straightforward.

The recovery question is whether the operator can identify completed work, remaining work, accepted constraints and current evidence. It is not simply whether the workflow opens another chat. Record any manual reconstruction needed and any contradiction between state records and actual artifacts.

For a measured comparison, decide whether this continuity exercise belongs inside the episode or is a separate intervention. Native state produced during an attempt may legitimately be retained for its continuation; state leaked from an earlier independent attempt must not quietly become an advantage. The reset policy needs to distinguish the two.

### Inspect a worker assignment for missing constraints

In the illustrative Core arrangement, split a policy change into work that assigns version at creation and work that resolves it at decision time. Give both assignments the same accepted vocabulary for v1, v2 and risk. Name where the resolver will obtain a version and which change owns the persistence format. Otherwise two workers can independently make plausible choices that cannot be integrated without rewriting one side.

A handoff should make a dependency concrete. If a worker needs the stored identifier but the creation work has yet to land, record whether that worker is building against an agreed interface, a temporary fixture or a completed upstream change. A temporary fixture can support early work. When it is replaced, inspect the actual creation path and refresh the checks that depended on the fixture. The plan can point to that integration observation without prescribing a particular task engine.

After a session interruption, have the next operator reconstruct the state from the retained decisions, plans and outputs. Ask them to identify what is ready to integrate and which verification used a temporary fixture. Any question they can answer only by asking the previous operator is a candidate handoff defect. This proposed exercise addresses the usefulness of the retained records for this change.

### Make a worker's completion report usable by integration

A proposed completion report can name the interface consumed, the change produced and the observation performed. For a resolver worker, the report might say that it consumed the agreed stored policy identifier and exercised the threshold against synthetic inputs. The integration owner still needs to connect creation and persistence to that interface.

List any provisional input beside the result. If the worker substituted a fixture for an unfinished creation path, identify that substitution and the observation required after replacement. A reviewer can then accept the component work while preserving the integration task. If the interface changes, the report gives the next operator a way to find affected evidence.

A useful final line states the next dependency. For example, the integrated preservation probe awaits the creation change and a migrated historical fixture. That line makes handoff actionable and keeps a favorable component result attached to its actual scope. The integration owner can update the dependency when the prerequisite arrives and retain the earlier report with its revision.

<!-- C05-S05 -->
## Verify, recover and close the work

Core's verification guide describes a user-acceptance conversation derived from execution summaries, with persisted progress and gap-fix planning. It separately describes shipping preflight and pull-request creation. Code review is optional rather than an automatic part of shipping. These are distinct activities in the inspected design. [Verification, gap closure and shipping](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/verify-and-ship.md#L9-L89)

The summary-derived checklist can help an operator inspect what the process reports as delivered. It cannot, by itself, establish that omitted requirements were tested. If the implementation summary never mentions a foreign-tenant direct-ID path, a checklist derived from it may omit that boundary as well.

Our case therefore retains an independent acceptance inventory. The process's verification record and the external checks should be related, not treated as interchangeable. For each CS requirement, identify the native evidence, any independent observation and the unresolved gap. This also makes it possible to discover when a source-native check is more useful than the initial book instrument expected.

Recovery begins with the failure's scope. A failed assertion may indicate wrong code, an incorrect fixture or an unresolved requirement. A diagnosis should distinguish those possibilities before generating a fix plan. Changing the expected outcome to agree with the implementation requires product authority when it changes accepted behavior.

The guide also describes stale verification. Current reports can fingerprint covered inputs and implementation files; older reports use a summary-modification-time rule. When relevant inputs change, the gate is supposed to require renewed verification. This establishes a designed freshness mechanism, not a test of its completeness or bypass resistance. [Staleness policy](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/verify-and-ship.md#L106-L115)

Freshness and correctness remain different. A verdict can be current for all files it covers and still omit a relevant dependency or business rule. A future review must inspect coverage as well as the digest. Conversely, a stale verdict should not be reused merely because the change looks small.

Closing a phase is another decision boundary. The source's ship behavior concerns repository delivery and PR preparation. It does not establish deployment, operational ownership or production acceptance. In this book, we do not execute that shipping command or infer authority to push an external change from a documentary description.

For an executed case, closure would preserve the baseline and final revision, actual checks and outputs, human responses, failed attempts, deviations and unresolved requirements. If the resource ceiling is reached, record a stopped attempt rather than relabel the remaining work complete. The current chapter has no such run record.

### Keep the acceptance response attached to its question

The re-inspected guide describes an interactive UAT flow in which an empty response can be treated as a passing answer. That documented interaction makes response interpretation part of the evaluation design. It does not establish that any absent answer in another workflow counts as consent. [UAT interaction and scope](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/verify-and-ship.md#L9-L89)

For a future trial, preserve the presented checkpoint, actual response and evidence the person used. A person saying yes after examining a display has answered that display question; they have not necessarily inspected a direct-ID authorization path or concurrent writes. The independent CS inventory needs its own observations.

If a checkpoint fails, retain the original observation through diagnosis and gap closure. An inadequate fixture may require a new check, whereas a real implementation defect requires repair. A changed product expectation requires authority and can change task identity. The final successful run should not erase which of these occurred.

### Review freshness coverage as well as freshness status

A freshness mechanism relates a verdict to its covered inputs. Inspect the actual covered set before interpreting a current status. For E2, the relevant requirement, policy interpretation and changed implementation need a clear relationship to the verification record. If fixture or environment changes matter, inspect how the selected arrangement accounts for them rather than assume that a file digest covers the whole exercise.

A changed fingerprint identifies a change in covered bytes, not its business meaning. A semantically unchanged edit may still require the designed recheck, while a relevant omission outside the covered set may need a separate acceptance observation. Neither fact justifies disabling the freshness rule. It identifies the additional interpretation duty.

The proposed evidence packet should retain both the earlier verdict and the renewed one, with the change that prompted reconsideration. That history can establish what was re-examined. A final status alone cannot show whether an operator reran the appropriate checks or merely edited a completion label.

### Reconstruct what a stale verdict covered

Imagine verification ran after the decision worker's changes but before the creation worker replaced the fixture. Later the integrated application compiles and someone sees a favorable verification status. The reviewer needs to identify the revision and the checked boundary before deciding whether the verdict can be reused. The earlier observation may still support the threshold calculation under its fixture. It leaves assignment through normal creation open.

Write a recovery note with three entries. The first identifies the old verdict and what it exercised. The second lists the inputs that changed, including the fixture and the source of the version identifier. The third names the fresh exercise and its prerequisite. For this example, create a v1 request through the service, switch the active policy and decide that same request. The result gives the next operator a way to distinguish an input change from a policy regression.

Run status and work status also age differently. An old summary may accurately describe a finished implementation task while a new finding reopens acceptance. Keep the summary as history, and record the open finding against the current integration revision. If the reviewer must redo the whole investigation to recover that distinction, improve the handoff before opening another phase.

An operator can apply this inspection to a stopped session without treating every old record as stale. Preserve the accepted product decision unless the owner changed it. Revisit checks that depend on the altered implementation or fixture. Identify any evidence whose revision cannot be recovered. This keeps recovery proportional while making the basis for closure visible.

<!-- C05-S06 -->
## Small repairs and policy changes

The phase-loop guide warns against phases that are either too broad or too fragmented and points a trivial repair toward a quick path. That documented allowance matters when comparing overhead. We should not require the full loop for a task the source routes differently. [Phase sizing and small-work guidance](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L77-L90)

A small presentation repair from chapter 2 could therefore be evaluated under a bounded route, preserving the same intent and regression duty. Its record would disclose the path actually used. If the task reveals a policy or data-model uncertainty, revisit the scope rather than cling to the initial small-task label.

The E2 policy change is different. A new high-risk v2 request needs two distinct eligible approvals; an existing v1 request retains its creation-time rule. A plan that changes only a global approval-count constant would leave policy binding unresolved. The required discussion and context must carry both the new behavior and the preserved old behavior.

Our documentary change trail would revisit the phase goal and decisions, inspect the prepared baseline, identify bounded plan dependencies and update the verification obligation. It would not reuse an obsolete success assertion from E1. The actual native file contents and commands remain to be produced by an executed profile, if readiness later permits one.

Acceptance examples need independent fixtures. A new high-risk request should remain pending after one eligible approval and complete after a second distinct approval. Repeating the first approver must not advance the count. A pending v1 request should retain its original threshold. These are case obligations, not observed Core outcomes.

For E3, use the same prepared defect and report for every method. The defect is a predetermined tenant-boundary error, not a different problem chosen after observing each method. The small-path comparison should preserve the diagnostic record, narrow repair and relevant regression evidence.

Existing code deserves particular care. Persistent plans describe intended work; the application describes current behavior. A conflict between them needs a decision. The inspected source set did not establish a complete reverse-engineering baseline procedure for every Core path, so we leave that broader capability unassessed rather than infer absence.

### Carry the change through the phase record

For our proposed v2 episode, compare the current phase goal, accepted context, affected plans and their later summaries. Each should describe the same change boundary. A summary saying support two approvers is not sufficient when the context also preserves v1 requests and standard-risk v2 behavior. The external inventory makes those omissions visible without dictating the native artifact format.

Then inspect closure dependencies. If one plan updates creation and another updates decision handling, a phase verdict should not rely on only one plan's local checks. If a policy question remains unresolved, retain the blocked scope rather than make a new worker guess. If the task legitimately becomes smaller, revise the episode definition visibly instead of treating omitted obligations as completed work.

These inspection steps do not prescribe the contents of generated files or predict an executor's behavior. They define how a reviewer could evaluate the phase-loop mechanism against one shared maintenance obligation, including partial progress and human correction.

### Separate the problem that needs a decision from the work that needs a plan

For a brownfield repair, the first uncertainty can be about what the software already does. Give the investigation a bounded deliverable: find the failing entry point, show which query it reaches and list the other callers of that query. Stop with those observations if the intended disclosure contract is still open. This keeps an investigation from quietly deciding what every unauthorized client should receive.

Once the owner settles the contract, scope the repair by affected call sites. An endpoint patch and a shared helper change carry different verification duties. An endpoint patch needs an explanation of why the other paths already enforce the boundary. A helper change needs observations that existing permitted reads continue to work across its callers. An investigation summary should preserve enough context to make that choice after the original session ends.

If the work begins as a quick repair and reveals three distinct data paths with incompatible assumptions, record why the original route stopped being sufficient. The operator can choose a plan sized to the expanded boundary and link it to the original finding. If the investigation finds one well-understood predicate and adequate existing controls, the original route can still be enough. Decide from the work discovered in the repository and the observations needed to accept it.

### Rehearse context recovery on a deliberately incomplete task

A team can inspect its proposed context arrangement with a small exercise. Stop after one worker completes a component check while integration remains open. Give a new operator the retained records and ask them to name the next authorized action, the input it needs and the old observation that cannot establish integration. Record where they find each answer.

The exercise has an expected outcome. The new operator should be able to distinguish accepted intent from a provisional fixture and identify the observation still required. If they infer that all work is complete from a favorable component result, inspect the summary and its link to the active plan. Correct the record at the first point where scope was lost.

Repeat the recovery using the corrected packet and retain the result. A successful local recovery would support a narrow claim about those records and conditions. It would also give the team a concrete handoff example to use when the next change stops halfway through.

<!-- C05-S07 -->
## Limits and conditional fit

The inspected Core design offers a concrete arrangement of decision context, bounded plans, workers, summaries and verification. Its potentially useful property is the explicit information flow between activities. Whether that flow reduces errors or effort remains an empirical question for the selected task and configuration.

Our conditional assessment is to investigate this arrangement when a project needs resumable bounded work and can support the required host/operator practices. Examine whether material decisions survive handoffs, whether plan dependencies reflect shared contracts, and whether verification detects omissions as well as implemented deliverables. These are evaluation premises, not a default adoption recommendation.

Setup and maintenance costs remain unmeasured. The same is true of actual context quality, collaboration among people and long-term operations. The installation discrepancy and source-versus-package identity must be resolved before a reproducible executable profile is claimed. None of these gaps is converted into a numerical penalty.

The model-worker arrangement is also not independent human review. Additional agents can provide useful perspectives, but the book still needs external scrutiny of its sourcing and any eventual case evidence. Solo orchestration cannot establish organization-wide coordination benefit.

For the comparison chapter, retain the strongest supported documentary conclusions: explicit phase decisions and plans, deliberately bounded context, summary-based UAT, separate optional review, and a designed freshness policy. Retain the qualifications beside them. We have no controlled GSD-versus-peer outcome from this project.

The practical question carried forward is whether the persistent record makes the next decision easier to recover without hiding what was never settled. That question can be asked of a quick repair, a policy change or a multi-session feature, with a proportionate path for each.
