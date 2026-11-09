# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted after RC-001 (Go, autonomous, not independent) | pending |

---

## Executive Summary

Coffee and Wifi is Day 62 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". The task is a small Flask website that lists London cafes (name, location, opening hours, coffee, wifi and power ratings) from a CSV file and lets people who know the secret `/add` route append a cafe. The project delivers a readable, runnable, tested solution that other course participants and repository viewers can learn from.

## Methodological and Standards Foundation

The artifacts follow the SQA/QC framework mounted at `framework/` (Larman-style analysis, ISO/IEC 25010:2023 quality tags). Code follows the `coding-conventions` and `clean-architecture` skills and is tested with pytest.

## Problem Statement

The assignment ships only a front-end skeleton. Participants must connect Flask-WTF, Bootstrap-Flask and CSV handling themselves, and solutions shared online are often undocumented, untested and hard to run.

## Business Opportunity

A documented, tested and screenshot-illustrated solution lets course participants compare approaches, and gives repository viewers a clear example of a small Flask project with planning, tests and a trilingual wiki.

## Objectives

1. Implement every requirement of the Day 62 assignment (home page, `/cafes` table, "Maps Link" anchors, "Show Me!" button, secret `/add` route, validated form, CSV append, working navigation).
2. Keep the assignment's function and route names so solutions are comparable.
3. Provide pytest tests for the CSV handling, the form validation and the routes.
4. Provide a README and a wiki in English, Danish and Bahasa Malaysia, each with a screenshot per lecture step and an explanation of what was gained.
5. Set the repository description and topics on the git host.

## Scope

### In Scope

- Flask application under `src/`, tests under `tests/`, documents under `docs/`.
- `pyproject.toml`, `constants.py`, Python `.gitignore`, `Doxyfile`, Doxygen comments, `.venv` instructions.
- README from the framework template; wiki in en, da and ms; screenshots taken in a container.
- Repository description and topics.

### Out of Scope

- Authentication, a database, deployment or hosting.
- Editing or deleting cafes.
- Designing a new front-end (the starting files supply it).

## Expected Benefits

### Tangible Benefits

- A passing pytest suite and an app that runs with a handful of commands.
- Wiki and README in three languages with a screenshot for each lecture step.

### Intangible Benefits

- Practice in Flask-WTF, Bootstrap-Flask, CSV handling and the planning-first workflow.
- A reusable example for other participants.

## Strategic Alignment

Supports the Product Owner's goal of finishing the 100 Days of Code course with documented, reviewable projects in one repository group (`Tirsvad-Udemy-100-days-of-code`).

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Assignment requirements met | 9 of 9 requirements demonstrably working | Checklist in the wiki, each with a screenshot |
| 2 | Automated tests pass | 100 % of pytest tests pass | `python -m pytest` exit code 0 |
| 3 | Runtime dependencies | Only what the assignment needs (Flask, Flask-WTF, Bootstrap-Flask) | `pyproject.toml` |
| 4 | Documentation languages | 3 (en, da, ms) | Wiki pages present |
| 5 | Repository metadata | Description and at least 5 topics set | Git host API |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The signed download link for the starting files has expired | The starting project cannot be fetched | Rebuild the front-end files (templates, CSS, CSV) from the assignment text, note it in the README, and ask the user for the zip |
| The Udemy page is behind a login and cannot be viewed | The desired final product cannot be compared | Work from the written requirements; S01 compares visually |
| A token leaks into the repository | Security incident | Tokens are read from `../.env` into the process environment only, never printed, committed or imported by the project; `.env` is git-ignored |
| GUI screenshots taken on the host desktop | Takes over the user's mouse and keyboard | Screenshots are taken headless in a Docker container (`framework/process/gui-testing.md`) |
| Translation quality of da and ms | Wiki unclear | Short sentences; S01 reviews |

## Assumptions

- The Product Owner is also the developer and reviewer (S01).
- Python 3.13 or newer is installed.
- Docker is available for the screenshot step; if it is not, that step stops and is reported.

## Constraints

- Python 3.13+, `venv`, pytest, `pyproject.toml`, `constants.py` for constants.
- Doxygen comments in the source and a `Doxyfile`.
- Folders `src/`, `tests/`, `docs/`.
- Product Owner language English, domain IT.
- Delivery window 2026-11-09 to 2026-11-13, set by S01.
- One branch and pull request per milestone.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one working day of AI-assisted effort plus review time by S01; no licence or hosting cost (qualitative: this is a learning project, a monetary estimate is not meaningful) | A documented reference solution, a trilingual wiki and a repeatable project pattern for the next course days |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a correct, learnable solution |
| S02 | Udemy coursists; want readable, runnable code with the assignment's function names and run instructions |
| S03 | GitHub viewers; want a clear description, topics and README, and no extra runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks are mitigated and the outcome serves all three stakeholders.
