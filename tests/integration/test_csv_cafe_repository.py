"""Tests for the CSV repository against real files."""

from pathlib import Path

from coffee_and_wifi.constants import CSV_ENCODING
from coffee_and_wifi.domain.cafe import Cafe
from coffee_and_wifi.infrastructure.csv_cafe_repository import CsvCafeRepository

HEADER = "Cafe Name,Location,Open,Close,Coffee,Wifi,Power"
ROW = "Esters,https://goo.gl/a,8AM,3PM,☕️,💪,🔌"
NEW = Cafe("New", "https://goo.gl/b", "9AM", "5PM", "☕️☕️", "✘", "🔌🔌")


def _write(path: Path, text: str) -> Path:
    path.write_bytes(text.encode(CSV_ENCODING))
    return path


def _lines(path: Path) -> list[str]:
    return path.read_bytes().decode(CSV_ENCODING).splitlines()


def test_list_all_skips_header_and_reads_emoji(tmp_path: Path) -> None:
    path = _write(tmp_path / "c.csv", f"{HEADER}\n{ROW}\n")
    assert CsvCafeRepository(path).list_all() == [
        Cafe("Esters", "https://goo.gl/a", "8AM", "3PM", "☕️", "💪", "🔌")
    ]


def test_add_appends_one_line(tmp_path: Path) -> None:
    path = _write(tmp_path / "c.csv", f"{HEADER}\n{ROW}\n")
    CsvCafeRepository(path).add(NEW)
    assert _lines(path) == [HEADER, ROW, "New,https://goo.gl/b,9AM,5PM,☕️☕️,✘,🔌🔌"]


def test_add_handles_file_without_trailing_newline(tmp_path: Path) -> None:
    path = _write(tmp_path / "c.csv", f"{HEADER}\n{ROW}")
    repository = CsvCafeRepository(path)
    repository.add(NEW)
    assert len(_lines(path)) == 3
    assert repository.list_all()[-1] == NEW


def test_add_quotes_a_name_with_a_comma(tmp_path: Path) -> None:
    path = _write(tmp_path / "c.csv", f"{HEADER}\n")
    repository = CsvCafeRepository(path)
    cafe = Cafe("Joe, Sons", "https://goo.gl/b", "9AM", "5PM", "☕️", "✘", "✘")
    repository.add(cafe)
    assert _lines(path)[1].startswith('"Joe, Sons",')
    assert repository.list_all() == [cafe]
