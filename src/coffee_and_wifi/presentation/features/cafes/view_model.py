"""View model of the cafe table.

@file view_model.py
@brief Plain data for the table: header first, links already decided.
"""

from dataclasses import dataclass

from coffee_and_wifi.constants import CSV_HEADER, LINK_PREFIX, MAPS_LINK_TEXT
from coffee_and_wifi.domain.cafe import Cafe


@dataclass(frozen=True, slots=True)
class CellView:
    """One table cell: the text to show and, for a link, where it points."""

    text: str
    href: str | None = None


def to_cell(value: str) -> CellView:
    """Turn a value into a cell; a value starting with http becomes a link."""
    if value.startswith(LINK_PREFIX):
        return CellView(text=MAPS_LINK_TEXT, href=value)
    return CellView(text=value)


def to_row(cafe: Cafe) -> list[CellView]:
    """Turn a cafe into the cells of one table row."""
    values = (
        cafe.name,
        cafe.location,
        cafe.open_time,
        cafe.close_time,
        cafe.coffee,
        cafe.wifi,
        cafe.power,
    )
    return [to_cell(value) for value in values]


def build_rows(cafes: list[Cafe]) -> list[list[CellView]]:
    """Return the table rows with the header row first."""
    header = [CellView(text=name) for name in CSV_HEADER]
    return [header, *(to_row(cafe) for cafe in cafes)]
