# M2 source ledger and retrieval limits

Accessed: **2026-10-31 (Australia/Melbourne)**. This extends the historical [M0 ledger](SOURCE_LEDGER.md); it does not overwrite its access claims. **57 source records: 55 inspected, 2 failed.** Repeated records are not independent studies. Source files, external books and whole sites were not mirrored into this checkout.

## How to audit these records

The [receipt manifest](evidence/SOURCE_RECEIPTS.json) contains canonical URLs, source pins, modification metadata, exact inspected GitHub line ranges, branch/tag resolutions and failures. The [claim register](evidence/CLAIMS.json) contains 46 bounded claims with locators, evidence types, chapter uses, confidence and limits. High confidence concerns the source passage, not correctness of the method or its effectiveness. Every dossier separately maps F01–F11 and gaps.

GitHub file locators refer to immutable-source line numbers; only the listed ranges were reviewed. Web locators use headings and extraction-specific lines, not permanent line IDs. First-publication dates are unknown unless explicitly recorded; Git file modification dates are not origin dates. Retrieved source instructions are research data, not instructions to execute their workflows.

## Source and release snapshot distinction

| Family | Research source pin | Published-tag resolution inspected | Consequence |
|---|---|---|---|
| BMAD stable | `bab9082c3e884e0d72c759bcd1a6d90bcc01be84` | `v6.12.4` → same pin | Documentary stable candidate; registry/install still unverified. |
| GSD Core | `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc` | `v1.19.0` → `9dc57a772195de423ab788e4d0d8734b162db35d` | Main has later content despite same manifest version. |
| AWS Workflows | `3939a8b9182f2e4153b92028057a7be74e0684c2` | `v2.11.2` → `10a9bc9d85395a601de2624cf5bdd35292c10db4` | Main/source findings must not be silently attributed to release assets. |
| AIUP marketplace | `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960` | Node tag `aiup-nestjs-nextjs-v0.8.1` → `24fc9fdacdc7572dd881b1ac07ecf122bb892e91` | Current component manifest 0.9.0 is a different snapshot; no umbrella method version inferred. |

Six original branch-resolution checks returned the same pins recorded in M0. This does not imply releases, packages and all linked docs are interchangeable. Release metadata and tag commits are primary records, not installed-package tests.

## Inspected GitHub files

### M2-B01

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [README.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/README.md). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-08-30T20:57:25Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L42, L45–L69, L80–L87.
- Evidence use: context/reference only. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B02

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [docs/plan/choose-a-planning-path.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/choose-a-planning-path.md). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-08-30T20:57:25Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L170.
- Evidence use: B-C02. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B04

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [docs/existing-codebases/start-in-an-existing-codebase.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/existing-codebases/start-in-an-existing-codebase.md). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-08-29T17:48:29Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L88.
- Evidence use: B-C05. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B03

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [docs/build/build-a-change.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/build-a-change.md). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-09-03T15:48:03Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L14, L16–L43, L69–L116, L129–L145, L147–L154, L160–L164.
- Evidence use: B-C03. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B08

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [LICENSE](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/LICENSE). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-01-18T23:03:47Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L30.
- Evidence use: L-C01. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B09

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [TRADEMARK.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/TRADEMARK.md). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-01-18T23:03:47Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L14, L21–L26, L28–L44, L51–L56.
- Evidence use: context/reference only. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B07

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [docs/build/test-completed-work.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/build/test-completed-work.md). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-08-30T10:22:29Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L118.
- Evidence use: B-C06. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B05

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [docs/plan/define-requirements-and-a-specification.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/plan/define-requirements-and-a-specification.md). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-08-30T20:57:25Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L24, L31–L36, L59–L70, L72–L91, L95–L141.
- Evidence use: B-C04. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B10

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [package.json](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/package.json). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-10-14T21:18:43Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L25–L34, L115–L125.
- Evidence use: B-C01. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B06

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [docs/customize/adopt-bmad-across-a-team.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/docs/customize/adopt-bmad-across-a-team.md). Source ref: `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`.
- File modification: 2026-08-30T10:22:29Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L33, L37–L42, L72–L77, L124–L129, L148–L168, L180–L181.
- Evidence use: B-C07. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-G01

