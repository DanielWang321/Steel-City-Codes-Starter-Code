"""Starter code for the Hangman project."""

import random


words = ["python", "coding", "student"]


def choose_word():
    """Choose and return one word."""
    # TODO: Choose a random word from the list.
    return words[0]


def make_display(word, guessed_letters):
    """Return the word with blanks for unguessed letters."""
    # TODO: Build a display using underscores for missing letters.
    return "_ " * len(word)


def get_guess(guessed_letters):
    """Ask the user for one new letter."""
    # TODO: Keep asking until the guess is one unused letter.
    guess = input("Guess one letter: ").strip().lower()
    return guess


def play_game():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6

    # TODO: Add the main game loop.
    print("Word:", make_display(word, guessed_letters))
    print("Attempts left:", attempts_left)
    get_guess(guessed_letters)


def main():
    # TODO: Add a replay loop.
    play_game()


if __name__ == "__main__":
    main()
