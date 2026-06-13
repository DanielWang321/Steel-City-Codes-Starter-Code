"""Starter code for the Rock Paper Scissors project."""

import random


choices = ["rock", "paper", "scissors"]


def get_computer_choice():
    """Return the computer's choice."""
    # TODO: Return a random item from choices.
    return "rock"


def get_user_choice():
    """Ask the user for rock, paper, or scissors."""
    # TODO: Keep asking until the user enters a valid choice.
    user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    return user_choice


def decide_winner(user_choice, computer_choice):
    """Return a message that says who won."""
    # TODO: Compare the user choice and computer choice.
    # Think about ties first, then winning combinations.
    return "TODO: decide the winner"


def main():
    print("Rock Paper Scissors")

    # TODO: Add a loop so the game plays at least 3 rounds.
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print("Computer chose", computer_choice + ".")
    print(decide_winner(user_choice, computer_choice))


if __name__ == "__main__":
    main()
