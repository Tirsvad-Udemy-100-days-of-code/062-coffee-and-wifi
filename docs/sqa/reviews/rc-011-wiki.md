# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [1a4dff5] |

---

## Artifact Under Review

- Instance reviewed: the wiki in docs/wiki/
- Checklist used: [QC-WIKI-001] (`QC-WIKI-001`)
- Scope: full review of the wiki in the repository (milestone MIL-004)
- Language and domain: en, da, ms (wiki pages)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | docs/wiki/_Sidebar.md exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Sidebar starts with the bold title, then one English page list with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Home, Getting-Started, Lecture-Steps and Testing are listed; every link target exists (checked by script). |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | No related wikis, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is the last section: English, Dansk, Bahasa Melayu, each linking to its Home page. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list is not repeated per language. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English plus Danish and Bahasa Malaysia; English is the PO language. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Four pages in each of the three languages. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with the language line, the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Home-da.md, Home-ms.md style names; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, file names and code identifiers stay in English. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | Only a published wiki can be checked; the scoped publish workflow runs after the merge to main. Delta re-review follows (action item). |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No change to the layout rules. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | docs/wiki/ is flat, no subfolder. |

## Overall Verdict

Go-with-conditions — every Mandatory criterion that can be checked in the repository passes; criterion 14 is Pending until the wiki is published. Stand-in review in autonomous mode (`Mode: autonomous, not independent`); S01 may challenge it in the final summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| After the merge, check the published wiki, sidebar and every link on the host, then record a delta re-review of criterion 14 | S01 | 2026-11-12 |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[1a4dff5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/commit/1a4dff5be9182b072fd724ef71189827629ae32e
