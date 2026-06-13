"""Starter code for the Magic 8 Ball project."""

import random


# TODO: Add at least 9 answers.
# Include positive, neutral, and negative answers.
responses = [
    "TODO: add a Magic 8 Ball response",
]


def get_random_response():
    """Return one random Magic 8 Ball response."""
    # TODO: Choose and return one random response from the list.
    return "TODO: choose a random response"


def main():
    print("Welcome to Magic 8 Ball!")
    print("Ask a yes/no question, or type quit to stop.")

    # TODO: Replace this with a loop so the user can ask many questions.
    question = input("Question: ").strip()

    # TODO: Check whether the user wants to quit.
    # TODO: Check for blank questions.
    print("Magic 8 Ball says:", get_random_response())


if __name__ == "__main__":
    main()
