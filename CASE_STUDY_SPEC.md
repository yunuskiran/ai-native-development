# Common SaaS case — proposed specification

Status: **M1 DESIGN ACCEPTED BY THE AUTHOR — NOT EXPERIMENTALLY FROZEN OR IMPLEMENTED**, 2026-10-31, decision A06. Technology family: **TypeScript / Node.js**. The vendor-access approval domain and design direction are accepted for the book. Exact interfaces, fixtures, implementation stack and independent acceptance checks still require technical review and a later freeze. No experiment results are implied.

## Purpose, actors and boundaries

Working case name: **Vendor Access Requests**. A small B2B SaaS records requests for a vendor to receive temporary access, obtains tenant-local approval and preserves decision history. It records an authorization decision; it does not provision access in an external system. Two synthetic customer tenants expose isolation mistakes that a single-user task manager hides.

Actors: a requester creates a request; an approver reviews requests in their tenant; a tenant administrator manages local membership/roles. Roles may overlap, but requesting a particular item disqualifies that person from approving it. There is no cross-tenant superuser in the case's public business interface.

Non-goals: real identity federation, live vendor systems, external provisioning, subscriptions/payments, outbound email, file uploads, production hosting, regulatory certification and organization-wide productivity measurement. Synthetic fixtures and a local execution path are required. The term “Real-World” in chapter 11 denotes realistic constraints unless actual field evidence exists.

## Technical constraints and open choices

| Item | M1 disposition |
|---|---|
| Language/runtime family | **Author selected: TypeScript / Node.js** |
| Application boundary | Proposed typed HTTP/JSON business interface, with a minimal UI only if it improves the shared example |
| Web/UI framework, database and test libraries | **TBD** after M2 compatibility review; no implicit NestJS, Next.js or other framework choice |
| Exact Node.js/TypeScript, method, plugin, host/model versions | **TBD**; M0 pins are research candidates, not an installation freeze |
| Persistence | Must preserve business state across restart and support tested concurrency semantics; storage implementation is not selected |
| Authentication | Server-verifiable identity and tenant membership for the defined local exercise; test identities must not be mistaken for a production authentication design |
| Shared vs native artifacts | Same brief, external acceptance contract and synthetic data; method-native plans, use cases, stories and phase names remain allowed |
| Deployment | Local-only reproduction candidate. Any operational exercise is labeled; external deployment requires separate author action |

The interface contract and supporting scaffold must be frozen before matched runs. Do not add method-specific conveniences after observing outputs. The neutral scaffold must not contain one method's application architecture or hidden solution.

## Proposed business model and state rules

Minimum concepts: Tenant, User, Membership/Role, VendorAccessRequest, ApprovalDecision, PolicyVersion and AuditEvent. These are neutral business concepts, not an imposed persistence schema or class hierarchy.

A request records tenant, requester, synthetic vendor identifier, business reason, risk category (`standard` or `high`), requested expiry and policy version. Proposed states: `pending`, `approved`, `rejected`. A requester creates it in `pending`. A rejection while pending is terminal. An approval is terminal when the versioned policy's required distinct approvals are met. No actor can edit the accepted decision history through the public business interface.

For the base increment, one eligible distinct approver is required. In the change episode, policy v2 requires two distinct approvers for new high-risk requests; standard-risk requests still require one. **Proposed transition policy:** bind a request to the policy active when it was created; existing pending or completed v1 requests keep v1 semantics. Any alternative migration behavior must be specified before E2 is frozen.

Use a controllable UTC clock and synthetic identifiers in tests. Requested expiry must be in the future at creation. This case records the approved access period; expiry does not call external revocation services. Unspecified product behaviors remain open questions, not room for an agent to silently invent requirements.

## Acceptance inventory — definitions only, no test results

Each row needs independently reviewed executable checks later. All are **Not run**.

