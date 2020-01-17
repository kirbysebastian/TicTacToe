import pytest

from ai.algorithms import Minimax
from tic_tac_toe.board import Board

# SCORES
TIE = 0
MAX  = 1
MIN  = -1

'''
Board Position Representation
Player-X's turn
 O | O |  
---+---+---
 X | X | O 
---+---+---
 X |   |  
'''
def create_board(board_list):
	board = Board()
	board.place('O', '1')
	board.place('O', '2')
	board.place('X', '4')
	board.place('X', '5')
	board.place('O', '6')
	board.place('X', '7')
	return board
	
def test_maximizing_score_and_isterminal():
	board = create_board([])	
	algo = Minimax('X', 'O')
	assert TIE == algo.get_board_score(board.get_board())
	assert True == board.place('X', '3')
	assert MAX == algo.get_board_score(board.get_board())
	assert True == algo.is_terminal(board)

def test_minimizing_score_and_isterminal():
	board = create_board([])	
	algo = Minimax('X', 'O')
	assert TIE == algo.get_board_score(board.get_board())
	assert True == board.place('O', '3')
	assert MIN == algo.get_board_score(board.get_board())
	assert True == algo.is_terminal(board)
	
