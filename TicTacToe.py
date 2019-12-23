from Board import Board

class TicTacToe:
    def __init__(self, p1_char, p2_char):
       self.game_over = False
       self.player_one = p1_char
       self.player_two = p2_char
       self.board = Board()

    def start(self):
        while not self.game_over:
            #Player Turn
            #Check Winner
            #Print Board
            pass

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

    def announce_winner(self):
        pass

