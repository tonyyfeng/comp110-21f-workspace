"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730410711"


def test_only_evens_edge() -> None:
    """Tests only_evens when the list is empty."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_just_evens() -> None:
    """Test only_evens when all even."""
    xs: list[int] = [4, 2, 6, 8, 10, 12]
    assert only_evens(xs) == xs


def test_only_evens_and_odds() -> None:
    """Tests only_evens when odds and evens are mixed."""
    xs: list[int] = [2, 3, 5, 4545, 57, 75, 4]
    assert only_evens(xs) == [2, 4]


def test_sub_indexes_out_of_bounds() -> None:
    """Tests when the start index is too high or the end index is too low."""
    xs: list[int] = [2, 4, 5, 7, 8]
    assert sub(xs, 100, -111) == []


def test_sub_with_indexes_too_low_and_too_high() -> None:
    """Tests when the start index is lower than zero and the end index is higher than any index on the list."""
    xs: list[int] = [2, 4, 5, 6, 7, 8, 9]
    assert sub(xs, -100, 10) == xs


def test_sub_with_normal_indexes() -> None:
    """Tests normal conditions for the sub function."""
    xs: list[int] = [1, 2, 4, 5, 7, 8, 9]
    assert sub(xs, 3, 6) == [5, 7, 8]


def test_concat_edge_case() -> None:
    """Tests edge case for concat when both lists are empty."""
    xs_one: list[int] = []
    xs_two: list[int] = []
    assert concat(xs_one, xs_two) == []


def test_concat_equal_length() -> None:
    """Tests when both concat lists are of equal length."""
    xs_one: list[int] = [1, 2, 3, 4]
    xs_two: list[int] = [-1, -2, -3, -4]
    assert concat(xs_one, xs_two) == [1, 2, 3, 4, -1, -2, -3, -4]


def test_concat_different_lengths() -> None:
    """Tests when both concat lists are of different lengths."""
    xs_one: list[int] = [1, 2, 3]
    xs_two: list[int] = [6, 7, 8, 9]
    assert concat(xs_one, xs_two) == [1, 2, 3, 6, 7, 8, 9]