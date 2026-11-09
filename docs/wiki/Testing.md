**English** · [Dansk](Testing-da) · [Bahasa Melayu](Testing-ms)

# Testing

With `.venv` active:

```bash
python -m pytest
python -m ruff check src tests
python -m mypy src tests
```

## How the tests are organised

| Folder | What it checks |
| --- | --- |
| `tests/unit/` | The use cases (with a fake repository) and the view model; no files, no Flask |
| `tests/integration/` | `CsvCafeRepository` against a real CSV file in a temporary folder, including a missing final newline and a comma in a name |
| `tests/e2e/` | The whole site through Flask's test client: pages, validation, the CSV append and that every link works |

The tests never touch the real data file and never use the network.

## Screenshots

The screenshots are taken in a Docker container with a headless browser, so your mouse and keyboard stay yours:

```bash
bash tools/screenshots/run.sh
```

## What we gained

- Business rules (the use cases) are tested without a web framework, because they depend only on a repository interface.
- A fake is simpler than a mock where it is enough.
- A GUI is tested in a container, never on the developer's desktop.
