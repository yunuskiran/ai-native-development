# 12. Testing, Security & Production Readiness

Status: **M1 ARCHITECTURE BRIEF — NOT MANUSCRIPT**. Author-supplied title/order preserved. Chapter ID: C12. Approved planning allocation: **5,500 words**. M1 architecture accepted by the author on 2026-10-31; factual support still requires M2 evidence gates.

## Reader question

What evidence is needed to accept AI-assisted changes and judge readiness beyond a working local demonstration?

## Reader outcomes

- Distinguish generated tests from an independently reviewed acceptance oracle.
- Specify evidence for tenant/authorization/change boundaries without equating a passing suite with assurance.
- Separate local demonstration, operational exercises and actual production claims.

## Scope and dependencies

Own consolidated verification/security/operations evidence. Exclude framework-specific security tutorials, blanket certification, live deployment instructions and C13's detailed failure taxonomy.

Prerequisites: Acceptance obligations introduced in C02/C03 and applied in C04–C11; authoritative technical/security sources and actual runnable examples require M2/M4 validation.

## Proposed abstract

This chapter will consolidate verification duties that apply throughout the book rather than introduce testing after the case is complete. It will separate generated tests, independent acceptance checks, source-to-test traceability and human review. The SaaS tenant and approval boundaries will ground threat questions, negative cases and change safety, while operations coverage will distinguish a plan from demonstrated deployment and recovery. Readers will see how to assemble an evidence packet and identify unresolved risks. No checklist will be presented as security certification or proof of production reliability.

## Planned sections

| Section ID | Section | Purpose / evidence-bearing example |
|---|---|---|
| C12-S01 | Define acceptance and evidence ownership | Identify who decides expected behavior and how disagreements are adjudicated. |
| C12-S02 | Use generated tests without circular validation | Separate generated implementation/tests from frozen independent checks and mutation/negative evidence where justified. |
| C12-S03 | Trace requirements through changes | Inspect valid links and regressions rather than trust coverage assertions. |
| C12-S04 | Examine the SaaS boundaries | Plan tenant, role, self-approval, concurrency, audit and data-disclosure threat questions. |
| C12-S05 | Review dependencies, configuration and secrets | Specify review evidence and exact-version records; do not imply scans are comprehensive proof. |
| C12-S06 | From local evidence to operations | Separate observability, migration, rollback and recovery plans from actual exercised behavior. |
| C12-S07 | Assemble a release evidence packet | Summarize open risks, approvals and stop conditions under a defined assurance scope. |

## Artifacts and evidence needs

Original case threat-boundary model, acceptance-evidence checklist and proposed release evidence packet.

M0 does not supply a completed security dossier. M2 must inspect current primary technical/security guidance for selected components; M4 needs actual tests/build/scan/flow records and independent review. Regulatory and production assurance remain outside unobserved scope.

Source IDs refer to the [M0 source ledger](../research/SOURCE_LEDGER.md). They are research leads, not completed M2 dossiers. F01–F11 refer to the [comparison framework](../COMPARISON_FRAMEWORK.md). No benchmark outcomes or accepted implementation are implied.

## Handoffs and acceptance

C13 diagnoses failures using these checks; C10 may forward-reference this chapter when scenarios require stronger evidence.

Brief acceptance: one distinct reader question, outcomes and exclusions; 7 planned sections; original example/artifact role; explicit evidence gaps; coherent handoffs and proposed budget. Chapter prose requires later authorization and source/technical review.

