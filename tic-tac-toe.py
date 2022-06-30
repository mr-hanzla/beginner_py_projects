from ttt_players import HumanPlayer, ComputerPlayer, AiPlayer
import random


class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot==' ']
    
    def is_spot_available(self):
        return ' ' in self.board

    def num_empty_spots(self):
        return self.board.count(' ')
    
    def is_valid_spot(self, spot):
        return self.board[spot] == ' '

    def win_check(self, letter, opp_letter, spots):
        return ' ' not in spots and letter in spots and opp_letter not in spots
    
    def winner(self, spot, letter):
        row_index = spot // 3
        col_index = spot % 3
        row = self.board[row_index*3:row_index*3+3]
        col = self.board[col_index::3]
        rdig = self.board[0::3+1]
        ldig = self.board[3-1:len(self.board)-(3-1):3-1]
        if (
            all([i==letter for i in row]) or
            all([i==letter for i in col]) or
            all([i==letter for i in rdig]) or
            all([i==letter for i in ldig])
        ):
            return True
        return False

    def make_move(self, spot, letter):
        if self.is_valid_spot(spot):
            self.board[spot] = letter
            if self.winner(spot, letter):
                self.current_winner = letter
            return True
        return False
    
    def print_board(self):
        for row in [self.board[i*3:i*3+3] for i in range(3)]:
            print('|', ' | '.join(row), '|')
        print('')

    
    @staticmethod
    def print_board_numbers():
        for row in [[str(i) for i in range(j*3, j*3+3)] for j in range(3)]:
            print('|', ' | '.join(row), '|')


def play(game, x_player, o_player):
    letter = 'O'
    while game.is_spot_available():
        input_spot = None
        if letter == 'X':
            input_spot = x_player.game_move(game)
        else:
            input_spot = o_player.game_move(game)

        if game.make_move(input_spot, letter):
            print(f'Player {letter} made a move at {input_spot}')
            game.print_board()

            if game.current_winner:
                print(f'Player {letter} won...!')
                return letter

            letter = 'O' if letter=='X' else 'X'
    print('It\'s a Tie...no one won!')
    return None

if __name__ == '__main__':
    game = TicTacToe()
    x_player = AiPlayer('X')
    o_player = HumanPlayer('O')
    TicTacToe.print_board_numbers()
    play(game, x_player, o_player)
