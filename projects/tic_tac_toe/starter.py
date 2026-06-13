"""Starter code for the Tic-Tac-Toe project."""


def create_board():
    """Create and return an empty 3 by 3 board."""
    # TODO: Return a 2D list with 3 rows and 3 columns.
    return []


def print_board(board):
    """Print the board in a readable way."""
    # TODO: Print each row of the board.
    # Add row and column labels if that helps.
    pass


def get_move(player, board):
    """Ask a player for a valid row and column."""
    # TODO: Keep asking until the row and column are valid.
    # TODO: Make sure the chosen square is not already taken.
    row = input("Row (1-3): ")
    column = input("Column (1-3): ")
    return row, column


def check_winner(board, player):
    """Return True if the player has won."""
    # TODO: Check rows.
    # TODO: Check columns.
    # TODO: Check both diagonals.
    return False


def board_is_full(board):
    """Return True if there are no empty squares."""
    # TODO: Check every square on the board.
    return False


def play_game():
    """Play one game of Tic-Tac-Toe."""
    board = create_board()
    current_player = "X"

    # TODO: Add the main game loop.
    print_board(board)
    get_move(current_player, board)


def main():
    # TODO: Add a replay loop.
    play_game()


if __name__ == "__main__":
    main()
