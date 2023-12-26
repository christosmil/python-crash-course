# A class to test
class Accountant:
    """Manage a bank account."""

    def __init__(self, balance=0):
        """Set the initial balance."""
        self.balance = balance

    def deposit(self, amount):
        """Add to the balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Subtract from the balance."""
        self.balance -= amount