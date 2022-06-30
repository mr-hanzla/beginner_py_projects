from words import words
from man import *
import random

def show_part(part):
    switcher = {
        0: part0,
        1: part1,
        2: part2,
        3: part3,
        4: part4,
        5: part5,
        6: part6,
    }
    print(switcher.get(part, ''))

def get_blanks(word):
    return (len(word)//2)+1


def get_unique_blank_points(word):
    blank_points = set()
    blanks = get_blanks(word)
    while len(blank_points) != blanks:
        blank_points.add(random.randint(0, len(word)-1))
    return blank_points


def get_word_with_blanks(word):
    word_copy = list(word)
    blank_points = get_unique_blank_points(word)
    for blank_point in blank_points:
        word_copy[blank_point] = '_'
    return ''.join(word_copy)

def update_word(word, index, char):
    temp_word = list(word)
    temp_word[index] = char
    return ''.join(temp_word)


def update_word_with_occurances(word, occurances, char):
    for occurance in occurances:
        word = update_word(word, occurance, char)
    return word
 
def get_occurance_of_character(word, char):
    index = -1
    char = char.lower()
    char_occurances = list()
    while word.lower().find(char) != -1:
        index = word.lower().find(char)
        char_occurances.append(index)
        word = update_word(word, index, '_')
    return char_occurances

def validate_occs(occs, pre_occs):
    for occ in occs:
        if occ not in pre_occs:
            return True
    return False

def get_random_word():
    word = '-'
    while word.find(' ')!=-1 or word.find('-')!=-1:
        word = words[random.randint(0, len(words)-1)]
    return word

def get_pre_occs(word):
    temp = list()
    for i in range(len(word)):
        if word[i] != '_':
            temp.append(i)
    return temp


if __name__ == '__main__':
    word = get_random_word()
    print(word)

    user_word = get_word_with_blanks(word)

    pre_occs = get_pre_occs(user_word)

    mistake_count = 0
    show_part(mistake_count)

    while mistake_count != 6:
        print(user_word)

        user_input_char = input('Enter a character: ')

        occurances = get_occurance_of_character(word, user_input_char)
        print(occurances)
        print(pre_occs)
        if occurances and validate_occs(occurances, pre_occs):
            user_word = update_word_with_occurances(user_word, occurances, user_input_char)
            pre_occs = get_pre_occs(user_word)
            if word == user_word:
                print(word)
                print(user_word)
                print('You WON!')
                break
        else:
            mistake_count += 1
            show_part(mistake_count)



