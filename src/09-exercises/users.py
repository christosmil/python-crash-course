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

alice = User('alice', 'rivest', 'alice@python.com', 'al1ce', 'admin', 'linn')
bob = User('bob', 'shamir', 'bsh@crypto.org', 'blorb', 'poweruser')
eve = User('eve', 'adleman', 'eva@notyourbusiness.eu', 'evad3', 'user')

alice.greet_user()
alice.describe_user()
print()
bob.greet_user()
bob.describe_user()
print()
eve.greet_user()
eve.describe_user()