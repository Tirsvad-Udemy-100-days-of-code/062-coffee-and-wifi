"""CSV implementation of the cafe repository.

@file csv_cafe_repository.py
@brief Reads and appends cafes in a comma-separated file.
"""

import csv
from pathlib import Path

from coffee_and_wifi.constants import CSV_ENCODING
from coffee_and_wifi.domain.cafe import Cafe

_NEWLINE = b"\n"


class CsvCafeRepository:
    """Stores cafes as lines of a CSV file whose first line is the header."""

    def __init__(self, path: Path) -> None:
        """Create the repository for the CSV file at the given path."""
        self._path = path

    def list_all(self) -> list[Cafe]:
        """Return every cafe in the file, skipping the header and blank lines."""
        with self._path.open(newline="", encoding=CSV_ENCODING) as csv_file:
            rows = [row for row in csv.reader(csv_file) if row]
        return [Cafe(*row) for row in rows[1:]]

    def add(self, cafe: Cafe) -> None:
        """Append the cafe as one line, quoting values that need it."""
        prefix = "" if self._ends_with_newline() else "\n"
        with self._path.open("a", newline="", encoding=CSV_ENCODING) as csv_file:
            csv_file.write(prefix)
            csv.writer(csv_file, lineterminator="\n").writerow(
                [
                    cafe.name,
                    cafe.location,
                    cafe.open_time,
                    cafe.close_time,
                    cafe.coffee,
                    cafe.wifi,
                    cafe.power,
                ]
            )

    def _ends_with_newline(self) -> bool:
        with self._path.open("rb") as raw:
            if not raw.read(1):
                return True
            raw.seek(-1, 2)
            return raw.read(1) == _NEWLINE
