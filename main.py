import random
import art


def get_num():
    return random.randrange(1, 101)


def check_guess(guess, answer):
    if guess < answer:
        print("Too low")
        return False
    elif guess > answer:
        print("Too high")
        return False
    else:
        print("That's correct! Congrats")
        return True


def replay():
    re = input("Do you want to play again?").lower()
    if re == "yes":
        play_game()
    else:
        print("Goodbye")


def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")

    answer = get_num()
    diff = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
    if diff == "hard":
        tries = 5
    else:
        tries = 10

    while tries > 0:
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if check_guess(guess, answer):
            break  # Exit the loop if the guess is correct

        tries -= 1  # Decrement tries after each guess

    if tries == 0:
        print(f"Game Over. The correct number was {answer}.")

    replay()


play_game()
