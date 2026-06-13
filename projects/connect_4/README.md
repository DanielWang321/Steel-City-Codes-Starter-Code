# Connect 4

## Project Description

Create a command-line Connect 4 game where the player plays against the computer.

## Student Requirements

- Use a 6-row by 7-column board.
- Let the player choose a column.
- Let the computer randomly choose a valid column.
- Make each checker drop to the lowest open row in the chosen column.
- Validate column input.
- Detect wins horizontally, vertically, and diagonally.
- Detect ties.
- Use terminal input and printed output.

## Concepts Practiced

- input/output
- loops
- conditionals
- strings
- lists
- 2D lists
- random choices

## Optional Command-Line Add-Ons

- Let the player choose their symbol.
- Let the player choose whether to go first.
- Add a smarter computer move.

## Suggested Starter-Code TODOs

- Create a 6 by 7 board.
- Print the board with column numbers.
- Check whether a column is valid.
- Drop a checker into the lowest open row.
- Check for four in a row in all directions.
- Add a loop that alternates player and computer turns.

## Expected Behavior Example

```text
1 2 3 4 5 6 7
. . . . . . .
. . . . . . .
. . . X . . .
Choose a column (1-7): 4
```

## Manual Test Cases

1. Input: column `4`
   Expected: The player's checker lands in the bottom row of column 4.

2. Input: column `0`
   Expected: The program says the column is invalid and asks again.

3. Input: a full column
   Expected: The program says the column is full and asks again.

4. Input: moves that create four horizontally
   Expected: The program announces a win.

5. Input: moves that create four diagonally
   Expected: The program announces a win.

6. Input: moves that fill the board without a winner
   Expected: The program announces a tie.
