"""Route of the home page.

@file routes.py
@brief Shows the landing page with the button to the cafe table.
"""

from flask import Flask, render_template

from coffee_and_wifi.constants import ENDPOINT_HOME, ROUTE_HOME


def home() -> str:
    """Render the home page."""
    return render_template("index.html")


def register(app: Flask) -> None:
    """Add the home route to the app."""
    app.add_url_rule(ROUTE_HOME, endpoint=ENDPOINT_HOME, view_func=home)