| Requirement | Proposed behavior | Minimum positive/negative acceptance examples |
|---|---|---|
| CS-01 | Identity and tenant membership are established before business operations | Member succeeds within tenant; missing/invalid identity or non-member is denied. |
| CS-02 | Create a complete, valid tenant-bound request | Valid future-dated request becomes pending; invalid risk, missing reason or invalid expiry is rejected without partial state. |
| CS-03 | Read/list/search are tenant-isolated | Tenant A can read its own request; tenant B's direct-ID/list/search paths expose no record or sensitive existence detail under the chosen API policy. |
| CS-04 | Approval requires current approver membership in the request's tenant | Eligible approver succeeds; requester-only user, foreign-tenant actor and revoked approver cannot decide. |
| CS-05 | Self-approval is forbidden even when roles overlap | Requester holding approver/admin role is denied on their own request. |
| CS-06 | Base policy requires one eligible distinct approval | Eligible v1 approval completes the request; rejected actions do not count as approvals. |
| CS-07 | Reject/approve transitions are consistent and terminal | Pending request can be rejected; completed request cannot later be switched by a competing decision. |
| CS-08 | Retries are idempotent under a frozen request-key contract | Repeating an identical decision creates no duplicate approval/audit success event; a reused key with different payload has a defined conflict response. |
| CS-09 | Concurrent decisions preserve the policy and single terminal outcome | Race approvals/rejections and duplicate submissions; no partial decision state, duplicate completion or missing required count. |
| CS-10 | Successful business transitions have durable, tenant-scoped audit history | Actor, request, event, UTC time and policy version survive restart; foreign-tenant history reads and history mutation attempts are denied. |
| CS-11 | Role administration remains tenant-scoped and does not bypass CS-05 | Administrator can update local roles; foreign membership cannot be changed, and self-approval remains forbidden. |
| CS-12 | v2 high-risk requests require two distinct eligible approvers | First approval leaves pending; second distinct approval completes; repeated first approver does not advance the count. |
| CS-13 | Policy-version transition is explicit and preserves prior valid behavior | New high-risk v2 and standard-risk v2 behave differently as specified; existing v1 requests retain the proposed bound policy. |
| CS-14 | Errors do not leak tenant data or secrets | Not-found/denied responses follow the frozen disclosure policy; logs contain no credentials or unrelated tenant payloads. |
| CS-15 | The seeded isolation defect is repaired with regression evidence | Same predefined affected query fails an independent tenant check before repair and passes after repair; existing acceptance behavior remains valid. |

Detailed response codes, idempotency-key scope/retention, disclosure policy and error payloads must be fixed in the interface contract before code. These definitions do not constitute a complete security assurance or production-readiness assessment.

## Matched episodes and fixture design

- **E1 bounded feature:** same neutral scaffold and brief; implement the base request/decision/read/history path (CS-01–CS-10/CS-14 as applicable). Keep administrative fixture setup outside scored feature scope unless added uniformly.
- **E2 policy change:** same externally prepared working baseline and fixtures for every method; introduce CS-12/CS-13 and run earlier regression checks. Do not use different E1-generated implementations as matched inputs.
- **E3 boundary repair:** same prepared baseline with one predetermined isolation defect and the same observable report; assess CS-15 and retained behavior. Define the defect and hidden checks before runs.

Proposed fixtures: tenants A/B; a requester, two eligible approvers and a role-overlap user in each; one revoked member; standard/high-risk requests; pending and terminal requests under both policy versions; controllable timestamps. Generate no real personal/vendor data. Baseline generation and independent oracle review belong to M4, after scope approval.

## Readiness and open decisions

The [run protocol](research/RUN_PROTOCOL.md) assigns controls and owners; the [M0 readiness checklist](research/EXPERIMENT_READINESS.md) remains unpassed. Domain/design direction is accepted in A06. W04 chooses a qualitative walkthrough for current prose. Exact product contract, stack, host/model compatibility, resources, reviewer and baseline/oracle freeze remain open for executable work. An M1 paper specification is not an executed or technically validated case study.

## Development clarification — 2026-11-02

The accepted rules above are unchanged. Development identifies contract gaps that must not become silently invented acceptance criteria: the effect of revoking a prior valid approver before the second contribution; expiry while pending or at decision time; replay after a permission change or terminal completion; and explicit rejection authority for an otherwise eligible requester. See [P13–P16](research/OPEN_QUESTIONS.md#product-contract-backlog-found-during-development--2026-11-02). Keep unresolved alternatives outside scored expectations until reviewed and frozen. All CS rows remain Not run.
