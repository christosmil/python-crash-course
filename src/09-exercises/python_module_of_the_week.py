# Get familiar with the random module.

import random


# random_random.py
for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()
print("-- end of the first example\n")


# random_uniform.py
for i in range(5):
    print('%04.3f' % random.uniform(1, 100), end=' ')
print()
print("-- end of the second example\n")

# random_seed.py
random.seed(1) # Usually, seed is platform-specific or current time.

for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()
print("-- end of the third example\n")


# random_state.py
import os
import pickle

if os.path.exists('state.dat'):
    # Restore the previously saved state.
    print('Found state.dat, initializing random module.')
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Use a well-known start state.
    print('No state.dat, seeding.')
    random.seed(1)

# Produce random values.
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

# Save state for next time.
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

# Produce more random values.
print('\nAfter saving state:')
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()
print("-- end of the fourth example\n")


# random_randint.py
print('[1, 100]:', end=' ')

for i in range(3):
    print(random.randint(1, 100), end=' ')

print('\n[-5, 5]:', end=' ')
for i in range(3):
    print(random.randint(-5, 5), end=' ')
print()
print("-- end of the fifth example\n")


# random_randrange.py
for i in range(3):
    print(random.randrange(0, 101, 5), end=' ')
print()
print("-- end of the sixth example\n")

# random_choice.py
import itertools

outcomes = {
    'heads': 0,
    'tails': 0,
}
sides = list(outcomes.keys())

for i in range(10_000):
    outcomes[random.choice(sides)] += 1

print('Heads: ', outcomes['heads'])
print('Tails: ', outcomes['tails'])
print("-- end of the seventh example\n")


# random_shuffle.py
FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

def new_deck():
    # Creates an ordered deck of cards.
    return [
        # Always use 2 places for the value, so the strings
        # are a consistent width.
        '{:>2}{}'.format(*c)
        for c in itertools.product(
                itertools.chain(range(2, 11), FACE_CARDS),
                SUITS,
            )
    ]

def show_deck(deck):
    # Displays each card in a deck of cards.
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()

# Make a new deck, with the cards in order.
deck = new_deck()
print('Initial deck:')
show_deck(deck)

# Shuffle the deck to randomize the order.
random.shuffle(deck)
print('\nShuffled deck:')
show_deck(deck)

# Deal 4 hands of 5 cards each.
hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())

# Show the hands.
print('\nHands')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()

# Show the remaining deck.
print('\nRemaining deck:')
show_deck(deck)
print("-- end of the eighth example\n")


# random_sample.py
# This won't work on Windows, since there is no such path.
# with open('/usr/share/dict/words', 'rt') as f:
#     words = f.readlines()
# words = [w.rstrip() for w in words]

# for w in random.sample(words, 5):
#     print(w)
print("-- end of the ninth example\n")


# random_random_class.py
import time

print('Default initialization:\n')

r1 = random.Random()
r2 = random.Random()

for i in range(3):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))

print('\nSame seed\n')

seed = time.time()
r1 = random.Random(seed)
r2 = random.Random(seed)

for i in range(3):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))
print(f"-- end of the tenth example\n")


# random_system_random.py
print ('Default initialization:\n')

r1 = random.SystemRandom()
r2 = random.SystemRandom()

for i in range(3):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))

print('\nSame seed:\n')

seed = time.time()
r1 = random.SystemRandom(seed)
r2 = random.SystemRandom(seed)

for i in range(3):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))
print(f"-- end of the eleventh example\n")


# random_gauss.py
for i in range(10):
    print(random.gauss(mu=0, sigma=1))
print("-- end of the twelfth example\n")

# random_expovariate.py
for i in range(10):
    print(random.expovariate(1 / 2))
print("-- end of the thirteenth example\n")