"""This program is meant to have the user input two variables and then show the user using those two variables how the four interesting numerical operators work in Python"""
__author__ = "730410711"
left_number: int = int(input("What is the left-hand side number? (enter an integer) "))
right_number: int = int(input("What is the right-hand side number? (enter an integer) "))
print("Left-hand side: " + str(left_number))
print("Right-hand side: " + str(right_number))
print(str(left_number) + " ** " + str(right_number) + " is " + str(left_number ** right_number))
print(str(left_number) + " / " + str(right_number) + " is " + str(left_number / right_number))
print(str(left_number) + " // " + str(right_number) + " is " + str(left_number // right_number))
print(str(left_number) + " % " + str(right_number) + " is " + str(left_number % right_number))
