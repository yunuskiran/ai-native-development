# GSD framework lineage — M2 source dossier

Status: **research-editor extraction; independent technical review pending**. Access: 2026-10-31. Chapter 5's author-supplied title remains unchanged. [Claim register](../evidence/CLAIMS.json); [source ledger](../M2_SOURCE_LEDGER.md).

## Identity and lineage decision

The old `gsd-build/get-shit-done` README directs readers to `open-gsd/gsd-core` (G-C01). This establishes a maintainer-declared destination; it does not establish a complete ownership/dispute history. Current Core is the researched continuation, **not a silently adopted replacement for the author's historical scope**. Recommendation for author disposition: explain the lineage, then use a named Core snapshot for contemporary workflow discussion. Keep the standalone Pi product outside the peer-method comparison.

Research source: `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc`, manifest `@opengsd/gsd-core` `1.19.0`. The release tag `v1.19.0` instead resolves to `9dc57a77…`, earlier than the inspected main snapshot (V-C01). Findings below belong to the source pin; published-asset equivalence is unverified. Origin/founder and complete naming history remain open.

## Process and artifacts

The phase-loop guide connects discussion decisions (`CONTEXT.md`), research/plans, execution summaries, verification and shipping with state that persists across sessions (G-C02). Context engineering documents a thin orchestrator with fresh worker contexts (G-C07). This is the designed information-flow mechanism; its claimed prevention of degradation is not a measured outcome.

The verification guide adds user-observable UAT, persisted progress and gap-fix planning. Standalone code review is optional rather than an automatic part of ship (G-C05). A completion record is not interchangeable with an independent acceptance oracle.

## F01–F11 evidence map

All runtime/effectiveness outcomes are **Not assessed**.

| Dimension | Documentary finding or explicit gap | Evidence / qualification |
|---|---|---|
| F01 Decision rights | Discussion records user choices; UAT asks whether delivered behavior matches expectations. | G-C02/G-C05; [G01](../M2_SOURCE_LEDGER.md#m2-g01), L25–L39; [G04](../M2_SOURCE_LEDGER.md#m2-g04), L15–L22. Actual checkpoint enforcement untested. |
| F02 Overhead/scale | Phase sizing discussion warns of excessive fragmentation and points tiny edits to a quick path. | G01 L77–L90. Time/rework tradeoff not measured. |
| F03 Artifact lifecycle | Persistent planning/state records connect steps; shipping archives phase artifacts. | G-C02, G01 L53–L69. Retention does not prove specification correctness. |
| F04 Traceability | Verification describes checking requirement and recorded-decision coverage. | G01 L53–L55; G04 L60–L66. Actual links/coverage not independently checked. |
| F05 Context | Fresh worker contexts and durable file state are central documented mechanisms. | G-C07; [G02](../M2_SOURCE_LEDGER.md#m2-g02), L26–L65. Fixed window numbers are not portable guarantees. |
| F06 Solo/team | Agent-role/plan-wave coordination is documented. | G01 L35–L47. Real human-team ownership/handoff outcomes not established in this scope. |
| F07 Brownfield | Bounded change/repair planning is described, but a full reverse-engineering baseline procedure was not reviewed. | G01 L77–L90. **Not assessed** beyond inspected change guidance. |
| F08 Testing | UAT, gap closure and optional code review are distinct; completion checks can become stale. | G-C05/G-C06; G04 L9–L89/L106–L115. No tests executed. |
| F09 Operations | Ship documents PR creation/preflight, not comprehensive production operation. | G04 L45–L66. Deployment/rollback/long-term operations **Not assessed**. |
| F10 Portability | Distinct host installation/adapter paths and differing hook capabilities are documented. | G-C03; [G03](../M2_SOURCE_LEDGER.md#m2-g03), L122–L180. Do not reuse an older “single-host only” rating. |
| F11 Maintainability | Input-fingerprint staleness checks and persistent state address later changes. | G-C06. Execution correctness and longitudinal benefit untested. |

## Concrete conflicts and case implications — analysis

At the exact same pin, the install guide says Node 18+ while the package requires Node >=24 and npm >=10 (G-C04). Do not publish a setup recipe using the lower requirement until reconciled. The [compatibility note](../TYPESCRIPT_COMPATIBILITY.md) proposes a supported Node major only as a candidate, not a frozen working installation.

Host adaptations matter: the Core guide explicitly identifies absent context-warning capability on one documented host. Thus “supports multiple hosts” does not mean equivalent context behavior. Fix host/model configuration before matched runs; count all worker calls and disclose differences.

For E1/E2/E3, retain native plans, summaries and verification records. Independently check the tenant/approval invariants instead of accepting a summary-derived UAT list as the complete oracle. Compare phase sizing proportionately; do not force the full loop onto a trivial repair merely to make GSD look costly.

## Limits, counterevidence and rights

Primary documentation supplies both context-quality claims and concrete integration/requirement limitations. No method-specific controlled speed, quality or safety benefit was established. The historical comparative paper's GSD assessment belongs to its own source era, not this Core snapshot.

[G05](../M2_SOURCE_LEDGER.md#m2-g05) identifies the inspected licence as MIT. Reuse clearance is asset-specific; no prompt collection or code was copied. Before pilot prose: author disposes of the lineage recommendation, source-vs-release policy is explicit, Node discrepancy is retained/resolved, and G2 technical source review is complete.
