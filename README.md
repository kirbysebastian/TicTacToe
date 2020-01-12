# TicTacToe
TicTacToe Game made with Python3.

## Rules
1. The game is played on a 3x3 grid with 2 players.
2. Players get to choose their own character as a marker.
3. The first player to get a straight line with their own marker, wins.
4. When all 9 squares are full, with players having no straight line on the grid, ends the game and results in a tie.

## Modes
 * (1) - Human to Human Game Mode
 * (2) - Human to AI Game Mode  ***// Not yet supported***
 * (3) - AI to AI Game Mode  ***// Not yet supported***

## Game Usage
### Setup
```
chmod +x play.py
```
### Running the game
Plays Human to Human game mode by default
```
./play
```
or
```
./play --mode <mode number>
```

## Running Tests
Runs with pytest
```
python3 -m pytest
```

## Continuous Integration
Runs a travis-ci: [Travis-CI](https://travis-ci.org/kirbysebastian/TicTacToe)

## AI
Still todo. Maybe use minimax algorithm (alpha beta pruning)

## TODO
~~- Fix bug when players have the same character~~
~~- Add text/labels for player turn to identify current player's turn~~
~~- Rename modules with lowercase and fix imports~~

- BUG: Make only 1 character input for players

