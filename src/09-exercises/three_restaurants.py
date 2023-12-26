class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name an cuisine attribtues."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the attributes."""
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Here we specialize in {self.cuisine_type. title()} cuisine.")

    def open_restaurant(self):
        """Simulate the opening of the restaurant."""
        print(f"{self.restaurant_name} is open for business!")

italian_res = Restaurant('la pasteria', 'italian')
mexican_res = Restaurant('mamacita', 'mexican')
ethnic_res = Restaurant('altamira', 'ethnic')

italian_res.describe_restaurant()
mexican_res.describe_restaurant()
ethnic_res.describe_restaurant()