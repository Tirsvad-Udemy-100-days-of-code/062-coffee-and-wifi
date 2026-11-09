[English](Testing) · **Dansk** · [Bahasa Melayu](Testing-ms)

# Test

Med `.venv` aktiv:

```bash
python -m pytest
python -m ruff check src tests
python -m mypy src tests
```

## Sådan er testene opbygget

| Mappe | Hvad den tester |
| --- | --- |
| `tests/unit/` | Use cases (med et falsk repository) og view-modellen; ingen filer, ingen Flask |
| `tests/integration/` | `CsvCafeRepository` mod en rigtig CSV-fil i en midlertidig mappe, også uden afsluttende linjeskift og med komma i et navn |
| `tests/e2e/` | Hele sitet via Flasks testklient: sider, validering, tilføjelse til CSV og at alle links virker |

Testene rører aldrig den rigtige datafil og bruger aldrig netværket.

## Skærmbilleder

Skærmbillederne tages i en Docker-container med en headless browser, så din mus og dit tastatur er dine egne:

```bash
bash tools/screenshots/run.sh
```

## Hvad vi lærte

- Forretningsreglerne (use cases) testes uden et webframework, fordi de kun afhænger af en repository-grænseflade.
- En fake er enklere end en mock, når den er nok.
- En GUI testes i en container, aldrig på udviklerens skrivebord.
