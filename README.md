<!-- Built from framework/templates/README-template.md. The screenshots for each lecture step are added by milestone MIL-003. -->

# ☕ Coffee and Wifi

Day 62 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": a small Flask site that lists London cafes from a CSV file and lets people who know the secret `/add` route append a new cafe. Made for course participants and anyone browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The site has three pages: the home page with a "Show Me!" button, `/cafes` with a Bootstrap table of every cafe (the location is shown as a "Maps Link"), and the secret `/add` form that validates the data and appends one line to the CSV file.

| Folder | What it holds |
| --- | --- |
| `src/coffee_and_wifi/` | The application: `constants.py`, templates, static files and the data file |
| `tests/` | The pytest tests |
| `docs/` | The project documents (business case, plan, milestones, reviews) |

The code is documented with Doxygen comments; `Doxyfile` builds the HTML reference.

## 📋 Requirements

- Python 3.13 or newer, because `pyproject.toml` requires it.
- `venv` (part of Python) to keep the packages away from your system Python.
- Runtime packages: Flask, Flask-WTF and Bootstrap-Flask, the three the assignment needs. Nothing else.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the code reference.

## 🛠️ Setup

Create a local virtual environment in `.venv`, activate it, upgrade pip and install the project with the test tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. The `.venv` folder is ignored by git.

## ▶️ Run

With the environment active:

```bash
python -m coffee_and_wifi
```

Open <http://127.0.0.1:5000/> for the home page and click "Show Me!" to reach `/cafes`. The secret form is at <http://127.0.0.1:5000/add>; nothing links to it.

Optional environment variables: `SECRET_KEY` (a random key is generated at start when it is not set) and `COFFEE_AND_WIFI_DATA_FILE` (path of the CSV file; the default is the file in the package).

## 🧪 Tests

With the environment active:

```bash
python -m pytest
```

Build the code reference (optional) with `doxygen Doxyfile`; the result is in `docs/doxygen/html/index.html`.

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/062-coffee-and-wifi/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
