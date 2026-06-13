# Hangman

## Project Description

Create a command-line Hangman game where the player guesses a hidden word one letter at a time.

## Student Requirements

- Choose a random word from a list.
- Display blanks for letters that have not been guessed.
- Ask the user to guess one letter at a time.
- Track incorrect guesses and remaining attempts.
- Show guessed letters.
- Detect when the user wins or loses.
- Ask if the user wants to play again.
- Use terminal input and printed output.

## Concepts Practiced

- strings
- loops
- conditionals
- lists
- random choices
- input validation

## Optional Command-Line Add-Ons

- Add hints for each word.
- Prevent repeated guesses from using an attempt.
- Let the user choose a difficulty level.

## Suggested Starter-Code TODOs

- Add a list of possible words.
- Choose one random word.
- Build the display with blanks and guessed letters.
- Validate that each guess is one letter.
- Track correct and incorrect guesses.
- Add a replay loop.

## Expected Behavior Example

```text
Word: _ _ _ _ _ _
Guessed letters:
Attempts left: 6
Guess one letter: p
Good guess!
```

## Manual Test Cases

1. Input: a correct letter in the word
   Expected: The blank display reveals that letter.

2. Input: an incorrect letter
   Expected: Attempts left decreases by 1.

3. Input: `ab`
   Expected: The program asks for one letter only.

4. Input: the same guessed letter twice
   Expected: The program says the letter was already guessed.

5. Input: enough correct letters to complete the word
   Expected: The program announces a win.

6. Input: enough wrong letters to run out of attempts
   Expected: The program announces a loss and shows the word.
