from tic_tac_toe.board import Board
from utils.utilities import clear, is_winner

class TicTacToe:
    def __init__(self, player1, player2):
       self.game_over = False
       self.player_one = player1
       self.player_two = player2
       self.board = Board()

    def start(self):
        self.player_one.make_turn(True)
        board = self.board
        
        while not self.game_over:
            clear()
            print(board)

            self.next_turn()
            self.check_winner()

    def next_turn(self):
        p1 = self.player_one
        p2 = self.player_two

        if p1.is_turn():
            pos = p1.get_turn_position(self.board)
            if pos == None:
                return

            self.board.place(str(p1), pos)
            p1.make_turn(False)
            p2.make_turn(True)
        elif p2.is_turn():
            pos = p2.get_turn_position(self.board)
            if pos == None:
                return

            self.board.place(str(p2), pos)
            p2.make_turn(False)
            p1.make_turn(True)

    def check_winner(self):
        if self.is_player_winner(self.player_one):
             self.announce_winner(self.player_one)
             self.game_over = True
        elif self.is_player_winner(self.player_two):
             self.announce_winner(self.player_two)
             self.game_over = True
        elif self.board.is_full():
             self.announce_tie()
             self.game_over = True

    def is_game_over(self):
        return self.game_over

    def is_player_winner(self, player: str):
        p_char = str(player)
        m_board = self.board.get_board()
        
        return is_winner(m_board, p_char)

    def announce_winner(self, player):
        clear()
        print(self.board)
        print('\nWinner is, player {}!'.format(str(player)))

    def announce_tie(self):
        clear()
        print(self.board)
        print("\nIt's a tie!")

