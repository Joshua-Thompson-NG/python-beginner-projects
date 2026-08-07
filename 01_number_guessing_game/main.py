# --- NUMBER GUESSING GAME ---
import random

computer_num = random.randint(1, 20)
attempts = 0

while True:

    try:
        user_input = int(input("Enter your guess (1-20): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if user_input < 1 or user_input > 20:
        print("Invalid input. Please enter a number between 1 and 20.")
        continue


    attempts += 1

    if user_input == computer_num:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif user_input < computer_num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")