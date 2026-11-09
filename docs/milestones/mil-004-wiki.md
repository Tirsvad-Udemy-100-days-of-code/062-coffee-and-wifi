# Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [40ac86a] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted after RC-007 (Go, autonomous, not independent) | [40ac86a] |

---

## Purpose

Decides whether the wiki explains, in three languages, what each lecture step teaches.

## Deliverable

Wiki pages in English, Danish and Bahasa Malaysia, each with the screenshot of every lecture step and a "what we gained" explanation.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Wiki pages exist for en, da and ms | Yes | No |
| 2 | Each page has all nine steps with a screenshot | Yes | No |
| 3 | `framework/scripts/check-languages.sh` passes if it applies | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Needs the screenshots |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4; success criteria 1 and 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — within the plan window of the Project Plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Follow `framework/process/wiki.md`; one section per lecture step with its screenshot and what was gained. | No | |
| 2 | Write the Danish wiki | Same content in Danish. | No | |
| 3 | Write the Bahasa Malaysia wiki | Same content in Bahasa Malaysia. | No | |
| 4 | Publish the wiki | Put the pages into the repository wiki on the git host (outward-facing, done only after the milestone is accepted). | No | |

---

[BC-001]: ../business-case.md
[40ac86a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/commit/40ac86a92ce1d06f218c8f65b8faaee1d5cd018e
