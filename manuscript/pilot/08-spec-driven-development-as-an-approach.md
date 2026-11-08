# 8. Spec-Driven Development as an Approach

> Author manuscript · completed 2026-11-05 · C08 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C08-S01 -->
## From the primer to a lifecycle policy

A specification is most informative when something changes. Before implementation, it can make intent explicit. During review, it can identify the behavior the code owes its users. During maintenance, it can preserve an earlier decision or reveal a conflict. Those roles require a policy for ownership, retention and reconciliation.

Chapter 3 introduced the vocabulary. The four deep dives then showed why the label spec-driven is insufficient. A maintained use case, a phase plan, an epic contract and an original request record can all guide development. They differ in the decisions they own and the period for which they remain authoritative.

Consider our E2 requirement: new high-risk v2 requests need two distinct eligible approvals, while existing requests keep their creation-time policy. A document can state that rule clearly on the day it is written. The harder question is what happens when the implementation changes, a reviewer notices an omission or a later request proposes retroactive treatment.

A lifecycle policy needs answers to five questions: which artifact owns the behavior, who may change it, which dependent records must be reconciled, how code/test disagreement is resolved and what evidence justifies acceptance. Without those answers, calling a document the source of truth leaves the maintenance procedure unspecified.

We can compare the policy at several scopes. A small repair may need one current issue and a regression expectation. A long-lived business rule may merit a maintained specification with stable references. A generated subsystem may place stricter limits on direct implementation edits. The appropriate arrangement depends on the work and the team, not document length alone.

This is why Spec-Driven Development (SDD) is cross-cutting in the book. It describes choices about how specifications participate in development. Those choices can appear within several frameworks and through different tools. The presence of a specification does not establish a distinct fifth intervention comparable to four complete process profiles.

### Define what it means for a specification to stay current

A current specification identifies the accepted behavior for the relevant population and the condition under which it applies. A recently edited document can still describe a future policy while the deployed service handles earlier requests under another version. Put the applicability boundary in the rule and its examples.

A reconciliation record should say which implementation revision and policy cohort were reviewed. If a known gap remains, identify it alongside the intended rule and name the owner of its disposition. This lets a maintainer find accepted intent without confusing it with an observation that every path already follows it.

<!-- C08-S02 -->
## Three attributed patterns, not a ladder

Birgitta Böckeler's 2025 analysis supplies the terms spec-first, spec-anchored and spec-as-source. They distinguish initial specification use, retention through later work and an arrangement in which humans edit the specification rather than implementation. We attribute the vocabulary and use it to ask lifecycle questions, not award quality levels. [Original analysis](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

The order question is the smallest: was intended behavior described before implementation? It leaves retention and maintenance unresolved. A team can use a useful temporary change specification without committing to maintaining that exact artifact forever. Conversely, retaining the file does not establish that later work consults or updates it.

The maintenance question asks whether the specification remains a working reference after the initial feature. Who owns an update? Does a changed requirement propagate into code and checks? How is an outdated record detected? A spec-anchored claim becomes meaningful through those policies and their actual use.

The editing-boundary question is stricter. If implementation is regenerated from specification changes, a manual code patch may be overwritten or may break the declared process. The team needs a rule for emergency changes, generated versus hand-maintained regions, and reconciliation afterward. These are policy questions to investigate in the selected arrangement; the label does not answer every exception.

Do not treat the strictest editing boundary as the best outcome by definition. It may fit a well-bounded generation domain and impose costs elsewhere. A manually maintained implementation can still have explicit intent, strong acceptance evidence and a useful long-lived specification. Suitability requires the scenario and observations.

Nor should the labels be assigned to an entire framework from one file. BMAD's epic specification ownership and its existing-code context policy operate at different scopes. A GSD phase record may persist as workflow history without becoming the permanent product specification. Inspect the actual artifact and change rule before making a category claim.

### Set a policy for each kind of record

Consider a team adopting a specification practice halfway through the approval service's life. It already has issue descriptions, a product rule about tenant ownership, a database migration convention and a directory of generated plans. Applying one edit policy to every file would make the workflow awkward. The product rule needs a decision owner. The migration convention needs a maintainer and a way to test changes. The generated plan needs the identity of its inputs and a clear point at which it can be archived.

The team can choose a durable specification for decision behavior and keep plans local to each change. When E2 arrives, the decision owner updates the rule for new high-risk requests and records the scope of the v1 exception. The developer revises the plan and brings the repository into alignment. The reviewer asks for an observation on both versions. After release, the accepted behavior and evidence stay available, while the task plan can be archived with the revision it describes.

