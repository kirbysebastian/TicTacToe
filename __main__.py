from player import Player
from tic_tac_toe import TicTacToe

def generate_players():
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

def main():
    p1, p2 = generate_players()
    game = TicTacToe(p1, p2)
    game.start()

if __name__ == '__main__':
    main()
