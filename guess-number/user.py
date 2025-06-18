import random

def guess_number(number):
    random_number = random.randint(1,number)
    guess = 0
    while random_number != guess:
        guess= int(input(f"Guess a number between 1 and {number}:  "))
        if random_number < guess:
         print("Sorry, its too high")
        elif random_number > guess:
         print("Sorry, its too low")
        else:
         print(f"hey you have guessed the {random_number} correct")

guess_number(10)


