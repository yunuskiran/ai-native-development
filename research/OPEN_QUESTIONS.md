# M0 open questions and author decisions

Status: **Decision register with current A11 dispositions**, updated 2026-11-02. The author accepted M1 architecture in A06 and authorizes autonomous research, drafting and reversible editing in A11. W04 selects contemporary Core for GSD prose and the qualitative case route. These working decisions require no repeated approval. Installed versions, technical validation and execution resources remain open where a later run depends on them. See the [decision log](DECISION_LOG.md); older dated dispositions below retain their historical scope.

## Decisions and current disposition

| ID | Decision / conflict | Recommendation for review | What it unblocks / acceptance evidence |
|---|---|---|---|
| D01 | Missing planning documents and their authority | **Prepared under M1 authorization:** new root brief/protocol/framework/case/gates/source-index/roadmap are labeled M1 drafts; original master remains in `docs/`. No `AGENTS.md` was supplied or fabricated. | Reconstruction/layout is a reversible working convention; no claim of recovering missing originals. Future originals must be reconciled explicitly. |
| D02 | Does “GSD (Get Shit Done)” mean historical framework behavior or the current Core continuation? | **Working prose scope resolved in W04:** contemporary Core, with historical naming and migration qualifiers. Exclude Pi as a peer arm. | Exact installed package/profile remains unfrozen for experiments; complete origin/ownership history is not established. [Sources](SOURCE_LEDGER.md#s03--former-gsd-framework-repository-migration-notice) |
| D03 | Which research/experiment snapshots represent the methods? | Start version evaluation with BMad stable source `6.12.4`, GSD Core source `1.19.0`, AWS Workflows README `2.11.2`, AIUP pinned marketplace; treat all as candidates only. | Author accepts stable/preview policy and original-vs-current AWS mapping; exact package and plugin pins validated before M4. [Ledger](SOURCE_LEDGER.md) |
| D04 | SDD and implementation context within the supplied structure | **Structural direction recorded:** four framework deep dives, dedicated SDD chapter 8, tools as context. M1 proposes a short prerequisite primer in chapter 3; no fifth trial arm. | Scope notes and taxonomy wording are ready for review, without changing chapter titles/order. [Map](CROSS_REFERENCE_MAP.md) |
| D05 | Audience, depth, length and chapter boundaries | **Accepted in A06:** practicing engineers/leads/architects; 66,500-word main text, 72,000 with allowances; fourteen briefs and scope boundaries. | Architecture choice resolved. Use [BOOK_BRIEF.md](../BOOK_BRIEF.md) and [WORD_BUDGET.md](WORD_BUDGET.md); changes need explicit change control. |
| D06 | Case domain and implementation choices | **Design accepted in A06:** synthetic tenant-scoped vendor-access approvals using TypeScript / Node.js, as specified in the M1 design. | Domain/design direction resolved. Framework, database, exact runtime/compiler, host/model, adapters and technical/freeze review remain open; no application or tested baseline exists. |
| D07 | Controlled trial or qualitative walkthrough? No resources, host or model access established. | **Working route resolved in W04:** an explicitly qualitative walkthrough. A stronger measured comparison needs the readiness gate, credible controls and replication. | No fictional runs are needed to finish documentary drafting. Host/model, run/time/spend ceilings and independent checks must be settled before any later measured exercise. |
| D08 | Inference and scoring policy | Master's evidence rule is operationalized in the [comparison framework](../COMPARISON_FRAMEWORK.md): conditional fit, no universal winner or intuitive numeric scores; one-case outcomes remain bounded. | Instrument ready for review; any future numerical rubric/causal inference requires adequate predeclared design, not author preference alone. |
| D09 | Who supplies independent review and declares interests? | Name an outside technical reviewer and an author conflict-of-interest disclosure, including method/community ties if any. | Named reviewer or transparent plan; do not treat simulated editorial roles as independent validation. |
| D10 | Can the author supply lawful access to the Apress full text, or is public-scope positioning sufficient for M1? | Public-scope comparison is sufficient to plan; reserve a full originality/permissions review before drafting and release. | Author records access/review route and confirms no claim of whole-book independence has yet been established. [Positioning](COMPETITOR_POSITIONING.md) |
| D11 | Document layout and claims cutoff | M1 working layout: root planning docs, `research/` evidence/editorial notes, `chapter_briefs/`, `templates/`; original master stays under `docs/`. Claims cutoff remains unfrozen. | Layout recorded for review; exact source/run versions and edition cutoff are later M2/M4 decisions. No original moved. |
| D12 | Existing O'Reilly and Pragmatic titles use “Beyond Vibe Coding.” | Preserve the requested working title during M0; review whether its packaging makes the comparative-method purpose sufficiently clear. No rename is applied. | Author/publisher records title-positioning choice before release; not a legal clearance or a reason to halt M1. [Sources S18–S19](SOURCE_LEDGER.md#s18--oreilly-adjacent-book-and-title-overlap) |

M1 architecture is accepted and the M2 research package is prepared. A11 permits manuscript preparation; W04 resolves the working prose and case routes. The remaining evidence, installation, review and release questions are scheduled before dependent acceptance or execution. No run is frozen and independent technical review remains pending.

## Product-contract backlog found during development — 2026-11-02

These are bounded preparation questions for an eventual executable contract, not requests to stop routine writing. They do not amend the accepted CS rules. The expanded [case chapter](../manuscript/pilot/11-real-world-case-study-building-a-saas.md) excludes unfrozen alternatives from scored expectations.

| ID | Accepted surrounding rule | Unresolved behavior / required disposition |
|---|---|---|
| P13 | CS-04 requires current eligibility when an actor decides; CS-12 counts distinct eligible contributions | If a prior valid contributor is revoked before a second approval, decide whether that contribution remains valid, is invalidated, or requires another specified treatment. The current rule does not explicitly impose retroactive invalidation. Review and freeze the chosen behavior before adding a scored scenario. |
| P14 | CS-02 requires future expiry at creation; no external provisioning/revocation is performed | Decide the consequence of expiry while pending and at decision time. Keep unrelated authorization checks within valid clock conditions until the rule is settled. |
| P15 | CS-08 requires a frozen request-key contract; CS-01/04 retain identity and current eligibility duties | Define key scope/retention, conflicting payloads and replay behavior after terminal completion or changed authority. Duplicate-actor prevention in the local model does not settle these API rules. |
| P16 | CS-05 forbids approving one's own request even with overlapping roles; CS-07 defines rejection as terminal while pending | Clarify rejection authority, especially whether a requester who also holds an otherwise eligible role may reject their own item. Do not infer the answer from self-approval wording or an overly broad decide-use-case sketch. Existing tenant/membership exclusions remain intact; freeze the explicit rejection rule before scoring it. |

For each choice, retain the decision owner, accepted interpretation, affected requirements/checks and contract revision. No HTTP code, migration mechanism or database choice is inferred here.

## Research backlog, not questions the author must answer from memory

| ID | Unresolved evidence | Next action | Required before |
|---|---|---|---|
| R01 | BMad preview label vs expired ETA; current stable package provenance | Resolve releases and installed package against immutable source; keep preview docs out of stable claims. | M2 dossiers / any setup instructions |
| R02 | GSD lineage, old naming and package/version resets | Trace primary migration/release records for chosen lineage; do not repeat community allegations as facts. | Historical prose and run freeze |
| R03 | AWS three-phase concept vs five-phase implementation; profile-dependent gates | Build a sourced mapping; inspect selected profile's decision rights and actual enforcement. | Method abstract detail / M4 |
| R04 | AIUP plugin compatibility and lifecycle guarantees | Check exact selected stack adapter, tests and source; distinguish a documented artifact chain from demonstrated traceability. | Stack commitment / M4 |
| R05 | Independent outcome evidence for all methods | Search controlled research and field reports with disclosed confounders; review S17 full paper before citing its rubric/results. | M2 synthesis |
| R06 | Licence/trademark and quote/figure permissions | Read exact licence/NOTICE/trademark files for any reused material. Avoid reusing prompts/figures until cleared. | M2 and M6 |
| R07 | Existing book's detailed examples and argumentative sequence | Review lawful full text if available; record independent review rather than reproducing it. | Substantive originality assessment |
| R08 | Precise metric definitions and reviewer reliability | Pre-register timing, acceptance, defects, human intervention, artifact usefulness and missing-data rules; calibrate reviewers on non-scored work. | Before measured trials |
| R09 | Tiny changes and counterexamples to the editorial thesis | Include a bounded repair scenario where process overhead can outweigh value; do not assume every project needs full ceremony. | M1 examples plan / M2 evidence |
| R10 | Reproducibility and artifact access | Define companion licensing, redaction, model limitations and whether source-only/local artifacts suffice. Hosting remains unapproved. | M4 packaging / M7 release |
| R11 | Native passage-to-claim/locator accuracy beyond range bookkeeping | Nov 2 raw BMAD inspection exposed mismatched locators, corrected in current prose. Audit remaining cited passages against exact native content, preserve historical receipts and retry unreachable AWS/AIUP passages. Do not infer an upstream change from a mismatch at an immutable pin. | G2 source acceptance and later release; newly unsupported details must not be added as verified facts |

## Assumptions used only to make M0 reviewable

- The master plan, original request and subsequent author-supplied fourteen-chapter structure are the available authority. Other missing documents are not assumed empty, approved, or equivalent to our proposals.
- Scope remains the named four frameworks plus cross-cutting SDD. No additions were made to the approved coverage map.
- Synthetic vendor-access approvals and TypeScript / Node.js are accepted for the M1 design. `CASE_STUDY_SPEC.md` is a new architecture document, not a recovered original, executed application or frozen run baseline.
- No existing source code, test harness, benchmark logs or measured outcomes were found at M0 intake. The M0 package contains no results. The later [policy-model run](evidence/POLICY_MODEL_RUN.json) is a bounded local observation, separate from unexecuted application/method trials.
- This checkout had no Git commits or tracked files at intake; the master plan was already untracked. Original-file preservation is checked by a recorded hash instead of relying on a Git diff.

## M2 disposition — 2026-11-01

The [research package](M2_REPORT.md) is prepared; independent G2 review remains pending. M1 approvals remain intact.

| Question | Research disposition | What remains |
|---|---|---|
| D02 / R02 | Migration notice and current Core sources inspected; recommend contemporary Core with a provenance note | Author chooses edition scope; complete origin/ownership history is not established. |
| D03 / R01 | Branch/tag differences verified; BMAD stable matches its tag | Choose source-snapshot vs released-artifact policy; exact installed versions not frozen. |
| R03 | Original/current AWS phase and profile/guard differences mapped | Actual configured enforcement and any local substitutions require later checks. |
| R04 | Node adapter, stack assumptions and coverage-auditor gap documented | Common framework/database/compiler/host selection and actual compatibility remain open. |
| R05 | Prior comparison read beyond abstract; controlled AI-tool reports and field limits reviewed | No controlled four-method outcome winner established; broader/longitudinal evidence still needed for such claims. |
| R06 | Source licence/NOTICE/trademark text inspected | Per-asset permission and release clearance remain incomplete. |
| R07 | Publisher public metadata only; full book unavailable | Lawful full-text originality review remains pending. |
| R08 / R10 | Run-protocol controls and evidence package planned | No oracle, baseline, model/resource approval or experiment execution completed. |
| R09 | Small-change and testing limitations incorporated into dossiers | Actual counterexample outcomes require later records, not invented runs. |

Priority review items: GSD edition scope, snapshot policy, TypeScript/Node stack path, and named technical reviewer. None requires reopening the fourteen chapters, audience, word budget or approved case domain.

## M3 disposition — 2026-11-01

The [pilot samples](../manuscript/pilot/README.md) are prepared under A08 with explicit draft status. BMAD's inspected 6.12.4 source supplies the prose illustration; this is not the experimental version decision in D03. D09 independent review remains open, and D10/R07 full-text originality work is still pending. The pilot uses independently composed prose and original synthetic examples without outside book/prompt/figure reproduction. The [AI review](M3_PILOT_REVIEW.md) does not close independent technical or originality review. No further author input was needed to finish this bounded draft delivery.
