**English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

# Getting Started

You need Python 3.13 or newer. The packages go into a local virtual environment called `.venv`, so nothing touches your system Python.

## 1. Create and activate `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Upgrade pip and install

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The runtime needs only Flask, Flask-WTF and Bootstrap-Flask. The `dev` extra adds pytest, ruff and mypy.

## 3. Run

```bash
python -m coffee_and_wifi
```

Open `http://127.0.0.1:5000/`. The secret form is at `http://127.0.0.1:5000/add`.

## What we gained

- A virtual environment keeps each project's packages separate (isolation, repeatable installs).
- `pyproject.toml` is the single place for the project name, Python version and dependencies.
- `python -m package` runs a package the same way on every system.
