"""Starter code for the Connect 4 project."""

import random


ROWS = 6
COLUMNS = 7
EMPTY = "."
PLAYER = "X"
COMPUTER = "O"


def create_board():
    """Create and return an empty board."""
    # TODO: Return a 2D list with 6 rows and 7 columns.
    return []


def print_board(board):
    """Print the board and column numbers."""
    # TODO: Print column numbers.
    # TODO: Print each row.
    pass


def get_player_column(board):
    """Ask the player for a valid column."""
    # TODO: Keep asking until the player chooses a valid non-full column.
    column = input("Choose a column (1-7): ")
    return column


def get_computer_column(board):
    """Choose a valid column for the computer."""
    # TODO: Build a list of valid columns.
    # TODO: Return one random valid column.
    return 0


def drop_checker(board, column, symbol):
    """Drop a checker into the lowest open row."""
    # TODO: Find the lowest empty row in the column and place the symbol there.
    return False


def check_winner(board, symbol):
    """Return True if the symbol has four in a row."""
    # TODO: Check horizontal, vertical, and diagonal directions.
    return False


def board_is_full(board):
    """Return True if the board has no open spaces."""
    # TODO: Check whether the top row is full.
    return False


def main():
    board = create_board()

    # TODO: Add the main game loop.
    print_board(board)
    get_player_column(board)


if __name__ == "__main__":
    main()
