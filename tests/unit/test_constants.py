"""Tests for the shared constants.

@file test_constants.py
@brief Checks the constants against the data file they describe.
"""

import csv

from coffee_and_wifi import constants


def test_default_data_file_exists() -> None:
    assert constants.DEFAULT_DATA_FILE.is_file()


def test_csv_header_matches_the_data_file() -> None:
    with constants.DEFAULT_DATA_FILE.open(
        newline="", encoding=constants.CSV_ENCODING
    ) as csv_file:
        header = next(csv.reader(csv_file))
    assert tuple(header) == constants.CSV_HEADER


def test_routes_start_with_a_slash() -> None:
    for route in (constants.ROUTE_HOME, constants.ROUTE_CAFES, constants.ROUTE_ADD):
        assert route.startswith("/")
