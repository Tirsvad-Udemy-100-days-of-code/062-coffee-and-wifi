# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [src-mil-001]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of MIL-001 code (constants.py, test_constants.py)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |
| 7 | Files, locks and connections are managed with context managers | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging in this milestone. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; MIL-001 holds constants only, so there is no class to trace. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | tests/unit/test_constants.py, 3 behaviour tests, no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` reports no issues; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Flask, Flask-WTF, Bootstrap-Flask declared with lower bounds; pytest, ruff, mypy in the dev extra. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | constants.py imports only pathlib. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | N-A | No classes yet. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Only constants.py exists; layer packages are created with their first file (MIL-002). |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Checked in src/coffee_and_wifi/constants.py and tests/unit/test_constants.py; ruff and pytest pass. |

## Overall Verdict

Go — every Mandatory criterion passes. Stand-in review in autonomous mode (`Mode: autonomous, not independent`); S01 may challenge it in the final summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-09 |

---

[src-mil-001]: ../../../src
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
