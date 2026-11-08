# 11. Real-World Case Study: Building a SaaS

> Author manuscript · completed 2026-11-05 · C11 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C11-S01 -->
## Scope, realism and approved decisions

A useful case needs more than an appealing feature. It should expose decisions that different processes have to carry, boundaries that a positive-path demonstration can miss, and changes that test whether the original intent remains recoverable. Vendor-access approval supplies those conditions without requiring a live business deployment.

The service records a request for temporary vendor access, an eligible decision and its history. It does not grant access in an external system. There are two synthetic customer tenants, overlapping roles and a later policy change. The author selected TypeScript / Node.js and accepted this domain/design direction. No web framework, database, model or host has been selected as an executed common stack.

The complete design authority is the [case specification](../../CASE_STUDY_SPEC.md). It distinguishes accepted direction from unresolved interfaces and future acceptance checks. This chapter explains how to walk that design through the selected source mechanisms. It does not turn a paper design into an implementation result.

The business model needs Tenant, User, Membership/Role, VendorAccessRequest, ApprovalDecision, PolicyVersion and AuditEvent concepts. These names describe responsibilities, not an imposed ORM schema or class hierarchy. Each method remains free to organize native planning artifacts and a future implementation within the agreed constraints.

A request begins pending after valid creation. An eligible different tenant member can approve or reject according to its bound policy. A rejection while pending is terminal. Approval becomes terminal when the policy's required distinct approvals are present. Public business operations cannot rewrite accepted decision history. Those are expectations to realize and check later.

Realistic constraints include tenant isolation, current membership, no self-approval, retries, concurrency and durability. Real identity federation, live provisioning, billing, email, production hosting and regulatory certification are excluded. The narrow scope lets us reason about meaningful behavior while keeping the evidence claim local and explicit.

The missing application/framework execution layer is material. We cannot report SaaS build success, defect counts, elapsed times or framework effectiveness. A transparent qualitative walkthrough can still show which questions and artifact relationships a reader should inspect. It also identifies the concrete work required before a measured comparison would be credible.

<!-- C11-S02 -->
## Requirements, fixtures and acceptance oracle

Mira requests access in tenant A. Leon and Priya are eligible approvers in A. Ozan belongs to B. A role-overlap variant gives Mira approver and administrator roles. A revoked member tests current eligibility rather than a stale role assumption. These are proposed fixture roles; no database has been seeded.

Use a controllable clock and synthetic identifiers. A valid creation expiry is after the controlled creation time. Keep unrelated checks within a valid time range so an expiry failure does not hide the intended authorization or state-machine question. Behavior after expiry at decision time remains an interface/product detail to settle rather than infer silently.

Each negative check needs a meaningful positive control. Foreign-tenant access requires a record that actually exists in A and an A actor who can obtain the permitted view. Self-approval requires a pending request and a requester who otherwise holds sufficient roles. A completed or nonexistent request could deny the action for an irrelevant reason.

The proposed requirement/check inventory is:

| ID | Business obligation | Proposed acceptance probe — all Not run |
|---|---|---|
| CS-01 | Established identity and tenant membership | Valid member versus missing/invalid identity and non-member |
| CS-02 | Complete valid creation | Future expiry and valid content versus invalid/missing fields without partial state |
| CS-03 | Tenant-isolated reads, lists and searches | Existing A record read/list/search by A versus B, including direct identifiers |
| CS-04 | Current eligible approver | Same-tenant approver versus revoked/foreign/requester-only actor |
| CS-05 | No self-approval with overlapping roles | Pending request, requester with approver/admin roles, and separate eligible-actor control |
| CS-06 | One eligible approval under base policy | Valid v1 decision completes; invalid actions do not contribute |
| CS-07 | Consistent terminal behavior | Pending rejection/approval, then prohibited conflicting terminal changes |
| CS-08 | Idempotent retries | Same key/payload repetition and conflicting key reuse under the future frozen contract |
| CS-09 | Concurrency preserves policy | Competing decisions and duplicate submissions with resulting state/history inspected |
| CS-10 | Durable tenant-scoped audit | Restart, permitted history read, foreign-history read and mutation attempt |
| CS-11 | Scoped role administration | Local changes, foreign membership denial and preserved self-approval exclusion |
| CS-12 | Two distinct high-risk v2 approvers | First leaves pending, second distinct completes, repeated first does not advance |
| CS-13 | Explicit version transition | New v2 versus existing v1 and standard-risk versus high-risk |
| CS-14 | No prohibited data/secret leakage | Error/log inspection under the selected disclosure policy |
| CS-15 | Predetermined boundary repair | Known failing baseline probe before repair and retained regression evidence afterward |

The oracle is the reviewed decision procedure that relates these expectations to observations. It includes fixtures, assertions and adjudication rules for ambiguous results. It must be independent of the implementation's accidental behavior. A generated test that repeats a defect is not a valid external expectation.

Several details remain unfrozen: exact interface, response/disclosure policy, idempotency-key scope/retention, error representation and persistence/concurrency design. This chapter does not invent those decisions to make the checklist appear executable. A measured exercise must settle them before exposing each framework to the task.

Role administration also needs episode scope. E1's bounded feature can use prepared membership fixtures without implementing a complete admin interface. If administration is added to scored work, add it uniformly before runs. The common specification can cover more product behavior than one episode implements.

