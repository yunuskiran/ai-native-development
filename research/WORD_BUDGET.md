# Proposed word budget

Status: **M1 PLANNING BUDGET ACCEPTED BY THE AUTHOR**, 2026-10-31, decision A06. These are planned manuscript allocations, not drafted or measured chapter lengths. The author's fourteen titles/order are unchanged. Later reallocations must follow change control.

## Chapter allocations

| Chapter | Title / architecture brief | Target words | Editorial purpose |
|---|---|---:|---|
| 1 | [The Evolution of AI-Assisted Development](../chapter_briefs/01-the-evolution-of-ai-assisted-development.md) | 3,000 | Bounded history; avoid a product catalog. |
| 2 | [Beyond Vibe Coding](../chapter_briefs/02-beyond-vibe-coding.md) | 3,500 | Practical discipline with a tiny-change counterexample. |
| 3 | [Understanding AI-Driven Methodologies](../chapter_briefs/03-understanding-ai-driven-methodologies.md) | 4,500 | Taxonomy, instrument and brief case prerequisites. |
| 4 | [BMAD Method — Deep Dive](../chapter_briefs/04-bmad-method-deep-dive.md) | 5,500 | Equal allocation for a method-specific account with common evidence obligations. |
| 5 | [GSD — Deep Dive](../chapter_briefs/05-gsd-deep-dive.md) | 5,500 | Equal allocation for a method-specific account with common evidence obligations. |
| 6 | [AWS AI-DLC — Deep Dive](../chapter_briefs/06-aws-ai-dlc-deep-dive.md) | 5,500 | Equal allocation for a method-specific account with common evidence obligations. |
| 7 | [AI Unified Process — Deep Dive](../chapter_briefs/07-ai-unified-process-deep-dive.md) | 5,500 | Equal allocation for a method-specific account with common evidence obligations. |
| 8 | [Spec-Driven Development as an Approach](../chapter_briefs/08-spec-driven-development-as-an-approach.md) | 4,500 | Full cross-cutting SDD treatment. |
| 9 | [Comparing the Methodologies](../chapter_briefs/09-comparing-the-methodologies.md) | 5,000 | Evidence synthesis, separate from selection. |
| 10 | [Choosing the Right Methodology](../chapter_briefs/10-choosing-the-right-methodology.md) | 4,500 | Conditional decisions and adoption/exit rules. |
| 11 | [Real-World Case Study: Building a SaaS](../chapter_briefs/11-real-world-case-study-building-a-saas.md) | 8,000 | Complete original case and reproduction account. |
| 12 | [Testing, Security & Production Readiness](../chapter_briefs/12-testing-security-and-production-readiness.md) | 5,500 | Consolidated verification and operational boundaries. |
| 13 | [Common Failures and Anti-Patterns](../chapter_briefs/13-common-failures-and-anti-patterns.md) | 3,500 | Diagnosis and recovery without repeating foundations. |
| 14 | [The Future of AI-Native Engineering](../chapter_briefs/14-the-future-of-ai-native-engineering.md) | 2,500 | Qualified future scenarios and reevaluation. |
| **Main text** | **14 chapters** | **66,500** | Accepted planning target; not a completed manuscript length. |
| Appendices | Dated setup/snapshot notes, blank instruments and glossary | 3,500 | Larger runnable code stays outside the text if later authorized. |
| Front/back matter | Preface, how to use the book and acknowledgments | 2,000 | Bibliography and index excluded from this allowance. |
| **Planned total** | **Main text + allowances** | **72,000** | No print-page estimate or production promise. |

## Counting and change policy

Count original prose, list/table text and captions. Track code separately; bibliography/index and companion code are outside the target. Architecture briefs and their abstracts are planning artifacts, not chapter manuscript. The machine-readable [chapter plan](CHAPTER_PLAN.json) records the same allocations and stable section IDs.

For developmental editing, a chapter may vary by roughly 10% before an explicit rebalance is proposed. This is a proposed tolerance, not permission to silently increase scope. Maintain equal evidence obligations for chapters 4–7 even if their final lengths differ. Do not pad a shorter well-supported method account or invent claims to meet an allocation.

Review tradeoffs: chapter 11 has the largest allocation because it owns full requirements, three episodes, failure evidence and reproduction; chapter 3 gives prerequisites without stealing the full case/SDD treatment. Chapters 9 and 10 have separate analytical and decision jobs. A 72,000-word plan can still be too broad if full tutorials creep in; the cross-reference map controls duplication.

Author disposition: primary audience, overall planning length and relative allocations accepted with M1 in A06. No chapter-count or title change is proposed. Planned word targets remain distinct from actual manuscript lengths.

## M3 actual draft counts — v0.3, 2026-11-01

| Artifact | Pilot words | Full chapter planning allocation |
|---|---:|---:|
| C01 introduction material | 1,873 | 3,000 |
| C02 first draft | 3,211 | 3,500 |
| C03 first draft | 4,101 | 4,500 |
| C04 BMAD method sample | 3,254 | 5,500 |
| C10 selection sample | 2,356 | 4,500 |
| **Chapter prose** | **14,795** | **21,000 across these five chapters** |
| Case companion | 784 | Outside chapter totals until incorporated and deduplicated |
| **Extended pilot delivery** | **15,579** | **Not the manuscript completion count** |

Counts include original headings, prose and table/list text; exclude review banners, HTML section markers, Markdown link destinations and table separators. No executable code or separate bibliography is present. The [checker](../scripts/check_pilot.py) and [manifest](evidence/PILOT_MANIFEST.json) make this convention reproducible. Samples are deliberately below final allocations; expansion must add justified substance, not padding.

Historical [v0.1](evidence/PILOT_V0_1_SNAPSHOT.json): 7,721 words; [v0.2](evidence/PILOT_V0_2_SNAPSHOT.json): 8,267 words. C02/C03 add 7,312 words under A10. They are within 10% below their planning allocations; chapter acceptance and any later rebalance remain separate. No approved allocation changed.

## Current complete chapter sequence — A11 development, 2026-11-02

At the superseded editorial checkpoint, all fourteen chapters had provisional prose totaling **60,517 words**, plus the historical 784-word companion. The approved main-text allocation remains **66,500 words**. That checkpoint retained a **5,983-word gap**, subsequently closed in edition 1.0. The first-pass checkpoint preserves 34,114 words; the [case/selection pass](DEVELOPMENT_PASS_2026_11_02.md) adds 5,717 words and the [method pass](METHOD_DEPTH_REVIEW_2026_11_02.md) adds 5,197. The two Nov 4 passes add 9,689 and 5,856 words respectively. Per-chapter counts are in the [current report](MANUSCRIPT_REPORT.md) and [manifest](evidence/MANUSCRIPT_MANIFEST.json).

Source notes and example code are outside main-text prose. The separate local policy model has ten passing checks but supplies no framework/application benchmark or justification to fill word targets with invented evidence. Full-length acceptance remains open.


## Completed author manuscript — 2026-11-05

Edition 1.0 contains **66,516 main-text words** against the **66,500-word** allocation. The writing allocation is met. The historical companion contributes 784 additional words outside the main text. Final counts are recorded in the [manuscript report](MANUSCRIPT_REPORT.md) and [manifest](evidence/MANUSCRIPT_MANIFEST.json). Independent and publication review remain pending.
