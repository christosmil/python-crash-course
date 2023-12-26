"""Shuffle a list; the list permanently loses its original order."""

from random import shuffle

players = ['charles', 'martina', 'michael', 'florence', 'eli']

shuffled_players = players[:]
shuffle(shuffled_players)

print(players)
print(shuffled_players)