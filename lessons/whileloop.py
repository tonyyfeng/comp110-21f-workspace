counter: int = 0
maximum: int = int(input("Count up to but not including what? "))

while counter < maximum:
    counter_sqrd: int = counter ** 2
    print("the square of " + str(counter) + " is " + str(counter_sqrd))
    counter = counter + 1
print("Done!")

import random
bla: int = random.randint(1, 10)
print(bla)
