"""CSV implementation of the cafe repository.

@file csv_cafe_repository.py
@brief Reads and appends cafes in a comma-separated file.
"""

import csv
from pathlib import Path

from coffee_and_wifi.constants import (
    CSV_ENCODING,
    CSV_FORMULA_ESCAPE,
    CSV_FORMULA_TRIGGERS,
)
from coffee_and_wifi.domain.cafe import Cafe

_NEWLINE = b"\n"


def neutralise_formula(value: str) -> str:
    """Return the value, prefixed with a quote when a spreadsheet would run it.

    @param value The text of one cell.
    @return The same text, or the text after the escape prefix.
    """
    if value.startswith(CSV_FORMULA_TRIGGERS):
        return CSV_FORMULA_ESCAPE + value
    return value


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
        """Append the cafe as one line, quoting values that need it.

        Values that start with a formula trigger are stored with a quote prefix.
        """
        prefix = "" if self._ends_with_newline() else "\n"
        with self._path.open("a", newline="", encoding=CSV_ENCODING) as csv_file:
            csv_file.write(prefix)
            # Every value passes neutralise_formula, so defusedcsv adds nothing.
            # nosemgrep: opengrep.rules.python.lang.security.use-defusedcsv
            writer = csv.writer(csv_file, lineterminator="\n")
            writer.writerow(
                neutralise_formula(value)
                for value in (
                    cafe.name,
                    cafe.location,
                    cafe.open_time,
                    cafe.close_time,
                    cafe.coffee,
                    cafe.wifi,
                    cafe.power,
                )
            )

    def _ends_with_newline(self) -> bool:
        with self._path.open("rb") as raw:
            if not raw.read(1):
                return True
            raw.seek(-1, 2)
            return raw.read(1) == _NEWLINE
