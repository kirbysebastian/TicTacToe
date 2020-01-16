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

#def create_board(board_list):
#	board = Board()
#	for rows in board_positon:
#		for ch in rows:
#			board.place(ch, i+1)		
#			board.place(rows[i+1], i+1)		
#			board.place(rows[i+2], i+1)		
	
	
def test_minimax():
	pass
	
