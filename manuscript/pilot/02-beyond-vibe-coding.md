# 2. Beyond Vibe Coding

> Author manuscript · completed 2026-11-05 · C02 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C02-S01 -->
## Define the behavior behind the label

An assistant produces a change. You try it, describe what looks wrong and ask for another version. That conversation can be a productive way to explore an unfamiliar problem. A prototype may reveal that a proposed interaction is confusing, that a requirement is incomplete or that the idea itself is unnecessary. Those are useful discoveries even if the first implementation is discarded.

The difficulty begins when a plausible result becomes an accepted change without a clear account of the decisions and evidence behind it. For this book, **vibe coding** names a working pattern: implementation advances through conversational intent while decisions, constraints and acceptance evidence are not consistently preserved. The definition describes behavior we can inspect. It does not classify a person, an editor or every use of conversation in development.

The relevant boundary is acceptance. What was acceptable as an experiment may need additional work before someone relies on it. A prototype's author might know that all the data are fictional and that a button bypasses several checks. A later maintainer, encountering the same code in a service, may not have that context. The engineering task is to decide what can be carried forward, what must change and which assumptions need a durable record.

Imagine that our vendor-access application has a history view. During exploration, a developer asks for a list that makes the screen easy to inspect. The assistant supplies synthetic events and a convenient route to reach them. The next request is to connect real business records. At that point, tenant scope and visibility are material decisions. The prototype's convenience does not establish the intended access rule.

We can examine this transition without judging whether the first conversation was disciplined enough. Ask what the next person can establish from the repository and the change record. Can they identify the behavior being requested? Can they distinguish a product decision from an implementation convenience? Can they find observations that bear on acceptance? A record that answers these questions may be compact.

Conversational coding and engineering discipline can coexist. A developer can discover a requirement in dialogue, summarize the decision in an issue, implement a constrained change and attach relevant checks. Conversely, an elaborate process can produce many files while leaving the decisive rule unresolved. The book evaluates the connection among intent, work and evidence.

That connection also sets a limit on the title's promise. Moving beyond the working pattern does not mean replacing every conversation with a document. It means making the accepted commitment understandable and reviewable. We will examine whether named frameworks help establish that connection, what they cost and where a smaller arrangement is enough.

<!-- C02-S02 -->
## From intent to an accepted change

Take this illustrative request: “Let a tenant member inspect the decision history for a vendor-access request.” In the common case, history must remain tenant-scoped and successful business transitions must have durable audit records. The request is therefore connected to CS-03 and CS-10 in the [case specification](../../CASE_STUDY_SPEC.md). It does not authorize an application framework, a new persistence design or a production deployment.

Begin by separating what is agreed from what the sentence leaves open. The tenant boundary is part of the accepted case direction. The detailed disclosure policy and interface contract are still unresolved. A missing record and a foreign-tenant identifier need defined treatment before an executable acceptance check can assert the exact response. Choosing that response during implementation would turn an unrecorded assumption into product behavior.

The first useful output is a decision about the work's boundary. Which history is being exposed? Does this increment read existing audit events, or must it also establish the write path? Which successful transitions are included? What does the exercise exclude? Questions about operational log retention or real identity federation belong outside this small increment unless the common scope is explicitly changed.

Repository investigation supplies a different kind of answer. In an established application, the implementing engineer can inspect how identity is established, how requests are located and where audit events are stored. Those observations describe the current implementation. They do not automatically settle the desired visibility rule. If an existing query crosses tenant boundaries, matching it would preserve the wrong behavior for this case.

Next, record the decisions needed before coding proceeds. Some can be resolved from current project guidance; some require the product owner. A useful question includes the evidence already found and the choice that remains. “The current reader accepts a request identifier without tenant scope; should history follow the case's tenant-local rule?” is more actionable than a general invitation to discuss security. In our case, the approved rule supplies the answer; the detailed interface still needs a contract.

Implementation then becomes a bounded attempt to realize that intent. Its record should identify the relevant changes and important deviations. If the assistant discovers that audit events do not survive restart, the scope of a read-only history change may no longer describe the work. That finding calls for a visible decision: repair the persistence behavior, split the work or stop the increment with the dependency unresolved. Quietly expanding the change would make effort and acceptance harder to interpret.

Acceptance needs an observation suited to each obligation. An own-tenant history read addresses useful behavior. A foreign-tenant read addresses the isolation boundary. A restart exercise addresses persistence. These observations establish different things; one cannot stand in for the others. Their fixture conditions, commands and outputs must be recorded when the exercise is actually executed.

A reviewer also needs to know the limits of the evidence. If only the reader has changed, existing audit-write checks may remain relevant, but their results must come from the baseline and environment being reviewed. A result from another revision cannot silently certify this change. If a check was not run, the record should say so and explain what acceptance remains unresolved.

Finally, someone makes the acceptance decision. That person needs the agreed intent, implementation boundary, relevant observations and open issues. “The assistant finished” describes an event in the workflow. Acceptance is a decision about whether the work meets the agreed conditions. The same person may implement and review a tiny change, but the record should make that overlap visible rather than imply an independent assessment.

This sequence can happen within a short issue and a small pull request. Its usefulness depends on the decisions it preserves and the questions its evidence answers. The named framework comes later; first establish the work that any chosen process must support.

<!-- C02-S03 -->
## The smallest useful engineering record

A compact record needs enough information to distinguish an intended result from a plausible approximation. For a small change, five entries are a useful starting point: intent, constraints, change boundary, acceptance basis and disposition. The entries can live together in an issue or review description. They need not become five separate files.

Here is an original teaching example for the history increment. It is a planning record, not an executed run or a frozen interface contract:

| Entry | Proposed content |
|---|---|
| Intent | A member can inspect the permitted decision history of a request in their own tenant |
| Constraints | Preserve tenant isolation and existing request decisions; expose no other tenant's history; retain durable audit obligations |
| Change boundary | Identify the history reader and its authorization/data-access path after repository inspection; do not add provisioning, billing or unrelated interface changes |
| Acceptance basis | Own-tenant positive read, foreign-tenant direct-identifier negative read, and relevant persistence/regression checks under the agreed disclosure contract |
| Disposition | Interface details unresolved; no implementation or acceptance checks executed |

The last row matters. It prevents a well-formed record from looking like completed work. After execution, that row could link to real observations and an acceptance decision. Until then, the document describes obligations. A future report must preserve the difference.

Each entry should carry a decision rather than a generic assurance. “Follow best practices” leaves the reviewer to invent the applicable rules. “History reads use the authenticated tenant boundary, including direct identifiers” identifies behavior to inspect. “All tests pass” omits which tests, on which revision, and what they establish. A link to a particular command/output record is more informative when execution exists.

The acceptance basis should also expose why a check could fail for the wrong reason. A foreign-tenant read cannot establish isolation if the request identifier is absent from every tenant. The fixture needs a real record in tenant A, a permitted A reader and a B reader attempting the corresponding access. The disclosure contract determines the allowed response; the check must still distinguish isolation from an unusable reader.

Apply the same care to self-approval. An already completed request might reject every new decision, masking an implementation that would allow its requester to approve a pending item. The negative example must begin with a pending request and a requester who otherwise has the required role. A separate equivalent fixture establishes that an eligible different person can approve. These are proposed design conditions, not tests we have run.

The change boundary is equally important. An assistant may propose useful cleanup while inspecting the reader. A reviewer needs to decide whether that work belongs in this increment. Deferring it can preserve a clear acceptance question. Including it may be justified if the intended behavior cannot be implemented without it. Record the reason so the diff remains understandable.

Keep the record close to the work that consumes it. If a reviewer must reconstruct the accepted rule from a long chat, a link to the chat is not an adequate handoff by itself. Summarize the consequential decision and cite the supporting discussion where useful. If the rule already lives in a maintained requirement, link it and describe the change rather than create a second version with different wording.

During review, use the record in both directions. From intent, ask where the behavior is realized and observed. From the diff, ask which requirement or necessary supporting change explains each material addition. A modified reader justified by tenant isolation has a different status from an unrelated persistence rewrite. Both might be valid work, but their reasons and acceptance boundaries should be explicit.

A compact record can evolve as facts emerge. Preserve the initial uncertainty and its resolution where they explain a consequential choice. For a routine detail, a short final rationale may be enough. For a scope change that affects acceptance or evaluation, a dated decision and explicit deviation are more useful than silently replacing the old request.

