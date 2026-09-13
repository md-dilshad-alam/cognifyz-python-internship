import random

secret_number = random.randint(1, 100)

print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Correct! You guessed the number.")
        break