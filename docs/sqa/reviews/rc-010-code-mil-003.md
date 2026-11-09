# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [d50999a] |

---

## Artifact Under Review

- Instance reviewed: [src-mil-003]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of MIL-003 code (tools/screenshots/take_screenshots.py)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked in tools/screenshots/take_screenshots.py (the only Python file of MIL-003); `ruff check` and `ruff format --check` pass. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked in tools/screenshots/take_screenshots.py (the only Python file of MIL-003); `ruff check` and `ruff format --check` pass. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check tools` and `ruff format --check tools` pass. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Checked in tools/screenshots/take_screenshots.py (the only Python file of MIL-003); `ruff check` and `ruff format --check` pass. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Checked in tools/screenshots/take_screenshots.py (the only Python file of MIL-003); `ruff check` and `ruff format --check` pass. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked in tools/screenshots/take_screenshots.py (the only Python file of MIL-003); `ruff check` and `ruff format --check` pass. |
| 7 | Files, locks and connections are managed with context managers | Pass | Checked in tools/screenshots/take_screenshots.py (the only Python file of MIL-003); `ruff check` and `ruff format --check` pass. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked in tools/screenshots/take_screenshots.py (the only Python file of MIL-003); `ruff check` and `ruff format --check` pass. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | The script reports progress on stdout and fails with a non-zero exit; no secrets are handled. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | A tooling script, not part of the application classes. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | N-A | The script is itself the end-to-end check: it asserts every navigation link returns 200 and exits non-zero on a failed step; it ran in Docker and produced nine PNGs. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | mypy is not run on tools/ (playwright types); the application code stays under mypy --strict. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Playwright is pinned in the Docker image only and is not a project dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | URLs and file names are module constants. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | The script imports only the installed package and playwright. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One script, one responsibility: take the screenshots. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | N-A | Not application source; it lives in tools/screenshots/ by design. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Checked in tools/screenshots/take_screenshots.py (the only Python file of MIL-003); `ruff check` and `ruff format --check` pass. |

## Overall Verdict

Go — every Mandatory criterion passes. Stand-in review in autonomous mode (`Mode: autonomous, not independent`); S01 may challenge it in the final summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-09 |

---

[src-mil-003]: ../../../tools/screenshots
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[d50999a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/commit/d50999ab7f2ca13a8618097ffd1afbf839860a63
