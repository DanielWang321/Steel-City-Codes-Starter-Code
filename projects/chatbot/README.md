# Chatbot

## Project Description

Create a friendly command-line chatbot that responds to messages from the user.

## Student Requirements

- Greet the user.
- Let the user type messages in a loop.
- Recognize several keywords.
- Make keyword checks not case-sensitive.
- Handle simple plural words when reasonable, such as `bear` and `bears`.
- If no keyword is recognized, print hints about known topics.
- Let the user exit.
- Use terminal input and printed output.

## Concepts Practiced

- strings
- `.lower()`
- substring checks
- conditionals
- loops
- random choices

## Optional Command-Line Add-Ons

- Randomly choose from several possible responses.
- Store keywords and responses in a dictionary.
- Add a help command that lists known topics.

## Suggested Starter-Code TODOs

- Choose the topics your chatbot knows about.
- Convert user messages to lowercase before checking keywords.
- Check for both singular and plural keyword forms.
- Add a fallback response with hints.
- Add an exit command.

## Expected Behavior Example

```text
Hello! I am a Python chatbot.
You: Tell me about bears.
Bot: Bears are strong mammals. Some live in forests and mountains.
You: bye
Bot: Goodbye!
```

## Manual Test Cases

1. Input: `hello`
   Expected: The bot responds with a greeting.

2. Input: `Tell me about bears`
   Expected: The bot recognizes the bear topic.

3. Input: `Do you like PYTHON?`
   Expected: The bot recognizes the Python topic even with uppercase letters.

4. Input: `unknown topic`
   Expected: The bot prints hints about known topics.

5. Input: `bye`
   Expected: The bot exits with a goodbye message.

6. Input: blank line
   Expected: The bot asks the user to type a message.
