#!/usr/bin/python3.7

import sys

from tic_tac_toe.player import Player, AI
from tic_tac_toe.tic_tac_toe import TicTacToe
from utils.utilities import clear

def get_validated_inputs():
    areValidInputs = False
    is_p1_valid = False
    is_p2_valid = False
    while not areValidInputs:
        if not is_p1_valid:
            p1_char = input('Enter Player 1 Character: ')

        if (not is_p1_valid) and ( (len(p1_char) > 1) or (p1_char.isnumeric()) ):
            print('Please enter valid character.')
            continue

        is_p1_valid = True

        p2_char = input('Enter Player 2 Character: ')
        if len(p2_char) > 1 or (p2_char.isnumeric()):
            print('Please enter valid character.')
            continue
        elif p2_char == p1_char:
            print('Chosen character is same with Player 1. Try again.')
            continue

        break

    return p1_char, p2_char

def generate_players(is_p1_ai=False, is_p2_ai=False):

    p1_char, p2_char = get_validated_inputs()

    if is_p1_ai == True:
        player1 = AI(p1_char, p2_char)
    else:
        player1 = Player(p1_char)

    if is_p2_ai == True:
        player2 = AI(p2_char, p1_char)
    else:
        player2 = Player(p2_char)

    return player1, player2

def greetings():
    print('WELCOME TO MY VERY OWN PYTHON-TICTACTOE GAME!\n')

modes = {
    0: 'NULL',
    1: '2-Player',
    2: 'AI',
    3: 'AIvsAI'
    }
def get_mode(args):
    mode = parse_args(args)
    if mode not in modes.keys() or mode == 0:
        print('Invalid mode!')
        return modes[0]

    return modes[mode]

def parse_args(args) -> int:
    if '--mode' not in args:
        return 1

    return int(args[args.index('--mode') + 1])

def main(args):
    clear()
    mode = get_mode(args)
    greetings()

    if mode == '2-Player':
        p1, p2 = generate_players()
    elif mode == 'AI':
        p1, p2 = generate_players(is_p1_ai=False, is_p2_ai=True)
    elif mode == 'AIvsAI':
        p1, p2 = generate_players(is_p1_ai=True, is_p2_ai=True)
    else:
        print('Cannot start the game.')
        return

    game = TicTacToe(p1, p2)
    game.start()

if __name__ == '__main__':
    main(sys.argv)

