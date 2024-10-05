
# To-Do List Manager with Error Handling

## Overview

The **To-Do List Manager** is a simple Python program that allows users to manage tasks through a command-line interface. It supports adding, viewing, and removing tasks, while implementing error handling to ensure robustness and a better user experience.

## Features

- **Add Task**: Users can add tasks to their to-do list.
- **View Tasks**: Users can view all tasks currently in their list.
- **Remove Task**: Tasks can be removed by their index.
- **Error Handling**:
    - Handles invalid inputs (e.g., non-numeric input when removing tasks).
    - Prevents task removal from an empty list.

## How to Run the Program

1. Make sure you have Python installed (Python 3.x recommended).
2. Download the `to_do_list_manager.py` file from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `to_do_list_manager.py` file is saved.
5. Run the program using the following command:

    ```bash
    python to_do_list_manager.py
    ```

6. Follow the prompts to add, view, and remove tasks.

## Example Interaction

```text
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Exit
Choose an option (1-4): 1
Enter a new task: Buy groceries
Task 'Buy groceries' added.

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Exit
Choose an option (1-4): 2

Your To-Do List:
1. Buy groceries

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Exit
Choose an option (1-4): 3
Enter the task number to remove: 1
Task 'Buy groceries' removed.

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Exit
Choose an option (1-4): 4
Goodbye!
```

## License

This project is open-source and available for educational purposes. Feel free to modify and share it!
