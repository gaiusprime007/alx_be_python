class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    #Withdraw moned
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print(f'Your balance is insufficient to withdraw {amount}')
            return False
        
    def display_balance(self):
        print(f'Your current balance is {self.account_balance}')
        
