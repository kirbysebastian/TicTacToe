import os
from Board import Board

def clear():
    import sys
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')

class TicTacToe:
    def __init__(self, player1, player2):
       self.game_over = False
       self.player_one = player1
       self.player_two = player2
       self.board = Board()

    def start(self):
        p1 = self.player_one
        p1.make_turn(True)
        p2 = self.player_two
        board = self.board
        
        clear()
        print(board)
        while not self.game_over:
            #Player Turn
            turn_pos = input()
            if not board.is_space_available(turn_pos):
                print('Position {} not available.'.format(turn_pos))
                input('Press any ckey to continue...')
                continue

            if p1.is_turn():
                board.place(str(p1), turn_pos)
                p1.make_turn(False)
                p2.make_turn(True)
            elif p2.is_turn():
                board.place(str(p2), turn_pos)
                p2.make_turn(False)
                p1.make_turn(True)

            clear()
            print(board)

            #Check Winner
            if self.is_player_winner(p1):
                self.announce_winner(p1)
                self.game_over = True
            elif self.is_player_winner(p2):
                self.announce_winner(p2)
                self.game_over = True
            elif board.is_full():
                self.announce_tie()
                self.game_over = True
            #Print Board

    def is_game_over(self):
        return self.game_over

    def is_player_winner(self, player: str):
        p_char = str(player)
        m_board = self.board.get_board()
        diag_check = (p_char == m_board[0][0] ==
            m_board[1][1] == m_board[2][2]) or (
            p_char == m_board[0][2] ==
            m_board[1][1] == m_board[2][0])
        
        ver_check = (p_char == m_board[0][0] ==
            m_board[1][0] == m_board[2][0]) or (
            p_char == m_board[0][1] ==
            m_board[1][1] == m_board[2][1]) or (
            p_char == m_board[0][2] ==
            m_board[1][2] == m_board[2][2])

        horz_check = (p_char == m_board[0][0] ==
            m_board[0][1] == m_board[0][2]) or (
            p_char == m_board[1][0] ==
            m_board[1][1] == m_board[1][2]) or (
            p_char == m_board[2][0] ==
            m_board[2][1] == m_board[2][2]) 

        return diag_check or ver_check or horz_check 

    def announce_winner(self, player):
        print('\nWinner is, player {}!'.format(str(player)))

    def announce_tie(self):
        print("\nIt's a tie!")

