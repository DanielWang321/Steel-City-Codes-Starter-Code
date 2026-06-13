# Adventure Map

## Project Description

Create a command-line text adventure where the player moves through a map or set of rooms to reach a goal.

## Student Requirements

- Use a grid map or room system.
- Let the user move with commands such as `north`, `south`, `east`, and `west`.
- Include walls or blocked paths.
- Include a goal location.
- Print the map or current room information.
- Keep running until the user reaches the goal or quits.
- Use terminal input and printed output.

## Concepts Practiced

- input/output
- conditionals
- loops
- functions
- lists
- optional object-oriented programming

## Optional Command-Line Add-Ons

- Add items the player must collect.
- Add locked doors.
- Track the number of moves.
- Use classes for the player, rooms, or game.

## Suggested Starter-Code TODOs

- Design the map or room connections.
- Track the player's current location.
- Write a function that prints the current location.
- Write a function that moves the player if the path is not blocked.
- Detect when the player reaches the goal.
- Add commands such as `help` and `quit`.

## Expected Behavior Example

```text
You are in the forest path.
Exits: north, east
Command: north
You walk north.
```

## Manual Test Cases

1. Input: a valid movement command
   Expected: The player's location changes.

2. Input: a blocked direction
   Expected: The program says the path is blocked.

3. Input: `help`
   Expected: The program lists useful commands.

4. Input: `quit`
   Expected: The program ends with a goodbye message.

5. Input: commands that reach the goal
   Expected: The program announces that the player won.

6. Input: uppercase movement command such as `NORTH`
   Expected: The program accepts the command.
