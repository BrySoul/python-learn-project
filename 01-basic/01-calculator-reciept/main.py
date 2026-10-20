import random

# Game configuration
secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("=" * 45)
print(f"{'Welcome to the Number Guessing Game!':^45}")
print("=" * 45)
print("Guess the secret number between 1 and 100.")
print(f"You have a total of {max_attempts} attempts. Good Luck!\n")

# Main game loop
while attempts < max_attempts:
    user_input = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")

    # Input validation
    if not user_input.isdigit():
        print("Invalid input! Please enter a number between 1 and 100.\n")
        continue

    guess = int(user_input)
    attempts += 1

    # Hint Logic
    if guess < secret_number:
        print("Too low! Try a higher number.\n")
    elif guess > secret_number:
        print("Too high! Try a lower number.\n")
    else:
        print("\n" + "*" * 45)
        print(
            f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!"
        )
        print("*" * 45)
        break
else:
    print("\n" + "*" * 45)
    print(f"Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")
    print("*" * 45)
