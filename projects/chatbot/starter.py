"""Starter code for the Chatbot project."""

import random


known_topics = ["hello", "python", "bear", "music"]


def get_response(message):
    """Return the chatbot's response to one message."""
    message = message.lower()

    # TODO: Check for greetings such as hello or hi.
    # TODO: Check for keywords such as python, bear/bears, or music.
    # TODO: Return helpful hints if no keyword is found.
    return "TODO: write a chatbot response"


def main():
    print("Hello! I am a Python chatbot.")
    print("Type bye to exit.")

    # TODO: Replace this with a loop so the user can keep chatting.
    message = input("You: ").strip()

    # TODO: Check whether the user wants to exit.
    # TODO: Check for blank input.
    print("Bot:", get_response(message))


if __name__ == "__main__":
    main()