We will use this record as a minimum question set, not a required template for every method. A native story, phase plan or use-case record may carry the same information differently. Chapter 3 establishes how to compare those arrangements without requiring identical documents.

A practical record can also name its stopping point. If investigation depends on an unresolved disclosure rule, record that dependency and the owner who can resolve it. The next contributor can continue the authorized investigation while keeping the dependent implementation decision open.

<!-- C02-S04 -->
## When ceremony costs more than it helps

Now reduce the problem. Assume an existing, reviewed interface has a navigation link labeled “View history.” A small copy change asks for “View decision history.” The destination, visibility policy and underlying query must remain unchanged. This is a hypothetical interface repair; the book's application and optional UI have not been built.

The intent is clear under those assumptions. The implementing engineer should first confirm that the change is confined to presentation and identify any related accessible name or interaction expectation. If inspection reveals that the link also changes a route or permission condition, the initial description is incomplete and needs revision.

For the bounded copy change, a short issue, constrained diff and relevant navigation check could carry the necessary record. A new product vision, domain model and architecture review would need a concrete reason. Requiring them merely because a framework can generate them would add activities without identifying another decision to make.

BMAD's inspected guidance explicitly allows trivial edits to bypass its process, while offering a bounded Build path for other small changes. That is documentary evidence that at least this source profile allows proportionate use; it is not a measured estimate of effort saved. [Small-change guidance, lines 15–23](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L15-L23)

The counterexample tests the book's thesis. If the useful decision record already exists and the change preserves it, additional ceremony may supply little new information. We should be willing to record that result in a future exercise. A framework does not earn an advantage because it generated more artifacts for the same accepted behavior.

The comparison must count the whole relevant effort. A fast initial edit followed by a long investigation of unintended changes is different from a fast accepted repair. An extensive setup used for many later changes is also different from a setup repeated for each one. State what cost is being allocated and which later work the observation includes.

One practical check is to ask what each proposed activity will decide. If a new architecture document would merely repeat an unchanged route and query boundary, reuse the accepted context. If a review of the label reveals an unexpected navigation change, inspect and resolve that change. The activity earns its place through the uncertainty it addresses, rather than through a standard document count.

An evaluation record can distinguish one-time setup, task-specific preparation, implementation, acceptance work and repair without assigning invented durations. Leave a category unmeasured until instrumentation exists. When tasks overlap, record the overlap rather than add worker durations and call the sum elapsed time. This prepares an honest cost account while leaving the tiny repair itself small.

Do not assume the opposite result either. A compact repair may depend on a costly understanding of the existing system. The developer who already knows the route, tests and authorization boundary brings context to the task. A new operator may need more investigation before the same small diff is defensible. Line count alone does not describe that difference.

Process size should follow unresolved decisions, consequences and the available evidence. A short request can change a business policy; a longer presentation update can preserve one. If the record shows no material policy or technical uncertainty, choose a small path. If inspection exposes one, enlarge the process for that reason and preserve the discovery.

The method chapters will therefore examine both ordinary increments and bounded repairs. We will not force a large planning route onto a method that offers a smaller one, or remove a required activity to make another method appear cheaper. The evaluated path must be a recognizable configuration of the process being discussed.

### Choose the smallest record by looking at the cost of being wrong

A maintainer can change an explanatory comment after checking that it describes the current behavior. The issue and diff may carry everything a reviewer needs. A change to a shared lookup has a wider effect. The issue should name the intended tenant rule, the paths using the helper and the control that demonstrates authorized reads continue to work. The extra record earns its keep because a reviewer can use it to find a missed path.

When a team debates how much process to apply, name the failure it wants to detect. If the concern is an unstated product decision, assign an owner and record the answer. If the concern is an unnoticed side effect, design an observation where the effect would appear. If the concern is an unattended restart, identify the record the next operator needs. The result can be a small set of concrete duties that already fit the team's review practice.

<!-- C02-S05 -->
## What evidence can establish

A demonstration, a generated test suite and an independently assessed acceptance result answer different questions. A demonstration shows a particular interaction under particular conditions. A suite establishes its assertions for the executed revision and environment. An acceptance judgment relates observations to agreed behavior. None becomes broader merely because its output is confidently phrased.

