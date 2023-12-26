class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize first name, last name, and annual salary."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, amount=5_000):
        """Give a raise to the employee; by default 5,000$."""
        if amount < 0:
            print("This is not a raise, it's a pay cut!")
        elif amount == 0:
            print("So, practically no raise.")
        else:
            self.annual_salary += amount