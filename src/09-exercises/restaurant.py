class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name an cuisine attribtues."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the attributes."""
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Here we specialize in {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Simulate the opening of the restaurant."""
        print(f"{self.restaurant_name} is open for business!")

restaurant = Restaurant('la pasteria', 'italian')
print(f"I just created a restaurant named {restaurant.restaurant_name}.")
print(f"{restaurant.restaurant_name} specializes in "
    f"{restaurant.cuisine_type.title()} cuisine.")
restaurant.describe_restaurant()
restaurant.open_restaurant()