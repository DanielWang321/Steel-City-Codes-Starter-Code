# Magic 8 Ball

## Project Description

Create a Magic 8 Ball program. The user asks a yes-or-no question, and the program prints a random answer.

## Student Requirements

- Ask the user to type a question.
- Randomly choose from at least 9 possible responses.
- Include positive, neutral, and negative responses.
- Let the user ask more than one question.
- Let the user quit when they are finished.
- Use terminal input and printed output.

## Concepts Practiced

- `input()`
- `print()`
- loops
- conditionals
- lists
- random choices

## Optional Command-Line Add-Ons

- Count how many questions the user asked.
- Keep asking until the user types `quit`, `q`, or `exit`.
- Print a special message if the user enters a blank question.

## Suggested Starter-Code TODOs

- Add at least 9 responses to the response list.
- Write code that chooses one random response.
- Add a loop so the user can ask multiple questions.
- Check for blank input.
- Check whether the user wants to quit.

## Expected Behavior Example

```text
Welcome to Magic 8 Ball!
Ask a yes/no question, or type quit to stop.
Question: Will I learn Python?
Magic 8 Ball says: Yes, definitely!
Question: quit
Thanks for playing!
```

## Manual Test Cases

1. Input: `Will I pass my quiz?`
   Expected: The program prints one Magic 8 Ball response.

2. Input: `quit`
   Expected: The program ends with a goodbye message.

3. Input: blank line
   Expected: The program asks the user to type a real question.

4. Input: `Is pizza good?`, then `Will it rain?`, then `quit`
   Expected: The program answers both questions before ending.

5. Input: `EXIT`
   Expected: The program treats the command like quitting.

6. Input: a question with extra spaces before or after it
   Expected: The program still accepts the question.
