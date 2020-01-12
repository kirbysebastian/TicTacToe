
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

    # Argument board for player's feedback of the current game status.
    def get_turn_position(self, board, msg: str):
        while True:
            pos = input(msg)
            if not board.is_space_available(pos):
                print('Position {} not available.'.format(pos))
                continue
            break
        return pos

class AI(Player):
    def __init__(self, p_char):
        super().__init__(p_char)

    # Override get_turn_position function here...
    def foo(self):
        pass
