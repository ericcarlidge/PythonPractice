# Generate a random number between 1 and 9 (including). Ask the user to guess the number, 
# then tell them if they're too high. too low, or correct until they guess correctly.

from random import randint

num = randint(1, 9)

def guessinggame():
    count = 0
    while True:
        guess = int(input("Guess a number between 1 and 9: "))
    
        if guess > num:
            count += 1
            print("Your guess is too high.")
        elif guess < num:
            count += 1
            print("Your guess is too low.")
        else:
            count += 1
            print("You are correct!")
            print("You guessed the number in " + str(count) + " guess(es)!")
            return

guessinggame()

