"""Practice with dictionaries."""

__author__ = "730410711"

# Define your functions below


def invert(invert: dict[str, str]) -> dict[str, str]:
    """This function will alter a dictionary so that the keys are the values and the values are the keys."""
    list_key: list[str] = list()
    list_value: list[str] = list()
    for key in invert:
        list_key.append(key)
    for value in invert:
        list_value.append(invert[value])
    i: int = 0
    counter: int
    while i < len(list_value):
        counter = i + 1
        while counter < len(list_value):
            if list_value[counter] == list_value[i]:
                raise KeyError("The dictionary you provided has duplicate values and thus cannot be reversed!")
            counter += 1
        i += 1
    i = 0
    new_dictionary: dict[str, str] = dict()
    while i < len(invert):
        new_dictionary[list_value[i]] = list_key[i]
        i += 1
    return new_dictionary


def favorite_color(colors: dict[str, str]) -> str:
    """Given a dictionary full of names of people and their favorite colors, this function will return the color that is the favorite of the most people."""
    count_color: dict[str, int] = dict()
    for key in colors:
        if colors[key] in count_color:
            count_color[colors[key]] += 1
        else:
            count_color[colors[key]] = 1
    counter: int = 0
    for color in count_color:
        counter = 0
        for color_compare in count_color:
            if count_color[color] >= count_color[color_compare]:
                counter += 1
                if counter == len(count_color):
                    return color
    return "No Color"


def count(list_counted: list[str]) -> dict[str, int]:
    """Given a list of strings, return a dictionary with how many times elements in that list are repeated."""
    counter: dict[str, int] = dict()
    for item in list_counted:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter