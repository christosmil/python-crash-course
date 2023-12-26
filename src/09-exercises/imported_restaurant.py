"""A class to represent a restaurant."""

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name an cuisine attribtues."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the attributes."""
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Here we specialize in {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Simulate the opening of the restaurant."""
        print(f"{self.restaurant_name} is open for business!")

    def get_number_served(self):
        """Displays the number of customers that have been served."""
        msg = f"{self.restaurant_name} has served {self.number_served} people."
        print(msg)

    def set_number_served(self, customers):
        """Sets the number of customers that have been served."""
        if customers >= 0:
            self.number_served = customers
        else:
            print("You can't have a negative number of customers!")

    def increment_number_served(self, customers):
        """Update the number of customers that have been served."""
        if customers >= 0:
            self.number_served += customers
        else:
            print("You can't remove customers that have already been served!")