# SDD and implementation context — M2 evidence note

Status: research-editor synthesis; technical review pending. Access: 2026-10-31. Four frameworks remain peer coverage; SDD is cross-cutting, with chapter 8 as its full treatment. [Claims](evidence/CLAIMS.json); [sources](M2_SOURCE_LEDGER.md).

## What the terminology supports

Attribute the spec-first, spec-anchored and spec-as-source lens to Böckeler's analysis rather than present it as a universal standard or our invention (S-C01, [W03](M2_SOURCE_LEDGER.md#m2-w03)). The patterns distinguish when specifications are used, whether retained and what humans edit. They are not an effectiveness ranking. Source-era judgments about particular tools do not establish their current behavior.

AIUP's spec-anchored description is self-classification, not demonstrated alignment (S-C02, [W02](M2_SOURCE_LEDGER.md#m2-w02)). Its interpretation of spec-first as discarded material should not silently narrow every author's usage of that label. Record each source's retention and change policy explicitly.

## What the four source snapshots actually document

| Framework scope | Evidence of policy | What may be said / limit |
|---|---|---|
| BMAD stable | B-C04/B-C05: stable spec identifiers, skill-mediated updates and brownfield prioritization of current code | A retained epic/spec contract is documented, but do not label all BMAD artifacts permanent. Archiving historical planning context qualifies blanket spec-persistence claims. |
| GSD Core research pin | G-C02/G-C06: native phase/state records and verification staleness checks | Durable process/context evidence is documented. A phase plan is not automatically a maintained domain specification for the life of the product. |
| AWS Workflows research pin | A-C05: intent state, audit and verification records | Persistent lifecycle evidence is documented. That alone does not settle long-lived behavioral-spec ownership or regeneration policy. |
| AIUP core + Node combined adapter | U-C07/U-C08: specification-led in-place changes; U-C06 limits adapter coverage automation | Persistent behavioral specifications are a documented design. Guaranteed drift prevention or identical automation across adapters is unsupported. |

These are descriptions of mechanisms, not experimentally established SDD classifications. None is assigned spec-as-source merely because it generates code. A specification that directs a model is not necessarily an executable specification; an actual mechanical validation path must be identified.

## Tools as context, with scope discipline

Spec Kit and OpenSpec retain their M0 introductory records S14/S15: both have process content, and neither was deeply re-audited for current feature coverage in M2. Their exclusion from main method chapters follows the author scope, not a claim that they are merely editors.

Kiro's official docs show a product's specification artifacts and surface-dependent workflow capabilities ([W12](M2_SOURCE_LEDGER.md#m2-w12)). This supports an implementation example, not treating the IDE as a fifth methodology. Agent Skills and Task Master-specific capabilities beyond the M0 leads remain **NOT VERIFIED IN THIS SESSION**.

## Writing and experiment consequences

Chapter 3 should introduce enough policy vocabulary for chapters 4–7; chapter 8 compares these policies with source qualifiers. The E2 policy change should inspect ownership, stable links, reconciliation and disagreement rather than count Markdown files. Method-native artifacts remain allowed; no common AIUP template is imposed on peers. Exact SDD placement may stay Not assessed when a selected profile's maintenance policy is unresolved.
