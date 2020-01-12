import copy
import math
from ai.minimax import Minimax

class Player:
    def __init__(self, p_char):
        self.char = p_char
        self.is_player_turn = False

    def __str__(self):
        return self.char

    def is_turn(self):
        return self.is_player_turn

    def make_turn(self, is_turn: bool):
        self.is_player_turn = is_turn

    def get_turn_position(self, board):
        pos = input("Player-{}'s turn: ".format(self.char))
        if not board.is_space_available(pos):
            print('Space not available')
            return None
          
        return pos

class AI(Player):
    def __init__(self, p_char, opp_char):
        super().__init__(p_char)
        self.algo = Minimax(p_char, opp_char)

    # Override get_turn_position function here...
    def get_turn_position(self, game_board):
        g_board = copy.deepcopy(game_board)        
        board = g_board.get_board()

        best_pos = 0
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if g_board.is_space_available(board[row][col]):
                    pos = board[row][col] 
                    board[row][col] = self.char

                    score = self.algo.calculate(g_board, depth=5, isMaximizingPlayer=False)
                    board[row][col] = pos # Reset to original position
                    if score > best_score:
                        best_score = score
                        best_pos = pos

                    
        if not g_board.is_space_available(best_pos):
            return None

        return best_pos


