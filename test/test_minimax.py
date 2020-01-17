import pytest

from ai.algorithms import Minimax
from tic_tac_toe.board import Board

'''
Board Position Representation
Player-X's turn
 O | O |  
---+---+---
 X | X | O 
---+---+---
 X |   |  
'''
board_position = [
	['O', 'O', '3'],
	['X', 'X', 'O'],
	['X', '8', '9']
]

TIE = 0
P1  = 1
P2  = -1

#def create_board(board_list):
#	board = Board()
#	for rows in board_positon:
#		for ch in rows:
#			board.place(ch, i+1)		
#			board.place(rows[i+1], i+1)		
#			board.place(rows[i+2], i+1)		
	
def create_board(board_list):
	board = Board()
	board.place('O', '1')
	board.place('O', '2')
	board.place('X', '4')
	board.place('X', '5')
	board.place('O', '6')
	board.place('X', '7')
	return board
	

def test_minimax():
	board = create_board([])	
	algo = Minimax('X', 'O')
	assert TIE == algo.get_board_score(board.get_board())
	assert True == board.place('X', '3')
	assert P1 == algo.get_board_score(board.get_board())

