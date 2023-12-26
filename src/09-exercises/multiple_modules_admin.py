"""A set of classes to represent admin users."""
from multiple_modules_user import User

class Privileges:
    """A simple attempt to model user privileges."""

    def __init__(self, privileges):
        """Initialize class attributes."""
        self.privileges = privileges

    def show_privileges(self):
        """Displays the list of priviledges for a user."""
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A simple attempt to model an admin user."""

    def __init__(self, first, last, email, username, rights, middle=''):
        """Initialize parent and child class attributes."""
        super().__init__(first, last, email, username, rights, middle)
        self.user_privileges = Privileges([
            'can add post', 'can delete post', 'can ban user'
            ])