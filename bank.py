class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount >= 0):
            self.balance -= amount
        else:
            print("Insufficient funds")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance + self.int_rate)
            return self
    
checkings = BankAccount(.04, 500)
savings = BankAccount(.1, 1000)

checkings.deposit(100).deposit(300).deposit(400).withdraw(500).yield_interest().display_account_info()
savings.deposit(200).deposit(900).withdraw(300).withdraw(200).withdraw(100).withdraw(200).yield_interest().display_account_info()