- Publisher: open-gsd/gsd-core maintainers. [docs/explanation/the-phase-loop.md](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md). Source ref: `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc`.
- File modification: 2026-06-02T12:13:09Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L21–L74, L77–L84, L88–L95.
- Evidence use: G-C02, G-C07. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-G04

- Publisher: open-gsd/gsd-core maintainers. [docs/how-to/verify-and-ship.md](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/verify-and-ship.md). Source ref: `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc`.
- File modification: 2026-09-14T20:49:52Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L138.
- Evidence use: G-C05, G-C06. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-G05

- Publisher: open-gsd/gsd-core maintainers. [LICENSE](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/LICENSE). Source ref: `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc`.
- File modification: 2026-06-16T12:48:35Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L22.
- Evidence use: L-C01. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-G02

- Publisher: open-gsd/gsd-core maintainers. [docs/explanation/context-engineering.md](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/context-engineering.md). Source ref: `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc`.
- File modification: 2026-07-04T17:32:51Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L75.
- Evidence use: G-C07. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-G06

- Publisher: open-gsd/gsd-core maintainers. [package.json](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/package.json). Source ref: `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc`.
- File modification: 2026-10-26T14:58:13Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L44–L49, L68–L74, L80–L81.
- Evidence use: G-C04, T-C01. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-G03

- Publisher: open-gsd/gsd-core maintainers. [docs/how-to/install-on-your-runtime.md](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/install-on-your-runtime.md). Source ref: `72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc`.
- File modification: 2026-10-26T14:58:13Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L14, L17–L52, L63–L72, L74–L93, L122–L187.
- Evidence use: G-C03, G-C04. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-A05

- Publisher: awslabs/aidlc-workflows maintainers. [LICENSE](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/LICENSE). Source ref: `3939a8b9182f2e4153b92028057a7be74e0684c2`.
- File modification: 2025-11-13T22:05:11Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L18.
- Evidence use: L-C01. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-A01

- Publisher: awslabs/aidlc-workflows maintainers. [docs/guide/04-phases-and-stages.md](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/04-phases-and-stages.md). Source ref: `3939a8b9182f2e4153b92028057a7be74e0684c2`.
- File modification: 2026-10-29T08:15:19Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L12–L45, L47–L82.
- Evidence use: A-C02, A-C06. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-A02

- Publisher: awslabs/aidlc-workflows maintainers. [docs/guide/workflow-profiles.md](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/workflow-profiles.md). Source ref: `3939a8b9182f2e4153b92028057a7be74e0684c2`.
- File modification: 2026-10-26T02:07:07Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L18–L30, L36–L103, L108.
- Evidence use: A-C02, A-C03. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-A04

- Publisher: awslabs/aidlc-workflows maintainers. [docs/guide/14-artifacts-reference.md](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/docs/guide/14-artifacts-reference.md). Source ref: `3939a8b9182f2e4153b92028057a7be74e0684c2`.
- File modification: 2026-10-26T15:33:16Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L14, L17–L22, L24–L83, L101–L102.
- Evidence use: A-C05. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-A03

- Publisher: awslabs/aidlc-workflows maintainers. [core/hooks/aidlc-plan-approval-guard.ts](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/core/hooks/aidlc-plan-approval-guard.ts). Source ref: `3939a8b9182f2e4153b92028057a7be74e0684c2`.
- File modification: 2026-10-29T16:20:24Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L20–L25, L42–L47, L49–L56, L59–L68, L110–L115, L163–L168, L173–L183, L189–L190, L2384–L2418.
- Evidence use: A-C04. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U04

- Publisher: AI-Unified-Process/marketplace maintainers. [aiup-nestjs-nextjs/.claude-plugin/plugin.json](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/.claude-plugin/plugin.json). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-10-29T10:05:35Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L12.
- Evidence use: U-C05, V-C02. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U03

- Publisher: AI-Unified-Process/marketplace maintainers. [aiup-core/skills/spec-review/SKILL.md](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-core/skills/spec-review/SKILL.md). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-10-29T10:05:35Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L16, L25–L75, L79–L81.
- Evidence use: U-C03. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U02

