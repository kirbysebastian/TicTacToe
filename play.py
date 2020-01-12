#!/usr/bin/python3.7

import sys

from tic_tac_toe.player import Player
from tic_tac_toe.tic_tac_toe import TicTacToe
from utils.clear import clear

def generate_players(is_p1_ai=False, is_p2_ai=False):
    p1_char = input('Enter Player 1 Character: ')

    while True:
        p2_char = input('Enter Player 2 Character: ')
        if p2_char == p1_char:
            print('Player 2 charater is same with Player 1. Please change...')
            continue

        break

    player1 = Player(p1_char)
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