### Design a fixture that answers one question

A fixture is part of the argument for a check. Its important properties are the ones that make the target rule distinguishable from other reasons the operation could succeed or fail. A convenient collection of users and requests is not sufficient if the expected outcome has several unrelated explanations.

For the requester exclusion, prepare two equivalent pending requests in A, with the same policy and valid creation conditions. In one independent check, Mira has requester, approver and administrator roles and attempts to approve her own item. In the positive control, Leon is a current eligible A approver who did not create the other item. The actor/request relationship is the material difference. Do not run the second case on the already completed output of the first.

For tenant isolation, start with a known A request that an A member can read. Use Ozan in B to attempt the corresponding foreign access. A denial is informative only alongside evidence that the target exists and the permitted reader works. For list/search checks, choose fixture values that would match the query if tenant scope were removed. A search term that matches nothing in either tenant would make a broken scope look correct.

For current membership, preserve the relevant role while marking the actor's membership inactive before the attempted action. Otherwise a denial could be explained by absence of the approver role. For a role-only check, keep membership active and remove the required role. A small fixture matrix makes those distinctions reviewable:

| Probe family | Condition deliberately varied | Conditions held suitable |
|---|---|---|
| Self-approval | Actor is the requester | Pending state, same tenant, current membership, approver role |
| Tenant boundary | Actor's permitted tenant context differs from target | Existing target, active eligible role in the actor's own tenant |
| Revocation | Current membership is inactive | Existing pending target, otherwise relevant role |
| Role eligibility | Approver role is absent | Active same-tenant membership, different requester |
| Terminal behavior | Request is already approved or rejected | Otherwise eligible different actor |
| Distinct-count behavior | Actor already contributed an approval | Pending high-risk v2 request, current same-tenant eligibility |

These are proposed controls. They have not been instantiated against an application. They are also not a rule that every check must vary exactly one input: integration behavior often involves several conditions. Their purpose is to make the claim and the possible confounders explicit.

### Separate required semantics from unresolved policy

Do not let a larger fixture set create new product rules accidentally. Current membership at decision time is defined. The effect of revoking a *previous* approver after their valid contribution but before a second approval needs a separate policy decision. The existing requirement does not explicitly say that historical approvals become invalid retroactively. That scenario should remain outside scored expectations until the contract settles it.

Expiry creates a similar boundary. Creation needs a future expiry. The exercise has not settled every consequence of reaching expiry while a request is pending. Use a controlled clock to keep ordinary authorization checks away from that ambiguity, and record an explicit decision before testing expiry-at-decision behavior. A model should not infer it from the word temporary.

For each unresolved scenario, record the accepted surrounding rule, the ambiguity, the alternatives and which checks depend on the answer. That is a concrete preparation task rather than a reason to ask the author the same broad case question again. The comparison can continue as a documentary walkthrough while the executable contract remains unfrozen.

### An observation has more than a result label

A useful future observation record identifies the starting fixture, command, expected result set, resulting business state and relevant side effects. Add revision/environment identity and the actual command/output locator when execution exists. A field called Pass without that context is difficult to challenge or reproduce.

The expected result can be a set of legal histories, especially for concurrent work. It should be defined before observing an implementation. An operator must not select whichever outcome occurred and then call it the intended one. Conversely, requiring one arbitrary ordering can reject an implementation whose result is legal under the agreed model.

Keep an adjudication rule for observations that do not fit the expected shape. An environment failure may make a business assertion unassessed. A malformed fixture may invalidate the check. A genuine forbidden transition may establish a product defect. Retain the raw observation while the interpretation is reviewed; changing its category should not erase the original record.

<!-- C11-S03 -->
## Freeze profiles and per-episode baselines

A documentary pin identifies the instructions inspected. An experimental freeze requires more: actual package contents, host/model conditions, enabled modules, application stack, baseline code, fixtures, checks and allowed interventions. None of those additional controls should be inferred from a repository URL.

The working source identities are:

| Subject | Documentary source identity | Execution disposition |
|---|---|---|
| BMAD | `bab9082c3e884e0d72c759bcd1a6d90bcc01be84` | Native path/module/host and installed artifact unfrozen |
| GSD Core | `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc` | Contemporary lineage scope; runtime conflict and package identity unresolved |
| AWS workflow | `3939a8b9182f2e4153b92028057a7be74e0684c2` | Profile, guard and local/operations route unfrozen |
| AIUP | `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960` | Core/Node candidate; common stack and coverage route unresolved |

These are the sources used in chapters 4–7, not four completed installations. The [source receipts](../../research/evidence/SOURCE_RECEIPTS.json) preserve their provenance and inspection limits. All thirteen [experiment readiness checks](../../research/EXPERIMENT_READINESS.md) remain open.

Each episode needs a controlled starting state. E1 starts from one neutral scaffold. E2 starts from one externally prepared working baseline with v1 behavior. E3 starts from one prepared baseline with a predetermined tenant-boundary defect. No such code baseline exists here, so there is no baseline hash to report.

Matched starting state is different from longitudinal continuity. If every method maintains its own E1 output in E2, the episode includes earlier architectural and quality differences. That is a legitimate different study, but it does not isolate the change procedure on a common application. Keep the designs separate.

