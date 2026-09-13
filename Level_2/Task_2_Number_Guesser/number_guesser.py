import random

secret_number = random.randint(1, 100)

print("I have selected a number between 1 and 100.")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Correct! You guessed the number.")
else:
    print("Wrong guess! The correct number was:", secret_number)