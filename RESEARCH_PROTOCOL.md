# Research protocol

Status: **M1 proposed operating protocol**, 2026-10-31. Applies to subsequent research and drafting after the relevant milestone authorization. Existing M0 records retain their actual inspection limits; this document does not retrospectively validate them.

## Research questions

For each selected method/profile, establish what initiates work, who decides, which artifacts are required, how context persists, how changes are verified, how existing code and operations are handled, what may be omitted and what the method explicitly does not cover. Compare mechanisms separately from outcomes. Search for counterexamples, small-task overhead, maintenance failures and incomplete evidence as well as favorable reports.

The comparison unit is **method source/version + implementation profile + host/model configuration + task + operating conditions**. Do not use a product name as a sufficient experimental specification. Four named frameworks are in scope; SDD is a cross-cutting analytical lens.

## Source strategy and search record

1. Start with creator/maintainer documentation, pinned source, versioned specifications and original announcements. Trace links to the canonical destination rather than treating search snippets as proof.
2. Seek independent primary research and first-hand field reports with disclosed tasks, operators, versions, failures and resource use. A publisher or maintainer can establish its own intended process but not independently verify its effectiveness.
3. Inspect relevant passages directly. Record query, date, inclusion reason, access result and exact inspected scope in the ledger/dossier. Exclude marketing-only comparisons from outcome synthesis; retain them as claims when relevant.
4. For books, inspect lawful publisher descriptions/contents first. Use lawful full-text access only when available; never infer uninspected content or reproduce complete external works.
5. When browsing is unavailable or retrieval fails, label affected claims **NOT VERIFIED IN THIS SESSION**, record the failed route and continue with accessible evidence. A successful alternative must be identified separately.

M2 must review the adjacent comparative paper beyond its abstract before relying on its rubric or findings. The existing [ledger](research/SOURCE_LEDGER.md) is the starting point, not an exhaustive literature search.

## Claim record and evidence types

Each substantive factual or evaluative claim gets a stable ID, proposed wording, chapter/section, source ID and URL, passage locator, source author/publisher, publication/update/access dates, version/commit, inspected scope, evidence type, conflict-of-interest note, counterevidence, confidence and reuse limits. Compound claims must be split when different evidence supports their components.

| Evidence type | Allowed conclusion | Prohibited shortcut |
|---|---|---|
| Documented design | A defined source/profile prescribes a mechanism or artifact | “The mechanism always works” from a README alone |
| Interested-party outcome claim | The identified party reports or promises an outcome | Presenting it as independently measured fact |
| First-hand field observation | Specific observers report behavior in disclosed conditions | Generalizing across teams, models or versions without support |
| Controlled observation | A predeclared procedure produced recorded outcomes | Hiding failures, confounders or changes to the protocol |
| Editorial analysis | Our reasoning from cited premises and stated assumptions | Passing judgment off as a source's finding |
| Forecast / hypothesis | A possible future or testable proposition | Reporting a projection as current capability |

Confidence concerns support for the exact claim: high (direct, well-defined passage/record), moderate (direct but incomplete context), low (limited evidence). Confidence is not a method quality score. Independence, completeness and runtime validation are separate fields.

## Verification states

- **Inspected:** stated material examined; full-site reading and execution not implied.
- **Supported for stated scope:** the record supports the precise, bounded claim after review.
- **Contested:** credible evidence conflicts; preserve both and describe the disagreement.
- **Pending verification / NOT VERIFIED IN THIS SESSION:** source or claim not adequately inspected. This does not mean false.
- **Not assessed:** a comparison dimension has insufficient evaluation evidence.
- **Superseded:** retain the old record with its version/date; link the replacement rather than overwrite history.

“Not documented in inspected passages” is not equivalent to “not supported by the method.” Never replace missing evidence with a zero score.

## Snapshots, updates and reproducibility

Pin repository claims to immutable commits and include package/plugin versions when applicable. A source manifest does not prove registry publication or installed contents. Record mutable-page access dates and permitted short evidence receipts/hashes when later research is authorized. Record exactly which passages were inspected; external links inside a retrieved README are not inspected automatically.

M0 snapshots are candidates dated 2026-10-31, not assertions of the latest release. M2 must reconcile method/profile provenance and Node.js/TypeScript compatibility using current primary documentation before any run freeze. Exact model revisions/settings exposed by providers, run dates and version uncertainty must be recorded. Use a new experimental block when material drift prevents pooling outcomes.

Freeze claims for an edition only after author/reviewer disposition. Material later changes get dated notes or an appendix and a decision-log entry. No silent rewrite of the comparison or experimental intervention.

## Citation, originality and reuse controls

Cite the original source for external terminology, figures, historical assertions and factual claims. Preserve each source's access/quotation constraints; use independent summaries and short necessary quotations with locators. Attribution does not establish permission. Before reusing code, prompts, artwork, logos or figures, inspect the applicable licence/NOTICE/trademark terms and record the intended use. Permission status remains pending until actual review; this protocol supplies no legal clearance.

Maintain per-asset provenance for original diagrams, fixtures and examples. Distinguish prior ideas from our comparison instrument. A different case domain or new title does not establish whole-book originality. Keep a full-text review route and independent technical/editorial review visible in the gates.

## Dossier acceptance and milestone boundaries

Each M2 method dossier must cover identity/history, chosen version/profile, terminology, decision rights, artifact lifecycle, workflow/variants, testing/operations, project fit, limitations, controversies, implementation/tool boundaries and unresolved claims. Every comparison-framework row needs evidence or an explicit gap, plus at least one serious attempt to find counterevidence. A second AI role is a review pass, not independent human validation.

The technical reviewer verifies dossier support before method-specific prose is treated as fact-checked. M3 pilots may expose questions; they do not authorize M4 measurement. The [quality gates](QUALITY_GATES.md) identify approvers and required records. No source, chapter or experiment is “complete” merely because a template is filled.
