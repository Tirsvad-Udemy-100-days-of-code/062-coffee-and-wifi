# Screenshots and README

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted after RC-006 (Go, autonomous, not independent) | pending |

---

## Purpose

Decides whether the running application is documented by a screenshot for each lecture step and a README that lets a stranger run it.

## Deliverable

PNG screenshots under `docs/screenshots/` (one per lecture step) and a README built from the framework template.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | One screenshot exists for each of the nine requirements | Yes | No |
| 2 | Screenshots were taken in a Docker container, not on the host desktop | Yes | No |
| 3 | `framework/scripts/check-readme.sh` passes | Yes | No |
| 4 | README has run and test instructions | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Needs the working application |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4; success criterion 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-11 — within the plan window of the Project Plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add a headless screenshot script and container | A Dockerfile and script that start the app and take screenshots with a headless browser inside a Linux container, so the user desktop is never touched (`framework/process/gui-testing.md`). | No | |
| 2 | Take one screenshot per lecture step | Capture the home page, cafes table, Maps Link, Show Me! navigation, the add form, the validation error, the success result and the navigation; save under `docs/screenshots/`. | No | |
| 3 | Write the README | Use the framework README template; include description, run and test instructions, venv steps and the screenshots. | No | |

---

[BC-001]: ../business-case.md
