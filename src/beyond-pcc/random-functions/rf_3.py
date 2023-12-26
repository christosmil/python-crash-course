"""Choose an element from a list; do not remove the element."""

from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
random_player = choice(players)
print(random_player)