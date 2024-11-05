class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.__balance:
                print("Insufficient funds.")
            else:
                self.__balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance
# Usage
account1 = BankAccount()
account1.deposit(1000)
account1.withdraw(200)
account1.withdraw(150)
print(f"Final balance: {account1.get_balance()}")
