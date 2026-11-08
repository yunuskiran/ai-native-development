# Contested claims, qualifications and unresolved decisions

Prepared: **2026-11-01** from the **2026-10-31** evidence snapshot. This is an editorial disposition record, not a defect ranking. [Source ledger](M2_SOURCE_LEDGER.md); [claim register](evidence/CLAIMS.json).

| ID | Tempting but unsupported wording | Evidence / disposition | Required resolution |
|---|---|---|---|
| Q01 | “GSD Core needs only Node 18+.” | At the same research pin, guide and manifest conflict: 18+ vs >=24/npm >=10 (G-C04). | Preserve the discrepancy; verify exact selected package and runtime before setup/run instructions. |
| Q02 | “Version number X identifies all reviewed behavior.” | BMAD tag matches its research source; Core/AWS same-version tags precede researched main. AIUP source component is 0.9.0 while latest component tag is 0.8.1 (V-C01/V-C02). | Choose released-package or source-snapshot policy; inspect/test the actual chosen artifact. Never silently transfer newer main behavior to a tag. |
| Q03 | “GSD is single-host, or all supported hosts work the same.” | Current Core docs enumerate integrations and capability differences (G-C03); older commentary has a different scope. | Keep source-era qualifications; declare host-specific exceptions and validate the actual host. |
| Q04 | “AWS AI-DLC always enforces every approval the same way.” | Profiles alter review/guard defaults and expose overrides; one disable branch is visible in source (A-C03/A-C04). | Record profile, settings and observed gate events. Static inspection is not a comprehensive enforcement audit. |
| Q05 | “AIUP has identical coverage automation on every stack.” | Core workflow explicitly qualifies the combined Node auditor gap; layered rights do not automatically apply to combined adapters (U-C02/U-C06). | Name the adapter and any manual/custom audit. Do not import another stack's features as Node defaults. |
| Q06 | “TypeScript/Node automatically means the native AIUP stack.” | Author selected a language/runtime family; Node adapter assumes NestJS, Next.js, Drizzle/PostgreSQL and related testing (U-C04). | Deliberately adopt a common native stack or record a changed construction intervention. No framework/database choice is silently made. |
| Q07 | “Persistent specs guarantee correct code/tests.” | Retention/reconciliation mechanisms are documented, but alignment is not measured. BMAD's brownfield archive policy also qualifies blanket persistence (B-C05/U-C08). | Inspect actual links, disagreements and change outcomes; use an independent oracle. |
| Q08 | “Tests, gates or green status prove production readiness.” | Generated QA, user UAT, semantic review and deterministic checks have different scopes. No case execution exists. | Define/execute acceptance and operational checks; disclose local/solo scope. No security/compliance certification inferred. |
| Q09 | “Independent research proves which of the four is faster.” | The inspected documentary comparison is not an outcome trial; other research concerns different AI-tool settings, and field accounts have distinct interests/scope (R-C01–R-C05). | Keep outcomes Not assessed; seek valid matched/longitudinal evidence rather than transplant results. |
| Q10 | “The original vibe-coding post was verified, and all source reuse is cleared.” | Original-post retrieval failed; source notices were inspected but book/asset clearance remains incomplete (W14, L-C01). | Mark the historical attribution unverified; retain per-asset and lawful full-text review tasks. |

## Author/reviewer decisions before dependent work

- **Edition scope:** use the current Core continuation with a historical GSD note, or an explicitly historical framework snapshot. The research recommendation is current Core with provenance, but the author has not yet chosen this scope.
- **Snapshot policy:** BMAD stable is a matching source/tag candidate; decide how to handle later main snapshots for Core/AWS and AIUP's component releases. No installed/run versions are frozen.
- **Common stack:** retain TypeScript/Node; decide native-adapter stack versus explicitly adapted minimal implementation after compatibility review.
- **Technical reviewer:** a named person must verify G2 source support. AI extraction/checks do not satisfy independent human review.

M1-approved titles, audience, length and case direction are not reopened. Model access, spend ceilings, actual experiments, deployment and publication remain later decisions. These open issues are retained in the M2 handoff rather than hidden by a “complete” label.
