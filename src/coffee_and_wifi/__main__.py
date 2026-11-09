"""Command line entry point.

@file __main__.py
@brief Runs the development server with `python -m coffee_and_wifi`.
"""

from coffee_and_wifi.constants import DEBUG, HOST, PORT
from coffee_and_wifi.presentation.app import create_app


def main() -> None:
    """Start the development server."""
    create_app().run(host=HOST, port=PORT, debug=DEBUG)


if __name__ == "__main__":
    main()