A different team might generate a reviewable contract from a deliberately owned source. In that arrangement, editing the generated file during a repair can hide the change from the next regeneration. The team should identify where to correct the source, how to preview downstream changes and how to handle a release whose current implementation predates the new contract. These choices concern an individual artifact and its consumers. The same team might still edit its test fixtures directly and archive short-lived planning notes.

| Record | Proposed authority | Evidence that an update took effect |
|---|---|---|
| Behavior specification | Product decision owner | Reviewed rule and acceptance examples for affected versions |
| Generated interface description | Maintained upstream input | Reproduction using the declared input and comparison with the reviewed output |
| Implementation plan | Engineer responsible for the change | Work references the accepted decision and identifies unresolved assumptions |
| Acceptance record | Reviewer responsible for the observation | Fixture, revision and actual output can be retrieved |

Put this policy where contributors encounter the record. During a correction, the engineer should be able to tell where to make the change without asking everyone who ever edited the file. A record that no contributor can locate or interpret has little practical authority, regardless of how carefully it was written.

### Choose which records should be regenerated

A team can use generated plans without making its accepted behavioral rules disposable. Identify the input that owns intent and the records derived for a particular task. When intent changes, regenerate the task-specific material from the revised input and inspect what changed. Retain the old plan with the revision it described.

A different artifact may deserve direct maintenance. A brief decision rationale that explains a preserved policy can remain useful across many tasks. Replacing it on every generation risks losing the reason a later maintainer needs. The team can retain that rationale and reference it from new plans.

Review the policy using a concrete correction. Ask where an engineer should edit an ambiguous rule, which downstream records must change and how a reviewer checks that they did. If those answers are clear, the policy has a practical maintenance path. If contributors routinely edit a generated output because they cannot find the owned input, improve the entry point before adding more generation.

<!-- C08-S03 -->
## Specifications, context and executable contracts

Specifications and context overlap, but their roles differ. A glossary provides meaning. A repository map helps navigation. A business rule states required behavior. A phase summary records work. An agent may need all of them; only some define the expectation against which the change is accepted.

For the approval service, “Mira created request R” is fixture context. “The requester may not approve that request” is a behavioral constraint. “The last session changed the decision reader” is workflow history. Mixing these in one prompt does not remove the need to identify which statements are authoritative and current.

An executable contract adds a defined mechanical path. A schema validator can check properties it encodes. A test can exercise selected behavior under a fixture. A reference model can provide a decision expectation for a defined input space. None automatically captures every business requirement, and a natural-language instruction interpreted by a model is not executable merely because code follows it.

Use a separation record when the artifact's role is ambiguous:

| Content | Proposed authority | Appropriate check |
|---|---|---|
| Policy binding at request creation | Accepted business requirement | Reviewed expectation and later transition/regression observations |
| HTTP error representation | Frozen interface contract, once chosen | Contract checks for the selected interface |
| Native workflow status | Process record | Consistency with actual work/evidence and known gaps |
| Test fixture identities | Exercise definition | Positive/negative controls establish that the intended boundary is exercised |
| Agent's completion summary | Report of work | Inspect supporting changes and observations before accepting it |

The record can be compact. Its purpose is to prevent an implementation or report from quietly becoming the authority for a missing requirement. It also helps reviewers identify where a correction belongs.

Generated code need not be identical across repeated runs for a process to be auditable. Retain the inputs, source/configuration, outputs and observations needed to compare behavior. If exact regeneration is part of a claim, test that claim under stated conditions rather than infer determinism from the phrase source of truth.

### Show how one sentence becomes an observable contract

Start with “high-risk requests require two approvals.” That sentence leaves open who counts, when the new rule applies and what a client can see after the first action. Add a short sequence: create a high-risk request under v2, accept an eligible approval from Leon, and leave the request pending. Submit another action from Leon and verify that the count does not increase. Accept an eligible approval from Priya and check the approved state and durable history. Keep the response to a repeat unspecified until the contract distinguishes a replay from a different action.

Add a preservation example before describing implementation. Create an equivalent request under v1 and leave it pending while v2 becomes active. An eligible approval still resolves it under v1. This example makes the scope of the specification clearer than the threshold sentence alone. It also shows why a contract author should name the creation-time assignment separately from the rule that resolves a decision.

The examples can be used at several levels. A reviewer can inspect the behavior without knowing an endpoint. A test designer can turn it into a fixture after interface and observation rules are agreed. An implementation agent can use it alongside code locations and local conventions. Give each consumer the relevant context and preserve a link back to the owned decision. Copying the full specification into every task introduces additional places to reconcile when a single rule changes.

