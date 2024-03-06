class BankAccount:
    def __init__(self, customer_name, account_number, balance):
        self.customer_name = customer_name
        self.account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = value

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance
    
    # nome do método: check_balance - por convenção - snake_case
    def check_balance(self):
        return self.balance

