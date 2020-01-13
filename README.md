# TicTacToe
![](https://raw.githubusercontent.com/kirbysebastian/TicTacToe/master/tictactoe_game.png)

A terminal TicTacToe game made with Python3.

## Rules
1. The game is played on a 3x3 grid with 2 players.
2. Players get to choose their own character as a marker.
3. The first player to get a straight line with their own marker, wins.
4. When all 9 squares are full, with players having no straight line on the grid, ends the game and results in a tie.
---

## Modes
 * (1) - Human to Human Game Mode
 * (2) - Human to AI Game Mode  
 * (3) - AI to AI Game Mode
---

## Game Usage
### Setup
```
chmod +x play.py
```
### Running the game
Plays Human to Human game mode by default
```
// For Linux
./play

// For Windows
python3 play.py
```
or
```
// For Linux
./play --mode <mode number>

// For Windows
python3 play.py --mode <mode numer>
```
---

## Running Tests
Runs with pytest
```
python3 -m pytest
```
---

## Continuous Integration
Runs a travis-ci: [Travis-CI](https://travis-ci.org/kirbysebastian/TicTacToe)

## Artificial Intelligence
[Minimax algorithm](https://en.wikipedia.org/wiki/Minimax) was used.
```
Scores: -1, 0, 1
```

Maximizing player gets the score of 1 while minimizing player gets the score of 2. If in case a tie, score will be 0.
For more information of how this algorithm works: [Game Theory](https://en.wikipedia.org/wiki/Minimax#Combinatorial_game_theory)

### Pseudocode
Based on [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax#Pseudocode)
```
function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value
```
### Notes:
The most optimal value of depth for this game would be 5 before the AI have the most sensible move. Beat it if you can! :D

## TODOs
- ~~Fix bug when players have the same character~~
- ~~Add text/labels for player turn to identify current player's turn~~
- ~~Rename modules with lowercase and fix imports~~
- ~~BUG: Make only 1 character input for players~~
- ~~Make digit input character for players invalid!~~

- Fix Minimax Algo (but is somehow working...)
- Create a test for minimax.py
- Nice to have: Setting of AI difficulty. :)
---

