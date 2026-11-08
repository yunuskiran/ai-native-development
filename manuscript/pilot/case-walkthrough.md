# Pilot case: following one approval decision

> M3 narrative walkthrough v0.2 · 2026-11-01 · Design only; AI revision complete. Companion to the chapter samples, not chapter 11 or an executed trial. All actors and events are synthetic. Independent review remains pending.

Mira belongs to tenant A and requests temporary access for a vendor. Leon and Priya are approvers in A. Ozan belongs to tenant B. An overlapping-role variant also gives Mira approver and administrator roles, so the example can expose an accidental self-approval exception.

The service records an approval decision; it does not create a vendor account or grant access in another system. That boundary keeps the proposed exercise local. TypeScript / Node.js is the author's selected technology family. Framework, database and exact versions remain open.

## Establish the rule before constructing the story

Under the proposed base policy, Mira's valid request becomes pending. One eligible, different approver in A may approve it. A requester may not approve their own item even if they hold other roles. Ozan must not obtain A's request through reads, lists, searches or direct identifiers. Successful business transitions require durable, tenant-scoped audit history. These are design obligations in CS-01–CS-10 and CS-14 of the [case specification](../../CASE_STUDY_SPEC.md), not observed behavior.

Before an executable acceptance check can be written, the interface contract must settle several details. What response distinguishes a conflicting idempotency key from a harmless retry? What disclosure policy applies to a foreign-tenant identifier? How will fixtures establish identity and membership? An agent must not silently supply these decisions during a measured run.

We can nevertheless describe the intended acceptance boundary. These rows are independent checks, not actions performed in sequence on one request. Reset the fixture for each row. In particular, the self-approval request must still be pending and Mira must otherwise hold the required roles. A denial caused by an already completed request would not establish CS-05.

| Proposed action | Required interpretation | Observation needed later |
|---|---|---|
| Leon approves Mira's pending v1 request | Eligible same-tenant decision | Terminal approved state and matching durable audit record |
| On a separately reset pending v1 request, Mira with approver/admin roles attempts approval | Forbidden self-approval | Denial with no successful decision or success audit event |
| Ozan reads the request by its identifier | Foreign-tenant access | No request data or prohibited existence detail under the frozen disclosure policy |
| Within one isolated retry check, an eligible decision is submitted twice with the same key and payload | Idempotent repetition | No duplicate approval or success audit event under the frozen key contract |

Each row describes a future check. None has passed. Concurrent approval/rejection and persistence across restart remain additional obligations; the four rows are not a complete acceptance suite.

## Carry a change without rewriting the past

The second episode introduces policy v2: a new high-risk request requires two distinct eligible approvers. One approval leaves it pending; a second distinct approval completes it. Repeating Leon's approval must not substitute for Priya's. Standard-risk v2 requests still require one approval.

The accepted design direction binds requests to the policy active at creation. An existing pending v1 request therefore keeps v1 semantics. This makes the change a useful test of how a process carries a decision across artifacts and code. An instruction as short as “require two approvals for high risk” would leave the treatment of existing requests unresolved.

For a controlled comparison, each framework would begin this episode from the same externally prepared working baseline. Feeding each method its own previous feature output would entangle the change procedure with differences in those implementations. The proposed matched baseline controls that starting condition; it does not eliminate every confounder.

The third episode repairs one predetermined tenant-boundary defect in another shared baseline. Its exact query, report and hidden regression checks must be frozen before runs. We will not plant a different defect after seeing which failure a method handles well.

## Preserve native work and a common acceptance boundary

A BMAD path may organize the work around a specification and linked stories. Another framework may use phases or use-case records. The comparison should retain those native artifacts while holding business intent, starting state and external acceptance obligations constant. Requiring identical planning files would change the intervention being evaluated.

The pilot prose asks whether the reader can follow that distinction. It does not answer which framework produces the best implementation. A later run would need the exact source and package identities, enabled modules, host/model settings, operator interventions, resource ceiling, baseline hash and actual command/output records defined in the [run protocol](../../research/RUN_PROTOCOL.md).

There are two legitimate future deliverables with different evidential scope. A documentary walkthrough can show how the selected instructions would organize this problem. An executed exercise can add observations from a real environment. Only the latter can support claims about what happened during that execution, and neither alone establishes organization-wide productivity or production safety.

The current artifact is the first kind. The [experiment readiness checklist](../../research/EXPERIMENT_READINESS.md) remains open; no baseline, independent executable oracle or trial has been completed.
