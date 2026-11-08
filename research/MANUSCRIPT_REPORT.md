# Publication preparation — edition 1.1

Completed **2026-11-05**. The book contains **66,497 chapter words**, fourteen chapters and all 95 planned sections. The final copyedit removed 19 words from the preceding 66,516-word manuscript. The planning allocation remains 66,500 words. The author requested completion without further routine questions. Writing, the recorded AI editorial pass and manuscript assembly are complete for this edition.

## Read the book

The [complete manuscript](../manuscript/REVIEW_MANUSCRIPT.md) contains the chapters in the approved order, a linked contents list and the source notes. A typeset reading copy is provided at [Engineering with AI](../output/pdf/engineering-with-ai.pdf). The A4 reading PDF has 141 pages. The paperback interior has 236 pages at 6 x 9 inches. The [publication format check](evidence/PUBLICATION_FORMAT_CHECKS.json) verifies 1,088 long chapter paragraphs in print PDF, reading PDF and EPUB, all print fonts embedded, and 133 internal EPUB references. The [publication review report](../publication/REVIEW_REPORT.md) identifies the source, similarity and editorial scope. The individual chapter files remain editable under `manuscript/pilot/`.

| Chapter | Words | Allocation |
|---|---:|---:|
| C01 | 2,991 | 3,000 |
| C02 | 3,493 | 3,500 |
| C03 | 4,547 | 4,500 |
| C04 | 5,492 | 5,500 |
| C05 | 5,590 | 5,500 |
| C06 | 5,566 | 5,500 |
| C07 | 5,379 | 5,500 |
| C08 | 4,613 | 4,500 |
| C09 | 4,853 | 5,000 |
| C10 | 4,438 | 4,500 |
| C11 | 7,949 | 8,000 |
| C12 | 5,453 | 5,500 |
| C13 | 3,653 | 3,500 |
| C14 | 2,480 | 2,500 |
| **Main text** | **66,497** | **66,500** |

The historical 784-word companion remains separate. Source notes, front matter and companion code are outside the main-text count.

## Content and editorial work

The completion pass added 5,999 net words from the 60,517-word checkpoint. It fills practical gaps in delegation briefs, planning decisions, context recovery, configuration overrides, adapter boundaries, specification maintenance, comparison interpretation, baseline preparation and failure diagnosis. The final application exercises give each chapter a task the reader can inspect or reproduce in their own environment.

The AI editorial pass checked exact paragraph duplication across chapters, repaired premature closing transitions in C04/C09/C12/C14 and reconciled banners and current counts. The method accounts retain their pinned documentary scope. Illustrative exercises and synthetic fixtures are identified in the chapter prose. The [completion checkpoint](evidence/COMPLETION_BASE_2026_11_05.json) preserves the preceding text and manifest.

## Source and execution evidence

The source notes cover 35 cited source records. On November 5, selected AWS profile and AIUP workflow passages were retrieved through the GitHub connector. The [recheck record](evidence/EDITORIAL_SOURCE_RECHECKS_2026_11_05.json) identifies the exact URLs and ranges. It supports the selected profile routing/review configuration and AIUP input/decision-rights/coverage-adapter statements. Historical failed retrievals remain in dated records.

The TypeScript policy model has ten passing sequential checks. Its [registered execution record](evidence/POLICY_MODEL_RUN.json) identifies the original command, runtime and file hashes. A November 4 rerun returned ten passes and zero failures on Node.js v26.13.0. Static type-checking was unavailable in the original run. The example has an intentionally bounded in-memory scope documented in its README.

The case follows the qualitative walkthrough route authorized in A11. Actual framework/application trials remain unperformed. The manuscript reports no comparative productivity or production outcome.

## Reproduce the deliverables

1. Run `python3 scripts/build_review_manuscript.py`.
2. Run `python3 scripts/build_review_manuscript.py --check`.
3. Build the PDF with the bundled Python environment and `scripts/build_book_pdf.py`.
4. Run `python3 scripts/check_manuscript.py`.

The [manifest](evidence/MANUSCRIPT_MANIFEST.json) records input and output identities. The [integrity result](evidence/MANUSCRIPT_DOCUMENT_CHECKS.json) covers registered counts, hashes, titles, section IDs, source-locator bookkeeping, local link paths and original-plan preservation.

## Independent and publication review

Independent technical review, broad passage-to-claim semantic validation, full-book originality/rights review, professional copyedit and final publication approval remain pending. The author manuscript is complete and available for those reviews. G2/G3/G6/G7 dispositions require their stated evidence and approvers. Actual application trials retain the thirteen open readiness checks.

## Publication package

The [store listing](../publication/STORE_LISTING.md) contains the retained title, connected-profile byline Yunus Kiran, description, category candidates and seven keyword fields. The cover uses original AI-designed typography and geometry. The ebook is EPUB 3. The print specification is 6 x 9 inches, black ink and white paper, no interior bleed, with a full-wrap cover calculated from 236 pages.

EPUBCheck 5.4.0 returned zero errors and warnings. Official Kindle Previewer inspection remains open because both the downloaded package and extracted application failed signature verification. The application was not executed. The [status record](evidence/KINDLE_PREVIEWER_STATUS.json) retains the actual result. No independent human review, marketplace upload or GitHub publication occurred in this pass.
