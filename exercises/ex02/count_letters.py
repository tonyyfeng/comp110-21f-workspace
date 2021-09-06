"""Counting letters in a string."""

__author__ = "730410711"


# Begin your solution here...
letter: str = input("What letter do you want to seach for?: ")
word: str = input("Enter a word: ")
length: int = len(word)
i: int = 0
letter_counter: int = 0
while i < length:
    specific_letter: str = word[i]
    i = i + 1
    if specific_letter == letter:
        letter_counter = letter_counter + 1
print("Count: " + str(letter_counter))