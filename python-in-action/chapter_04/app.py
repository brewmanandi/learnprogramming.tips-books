# Welcome to the Witty To-Do List Manager

# Step 1: Define the main menu function
def show_menu():
    print("\nWelcome to the Witty To-Do List Manager!")
    print("What would you like to do today?")
    print("1. 📝 Add a task")
    print("2. 👀 View all tasks")
    print("3. ❌ Remove a task")
    print("4. 🚪 Exit")

# Step 2: Function to add a task to the list
def add_task(tasks):
    task = input("What's the next thing you need to get done? ✏️: ")
    tasks.append(task)
    print(f"Nice! I've added '{task}' to your list. Keep crushing it! 💪")

# Step 3: Function to view all tasks in the list
def view_tasks(tasks):
    if len(tasks) == 0:
        print("You're all caught up! No tasks on your list. 🎉")
    else:
        print("\nHere's what you've got on your plate 🗒️:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("Keep up the good work! 🚀")

# Step 4: Function to remove a task by its number
def remove_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return  # No tasks, nothing to remove
    try:
        task_index = int(input("Which task would you like to remove? (Enter the number) ❌: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' has been removed. One less thing to worry about! 🎯")
        else:
            print("Oops! That number doesn't match any tasks. Try again. 🤔")
    except ValueError:
        print("That's not a number! Are you trying to trick me? 😅")

# Step 5: Main function to manage the to-do list
def to_do_list_manager():
    tasks = []  # Start with an empty list
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! Go crush those tasks like the productivity ninja you are! 🥷")
            break
        else:
            print("Uh-oh! That's not a valid option. Try again! 🤓")

# Run the to-do list manager
to_do_list_manager()
