"""Route of the cafe table.

@file routes.py
@brief Shows every cafe in a Bootstrap table.
"""

from collections.abc import Callable

from flask import Flask, render_template

from coffee_and_wifi.application.list_cafes import ListCafes
from coffee_and_wifi.constants import ENDPOINT_CAFES, ROUTE_CAFES
from coffee_and_wifi.presentation.features.cafes.view_model import build_rows


def make_cafes(list_cafes: ListCafes) -> Callable[[], str]:
    """Build the view function that lists cafes with the given use case."""

    def cafes() -> str:
        """Render the table of all cafes."""
        return render_template("cafes.html", cafes=build_rows(list_cafes.execute()))

    return cafes


def register(app: Flask, list_cafes: ListCafes) -> None:
    """Add the cafes route to the app."""
    app.add_url_rule(
        ROUTE_CAFES, endpoint=ENDPOINT_CAFES, view_func=make_cafes(list_cafes)
    )
