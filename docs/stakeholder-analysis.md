# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [40ac86a] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted after RC-002 (Go, autonomous, not independent) | [40ac86a] |

---

## Purpose

Identify who is affected by the Coffee and Wifi project, who decides and who reviews. Method: power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, well documented solution for every assignment requirement |
| S02 | Udemy coursists | Course participants who share and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and README run instructions |
| S03 | GitHub viewers | Visitors browsing the repository for ideas | Public | LOW | MEDIUM | Keep Informed | A clear description, topics and README, and no runtime dependencies beyond need |

## Power/Interest Classification Rationale

S01 decides scope, reviews and accepts every artifact, so power and interest are both high. S02 and S03 cannot change the project but consume its output; S02 has a direct stake in the exercise, S03 a casual one.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | All nine assignment requirements work | Functionality |
| CN-002 | S01 | Tested, reviewable code | Reliability |
| CN-003 | S02 | Assignment function names kept; easy to run | Usability |
| CN-004 | S03 | Clear README, description, topics | Usability |
| CN-005 | S03 | No unnecessary runtime dependencies | Supportability |
| CN-006 | S02 | Wiki in en, da and ms | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Chat and pull request review (S01) | Per milestone | Pull request with `RC-*` records | All milestones |
| CM-002 | README and wiki (S02, S03) | At release | README, trilingual wiki, screenshots | MIL-003, MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Minimal dependencies versus validation convenience | S03, S01 | Only Flask, Flask-WTF and Bootstrap-Flask at runtime; pytest is a dev dependency |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | Objectives 1 and 3 |
| S02 | CN-003, CN-006 | Objectives 2 and 4 |
| S03 | CN-004, CN-005 | Objectives 4 and 5 |

## Sign-Off

| Stakeholder | Role | Date | Signature |
| --- | --- | --- | --- |
| S01 | Product Owner | | [40ac86a] |

---

[BC-001]: ./business-case.md
[40ac86a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/commit/40ac86a92ce1d06f218c8f65b8faaee1d5cd018e
