from email.mime.application import MIMEApplication
import random
from xmlrpc.client import MAXINT, MININT


def guess_the_number_computer(num):
    min_int = MININT
    max_int = MAXINT
    guess_num = 0
    while guess_num != num:
        guess_num = random.randint(min_int, max_int)
        if guess_num < num:
            min_int = guess_num
            print('Computer is getting close.... guessed > {}'.format(guess_num))
        elif guess_num > num:
            max_int = guess_num
            print('Computer Passed the value... guessed > {}'.format(guess_num))
        
    print(f'COmputer guess your number {num}... Enjoy da life...')


guess_the_number_computer(450)
print(MAXINT)
print(MININT)
