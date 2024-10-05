
# Student Grade Tracker

def show_menu():
    print("\n🎓 Student Grade Tracker")
    print("1. 📝 Add a student and their grade")
    print("2. 👀 View all students and grades")
    print("3. ❌ Remove a student")
    print("4. 🚪 Exit")

def add_student(grades):
    name = input("Enter the student's name: ")
    grade = input(f"Enter {name}'s grade: ")
    grades[name] = grade
    print(f"Added {name} with grade '{{grade}}'. Well done!")

def view_grades(grades):
    if len(grades) == 0:
        print("No students in the grade tracker. Add some students first!")
    else:
        print("\n📋 Student Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")

def remove_student(grades):
    name = input("Enter the student's name to remove: ")
    if name in grades:
        del grades[name]
        print(f"Removed {name} from the tracker.")
    else:
        print(f"Student '{{name}}' not found.")

def grade_tracker():
    grades = {}  # Initialize an empty dictionary
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_student(grades)
        elif choice == "2":
            view_grades(grades)
        elif choice == "3":
            remove_student(grades)
        elif choice == "4":
            print("Goodbye! Hope your students ace their exams! 🎓")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the student grade tracker
grade_tracker()
