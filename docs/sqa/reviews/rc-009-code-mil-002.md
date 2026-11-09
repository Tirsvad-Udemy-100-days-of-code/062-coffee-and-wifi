# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [f608962] |

---

## Artifact Under Review

- Instance reviewed: [src-mil-002]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of MIL-002 code (all layers and tests)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked across src/coffee_and_wifi (domain, application, infrastructure, presentation) and tests/; ruff, ruff format, mypy --strict and pytest (23 tests) pass. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked across src/coffee_and_wifi (domain, application, infrastructure, presentation) and tests/; ruff, ruff format, mypy --strict and pytest (23 tests) pass. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass; one `type: ignore[misc]` on CafeForm, justified because FlaskForm is untyped. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Checked across src/coffee_and_wifi (domain, application, infrastructure, presentation) and tests/; ruff, ruff format, mypy --strict and pytest (23 tests) pass. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; no swallowed exceptions. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked across src/coffee_and_wifi (domain, application, infrastructure, presentation) and tests/; ruff, ruff format, mypy --strict and pytest (23 tests) pass. |
| 7 | Files, locks and connections are managed with context managers | Pass | CSV files are opened with `with`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked across src/coffee_and_wifi (domain, application, infrastructure, presentation) and tests/; ruff, ruff format, mypy --strict and pytest (23 tests) pass. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging in the application; nothing is printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists for this small project; classes follow the clean-architecture layers (Cafe, CafeRepository, CsvCafeRepository, AddCafe, ListCafes). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 23 tests: unit (use cases, view model), integration (CSV repository incl. no trailing newline and a comma in a name), e2e (routes, validation, append, links); no network, temp copies of the data file. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` is clean; the stubless packages flask_wtf, wtforms and flask_bootstrap have a mypy override in pyproject.toml. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Flask, Flask-WTF, Bootstrap-Flask only at runtime; none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The 'http means link' rule lives once in the cafes view model; constants in constants.py. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports no framework; application imports domain; infrastructure imports domain; only presentation/app.py (composition root) names infrastructure. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One responsibility per module; the use cases depend on the CafeRepository Protocol. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Packages domain, application, infrastructure, presentation under src/coffee_and_wifi; tests/unit, integration, e2e. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Checked across src/coffee_and_wifi (domain, application, infrastructure, presentation) and tests/; ruff, ruff format, mypy --strict and pytest (23 tests) pass. |

## Overall Verdict

Go — every Mandatory criterion passes. Stand-in review in autonomous mode (`Mode: autonomous, not independent`); S01 may challenge it in the final summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-09 |

---

[src-mil-002]: ../../../src
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[f608962]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/commit/f608962dbde84ec31a42383c25c2ece9c4d37f98
