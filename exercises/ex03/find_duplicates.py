"""Finding duplicate letters in a word."""

__author__ = "730410711"

word: str = input("Enter a word: ")
counter_one: int = 0
counter_two: int = 0
duplicate: bool = False

while counter_one < len(word):
    counter_two = counter_one
    while counter_two < len(word) - 1:
        counter_two = counter_two + 1
        if word[counter_one] == word[counter_two]:
            duplicate = True
    counter_one = counter_one + 1

print("Found Duplicate: " + str(duplicate))
