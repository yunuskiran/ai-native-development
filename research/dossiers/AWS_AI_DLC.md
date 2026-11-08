# AWS AI-DLC — M2 source dossier

Status: **research-editor extraction; independent technical review pending**. Access: 2026-10-31. This distinguishes lifecycle concepts from a versioned workflow implementation; it is not an AWS service/deployment tutorial. [Claim register](../evidence/CLAIMS.json); [source ledger](../M2_SOURCE_LEDGER.md).

## Identity and concept-to-implementation map

AWS's original article is dated 2025-07-31 and describes inception, construction and operations (A-C01). The inspected AWS Labs Workflows source at `3939a8b9182f2e4153b92028057a7be74e0684c2` describes initialization, ideation, inception, construction and operation (A-C02). Keep both source scopes explicit rather than treating a phase count as timeless or as an implementation defect.

The source README displays `2.11.2`; GitHub's `v2.11.2` tag resolves to `10a9bc9d…`, an earlier commit (V-C01). These notes concern the researched source pin, not asserted contents of release assets. A concrete trial would additionally identify profile, depth, test strategy, guard policy, host and deviations. The original article's linked white paper was not inspected; a complete origin/history dossier remains limited to recorded primary anchors.

## Native workflow and profile boundaries

The phase guide describes routes, unit-level construction and phase-boundary checks. Profile tables exclude three setup stages from their denominator, explaining 30 post-setup vs 33 total stages (A-C02). Construction can use serial unit-major, stage-major or conditional parallel/team paths (A-C06).

Profiles are substantive interventions. Classic and Express differ in included design/operational work, review and ceremony; their guard-policy defaults and overrides are documented (A-C03). A selected hook contains an explicit disable-flag return path (A-C04). This is a static observation of selected code, not a complete enforcement/security audit. A slogan about human oversight cannot substitute for the exact configuration.

## F01–F11 evidence map

All runtime/effectiveness outcomes are **Not assessed**.

| Dimension | Documentary finding or explicit gap | Evidence / qualification |
|---|---|---|
| F01 Decision rights | Approval/plan authority is described, with profile-dependent guard behavior and an explicit bypass setting. | A-C03/A-C04; [A02](../M2_SOURCE_LEDGER.md#m2-a02), L45–L95; [A03](../M2_SOURCE_LEDGER.md#m2-a03), L2391–L2397. Enforcement not executed. |
| F02 Overhead/scale | Profiles intentionally include/omit stages and review depth. | A02 L24–L43/L76–L98. Stage counts are not measured effort or quality. |
| F03 Artifact lifecycle | Intent record contains persistent state/audit/verification and separate transient engine files. | A-C05; [A04](../M2_SOURCE_LEDGER.md#m2-a04), L25–L54. Persistence does not prove correctness. |
| F04 Traceability | Phase-boundary checks are described as detecting missing/orphaned links and inconsistencies. | [A01](../M2_SOURCE_LEDGER.md#m2-a01), L61–L63; artifact records A04. Actual coverage/completeness unassessed. |
| F05 Context | Original concept passes repository context between lifecycle work; implementation stores intent/state records. | A-C01/A-C05. Context relevance and model effects not measured. |
| F06 Solo/team | Source distinguishes solo unit checkpoints, team ownership and parallel execution conditions. | A-C06; A01 L72–L82. No observed organizational benefit established. |
| F07 Brownfield | Reverse engineering is conditionally routed in the profile description. | A02 L38–L43/L82–L85. Full baseline recovery correctness not assessed. |
| F08 Testing | Profiles select different test strategies and reviewer behavior; boundary checks and records are specified. | A02 L24–L36/L54–L63/L82–L95. Actual acceptance/negative checks absent. |
| F09 Operations | Operation appears in the full lifecycle; some profiles leave it a placeholder or omit it. | A01 L42–L45; A02 L45–L52. No deployment/rollback exercise performed. |
| F10 Portability | README describes a harness-neutral core; native engine dependencies differ from the app runtime. | A-C07; [A06](../M2_SOURCE_LEDGER.md#m2-a06), L3–L6/L29–L45. Host equivalence untested. |
| F11 Maintainability | Persistent audit/state and review evidence are designed to survive workflow changes. | A-C05; A04 L18–L54. Longitudinal effect remains unassessed. |

## Case implications and source limitations — analysis

For E1, identify whether a local-only route preserves the required intent/design/acceptance duties. For E3, a focused profile may fit the task, but any differences from E1 are part of the treatment. Do not force every task through the longest route or silently remove operational stages to improve timing. Record all overrides, gates, accepted local substitutes and worker calls.

The [independent-evidence note](../HISTORY_AND_INDEPENDENT_EVIDENCE.md) separates documentary analysis, an affiliated first-hand collaborative-platform account and controlled AI-tool research. None is a controlled head-to-head trial of this source/profile against the other three. A sample platform's incident or timing does not automatically characterize the core workflow engine.

Benefits in the original vendor article remain attributed claims. No universal speed/quality, enterprise-readiness or compliance conclusion is supported by this dossier. The [contested register](../CONTESTED_CLAIMS.md) records configuration and version qualifications needed before prose.

## Rights and review handoff

[A05](../M2_SOURCE_LEDGER.md#m2-a05) identifies MIT-0 in the inspected licence file. This does not clear AWS marks, external figures or an entire specification PDF for reuse. No external service was deployed and no source workflow was installed. Before pilot prose: choose concept/source/profile policy, retain configuration caveats and obtain G2 source review; actual host, model, budget and operational claims await later validation.
