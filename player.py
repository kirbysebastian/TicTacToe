
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

