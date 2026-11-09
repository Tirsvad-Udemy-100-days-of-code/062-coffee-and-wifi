"""Tests for the cafe use cases with a fake repository."""

from coffee_and_wifi.application.add_cafe import AddCafe
from coffee_and_wifi.application.list_cafes import ListCafes
from coffee_and_wifi.domain.cafe import Cafe

CAFE = Cafe("Esters", "https://goo.gl/x", "8AM", "3PM", "☕️", "💪", "🔌")


class FakeCafeRepository:
    def __init__(self, cafes: list[Cafe] | None = None) -> None:
        self.cafes = list(cafes or [])

    def list_all(self) -> list[Cafe]:
        return list(self.cafes)

    def add(self, cafe: Cafe) -> None:
        self.cafes.append(cafe)


def test_list_cafes_returns_all_cafes_of_the_repository() -> None:
    assert ListCafes(FakeCafeRepository([CAFE])).execute() == [CAFE]


def test_list_cafes_returns_empty_list_when_repository_is_empty() -> None:
    assert ListCafes(FakeCafeRepository()).execute() == []


def test_add_cafe_stores_the_cafe_after_existing_ones() -> None:
    other = Cafe("Other", "https://x.y", "9AM", "5PM", "☕️", "✘", "✘")
    repository = FakeCafeRepository([CAFE])
    AddCafe(repository).execute(other)
    assert repository.cafes == [CAFE, other]
