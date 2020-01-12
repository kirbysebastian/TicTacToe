import os

def clear():
    import sys
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')

def is_winner(board_list, char):

    diag_check = (char == board_list[0][0] ==
        board_list[1][1] == board_list[2][2]) or (
        char == board_list[0][2] ==
        board_list[1][1] == board_list[2][0])
    
    ver_check = (char == board_list[0][0] ==
        board_list[1][0] == board_list[2][0]) or (
        char == board_list[0][1] ==
        board_list[1][1] == board_list[2][1]) or (
        char == board_list[0][2] ==
        board_list[1][2] == board_list[2][2])

    horz_check = (char == board_list[0][0] ==
        board_list[0][1] == board_list[0][2]) or (
        char == board_list[1][0] ==
        board_list[1][1] == board_list[1][2]) or (
        char == board_list[2][0] ==
        board_list[2][1] == board_list[2][2]) 

    return diag_check or ver_check or horz_check 
