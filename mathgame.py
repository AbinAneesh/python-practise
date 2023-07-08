# Guess the Number Game

import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Set the number of guesses to zero
num_guesses = 0

# Loop until the user guesses the correct number or runs out of guesses
while num_guesses < 3:
    # Prompt the user to guess a number
    guess = int(input("Guess a number between 1 and 10: "))

    # Increment the number of guesses
    num_guesses += 1

    # Check if the user's guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break

    # Check if the user's guess is too high or too low
    elif guess < number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")

# If the user has used up all their guesses without guessing the correct number
if num_guesses == 3:
    print("Sorry, you've run out of guesses. The number was", number)
    