
# Contact Book

## Overview

The **Contact Book** is a simple Python program that allows users to manage contacts by storing names, phone numbers, and email addresses in a text file. The program provides a menu-based interface for:

1. ➕ Adding a new contact.
2. 👀 Viewing all saved contacts.
3. 🔍 Searching for a contact by name.
4. 🚪 Exiting the program.

## Features

- **Add a Contact**: Input a contact's name, phone number, and email address, which will be saved to a text file.
- **View All Contacts**: Display all contacts currently stored in the file.
- **Search for a Contact**: Find a specific contact by their name.
- **Persistent Data**: Contacts are stored in a text file, so they persist between program runs.

## How to Run the Program

1. Make sure you have Python installed (Python 3.x recommended).
2. Download the `contact_book.py` file from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `contact_book.py` file is saved.
5. Run the program with the following command:

    ```bash
    python contact_book.py
    ```

6. Follow the on-screen prompts to add, view, and search contacts.

## Example Interaction

```text
📖 Contact Book
1. ➕ Add a new contact
2. 👀 View all contacts
3. 🔍 Search for a contact by name
4. 🚪 Exit
Choose an option (1-4): 1
Enter the contact's name: Alice
Enter the contact's phone number: 123-456-7890
Enter the contact's email address: alice@example.com
Contact Alice has been added.

📖 Contact Book
1. ➕ Add a new contact
2. 👀 View all contacts
3. 🔍 Search for a contact by name
4. 🚪 Exit
Choose an option (1-4): 2

📋 All Contacts:
Name: Alice, Phone: 123-456-7890, Email: alice@example.com

📖 Contact Book
1. ➕ Add a new contact
2. 👀 View all contacts
3. 🔍 Search for a contact by name
4. 🚪 Exit
Choose an option (1-4): 4
Goodbye! Don't forget to keep in touch with your contacts! 📱
```

## License

This project is open-source and available for educational purposes. Feel free to modify and share it!
