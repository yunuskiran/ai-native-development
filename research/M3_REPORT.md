# M3 provisional pilot report

Prepared and extended **2026-11-01 (Australia/Melbourne)** under author continuations A08–A10. **Extended pilot v0.3 is written; G2 independent technical review and G3 acceptance remain pending.** A10 adds C02/C03 first drafts at the existing general style. The author's positive initial impression is not detailed acceptance or independent review.

## Actual manuscript delivered

| Artifact | Words | Coverage |
|---|---:|---|
| [Chapter 1 introduction material](../manuscript/pilot/01-the-evolution-of-ai-assisted-development.md) | 1,873 | Six sections: bounded history, delegated work, responsibilities, maintenance example, uncertainty and reading path |
| [Chapter 2 first draft](../manuscript/pilot/02-beyond-vibe-coding.md) | 3,211 | Six sections: working definition, accepted change, compact record, proportionate process, evidence and repeatable habits |
| [Chapter 3 first draft](../manuscript/pilot/03-understanding-ai-driven-methodologies.md) | 4,101 | Seven sections: comparison unit, taxonomy, SDD primer, neutral SaaS, F01–F11, evidence and deep-dive reading guide |
| [Chapter 4 BMAD method sample](../manuscript/pilot/04-bmad-method-deep-dive.md) | 3,254 | Seven sections: pinned scope, planning depth, decision rights, artifacts/context, QA/acceptance, existing code/change and limits |
| [Chapter 10 selection sample](../manuscript/pilot/10-choosing-the-right-methodology.md) | 2,356 | Seven sections: constraints, duties, filtering, four scenarios, adaptation, pilot/exit and decision record |
| [Pilot case companion](../manuscript/pilot/case-walkthrough.md) | 784 | Synthetic approval story, v1/v2 behavior, matched baselines and future evidence boundary |
| **Total** | **15,579** | **14,795 chapter-prose words + 784 companion words** |

These are original English drafts, not expanded abstracts. Five chapter artifacts cover **33 planned sections**. C02/C03 contribute **7,312 new words** and are within 10% below their 3,500/4,500-word planning allocations. C01/C04/C10 remain shorter samples; C04 is not an accepted full-length method chapter. The companion is not chapter 11. No word allocation, chapter title or chapter order changed.

The method sample uses BMAD source `bab9082…`, manifest 6.12.4, for documentary illustration. It distinguishes planning paths, specification ownership, model review and built-in QA from optional TEA. The selection sample offers an original decision-record template and conditional scenarios, rather than a winning-method recommendation. TypeScript / Node.js remains the case technology family; no framework/database/host or run version has been adopted.

## Sources and review

The initial pilot rechecked **13 distinct primary sources on 2026-11-01**. Revision v0.2 added two versioned primary-paper metadata/abstract records and bounded historical claims. The C02/C03 extension adds five existing M2 source records to pilot coverage and supplementary AIUP passage ranges; current prose cites **20 distinct sources**. These counts are not independent studies or full-paper reviews. The [initial receipts](evidence/M3_SOURCE_RECHECKS.json), [v0.2 additions](evidence/M3_REVISION_SOURCES.json) and [foundation source record](evidence/M3_CHAPTER_02_03_SOURCES.json) delimit the inspected scope. M2's historical 57-source/46-claim inventory remains unchanged.

The [initial AI review](M3_PILOT_REVIEW.md) maps assertion groups; the [v0.2 revision](M3_REVISION_REVIEW.md) records seven findings; the [foundation review](M3_FOUNDATION_CHAPTERS_REVIEW.md) checks C02/C03 scope, support and overlap. No runnable application code, generated application artifact, copied prompt, external figure or outside book passage was introduced. Case events and proposed checks are synthetic or future work. C02's empirical statements are explicitly attributed external-study findings, not book-run results. No test, timing, defect-detection or productivity result was invented.

## Revision findings addressed

The main technical correction makes acceptance-table rows independent checks with explicit pending-state and role preconditions. Otherwise a terminal-state denial could falsely appear to establish no self-approval. C01 and C04 now carry the same distinction. The case's overlapping-role actor is also unambiguous.

C01 gains two bounded research anchors; C04 gains a concrete requirement-to-evidence mapping and narrower named-file ownership wording; C10 gains a populated four-candidate decision exercise. Repeated process notices and favorable QA wording were shortened or replaced. The [v0.1 snapshot](evidence/PILOT_V0_1_SNAPSHOT.json) preserves all four prior texts and their manifest/check results.

## Foundation extension under A10

C02 develops proportionate engineering practice through a history increment, compact decision record and a presentation-only repair counterexample. Its operational vibe-coding definition avoids an unverified origin claim. External AI-tool research is used only with its stated conditions and later study-design limits.

C03 establishes the source/profile/operating-condition unit, four-framework/SDD/tool taxonomy, short specification primer, neutral case and shared evidence instrument. It introduces no method score or winner. The old four artifact texts remain unchanged from the [v0.2 snapshot](evidence/PILOT_V0_2_SNAPSHOT.json). Chapters 1–4 now have a consecutive prose sequence; nine chapters remain briefs, with C10 available as a separate sample.

## Verification

Run `python3 scripts/check_pilot.py` from the repository root. The [checker](../scripts/check_pilot.py) verifies artifact hashes/counts, approved titles and section IDs, cited source/range coverage, local Markdown link paths, original-master/outline preservation and the thirteen still-open experiment readiness checks. It does not verify every Markdown anchor, certify source truth, run an application or supply independent review. Exact output is recorded in [M3_DOCUMENT_CHECKS.json](evidence/M3_DOCUMENT_CHECKS.json).

## Remaining work and acceptance

1. A named technical reviewer must complete G2 and review pilot-specific interpretations. The drafting assistant's review does not count as independent human review.
2. Author/editorial review must assess voice, practical depth, repeated case setup and usefulness of the foundation/selection explanations before G3 acceptance. A10 authorized only the completed C02/C03 extension, not all remaining chapter work.
3. Broader C01 history, lawful full-book originality review, source-versus-release/GSD edition decisions and adapter compatibility remain evidence/edition work. The public Apress metadata was not mistaken for a full-text comparison.
4. The executable case still needs a chosen stack/host/model, frozen contract/baselines, independent oracle, approved resources and readiness disposition. The present walkthrough supplies no benchmark observations.

The original master and fourteen-title outline are preserved. Gates, roadmap, decision log, word budget, open questions and task register now distinguish provisional prose from accepted manuscript and experimental evidence. No payments, deployment or publication occurred.

**M3 EXTENDED PILOT v0.3 PREPARED — G2/G3 HUMAN REVIEW PENDING.**
