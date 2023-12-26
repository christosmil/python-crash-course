from random import randint

class Die():
    """A class to represent a die."""

    def __init__(self, sides=6):
        """Initializes die's sides. Default value is six-sided die."""
        self.sides = sides

    def roll_die(self):
        """Returns the result of a die's roll."""
        return randint(1, self.sides)

# Create a six-sided die (default value).
d6 = Die()
# Roll the six-sided die ten times.
res = []
for number_of_rolls in range(10):
    res.append(d6.roll_die())
# Print the results.
print(f"D6 die rolls:  {res}")

# Create a ten-sided die.
d10 = Die(10)
# Roll the ten-sided die ten times.
res = []
for number_of_rolls in range(10):
    res.append(d10.roll_die())
# Print the results.
print(f"\nD10 die rolls: {res}")

# Create a twenty-sided die.
d20 = Die(20)
# Roll the twenty-sided die ten times.
res = []
for number_of_rolls in range(10):
    res.append(d20.roll_die())
# Print the results.
print(f"\nD20 die rolls: {res}")