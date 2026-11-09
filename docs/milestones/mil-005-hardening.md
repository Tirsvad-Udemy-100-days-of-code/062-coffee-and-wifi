# Hardening

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted after RC-015 (Go, autonomous, not independent) | pending |

---

## Purpose

Decides whether the two findings the git host code scan (OpenGrep) reported as notices on the merged code are fixed, so the scan is clean of security notices.

## Deliverable

A CSV repository that neutralises cells that a spreadsheet would read as formulas, tests for it, and a screenshot container image whose base image is pinned by digest.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A cafe name or other text starting with `=`, `+`, `-` or `@` is stored so that a spreadsheet shows it as text, and a test proves it | Yes | No |
| 2 | Ordinary values, including emoji and a leading space in a time, are stored unchanged and the existing 23 tests still pass | Yes | No |
| 3 | `tools/screenshots/Dockerfile` pins its `FROM` image by digest and `bash tools/screenshots/run.sh` still produces nine screenshots | Yes | No |
| 4 | The OpenGrep check of the pull request reports no `use-defusedcsv` and no `dockerfile-source-not-pinned` finding | Yes | No |
| 5 | The code was reviewed against `qc-programming-python.md` with a `Go` | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Changes its CSV repository |
| MIL-003 | Changes its container image |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3 (tested CSV handling); success criterion 2; scope item "hardening of the code scan findings" | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — inside the delivery window 2026-11-09 to 2026-11-13 of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Neutralise CSV formula injection | When the CSV repository writes a cell that starts with `=`, `+`, `-` or `@` it prefixes a single quote so a spreadsheet shows text, not a formula (OpenGrep rule `use-defusedcsv`). Existing rows are not rewritten and reading returns the stored text as it is (the OWASP recommended prefix stays visible in the table). Plain values stay unchanged. Python in `src/`, done through the `python-developer` agent. | No | |
| 2 | Add tests for the CSV hardening | Unit or integration tests: each of the four leading characters, an ordinary value, an emoji value and a time with a leading space, and a round trip through `list_all`. | No | |
| 3 | Pin the screenshot image by digest | Replace the tag in `tools/screenshots/Dockerfile` by the image digest (keeping the tag in a comment), rebuild with `run.sh` in Docker and check that nine screenshots are produced (OpenGrep rule `dockerfile-source-not-pinned`). | No | |
| 4 | Review the code against the Python checklist | Review the changed code against `qc-programming-python.md` and write the `RC-*` record. | No | |

---

[BC-001]: ../business-case.md
