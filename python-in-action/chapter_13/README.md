
# Quiz Game

## Overview

The **Quiz Game** is a Python application that asks the user trivia questions and evaluates their answers. The game loads questions from a text file, presents multiple-choice questions to the user, keeps track of the score, and provides feedback for correct and incorrect answers.

## Features

- **Multiple-Choice Questions**: Questions are loaded from a file, each with four answer choices.
- **Score Tracking**: The game keeps track of the player's score and displays it at the end.
- **File-Based Questions**: Questions are read from a file, making it easy to add new questions.

## How to Run the Program

### Requirements:
- Python 3.x

### Steps:
1. Download the `quiz_game.py` file from this repository.
2. Create a text file for the quiz questions in the following format:
    ```
    What is the capital of France?
    a. Paris
    b. London
    c. Berlin
    d. Madrid
    a

    Who wrote '1984'?
    a. George Orwell
    b. J.K. Rowling
    c. Ernest Hemingway
    d. William Shakespeare
    a
    ```
3. Open a terminal or command prompt and navigate to the directory where `quiz_game.py` is saved.
4. Run the program using the following command:

    ```bash
    python quiz_game.py
    ```

5. Enter the name of the question file when prompted, and the game will begin.

## Example Interaction

```text
Welcome to the Quiz Game!
Enter the name of the question file: questions.txt
What is the capital of France?
1. a. Paris
2. b. London
3. c. Berlin
4. d. Madrid
Your answer (a/b/c/d): a
Correct!

Who wrote '1984'?
1. a. George Orwell
2. b. J.K. Rowling
3. c. Ernest Hemingway
4. d. William Shakespeare
Your answer (a/b/c/d): c
Incorrect! The correct answer was: a

Your final score is 1/2.
```

## License

This project is open-source and available for educational purposes. Feel free to modify and share it!
