# 12. Testing, Security & Production Readiness

> Author manuscript · completed 2026-11-05 · C12 · Documentary method accounts and synthetic teaching examples. Source and execution scope are summarized in the front matter and source notes.

<!-- C12-S01 -->
## Define acceptance and evidence ownership

Acceptance begins with an expected behavior and someone authorized to decide whether the evidence supports it. Generated code, a test report and a workflow status can contribute, but none can supply a missing product decision by itself. The same obligation applies regardless of which framework arranged the work.

For the SaaS, CS-05 forbids self-approval even when roles overlap. The expectation comes from the agreed case requirement. Implementation and acceptance checks must be assessed against that rule. If a test expects administrator self-approval, a passing result would preserve the wrong expectation.

Assign ownership at the decision level. The product owner resolves intended behavior. The implementing engineer explains the design and changes. The acceptance reviewer checks the expectation, fixture and observation. An operational owner decides which further conditions justify deployment. One person may hold several duties, but the record must expose that overlap.

Independent review requires a real reviewer arrangement with interests disclosed. Another model invocation can provide a useful perspective, but it is not independent human validation. A generated checklist can support a reviewer; it does not appoint one or establish that the review occurred.

NIST's SSDF 1.1 publication describes high-level secure-development practices that can be integrated into a lifecycle. We use it as a reminder that selecting an AI-oriented process does not exhaust secure-development duties. This is a fixed-version reference, not a claim of SSDF compliance. [NIST SP 800-218, SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final)

The acceptance decision should identify the reviewed revision, relevant observations, unresolved risks and scope. “Accept the local synthetic increment with specified limits” differs from “release a supported service.” Keep those decisions separate even when one meeting discusses both.

### Write the decision before collecting results

Suppose an engineer proposes releasing the v2 policy to a synthetic test environment. The release question is whether new requests can be bound to v2 while existing v1 requests can still be decided under v1. The reviewer needs evidence about both populations. A checklist headed “v2 tests passed” gives no way to tell whether the release could strand an existing request. Write the decision sentence first, then identify the observations that would change the decision.

One workable separation is to ask the product owner to name the protected behaviors, the acceptance reviewer to define the fixture and inspect the result, and the release owner to set the operating boundary. For this exercise, a release owner might allow a synthetic environment to be rebuilt after a failed migration. The same recovery decision would be inappropriate for an environment carrying real decisions and audit records. State the environment in the disposition so someone cannot lift the sentence out of the packet and apply it elsewhere.

When a check fails, distinguish the requirement from the failure mechanism. If the v1 request stays pending after an otherwise eligible approval, the reviewer can record the contradiction before anyone diagnoses it. If the fixture accidentally assigned v2 at creation, correct the fixture and retain both records. If v1 was assigned correctly and the runtime applied v2 anyway, the application is the repair target. This sequence gives reviewers a common observation even when they disagree about the cause.

<!-- C12-S02 -->
## Use generated tests without circular validation

Generated tests are useful when their assertions address intended behavior. Their existence and passing status do not establish that relation. An implementation can embody a mistaken assumption, and a test derived from it can repeat the assumption precisely.

Separate three inputs: the business expectation, the fixture that makes the expectation observable, and the implementation under examination. For the self-approval rule, begin with a pending request, valid same-tenant membership and a requester who otherwise holds sufficient roles. An invalid identity or terminal request could produce a denial without exercising the requester exclusion.

Use a separate positive control. An eligible different actor should be able to make the permitted decision on an equivalent pending request. If every action fails because the fixture is broken, the negative example has not established the intended boundary.

The same reasoning applies to tenant isolation. A B actor attempting an A identifier is informative only if the record exists and a permitted A view works. Lists and searches need fixtures that would expose a leak if scope were missing. A page containing no data by accident cannot certify isolation.

An independent acceptance inventory can coexist with native generated tests. Keep the generated suite for its useful implementation coverage, then map external expectations to actual observations. Do not discard a stronger native check merely because it was generated; inspect its basis and scope.

Where justified, a controlled fault or mutation can help test whether an acceptance check detects the intended defect. If removing an eligibility guard leaves the relevant check green, investigate the fixture/assertion. Such a diagnostic must be deliberately scoped and kept separate from production. No mutation exercise was performed here.

Record actual commands and outputs when checks run. Include the revision, environment, fixtures, selected tests, result and interpretation. A textual summary without a retrievable observation cannot support the same claim. Unexecuted checks remain Not run, including every application check proposed in this book.

