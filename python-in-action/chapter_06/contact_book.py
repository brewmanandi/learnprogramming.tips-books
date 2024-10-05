
# Contact Book

def show_menu():
    print("\n📖 Contact Book")
    print("1. ➕ Add a new contact")
    print("2. 👀 View all contacts")
    print("3. 🔍 Search for a contact by name")
    print("4. 🚪 Exit")

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print(f"Contact {name} has been added.")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

            if len(contacts) == 0:
                print("No contacts found. Start adding some!")
            else:
                print("\n📋 All Contacts:")
                for contact in contacts:
                    name, phone, email = contact.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")
    except FileNotFoundError:
        print("No contacts file found. Start by adding a contact!")

def search_contact():
    search_name = input("Enter the name of the contact to search for: ").lower()

    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

            found = False
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                if search_name == name.lower():
                    print(f"📞 Found: {name}, Phone: {phone}, Email: {email}")
                    found = True
                    break

            if not found:
                print(f"No contact found with the name {search_name}.")
    except FileNotFoundError:
        print("No contacts file found. Start by adding a contact!")

def contact_book():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodbye! Don't forget to keep in touch with your contacts! 📱")
            break
        else:
            print("Invalid option. Please try again.")

# Run the Contact Book program
contact_book()
