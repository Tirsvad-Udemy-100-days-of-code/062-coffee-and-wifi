"""Application factory and composition root.

@file app.py
@brief Builds the Flask app and wires the repository into the use cases.
"""

import os
import secrets
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from flask import Flask
from flask_bootstrap import Bootstrap5

from coffee_and_wifi.application.add_cafe import AddCafe
from coffee_and_wifi.application.list_cafes import ListCafes
from coffee_and_wifi.constants import (
    CONFIG_DATA_FILE,
    DEFAULT_DATA_FILE,
    ENV_DATA_FILE,
    ENV_SECRET_KEY,
    SECRET_KEY_BYTES,
    STATIC_DIR,
    TEMPLATES_DIR,
)
from coffee_and_wifi.infrastructure.csv_cafe_repository import CsvCafeRepository
from coffee_and_wifi.presentation.features.add_cafe import routes as add_cafe_routes
from coffee_and_wifi.presentation.features.cafes import routes as cafes_routes
from coffee_and_wifi.presentation.features.home import routes as home_routes


# Any: Flask config values have no common type.
def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    """Create the app; test_config overrides the environment based settings."""
    app = Flask(
        __name__,
        template_folder=str(TEMPLATES_DIR),
        static_folder=str(STATIC_DIR),
    )
    app.config["SECRET_KEY"] = os.environ.get(
        ENV_SECRET_KEY, secrets.token_hex(SECRET_KEY_BYTES)
    )
    app.config[CONFIG_DATA_FILE] = Path(
        os.environ.get(ENV_DATA_FILE, str(DEFAULT_DATA_FILE))
    )
    if test_config is not None:
        app.config.update(test_config)

    Bootstrap5(app)
    repository = CsvCafeRepository(Path(app.config[CONFIG_DATA_FILE]))
    home_routes.register(app)
    cafes_routes.register(app, ListCafes(repository))
    add_cafe_routes.register(app, AddCafe(repository))
    return app
