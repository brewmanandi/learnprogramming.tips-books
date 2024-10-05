
# Bank Account Management System

## Overview

This **Bank Account Management System** demonstrates the use of Object-Oriented Programming (OOP) principles in Python. It includes base and derived classes to represent different types of bank accounts: checking and savings accounts. The system allows for the creation of accounts, deposits, withdrawals, and interest calculations for savings accounts.

## Features

- **Base Class: `BankAccount`**:
    - Stores common account information (account holder, balance).
    - Provides methods for depositing and withdrawing money.
  
- **Derived Class: `CheckingAccount`**:
    - Inherits from `BankAccount`.
    - Includes an overdraft limit, allowing withdrawals beyond the account balance.
  
- **Derived Class: `SavingsAccount`**:
    - Inherits from `BankAccount`.
    - Includes an interest rate and provides a method for adding interest to the balance.

## How to Run the Program

1. Make sure you have Python installed (Python 3.x recommended).
2. Download the `bank_account_system.py` file from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `bank_account_system.py` file is saved.
5. Run the program using the following command:

    ```bash
    python bank_account_system.py
    ```

6. The program will create and manage checking and savings accounts, showing deposits, withdrawals, and interest calculations.

## Example Interaction

```text
Account Holder: Alice
Balance: 1000
Withdrew 1200. New balance: -200
Deposited 500. New balance: 300

Account Holder: Bob
Balance: 2000
Added interest: 40.0. New balance: 2040.0
```

## License

This project is open-source and available for educational purposes. Feel free to modify and share it!