Neutrality also needs review. A scaffold with one method's domain layers, hidden helper implementation or preferred generated tests could advantage that arrangement. Define the interface and public obligations without embedding a solution. Record any unavoidable adapter or host asymmetry rather than silently call it controlled.

For actual runs, predeclare operator familiarization, order, replication, resource ceiling, stopping conditions, missing-data treatment and permitted manual intervention. Count worker calls and setup/adaptation effort. No fixed model access or spending authority has been established by this documentary chapter.

### What neutrality requires of the scaffold

A neutral scaffold should make the common task possible without deciding its implementation. It can define how the exercise starts, how synthetic identities are supplied, how checks address the business interface and how a clean reset is performed. It should not secretly contain the completed approval state machine or one framework's generated architecture.

Some shared components are necessary for a bounded exercise. The evaluation must state which behavior they already supply. If identity establishment is prepared infrastructure, assess its integration and assumptions without attributing its implementation to each method. If an arm must implement it, add that work uniformly to the episode. Mixing those scopes would change both effort and defect opportunity.

A baseline acceptance packet should identify four things: what is already correct, what is deliberately missing, what is intentionally defective in E3 and what is excluded. The E2 baseline needs actual evidence of working v1 behavior before the policy change begins. The E3 baseline needs a reproducible failing probe before repair. A design promise is not that evidence.

Prepare separate working copies per attempt. A reset must restore code, persistence, fixtures, clock and workflow state that the task assumes. Clearing one framework's chat while leaving another's generated application records or previous decisions in place would provide unequal starting information. The procedure must identify the method-native state that is legitimately part of the selected intervention and the stale state that must not leak from an earlier attempt.

The local teaching model cannot simply become the hidden scaffold solution. It already embodies selected approval rules. Giving it to one arm while asking another to derive the behavior would alter the task. It may be a public illustrative reference for readers or a separately reviewed ingredient in an oracle design, but either use must be declared before a measured exercise.

### Record deviations at the right level

Suppose a method's selected adapter needs a database not present in the common environment. A manual port, custom adapter or stack change is an intervention, not an invisible setup detail. Record who performed it and what changed. Its cost belongs somewhere in the accounting policy even if it occurs before scored execution.

Likewise, an operator may answer a material policy question after work starts. Preserve the question, answer, affected work and reason it was not settled earlier. The final implementation might still meet the contract. The record would then support a conclusion about the combined assisted arrangement, including the intervention, rather than the initial autonomous route alone.

These controls do not guarantee a causal experiment. They make its remaining confounders inspectable. The present chapter has no completed baseline/reset exercise and therefore makes no stronger claim.

### Verify that two baselines agree before comparing their repairs

A future evaluator should inspect the prepared baseline through a small set of common observations before dispatching it to any arm. Confirm the expected initial records, the relevant policy behavior and the known defect for the repair episode. Record the source identity and fixture identity together. A matching source revision with different fixture populations can produce a different task.

Preserve a clean copy of the baseline and the preparation record. If an operator changes it while diagnosing setup, distinguish that attempt from the intended starting state. The evaluator can decide whether to restart from the clean baseline or report the deviation. Either choice needs a visible account before results are compared.

Use the same principle for the policy-change episode. The baseline needs a request that genuinely predates the switch, along with the current rule and the observation channel. A manually invented precondition that only one arm receives would change the information available for the task. Freeze that preparation before examining candidate output.

<!-- C11-S04 -->
## E1: a bounded feature

E1 asks each selected arrangement to address the same base behavior: valid request creation, eligible decision, tenant-local reads/history and the applicable audit/retry/concurrency obligations. Administrative fixtures can remain outside the scored feature scope when declared uniformly.

The first business review should make the requester exception and tenant boundary explicit. A plausible plan that treats administrator status as universal authority would contradict CS-05. A history endpoint scoped only by request identifier would need examination against CS-03/10. These are diagnostic questions, not defects observed in an implementation.

The source mechanisms suggest different documentary trails:

| Arrangement | Native trail to inspect for E1 | External question |
|---|---|---|
| BMAD | Intent-sized planning, named specification where used, linked Build record | Are accepted constraints present through the chosen small/epic route? |
| Core | Discussion context, bounded plans, summaries and verification | Do context and checks include constraints the implementation might omit? |
| AWS workflow | Intent, configured route/unit records, approval and boundary evidence | Which decisions were reviewed and which checks were actually active? |
| AIUP | Requirements/use case, selected construction inputs and acceptance trail | Are applicable constraints linked and realized through the chosen adapter? |

The deep dives cite the exact instructions behind these trails. The table is an author-designed inspection plan; it does not report native files generated in four sessions.

For a future completion record, keep requirement-level states. A positive-path demo may establish one observation while leaving retries and foreign-tenant reads Not run. Do not promote an aggregate “done” label to full acceptance. The external inventory should identify every applicable unmet obligation.

A useful independent check also isolates its cause. The self-approval probe starts pending, with a role-overlap requester and a valid tenant relationship. The positive control uses a separate equivalent request and an eligible different actor. The foreign-read probe uses a known existing A record, not an arbitrary missing identifier.

No observation is supplied here. E1's documentary result is the inspection trail and the list of decisions that must be settled for execution. Its implementation acceptance, effort and defect outcomes remain Not assessed.

