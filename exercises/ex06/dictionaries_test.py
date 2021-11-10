"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count


__author__ = "730410711"


def test_invert_edge() -> None:
    """Tests an empty dictionary."""
    xs: dict[str, str] = dict()
    assert invert(xs) == {}


def test_invert_normal_one() -> None:
    """Tests a normal use case of strings and strings."""
    xs: dict[str, str] = {"hi": "yo", "boo": "ahhh", "what": "nothing"}
    assert invert(xs) == {"yo": "hi", "ahhh": "boo", "nothing": "what"}


def test_invert_normal_two() -> None:
    """Tests another normal use case of different strings."""
    xs: dict[str, str] = {"123": "456", "789": "0", "345": "678"}
    assert invert(xs) == {"456": "123", "0": "789", "678": "345"}


def test_favorite_color_empty_dictionary() -> None:
    """Tests an empty dictionary."""
    xs: dict[str, str] = dict()
    assert favorite_color(xs) == "No Color"


def test_favorite_color_blue() -> None:
    """Tests a scenario where the favorite color is blue."""
    xs: dict[str, str] = {"asdf": "blue", "hello": "red", "chicken": "green", "bob": "green", "bib": "blue", "yo": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_tied_colors() -> None:
    """Tests a scanrio where there are multiple colors with the most amount of people having them as their favorite."""
    xs: dict[str, str] = {"asdf": "blue", "hello": "red", "chicken": "green", "bob": "green", "bib": "blue", "yo": "red"}
    assert favorite_color(xs) == "blue"


def test_count_empty_list() -> None:
    """Tests when the input is an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_list_of_one_word() -> None:
    """Tests a list of strings that are all identical."""
    xs: list[str] = ["hello", "hello", "hello", "hello", "hello", "hello", "hello"]
    assert count(xs) == {"hello": 7}


def test_count_regular_list() -> None:
    """Tests a regular string of various lists."""
    xs: list[str] = ["hello", "yo", "hi", "hello", "hi", "what up", "what up", "ok"]
    assert count(xs) == {"hello": 2, "yo": 1, "hi": 2, "what up": 2, "ok": 1}