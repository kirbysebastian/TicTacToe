import pytest

from tic_tac_toe.player import Player

def test_player_character():
    player1 = Player('*')
    assert str(player1) == '*'
    player2 = Player('#')
    assert str(player1) != str(player2)

def test_player_turn():
    player = Player('#')
    player.make_turn(True)
    assert player.is_turn() == True
    player.make_turn(False)
    assert player.is_turn() == False
