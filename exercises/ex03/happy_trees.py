"""Drawing forests in a loop."""

__author__ = "730410711"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
forest: str = ""
counter_one: int = 0
counter_two: int = 0

while counter_one < depth:
    counter_one = counter_one + 1
    forest = ""
    counter_two = 0
    while counter_two < counter_one:
        forest = forest + TREE
        counter_two = counter_two + 1
    print(forest)