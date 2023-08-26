import random

def guess_number():
    print("Welcome to Guess the Number Game!")
    secret_number = random.randint(1, 10)  # Generate a random number between 1 and 10
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess == secret_number:
                print("Congratulations! You guessed the correct number!")
                break  # Exit the loop if the guess is correct
            elif guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
            else:
                print("Wrong guess. Try again!")
        except ValueError:
            print("Invalid input. Please enter a number.")

guess_number()
