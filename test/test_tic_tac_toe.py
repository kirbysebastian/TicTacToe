import pytest
from TicTacToe import TicTacToe
from Player import Player

def test_ttt_is_game_over():
    p1 = Player('O')
    p2 = Player('X')
    game = TicTacToe(p1, p2)
    assert game.is_game_over() == False

def test_ttt_is_player_winner():
    p1 = Player('X')
    p2 = Player('O')
    game = TicTacToe(p1, p2)
    assert game.is_player_winner(p1) == False
    assert game.is_player_winner(p2) == True
