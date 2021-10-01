"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730410711"


def test_only_evens_edge() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_just_evens() -> None:
    xs: list[int] = [4, 2, 6, 8, 10, 12]
    assert only_evens(xs) == xs


def test_only_evens_and_odds() -> None:
    xs: list[int] = [2, 3, 5, 4545, 57, 75, 4]
    assert only_evens(xs) == [2, 4]


def test_sub_indexes_out_of_bounds() -> None:
    xs: list[int] = [2, 4, 5, 7, 8]
    assert sub(xs, 100, -111) == []


def test_sub_with_indexes_too_low_and_too_high() -> None:
    xs: list[int] = [2, 4, 5, 6, 7, 8, 9]
    assert sub(xs, -100, 10) == xs


def test_sub_with_normal_indexes() -> None:
    xs: list[int] = [1, 2, 4, 5, 7, 8, 9]
    assert sub(xs, 3, 6) == [5, 7, 8]


def test_concat_edge_case() -> None:
    xs_one: list[int] = []
    xs_two: list[int] = []
    assert concat(xs_one, xs_two) == []


def test_concat_equal_length() -> None:
    xs_one: list[int] = [1, 2, 3, 4]
    xs_two: list[int] = [-1, -2, -3, -4]
    assert concat(xs_one, xs_two) == [1, 2, 3, 4, -1, -2, -3, -4]


def test_concat_different_lengths() -> None:
    xs_one: list[int] = [1, 2, 3]
    xs_two: list[int] = [6, 7, 8, 9]
    assert concat(xs_one, xs_two) == [1, 2, 3, 6, 7, 8, 9]