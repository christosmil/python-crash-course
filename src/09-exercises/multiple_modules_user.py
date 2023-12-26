"""A class that is used to represent users."""

class User:
    """An simple attempt to model a user."""

    def __init__(self, first, last, email, username, rights, middle=''):
        """Initialize all attributes."""
        self.first = first.title()
        self.middle = middle.title()
        self.last = last.title()
        self.email = email
        self.username = username
        self.rights = rights
        self.login_attempts = 0

    def describe_user(self):
        """Describes the user by providing all of the attributes."""
        print("User settings:")
        print(f"\tFirst name: {self.first}")
        if self.middle:
            print(f"\tMiddle name: {self.middle}")
        print(f"\tLast name: {self.last}")
        print(f"\tEmail: {self.email}")
        print(f"\tUsername: {self.username}")
        print(f"\tUser rights: {self.rights}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"Hello, {self.username}!")

    def increment_login_attempts(self):
        """Increases the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempts to 0."""
        self.login_attempts = 0

    def print_login_attempts(self):
        """Displays the number of login attempts."""
        print(f"User {self.username} has made {self.login_attempts} attempts.")