- Publisher: AI-Unified-Process/marketplace maintainers. [aiup-nestjs-nextjs/README.md](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/README.md). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-10-27T15:44:48Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L141.
- Evidence use: U-C04. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U01

- Publisher: AI-Unified-Process/marketplace maintainers. [docs/workflow.md](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/docs/workflow.md). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-10-29T10:05:35Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L16, L19–L24, L46–L66, L111–L136, L153–L158, L169–L174, L210–L212, L300–L447, L475–L500.
- Evidence use: U-C01, U-C02, U-C06, U-C08, U-C09. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U05

- Publisher: AI-Unified-Process/marketplace maintainers. [LICENSE](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/LICENSE). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-08-21T07:32:32Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L16, L35–L40, L49–L56, L58–L72, L89–L125, L137–L151.
- Evidence use: L-C01. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U07

- Publisher: AI-Unified-Process/marketplace maintainers. [aiup-nestjs-nextjs/skills/nest-test/SKILL.md](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/skills/nest-test/SKILL.md). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-10-27T15:44:48Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L11, L16–L34, L37–L71.
- Evidence use: context/reference only. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U06

- Publisher: AI-Unified-Process/marketplace maintainers. [NOTICE](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/NOTICE). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-08-21T07:32:32Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L17.
- Evidence use: L-C01. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-A06

