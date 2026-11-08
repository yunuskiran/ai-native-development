# 7. AI Unified Process — Deep Dive

> Author manuscript · completed 2026-11-05 · C07 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C07-S01 -->
## Define the method and adapter boundary

AI Unified Process (AIUP) makes requirements, use cases and their downstream relationships central to its documented workflow. The engineering question is what those relationships let a reviewer establish and how they survive change. A set of identifiers is a starting structure, not proof of aligned behavior.

The inspected artifact map connects requirements, domain records, use cases, architecture decisions, test journeys and acceptance/release documents. It identifies producers and consumers, including human responsibilities. This supplies a concrete process to examine without adopting every implementation product as part of the method. [Core artifact flow](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L48-L66)

The TypeScript / Node.js case preference makes adapter scope material. The inspected combined construction plugin targets NestJS, Drizzle over PostgreSQL and a Next.js App Router frontend. That is a particular application arrangement. Choosing a language family does not automatically choose these technologies or demonstrate that the plugin works in the book's environment. [Combined Node adapter](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/README.md#L9-L26)

Keep three layers separate: core behavioral artifacts, the selected construction path, and any host or product used to operate it. A core specification convention can be common across paths while the implementation and coverage mechanisms differ. A repository snapshot is also not an umbrella semantic version for the entire methodology.

This chapter therefore examines core artifact/maintenance rules with the combined Node path as a documentary candidate. No plugin installation, database, frontend or compiler has been frozen. The future comparison must either adopt a compatible common stack deliberately or disclose the work and limitations of an adaptation.

The case remains our original vendor-access service. Its actors, tenant boundary and policy change come from the common specification. We do not reproduce an external book's application or sequence of exercises. Lawful full-text originality review remains outstanding; independently composed case material does not close that review by itself.

### Identify which part of an adapter is being evaluated

A stack adapter can supply construction conventions, testing guidance and ways to interpret markers. Inventory the pieces actually used in the candidate setup. A document that describes an implementation route supports a claim about the prescribed route. A successful local build would add evidence about its compatibility in the chosen environment. A coverage report would address another boundary again.

For the Node case, keep the inspected limitation on a shipped equivalent auditor visible when describing traceability. A team may perform the review manually or adopt another supported arrangement. Record that work in the evaluation packet, including who interpreted the specification-to-code relationship and what evidence they inspected. The configured arrangement then has an identifiable review duty even where automation differs.

<!-- C07-S02 -->
## Requirements and use-case ownership

A useful requirement identifies what the service owes its users. A use case organizes behavior around an actor's goal and the conditions under which the goal succeeds or fails. In the inspected workflow, stable requirement/use-case/rule references form a trace chain into construction and tests. The source separately describes isolated use-case tests and journeys connecting use cases. [Traceability convention](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L111-L136)

For the common approval increment, the relevant goal is to contribute a permitted approval to a pending vendor-access request. The actor must be currently eligible in the request's tenant and must not be the requester. The goal cannot be specified as “click Approve” alone: that wording leaves the business preconditions and effects outside the statement. Rejection authority needs an explicit contract; the self-approval exclusion alone does not settle whether an otherwise eligible requester may reject their own item.

The following is an original use-case content sketch. Its local identifier is illustrative; the common CS identifiers remain the external acceptance vocabulary:

| Field | Teaching content for `UC-001 — Contribute an approval` |
|---|---|
| Primary actor | Current eligible approver in the request's tenant |
| Goal | Record a permitted approval contribution on a pending request |
| Preconditions | Authenticated tenant membership; existing tenant-local pending request; selected policy known |
| Main success direction | Validate approval eligibility, apply the bound policy, preserve the contribution, resulting state and audit history |
| Required alternatives | Requester deciding own request, foreign/revoked actor, terminal request, retry/conflict and competing decisions |
| Related requirements | CS-04–CS-10, with tenant reads governed by CS-03 |
| Open questions | Detailed interface/disclosure contract, idempotency-key scope and persistence mechanism |