### Four native handoff sketches

The following short records are original teaching sketches. They express the same accepted business intent in forms a reviewer could look for along each native trail. They are not copied prompts, official templates or outputs of installed workflows. The aim is to show a meaningful handoff without forcing identical artifacts onto all four methods.

**BMAD sketch.** A specification capability describes an eligible decision on a pending tenant-local request, with requester exclusion as a constraint. Its success condition points to the business state and durable history, not just an approval button. A linked story identifies the independently reviewable slice and the checkpoint chosen by the operator. The Build record should explain the relevant existing patterns, implementation changes, checks and deferred unrelated work. If the route is smaller, the reviewer still needs to find the accepted constraints in its current record.

The diagnostic question is whether decomposition preserved cross-cutting obligations. A story for the history reader cannot treat tenant isolation as another story's future responsibility. A record can link to the common requirement instead of repeating it, but the link must make the applicable behavior recoverable.

**Core sketch.** Phase context records the accepted actor/tenant policy and the open interface details. The bounded plan identifies its goal, dependencies and acceptance criteria. A worker should receive the relevant current context and plan, and its summary should distinguish changes from unexecuted checks. Verification should examine requirement and decision coverage, while the external inventory checks obligations omitted from a summary-derived list.

The diagnostic question is whether context selection changed meaning. If the phase goal survives but the requester exception disappears from the worker's input, the record is persistent yet incomplete. A fresh session does not cure that omission. The observation needed later is the actual handoff and resulting correction, not a claimed capacity number.

**AWS workflow sketch.** Intent records the business goal and exclusions. The selected route identifies its included stages, unit structure, approval duties and active guard configuration. A design decision makes actor/request/tenant relationships explicit. Construction and boundary records explain which artifacts and links were checked. Local substitutions and operational exclusions remain visible instead of being hidden behind a lifecycle completion status.

The diagnostic question is which authority advanced the work. Approval of a development plan must not be confused with an approval in the business application. A workflow audit can help reconstruct the former; the application's tenant-scoped audit must establish the latter. Their different purposes remain visible in the evidence packet.

**AIUP sketch.** Requirements identify tenant locality, current eligibility, no self-approval and durable decision history. A use case organizes the actor's goal, preconditions, permitted path and required alternatives, linking all applicable constraints. Construction uses the selected core/adapter inputs, and tests and acceptance records address the same business behavior. Any manual coverage route compensating for an adapter limitation is named rather than attributed to automatic core enforcement.

The diagnostic question is whether the behavioral links are complete and correct. A use case can reference a membership requirement while missing the requester exception. A code marker and test label can resolve while the assertion exercises the wrong state. Structural resolution is valuable, but semantic review and actual acceptance still have separate jobs.

Across all four sketches, preserve native identifiers and add the external CS mapping beside them. Do not rename a GSD phase as an AIUP use case or require every method to emit a BMAD story file. The comparison concerns how the method carries the common work, not whether it can imitate another method's paperwork.

<!-- C11-S05 -->
## E2: a policy change

The E2 change introduces two distinct eligible approvals for newly created high-risk requests. Standard-risk v2 requests still need one. Existing v1 requests retain the policy bound when they were created. This is accepted case direction, not a conclusion discovered by a run.

The proposed behavior matrix makes preserved and changed expectations visible:

| Request fixture | Required interpretation |
|---|---|
| Pending v1 high-risk request | One eligible distinct approval can complete under v1 |
| New v2 standard-risk request | One eligible distinct approval can complete |
| New v2 high-risk request, no approval | Remains pending until its required distinct approvals are obtained |
| New v2 high-risk request, one eligible approval | Remains pending; decision/history remain consistent |
| Same first approver repeats | Does not advance the distinct count; retry details follow the frozen contract |
| Second distinct eligible approver acts while pending | Can complete if no competing terminal outcome has already prevailed |
| Already terminal request | A later conflicting action cannot switch its accepted outcome |

The distinction between a valid partial approval and terminal completion matters. A test that checks only the final approved state could miss an implementation that completes after the first approval. A test that checks only two actor identifiers could miss a revoked or foreign-tenant participant. Preserve both policy and eligibility.

The native change trail differs by method, but each should carry the same semantics. BMAD's named specification update path can preserve capability references. Core's new decisions/plans and fresh verification can carry the altered rule. AWS's configured route can record the intent and approved construction change. AIUP's requirements/use-case reconciliation can identify downstream effects. Those are documentary paths, not evidence that the paths succeeded.

Concurrency adds valid outcome sets. Under v1, an approval and rejection racing on one pending request must not produce incompatible terminal states or mismatched history. Under high-risk v2, the order of partial approvals and rejection can matter while pending. The acceptance contract must identify legal histories under the chosen semantics rather than demand one arbitrary scheduler order.

Record actual interleavings or a controlled test strategy when execution exists. A sequential test with two calls does not establish a concurrency result. Likewise, a schema field called `policyVersion` does not prove correct binding; its use in every relevant decision path needs inspection.

E2 is designed to expose maintenance, context and traceability questions. It supplies no measured superiority. A long-lived benefit would require more than this one change and should not be inferred from a neatly updated artifact.

### Read a proposed trace as an expectation

