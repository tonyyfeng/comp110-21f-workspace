"""Utility functions."""

__author__ = "730410711"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    """Only select the first X rows of data from a CSV file."""
    header: dict[str, list[str]] = {}
    i: int = 0
    for column in table:
        item: list[str] = []
        while i < row_number:
            item.append(table[column][i])
            i += 1
        i = 0
        header[column] = item
    return header


def select(table: dict[str, list[str]], selecting: list[str]) -> dict[str, list[str]]:
    """Select only certain columns of data."""
    selected: dict[str, list[str]] = {}
    for column in selecting:
        selected[column] = table[column]
    return selected


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Make a table that is the combination of two other tables."""
    concated: dict[str, list[str]] = {}
    for column in table_one:
        concated[column] = table_one[column]
    for column in table_two:
        if column in concated:
            for data_point in table_two[column]:
                concated[column].append(data_point)
        else:
            concated[column] = table_two[column]
    return concated


def count(keys: list[str]) -> dict[str, int]:
    """Count the number of times an item appears in a list of strings."""
    counted: dict[str, int] = {}
    for key in keys:
        if key in counted:
            counted[key] += 1
        else:
            counted[key] = 1
    return counted


def addition_interest(table: dict[str, list[str]], majors: list[str], number_of_major: int) -> float:
    """Counts the average interest in the subject."""
    i: int = 0
    total_interest: int = 0
    average_interest: float
    for major in majors:
        i = 0
        while i < len(table["comp_major"]):
            if table["comp_major"][i] == major:
                total_interest += int(table["interesting"][i])
            i += 1
    average_interest = total_interest / number_of_major
    return average_interest
        