This sketch is not a complete executable specification. It helps a reviewer identify which business decisions are present and which remain unresolved. A generated artifact could improve or contradict it; the comparison should inspect that difference rather than force the sketch into every native file.

Ownership matters when a use case is ambiguous. A model can propose an alternative flow; the product decision owner must accept a change to intended behavior. The implementing path can choose technical details within its allowed boundary, but it must not silently settle an unanswered business limit.

The workflow's explicit authority categories are scoped to layered orchestration. Its defaults distinguish agent-alone decisions, questions requiring an answer and prohibited unilateral changes. The combined Node path has separate instructions. We should not apply the layered list universally merely because both paths belong to AIUP. [Construction inputs and scoped decision rights](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L319-L357)

For our teaching case, authority remains explicit: the author supplies the accepted business direction; technical choices and actual acceptance need review. The same author acting in several roles is not independent validation. The workflow can organize responsibilities, but it cannot create an outside reviewer by naming an agent role.

### Specify the actor's contribution, not only the final state

The E2 policy changes the meaning of a successful approval action. Under high-risk v2, the first eligible contribution succeeds while the request remains pending. A use case whose only success outcome is request approved would leave this legitimate intermediate result unclear. The behavioral record needs to distinguish recording a valid contribution from completing the overall request.

An original refinement of the sketch can express a common entry condition, the actor's permitted contribution and the resulting state under the bound policy. Alternatives then address requester exclusion, missing current eligibility, an already terminal request and duplicate/conflicting commands under the future contract. This is a content design, not a demand for one particular native decomposition.

Avoid resolving that ambiguity by splitting the same rule into several uncoordinated descriptions. Separate use cases may be appropriate when actors' goals or responsibilities differ. They still need one consistent account of policy and shared invariants. A reader should be able to identify which accepted requirement determines each outcome.

The actor is also more specific than approver. A person can possess that role and remain disqualified for their own request. A person can have contributed validly earlier while a later command must satisfy current eligibility. The effect of revoking a prior contribution remains a separate open contract question; adding an alternative flow must not silently decide it.

### Write an alternate flow with its own observable result

In the proposed approval use case, the primary flow begins with a pending request and an eligible actor. It ends with the state allowed by the bound policy. A useful alternate flow covers an overlapping-role requester. That actor has enough role privileges to reach the ordinary eligibility check and still cannot approve their own request. If the flow only says “authorization fails,” an implementer may exercise it with a missing role and leave the requester exclusion untested.

Write the preconditions and preservation obligation separately. The actor is a current member of the tenant. The request is pending and belongs to that actor. The command reaches decision authorization. The expected result is the contract's denial behavior with the prior state and success history preserved. The exact response and any permitted denial event belong to the selected interface contract.

An alternate flow for a second distinct actor begins in a different state. The request is high-risk v2 and already carries one eligible approval. The second actor must differ from the first and satisfy the same eligibility constraints. This gives the reviewer a path to inspect the threshold without conflating actor identity with request retries. A repeat by the original actor and a replay of the same command can have separate observable results once the replay contract has been settled.

Review the flows against the decisions they own. If a variant requires a different response for foreign-tenant lookups, make the disclosure decision explicit before assigning an expected result. Link common invariants rather than copying them into every variant. A correction can then update the authoritative rule and identify which flows need revised evidence.

<!-- C07-S03 -->
## Persistent specifications as a working record

The core workflow selects construction context through linked requirement rows, a use case, domain information and applicable accepted decisions/conventions. It does not describe every construction task as reading the whole catalog. This makes the completeness of the relevant links consequential. [Construction inputs](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L319-L337)

Suppose the illustrative use case links CS-04 but omits CS-05. An implementer could see the membership obligation while missing the self-approval exception. A well-formatted requirement line would then carry incomplete intent. Review must ask whether all applicable constraints are linked, not only whether listed references resolve.

Persistent artifacts can make that omission inspectable. They also create a maintenance duty: changes must reach the places that depend on them. Repetition of the same rule in several records can produce disagreement unless ownership and reconciliation are clear. Keep a stable requirement's meaning authoritative and use links to connect its applications where the selected convention permits.

AIUP's inspected specification review separates deterministic lint from judgment-based semantic review. The former checks defined structural conditions; the latter raises findings requiring interpretation. The source explicitly separates their blocking authority and keeps the review report distinct from fixing the findings. [Specification-review boundary](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-core/skills/spec-review/SKILL.md#L41-L65)

For the case, three questions should remain separate:

| Question | Example | What it establishes |
|---|---|---|
| Does the reference resolve? | The use case names an existing requirement | Structural linkage |
| Is the linked intent complete and consistent? | The requester exception and tenant boundary apply to this operation | A semantic judgment requiring review |
| Does the application realize it? | An otherwise eligible requester cannot approve a pending item | Behavioral evidence from an actual check |

Passing the first does not settle the other two. A semantic reviewer can also be mistaken, so retain its findings and resolutions rather than transform judgment into certainty. Where a report is advisory, the acceptance owner needs an explicit disposition of material issues.

The persistent record is most useful when a later engineer can recover why the behavior exists and which change is now intended. It is less useful if status labels outpace evidence or if a current-looking artifact quietly contains an old policy. Long-term benefit therefore remains an outcome to investigate, not a consequence of file retention alone.

### Inspect missing links as well as broken ones

A structural check can discover that a named requirement does not exist. A different failure is that an applicable requirement was never named. The latter may leave every visible reference valid. For the decision use case, current membership and requester exclusion both apply; linking only one can produce a clean-looking but incomplete construction input.

An original trace review therefore begins in two directions. From a requirement, identify every behavior that should consume it. From a use case, identify the constraints that apply even when the current links omit them. Compare those sets with the selected native record. The review is about semantic coverage, not a count of references.

Then follow a concrete alternative into its check. The requester-exclusion alternative needs an otherwise eligible requester and a pending request. A label attached to an assertion that only exercises terminal state would not establish the intended behavior. The implementation location, test fixture and observation must agree about the rule being examined.

This review can produce a useful finding without executing an application: a missing link or contradictory expectation is a documentary defect. It is not yet an observed application failure. Retain the finding, its basis and the affected downstream inputs so later construction does not inherit an already known omission.

### Give semantic findings an explicit disposition

Because structural lint and semantic judgment have different authority, a review report needs a route for consequential advisory findings. An acceptance owner should be able to see whether a finding was accepted, rejected with reasons, deferred outside scope or left unresolved. The existence of a report does not establish that someone acted on it.

For an illustrative contradiction, a use case may describe current same-tenant eligibility while an alternative implies that administrator status bypasses requester exclusion. The correction needs the accepted business rule, not a vote among generated perspectives. If the rule is already clear, reconcile the record; if it is genuinely open, obtain the responsible owner's decision before treating it as executable intent.

Keep review and repair distinct in the evidence trail. A report authored before correction and a revised specification serve different purposes. Preserve enough identity to tell which implementation consumed which version. Otherwise a final clean document can conceal that the original construction input was materially different.

### Maintain a small glossary at a shared business boundary

The approval case uses words that can hide different identities. A requester is an actor in relation to a specific request. An approver role is a privilege held through membership. An approval is a successful contribution to a particular decision history. A repeated command can refer to the same contribution. Writing these meanings once gives the use-case owner and implementer a common starting point.

The distinction becomes concrete in a fixture. Mira can hold an approver role and still be the requester excluded from this request. Leon can send the same command twice and still contribute one distinct approval. Priya can provide the second eligible contribution. The glossary should support those examples and identify where each meaning is applied. It need not describe every class or field.

Review terminology when an implementation introduces a new name. If a field called approvalCount actually stores successful commands, an engineer should inspect whether the name reflects the business concept and whether replay can inflate it. The glossary cannot repair the implementation, but it can make the mismatch visible. A reviewed rename can preserve behavior while making a later defect easier to recognize.

