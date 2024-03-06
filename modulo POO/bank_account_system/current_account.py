from bank_account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, customer_name, account_number, balance, overdraft_limit):
        super().__init__(customer_name, account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.overdraft_usage = 0

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return 'Insufficient funds'
        if self.balance < amount:
            if self.overdraft_limit - self.overdraft_usage < amount - self.balance:
                return 'Overdraft limit exceeded'
            self.overdraft_usage += amount - self.balance
            self.balance = 0
            return self.balance
        self.balance -= amount
        return self.balance

    def check_balance(self):
        if self.balance < 0 and self.overdraft_limit > 0:
            return f'Current balance: {self.balance}, Overdraft limit: {self.overdraft_limit}'
        return self.balance