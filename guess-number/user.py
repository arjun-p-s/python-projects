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


def computer_guess(number):
  low = 1
  high = number
  feedback = ''
  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low
    feedback = input(f"hey the guess is {guess} is high for (h), low for (l), is it correct (c)")
    if feedback == 'l':
      low = guess+1
    elif feedback == 'h':
      high = guess - 1
  print("hey we have guessed  correctly...")
      
      
    
  

computer_guess(100)