A shared term can also be too broad. A status called complete could refer to the use-case document, construction work, test coverage or the business request. Qualify the record so a contributor can tell which lifecycle it belongs to. A reader should be able to follow an implementation status without mistaking it for a release decision or a terminal request state.

Keep glossary changes under the specified ownership policy. If an agent discovers a contradiction, it can report the competing uses and affected records. The owner can then decide whether the rule needs clarification or the code needs reconciliation. The resulting change should identify downstream examples that need fresh review.

<!-- C07-S04 -->
## Implementation and traceable tests

The construction path should connect the reviewed use case to a bounded implementation and appropriate checks. For the inspected Node adapter, the test skill describes a unit tier with stubbed repositories and a real-application HTTP tier using Supertest and PostgreSQL in Testcontainers. This is a prescribed testing arrangement, not a suite executed here. [Node test tiers](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/skills/nest-test/SKILL.md#L22-L32)

Those tiers address different uncertainties. A pure policy check can inspect the distinct-approver rule under selected inputs. An application/database check can inspect whether actual persistence and request handling realize that rule. Neither should be described as proving the whole service secure. Their fixtures and assertions determine the observation's scope.

The workflow explicitly qualifies coverage automation: the combined Node adapter does not yet ship the equivalent auditor described for certain other adapters. Manual checking is discussed as a route. Preserve this limit when evaluating traceability rather than borrowing another stack's assurance claim. [Coverage-auditor boundary](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L388-L417)

For the common case, a requirement-to-evidence map might identify:

| Requirement | Implementation question | Check required later |
|---|---|---|
| CS-04 | Is current same-tenant eligibility checked at decision time? | Eligible actor succeeds; revoked/foreign actors fail under appropriate fixtures |
| CS-05 | Is requester identity independently considered? | Pending-state overlapping-role negative case and separate positive control |
| CS-08 | Is retry/conflict behavior consistent across state and audit? | Same-key repetition and conflicting reuse under the frozen contract |
| CS-09 | Is the policy preserved under competing decisions? | Controlled concurrency with final state and history inspected |
| CS-10 | Are successful transitions and history durable and tenant-scoped? | Restart and foreign-history access checks |

These are proposed checks. The application, database configuration and independent oracle remain unprepared. Source-native tests can contribute to the evidence packet, but their expected behavior must be checked against the agreed requirement rather than inferred solely from generated code.

The implementation skill's scope also matters. Its instructions separate implementation from test generation and restrict changes to existing tests/documents for that role. This does not mean that the entire method never changes tests. It means the selected workflow assigns that work elsewhere. [Node implementation role boundaries](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/skills/implement/SKILL.md#L47-L79)

At acceptance, distinguish a structural marker, an agent's coverage finding and a human decision supported by actual observations. A rule marker can help locate code; it cannot prove the code's condition is correct. A coverage matrix can expose gaps; it needs inspection of what each covered entry means. Human confirmation can close a workflow state while leaving wider operational claims unresolved.

The transition guidance describes acceptance records with named results and human confirmation before accepted use cases reach Done. This is a documented decision procedure, not a completed round for our example. [Transition and acceptance](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L419-L447)

### State which instruction set governs construction

A reproducible profile needs the core revision, selected adapter, applicable construction instructions and any local substitution. Do not combine a layered-orchestration decision rule with a Node implementation command and assume that the combination is the documented default. Record why each instruction applies and where its authority ends.

For the book's hypothetical Node path, an original profile note would identify the accepted requirements/use case, the stack assumptions, the implementation/testing role split, the chosen review route and outstanding environment checks. A language-family preference cannot fill the database, framework, package or compiler fields. An adapter's availability is a compatibility lead until those dependencies are actually exercised.

Role boundaries become practical when intended behavior changes an existing test expectation. If the implementation role is not allowed to edit that test, the workflow needs an explicit handoff to the responsible testing role. The old expectation should not be preserved merely to avoid a prohibited edit, and the implementation role should not silently exceed its scope. Reconcile the accepted rule through the assigned route.

That handoff has a cost and an observable outcome. Retain the question, relevant requirement revision, test change and actual command/result when they exist. A future evaluation should count compensating manual work rather than attribute it to an automatic adapter capability.

### Match each test tier to its uncertainty

A repository-stubbed policy test can vary eligibility and contribution inputs cheaply, but the stub does not establish real query scoping or transaction behavior. A real-application HTTP/database tier can inspect those integration boundaries when it is actually configured with meaningful fixtures. Its existence in a skill description is not an executed observation.

For CS-03, establish a known foreign record and a permitted positive control at the real boundary being checked. For CS-10, observe the required state/history relationship across the declared persistence/restart procedure. For CS-09, define legal competing histories before choosing the concurrency exercise. Those duties do not become satisfied merely because tests are categorized as integration tests.

The Node coverage-auditor gap makes the selected review route especially important. A manual review can be legitimate when its owner, scope, inputs and decisions are explicit. It still requires inspection of assertions and omissions. Counting requirement markers or rows marked covered cannot establish the semantic relation between behavior and evidence.

### Inspect the path between a use case and an observation

Take the use case in which an eligible actor approves a high-risk v2 request for the second time in the sequence. The use case's success condition needs to identify a second distinct actor, a terminal state and durable history. A structural check can establish that the use case identifier appears in construction and test records. A reviewer still needs to read the fixture and determine whether it supplies two different actors and exercises the expected transition.

In the Node teaching arrangement, map that observation through the selected application layers. A policy-function assertion may confirm that two different actors are counted. A service-level probe can check that an authenticated command reaches that policy with the correct request version. A persistence observation can check that the final state and history agree. Label the evidence by boundary so one passing assertion cannot be mistaken for coverage across all three.

If the implementation reveals an absent contract decision, record it at the behavior level before reconciling the lower-level artifacts. For example, two calls could present the same key with different payloads. The use-case owner needs to settle the expected result before a construction path can produce meaningful acceptance evidence for it. A developer's local workaround is useful as a proposal and should be reviewed in that role.

<!-- C07-S05 -->
## Policy change and existing systems

The inspected change guidance begins with updated intent/requirements, reconciliation of affected specifications and downstream implementation/tests. Its reverse-engineering guidance treats recovered artifacts as a proposed baseline whose gaps and contradictions need resolution. [Change and existing-code guidance](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L475-L494)

The word proposed matters. Existing code can reveal what the service does, but the desired behavior may differ. If reverse engineering documents self-approval as allowed because that is the current implementation, the accepted case rule still requires a correction. A recovered specification cannot acquire normative authority simply by describing code accurately.

For E2, the revised intent must include both the new high-risk threshold and the preserved creation-time policy for v1 requests. Review the effects on eligibility, distinct counting, pending/terminal state and audit. Some requirements stay unchanged but remain relevant to every modified use case.

An original change-impact note could separate:

- Changed behavior: new high-risk v2 requests need two distinct eligible approvals.
- Preserved behavior: v1 requests retain their bound policy; standard-risk v2 still needs one.
- Preserved invariants: tenant locality, no self-approval, retry consistency and durable history.
- Technical uncertainty: representation, migration and concurrency mechanism, to be settled under the common stack/contract.

The selected Node implementation instructions favor reconciling existing functionality in place, preserving unrelated behavior and adding migrations rather than rewriting already-applied ones. This is a source-specific change discipline. We have not exercised a migration or established that the application's schema realizes the intended policy binding. [In-place reconciliation](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/skills/implement/SKILL.md#L47-L68)

For a fair episode, every method starts from the same prepared baseline, not its own potentially different E1 output. Preserve the native AIUP artifact trail while retaining common business obligations and external checks. If the adapter needs a different stack or a custom adaptation, report that intervention and its preparation effort.

The smaller E3 repair should also preserve proportionality. A tenant query correction may require a narrow implementation change and meaningful regression evidence, while specifications clarify the intended boundary. The inspected set does not establish the minimum artifact cost for every tiny AIUP task. We leave overhead unmeasured rather than infer it from the number of available documents.

### Reconcile the change without rewriting its history

A proposed change-impact review starts with the accepted delta: new high-risk v2 requests need two distinct eligible contributions. It then names preserved cases, affected use cases, shared rules and technical decisions still open. An unchanged rule such as no self-approval can remain relevant even when its requirement text does not need revision.

Follow that delta through construction inputs. A use case that still treats every successful contribution as terminal completion needs reconciliation. A data representation that cannot retain creation-time policy needs a technical decision. A test expecting retroactive v2 thresholds needs correction to the accepted rule through the responsible testing path. These are distinct effects of the same change.

Preserve the prior accepted specification and the new revision in the evidence history. A current catalog should explain intended current work; the earlier version explains what a prior implementation or verdict was assessed against. Replacing the old file's meaning without retaining identity would make later maintenance claims difficult to examine.

For recovered existing systems, use a three-column investigation note: observed behavior, accepted intended behavior and reconciliation required. If observed code permits self-approval, record that fact without turning it into an accepted product rule. If a recovered use case is incomplete, mark the baseline proposed rather than declaring requirements complete because a reverse-engineering step ended.

### Preserve the meaning of a use case across a change in policy

An owner can express the E2 policy with one new variant for high-risk v2 and a preservation clause for requests that predate the change. This avoids duplicating the whole approval use case while showing which path now remains pending after the first eligible action. The use case still needs common invariants for tenant scope, actor eligibility and the relationship between the committed decision and its history.

A reconciliation review can look for two kinds of omission. The implementation may have added the new variant while forgetting the preserved path. The tests may cover the preserved path only by seeding records directly, leaving version selection at creation unchecked. Ask the contributor to show how each observation starts, where the stored version comes from, and which actor makes each decision. A use case with a readable flow gives the reviewer a stable basis for those questions.

Existing implementation evidence can reveal further variations. If older data lacks an explicit version field, the use case cannot settle the migration by assuming all rows were created the same way. The architecture and product owners should agree which evidence classifies old records and what happens when the classification is unclear. Carry that decision into construction and acceptance. Record any unresolved population separately so a check on clean synthetic rows cannot stand for it.

### Review an obsolete flow before removing it

A product change can retire a use case while records created under that behavior remain in the system. Before marking the flow obsolete, identify which existing records still require its interpretation and whether any client or operational procedure depends on it. A new use case can govern future work while a historical rule remains necessary for maintenance.

For the approval case, retiring v1 for new creation does not decide how an old pending request is resolved. Preserve the relevant behavior and acceptance example until its population has an agreed disposition. The requirement record should let a reviewer see that distinction without relying on an obsolete implementation plan.

If the team later removes the compatibility path, give that change a separate decision and evidence. Identify the population inspected, the condition that makes removal acceptable and the owner who accepted it. A structural status update can then reflect the reviewed lifecycle decision rather than become the only evidence for it.

<!-- C07-S06 -->
## The same increment, original artifacts

Our teaching use case concerns a business decision, not a sample application borrowed from another publication. The neutral CS requirements stay external to native notation. A future AIUP record would map its own stable identifiers to those requirements so readers can inspect coverage without confusing the book's numbering with generated framework output.

The resulting trail would be intelligible in both directions. From CS-05, find the relevant use case, the requester-exclusion rule, implementing location and acceptance observation. From an implementation change, find the rule or technical decision that justifies it. If either direction ends at a generic statement such as “authorization handled,” the record needs more specific inspection.

Do not reproduce a full prompt collection to show this trail. The important content is the business decision and its consequence, not every instruction used to create a file. Likewise, a complete framework tutorial would distract from the comparison unless a particular setup choice changes the intervention.

For the base increment, the original artifact set we would expect to inspect includes a bounded requirement/use-case record, applicable domain/architecture decisions, open questions, implementation rationale and test/acceptance evidence. That is a functional inventory, not a claim that a workflow emitted those files here.

The case also keeps application architecture separate from process fit. NestJS/Next.js may be a plausible candidate for the inspected adapter, but plausibility is not a shared-stack decision. If the book chose it solely because one adapter requires it, that choice and any resulting advantages or constraints would need disclosure in the comparison design.

Human inspection should focus on whether persistent records carry the correct behavior through change. A use case that omits creation-time policy binding can be polished, traceable and wrong for E2. An implementation that matches it would still fail the shared contract. This is why equal external obligations matter alongside native artifacts.

### Walk one obligation in both directions

Begin an original paper exercise with CS-05. Locate its native requirement equivalent, the decision use case, the requester-exclusion alternative and the construction input that must carry it. Identify the proposed implementation boundary and the independently expected fixture. Leave actual code/test/result locators empty until the application exists.

Now reverse the exercise. Start from a proposed assertion denying an overlapping-role requester. Ask which accepted rule makes denial correct, whether the fixture isolates that rule and which use case requires the alternative. If the assertion instead targets a terminal request, the reverse walk exposes a mismatch even when the forward references look complete.

Repeat for CS-13, where creation-time binding crosses creation, decision and historical interpretation. One local success assertion cannot cover that whole chain. Identify the places that must retain the policy's meaning and the later observations needed to assess them.

The resulting artifact is a review map with specific gaps, not a simulated coverage result. Its usefulness lies in making a missing relation challengeable. Whether an executed AIUP arrangement produces and maintains a better map than another method remains a separate empirical question.

### Reconcile a structural pass with a semantic finding

Suppose the requirement, use case, construction record and tests all carry the right identifiers. The structural report is green. A reader of the actual fixture notices that the purported second approver is represented by the same actor with another role. The test expects approval after two commands. Its trace links are intact, yet the linked example contradicts the intended behavior.

Record the defect at the level where it occurs. The specification is clear about distinct actors in this example. The test expectation needs repair, and the implementation must be inspected to see whether it also counts roles or commands. Use separate fixtures for the repeated actor and the permitted second actor. The review can then distinguish a test problem from a behavior problem. Retain the structural pass with its own scope and record the semantic finding and disposition beside it.

If the use case was ambiguous, the owner would first decide what counts as distinct. A role-based implementation might have been a reasonable interpretation of an incomplete record. In that situation, preserve the observation, revise the owning specification and reconcile the construction and test records from that decision. The disposition should show whether the new work corrects a defect against existing intent or implements a newly settled rule.

<!-- C07-S07 -->
## Limits and conditional fit

The inspected AIUP design provides durable requirements/use-case relationships, specified construction inputs, review conventions and an explicit downstream change path. These mechanisms support concrete questions about ownership and traceability. They do not establish automatic synchronization, reduced maintenance cost or superior acceptance quality.

Our conditional assessment is to investigate this arrangement where a team wants owned behavioral specifications to remain a working product record and can assign the maintenance/review duties they require. Verify that the selected adapter fits the application constraints and that its actual coverage route meets the project's acceptance needs.

The Node auditor qualification, role-specific edit boundaries and stack assumptions are material. Keep them in any summary of fit. Core portability in design does not prove that every construction plugin is interchangeable, and a different plugin's completed check does not certify this one.

No controlled AIUP-versus-peer advantage is established here. Tiny-task overhead, real human-team coordination and long-term drift outcomes remain unassessed. Transition documentation is useful to inspect, but it is not evidence of production operation, recovery or regulatory compliance.

Independent source review and full-book originality/permissions review also remain open. The chapter's independently composed artifacts and shared synthetic case establish a distinct working route; they do not replace external scrutiny. We will carry the same limits into the SDD and comparison chapters.

The practical question is whether maintaining this behavioral record helps the team make and check its next change under real constraints. The method's design tells us where to look. Actual observations must establish what happened.
