"""Constants shared by every layer of Coffee and Wifi.

@file constants.py
@brief The single place for routes, file names, field names and limits.
"""

from pathlib import Path

## @brief Directory of the installed package.
PACKAGE_DIR: Path = Path(__file__).resolve().parent

## @brief Default location of the cafe data file.
DEFAULT_DATA_FILE: Path = PACKAGE_DIR / "data" / "cafe-data.csv"

## @brief Environment variable that overrides the data file location.
ENV_DATA_FILE: str = "COFFEE_AND_WIFI_DATA_FILE"

## @brief Environment variable that holds the Flask secret key.
ENV_SECRET_KEY: str = "SECRET_KEY"

## @brief Encoding of the CSV file (it holds emoji).
CSV_ENCODING: str = "utf-8"

## @brief Column names of the CSV file, in file order.
CSV_HEADER: tuple[str, ...] = (
    "Cafe Name",
    "Location",
    "Open",
    "Close",
    "Coffee",
    "Wifi",
    "Power",
)

## @brief Route of the home page.
ROUTE_HOME: str = "/"

## @brief Route of the cafe table.
ROUTE_CAFES: str = "/cafes"

## @brief Route of the secret form for adding a cafe.
ROUTE_ADD: str = "/add"

## @brief Text of the link that replaces a location URL in the table.
MAPS_LINK_TEXT: str = "Maps Link"

## @brief A value that starts with this text is treated as a link.
LINK_PREFIX: str = "http"

## @brief Rating choices of the coffee field.
COFFEE_CHOICES: tuple[str, ...] = ("☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️")

## @brief Rating choices of the wifi field.
WIFI_CHOICES: tuple[str, ...] = ("✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪")
## @brief Rating choices of the power field.
POWER_CHOICES: tuple[str, ...] = ("✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")
