"""An example function definition."""


def my_max(a: int, b: int) -> int:
    """returns largest argument"""
    if a >= b:
        return a
    else:
        return b

print(my_max(4, 2))