# 13. Common Failures and Anti-Patterns

> Author manuscript · completed 2026-11-05 · C13 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C13-S01 -->
## A diagnostic pattern with evidence labels

A symptom is not a cause. An approval result that violates intent could arise from an omitted requirement, stale context, incorrect code, a wrong test expectation or a broken fixture. Starting with a favored explanation can lead to an elaborate repair of the wrong problem.

Use a diagnostic record with six entries: observable symptom, conditions, candidate mechanism, discriminating check, proposed recovery and recurrence-prevention question. Label the evidence type. A practitioner's report, an executed case observation and an invented teaching scenario are not interchangeable.

For example, “a requester can approve their own item” is an alleged business symptom. To investigate it, retain actor roles, tenant, request state, policy and the operation used. A screenshot of an approval button is weaker evidence than a recorded successful forbidden transition, but neither should be discarded without understanding its scope.

The following sections organize useful failure hypotheses across methods. They do not establish that a particular framework causes them or that they occur at a measured rate. The purpose is to help a reader ask a discriminating question before changing the process.

### Keep a symptom distinct from its cause

An illustrative support ticket says two users saw the same approval message. That observation could reflect duplicate delivery, two distinct decisions or a presentation bug that rendered one event twice. It can be tempting to classify the incident immediately as broken idempotency. A diagnosis starts by establishing which layer produced the duplicate and which durable records exist.

Ask the engineer to preserve the two messages and recover their source identifiers under the agreed data-handling rules. If both messages refer to one decision, inspect delivery and display. If there are two successful decisions for an action the contract treats as a replay, inspect command identity and persistence. If the available evidence lacks identifiers, record that as an observation gap and design a reproduction with synthetic markers.

This approach also protects the process review. A team can see one incident after adopting a methodology and still need evidence that a specific handoff contributed. If the intended replay rule never reached the implementer, inspect how the rule was recorded and passed forward. If the rule reached implementation but a dependency failed during delivery, the useful correction may be elsewhere. Keep the process explanation as a hypothesis until the records support it.

<!-- C13-S02 -->
## Ambiguous intent and invisible decisions

**Hypothetical symptom:** a policy change applies two approvals to every pending high-risk request, including v1 requests. The code and tests agree, but the accepted case binds policy at creation.

The first candidate cause is missing or misread intent. Inspect the request, decision record and relevant native artifacts. Was v1 preservation stated? Did a later summary omit it? Was retroactivity proposed and explicitly accepted as a task change? These possibilities call for different corrections.

If the requirement was missing, the product owner must settle the behavior before implementation is evaluated. If it was present but dropped from worker context, repair the handoff and inspect affected work. If it reached the worker and was implemented incorrectly, the technical correction belongs downstream. Do not automatically rewrite the specification to match a coherent output.

A useful recovery record would preserve the agreed rule, the location where meaning diverged, the bounded correction and relevant checks. The recurrence-prevention question is specific: which decision should have been visible at the point of implementation or review?

An additional approval ceremony may help only if it exposes that decision. A general “approve plan” prompt without the material policy can reproduce the same failure with more steps. The evidence should justify the process change.

### Recognize when a repair actually needs a product decision

A support report says users sometimes see “pending” after a successful approval. The implementation team assumes this is a bug and asks an agent to mark every successful approval terminal. Under v1 that may look plausible. Under high-risk v2, pending is the intended state after the first eligible approval. The report needs the policy version, prior state and actor sequence before the team can infer a defect.

Start with one observed request and reconstruct its legal history from authorized evidence. Establish which policy was bound, which actors contributed and whether the observed response and durable state agree. If the request is high-risk v2 with one approval, the product decision may concern how the interface explains progress. If it is a v1 request incorrectly evaluated under v2, the repair belongs in policy resolution. If the evidence does not establish the starting state, record the missing fact before opening either change.

A narrow repair can proceed once the owner chooses a direction. Keep the support report linked as the original observation. Record the interpretation separately so that a later reviewer can see how the same symptom led to a particular action. This is especially useful when an agent proposes a broad fix before the team identifies the condition in which the reported behavior is legitimate.

<!-- C13-S03 -->
## Stale artifacts and lost context

**Hypothetical symptom:** a later session reintroduces an old threshold after E2. Candidate causes include an obsolete context file, a plan linked to the wrong requirement, a current specification ignored during implementation or a verification verdict reused after inputs changed.

Inspect what the session actually received where records exist. The repository containing the right requirement does not establish that the relevant worker saw it. A summary saying “context loaded” needs the identity and scope of those inputs before it supports a stronger claim.

