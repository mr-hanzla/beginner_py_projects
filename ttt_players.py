import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter # 'X' or 'O'
    
    def game_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def game_move(self, game):
        input_spot = input_spot = input(f'(Player-{self.letter})Select a spot from {game.available_moves()}: ')
        try:
            input_spot = int(input_spot)
            if input_spot not in game.available_moves():
                raise ValueError
        except ValueError:
            print('Invalid Value! Try Again!')
        # while input_spot not in spots:
        #     print('Invalid spot or spot not available, Try Again')
        #     input_spot = int(input(f'Select a spot from {spots}: '))
        return input_spot


class ComputerPlayer(Player):
    def __init(self, letter):
        super().__init__(letter)

    def game_move(self, game):
        return random.choice(game.available_moves())


class AiPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def game_move(self, game):
        if game.available_moves() == 9:
            input_spot = random.choice(game.available_moves())
        else:
            input_spot = self.minimax(game, self.letter)['position']
        return input_spot
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player=='X' else 'X'

        # base case(s)
        if state.current_winner == other_player: # this can be set to check as != None
            return {
                'position': None,
                'score': 1*(state.num_empty_spots()+1) if other_player==max_player else -1*(state.num_empty_spots()+1)
            }
        elif not state.is_spot_available():
            return {'position': None, 'score': 0}
        
        # initialize some dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)
            # step 3: undo that move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

