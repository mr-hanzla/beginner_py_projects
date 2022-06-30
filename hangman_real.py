import random
from words import words
import string
from man import *

def show_part(part):
    switcher = {
        0: part0,
        6: part1,
        5: part2,
        4: part3,
        3: part4,
        2: part5,
        1: part6,
    }
    print(switcher.get(part, '\t'))

def get_random_word():
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

def play_hangman():
    word = get_random_word()
    print(word)
    word_set = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_set) > 0 and lives > 0:
        print(f"\n\nCurrent Word: {' '.join([letter if letter not in word_set else '_' for letter in word])}")
        print(f"Already Used Letters: {' '.join(used_letters)}")
        user_input = input('Guess a letter: ').upper()

        if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            if user_input in word_set:
                word_set.remove(user_input)
            else:
                show_part(lives)
                lives -= 1
        elif user_input in used_letters:
            print('----->>>>>>Letter Already Used')
        else:
            print('----->>>>>>Invalid Input')
    if lives > 0:
        print('Voila, You guess the word, {}'.format(word))
    else:
        print('You Lost!!!!!')



if __name__ == '__main__':
    play_hangman()


