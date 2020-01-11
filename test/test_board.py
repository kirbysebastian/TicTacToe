import pytest

from tic_tac_toe.board import Board

def test_board_place_with_integer_pos():
    board = Board()
    out = board.place('*', 4)
    assert out == False 

def test_board_place_with_invalid_pos():
    board = Board()
    out = board.place('*', '0')
    assert out == False

def test_board_place():
    board = Board()
    out = board.place('*', '5')
    assert out == True

def test_board_is_full():
    board = Board()
    board.place('*', '1')
    board.place('*', '2')
    board.place('*', '3')
    board.place('*', '4')
    board.place('*', '5')
    board.place('*', '6')
    board.place('*', '7')
    board.place('*', '8')
    board.place('*', '9')
    assert board.is_full() == True

def test_board_is_not_full():
    board = Board()
    board.place('*', '1')
    board.place('*', '2')
    board.place('*', '3')
    board.place('*', '4')
    board.place('*', '5')
    board.place('*', '6')
    board.place('*', '7')
    board.place('*', '8')
    assert board.is_full() == False
    
def test_board_place_correct_position():
    first_board = Board()
    second_board = Board()
    first_board.place('*', '5')
    second_board.place('*', '5')
    assert str(first_board) == str(second_board)

def test_board_place_incorrect_position():
    first_board = Board()
    second_board = Board()
    first_board.place('*', '3')
    second_board.place('*', '2')
    assert str(first_board) != str(second_board)

def test_board_is_space_available():
    board = Board()
    assert board.is_full() == False
    for num in range(1, 10):
        assert board.is_space_available(str(num)) == True
        board.place('*', str(num))
        assert board.is_space_available(str(num)) == False
    assert board.is_full() == True
