import copy
import math

# STILL TODO

'''
Board Position Representation
 1 | 2 | 3
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9
'''

# STEPS
# - Loops to every space in board
# - Check if space is available then place position
# - Check if there is winner

# WHAT WE NEED??
# - Function that can check if space is available in board
# - Function that checks the current board state's winner
#
#
#
#
#
#
#
#
score = {

    }

# GOAL: Returns the best position available in board
class Minimax():
    def __init__(self, player_char, opp_char):
        self.char = player_char
        self.x_char = opp_char
    
    def check_board_state(self):
        pass
    
    def calculate(self, game_board, depth, isMaximizingPlayer) -> tuple:
        g_board = copy.deepcopy(game_board)
        board = g_board.get_board()

        if depth == 0 or self.is_terminal(g_board):
            return self.get_board_score(board)

        if isMaximizingPlayer is True:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if g_board.is_space_available(board[row][col]):
                        print("ano!", type(board))
                        pos = board[row][col] 
                        board[row][col] = self.char
                        score = max(best_score, self.calculate(g_board, depth-1, False))
                        board[row][col] = pos

                        if score > best_score:
                            best_score = score

            return best_score
        else: # MinimizingPlayer
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if g_board.is_space_available(board[row][col]):
                        print("ano!", type(board))
                        pos = board[row][col] 
                        board[row][col] = self.x_char
                        score = min(best_score, self.calculate(g_board, depth-1, True))
                        board[row][col] = pos
                        
                        if score > best_score:
                            best_score = score

            return best_score

    def is_terminal(self, game_board):
        return game_board.is_full()

    def get_board_score(self, board):
        return 1
        



