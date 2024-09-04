import random

print("Welcome to the Number Guessing Game!")


num = random.randrange(1, 100)

diff = input("Choose a difficulty. Type 'easy or 'hard': ")
if diff == "hard":
    tries = 5
else:
    tries = 10

while tries != 0:
    print(f"You have {str(tries)} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess != num:
        if guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
        tries -= 1
    else:
        print("That correct! Congrats")
        tries = 0

print("Game Over")