The [policy-model companion](../../examples/approval-policy/README.md) supplies a deliberately narrow example: ten locally executed checks of a sequential approval function passed, including a pending-state self-approval negative case and a separate positive control. Its [run record](../../research/evidence/POLICY_MODEL_RUN.json) preserves the command, runtime and file hashes. That is an observation about the authored in-memory model, not independent application acceptance. Database, audit, retries, concurrency and static type-checking remain outside that result.

### Design an oracle around a plausible false pass

Take two requests in the same tenant, both pending and owned by Mira. On the first, submit a decision as Mira with the roles needed to pass the ordinary role check. On the second, submit an equivalent decision as Leon with the same applicable role. Establish that both actors can reach the operation under the fixture's authentication assumptions. Keep request state and policy version equal across the pair, and vary the relationship between actor and requester. The positive control needs its own record so it cannot be affected by the denial attempt.

Observe both the decision and durable state. If the self-approval action returns the expected denial but inserts an approval row before returning, an assertion on the response alone misses the defect. A later eligible decision can make the inconsistency harder to diagnose. Read state and history through an agreed observation path, compare them with the known initial values, and name the exact records that are forbidden to appear. Any denial event permitted by the contract needs a separate assertion from the prohibition on a success event.

A test author can diagnose the quality of this check by proposing an intentional fault and predicting which assertion would notice it. Imagine preserving the rejection response but moving the state write ahead of the actor check. A robust design would detect the write regardless of the apparent response. Imagine instead making every request fail before authorization. The positive control should detect the broken entry path. These are thought experiments for inspecting a proposed oracle. If a reviewer later executes a fault probe, restore the reference revision and record the faulted revision separately.

One suite can contain fast in-memory checks and slower tests across the actual persistence boundary. The first can answer whether the policy function computes a transition. The second can answer whether the service applies it to the right row under the agreed fixture. Give them distinct names and retain both. A failure in a fast check helps localize a policy regression, while a failure only at the boundary can reveal integration behavior the function was never asked to model.

<!-- C12-S03 -->
## Trace requirements through changes

Traceability is an inspection route. It should let a reviewer travel from requirement to decision, implementation and observation, and back from a material change to its justification. The quality of the links matters more than their count.

For E2, the changed high-risk threshold is only part of the requirement. Existing v1 requests retain their creation-time policy, standard-risk v2 remains one-approval, and tenant/self-approval constraints continue to apply. A narrow test of the final high-risk approved state leaves several obligations unresolved.

Use a requirement-impact record to distinguish changed, preserved and newly relevant checks. A stable requirement ID can retain its intent while new code locations depend on it. A test that was sufficient before the change may no longer address all affected paths.

The observed revision must also match the reviewed one. GSD Core's source describes fingerprint-based verification staleness and a legacy modification-time rule. That is one explicit freshness mechanism, not proof that all relevant inputs are covered. Inspect both freshness and semantic coverage. [Core verification freshness](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/verify-and-ship.md#L106-L115)

AIUP separates structural specification checks, semantic advice and implementation/test coverage, with adapter-specific limits. BMAD separates built-in generated QA from optional broader testing. AWS profiles alter checks and reviews. Their mechanisms can support the evidence packet, but the common acceptance question remains external to any favorable status. [AIUP coverage scope](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md#L388-L417), [BMAD QA boundary](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/test-completed-work.md#L76-L105), [AWS profile differences](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/workflow-profiles.md#L45-L95).

A useful report therefore includes both the native verdict and its interpreted scope. If a requirement is linked but untested, say so. If a check failed for an unrelated fixture issue, preserve the failure and correction rather than call it a product defect without evidence.

### Read the change from both directions

An impact review begins at the requirement and ends at something observable. For creation-time policy binding, the reviewer first locates where creation selects the version, then where decisions resolve that saved version, then where a check creates a request under one policy and decides it after the policy changes. A test that inserts a v1 marker directly can isolate the resolver, but leaves the creation path open. Pair it with a sequence that goes through creation and assert the stored version before attempting the decision.

Then reverse the walk. Start from each edited boundary and ask which obligation it affects. If a migration changes both the policy representation and the index used for tenant-scoped lookups, the change reaches beyond threshold behavior. A reviewer needs to know whether direct lookup, history and search still enforce the intended tenant scope. The code diff can reveal an affected path that the original ticket did not name. Update the impact record before using the earlier acceptance plan.

| Changed surface | Preserved obligation | Observation to request |
|---|---|---|
| Request creation | Version fixed at creation | Requests created before and after policy switch retain their respective identifiers |
| Decision command | Distinct eligible actors | Repeat one actor on high-risk v2 and inspect count and terminal state |
| Migration | Existing v1 stays decidable | Use a pre-migration fixture, migrate it, then decide it through the normal entry point |
| Tenant lookup used by history | Foreign actors cannot obtain case history | A known existing record is visible within A and protected from B under the agreed contract |

The table is an example of a proposed review, and every observation is still open. The useful evidence key is the combination of expected behavior, observation and identity of the checked artifact. If a developer edits the migration after the reviewer observed it, a passing log can remain useful history. The decision about the new revision needs either a fresh observation or an explicit explanation of why that specific evidence still applies.

### Use a trace review to decide which checks need another run

A small change to a display label can leave policy-function evidence intact while requiring a visual check at the affected screen. A change to the resolver can leave the accepted policy record intact while requiring fresh behavior observations. Write the affected dependency next to the check so a reviewer can explain the difference.

For the case, a migration change can affect the creation-time version even if the decision function remains byte-for-byte identical. The preservation probe needs the migrated record as its input. A fresh function check alone would leave that path open. Conversely, if a documentation correction changes no executable input, a reviewer can retain the earlier run and inspect the corrected explanation.

The decision to reuse evidence should state its premise. Identify which inputs stayed the same, which changed and why the observation still addresses the claim. If the inputs cannot be recovered, mark the evidence as historical and schedule the observation needed for the current candidate. This is a bounded freshness review that a later contributor can repeat.

<!-- C12-S04 -->
## Examine the SaaS boundaries

The case's security-relevant boundaries are business-specific. Identify the actor, target resource, tenant, current membership, requested action and current state. An administrator role alone cannot override the requester exclusion. A difficult-to-guess identifier cannot substitute for an authorization rule.

OWASP's authorization guidance recommends denying by default and validating permissions on every request. Those are general principles; the concrete case expectation still comes from the defined tenant and actor rules. A local check against selected paths does not establish comprehensive authorization coverage. [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

An original boundary model for this exercise is:

| Boundary | Case question | Proposed negative/consistency evidence |
|---|---|---|
| Identity to membership | Is this actor a current member of the selected tenant? | Invalid, foreign and revoked membership fixtures |
| Membership to request | Does the target request belong to the permitted tenant scope? | Direct-ID, list, search and history probes |
| Actor to decision | Is the actor eligible and different from the requester? | Pending-state overlapping-role control and permitted different actor |
| Decision to persistence | Can competing or repeated actions break the versioned policy? | Defined retry/concurrency tests with final state/history inspection |
| Persistence to history | Is the successful transition represented durably without foreign disclosure? | Restart, scoped read and history-mutation probes |
| Service to logs/errors | Does the defined response disclose only permitted information? | Contract/error/log review with synthetic sensitive markers |

Concurrency requires a declared legal-outcome model. Two calls returning success is not necessarily sufficient evidence: inspect distinct approvals, terminal state and audit consistency. Conversely, one losing concurrent action may be expected. The chosen semantics and execution record determine the conclusion.

Durability also needs an actual boundary. An in-memory assertion before restart does not establish persistence. A database row can exist while a matching audit record is missing. The future design must define which changes must commit consistently and how its checks observe that obligation.

OWASP ASVS supplies a broader security-requirement framework; the inspected site identifies release 5.0.0. It can guide a separately scoped assessment. We have not applied every ASVS requirement or certified this case against the standard. [ASVS overview and edition](https://asvs.owasp.org/)

The local exercise intentionally excludes production federation and real access provisioning. Those exclusions remove particular integrations from the example, not from the duties of a service that later adopts them. Expand the assessment when the system boundary changes.

### Use the access model to find paths the happy flow hides

Build a small surface inventory before selecting checks. A request can be reached by a direct identifier, a filtered list, a search result, an audit-history view and an action command. If a future UI adds counts or previews, include those outputs too. Each surface can reveal different information. The visible rows in a list could be correctly scoped while a total count includes foreign rows. A foreign direct request could conceal content while exposing a distinguishable error. The case owner has to settle the disclosure contract before the reviewer interprets those differences.

Construct the fixture so a missing filter could plausibly change the answer. Put matching search terms in both tenants. Use enough rows to exercise a cursor or page transition if that interface exists. Keep the permitted result visible while checking the prohibited result. Use synthetic markers with no production meaning so the reviewer can identify leakage across bodies, counts and history without copying personal data into the evidence.

A write check should distinguish lookup scope from authority over the transition. If B sends a decision request against A, inspect the externally permitted response and verify that A's state and success history remain unchanged. If a tester uses only an identifier that was never stored, the lookup can fail before tenant logic is involved. Establish existence through an authorized A path and use a different observation channel for the negative request. The evaluator can then explain exactly what the case exercises.

### Turn competing writes into a finite set of legal outcomes

For a single-approval pending request, imagine an eligible approve and an eligible reject released from a coordinated starting point. The product contract has to say which actions are terminal and how a losing action is reported. If either decision may win, the oracle can accept either of two final histories. It should still reject a history with both successful terminal decisions, an unmatched success event, or a terminal state that contradicts its recorded winner.

A separate probe covers a high-risk v2 request receiving two distinct approvals. The contract may permit either actor to be first. The oracle should reconstruct the sequence from durable evidence rather than assuming the client response order is the commit order. Both requests returning without transport error gives little information about the resulting state. The useful question is whether the durable outcome belongs to the set the contract permits.

A retry introduces another dimension. The same actor may repeat a successful request after losing the response. The case needs a frozen scope for the key and a defined result when a reused key arrives with a different payload. Keep that test separate from two distinct actors competing. The first tests command identity and replay behavior. The second tests simultaneous transitions and decision eligibility. Combining them in one fixture can obscure which rule prevented an unwanted second transition.

A deterministic schedule can make an exercise easier to diagnose, while repeated schedules can expose outcomes the first one misses. Record whatever coordination the harness actually provided. Launching requests together at the client only proves that the client issued them together. If the service serialized them before the contested boundary, describe that observation and qualify the concurrency claim. A useful report can show a specific prohibited state was absent in a specific exercise without generalizing to all schedules.

### Inspect failure after a permitted action begins

Authorization is only the beginning of a successful decision. Suppose a permitted approval reaches persistence and the storage operation fails. The service needs a defined way to represent the action's outcome so a client can decide whether to retry. The contract should identify what proves a committed contribution and what a later retry can observe.

A proposed failure probe can begin with a pending request and one authorized command. Introduce a controlled failure at the boundary the architecture claims to handle, then inspect response, durable state and success history. The expected result depends on the selected design. A single transactional design and a separately delivered history design need different observation rules.

Keep this probe separate from an unauthorized attempt. Otherwise a denial can mask the persistence path the test was meant to exercise. A positive control should demonstrate that the same fixture can complete a permitted action when the injected condition is absent. Record the actual failure point provided by the harness, since a failure before the write and one after commit ask different questions of the retry contract.

<!-- C12-S05 -->
## Review dependencies, configuration and secrets

An application can satisfy a business assertion while relying on an unsuitable dependency or configuration. Record exact runtime/compiler/library versions, lockfiles, build inputs and enabled options when execution exists. A framework's minimum version statement does not prove a common stack actually builds or behaves correctly.

The Core guide/manifest discrepancy and AIUP Node adapter assumptions are concrete examples from our evidence base. Resolve them through an installed-artifact and compatibility exercise before publishing a setup recipe as tested. Do not average conflicting prerequisites or transfer one adapter's tested status to another.

Build, lint, dependency and security scans supply scoped observations. A clean report means the selected checks found no reportable issue under their rules/database/configuration. It does not establish absence of every vulnerability. Retain tool versions, inputs, exclusions and findings requiring judgment.

Secrets have a lifecycle beyond keeping them out of a source file. OWASP discusses creation, rotation, revocation and expiration. An exposed credential may need revocation or replacement in its backing system; restarting an application is not that action. We have inspected guidance, not an actual credential exposure in this project. [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

Use synthetic data and controlled credentials in any future local example, and keep real secrets out of prompts, logs, screenshots and evidence packets. Record redaction and access rules without including the secret values. If a supporting service is unavailable, document the limitation rather than invent successful integration evidence.

There is also a development-agent boundary. The SaaS need not expose an LLM endpoint for repository text, issue content or tool output to carry adversarial instructions to a coding agent. Treat external content as data, constrain tool permissions and validate consequential actions at the execution boundary. OWASP's prompt-injection guidance describes layered controls; it does not promise complete prevention. [OWASP prompt-injection guidance](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)

Keep agent and application assurance separate. An agent's permission to edit files does not authorize a production deployment. An application's tenant check does not protect the agent from following hostile repository instructions. Both boundaries need their own design and evidence.

### Inspect the configuration that will actually run

Start with a candidate release that passed its local application checks. Suppose the test process used a fixture identity provider while the intended environment uses a real integration. The evidence packet should name the identity mode used in each environment and explain which behaviors the test mode bypasses. An engineer reviewing the release can then see whether the claimed check exercised membership, request scoping and policy decisions, and whether it exercised any part of the integration.

For dependencies, preserve the resolved input and the scan configuration together. A finding has an affected component, a version and a path into the build. The disposition should explain whether the component reaches the running service, what action was taken, and how the revised release was checked. If the team accepts a finding temporarily, name the owner and the condition that triggers a new decision. This is an illustrative review procedure. No scanner or dependency database was selected for the case.

The agent boundary deserves a concrete review as well. Imagine an issue attachment containing a command that asks the agent to fetch an environment file and send it to an external endpoint. The issue may provide useful reproduction details while carrying unrelated text. The review should trace the authorized task through permitted reads and edits, then check that external actions require authorization from the controlling workflow. Repository write permissions and application network permissions should be inspected separately. A synthetic exercise can record the attempted action and its disposition without including real credentials or sending data.

### Separate the shipped dependency graph from the development environment

Suppose a local check passes using a developer's installed tooling and a lockfile that changed during experimentation. A release reviewer needs to know which inputs actually built the candidate. Record the package lock, build environment and resulting revision, along with the configuration consumed by the deployed service. When a local helper exists only on the developer's machine, describe that dependency before interpreting the command as reproducible.

A finding in an installation tool has different reach from a finding in code loaded by the running service, although both can matter. Inspect the path by which the affected component enters the build or runtime and identify what privileges it receives. A component that executes during the build may see build credentials even if it does not ship. A runtime library may handle request data without ever touching deployment credentials. These distinctions inform the scope of a proposed fix and the evidence needed to review it.

If the fix updates a package shared by test and production, rerun the checks tied to affected behavior and retain the resolved versions used by that run. A scan can contribute a new finding or confirm the scanner's revised view of the dependency graph. The decision about release also depends on the service behavior and on the disposition of any unresolved findings. In this book those steps describe a possible review packet for a future executable case.

<!-- C12-S06 -->
## From local evidence to operations

A local demonstration can establish useful observations about a selected revision and environment. Production readiness asks wider questions about service ownership, changes, failure and recovery. The word ready needs a declared scope rather than a universal status.

For the approval service, operational questions include detecting decision failures, preserving state/history through restart or migration, recognizing a bad policy rollout and recovering without changing already-bound request semantics accidentally. A rollback plan must account for data created under the newer policy, not only code reversal.

These are questions for a selected architecture and environment. No database, migration tool, deployment platform or backup system is frozen here. We therefore do not supply untested commands or claim that a particular transaction/isolation setting solves every case boundary.

Separate planned controls from exercised controls. A documented restore procedure is preparation. A retained restore exercise with checked business state is an observation. A successful local exercise still leaves scale, failure modes and operational responsibilities outside its conditions.

Assign an owner for each consequential decision: release, stop, recovery, incident communication and acceptance of unresolved risk. A generated runbook can help that person, but it cannot accept responsibility. A process that names an operations phase may still leave these duties to the organization.

The evidence packet should include failure cases as well as the happy path. What happens if a transition cannot persist its audit record? If a migration changes the representation of a policy, how is existing-request behavior checked? If identity or authorization support is unavailable, which operations stop? The exact responses belong in the chosen design and contract before their tests are interpreted.

Operational readiness remains open. The packet identifies the exercises and decisions still needed for the selected environment.

### Rehearse a rollback with data already written

Design a recovery scenario around three records: a pending v1 request from before the rollout, a pending high-risk v2 request with one approval, and an approved v2 request with its complete history. The second record is particularly useful because v1 code that reads it as an ordinary pending request could finalize it under the wrong threshold. Before selecting a rollback mechanism, decide how the older application will treat each record shape and policy version.

One proposed response is to pause decision writes while preserving authorized reads and to repair forward with software that understands both versions. Another possible design is an older release that was deliberately made compatible before rollout. The service contract, deployment architecture and already-written data determine whether either response is available. An operator needs a decision boundary and an observation that tells them which state they are in. Record these conditions before a rehearsal so the reviewer can tell whether the response followed the intended policy.

A rehearsal should check business state after recovery, with pre-change and post-change observations for the same named records. A process health signal can confirm that an endpoint responds. It cannot tell whether the high-risk pending request still has one approval and still requires a second eligible actor. Include an authorized history lookup and an attempted transition under each relevant version in the proposed observation plan. Define who will decide whether writes may resume.

A second rehearsal can address persistence failure during a decision. The release owner needs to know whether the service rejected the action, committed the decision with an authorized delivery state, or entered an inconsistency requiring intervention. Those alternatives depend on the selected architecture. If the case adopts a single durable transaction, the oracle can inspect whether both rows were committed together. If the design adopts separately delivered history, the contract must first define which durable record proves the outcome and how a delayed delivery is represented. Choose the observation to match the design.

### Choose operational signals around the failure you can act on

A rollout dashboard could report accepted requests and decision failures. Add the business interpretation before relying on either. An increase in pending high-risk v2 requests may be normal if the second approver has not acted. The same increase among eligible v1 requests after one recorded approval would warrant a different investigation. The operator needs a way to distinguish policy version and risk under the service's disclosure and data-handling rules.

Design the signal with a response. An unmatched success event and terminal state may warrant pausing the affected action while a reviewer identifies the affected revisions and records. An ordinary rise in denials after an authorization change may call for a fixture-based check of authorized paths. Write the action and its owner alongside the proposed signal, so an alert has a useful disposition. For the book's case these are design candidates that would require actual exercises to support readiness claims.

<!-- C12-S07 -->
## Assemble a release evidence packet

A release evidence packet connects a decision to retrievable facts. Its size should follow the service and risk, but its contents need clear owners and limits. For this case, the proposed packet would contain:

1. Accepted requirements and interface/policy contract, including version binding and exclusions.
2. Exact source/package, application and environment identities, with enabled modules/configuration.
3. Requirement-to-change/check mapping and actual build/test/flow outputs.
4. Review findings, structural/semantic distinctions, human dispositions and interests.
5. Dependency/configuration/secrets assessment with actual scan scope and unresolved issues.
6. Migration, observability, rollback/recovery evidence appropriate to the operational scope.
7. Named acceptance/release authority, explicit remaining risks and stop conditions.

The case packet contains the design, documentary source work and proposed checks described here. No application item can be marked passed. Document integrity checks on the manuscript are a different kind of evidence and must not appear as SaaS acceptance results.

The packet should make disagreement actionable. A reader must be able to identify which requirement or observation blocks acceptance, who can resolve it and what additional evidence is needed. Vague reassurance makes the decision harder to review; an honest Not run makes the next task clear.

### Walk a proposed release decision

Imagine the review packet arrives with three entries. A local check confirms that the policy function counts distinct actors under v2. A service-level probe reports that a foreign request receives the contract's permitted response. The migration rehearsal is marked Not run. The first entry supports the function behavior. The second supports a response observation on the specified path, and its reviewer still needs to confirm whether durable state and history were inspected. The third leaves the behavior of existing requests during rollout open.

A release owner could accept the packet for continued work in a disposable environment and leave authorization for any stateful rollout open. The disposition should identify the missing evidence and the next review trigger. For example, require a rehearsed migration and recovery of a pre-existing v1 request and an in-progress v2 request before the stateful decision returns. Use a named revision and keep the original packet available, so later evidence changes the disposition without erasing how the earlier decision was reached.

If the reviewer requests another check, give that request the same precision as a finding. Identify the requirement, expected observation, fixture and owner. “More security testing” is hard to finish. “Add a foreign-tenant write probe against an existing A request and inspect A's durable state and success history” makes an unresolved claim reviewable. Once the check has run, attach the result and update only the claims it addresses.

### Maintain the disposition after an accepted change

A team can finish one release review and then discover that a dependency fix changed the runtime used in the acceptance environment. Open the packet at the decision that used the old observation. Identify which parts of the review depend on that environment and which remain supported by unchanged inputs. A specification sign-off can remain applicable while a boundary probe needs to be repeated.

Preserve the earlier approval and record the new condition that reopened the decision. For the synthetic service, the reviewer might repeat a tenant-isolation probe and a migration rehearsal if the dependency change affects database access. The release owner can then make a fresh disposition for the candidate that was actually built. The packet becomes a record of decisions over time, with each approval attached to what reviewers inspected.

The same practice helps an incident review. If a rollout exposes a problem despite a favorable packet, find the accepted observation and reconstruct its assumptions. The fixture might have omitted the affected data shape, or the deployed configuration might differ from the checked one. Revise the smallest part of the review that would have detected the gap and record the later exercise that tests that correction.

Chapter 13 uses these distinctions diagnostically. The aim is to recover from a concrete failure without replacing evidence with another status label, and to improve the process only where the observed problem justifies a change.
