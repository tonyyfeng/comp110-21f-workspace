"""List utility functions."""

__author__ = "730410711"


# TODO: Implement your functions here.
def all(search: list[int], specific_number: int) -> bool:
    """Determines if all the list values matches a specific integer."""
    i: int = 0
    length: int = len(search)
    if length == 0:
        return False
    while i < length:
        if search[i] == specific_number:
            i += 1
        else: 
            return False
    return True


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Determines if two lists are exactly the same."""
    i: int = 0
    length_one: int = len(list_one)
    length_two: int = len(list_two)
    if length_one != length_two:
        return False
    else:
        while i < len(list_one):
            if list_one[i] == list_two[i]:
                i += 1
            else:
                return False
    return True


def max(maximum_list: list[int]) -> int:
    """Determines the maximum in a list of integers."""
    if len(maximum_list) == 0:
        raise ValueError("max() arg is an empty List")
    maximum: int = maximum_list[0]
    i: int = 1
    while i < len(maximum_list):
        if maximum_list[i] > maximum:
            maximum = maximum_list[i]
        i += 1
    return maximum
    