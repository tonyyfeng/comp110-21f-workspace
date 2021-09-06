"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730410711"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune: int = randint(1, 4)
print("Your fortune cookie says...")
if fortune == 1:
    print("You will recieve $100000 tomorrow!")
else:
    if fortune == 2:
        print("You will find a chocolate chip cookie tomorrow and it will be delicious!")
    else:
        if fortune == 3:
            print("Absolutely nothing of note will happen tomorrow.")
        else:
            if fortune == 4:
                print("You will be able to make money doing whatever your dream job is for the rest of your life!")
print("Now, go spread positive vibes!")