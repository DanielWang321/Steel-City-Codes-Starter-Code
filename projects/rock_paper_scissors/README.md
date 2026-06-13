# Rock Paper Scissors

## Project Description

Create a Rock Paper Scissors game where the user plays against the computer in the terminal.

## Student Requirements

- Let the user choose `rock`, `paper`, or `scissors`.
- Let the computer randomly choose `rock`, `paper`, or `scissors`.
- Play at least 3 rounds, or allow the user to keep playing.
- Print whether the user wins, loses, or ties each round.
- Validate input so invalid choices do not crash the program.
- Use terminal input and printed output.

## Concepts Practiced

- `input()`
- `print()`
- strings
- conditionals
- loops
- random choices

## Optional Command-Line Add-Ons

- Track wins, losses, and ties.
- Let the user type `r`, `p`, or `s` as shortcuts.
- Ask the user whether they want to play again.

## Suggested Starter-Code TODOs

- Write a function that gets a valid user choice.
- Write a function that randomly chooses for the computer.
- Write conditionals that decide the winner.
- Add a loop for multiple rounds.
- Add score tracking if you want an extra challenge.

## Expected Behavior Example

```text
Rock Paper Scissors
Choose rock, paper, or scissors: rock
Computer chose scissors.
You win!
```

## Manual Test Cases

1. Input: `rock` while computer choice is `scissors`
   Expected: The program says the user wins.

2. Input: `paper` while computer choice is `scissors`
   Expected: The program says the user loses.

3. Input: `scissors` while computer choice is `scissors`
   Expected: The program says it is a tie.

4. Input: `banana`
   Expected: The program says the choice is invalid and asks again.

5. Input: `ROCK`
   Expected: The program accepts the choice as `rock`.

6. Input: three valid choices in a row
   Expected: The program plays at least three rounds.