### Distinguish a behavioral rule from a convenient test example

A specification can include a concrete example that is narrower than the rule it explains. “Leon and Priya approve this high-risk request” illustrates two distinct eligible actors. It does not make those two names part of the product contract. An implementation that recognizes only the fixture identities can pass the example while violating the general rule.

Write the general condition near the example. Identify the relationship among actor, membership, requester, tenant, policy and current state. Then vary one relationship in a second example. A different eligible actor should be able to make the same kind of contribution. The requester should remain excluded when their role set changes. A reviewer can inspect whether the implementation expresses the relationship or merely recognizes the demonstration.

The same problem appears in a generated interface. An example response might contain a single approval without explaining whether the operation has finalized the request. Give the response a defined meaning and identify the business state a client can infer. If the contract permits a successful contribution while the request remains pending, show both a partial and a terminal outcome.

A test derived from an example should identify the rule it addresses. This helps a reviewer decide which fixture variations are material. Varying an irrelevant display name may add little evidence. Varying the requester relationship or bound policy can expose a different decision branch. The specification owner and test reviewer can use the same short rule to explain why one variation belongs in acceptance.

When a fixture changes during maintenance, revisit the observation rather than simply updating expected output. If a previously distinct actor becomes the requester in the new fixture, the expected result changes for a reason. Record that reason with the requirement so future contributors can distinguish a deliberate fixture correction from a test weakened to match code.

<!-- C08-S04 -->
## Who resolves disagreement

Disagreement is useful evidence. It means two records or observations cannot both be accepted without qualification. The next step is to identify the authoritative decision and the type of conflict, rather than automatically editing the most convenient side.

If a specification forbids self-approval but the implementation allows it, the current case points toward an implementation defect. If the test expects administrators to approve their own requests, its expectation contradicts CS-05. If the product owner now wants that exception, the accepted requirement must be changed explicitly and the study's task identity reconsidered.

An original reconciliation map can make the duties visible:

| Conflict | First question | Owner/action |
|---|---|---|
| Requirement versus use case | Is behavior missing, contradictory or intentionally changed? | Product decision owner resolves intent; update dependent records |
| Specification versus code | Is the specification still the agreed behavior? | Implementing engineer proposes correction; policy changes require authority |
| Code versus test | Does the assertion express the agreed expectation and fixture? | Acceptance/test reviewer checks both sides |
| Two specifications | Which scope owns the rule, and why were copies allowed to diverge? | Artifact owners reconcile and clarify maintenance policy |
| Current record versus old verdict | Which inputs changed after review? | Revalidate affected evidence rather than reuse the old status |

BMAD's selected source designates `bmad-spec` as writer of the named specification and preserves capability IDs through updates. AIUP describes intent/specification changes before downstream reconciliation. Both supply a maintenance route; neither source alone demonstrates successful synchronization in our case. [BMAD ownership](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/define-requirements-and-a-specification.md#L97-L124), [AIUP change route](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L475-L494)

A semantic review can identify a possible conflict without having authority to settle it. Retain that distinction in automation. A tool that changes a requirement to make a check pass may erase precisely the disagreement a reviewer needed to inspect.

For urgent repairs, preserve a small decision record even when the implementation must be corrected first under an authorized emergency procedure. State the temporary deviation and the reconciliation duty. This is an editorial process design, not a claim that every selected framework supplies the same emergency path.

### Resolve a conflict in the order that protects existing users

Suppose the specification says v1 behavior is preserved, the implementation reads the latest policy on every approval and the generated test expects the current implementation. Begin with the accepted decision and an observation against a pre-existing request. If the fixture confirms the contradiction, record the behavior people may already have encountered before editing anything. The owner may need a decision about previously processed records and a separate repair for future actions.

The repair must reach every record whose role changed. Fix the resolver, revise the test that encoded the wrong expectation, and annotate the old evidence with the revision it describes. A new test should observe the state change through the public entry path used by the affected workflow. A developer can additionally retain a direct resolver test for fault localization. The decision record can then point to both and explain what each covers.

When authority is genuinely ambiguous, write down the smallest decision that unlocks the next step. For example, decide whether newly created requests retain the policy even if a reviewer changes a tenant setting later the same day. Defer unrelated policy changes to their own decisions. This keeps the reconciliation bounded and gives an acceptance reviewer an explicit expected result.

### Review a conflict without changing both sides at once

Choose a synthetic disagreement between a maintained specification and an implementation. Write down the accepted rule and the observed behavior before editing either. Ask the owner whether the observation reveals a defect or a desired change that has not yet been approved. Record that disposition with the affected population and revision.

