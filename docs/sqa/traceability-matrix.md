# Traceability Matrix: Coffee and Wifi

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the baseline milestone and its review records (autonomous, not independent) | pending |

---

## Purpose

Tracks backward and forward links between the artifact instances of Coffee and Wifi so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-006] | [RC-017], [RC-013], [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | MIL-001 to MIL-006 | [RC-018], [RC-014], [RC-003] |
| [MIL-001] | Milestone | en | it | [PP-001] | tasks of MIL-001 | [RC-004], [RC-008] |
| [MIL-002] | Milestone | en | it | [PP-001], [MIL-001] | tasks of MIL-002 | [RC-005], [RC-009] |
| [MIL-003] | Milestone | en | it | [PP-001], [MIL-002] | tasks of MIL-003 | [RC-006], [RC-010] |
| [MIL-004] | Milestone | en | it | [PP-001], [MIL-003] | tasks of MIL-004 | [RC-007] |
| [MIL-005] | Milestone | en | it | [PP-001], [MIL-002], [MIL-003] | tasks of MIL-005, [MIL-006] | [RC-015], [RC-016] |
| [MIL-006] | Milestone | en | education | [BC-001], [PP-001], [MIL-004], [MIL-005] | tasks of MIL-006 | [RC-019], [RC-020] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-004] | - | [RC-020], [RC-012], [RC-011] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] (criteria 2 to 4), [MIL-003] (criterion 1) | - | - | Covered |
| CN-002 | [MIL-002] (criteria 1 and 5), [MIL-005] (criteria 1 to 5) | - | - | Covered |
| CN-003 | [MIL-002] (criteria 2 to 4), [MIL-003] (criterion 4) | - | - | Covered |
| CN-004 | [MIL-001] (criterion 1), [MIL-003] (criteria 3 and 4) | - | - | Covered |
| CN-005 | [MIL-001] (criterion 2) | - | - | Covered |
| CN-006 | [MIL-004] (criteria 1 and 2) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

No view, design or test-plan artifact exists (the scope excludes them), so the concerns are covered by the Go/No-Go criteria of the milestones. In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it yet.

The domain of BC-001, PP-001 and MIL-006 is `education` since MIL-006; the other documents keep the domain `it` they were accepted with (see the Open Issues of PP-001). MIL-006 changes no source, test, screenshot, tool or wiki file. The wiki has a row of its own here (it is reviewed in [RC-020]). The review records RC-001 to RC-020 are not rows themselves.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-application.md
[MIL-003]: ../milestones/mil-003-screenshots-readme.md
[MIL-004]: ../milestones/mil-004-wiki.md
[MIL-005]: ../milestones/mil-005-hardening.md
[MIL-006]: ../milestones/mil-006-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
[RC-008]: ./reviews/rc-008-code-mil-001.md
[RC-009]: ./reviews/rc-009-code-mil-002.md
[RC-010]: ./reviews/rc-010-code-mil-003.md
[RC-011]: ./reviews/rc-011-wiki.md
[RC-012]: ./reviews/rc-012-wiki-published.md
[RC-013]: ./reviews/rc-013-business-case-rereview.md
[RC-014]: ./reviews/rc-014-project-plan-rereview.md
[RC-015]: ./reviews/rc-015-mil-005.md
[RC-016]: ./reviews/rc-016-code-mil-005.md
[RC-017]: ./reviews/rc-017-business-case-baseline.md
[RC-018]: ./reviews/rc-018-project-plan-baseline.md
[RC-019]: ./reviews/rc-019-milestone-006.md
[RC-020]: ./reviews/rc-020-wiki-baseline.md
