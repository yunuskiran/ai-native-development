# Cross-method documentary comparison

Prepared: **2026-11-01**; source snapshot **2026-10-31**. This compares inspected mechanisms, not measured outcomes. Source/claim locators are in the [M2 ledger](M2_SOURCE_LEDGER.md) and [claim register](evidence/CLAIMS.json). The four [dossiers](dossiers/BMAD.md) distinguish documented mechanisms from gaps. No numeric scores, weighted totals or universal winner are assigned.

## Unit and evidence limits

BMAD uses the stable-source pin matching tag 6.12.4. GSD Core and AWS Workflows use later source commits than their same-version release tags. AIUP uses a marketplace source pin with a Node component manifest different from its latest component release. These are research subjects, not approved run versions; see V-C01/V-C02 and [snapshot policy](CONTESTED_CLAIMS.md).

All execution, overhead, productivity, quality, security and longitudinal outcomes below remain **Not assessed**. “Gap” means the inspected scope did not establish the mechanism; it does not mean the method lacks it. Same terminology or artifact counts do not establish equivalent scope.

## F01–F11 synthesis

| Dimension | BMAD stable source | GSD Core source | AWS Workflows source | AIUP core / Node path |
|---|---|---|---|---|
| F01 Decision rights | Light vs flagged-plan paths; human answers/approval when flagged (B-C03). | Discussion choices and human UAT; enforcement untested (G-C02/G-C05). | Profile/config-dependent gate and guard policy; disable branch inspected (A-C03/A-C04). | Explicit layered-stack rights; combined Node restrictions separately scoped (U-C02/U-C07). |
| F02 Overhead/scale | Intent-sized planning; trivial edits may skip process (B-C02). | Bounded phases and quick-path advice; no effort measurement (G01 L77–L90). | Profiles deliberately vary route/test/review depth (A-C03). | Durable artifacts documented; tiny-task cost/minimal path not established (U-C01, gap). |
| F03 Artifacts | Stable capability IDs/spec updates; old greenfield context may be archived (B-C04/B-C05). | Persistent phase/state records and phase archive (G-C02). | Persistent intent/state/audit versus transient engine data (A-C05). | Persistent specs and downstream reconciliation (U-C01/U-C08). |
| F04 Traceability | Capability/story links; completeness not tested (B-C04). | Requirement/decision verification described (G01 L53–L55). | Phase-boundary link checks described (A01 L61–L63). | Identifier/marker chains; adapter-specific audit differences (U-C01/U-C06). |
| F05 Context | Fresh Build session, repository investigation and compact current context (B03/B04). | Fresh workers and durable file state; quality benefit is a claim (G-C07). | Repository/intent/state context across work (A-C01/A-C05). | Linked construction inputs and owned specifications (U01 L319–L337). |
| F06 Solo/team | Shared and personal overrides documented; team outcomes unobserved (B-C07). | Agent-role coordination documented; human-team outcomes unobserved (G01). | Solo/team unit paths and conditional parallelism documented (A-C06). | Artifact roles and team decision records documented; team outcomes unobserved (U-C01/U-C02). |
| F07 Brownfield | Existing-code-first guidance and context archive policy (B-C05). | Change/repair guidance; full baseline recovery not reviewed (gap). | Conditional reverse-engineering route; correctness untested (A02). | Reverse-engineered proposed baseline and in-place Node reconciliation (U-C08/U-C07). |
| F08 Testing | Built-in generated QA vs separate TEA, with stated limits (B-C06). | Human UAT, optional code review and stale-verdict checks (G-C05/G-C06). | Profile-dependent tests/review/checks; no acceptance run (A-C03). | Deterministic spec lint vs semantic advice; Node audit limitation (U-C03/U-C06). |
| F09 Operations | Comprehensive operational governance not established (gap). | PR/shipping preflight documented; production operations not established (gap). | Operation phase present in full routes; omitted/placeholder in some profiles (A01/A02). | Acceptance/release documents present; full production operation not established (U-C09, gap). |
| F10 Portability | Coding-host/reviewer capabilities and installer dependencies matter (B01/B03). | Multiple documented hosts with unequal hooks and runtime discrepancy (G-C03/G-C04). | Harness-neutral core claim; native engine separate from app runtime (A-C07). | Core artifacts portable in design; Node adapter assumes a specific stack (U-C04). |
| F11 Maintenance | Stable IDs, spec updates and existing-code guidance (B-C04/B-C05). | Persistent state and verification staleness policy (G-C06). | Audit/state lifecycle records; longitudinal benefit untested (A-C05). | Spec-led changes and in-place reconciliation; long-term alignment untested (U-C07/U-C08). |

Short source labels refer to `M2-` entries in the ledger; claim IDs refer to the extracted register. Each dossier supplies the fuller source scope and exceptions.

## Selection implications — editorial analysis

Documentary evidence supports asking conditional questions, not choosing a winner. For a tiny repair, compare the smallest prescribed path. For a long-lived domain, inspect who maintains behavioral specifications and resolves conflicts. For a team, inspect decision ownership and actual human wait/coordination evidence. For a controlled case, first establish equal application/host/model conditions and distinguish required core from optional add-ons.

The most consequential confounders identified here are source-vs-release drift, GSD runtime/host variation, AWS profile/guard settings, and AIUP adapter-specific automation/stack assumptions. None is converted into an intuitive penalty or performance score. A future execution may strengthen, weaken or contradict these design expectations.

Chapter 9 can use this matrix only with source qualifiers and G2 review. Chapter 10 should use supported constraints and uncertainties in scenarios. Chapter 11 still needs an approved protocol and actual records, or an explicit walkthrough label; this table supplies no benchmark results.
