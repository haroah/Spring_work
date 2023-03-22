import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        # ' ',.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives and you have already used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list =  [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
 
        user_letter = input('Guess an letter: ').upper()
    if user_letter in alphabet - user_letter:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

        else:
            lives = lives - 1 # takes away a life if wrong
            print('Letter is not in word.')

    elif user_letter in used_letters:
        print('You have already used that. Try again.')
    else:
        print('Invalid character. Please try agian.')

# gets here when len(word_letters) == 0 

hangman()

user_input = input('Type something')
print(user_input)