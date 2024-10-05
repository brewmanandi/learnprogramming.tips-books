
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = 500

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Exceeded overdraft limit!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
        self.interest_rate = 0.02

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest: {interest}. New balance: {self.balance}")


def main():
    # Create a checking account
    checking_account = CheckingAccount("Alice", 1000)
    checking_account.display_info()
    checking_account.withdraw(1200)
    checking_account.deposit(500)

    print("\n")

    # Create a savings account
    savings_account = SavingsAccount("Bob", 2000)
    savings_account.display_info()
    savings_account.add_interest()


if __name__ == "__main__":
    main()
