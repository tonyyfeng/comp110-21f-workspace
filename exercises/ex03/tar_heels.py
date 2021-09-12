"""An exercise in remainders and boolean logic."""

__author__ = "730410711"


# Begin your solution here...
integer: int = int(input("Enter an int: "))
phrase: str = ""
if (integer % 2) == 0:
    phrase = phrase + "TAR"
if (integer % 7) == 0:
    if (integer % 2) == 0:
        phrase = phrase + " "
    phrase = phrase + "HEELS"
else:
    if (integer % 2) != 0:
        print("CAROLINA")

print(phrase)
