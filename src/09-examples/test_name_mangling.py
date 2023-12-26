class FootballPlayer:
    """A simple attempt to model a football player."""

    def __init__(self, first, last, salary):
        """Initialize class attributes."""
        self.first = first.title()
        self.last = last.title()
        self.__salary = salary

    def print_player(self):
        """Display the attributes of a player."""
        print(f"{self.first} {self.last} earns {self.__salary}$ per year.")

    def set_salary(self, salary):
        """Set the value of salary attribute."""
        if salary >= 0:
            self.__salary = salary
        else:
            print("A player should not pay to play.")


messi = FootballPlayer('lionel', 'messi', 71_000_000)
messi.print_player()

# This direct access to a class attribute will work.
messi.first = 'leo'.title()
messi.print_player()

# This direct access to a class attribute will not work.
messi.__salary = 41_000_000
messi.print_player()

# This indirect access to a class attribute will work.
messi.set_salary(41_000_000)
messi.print_player()

# This direct access to a class attribute will work (name mangling).
messi._FootballPlayer__salary = 200_000_000
messi.print_player()