Here is an authored scenario for a newly created high-risk v2 request. Each row describes an expected transition or invariant to check later; it is not a log from an execution. The concrete fixture identities and interface still need a reviewed contract.

| Proposed input sequence | Expected checkpoint |
|---|---|
| Create a valid request under v2 | Pending, bound to v2, no counted approvals |
| Leon supplies an eligible approval | Pending, one distinct contribution, required history consistent |
| Leon repeats the contribution | Still one distinct contributor; retry/error details follow the future contract |
| Priya is inactive and attempts approval | No successful new contribution |
| A separately prepared eligible Priya attempts approval while pending | Two distinct eligible contributions can complete the request |
| Another action tries to change the completed outcome | Terminal outcome remains consistent with the accepted history |

The inactivity and eligibility cases must be prepared deliberately. A test that mutates membership as part of its fixture should record when the change takes effect. If the test relies on a separate administration operation, that operation becomes a dependency whose correctness must be established for the observation to mean what it claims.

Repeat the relevant checks on a pending v1 high-risk request after v2 is introduced. Its one-approval expectation must come from the bound policy rather than a global current-policy lookup. A field named policy version is not sufficient: inspect how the decision path uses it and whether readers/history retain the same interpretation.

### Distinct approval is not request idempotency

The local model demonstrates that Leon cannot count as two different approvers. It intentionally does not implement a client request-key contract. Those are different mechanisms. A second call can be a retry of the same command, a new command from the same actor or a command that reuses a key incorrectly.

Before an executable comparison, define the key's scope. Tenant-wide, actor-scoped and target/operation-scoped designs have different collision and information-disclosure consequences. The case does not yet choose one. Whichever design is selected, apply it uniformly and define which payload differences constitute conflicting reuse.

Also define which authority applies before a replayed result is returned. A stored result should not quietly create a route around the current identity/tenant policy. The exact interaction among authentication, permission changes and replay needs a reviewed contract; the model's internal duplicate-actor reason code cannot answer it.

The acceptance inventory should distinguish at least these cases:

| Case | Question the future check must settle |
|---|---|
| Same authorized command/key/payload repeated | Is the business effect represented once, with consistent replay behavior? |
| Same scoped key with changed payload | Is conflicting reuse handled without a second unintended effect? |
| Same actor with a new key on high-risk v2 | Does distinct-actor counting still prevent a second contribution? |
| Same visible key in another tenant/actor scope | Does the chosen scope prevent cross-boundary disclosure or collision? |
| Retry after terminal completion | Does replay preserve the agreed result without creating new history? |
| Retry after authority changes | Which current-access and replay rules govern the response? |

These are contract-design questions and proposed probes, not newly asserted HTTP behavior. No response codes, retention duration or replay body has been frozen. That restraint prevents a method's preferred implementation from deciding what the oracle later calls correct.

### Observe state and history together

An implementation could satisfy a final-state assertion while losing the corresponding history, or retain a history event for a business transition that never became durable. CS-09 and CS-10 require the observation plan to connect these facts. The database and atomicity mechanism remain open, so this chapter does not prescribe a transaction recipe.

For a future fault exercise, identify intended interruption points such as before persistence, between related writes and after a durable effect but before acknowledgement. Define the legal recovered states before injecting faults. A consistent completed effect and a consistent absence of the effect are different possibilities; an unmatched business/history state should not be accepted merely because one record looks correct.

Partial approval under high-risk v2 adds another legitimate state: pending with one accepted contribution and its consistent required history. Recovery must not confuse that state with a failed terminal transition. The observation needs policy version and contribution identities as well as the overall request status.

This is why a sequential function check cannot establish persistence or race correctness. The model helps inspect selected policy logic. Application-level observation must address how that logic is integrated with actual identity, storage and concurrent requests.

### Define legal histories before racing commands

Consider a pending v1 request with no approvals. An eligible approval and an eligible rejection compete, with membership and other policy conditions held constant. The acceptance design should permit either command to prevail when their relative order is unconstrained. It should not permit a final approved state alongside a successful terminal rejection in the same business history.

The observer therefore needs more than two response bodies. Preserve the submitted operations, their acknowledged outcomes, the resulting request and the required durable history. The frozen interface may distinguish a rejected competing operation from a transport failure whose outcome is initially unknown. Those cases need different reconciliation rules; the chapter does not assign response codes in advance.

For a high-risk v2 request, the first approval is a successful partial contribution. If a rejection becomes effective while the request remains pending, the resulting history can legitimately include that contribution followed by a terminal rejection. If two distinct eligible approvals complete before a rejection takes effect, the accepted terminal history must remain consistent with approval. The oracle must inspect the complete sequence under its declared concurrency model rather than simply prohibit every mixture of approval and rejection records.

This distinction also prevents an overly strict test from rejecting valid business history. A prior partial contribution is not a second terminal outcome. A separate security log of an unsuccessful attempt is not a successful business transition. Define which record types the assertions count and which additional diagnostic records are allowed.

None of these histories has been observed here. They are proposed constraints for independent review before a concurrency test exists. The implementation's database isolation, synchronization and retry behavior still need a real design and exercise; a plausible order described in prose supplies none of those guarantees.

### Check version binding through creation and change

