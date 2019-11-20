# bankaccount.py
class BankAccount:
    """Bank Account protected by a pin number."""
    
    def __init__(self, pin):
        """Initial account balance is 0 and pin is 'pin'."""
        self.balance = 0
        print("Welcome to your bank account!")
        self.pin = pin
        
    def deposit(self, pin, amount):
        """Increment account balance by amount and return new balance."""
        if pin == self.pin:
            self.balance += amount
            return self.balance
        else:
            print("Invalid pin number.")
            
    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        if pin == self.pin:
            self.balance -= amount
            return amount
        else:
            print("Invalid pin number.")
            
    def get_balance(self, pin):
        """Return account balance."""
        if pin == self.pin:
            return self.balance
        else:
            print("Invalid pin number.")
            
    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
        if oldpin == self.pin:
            self.pin = newpin
            print("Changed pin number.")
        else:
            print("You failed to provide your old pin number correctly!") 
