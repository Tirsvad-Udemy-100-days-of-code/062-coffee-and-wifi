"""End-to-end tests of the site through the Flask test client."""

import re
import shutil
from pathlib import Path

import pytest
from flask import Flask
from flask.testing import FlaskClient

from coffee_and_wifi.constants import (
    CSV_ENCODING,
    DEFAULT_DATA_FILE,
    MAPS_LINK_TEXT,
    ROUTE_ADD,
    ROUTE_CAFES,
    ROUTE_HOME,
)
from coffee_and_wifi.presentation.app import create_app

VALID_FORM = {
    "cafe": "Test Cafe, Soho",
    "location": "https://goo.gl/maps/abc",
    "open_time": "8AM",
    "close_time": "5PM",
    "coffee_rating": "☕️",
    "wifi_rating": "💪",
    "power_rating": "🔌",
}
HREF = re.compile(r'href="([^"]+)"')


@pytest.fixture
def data_file(tmp_path: Path) -> Path:
    target = tmp_path / "cafe-data.csv"
    shutil.copy(DEFAULT_DATA_FILE, target)
    return target


@pytest.fixture
def client(data_file: Path) -> FlaskClient:
    app: Flask = create_app(
        {"TESTING": True, "WTF_CSRF_ENABLED": False, "DATA_FILE": data_file}
    )
    return app.test_client()


def _lines(path: Path) -> list[str]:
    return path.read_bytes().decode(CSV_ENCODING).splitlines()


def test_home_returns_200(client: FlaskClient) -> None:
    assert client.get(ROUTE_HOME).status_code == 200


def test_cafes_renders_table_with_one_maps_link_per_data_row(
    client: FlaskClient, data_file: Path
) -> None:
    response = client.get(ROUTE_CAFES)
    html = response.get_data(as_text=True)
    data_rows = len(_lines(data_file)) - 1
    assert response.status_code == 200
    assert "table table-dark table-striped table-hover" in html
    assert len(re.findall(rf">{MAPS_LINK_TEXT}</a>", html)) == data_rows
    assert not re.findall(r">\s*https?://", html)


def test_add_form_returns_200(client: FlaskClient) -> None:
    assert client.get(ROUTE_ADD).status_code == 200


def test_add_with_invalid_url_shows_error_and_keeps_csv(
    client: FlaskClient, data_file: Path
) -> None:
    before = data_file.read_bytes()
    response = client.post(ROUTE_ADD, data={**VALID_FORM, "location": "not a url"})
    assert response.status_code == 200
    assert "Enter a valid URL" in response.get_data(as_text=True)
    assert data_file.read_bytes() == before


def test_add_with_valid_data_appends_one_line_and_redirects(
    client: FlaskClient, data_file: Path
) -> None:
    before = _lines(data_file)
    response = client.post(ROUTE_ADD, data=VALID_FORM)
    assert response.status_code == 302
    assert response.headers["Location"].endswith(ROUTE_CAFES)
    after = _lines(data_file)
    assert len(after) == len(before) + 1
    assert after[-1].startswith('"Test Cafe, Soho",https://goo.gl/maps/abc,8AM')


@pytest.mark.parametrize("route", [ROUTE_HOME, ROUTE_CAFES])
def test_pages_do_not_link_to_the_secret_route(client: FlaskClient, route: str) -> None:
    html = client.get(route).get_data(as_text=True)
    assert ROUTE_ADD not in HREF.findall(html)


@pytest.mark.parametrize("route", [ROUTE_HOME, ROUTE_CAFES, ROUTE_ADD])
def test_every_local_link_resolves(client: FlaskClient, route: str) -> None:
    html = client.get(route).get_data(as_text=True)
    local = [h for h in HREF.findall(html) if h.startswith("/")]
    assert local
    for href in local:
        assert client.get(href).status_code == 200, href


def test_add_with_formula_name_stores_it_with_a_quote_prefix(
    client: FlaskClient, data_file: Path
) -> None:
    client.post(ROUTE_ADD, data={**VALID_FORM, "cafe": "=1+1"})
    assert _lines(data_file)[-1].startswith("'=1+1,")
