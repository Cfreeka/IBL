import random

# Prompt the user for a level until a positive integer is entered
while True:
    level_str = input("Enter a level (a positive integer): ")
    try:
        level = int(level_str)
        if level <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Generate a random number between 1 and the level, inclusive
secret_number = random.randint(1, level)

# Prompt the user to guess the secret number until it's guessed correctly
while True:
    guess_str = input("Guess the secret number between 1 and {}: ".format(level))
    try:
        guess = int(guess_str)
        if guess <= 0:
            raise ValueError
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
