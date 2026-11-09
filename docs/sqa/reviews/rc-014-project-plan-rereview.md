# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [ba840a5] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] (`QC-PP-001`)
- Scope: full re-review after MIL-005 was added; earlier record [RC-003]
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Re-checked in docs/project-plan.md after MIL-005 was added. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Five gateways, each once, with document, decision date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | MIL-005 decision date 2026-11-10 equals the date in its document and lies in the window 2026-11-09 to 2026-11-13. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | The hardening scope item is covered by MIL-005. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Dependency line MIL-002 to MIL-005 added; acyclic. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Re-checked in docs/project-plan.md after MIL-005 was added. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Re-checked in docs/project-plan.md after MIL-005 was added. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Re-checked in docs/project-plan.md after MIL-005 was added. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Re-checked in docs/project-plan.md after MIL-005 was added. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Re-checked in docs/project-plan.md after MIL-005 was added. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | MIL-005 deliverable matches its document. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Re-checked in docs/project-plan.md after MIL-005 was added. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt and the dependency list agree. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Closed gateways say closed; MIL-005 says pending sync. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Re-checked in docs/project-plan.md after MIL-005 was added. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | English, IT domain; Metadata rows present and valid; no translated twin; headings in English. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | English, IT domain; Metadata rows present and valid; no translated twin; headings in English. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | English, IT domain; Metadata rows present and valid; no translated twin; headings in English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | English, IT domain; Metadata rows present and valid; no translated twin; headings in English. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No DICT exists yet; only standard IT terms (Flask, CSV, pytest, venv) are used, each with one name. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | English, IT domain; Metadata rows present and valid; no translated twin; headings in English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | English, IT domain; Metadata rows present and valid; no translated twin; headings in English. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version; no earlier accepted version, so no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Confirmed by the AI as stand-in for S01 (reads English, knows the IT domain); not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (CSV, URL, CI) are common IT terms; PO, SA and MIL are spelled out in the headings or the glossary of the framework. |

## Overall Verdict

Go — every Mandatory criterion passes. Stand-in review in autonomous mode (`Mode: autonomous, not independent`); S01 may challenge it in the final summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-09 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[ba840a5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/commit/ba840a51f9f6ec2ac266cce649c16bd38b351af6
