[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

# Bermula

Anda memerlukan Python 3.13 atau lebih baharu. Pakej dipasang dalam persekitaran maya tempatan bernama `.venv`, supaya Python sistem anda tidak terjejas.

## 1. Cipta dan aktifkan `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS dan Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Naik taraf pip dan pasang

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Untuk dijalankan, hanya Flask, Flask-WTF dan Bootstrap-Flask diperlukan. Tambahan `dev` menambah pytest, ruff dan mypy.

## 3. Jalankan

```bash
python -m coffee_and_wifi
```

Buka `http://127.0.0.1:5000/`. Borang rahsia berada di `http://127.0.0.1:5000/add`.

## Apa yang kita pelajari

- Persekitaran maya mengasingkan pakej setiap projek (pengasingan dan pemasangan yang boleh diulang).
- `pyproject.toml` ialah satu tempat untuk nama projek, versi Python dan kebergantungan.
- `python -m pakej` menjalankan pakej dengan cara yang sama pada semua sistem.
