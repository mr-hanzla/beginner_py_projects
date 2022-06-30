import random
from enum import Enum

class Game(Enum):
    rock = 'Rock'
    paper = 'Paper'
    scissor = 'Scissor'
    r = 'Rock'
    p = 'Paper'
    s = 'Scissor'

def get(val):
    if val == 'r':
        return Game.rock
    elif val == 'p':
        return Game.paper
    elif val == 's':
        return Game.scissor
    return val

def did_player_win(player, opponent):
    if (
        (player==Game.rock and opponent==Game.scissor) or
        (player==Game.scissor and opponent==Game.paper) or
        (player==Game.paper and opponent==Game.rock)
    ):
        return True
    return False


def play():
    user_turn = None
    while True:
        print('-'*30)
        user_turn = get(input('Rock(R), Paper(P), Scissor(S), or QUIT(Q): ').lower())
        if user_turn == 'q':
            print('Allah Hafiz')
            break
        computer_turn = random.choice([Game.rock, Game.paper, Game.scissor])
        if user_turn == computer_turn:
            print('It\'s a Tie!')
        elif did_player_win(user_turn, computer_turn):
            print('User won...')
        elif did_player_win(computer_turn, user_turn):
            print('Computer Won!!')
        print(f'User: {user_turn.value} | Computer: {computer_turn.value}')



if __name__ == '__main__':
    play()
