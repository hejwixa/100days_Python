import random

# Welcome message and difficulty selection
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

# Setting the number of attempts based on difficulty
if difficulty == "hard":
    attempts = 5
elif difficulty == "easy":
    attempts = 10
else:
    print("Invalid input. Please type 'easy' or 'hard'.")
    exit()

# Generate random number to guess
number_to_guess = random.randint(1,100)

# Function to compare the guessed number with the target number
def compare(guess, number_to_guess):
    if guess > number_to_guess:
        return "Too high."
    elif guess < number_to_guess:
        return "Too low."
    elif guess == number_to_guess:
        return "Correct!"

# Main game loop
while attempts > 0:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess:\n"))
    result = compare(guess, number_to_guess)
    print(result)

    if result == "Correct!":
        print("You've guessed the number. You win!")
        break

    attempts -= 1

    if attempts == 0:
        print("You've run out of attempts. You lose!")
        print(f"The correct number was {number_to_guess}.")
