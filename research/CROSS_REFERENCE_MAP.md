# Chapter ownership and cross-reference map

Status: **M1 scope proposal**, 2026-10-31. Preserves the author's fourteen titles/order. Section IDs resolve to the [chapter plan](CHAPTER_PLAN.json) and the planned-section tables in each brief. These references are planning targets, not links to written chapter prose.

## Concept ownership and repetition control

| Concept | Primary home / section | Earlier/later references and boundary |
|---|---|---|
| Historical evolution | [C01](../chapter_briefs/01-the-evolution-of-ai-assisted-development.md#planned-sections), C01-S01/S02 | C02 may refer to the transition; C14 distinguishes history from forecast. No repeated tool timeline. |
| Accountable, proportionate engineering | [C02](../chapter_briefs/02-beyond-vibe-coding.md#planned-sections), C02-S02–S04 | C04–C07 use the tiny-change question; C13 diagnoses failures instead of repeating the framing. |
| Method/approach/tool taxonomy | [C03](../chapter_briefs/03-understanding-ai-driven-methodologies.md#planned-sections), C03-S01/S02 | Methods state their own boundary once. Tool examples do not become peer chapters. |
| Comparison questions and evidence types | [C03](../chapter_briefs/03-understanding-ai-driven-methodologies.md#planned-sections), C03-S05/S06 | Method chapters apply questions; C09 synthesizes evidence; C10 makes scenario decisions. |
| BMAD source/profile and artifact trail | [C04](../chapter_briefs/04-bmad-method-deep-dive.md#planned-sections), C04-S01–S07 | C08–C11 reference artifacts without retelling setup or method background. |
| GSD lineage/context/handoffs | [C05](../chapter_briefs/05-gsd-deep-dive.md#planned-sections), C05-S01–S07 | C08/C09 use qualified policy/evidence; product distinction is not a separate product review. |
| AI-DLC concept/profile mapping | [C06](../chapter_briefs/06-aws-ai-dlc-deep-dive.md#planned-sections), C06-S01–S07 | C09/C12 retain profile and local/team limits; do not blend source eras. |
| AIUP owned use-case artifacts/adapters | [C07](../chapter_briefs/07-ai-unified-process-deep-dive.md#planned-sections), C07-S01–S07 | C08/C09 compare on equal terms; no borrowed tutorial/sample application. |
| Full SDD lifecycle lens | [C08](../chapter_briefs/08-spec-driven-development-as-an-approach.md#planned-sections), C08-S02–S06 | C03-S03 supplies only the prerequisite primer. C04–C07 show native artifacts; they do not repeat the full taxonomy. |
| Comparative findings and uncertainty | [C09](../chapter_briefs/09-comparing-the-methodologies.md#planned-sections), C09-S02–S06 | C10 cites supported tradeoffs; no duplicate tables with different unexplained ratings. |
| Scenario choice/adoption/exit | [C10](../chapter_briefs/10-choosing-the-right-methodology.md#planned-sections), C10-S01–S07 | C09 avoids recommending a universal winner. C14 adds triggers to revisit the decision. |
| Neutral SaaS requirements and complete records | [C11](../chapter_briefs/11-real-world-case-study-building-a-saas.md#planned-sections), C11-S01–S08 | C03-S04 introduces the business problem; C04–C07 use a bounded slice. C09 can forward-reference records without duplicating them. |
| Verification, security and operations evidence | [C12](../chapter_briefs/12-testing-security-and-production-readiness.md#planned-sections), C12-S01–S07 | Minimum obligations introduced in C02/C03 and applied from the first example. Their late chapter placement never defers actual checking. |
| Failure diagnosis and recovery | [C13](../chapter_briefs/13-common-failures-and-anti-patterns.md#planned-sections), C13-S01–S07 | C02 frames discipline and C12 owns checks; C13 adds symptoms, causes, evidence and remedies. |
| Future scenarios and reevaluation | [C14](../chapter_briefs/14-the-future-of-ai-native-engineering.md#planned-sections), C14-S02–S06 | Do not insert forecasts as present evidence in earlier method chapters. |

## Dependency and forward-reference policy

Definitions needed to read a chapter must appear earlier. A forward reference may supply depth or the full evidence record, but never the first explanation of a necessary term. This handles the author's chosen placement of SDD in chapter 8 and the full SaaS case in chapter 11 without moving either.

Core reading path: C01 → C02 → C03 → C04–C07 → C08 → C09 → C10 → C11 → C12 → C13 → C14. Method chapters share C03's questions but do not depend on reading one peer as the default process. C09 can compare completed M2 dossiers even when M4 outcomes are unavailable; it must mark outcomes Not assessed. If experiments exist, C09 points to C11's full records, while defining its own comparison logic.

Editing rule: when a passage re-explains an owned concept beyond a brief prerequisite reminder, move/shorten it or justify the exception in the brief. A necessary example may recur with a new analytical question, but copy/pasted narrative is not a new treatment.

## Shared increment map

| Appearance | What the reader sees | What remains elsewhere |
|---|---|---|
| C03-S04 | Tenant-scoped business problem, actors and neutral acceptance intent | Full CS inventory/interface/fixtures in C11. |
| C04–C07 | Native questions, decisions and artifacts for the same E1 slice | No four full application tutorials. |
| C08-S05 | How E2 changes persistent specifications and code-edit policy | Full seed/changes/check records in C11. |
| C09 | Evidence-qualified comparison of the shared work | No invented outcomes or hidden unequal baselines. |
| C10 | A conditional selection record using the project's constraints | Not a claim that a method already won the case. |
| C11 | Full E1/E2/E3 requirements, procedure, records and rerun guide | Broad verification principles consolidated in C12. |
| C12–C13 | Review boundaries and diagnostic/recovery lessons grounded in actual or labeled illustrative evidence | No fabricated incidents or production history. |