The local policy model reads a supplied version. A stronger application check must establish where that version came from and whether later policy activation changes existing work. Merely constructing an in-memory record marked v1 cannot prove the creation/migration behavior required by CS-13.

A proposed acceptance card begins with a controlled v1 policy and creates a valid high-risk request through the agreed application boundary. Retain evidence of creation and leave the item pending. Activate the reviewed v2 policy through the exercise's defined setup procedure, then create new standard-risk and high-risk requests. Keep expiry, membership and other conditions suitable throughout.

The original high-risk request should still use its v1 threshold. The new standard-risk request should need one eligible contribution, and the new high-risk request should remain pending after its first and complete only after a second distinct eligible contribution. Observe the required history as well as state. A completed v1 request should also remain a consistent historical decision after policy activation.

The observation method must be agreed in advance. The contract may expose a version in the permitted response, or the reviewed harness may use a defined evidence view. The case does not require a newly invented public debugging endpoint. What matters is that the assertion establishes creation-time binding without trusting a field injected by the test itself.

This card is a future design, not an executable test or a completed migration exercise. It identifies the integration evidence missing from the narrow function example and gives every method the same preservation obligation.

<!-- C11-S06 -->
## E3: a boundary defect

E3 uses one predetermined defect in a shared prepared baseline. The proposed defect concerns tenant isolation on a defined query path. Its exact implementation and hidden acceptance probes must be fixed before runs; the current project has not created or exercised that seed.

A useful defect report should describe observable behavior without handing one method a more helpful diagnosis. For example, a synthetic report could identify that a B actor obtains data associated with an A request through a particular operation. That is a proposed report shape, not an incident that happened here.

The diagnostic procedure should first reproduce the boundary under controlled identities and a known existing record. Inspect the request/tenant relationship, current actor membership and relevant query/authorization path. An access denial obtained only by deleting the fixture would not be a repair.

Narrowness concerns intent, not the smallest line count. A correct repair may need a shared boundary check and multiple regression probes. An unrelated architectural rewrite would need a separate reason. Preserve failed attempts, especially when one closes the visible path but leaves a related route exposed.

The common acceptance inventory includes direct identifiers, lists and searches. The seeded defect may affect only one path, but regression scope should follow the shared boundary and the predefined contract. Do not expand hidden tests after observing which method performs well.

The four methods may legitimately take different small-change paths. Compare the documented selected route rather than force full greenfield planning on all of them. Record any departure, manual intervention or unavailable host capability. A profile change is part of the evaluated arrangement.

The expected execution packet would contain baseline evidence that the fixed probe fails before repair, actual change/diagnosis records and after-repair regression observations. None is present. CS-15 therefore remains Not run; the prose does not simulate a failed or successful trial to complete the narrative.

### Distinguish a narrow repair from a narrow check

A small code change can close a shared boundary while a single happy-path check leaves it unexamined. Conversely, many new tests can all exercise an unrelated denial condition. Choose regression scope from the affected requirement and dependency path, not from the patch's line count or the size of the generated suite.

The predetermined failing probe should name the actual operation and fixture. If a search path leaks an A record to B, choose a term that would reveal that record and keep the permitted A search as a control. If a direct-ID reader is affected, establish the target's existence and the actor's valid membership in B. Preserve those conditions across the before/after observation.

Then inspect related paths according to the predeclared acceptance inventory. A shared query helper could affect list and history behavior as well as direct lookup. A framework may recommend a broader review, but the scored boundaries and hidden checks must not be adjusted after observing an arm's result. Additional discoveries can be retained as out-of-scope findings or a separately declared follow-up.

Keep a failed attempt as an artifact with its baseline, change and observation. A later accepted repair does not make the earlier investigation disappear. The record may explain a context omission, a wrong diagnosis or an oracle defect. Those explanations have different implications for process selection.

For a future reset, restore the same prepared defect rather than hand-edit a vaguely similar error. Verify the baseline hash and fixture state, then confirm that the predeclared probe still exposes the intended behavior. Otherwise later arms might receive a different challenge even when the report text is identical.

No fault injection, baseline reset or repair check has been performed in this manuscript package. The concrete design gives a reviewer something to inspect and a future operator something to implement, without manufacturing the missing observations.

### Inspect the repair for permitted access as well as the leak

The proposed E3 repair starts from the same planted tenant-boundary defect for each future arm. One approach might add a tenant predicate at the reported endpoint. Another might change a shared lookup so callers must supply the tenant scope. Before choosing a design, inspect which paths use the affected helper and identify which ones should continue to retrieve the request. An overbroad fix that makes all reads fail would suppress the symptom and break the intended A path.

A proposed acceptance pair uses the same known A request. An authorized A actor exercises the reported path and sees the data permitted by the contract. An actor in B tries that identifier and receives the defined disclosure behavior. If the repair changes a shared lookup, repeat the observation for the applicable list, search or history paths. The exact interface and hidden regression inventory still need to be frozen by the evaluator.

Keep the planted defect and the acceptance observations outside the native repair notes used by an implementer. The issue should include the agreed reproduction and enough context for a legitimate investigation. The evaluator's additional probes should be prepared before seeing any repair. That division makes it possible to compare how the native work identifies affected paths without turning the hidden checks into a guide for one of the arms.

<!-- C11-S07 -->
## What the records support

