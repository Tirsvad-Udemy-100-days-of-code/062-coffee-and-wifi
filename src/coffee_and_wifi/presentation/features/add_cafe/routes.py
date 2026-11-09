"""Route of the secret add form.

@file routes.py
@brief Shows the form and stores a valid submission.
"""

from collections.abc import Callable

from flask import Flask, redirect, render_template, url_for
from werkzeug.wrappers import Response

from coffee_and_wifi.application.add_cafe import AddCafe
from coffee_and_wifi.constants import ENDPOINT_ADD, ENDPOINT_CAFES, ROUTE_ADD
from coffee_and_wifi.presentation.features.add_cafe.form import CafeForm


def make_add_cafe(add_cafe_use_case: AddCafe) -> Callable[[], str | Response]:
    """Build the view function that adds cafes with the given use case."""

    def add_cafe() -> str | Response:
        """Show the form; store a valid submission and go to the table."""
        form = CafeForm()
        if form.validate_on_submit():
            add_cafe_use_case.execute(form.to_cafe())
            return redirect(url_for(ENDPOINT_CAFES))
        return render_template("add.html", form=form)

    return add_cafe


def register(app: Flask, add_cafe_use_case: AddCafe) -> None:
    """Add the add-cafe route to the app (no page links to it)."""
    app.add_url_rule(
        ROUTE_ADD,
        endpoint=ENDPOINT_ADD,
        view_func=make_add_cafe(add_cafe_use_case),
        methods=["GET", "POST"],
    )
