# Generate a random number between 1 and 9 (including). Ask the user to guess the number, 
# then tell them if they're too high. too low, or correct until they guess correctly

from random import randint

num = randint(1, 9)

def guessinggame():
    while True:
        guess = int(input("Guess a random number between 1 and 9: "))
    
        if guess > num:
            print("Your guess is too high.")
        elif guess < num:
            print("Your guess is too low.")
        else:
            print("You are correct!")
            return

guessinggame()