The records currently support a business specification, source-specific process mechanisms and an original comparative inspection design. They support questions about how intent, context, authority and acceptance would be related. They do not establish implementation results or framework effectiveness.

Keep a claim/result distinction at the episode level:

| Item | Current disposition |
|---|---|
| Accepted domain and language family | Recorded author direction |
| Business requirement inventory | Design definition; executable review/freeze pending |
| Native artifact trails | Documentary teaching maps, not generated run outputs |
| Separate author-written policy model | Ten local sequential checks passed; not application acceptance or independent validation |
| E1 implementation acceptance | Not run |
| E2 policy-change acceptance | Not run |
| E3 failing baseline and repair regression | Not run |
| Timing, cost and defect comparison | Not assessed |
| Production/team/longitudinal outcomes | Not observed |

An author-designed example can reveal an ambiguity without proving how often it occurs. The earlier pilot's self-approval fixture ambiguity is a real editorial finding in the book material, not an application bug or a failed framework trial. Preserve that distinction when using it diagnostically.

If later execution fills these gaps, retain adverse results and the original protocol. An installation problem should not become an application failure score. A successful manual correction should not disappear from the effort record. A changed requirement should trigger a task-identity review rather than be silently absorbed into a favorable result.

The qualitative route is the honest current deliverable because essential execution controls are unmet. It remains useful as a reproducible way to inspect primary instructions against a shared business problem. It cannot answer which method is faster or safer.

### Separate what the walkthrough teaches from what a later run would establish

The walkthrough follows one set of business obligations through several representations. A reader can inspect whether the proposed artifacts preserve tenant scope, requester exclusion, version binding and distinct contributions. That inspection can reveal a contradiction in the design before any application exists. Record such a finding as a design issue with the owning rule and affected handoff.

An executable episode would add a different observation. It would identify the actual environment, input sequence and resulting durable state. A passing observation on one path supports that path under its fixture. A failing one can reveal a defect or an invalid fixture, and the record should preserve enough information to tell which. Neither outcome should be backfilled into this walkthrough as though the proposed artifact had produced it.

A comparative run would add the configured method and its operator actions. The evaluator could inspect which decisions were available, which interventions were needed and what each candidate produced against the common boundary. The case design gives that exercise a starting point and shows where independence and baseline control are required.

The resulting evidence packet should preserve all three kinds of work. The accepted design explains the expected behavior. The execution record shows what happened. The comparison interpretation explains which claims follow from those observations. Keeping their relationship explicit lets a reviewer challenge a conclusion without losing the useful design or the underlying result.

<!-- C11-S08 -->
## Reproduce and delimit the case

To reproduce this documentary exercise, begin with the case specification and its CS inventory. Read the four pinned source trails identified in chapters 4–7. Map each requirement into the selected native records, distinguish prescribed from optional work, and record unresolved decisions. Compare the resulting maps using F01–F11 without assigning outcomes that were never observed.

A narrow executable companion is available in [examples/approval-policy](../../examples/approval-policy/README.md). It models only an approval transition over trusted in-memory records: tenant/current-role eligibility, self-approval exclusion, distinct counting, terminal rejection of later approvals and creation-bound v1/v2 thresholds. Ten author-written checks passed under the locally available Node.js v26.13.0; the [actual output and file hashes](../../research/evidence/POLICY_MODEL_RUN.json) are retained. No package was installed.

