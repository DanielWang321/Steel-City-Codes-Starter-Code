"""Starter code for the Adventure Map project."""


# TODO: Design your map.
# You can use a grid, a list of rooms, or a dictionary of room connections.
rooms = {
    "start": {
        "description": "You are at the start of the adventure.",
        "exits": {},
    }
}


def show_location(current_room):
    """Print information about the player's current room."""
    # TODO: Print the room description.
    # TODO: Print the available exits.
    print("TODO: describe the current room")


def move_player(current_room, command):
    """Return the new room after the player tries to move."""
    # TODO: Check whether the command is a valid exit.
    # TODO: Return the new room if movement is allowed.
    # TODO: Return the same room if movement is blocked.
    return current_room


def main():
    current_room = "start"
    goal_room = "TODO: choose a goal room"

    print("Welcome to Adventure Map!")
    print("Type help for commands.")

    # TODO: Add the main adventure loop.
    show_location(current_room)
    command = input("Command: ").strip().lower()
    current_room = move_player(current_room, command)

    # TODO: Check whether current_room is the goal room.
    if current_room == goal_room:
        print("You reached the goal!")


if __name__ == "__main__":
    main()
