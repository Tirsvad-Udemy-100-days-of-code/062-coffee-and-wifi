"""Tests for the cafe table view model."""

from coffee_and_wifi.constants import CSV_HEADER, MAPS_LINK_TEXT
from coffee_and_wifi.domain.cafe import Cafe
from coffee_and_wifi.presentation.features.cafes.view_model import (
    CellView,
    build_rows,
    to_cell,
)


def test_to_cell_turns_http_value_into_maps_link() -> None:
    assert to_cell("https://goo.gl/a") == CellView(MAPS_LINK_TEXT, "https://goo.gl/a")


def test_to_cell_keeps_plain_value_as_text() -> None:
    assert to_cell("Esters") == CellView("Esters")


def test_build_rows_puts_header_first() -> None:
    cafe = Cafe("A", "https://x.y", "8AM", "3PM", "☕️", "💪", "🔌")
    rows = build_rows([cafe])
    assert [cell.text for cell in rows[0]] == list(CSV_HEADER)
    assert len(rows) == 2
    assert rows[1][1].href == "https://x.y"