- Publisher: awslabs/aidlc-workflows maintainers. [README.md](https://github.com/awslabs/aidlc-workflows/blob/3939a8b9182f2e4153b92028057a7be74e0684c2/README.md). Source ref: `3939a8b9182f2e4153b92028057a7be74e0684c2`.
- File modification: 2026-10-30T09:00:07Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L45.
- Evidence use: A-C07. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U08

- Publisher: AI-Unified-Process/marketplace maintainers. [aiup-core/skills/reverse-engineer/SKILL.md](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-core/skills/reverse-engineer/SKILL.md). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-10-25T08:43:23Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L25–L30, L48–L58, L95–L100, L108–L113, L132–L137, L156–L161, L262–L267, L298–L300.
- Evidence use: U-C08. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-G07

- Publisher: gsd-build/get-shit-done maintainers. [README.md](https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/README.md). Source ref: `bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815`.
- File modification: 2026-05-31T13:18:41Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L13.
- Evidence use: G-C01. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-B11

- Publisher: bmad-code-org/BMAD-METHOD maintainers. [README.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/README.md). Source ref: `61e01f82644c4bb533750cfa0d6d61ab61d2cc9b`.
- File modification: 2026-10-18T02:03:49Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L16–L33, L61–L66.
- Evidence use: B-C08. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-U09

- Publisher: AI-Unified-Process/marketplace maintainers. [aiup-nestjs-nextjs/skills/implement/SKILL.md](https://github.com/AI-Unified-Process/marketplace/blob/3ad51b0707e9bed6e54b9de46ebc2f28d7afa960/aiup-nestjs-nextjs/skills/implement/SKILL.md). Source ref: `3ad51b0707e9bed6e54b9de46ebc2f28d7afa960`.
- File modification: 2026-10-29T10:05:35Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L10, L16–L31, L36–L79.
- Evidence use: U-C07. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

### M2-R05

- Publisher: stephenlclarke/ai-dlc maintainers. [README.md](https://github.com/stephenlclarke/ai-dlc/blob/main/README.md). Source ref: `main`.
- File modification: 2026-08-03T10:01:19Z; first publication unknown. Status: **INSPECTED**. Inspected lines: L1–L23, L27–L32, L39–L61, L68–L70.
- Evidence use: R-C05. Maintainer material may describe intent and outcome claims; it is not independent effectiveness validation.

## Release metadata

### M2-VB

[GitHub latest-release endpoint](https://api.github.com/repos/bmad-code-org/BMAD-METHOD/releases/latest), inspected 2026-10-31; reports `v6.12.4`, published 2026-10-14T21:19:19Z. [Resolved tag commit](https://api.github.com/repos/bmad-code-org/BMAD-METHOD/commits/v6.12.4): `bab9082c3e884e0d72c759bcd1a6d90bcc01be84`. Release-body claims, assets, package registries and installation were not validated.

### M2-VG

[GitHub latest-release endpoint](https://api.github.com/repos/open-gsd/gsd-core/releases/latest), inspected 2026-10-31; reports `v1.19.0`, published 2026-10-26T14:20:25Z. [Resolved tag commit](https://api.github.com/repos/open-gsd/gsd-core/commits/v1.19.0): `9dc57a772195de423ab788e4d0d8734b162db35d`. Release-body claims, assets, package registries and installation were not validated.

### M2-VA

[GitHub latest-release endpoint](https://api.github.com/repos/awslabs/aidlc-workflows/releases/latest), inspected 2026-10-31; reports `v2.11.2`, published 2026-10-28T09:01:17Z. [Resolved tag commit](https://api.github.com/repos/awslabs/aidlc-workflows/commits/v2.11.2): `10a9bc9d85395a601de2624cf5bdd35292c10db4`. Release-body claims, assets, package registries and installation were not validated.

### M2-VU

[GitHub latest-release endpoint](https://api.github.com/repos/AI-Unified-Process/marketplace/releases/latest), inspected 2026-10-31; reports `aiup-nestjs-nextjs-v0.8.1`, published 2026-10-28T13:15:07Z. [Resolved tag commit](https://api.github.com/repos/AI-Unified-Process/marketplace/commits/aiup-nestjs-nextjs-v0.8.1): `24fc9fdacdc7572dd881b1ac07ecf122bb892e91`. Release-body claims, assets, package registries and installation were not validated.

## Web and primary research records

### M2-W01

- Publisher/author: AWS / Raja SP. [Primary page](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/). Publication: 2025-07-31; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Original methodology/phases and benefit language, headings What is / How does it work.

### M2-W02

- Publisher/author: AI Unified Process / Simon Martinelli. [Primary page](https://unifiedprocess.ai/methodology.html). Publication: not established in this record; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Spec-lifecycle self-classification, Level 2 and neighboring definitions.

### M2-W03

- Publisher/author: Birgitta Böckeler / Martin Fowler site. [Primary page](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html). Publication: 2025-10-15; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Definition, three patterns and evaluation caveats; historical tool observations not reused as current features.

### M2-W04

- Publisher/author: Sanderson Oliveira de Macedo. [Primary page](https://arxiv.org/html/2606.04967v1). Publication: 2026-06-03; version: arXiv v1.
- Status: **INSPECTED**. Scope: Sections 2, 4, 5, 6, 7, 8 and declared limitations/conflict; full-text HTML beyond abstract, not reproduction of all references.

### M2-W05

- Publisher/author: METR / Becker, Rush, Barnes, Rein. [Primary page](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). Publication: 2025-07-10; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Methodology, Core Result, generalization limits and later-update link.

### M2-W06

- Publisher/author: METR / Becker, Rush, Cunningham, Rein, Mahamud. [Primary page](https://metr.org/blog/2026-02-24-uplift-update/). Publication: 2026-02-24; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Study changes, selection and timing limitations; not treated as a clean current uplift estimate.

### M2-W07

- Publisher/author: Alexandre Agius (bio identifies AWS affiliation). [Primary page](https://www.agiusalexandre.com/blog/2026-09-26-ai-dlc-collaborative-team-bottleneck/). Publication: 2026-09-26; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: First-hand platform account, verification/failure sections and author limitations; not an independent method trial.

### M2-W08

- Publisher/author: Node.js project. [Primary page](https://nodejs.org/en/about/previous-releases). Publication: not established in this record; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Release-table and LTS guidance; date-stamped mutable page.

### M2-W09

- Publisher/author: Node.js project. [Primary page](https://nodejs.org/docs/latest-v24.x/api/typescript.html). Publication: not established in this record; version: Node.js v24.22.2.
- Status: **INSPECTED**. Scope: v24.22.2 docs: Full TypeScript support, Type stripping, module/features/decorator limits.

### M2-W10

- Publisher/author: TypeScript project. [Primary page](https://www.typescriptlang.org/docs/handbook/intro.html). Publication: not established in this record; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: The handbook's goal/static-typechecker passage; no exact compiler-version selection.

### M2-W11

- Publisher/author: GitHub / Nat Friedman. [Primary page](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/). Publication: 2021-06-29; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Original technical-preview announcement; page update 2022-02-23.

### M2-W12

- Publisher/author: Kiro. [Primary page](https://kiro.dev/docs/specs/). Publication: not established in this record; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Core Structure / three-phase workflow, surface capability table; page says updated 2026-10-15.

### M2-W13

- Publisher/author: Apress / Springer Nature. [Primary page](https://link.springer.com/book/10.1007/979-8-8688-2851-5). Publication: not established in this record; version: mutable page unless noted.
- Status: **INSPECTED**. Scope: Public bibliographic fields only in this follow-up; prior M0 contents review retained separately.

### M2-W14

- Publisher/author: Andrej Karpathy (candidate original post). [Primary page](https://x.com/karpathy/status/1886192184808149383). Publication: not established in this record; version: mutable page unless noted.
- Status: **NOT VERIFIED IN THIS SESSION — RETRIEVAL FAILED**. Scope: Direct retrieval failed with 403; secondary search mentions are not primary verification.

### M2-W15

- Publisher/author: Tessl registry. [Primary page](https://tessl.io/registry/ai-unified-process/aiup-core/evals). Publication: not established in this record; version: mutable page unless noted.
- Status: **NOT VERIFIED IN THIS SESSION — RETRIEVAL FAILED**. Scope: Direct retrieval failed, cache miss; search-result eval numbers not admitted as inspected findings.

### M2-W16

- Publisher/author: Node.js project. [Primary page](https://nodejs.org/api/typescript.html). Publication: not established in this record; version: Node.js v26.13.0.
- Status: **INSPECTED**. Scope: Default docs resolved to v26.13.0; type-stripping passage inspected, then version-24 docs used for candidate discussion.

### M2-W17

- Publisher: NestJS documentation. [Official page](https://docs.nestjs.com/first-steps); accessed 2026-10-31. Publication/update date not established.
- Status: **INSPECTED**. Scope: Language/Prerequisites/Setup; app and CLI requirements, not an installation. No runtime installation or code execution.

### M2-W18

- Publisher: Next.js documentation. [Official page](https://nextjs.org/docs/app/getting-started/installation); accessed 2026-10-31. Publication/update date not established.
- Status: **INSPECTED**. Scope: System requirements / Set up TypeScript; mutable docs, no installed framework pin. No runtime installation or code execution.

### M2-W19

- Publisher: TypeScript project. [Official page](https://www.typescriptlang.org/tsconfig/emitDecoratorMetadata.html); accessed 2026-10-31. Publication/update date not established.
- Status: **INSPECTED**. Scope: emitDecoratorMetadata description and compiler-output comparison; no compilation. No runtime installation or code execution.

## Search and access record

Directed, non-exhaustive queries included: BMAD/GSD controlled methodology evaluation; AIUP empirical evaluation; AI-DLC productivity/limitations; original Copilot announcement; Karpathy original post; official Node release/TypeScript guidance. Search snippets only discovered candidates. The original X post returned 403; Tessl's eval page returned a cache miss. Their contents/metrics were not validated. A temporary GitHub transport failure on the first BMAD tree request was retried successfully.

The comparative paper was examined beyond its abstract, including method, rubric and limitations; its scores were not imported. METR reports are about AI-assisted work in their own settings, not trials of these four frameworks. The AI-DLC field account identifies an AWS-affiliated author; the documentary review describes itself as independent but supplies no controlled method trial. These distinctions prevent false independent corroboration.

## Boundaries still open

No original external book full text was provided or purchased; the Apress follow-up is public metadata only. Licence/trademark/NOTICE files were inspected for source identification, not a final legal or per-asset clearance. Founding histories beyond recorded primary anchors, exact published asset equivalence, installed compatibility, long-term outcomes and case measurements remain incomplete or **Not assessed**. See [contested claims](CONTESTED_CLAIMS.md) and [M2 report](M2_REPORT.md) for the technical-review handoff.

