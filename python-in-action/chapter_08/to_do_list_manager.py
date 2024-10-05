
def show_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{{task}}' added.")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_index = int(input("Enter the task number to remove: ")) - 1

        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{{removed_task}}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def to_do_list_manager():
    tasks = []  
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the to-do list manager
to_do_list_manager()
