# Tic-Tac-Toe

## Project Description

Create a two-player command-line Tic-Tac-Toe game.

## Student Requirements

- Use a 3 by 3 board.
- Print the board each turn.
- Ask the current player for a row and column.
- Validate row and column input.
- Do not allow a player to use a taken square.
- Detect wins across rows, columns, and diagonals.
- Detect ties.
- Ask if the players want to play again.
- Use terminal input and printed output.

## Concepts Practiced

- functions
- loops
- conditionals
- lists
- 2D lists
- input validation

## Optional Command-Line Add-Ons

- Show row and column numbers around the board.
- Track how many games each player has won.
- Let players enter names.

## Suggested Starter-Code TODOs

- Create the board as a 2D list.
- Write a function to print the board.
- Write a function to validate a move.
- Write a function to check for a winner.
- Write a function to check for a tie.
- Add a replay loop.

## Expected Behavior Example

```text
Player X turn
Row (1-3): 1
Column (1-3): 2
  | X |
--+---+--
  |   |
--+---+--
  |   |
```

## Manual Test Cases

1. Input: row `1`, column `1`
   Expected: The current player's symbol appears in the top-left square.

2. Input: row `4`
   Expected: The program says the row is invalid and asks again.

3. Input: row `1`, column `1` after that square is taken
   Expected: The program says the square is already taken.

4. Input: X fills a full row
   Expected: The program announces that X wins.

5. Input: all squares fill with no winner
   Expected: The program announces a tie.

6. Input: `yes` after a finished game
   Expected: The board resets and a new game starts.
