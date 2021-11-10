"""Examples of imports."""

from lessons import helpers
"""When importing a module it fully evaluates the module, so it'll run print statements and stuff like that."""
"""When importing a module, it'll import where it comes from, but when runnign a module, it'll be __name__"""

# import using an alias
from lessons import helpers as hp

# Import names directly from globals of a module
from lessons.helpers import powerful
# Imports should be at top of file


def main() -> None:
    print(powerful(2,10))

    print(helpers.powerful(2, 4))

    print(helpers.THE_ANSWER)

    print(f"imports.py: {__name__}")

    print(hp.THE_ANSWER)


if __name__ == "__main__":
    main()