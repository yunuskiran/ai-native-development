# BMAD Method — M2 source dossier

Status: **research-editor extraction; independent technical review pending**. Access: 2026-10-31. This is evidence for chapters 4/8/9, not manuscript prose or an executed evaluation. Claim IDs resolve in the [claim register](../evidence/CLAIMS.json); source IDs link to inspected passages in the [M2 ledger](../M2_SOURCE_LEDGER.md).

## Identity and reproducible scope

Research candidate: `bmad-code-org/BMAD-METHOD`, stable `V6.12` source at `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`. The manifest identifies `6.12.4`; the GitHub release tag resolves to the same commit. Registry contents and installation were not checked (B-C01, V-C01). Main at `61e01f8…` describes v7 as preview; its expired ETA is not evidence of release (B-C08).

This dossier evaluates the inspected stable-source design, with built-in QA distinguished from TEA and other modules. Founder history, first release and a definitive acronym expansion are not established here; a package description alone is insufficient origin evidence.

## Process, artifacts and authority

The planning guide starts from defined intent and permits a small implementation path, specification/story decomposition or broader coordination as needed (B-C02). Build investigates code and upstream records, then distinguishes a light path from designs needing a written plan and human answers/approval (B-C03). It does not prescribe the same ceremony for every change.

`SPEC.md` records intent and success conditions with supporting artifacts; the guide directs changes through `bmad-spec`, preserving capability IDs and optionally producing `stories.yaml` (B-C04). This is a particular maintenance policy, not evidence that all documents are permanent or always loaded. Brownfield guidance explicitly prioritizes current code and archives older greenfield context away from ordinary changes (B-C05).

## F01–F11 evidence map

All effectiveness/runtime outcomes are **Not assessed**. “Documented” below means the selected passage prescribes a mechanism.

| Dimension | Documentary finding or explicit gap | Evidence / qualification |
|---|---|---|
| F01 Decision rights | Flagged designs require answers/plan approval; clear light-path work may proceed without that full checkpoint. | B-C03; [B03](../M2_SOURCE_LEDGER.md#m2-b03), L70–L98. Prompted workflow; enforcement not tested. |
| F02 Overhead/scale | Planning scales with intent; direct low-risk edits are allowed. | B-C02; [B02](../M2_SOURCE_LEDGER.md#m2-b02), L8–L45. No timing claim established. |
| F03 Artifact lifecycle | Spec updates preserve IDs; supporting documents and optional story inventory are linked. | B-C04; [B05](../M2_SOURCE_LEDGER.md#m2-b05), L99–L132. Brownfield archive policy qualifies persistence. |
| F04 Traceability | Capability IDs and parent-spec/story links supply a trace structure. | B-C04, B-C02. End-to-end code/test link correctness and completeness remain unassessed. |
| F05 Context | Fresh Build chat and repository/upstream investigation; compact current project context. | [B03](../M2_SOURCE_LEDGER.md#m2-b03), L31–L34/L70–L75; B-C05. No proven context-quality gain. |
| F06 Solo/team | Committed team overrides and separate personal overrides are documented. | B-C07; [B06](../M2_SOURCE_LEDGER.md#m2-b06), L8–L32. Not observed team collaboration. |
| F07 Brownfield | Existing code/conventions and bounded changes guide work; historical context may be archived. | B-C05; [B04](../M2_SOURCE_LEDGER.md#m2-b04). Preservation behavior not executed. |
| F08 Testing | Built-in generated QA differs from optional TEA; built-in coverage has explicit limits. | B-C06; [B07](../M2_SOURCE_LEDGER.md#m2-b07). Generated tests are not our independent oracle. |
| F09 Operations | Detailed production-operation/rollback governance was not established in the inspected scope. | **Not assessed**; do not translate this gap into a claim that BMAD cannot support operations. |
| F10 Portability | Runs through coding hosts; Build says richer reviewer dispatch benefits from worker/model capabilities. | [B01](../M2_SOURCE_LEDGER.md#m2-b01), L18–L24; B03 L95–L98. Host equivalence not tested. |
| F11 Maintainability | Stable spec IDs, change reconciliation and brownfield context guidance are prescribed. | B-C04/B-C05. Long-term maintainability outcomes not measured. |

## Case implications and tradeoffs — analysis

For the shared TypeScript/Node increment, record the exact path selected, required human answers and whether optional modules are enabled. Do not give BMAD an expanded TEA setup while calling it core, or force full product planning onto a tiny E3 repair. Preserve its native spec/story artifacts rather than substitute AIUP use cases.

Useful test questions: does a light path retain the tenant/self-approval constraints; do stable capability IDs survive E2; does archived greenfield context leave a needed invariant out of reach? These are future evaluation questions, not observed failures. Built-in QA generated from existing implementation needs independent CS acceptance checks.

## Limitations, counterevidence and rights

The method's own planning and QA limits constrain claims of universally beneficial ceremony or comprehensive testing. No controlled BMAD effectiveness comparison was established in this directed search. Source design, source-reported benefits and actual outcomes remain different evidence types.

[B08 licence](../M2_SOURCE_LEDGER.md#m2-b08) and [B09 trademark notice](../M2_SOURCE_LEDGER.md#m2-b09) were inspected. They are source-identification evidence, not per-asset publication clearance. No external prompts, code or diagrams are reproduced in this dossier. Before pilot prose: accept stable-source scope, review the claims/limitations, resolve any intended reuse and complete G2 technical review.
