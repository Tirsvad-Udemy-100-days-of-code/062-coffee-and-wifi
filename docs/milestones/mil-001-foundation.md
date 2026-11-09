# Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [40ac86a] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted after RC-004 (Go, autonomous, not independent) | [40ac86a] |

---

## Purpose

Decides whether the project skeleton and tooling are sound enough to start writing the application.

## Deliverable

A repository with description and topics, `pyproject.toml`, Python `.gitignore`, `constants.py`, `Doxyfile`, the starting files (templates, CSS, CSV) under `src/`, and venv instructions.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Repository description and at least 5 topics are set on the git host | Yes | No |
| 2 | `pip install -e ".[dev]"` succeeds in a fresh `.venv` on Python 3.13+ | Yes | No |
| 3 | `python -m pytest` runs without a collection error | Yes | No |
| 4 | `.gitignore` excludes `.venv/` and `.env` | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First phase |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5; Constraints (Python, venv, pytest, pyproject, Doxygen) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-09 — within the plan window of the Project Plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set the description and topics (python, flask, wtforms, bootstrap, udemy, 100-days-of-code) on the git host through its API, with the token read from the environment and never printed or stored. Serves S03. | No | |
| 2 | Fetch the starting files | Download the Day 62 starting zip into a separate folder, inspect it, and copy templates, static CSS and `cafe-data.csv` under `src/`. If the signed link has expired, rebuild them from the assignment text and note it. Nothing else from the zip is imported. | No | |
| 3 | Add pyproject.toml, .gitignore and constants.py | Python 3.13+ project configuration with Flask, Flask-WTF and Bootstrap-Flask as runtime dependencies, pytest as a dev extra, a Python `.gitignore` that also excludes `.env`, and `constants.py` for routes, file names and field names. | No | |
| 4 | Add Doxyfile and Doxygen comment convention | Add a `Doxyfile` that documents `src/` and note the comment style in the README. Serves S02. | No | |
| 5 | Document the local .venv | Describe how to create `.venv`, activate it (Windows and Unix), run `python -m pip install --upgrade pip`, install the project and run the tests. | No | |

---

[BC-001]: ../business-case.md
[40ac86a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/commit/40ac86a92ce1d06f218c8f65b8faaee1d5cd018e
