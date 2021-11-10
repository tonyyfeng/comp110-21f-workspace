SECRET: int = 3

guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!")
else:
    print("Sorry you guessed incorrectly.")
    if guess > SECRET:
        print("you guessed too high!")
    else:
        print("you guessed too low!")
        

print("Game over.")