import random

random_number = random.randint(1,10)  # numbers 1 - 10
guess = None

while guess != random_number:
    guess = input("Guess a number between 1 and 10: ")
    if guess:
        guess = int(guess)
        if guess > random_number:
            print(f"Too high, Try again!")
        elif guess < random_number:
            print(f"Too low, Try again!")
        else:
            print(f"You guessed it! You win!")
