"""List utility functions part 2."""

__author__ = "730410711"

# Define your functions below


def only_evens(original_list: list[int]) -> list[int]:
    """Returns only the even elements of a list of integers."""
    if len(original_list) == 0:
        return list()
    even_list: list[int] = list()
    for number in original_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def sub(original_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a start and end index and a list, will provide a list between those two indices including the start index but excluding the end index."""
    if len(original_list) == 0:
        return list()
    sub_list: list[int] = list()
    if start_index < 0:
        start_index = 0
    if end_index > (len(original_list)):
        end_index = len(original_list)
    while start_index < end_index:
        sub_list.append(original_list[start_index])
        start_index += 1
    return sub_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given two lists, this function will concatonate them into one list."""
    concat_list: list[int] = list()
    for list_item in list_one:
        concat_list.append(list_item)
    for list_item in list_two:
        concat_list.append(list_item)
    return concat_list