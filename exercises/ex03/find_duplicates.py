"""Finding duplicate letters in a word."""

__author__ = "730410711"

word: str = input("Enter a word: ")
counter_one: int = 0
counter_two: int = 0
duplicate: int = 0

while counter_one < len(word):
    counter_two = counter_one
    while counter_two < len(word) - 1:
        counter_two = counter_two + 1
        if word[counter_one] == word[counter_two]:
            duplicate = duplicate + 1
    counter_one = counter_one + 1

if duplicate > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")
