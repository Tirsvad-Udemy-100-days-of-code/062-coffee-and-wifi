[English](Getting-Started) · **Dansk** · [Bahasa Melayu](Getting-Started-ms)

# Kom i gang

Du skal bruge Python 3.13 eller nyere. Pakkerne lægges i et lokalt virtuelt miljø kaldet `.venv`, så dit systems Python ikke berøres.

## 1. Opret og aktivér `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS og Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Opgradér pip og installér

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Kørslen kræver kun Flask, Flask-WTF og Bootstrap-Flask. Udvidelsen `dev` tilføjer pytest, ruff og mypy.

## 3. Kør

```bash
python -m coffee_and_wifi
```

Åbn `http://127.0.0.1:5000/`. Den hemmelige formular ligger på `http://127.0.0.1:5000/add`.

## Hvad vi lærte

- Et virtuelt miljø holder hvert projekts pakker adskilt (isolation og gentagelige installationer).
- `pyproject.toml` er det ene sted for projektets navn, Python-version og afhængigheder.
- `python -m pakke` kører en pakke på samme måde på alle systemer.
