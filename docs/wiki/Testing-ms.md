[English](Testing) · [Dansk](Testing-da) · **Bahasa Melayu**

# Ujian

Dengan `.venv` aktif:

```bash
python -m pytest
python -m ruff check src tests
python -m mypy src tests
```

## Cara ujian disusun

| Folder | Apa yang diuji |
| --- | --- |
| `tests/unit/` | Kes guna (dengan repositori palsu) dan model paparan; tiada fail, tiada Flask |
| `tests/integration/` | `CsvCafeRepository` pada fail CSV sebenar dalam folder sementara, termasuk tiada baris baharu di hujung dan koma dalam nama |
| `tests/e2e/` | Seluruh laman melalui klien ujian Flask: halaman, pengesahan, penambahan pada CSV dan semua pautan berfungsi |

Ujian tidak pernah menyentuh fail data sebenar dan tidak menggunakan rangkaian.

## Tangkapan skrin

Tangkapan skrin diambil dalam bekas Docker dengan pelayar tanpa kepala, supaya tetikus dan papan kekunci anda kekal milik anda:

```bash
bash tools/screenshots/run.sh
```

## Apa yang kita pelajari

- Peraturan perniagaan (kes guna) diuji tanpa rangka kerja web kerana ia hanya bergantung pada antara muka repositori.
- Objek palsu lebih ringkas daripada mock apabila ia mencukupi.
- GUI diuji dalam bekas, tidak pernah pada desktop pembangun.