GSD Core's documented freshness policy is one concrete mechanism for detecting changes to covered verification inputs. It does not prove coverage completeness or prevent every semantic omission. A current digest of an incomplete input set can still support an incomplete verdict. [Verification staleness policy](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/verify-and-ship.md#L106-L115)

Recovery may require identifying the authoritative current decision, retiring or marking superseded material, refreshing the affected plan and rechecking the changed behavior. Loading every historical document is not an automatic cure; it can leave conflicting instructions competing for authority.

The prevention question is where current intent is owned and how a handoff selects it. A compact current record with a clear supersession link can be more useful than a larger archive with ambiguous status. Its usefulness still needs observation in the selected project.

### Diagnose a stale handoff before regenerating the plan

Imagine a developer resumes E2 after the policy owner has approved a clarification. The plan still describes all pending requests as v2, while the decision record protects v1. First establish the revision and date of the two records. Then inspect which one the implementer received and whether any code or tests were generated from it. The first observable failure might be that a preserved v1 request stays pending after one eligible approval. This sequence is illustrative.

Repair the link at the point where the stale record entered the work. Update the task plan and any fixture that copied its assumption. Refresh affected verification against the revised code. Keep the earlier output with its revision so a reviewer can distinguish an obsolete result from a failed check on the repaired implementation. Regenerating all documentation would create more material to review while making the provenance of the contradiction harder to see.

After the repair, ask a contributor to locate the governing policy using the normal handoff. Observe whether they reach the active record and can distinguish its v1 and v2 examples. If the active record is easy to find and the wrong plan was a one-off, a narrow repair may suffice. Repeated failures at the same handoff give a reason to change where the workflow records and consumes decisions.

### Diagnose a current document that carries an obsolete interpretation

A document may have a recent timestamp because someone changed formatting while leaving its behavioral assumption untouched. Inspect the accepted decision and the text that actually reached the work. Timestamp freshness alone cannot tell whether the interpretation is current.

Suppose a plan still treats every approval as terminal after the product owner introduced an intermediate pending state. The plan's revision may be newer than the policy decision. Compare the relevant sentences and trace which implementation and test expectations consumed them. Repair those dependencies and attach a fresh observation to the current candidate.

Then inspect the mechanism that selected context. If contributors chose the plan because it appeared first in search, a clear link to the accepted rule and an explicit supersession note can help. If the active work entry point copied the obsolete sentence, correct that entry point. The diagnosis should identify the path by which the assumption reached execution.

A later handoff exercise can test the repair. Ask another contributor to identify the expected result after the first eligible action on high-risk v2. Record the source they used and whether they found the preserved v1 rule as well. This gives the team an observation about the corrected context path.

<!-- C13-S04 -->
## Ceremony without useful decisions

**Hypothetical symptom:** a tiny display repair generates extensive product and architecture documents, while the only needed choice is already clear. Another project has the opposite symptom: a short path proceeds despite unresolved policy binding. Both concern process sizing, not the intrinsic virtue of fewer or more files.

For each activity, ask which decision it makes, which uncertainty it reduces or which acceptance obligation it supports. If the answer is a duplicate of current accepted context, reuse or link that context. If the activity exposes a material uncertainty, retain it even when the diff is small.

