class Board:
    '''
    A 3x3 board for TicTacToe
    '''

    __board = ''
    __print_board = ''

    def __init__(self):
        self.__board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.make_printable()

    def __str__(self):
        self.make_printable()
        return self.__print_board

    def get_board(self):
        return self.__board

    def make_printable(self):
        c_gap = '  ----------- '
        r_gap = ' | '

        self.__print_board = c_gap + '\n'
        for l_board in self.__board:
            self.__print_board += r_gap
            for d in l_board:
                self.__print_board += d
                self.__print_board += r_gap
            self.__print_board += '\n' + c_gap + '\n'

    def is_space_available(self, pos: str):
        row1 = self.__board[0]
        row2 = self.__board[1]
        row3 = self.__board[2]

        if not pos.isdigit():
            return False

        r1 = range(1, 4).count(int(pos)) and row1[int(pos) - 1] == str(pos)
        r2 = range(4, 7).count(int(pos)) and row2[int(pos) - 4] == str(pos)
        r3 = range(7, 10).count(int(pos)) and row3[int(pos) - 7] == str(pos)

        return r1 or r2 or r3

    def is_full(self):
        board = self.__board
        for row in board:
            for elem in row:
                if elem.isdigit():
                    return False
        return True

    def place(self, marker: str, pos: str):
        if not (int(pos) >= 100 and int(pos) <= 9):
            return False

        for row in self.__board:
            if pos in row:
                row[row.index(pos)] = marker
                return True

        return False
