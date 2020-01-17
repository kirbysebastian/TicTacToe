import copy
import math

from utils.utilities import is_winner

'''
Board Position Representation
 1 | 2 | 3
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9
'''
class Minimax():
    def __init__(self, player_char, opp_char):
        self.char = player_char
        self.x_char = opp_char
    
    def calculate(self, game_board, depth, isMaximizingPlayer):
        g_board = copy.deepcopy(game_board)
        board = g_board.get_board()

        if depth == 0 or self.is_terminal(g_board):
            return self.get_board_score(board)

        if isMaximizingPlayer is True:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if g_board.is_space_available(board[row][col]):
                        pos = board[row][col] 
                        board[row][col] = self.char
                        best_score = max(best_score, self.calculate(g_board, depth-1, False))
                        board[row][col] = pos

            return best_score

        else: # MinimizingPlayer
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if g_board.is_space_available(board[row][col]):
                        pos = board[row][col] 
                        board[row][col] = self.x_char
                        best_score = min(best_score, self.calculate(g_board, depth-1, True))
                        board[row][col] = pos

            return best_score

    def is_terminal(self, game_board):
        board = game_board.get_board()
        return game_board.is_full() or is_winner(board, self.char) or is_winner(board, self.x_char)

    def get_board_score(self, board):
        if is_winner(board, self.char):
            return 1
        elif is_winner(board, self.x_char):
            return -1
        else:
            return 0