If it is a defect, repair the implementation and the checks that repeated its assumption. If the owner chooses a changed rule, update the specification and reconcile its consumers from the new decision. In either case, retain the original observation so a reviewer can understand why the work began.

Changing the rule and expected output together can be legitimate after that decision. Without the recorded disposition, the same edit can conceal a regression. The review should be able to follow the direction of authority through the correction.

<!-- C08-S05 -->
## One policy change across native artifacts

E2 provides a common test of specification policy. The business change is fixed; each method's native artifacts remain different. The following is a documentary trace design, not a record of four runs:

| Selected source | Native record to inspect | Question for the E2 change |
|---|---|---|
| BMAD stable source | Maintained specification, optional story breakdown and implementation record | Does creation-time binding survive the skill-mediated update and reach acceptance? |
| GSD Core source | Phase decisions, plans, summaries and refreshed verification | Do workers receive both the new threshold and preserved v1 behavior? |
| AWS workflow source | Intent/state, selected stage/unit artifacts and boundary evidence | Does the configured route preserve the policy decision and disclose any skipped duty? |
| AIUP core/Node path | Requirements, affected use cases and downstream reconciliation | Do stable references preserve unchanged constraints and identify the changed behavior? |

The underlying source mechanisms are described in the deep dives: BMAD's linked specification path, Core's phase records, AWS's retained workflow/audit records and AIUP's specification-led changes. [BMAD](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/choose-a-planning-path.md#L118-L137), [Core](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L25-L59), [AWS](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/14-artifacts-reference.md#L25-L54), [AIUP](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L475-L494)

Use the same semantic probes for each. Where is v1 preservation stated? Where is distinct-actor counting stated? Which record changes when a previous interpretation is wrong? Which observations would detect a missed update? The answer may require several linked artifacts, but their number is not the outcome.

Stable identifiers help locate continuity; they do not guarantee unchanged meaning. An identifier retained while its rule silently becomes retroactive can make the trace look continuous while changing the task. Inspect text and behavior as well as reference stability.

The acceptance examples remain common: one high-risk v2 approval leaves pending, a second distinct approval completes, replay does not advance the count, and v1 retains its threshold. No method's generated suite replaces these obligations. A future exercise must retain actual expectations, outputs and exceptions.

### Decide which artifact should change during an urgent repair

Imagine an operator discovers that a search result exposes a request from another tenant. A temporary mitigation disables search while the team prepares a repair. The intended tenant rule was already recorded. The mitigation belongs in the operational record with an owner and an expiry condition. The behavioral specification can continue to describe the intended protection, while a known gap records where the current software fails to implement it.

Now suppose the repair review exposes an unresolved behavior: the contract says nothing about whether a result count can reveal matching foreign requests. Resolve that question in the owned specification before writing the corresponding assertion. Keep the prior observation and distinguish it from the new decision. Otherwise a future reader could infer that the specification had always forbidden the exact behavior exposed by the report.

A short reconciliation checklist can name the changed rule, the dependent plan or use case, the relevant implementation and the refreshed observation. The checklist is finished when a reviewer can follow each relationship. The file names and record format may differ across the four arrangements. The SDD question stays focused on which artifact represents intent and how the team restores consistency after a change.

<!-- C08-S06 -->
## Costs, drift and useful limits

Retained specifications require maintenance. The cost includes reading, reviewing, resolving contradictions, keeping references useful and retiring stale material. The possible benefit is a more recoverable decision record. Both sides need observation under an actual project lifetime; file presence establishes neither.

BMAD's existing-code guidance prioritizes current code and keeps historical greenfield context away from ordinary small changes. That qualifies a blanket claim that retaining and loading every planning document is always useful. It is source advice, not a measured benefit of archiving. [Existing-code context policy](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/existing-codebases/start-in-an-existing-codebase.md#L8-L79)

A useful retention decision distinguishes current intent from historical explanation. The original reason for a policy can remain available without being loaded into every small change. A superseded requirement should not compete silently with the current one. The authoritative record needs an owner and a visible supersession relationship.

Drift is also broader than code/spec disagreement. A test can lag behind both. A generated user guide can describe an old flow. A context file can preserve a discarded technical decision. Choose inspection and reconciliation by dependency, rather than assuming one updated document repairs every downstream artifact.

For a tiny display repair, a maintained domain specification may not need a change at all. Check whether the accepted behavior or contract changed before creating new product documentation. For a policy change, that same shortcut could omit the principal business decision. Proportionate SDD therefore depends on what the artifact owns.

No measured drift-prevention or maintenance advantage is reported here. The case design offers questions and controlled boundaries; it has no longitudinal evidence. A useful future evaluation would inspect several changes, reviewer disagreements and the effort needed to keep the selected record current.

### Put a maintenance cost on the adoption decision

Try the practice on one change that has a stable policy owner and a concrete preservation constraint. Record where reviewers found the rule, what had to be updated, which contradictions were detected and how much manual reconciliation the change required. The team can inspect these records after the next change to see which artifacts were actually reused. A field report should give the team, change and circumstances before drawing a lesson from the exercise.

A small documentation-only correction may need just the existing text and an inspection of the rendered result. If it affects no behavior or durable contract, creating a new behavioral specification adds an artifact with no future decision to own. For a policy change spanning creation, migration and audit, a short maintained rule may repay its upkeep by making the dependencies visible. The team can use the same decision criteria for both changes and choose a different amount of ceremony.

Retire a redundant artifact deliberately. Identify readers and downstream links, move any unique decisions into the surviving record, and leave an archive reference if someone will need historical evidence. Otherwise a stale copy can regain apparent authority the next time an agent searches the repository. An archive should say which revision or decision superseded it and where ongoing edits belong.

### Set a policy for a derived contract during migration

Consider a team that keeps a human-owned behavioral rule and derives an interface description from a maintained schema. The change to v2 adds a pending outcome after the first eligible approval. Existing clients can already display a pending state, but one downstream integration assumes a successful approval response always signals completion. The behavioral spec, generated description and integration assumptions now need to be reviewed together.

Start by identifying which consumers need a decision. The product owner can define what the first successful action means. The interface owner can decide how that outcome is represented and how older clients learn about it. The integration owner can identify the behavior that depends on the older assumption. Once these decisions are recorded, regenerate derived material from its owned input, compare the result with the proposed contract and check the affected integration. If the generated artifact conceals the meaning of the transition, add a reviewed example to the source that owns it.

There is a period in which old and new software may coexist. During that period, a contract can identify when the new behavior becomes active and what a client should do with a request created under an older policy. A repair to the generated text alone would leave the next generation or rollout ambiguous. A repair to the owned input plus a versioned observation gives the team a reproducible basis for the next change.

The team can choose a limited exception in an incident. If a client needs an urgent compatibility patch, record the operational scope and the date or event that ends the exception. Keep the canonical behavior and compatibility promise distinguishable. Otherwise a temporary accommodation can become the rule an agent discovers and repeats in an unrelated change.

<!-- C08-S07 -->
## Apply the lens without creating a fifth arm

Apply SDD questions inside each selected framework profile. Identify the behavioral record, its owner, its lifespan, its edit policy, its conflict procedure and its acceptance relationship. Leave the classification unresolved where the inspected scope does not establish an answer.

The experimental subject remains a configured framework applied to the common work. Adding a fifth label called SDD without a concrete workflow would create an unequal comparison unit. If a later study defines a distinct specification workflow, that would require its own scope and evidence design; it is outside this book's four-arm plan.

Chapter 9 now has a more precise comparison question: which source-specific mechanisms preserve intent and support checking through change, under which dependencies and limits? Chapter 10 can treat specification policy as a scenario constraint. Chapter 11 keeps the full case trail separate from these analytical questions.

The durable lesson is a procedure, not a badge. Name what the specification governs, make its maintenance obligations explicit and inspect the evidence when a change challenges it. That remains useful whether the team keeps one compact issue or a larger network of behavioral artifacts.

### Trace what happens when two teams own different records

Imagine that the service team owns the request policy and a separate client team owns the interaction. The accepted policy adds an intermediate pending outcome. The service team updates its behavior specification. The client team has a separate interaction specification that still assumes a successful approval takes a request out of the queue. Each specification has a legitimate owner. The conflict appears at the interface between them.

Write a small compatibility agreement for that interface. Name the response conditions the service promises, the meanings the client may infer, and when the changed behavior becomes active. Give the agreement one owner or define the joint decision it requires. A shared example can show one eligible approval on a high-risk request, the state the service reports, and the next action the client offers. The same example can be reviewed by both teams without exposing either team's internal design.

When someone proposes a change, inspect which agreement it crosses. A client wording change may leave the service obligation alone. Changing whether an intermediate approval returns the same success representation may need a joint decision. If one side releases independently, identify which combinations of old and new behavior can coexist and which require a coordinated rollout. The design can record a temporary compatibility window and the condition that ends it.

This exercise makes specification authority visible without introducing a new methodology category. The four native arrangements can use different records for these decisions. The inspection follows the same contract, its owners and its consumers. That gives a team a way to judge whether its existing practices are sufficient before creating another specification.
