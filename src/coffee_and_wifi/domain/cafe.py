"""The cafe entity.

@file cafe.py
@brief A cafe with its opening hours and its coffee, wifi and power ratings.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Cafe:
    """A cafe a person can work from."""

    name: str
    location: str
    open_time: str
    close_time: str
    coffee: str
    wifi: str
    power: str