BMAD and Core document small-work allowances in the inspected sources. Their presence is counterevidence to forcing every task through the largest route, but it does not establish the actual cost of a reduced path. [BMAD](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md#L15-L23), [Core](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md#L77-L90).

Recovery is a process decision: remove redundant work, clarify ownership or enlarge a path for a newly discovered risk. Record why. A future evaluation should include preparation, review and relevant repair rather than report only initial code generation time.

The prevention question is whether the selected profile has a recognizable task-sizing rule and a way to revisit it. An informal shortcut that silently omits a required gate is a deviation, not automatically a legitimate minimal path.

### Remove work only after finding the duty it serves

A team sees three review records generated for every repair. Each repeats the same file list and none names the product decision. Before eliminating the records, inspect who reads them and what decision each is meant to enable. The apparent duplication may conceal a real approval or evidence requirement. If one report is the only retained record of the release review, removing it without moving that duty would create a gap.

Try a narrower change. Preserve the release disposition and the evidence it relies on. Combine the duplicate preparation notes into one record that names the authorized repair, affected path and required observation. On the next repair, inspect whether a reviewer can still find the decision and reproduce the relevant check. The outcome tells the team whether the simplification preserved the duty under the selected conditions.

For a high-risk change, the team may need a separate decision before implementation and another before release. Those decisions can use different evidence even if they refer to one requirement. Keep both when they constrain different actions. The goal of a lighter workflow is to reduce the work required to make and inspect decisions, while keeping those decisions visible.

<!-- C13-S05 -->
## Circular checks and false completion

**Hypothetical symptom:** a suite passes while the agreed requester exclusion is absent. A candidate mechanism is circular validation: tests reproduce the implementation's assumption or exercise a different denial condition. Inspect expected behavior and fixtures before adding more tests of the same mistaken interpretation.

The book's earlier pilot contained a real editorial ambiguity: its case table could be read as completing a request before testing self-approval. The v0.2 correction made checks independent and required a pending-state fixture. This was a flaw in the teaching/test design, not an observed application or framework failure. The [revision record](../../research/M3_REVISION_REVIEW.md) preserves that distinction.

A separate first-hand account reports a collaborative AI-DLC sample marking empty stages successful after a credential-related error returned a zero exit code. Its author identifies an AWS role and states limits on what was observed. This is evidence about that reported platform incident, not an independent trial or a general result about AI-DLC. [Agius's field account](https://www.agiusalexandre.com/blog/2026-09-26-ai-dlc-collaborative-team-bottleneck/)

The diagnostic question is what the status actually measures. Did a process launch, did it produce the expected artifact, did a check assert the intended condition, or did a reviewer accept the behavior? Those events can diverge. Inspect the relevant output and its interpretation rather than assume green means the business goal was met.

Recovery may involve fixing a check, distinguishing empty output from completed work, invalidating a verdict or rerunning the affected activity. Preserve the initial result and reason for correction. A rewritten success summary alone would remove the evidence needed to understand the failure.

### Investigate an all-green suite

Suppose a report claims tenant isolation because a test attempted to read an A request as a B actor and received a denial. Inspect the fixture before examining the authorization branch. If the identifier never existed, a lookup without any tenant scope could produce the same result. A useful repair starts by creating the protected record and demonstrating that an authorized A actor can retrieve it. Repeat the B probe and check that the observed behavior matches the disclosure contract.

For a write path, check state and history as well as the response. A command can return a denial after doing work that should have been forbidden. Separately verify that an eligible action can succeed and produce the intended history on a clean fixture. These controls let a later reviewer explain what kind of failure a passing suite would detect. Chapter 12 develops the corresponding oracle design.

Record the original claim as unsupported by the old fixture, even if the repaired check subsequently passes. A corrected check establishes a new observation. It does not change what was exercised in the earlier run. The distinction matters when the original report was used to approve work or was cited as evidence for a larger process claim.

### Review a generated diagnosis against the actual failing observation

An agent may explain a failed probe with a plausible race condition. Before changing concurrency controls, ask which observation requires that explanation. A repeated response might come from transport retry, a duplicate display event or two durable contributions. Recover the identifiers and state necessary to distinguish them.

If the proposed cause predicts two approval rows but only one exists, revise the hypothesis. If two rows exist, inspect whether both are successful contributions under the contract and which commands created them. The next repair should follow the observed boundary. Preserve the rejected explanation only where it helps a future reviewer understand the investigation.

A diagnosis can be useful even when the first hypothesis fails. Record the observation that changed the interpretation and the narrower action it enabled. This gives the team a concrete improvement to its debugging practice and prevents a confident generated explanation from becoming accepted incident history without supporting evidence.

<!-- C13-S06 -->
## Repair narrowly and retain the record

For a tenant-boundary defect, narrow repair means a justified change boundary with meaningful regression evidence. It does not mean changing the fewest possible characters. The same boundary may apply to direct identifiers, lists, searches and history reads.

Begin with a known existing foreign record, controlled actors and the operation identified in the report. Record the pre-repair observation when an executable baseline exists. Inspect the relevant authorization/data-access path and propose the correction against the accepted requirement. Do not invent that observation when the baseline has not been prepared.

Preserve attempted repairs separately from accepted ones. A patch that blocks one route but leaves the shared query unscoped may be useful diagnostic evidence. A failed assertion caused by a bad fixture needs a different disposition. Both should remain visible with their conditions.

The proposed repair record contains:

| Entry | Purpose |
|---|---|
| Baseline and symptom | Makes the alleged failure recoverable |
| Fixture and expected result | Establishes which business boundary is under examination |
| Candidate causes and checks | Distinguishes diagnosis from speculation |
| Change and rationale | Explains why the scope is sufficient and proportionate |
| Actual regression observations | Relates repaired and preserved behavior to evidence |
| Open limits | Prevents a narrow repair from becoming a broad assurance claim |

No such application repair packet exists for our case. Chapter 11's E3 remains a design. The record here gives a future operator a structure for honest recovery rather than a simulated success narrative.

### Write a repair note that can be used next week

An illustrative record starts with the claim under review: the repair prevents foreign access to an existing request on the specified path. It then records the original observation and why its fixture could pass without exercising tenant scope. The revised fixture establishes that A can see the record and checks the defined B response. The remaining surfaces retain their own status. A later reviewer can tell which part of the earlier claim changed and why.

Link the evidence to the revision that produced it. If the repair later moves scope enforcement into a common helper, revisit the callers affected by that move. A prior result at one endpoint can remain useful, but the broader change creates additional questions. A small note with the original boundary, corrected fixture and affected callers can support that follow-up without reconstructing a long conversation.

### Repair the workflow at the first point of loss

A worked diagnosis can follow a decision from ownership through use. The owner resolves a disclosure rule in a review thread. The planner copies a short summary into an issue. The implementer sees the issue and treats the summary as permission to use a different error for a known foreign record. The acceptance reviewer checks only that the response body omits the record. The workflow has lost a constraint before implementation and selected an observation that cannot reveal the loss.

The team can repair both causes without rebuilding its process. Place the accepted rule where the work record links to it. Update the fixture to distinguish a known foreign record from a nonexistent identifier under the agreed response contract. Review the repair and record the earlier finding separately. Another run can then tell the team whether the corrected handoff and observation address the diagnosed failure.

If the next change still loses the rule, investigate how contributors select context. A document can be current and still never reach the actual work. Ask a contributor to show their inputs and how they determined the governing record. A small change to the work entry point may solve the problem more directly than another checklist at the end.

<!-- C13-S07 -->
## Use failure to update process choices

An incident should change a process choice when evidence identifies a weakness in the arrangement. A lost policy exception may justify better context ownership. Repeated stale verdicts may justify freshness checks. Excessive work on tiny repairs may justify a smaller profile. The remedy should address the mechanism the record supports.

Avoid universal conclusions from one event. A field report can reveal a concrete defect without establishing prevalence. A synthetic example can test reasoning without predicting production frequency. A failed host integration may concern the adapter rather than the method's core design.

Return to chapter 10's selection record. Update the evidence, affected constraint, cost/uncertainty and revisit trigger. Preserve the earlier reasoning so readers can see why the decision changed. An unsupported failure hypothesis should create an investigation task, not an intuitive penalty score.

The final chapter asks how this learning procedure survives changes in models, hosts and frameworks. Its starting point is the same discipline used here: identify the claim, inspect the conditions, preserve disagreement and make the next commitment proportionate to the evidence.

### Look for a repeated failure at the same boundary

A team might observe that two different changes passed native verification but each missed a preserved behavior. Before adding a new review phase, compare the two incidents. Did the owner fail to record the obligation, did the plan omit it, or did the fixture never exercise it? If both failures started in the fixture, a review rule that checks fixture preconditions may be more targeted than adding another plan approval.

Record the resulting process change as an experiment. Name the failure it should catch and choose an observation on the next applicable change. For the approval service, a reviewer could inspect whether the v1 preservation probe actually starts with a request created before the switch. If the process change catches a broken fixture, retain that observation and describe the conditions. If it finds nothing, distinguish absence of a defect from the test's ability to detect one.

Treat a counterexample as a reason to revise the rule. If a small repair produces clear evidence through an existing regression test, a new checklist may repeat information without exposing a new risk. Keep the review duty and adapt its form to the type of work. A repeatable process is easier to sustain when each required action has a visible purpose.

### Retire a corrective rule when its purpose disappears

A team may add a manual handoff check after repeatedly losing one product constraint. Later, a maintained work entry point can carry that constraint and expose stale evidence directly. Review whether the manual action still detects something the new arrangement misses. Use an actual bounded exercise and record the result.

If the manual check repeats an observation already available at the decision, the team can propose removing it and name where the duty now lives. If it still catches missing context, retain the action and explain the boundary it protects. This keeps process changes connected to the failures that justified them.

Review the retirement after the next applicable change. A simplified process can be accepted with a concrete observation, just as an added control can. The team can preserve the earlier incident and correction as history while keeping the active workflow understandable.
