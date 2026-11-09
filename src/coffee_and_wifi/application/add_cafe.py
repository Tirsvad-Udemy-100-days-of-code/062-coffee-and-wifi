"""The add-cafe use case.

@file add_cafe.py
@brief Stores one new cafe in the repository.
"""

from coffee_and_wifi.domain.cafe import Cafe
from coffee_and_wifi.domain.cafe_repository import CafeRepository


class AddCafe:
    """Adds a cafe."""

    def __init__(self, repository: CafeRepository) -> None:
        """Create the use case with the repository it writes to."""
        self._repository = repository

    def execute(self, cafe: Cafe) -> None:
        """Store the cafe."""
        self._repository.add(cafe)
