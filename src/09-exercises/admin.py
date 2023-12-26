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


class Admin(User):
    """A simple attempt to model an admin user."""

    def __init__(self, first, last, email, username, rights, middle=''):
        """Initialize parent and child class attributes."""
        super().__init__(first, last, email, username, rights, middle)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Displays the list of priviledges for an admin."""
        print(f"{self.username} ({self.rights}) has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin('peter', 'parker', 'pp@bugle.com', 'spidey', 'admin')
admin.show_privileges()