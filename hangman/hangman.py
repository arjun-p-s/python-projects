import random
from words import words
import string

def get_random_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_random_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6


    while len(word_letters) > 0 and lives > 0:
        print(" you have", lives , " life  left You have used this letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print("the current word is: ", ' '.join(word_list))

        user_letters = input("guess a letter: ").upper()
        if user_letters in alphabet -used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives = lives - 1
                print("sorry the letter is not in the word ")


        elif user_letters in used_letters:
            print("you have alredy used that charector try again: ")
        else:
            print("you have typed an invalid charector, please try again")

        if lives == 0:
            print("sorry you died , the word is : ", word)
        else:
            print("heyyy you have guessed the word correctly congratulations")

hangman()