Consider the history view again. Showing Mira her own request history is useful evidence about the positive path. It leaves foreign-tenant access unresolved. A negative check against an invalid identifier leaves the same gap. A suitable isolation check needs the relevant record and actors, plus an agreed interpretation of what the interface may disclose. Evidence becomes meaningful through that connection to the requirement.

Generated checks can contribute, but the origin of the expectation matters. If the assistant reads an implementation that mistakenly permits administrator self-approval, it might write a test that preserves that behavior. The test could pass while contradicting CS-05. Derive the acceptance expectation from the agreed requirement, then inspect whether the check actually exercises it.

We will call that expectation and its decision procedure the **acceptance oracle**. In a small exercise it may combine assertions, fixtures and a reviewer rule for ambiguous cases. Independence concerns its basis and review, not simply a different file or model invocation. The eventual case needs frozen, independently reviewed checks; none exists yet.

Evidence also needs a defined scope when making effectiveness claims. METR's July 2025 report describes a randomized study involving 16 experienced open-source developers and 246 issues, and reports that AI-allowed work took 19% longer in that setting. The finding concerns those developers, tasks and early-2025 tools. It does not compare our four frameworks or establish a universal slowdown. [METR's original study report](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

METR's February 2026 update then warns that participation, task-selection and concurrent-agent timing issues make its later experiment an unreliable signal of the current productivity effect. We cannot turn those later estimates into a clean trend line. [METR's study-design update](https://metr.org/blog/2026-02-24-uplift-update/)

These sources illustrate why scope and uncertainty matter. They do not settle whether a process improves our case. Nor would a successful synthetic SaaS exercise establish organization-wide benefit. The book needs to state which intervention was observed, which conditions were held constant and what alternative explanations remain.

Preserve missing and adverse evidence as carefully as success. A failed installation, an unexecuted check or a task stopped at a resource ceiling affects what the reader can conclude. Label it at the appropriate level. An environment failure may leave business behavior unassessed; a failed business check may establish a defect under its fixture. Combining both into an unexplained score would hide the difference.

Finally, keep documentary evidence in its proper role. A source can prescribe a human approval or a traceability check. That supports a claim about design. An execution record is needed to show that the activity occurred, and further assessment is needed to establish whether it was effective. This distinction will appear throughout the four deep dives because the same words can otherwise imply much more than the evidence supports.

### Match the completion claim to the entry point

A command handler can pass a unit check while its HTTP route supplies the wrong tenant. When reporting completion, name the entry point the observation exercised and the inputs supplied there. For a local function, record the function and fixture. For an integrated path, identify how identity, tenant and request state reached the decision. This small distinction helps the next reviewer decide which claim the output supports.

<!-- C02-S06 -->
## From habits to repeatable processes

The habits developed here form a small engineering loop: make intent explicit, investigate the relevant context, settle material decisions, bound the change, collect suitable observations and record acceptance or its limits. Repeatability means another person can understand how the work was arranged and examine its evidence. It does not promise identical generated text or code.

A named process may assign these activities to specialized roles, organize them into phases or maintain specifications through change. It may add useful checks and make some decisions easier to recover. It also introduces dependencies and work that deserve examination. The next chapter gives us a common vocabulary for that evaluation.

Before applying a framework, identify the point at which the current arrangement loses information. Does the agreed rule vanish between conversation and planning? Does implementation proceed while a product question remains open? Do acceptance checks reproduce the implementation's assumptions? Does the next session recover the decision, or infer it from stale code? These are questions to investigate in a particular project, not a diagnosis of every informal workflow.

Then ask how the proposed process addresses that point. An artifact needs an owner and a maintenance rule. A gate needs a decision-maker and evidence. A review needs an inspectable scope. A short path needs a way to notice when its assumptions no longer hold. These questions let us assess mechanisms before assigning them a benefit.

The compact record is available even if a team adopts no named methodology. The four frameworks provide larger arrangements to examine against the same obligations. We will preserve their native vocabulary while asking what decisions move through it and what the evidence establishes.

Carry one practical question into chapter 3: for this change, what would another engineer need to know before accepting responsibility for it? The answer sets the minimum useful process. A framework should help the team meet that obligation under its actual constraints, and its suitability remains a conclusion to earn.
