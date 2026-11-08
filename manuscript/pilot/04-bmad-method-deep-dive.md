# 4. BMAD Method — Deep Dive

> Author manuscript · completed 2026-11-05 · C04 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C04-S01 -->
## Define the BMAD intervention

The first decision in a BMAD evaluation is which BMAD we mean. A framework name is an incomplete description of an intervention. We need the source revision, the enabled modules, the coding host and the path selected for the work. Those choices determine what instructions and checks an operator actually encounters.

This chapter examines the stable-source candidate reviewed for the book, at commit `bab9082…`. Its package manifest identifies version 6.12.4. The pin fixes which source we discuss; registry contents and installation behavior require separate checks. [Inspected manifest, lines 1–8](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/package.json#L1-L8)

Within that boundary, we will follow the planning, specification, Build and completed-work testing guidance. Built-in QA is included in the discussion. TEA is a separate optional module, whose scope we distinguish from the base configuration.

Our business problem is the vendor-access request from the common case. A tenant member submits a request, an eligible different member decides it, and the service preserves the decision. The example has just enough policy to expose a dangerous shortcut: an administrator who submitted a request remains disqualified from approving that same item. The case has a TypeScript / Node.js direction, but that choice does not select an application framework or database.

The intervention can now be stated precisely enough to investigate:

| Item | Scope of this chapter |
|---|---|
| Source | Pinned BMAD source identifying manifest 6.12.4 |
| Workflow material | Planning path, specification, Build and existing-code guidance |
| Test-generation scope | Built-in QA described; TEA remains an optional alternative, unexecuted |
| Business slice | Tenant-local request/decision behavior and a later approval-policy change |
| Evidence | Inspected documentation, author-designed examples and explicit evaluation questions |
| Outcomes | Execution, effort, defect detection and maintenance benefit: not assessed |

Record optional modules and host behavior separately. An instruction to perform a review establishes the intended workflow; an execution record must establish whether and how the review happened.

<!-- C04-S02 -->
## Choose how much planning the change needs

BMAD's selected planning guide begins with the state of the intent. When the intent is defined, it can be shaped into a specification and built; when important intent is missing, planning activities help establish it. Those activities are selectable aids rather than a compulsory sequence of stages. The guide also permits an obvious low-risk edit without invoking BMAD. [Planning-path guidance, lines 8–65](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/choose-a-planning-path.md#L8-L65)

The practical question is what remains undecided. “Build vendor approvals” is not a defined intent for our exercise. It leaves the actor, tenant boundary, number of approvals, terminal behavior and existing-request policy open. “Reject self-approval even when the requester holds an administrator role, preserving other valid decisions” is a much narrower instruction. It still requires investigation of the existing application, but the product rule is clear.

For the first increment, we would give the process the agreed business behavior and identify unresolved interface details. We would not treat unanswered questions as implementation freedom. The idempotency-key contract, for example, affects what a retry means. Its answer belongs in the agreed behavior before the implementation is assessed against it.

For a small maintenance change, the selected Build documentation describes investigation before asking the user for information the repository can settle. It then distinguishes a light route from a written-plan route using missing intent, irreversible actions and the footprint of the change. Flagged designs require questions to be answered and a plan approved. [Build investigation and routing, lines 62–81](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L62-L81)

That route is a documented decision procedure, not a certified risk assessment. A reviewer must still examine whether the system identified the relevant uncertainty. If the proposed design says that self-approval is a user-interface concern, it has misunderstood a business-interface obligation in the case. Taking a light path after that misunderstanding would not settle the requirement.

We can make the routing judgment inspectable with a short, original planning note:

| Question for the proposed increment | Current case answer | Consequence for the operator |
|---|---|---|
| Is the actor rule agreed? | Yes: current same-tenant approver, excluding the requester | Carry CS-04 and CS-05 into the work |
| Is the retry behavior fully specified? | Not yet | Resolve the key/conflict contract before executable acceptance |
| Is external access provisioned? | No | Keep external systems outside the change |
| Is existing data affected? | Depends on the later policy episode | Make version binding explicit before that episode |

This original teaching note identifies decisions for a future route review. It is not output from a BMAD run.

Planning must also have an endpoint. Once the relevant intent is defined, repeatedly asking for a new product document would add work without necessarily adding a decision. Conversely, a short request does not make a change low risk. A one-line instruction that changes the meaning of existing approvals may require more investigation than a larger, isolated formatting change.

### Stress the route with a concrete change boundary

Consider three proposed requests for the same application. Correcting a label leaves policy and stored state alone. Moving an eligibility condition into a shared decision path may change several callers even if the diff is short. Introducing creation-time policy binding may affect existing records and require a migration whose behavior has not been agreed. These are different settled designs, not merely different amounts of text in a prompt.

For each, write a routing justification after discovery. Identify what is already known, what the operator would notice if guessed incorrectly, which actions affect durable state and where the change reaches beyond the apparent entry point. A statement such as small fix is not that justification. The reviewer should be able to challenge it using repository evidence.

Our v2 increment contains a useful trap: changing the current threshold to two might appear to implement the headline request. It would not preserve v1 semantics if every pending request reads that threshold dynamically. Discovery must therefore inspect the decision dependency, not merely locate the number one. The product rule is settled; the representation and migration remain technical questions.

If discovery reveals a new uncertainty, update the route before treating implementation progress as acceptance. A light-path decision need not be permanent. Equally, discovering a well-established convention can remove a technical question without reopening an agreed business rule. Record what changed the judgment so later evaluation can distinguish useful investigation from repeated ceremony.

### Choose a planning route from the unresolved work

An illustrative repair begins with a precise issue, an accepted response contract and a regression check that can reproduce the failure. The engineer knows which shared lookup is responsible and which callers need to keep working. A focused plan can identify the affected paths, the intended change and the observations required for acceptance. The review asks whether anything material remains undecided.

Now change one premise. The reported behavior is a failure only if the organization wants foreign identifiers and nonexistent identifiers to receive the same externally visible treatment. Nobody has settled that question. A detailed implementation plan cannot supply the missing authority. The next useful output is a short clarification that shows the alternatives and the paths affected. After the owner settles it, the planner can select a route sized to the actual repair.

Change another premise. The lookup is generated from a maintained schema, and the reported endpoint is one of several consumers. The plan now needs the generation source, a way to reproduce the derived code and a review of affected consumers. Even if the textual patch is small, the change crosses a broader maintenance boundary. The planning route should reveal that boundary before construction.

Record why a route was sufficient. For the first repair, the explanation may be that intent is accepted, the affected surface is bounded and existing regression infrastructure can observe it. For the second, clarification is a prerequisite. For the third, generation and integration require explicit coordination. These are case-specific reasons the reviewer can inspect after the work, without making route choice a proxy for sophistication.

<!-- C04-S03 -->
## Specialized perspectives and human decisions

The planning material assigns different jobs to research, product, UX, architecture and specification skills. Its guidance links the choice to the missing information: evidence for a decision, agreement about the product or shared technical choices, for example. A team does not have to invoke every perspective merely because the framework supplies it. [Planning activities and outputs, lines 50–86](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/choose-a-planning-path.md#L50-L86)

For the vendor-access increment, we would distinguish proposing a policy from accepting it. An AI-generated analysis could identify the ambiguity about existing v1 requests. It could propose retroactive migration or binding at creation. The product decision owner must choose the intended behavior. In this case, the accepted design direction binds a request to its creation-time policy. That answer comes from the case specification, not from the authority of a generated role.

Similarly, a technical perspective can propose where to enforce the rule and what persistence behavior is needed. The implementing engineer remains accountable for explaining the choice. If a proposal assumes a database or framework not yet selected for the book, it is a candidate design, not an authorized baseline. Good prose must keep that difference visible even when the proposed architecture sounds reasonable.

Build's documentation describes implementation followed by reviewer perspectives and correction of issues within the change. It also says that stronger dispatch depends on platform capabilities such as spawning workers or calling another model. [Implementation and review, lines 82–92](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L82-L92)

For our evaluation, several model perspectives would remain AI-assisted review. We would record which host could dispatch them, which model or process performed them, and what they inspected. We would not describe that arrangement as independent human acceptance. Even a separate model invocation could share the same mistaken interpretation of the case.

The operator's intervention is therefore part of the process evidence. Suppose a reviewer flags a possible self-approval issue. Did the operator reject the finding because it was out of scope, accept it as a requirement defect or ask for a code repair? Did the resolution alter the intent or merely its implementation? A record that contains only the final green verdict loses the decision we need to understand.

We would preserve disagreements at the level where they belong. If the requirement is wrong, revising the code alone leaves the wrong instruction available for the next session. If the requirement is right but the code is wrong, changing the requirement to match the output erases the defect. The selected Build guidance explicitly allows returning to an upstream plan or goal when that is the source of the problem. That is a mechanism worth evaluating through actual records, rather than assuming every reviewer exchange uses it correctly.

### Preserve the reason for a finding's disposition

A proposed review finding should identify the affected obligation, the relevant change and the evidence needed to decide it. For example, a concern about requester identity belongs to the current decision path when that path implements CS-05. A preference for an unrelated formatting convention may belong to later work. A tenant-boundary problem cannot be dismissed as unrelated if it invalidates the accepted scope of the increment.

The triage record can be compact: finding, basis, decision, responsible owner and follow-up evidence. Useful dispositions include correct the implementation, revise an inadequate plan, obtain a product decision, defer genuinely separate work, or reject with a reason. The labels describe different actions. They should not all collapse into resolved when the last review message ends.

Suppose an illustrative plan promises that administrators may always decide requests. A reviewer points to the requester exception. Repairing only the generated condition would leave the plan misleading for the next unit. The plan needs reconciliation with accepted intent, followed by the appropriate downstream change. Conversely, when the plan already carries the exception, the defect may be in implementation or testing. The same visible symptom can require a different upstream correction.

This review design is authored for the case. It does not claim a native report contains these fields or that a particular reviewer would discover the mistake. It defines the evidence we would preserve to evaluate the documented correction mechanism.

<!-- C04-S04 -->
## Carry artifacts and context forward

The selected specification guide gives `SPEC.md` a compact role. It describes five fields covering purpose, capabilities with success conditions, constraints, non-goals and a success signal. Supporting documents sit alongside the specification and are referenced from it. Updates go through `bmad-spec`, which is designated the writer of the file and is instructed to preserve capability identifiers. [Specification structure and maintenance, lines 97–124](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/define-requirements-and-a-specification.md#L97-L124)

That maintenance rule concerns the named `SPEC.md` artifact. It should not be generalized to every planning note or to the minimal specification mentioned in Build's light path. For a change to this artifact, the selected profile directs the operator through the designated skill. Chapter 8 compares specification ownership policies across approaches.

Here is an original content sketch for our case. It is a teaching table, not a generated `SPEC.md`, a copied prompt or an instruction to hand-edit that file:

| Content to carry | Proposed case content |
|---|---|
| Purpose | Record an accountable tenant-local decision about temporary vendor access |
| Capability and success condition | An eligible person can decide a pending request; the resulting state and audit history agree |
| Constraints | Tenant isolation, current membership, no self-approval, defined retry/concurrency behavior |
| Non-goals | External provisioning, billing, email and production identity federation |
| Success signal | Independent acceptance observations support the agreed behavior; unresolved cases stay visible |

The final row is our evaluation requirement. It is not a claim that BMAD supplies the independent acceptance reviewer or a completed oracle. A framework's artifact and the book's external acceptance boundary serve different purposes.

The linkage can be made explicit without forcing every method to use our file names. Retain BMAD's native capability identifiers and map them to the common CS requirements. The following teaching example shows the content of such a mapping; it does not assign native identifiers or claim that artifacts already exist:

| Proposed capability | Common requirement | Question for the implementation record | Acceptance evidence still needed |
|---|---|---|---|
| Decide a pending request | CS-04 | Where is current same-tenant approver membership checked? | Eligible actor succeeds; revoked and foreign-tenant actors are denied |
| Decide a pending request | CS-05 | Where is requester identity compared with decision-maker identity? | Overlapping-role requester denied on a pending request; separate eligible actor succeeds |
| Preserve the accepted decision | CS-07 | Which operation prevents a later conflicting terminal decision? | Controlled competing decisions retain one permitted outcome |
| Preserve decision history | CS-10 | How are the business decision and its audit record persisted together? | Matching state/history survive restart and remain tenant-scoped |

Every evidence cell describes future work. A real record would link the native capability, relevant story, implementation change and actual acceptance observation. If the story links to CS-05 but its check only hides a button, the chain has a semantic gap even though every file reference resolves. The correction belongs in the check or implementation, not in a stronger-looking traceability label.

If the work needs several sessions, the guide offers Story Breakdown, producing `stories.yaml` alongside the specification and letting the operator choose checkpoints. It describes implementation records linked to their parent specification or story. [Epic execution and linkage, lines 118–137](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/choose-a-planning-path.md#L118-L137)

Our proposed decomposition would preserve behavior across those slices. Creating requests, deciding requests and reading audit history may be separately reviewable work, but tenant isolation applies throughout. A story list that mentions isolation only in the final slice would need examination. The question is whether earlier slices can expose an unacceptable boundary while they are treated as complete.

Context transfer also needs a deliberate boundary. Build calls for a fresh chat, while investigation reads the repository and relevant upstream records. [Fresh-session instruction](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L28-L31), [investigation scope](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L62-L71). A fresh session is not evidence that the right context arrived. We would inspect whether the capability, constraints, agreed policy and relevant code were actually available when the change was made.

The useful artifact trail is consequently a set of checkable relationships: agreed intent to specification, specification to story, story to implementation record, and requirement to acceptance observation. Counting files would tell us little about the correctness of those relationships. A later experiment must examine the content and the decisions carried through it.

### Keep the unit and the larger undertaking distinct

The newly inspected Build page explicitly limits the unit's responsibility: larger work needs coordination above individual Build runs, with integration and later review outside that unit's own scope. It does not make Build the backlog owner. [Unit and larger-work boundary](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L132-L147)

For our proposed increment, a story that creates requests and a story that decides them must agree on tenant ownership and policy binding. Finishing both independently does not establish that the combined behavior is correct. Identify who chooses the next unit, who resolves a shared contract and who checks the integrated result. Those responsibilities must exist even if one person performs all three.

An illustrative decomposition could establish the request/identity boundary first, add eligible decisions next and then complete permitted history access, while checking the shared boundary at every exposed operation. This is not a requirement to use exactly three stories. It shows why cross-cutting constraints cannot be postponed to an unspecified final security story.

Checkpoint placement should follow decisions with downstream consequences. The first implementation may establish an authorization or persistence convention reused by later units. Review that convention before multiplying it. Later routine work can use an already accepted pattern, but a newly discovered contradiction reopens the relevant decision rather than becoming a local exception in each story.

Maintain a distinction between unit completion and increment acceptance in the evidence index. A unit can record a successful implementation step while the integrated requirement remains unassessed. The parent record needs enough information to find remaining work, failed checks and dependencies. A collection of individually confident summaries cannot supply that relationship automatically.

### Inspect a story split at a schema boundary

An illustrative BMAD planning record could split version binding into a creation story and a decision story. The creation story assigns a policy and persists the identifier. The decision story reads that identifier and resolves the eligible transition. Each seems small on its own. The order matters because a decision worker cannot distinguish an old request from a new one if the creation path leaves the identifier implicit. A reviewer can use the named specification to explain the dependency and ask the two story owners for one shared example.

Consider an existing request whose policy identifier is absent. One proposed migration fills the identifier with v1. Another makes the resolver infer the version when the field is missing. These lead to different consequences during rollout. Backfilling creates a migration step and an observable classification. Inferring in the resolver keeps the database shape simpler at first and makes every consumer of that resolver depend on the interpretation of an absent value. Before asking a story worker to implement either, record how historical rows will be classified and how ambiguous rows will be handled.

A useful story records the deliverable at its boundary. The creation worker can demonstrate that a request created under each supported policy carries the expected version. The decision worker can show how the saved version determines the threshold even after tenant settings change. The joint acceptance example begins with real creation, changes the active setting and decides the same stored request. Keeping the third observation visible prevents two individually complete stories from hiding a missing integration.

A different split puts the smallest end-to-end path into one story, then adds replay and exceptional histories separately. This exposes integration earlier, at the cost of a wider initial diff. The planner should choose based on whether the architecture is known and whether the team can review a vertical change coherently. The specification supplies the preserved rule in either split. Record the dependency and the acceptance owner in the work packet so a later reviewer can see why the split was chosen.

| Proposed handoff | Producer's deliverable | Consumer's question |
|---|---|---|
| Accepted behavior to story | Rule, preservation example and unresolved contracts | Which decisions can this story use? |
| Creation to decision | Defined persisted identifier and historical-data policy | Can the decision path recover the creation-time policy? |
| Integrated work to acceptance | Candidate revision and observations through creation and decision | Does an actual preserved request behave under its original version? |

These are proposed inspection points for the book's case. A reviewer applying them to an existing project should use the repository's actual data lifecycle and keep untested rollout behavior visible.

<!-- C04-S05 -->
## Build, review and establish acceptance

The selected Build page describes modified source, a local commit, an implementation record and passing tests when the project has a suite as intended outputs. It also separates unrelated work into a deferred-work record. These are documented outputs, not observations from our repository. [Build outputs and deferred work, lines 113–131](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L113-L131)

The distinction matters most at acceptance. An implementation record can say what changed and which checks were attempted. We still need the actual commands, the outputs and the relationship of each assertion to the business rule. If the suite has no test for overlapping roles, a passing result cannot answer CS-05.

The completed-work testing guide states the scope of its built-in QA: API and end-to-end coverage generated from existing code, with happy paths and a limited set of error cases. It distinguishes test generation from implementation review and describes more complex fixtures and additional coverage as follow-up work or reasons to use the separate TEA module. [Testing scope and optional module](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/test-completed-work.md#L8-L34), [explicit limits, lines 76–105](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/test-completed-work.md#L76-L105)

Generating tests from existing code can provide useful checks of that implementation. The acceptance question is broader: does the implementation satisfy behavior agreed independently of it? Our proposed external checks derive from the common case requirements. They should be prepared and reviewed before we inspect a method's generated solution. Otherwise, the implementation could quietly become the definition of what was required.

For this increment, we would look for evidence at several boundaries:

| Obligation | Proposed observation | What the observation would leave open |
|---|---|---|
| CS-05: no self-approval | On a pending request, an overlapping-role requester is denied; a separate equivalent fixture permits an eligible different approver | Other identity and authorization paths |
| CS-03: tenant isolation | Foreign-tenant direct-ID, list and search checks follow the disclosure contract | Unexamined interfaces and wider production assurance |
| CS-08: idempotent retry | A repeated identical decision creates no duplicate successful action | Key retention and other payload conflicts unless separately tested |
| CS-09: concurrency | Controlled competing decisions preserve one valid terminal outcome | Schedules and failure conditions outside the exercise |
| CS-10: durable audit | State and matching history survive a controlled restart | Backup, recovery and operational guarantees outside the test |

These checks need explicit starting conditions. If the self-approval attempt targets an already completed request, a terminal-state guard could reject it even when the identity rule is absent. Keep that request pending, give the requester the otherwise required role, and use a separate equivalent fixture for the allowed action. This isolates the rule the check is intended to examine.

Persistence and concurrency mechanisms remain unselected and untested. The case contract and independent reviewer must settle the executable checks before matched runs.

Adding TEA would change the evaluated configuration. It might be an appropriate separate profile, but its setup, selected skills and operator effort would need to be recorded. We should not silently give one arm more preparation or describe optional coverage as if it were produced by the base path. Equally, using a small built-in path does not justify claiming that BMAD cannot support broader testing.

The same discipline applies to review findings. A local fix, a generated test and an AI review verdict are different evidence items. The report should show which business uncertainty each addresses and which remains open. Chapter 12 develops the wider assurance obligations; this chapter keeps them connected to the workflow that produced the change.

### Inspect what generated coverage assumes

For a proposed approval test, ask where the expected outcome originated. A test derived from current code may assert that an administrator succeeds because the code currently permits it. The assertion is executable but contradicts the requester exception when that administrator created the request. More executions of that assertion would strengthen confidence in the wrong behavior.

Use the external CS inventory to inspect omissions as well as disagreements. A suite can cover valid approvals yet contain no foreign-tenant read. A test titled no self-approval can target an already terminal request and exercise only its terminal guard. Review the starting state and the observable effect, not just the test name or generated coverage summary.

The book's proposed check map should preserve which assertions came from native generation, which came from independent requirement review and which were added after a finding. That provenance matters when interpreting defect discovery. A later human-supplied counterexample is part of the evaluated arrangement; it must not be retroactively presented as autonomous coverage.

Changing from built-in QA to a larger optional testing path can be a reasonable response to an identified need. Record the profile change, the additional preparation and the obligations it is intended to address. Do not treat either the expanded configuration or the original narrower one as the only possible BMAD intervention.

### Review the Build handoff when the patch looks plausible

Consider a change that adds the two-approval rule by looking up a tenant's current settings inside the decision handler. The diff may be short and the happy path may pass. In the proposed case, this design still needs inspection because a v1 request can outlive the setting that was current when it was created. Give the reviewer the named specification and the linked work record, then ask them to trace the source of policy identity through creation and decision.

A useful review finding states the expected behavior, the proposed failure and the evidence needed. For example, a v1 request created before the policy switch should still be decidable with one eligible approval. If the implementation reads the newest settings, ask for an observation using a genuine pre-switch fixture. The developer can repair the resolver and update the linked work record. A refreshed result should identify the revision that contains both the fix and its check.

If the native review reports no findings, retain the report with its inputs and scope. The acceptance reviewer still has a distinct job. The native result helps explain how the change was reviewed, and the case observation explains whether the selected requirement held. The two records can be inspected together without treating one as a substitute for the other.

<!-- C04-S06 -->
## Existing code and evolving requirements

The existing-code guide prioritizes the current application, recommends compact project context where needed and advises keeping old greenfield material away from ordinary small changes. It also tells the process to use existing documentation and code when planning and to follow established patterns unless a change explicitly calls for a different one. These are source prescriptions, not evidence that the existing code is necessarily correct. [Existing-code guidance, lines 8–79](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/existing-codebases/start-in-an-existing-codebase.md#L8-L79)

This guidance creates a useful review question for the common case. Current code can show where an approval decision is made and what conventions the project uses. The accepted policy must still tell us whether that behavior is right. If an existing endpoint permits self-approval, faithfully preserving the pattern would preserve the defect.

We would separate repository discovery from normative intent. Discovery describes what the application does. The change request states what should become true. When the two disagree, the operator needs a record of the intended correction. Archiving stale product context can reduce competing instructions, but the evaluation must check that current invariants remain discoverable. We cannot infer either benefit or loss from an archive policy alone.

The proposed second episode makes that tension concrete. Policy v2 requires two distinct approvers for newly created high-risk requests. Existing v1 requests retain their creation-time policy; standard-risk v2 requests still need one approval. An instruction that mentions only the number two would leave several decisions unresolved.

We would first inspect the baseline's representation of policy, decisions and terminal state. Then the specification change would carry the agreed version-binding rule through the designated maintenance path, retaining capability identifiers where appropriate. The proposed story or implementation record would identify which existing behavior must stay valid and which new behavior is introduced. None of these steps has been performed in an installed BMAD session.

Acceptance needs both sides of the transition. A new high-risk v2 request should remain pending after the first eligible approval and complete after a second distinct one. A pending v1 request should keep the old threshold. Repeating the first approver must not advance the distinct count. Those examples come from CS-12 and CS-13, not from an imagined framework result.

For a fair method comparison, this episode would start from the same externally prepared baseline for every arm. Using each arm's feature output would make the change depend on different code structures and earlier mistakes. Native planning artifacts may differ; the starting business behavior and the acceptance boundary should not.

The third episode would ask for a narrow repair in a shared baseline containing one predefined tenant-boundary defect. BMAD's small-change path is relevant here. The evaluation should allow an appropriate bounded route rather than impose a full product-planning ceremony. It should also retain enough evidence to show that the repaired query and related behavior meet the agreed contract.

### A discovery note that preserves contradictions

Before the proposed policy change, record the baseline locations that currently create a request, establish membership, count contributions, determine a terminal outcome and expose history. For each location, separate observed behavior from the intended rule and the evidence still required. This is an investigation aid, not a prescribed BMAD file format.

If a maintained document says policy is bound at creation while the current decision path reads a global setting, retain both observations. Their disagreement is the important finding. Choosing the newer-looking file without inspecting the dependency would merely hide the conflict. Accepted intent determines what the change should achieve; discovery establishes what must actually be changed.

The follow-through then becomes reviewable: specification revision through its designated owner, affected story/implementation records, actual code and checks, and the integrated disposition. Stable references help connect the trail, but the reviewer still has to inspect their meaning. An unchanged capability identifier can carry a revised rule whose downstream consumers have not yet caught up.

No such baseline investigation has been executed here. The note's value is its concrete division between repository evidence, accepted behavior and unresolved work. It lets a future reader challenge the implementation plan before treating a clean artifact trail as a complete maintenance result.

### Inspect a repair that changes a generated surface

An existing-code repair may affect files produced by a generator. Ask the contributor to identify the maintained input, the derived output and the reproduction command used by the project. Review the proposed correction at the input that owns the behavior. Then compare regenerated output with the intended repair and inspect other consumers that generation affected.

If the repository cannot reproduce the current output, record that observation before choosing a repair path. A bounded manual correction can be proposed with its maintenance consequence and owner. The named specification and work record should expose where a future regeneration could undo the correction. That lets the reviewer assess the actual repair under the repository's conditions.

<!-- C04-S07 -->
## Limits and conditional fit

For this source profile, the central design is a choice of planning depth tied to intent, a compact specification with explicit maintenance ownership, linked implementation work and review/test activities whose scope must be identified. These mechanisms give us concrete things to inspect. They do not establish lower effort, better quality or sustained alignment.

Our editorial judgment is conditional. A team with reasonably clear intent and a need to scale between a bounded repair and multi-session work could investigate this profile. It should test whether the routing decision preserves its important constraints, whether the native artifact links remain useful after change, and whether its selected host can support the intended reviewer behavior. This is a proposal for evaluation, not a recommendation to adopt BMAD on reputation.

Three unknowns would materially affect that judgment. First, can operators reliably notice when apparently clear intent hides an important gap? Second, do the maintained artifacts help the next change enough to justify their cost? Third, does the chosen QA/review configuration find relevant defects under the available resource ceiling? Documentation supplies design expectations for these questions. Our research has not supplied their measured answers.

The operations boundary remains open as well. The inspected passages do not establish comprehensive production-operation or rollback governance. We should report that limit of inspection without turning it into a claim that the wider method lacks such practices. A local implementation exercise would still leave deployment, recovery and service ownership to be assessed separately.

Before accepting this chapter, a technical reviewer must check the selected source scope, artifact-ownership descriptions and the distinction between base QA and optional TEA. Before accepting executable examples, the book needs an actual environment, frozen inputs, independent checks and retrievable run records. The pilot has none of those results.

Chapter 9 compares the supported mechanisms across the four frameworks. Chapter 10 uses those boundaries to make conditional choices. The question carried forward from BMAD is practical: for this change, did the selected path preserve the decisions and evidence the team actually needed?
