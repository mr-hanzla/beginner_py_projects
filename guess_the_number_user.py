import random


def guess_the_number(num):
    random_number = random.randint(1, num)
    guess_num = 0
    while guess_num != random_number:
        guess_num = int(input('Guess the number: '))
        if guess_num < random_number:
            print('Getting close...keep trying!')
        elif guess_num > random_number:
            print('Hold on, you moved passed it, go Back!')
    print(f'My nigga! You guessed the number correctly {random_number}....have fun')



if __name__ == '__main__':
    guess_the_number(20)
