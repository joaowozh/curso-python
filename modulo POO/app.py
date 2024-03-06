
class BankAccount():
    """
    A class representing a bank account of a customer in the project XPTO.

    Attributes:
        name (str): The name of the account holder.
        balance (float): The current balance of the account.

    Methods:
        deposit(amount): Deposits the specified amount into the account.
        withdraw(amount): Withdraws the specified amount from the account.
        checkBalance(): Returns the current balance of the account.
        transfer(amount, recipient): Transfers the specified amount from the account to the recipient's account.
    """
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def checkBalance(self):
        return self.balance

    def transfer(self, amount, recipient):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        recipient.balance += amount
        return self.balance

    