This observation does not fill the application acceptance table. The example has no authentication, database, audit, HTTP interface, idempotency-key handling, rejection operation or concurrent execution. Its internal duplicate-actor result is not the future retry contract. TypeScript is executed through Node's type stripping; `tsc` is unavailable on the session PATH, so static type-checking was not performed. [Node's execution limits](https://nodejs.org/api/typescript.html) distinguish this from compiler validation. The model and checks were authored together and are not an independently reviewed oracle.

The repository's `python3 scripts/check_manuscript.py` command audits manuscript hashes/counts, section/title coverage, citation receipts and local-link paths. It checks document integrity. It does not install a methodology, build the SaaS or certify a requirement. The actual command/output record is linked from the manuscript report.

An executable reproduction requires the additional inputs defined in the [run protocol](../../research/RUN_PROTOCOL.md): stack/host/model identities, installed artifacts, per-episode baseline hashes, fixtures, independent checks, reset commands, allowed interventions, resource limits and retained outputs. Missing values must stay missing until genuinely supplied.

### Reproduce the documentary analysis

The paper exercise can be repeated without buying a model subscription or installing every workflow. Begin with one CS requirement and one episode. Read the cited pinned instructions and write down the artifact that should carry that requirement, who owns the relevant decision, and what evidence the selected route prescribes. Keep each statement's source locator next to it.

Next, test the interpretation against a counterexample. For CS-05, ask whether a plausible native record could omit requester identity while retaining an approver role. For CS-13, ask whether a global threshold change would satisfy the record while altering old requests. These are semantic probes of the documentary map; they are not attempts to predict a model's output.

Compare your map with the chapter's teaching sketches. Disagreement is useful when it identifies a source ambiguity, a version difference or a missing assumption. Record the two interpretations and the passage that would resolve them. Do not treat agreement with the book as the acceptance oracle for a future implementation.

Finally, complete a disposition for the chosen episode: documented mechanism, external dependency, unresolved contract, or observation needed. This produces a reviewable artifact even when execution is not yet possible. It also prevents an articulate walkthrough from quietly being relabeled a benchmark.

### Package the evidence for a future rerun

A future case packet should keep the common task and native outputs in separate locations with explicit links. The common area contains requirement/contract versions, fixture definitions, baseline identities and oracle rules. Each attempt area contains the selected profile/configuration, native planning/implementation/review records, operator interventions and actual outputs. A results index points to observations rather than restating unsupported success claims.

The package also needs a boundary around unavailable information. A hosted model may not expose a fully reproducible internal build identity; disclose the identifier available and run date. A required service may be inaccessible; record the stopped scope. A native artifact may contain sensitive content; preserve a reviewed redaction and state what cannot be independently recovered. None of those limits should be hidden by a generic reproducible label.

The present repository preserves source receipts, manuscript identities and the separate policy-model run. It does not contain the future common application packet. Keeping those artifact classes distinct lets readers reproduce what exists today and identify exactly what is needed for the stronger experiment.

### A concrete blank episode packet

An operator should be able to locate the common input and the evidence for one attempt without reconstructing the study from a chapter's narrative. The following packet design is original and proposed. Its fields are deliberately unfilled: no application baseline, installed profile or episode result exists to insert.

| Record | Fields to supply before or during a future attempt |
|---|---|
| Common episode definition | Episode ID, requirement/contract revision, included and excluded work, fixture definition, controlled clock and expected-result rules |
| Baseline identity | Source revision/hash, dependency identity, persistent-state reset, seed procedure and baseline verification evidence |
| Selected arrangement | Framework/source/package identity, host/model identifiers, profile/modules, guard/review settings and declared substitutions |
| Attempt identity | Unique attempt reference, episode, operator, order, familiarization and resource/stopping rules |
| Native evidence index | Actual intent/context/plan/implementation/review records and links to the external CS obligations |
| Observation entry | Check ID, starting fixture, actual command, exit/output evidence, observed state/history and interpretation |
| Intervention entry | Time/order, responsible person, trigger, action, affected artifacts and whether it changed the task |
| Attempt disposition | Completed, stopped or invalid under the predeclared rules, with missing observations and retained outputs |

The common definition and per-attempt identity have different jobs. A change to an attempt's native plan need not change the business task. A newly accepted rule or altered baseline may do so. Keep those revisions separate so a reviewer can decide whether two observations remain comparable.

Use stable references for observations rather than placing an unqualified Pass in the narrative. A reviewer should be able to move from CS-05 to the relevant fixture, then to the actual command/output and the state/history assertion. If a command never ran, the entry remains unexecuted. If an observation cannot be interpreted because setup failed, retain that failure and mark the business question unassessed.

The packet should also expose missing work. A completed local build would not substitute for a restart observation, and a passing policy test would not populate tenant-isolation fields. Do not fill empty cells with a nearby result simply to produce a complete table. Distinct evidence duties stay distinct even when the same command supplies several valid observations.

Review the packet from the perspective of a second operator. Can they identify the intended clean starting state? Can they tell which files are common inputs and which were produced by the attempt? Can they recover the policy decision used by a check? Can they distinguish a manual correction from the original output? A missing answer becomes a preparation defect to fix before claiming reproducibility.

The repository's existing manuscript manifest illustrates exact artifact identity, but it is a document manifest. Its chapter hashes and section checks cannot be reused as an application baseline record. The policy-model run preserves a real command/result, but only for that separate example. The future packet needs its own identities and observations for its own task.

The case can then produce bounded observations about this local synthetic service. Wider conclusions require different evidence: people and teams for coordination, operational exercises for recovery, longer maintenance for drift/cost, and replication for more stable estimates. No one local trial should stand in for all of them.

This chapter gives readers an inspection design they can challenge and a precise boundary around its present evidence. The next chapter develops the acceptance and operational duties needed before those missing results could support stronger claims.

### Give another reader a reproducible design packet

For the walkthrough, a second reader should be able to reconstruct each starting state without seeing a model conversation. Give each episode a manifest containing the business obligation, policy version, initial actors and records, known decision owners and the proposed observation. If the case later becomes executable, add the actual baseline revision, schema or fixture version, installed tool profile and commands under that episode's record.

Keep creation and evaluation inputs distinct. For a future repair trial, the implementer receives the authorized issue and a known reproduction. The independent reviewer holds the fuller inventory of protected surfaces and preserved behavior. Each receives a different view of the same agreed requirement, for a different job. A third person should be able to inspect that division after the run and tell whether one arrangement received extra guidance.

An example of a reproducibility failure is a v1 probe that depends on a manually seeded record with no documented version. The reported transition might be repeatable for the original operator and ambiguous for another reader. The repair is to define the record's origin and expected behavior before drawing a conclusion. The same principle applies to the experimental baseline. A Git revision identifies source, while fixtures, configuration and installed packages identify the starting conditions in which it was used.

Use the packet to retain unresolved questions as well as decisions. If replay conflict semantics remain unsettled, label the affected checks as awaiting a contract. The rest of the episode can still be inspected. This makes the qualitative walkthrough useful as a design even when the corresponding execution evidence is unavailable.
