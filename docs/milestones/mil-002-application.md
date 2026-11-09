# Application

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [40ac86a] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted after RC-005 (Go, autonomous, not independent) | [40ac86a] |

---

## Purpose

Decides whether the Flask application meets every requirement of the Day 62 assignment.

## Deliverable

A Flask application under `src/` (home, `/cafes`, secret `/add`) with a CSV repository, a validated form and a passing pytest suite, with Doxygen comments.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes | Yes | No |
| 2 | `GET /`, `/cafes` and `/add` return 200 and `/cafes` renders a Bootstrap table of all CSV rows | Yes | No |
| 3 | Location URLs render as `<a href=...>Maps Link</a>` | Yes | No |
| 4 | An invalid URL is rejected on `/add`; a valid submission appends one comma-separated line to the CSV | Yes | No |
| 5 | The code was reviewed against `qc-programming-python.md` with a `Go` | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the skeleton, tooling and starting files |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 3; success criteria 1 to 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — within the plan window of the Project Plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add base template and home page | Add the Bootstrap blocks and stylesheet link to `base.html` and make `/` render the home page with the "Show Me!" button linking to `/cafes`. | No | |
| 2 | Add CSV repository | Read all cafes from `cafe-data.csv` and append a cafe as one comma-separated line, quoting values that contain commas. Isolated from Flask so it is testable. | No | |
| 3 | Add /cafes table | Render all rows in a Bootstrap table; a value starting with `http` becomes an anchor with the text "Maps Link". | No | |
| 4 | Add secret /add form | Add the Flask-WTF form (cafe name, location URL, open, close, coffee, wifi, power) rendered with Bootstrap-Flask `render_form`, a URL validator and browser validation switched off; no navigation button points to it. | No | |
| 5 | Append submitted cafes to the CSV | On a valid submission append the row and redirect to `/cafes`. | No | |
| 6 | Make navigation links work | Check that every navigation link in the base template resolves. | No | |
| 7 | Write pytest tests | Test the CSV repository, the form validation and the routes with a temporary CSV. | No | |
| 8 | Review code against the Python checklist | Review the code against `qc-programming-python.md` and write the `RC-*` record. | No | |

---

[BC-001]: ../business-case.md
[40ac86a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/commit/40ac86a92ce1d06f218c8f65b8faaee1d5cd018e
