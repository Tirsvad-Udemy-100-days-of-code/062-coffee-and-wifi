"""The cafe repository port.

@file cafe_repository.py
@brief The storage contract the use cases need, defined by the business.
"""

from typing import Protocol

from coffee_and_wifi.domain.cafe import Cafe


class CafeRepository(Protocol):
    """Reads and stores cafes."""

    def list_all(self) -> list[Cafe]:
        """Return every stored cafe in storage order."""
        ...

    def add(self, cafe: Cafe) -> None:
        """Store one more cafe after the existing ones."""
        ...
