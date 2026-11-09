"""The list-cafes use case.

@file list_cafes.py
@brief Returns all cafes held by the repository.
"""

from coffee_and_wifi.domain.cafe import Cafe
from coffee_and_wifi.domain.cafe_repository import CafeRepository


class ListCafes:
    """Lists every cafe."""

    def __init__(self, repository: CafeRepository) -> None:
        """Create the use case with the repository it reads from."""
        self._repository = repository

    def execute(self) -> list[Cafe]:
        """Return all cafes."""
        return self._repository.list_all()
