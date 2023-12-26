from random import choice, choices, sample

numbers_and_letters = list(range(10))
numbers_and_letters.append('a')
numbers_and_letters.append('b')
numbers_and_letters.append('c')
numbers_and_letters.append('d')
numbers_and_letters.append('e')

# Select from a set k times with replacement.
winning_symbols = choices(numbers_and_letters, k=4)

# Format the ticket neatly.
winning_ticket = ''
for winning_symbol in winning_symbols:
    winning_ticket += str(winning_symbol)

# Print the ticket.
print(f"The winning ticket is: {winning_ticket}")

# Select from a set k times without replacement.
alphabet = numbers_and_letters[:]
winning_symbols = []
for i in range(4):
    winning_symbols.append(choice(alphabet))
    alphabet.remove(winning_symbols[-1])

# Format the ticket neatly.
winning_ticket = ''
for winning_symbol in winning_symbols:
    winning_ticket += str(winning_symbol)

# Print the ticket.
print(f"The winning ticket is: {winning_ticket}")

# Select from a set k times without replacement, using sample().
winning_ticket = ''
for winning_symbol in sample(numbers_and_letters, 4):
    winning_ticket += str(winning_symbol)

# Print the ticket.
print(f"The winning ticket is: {winning_ticket}")

# Check if I won the lottery.
my_ticket = [6, 'a', 4, 1]

# Conduct lottery draws, until I win.
counter = 0
while True:
    counter += 1
    winning_symbols = []
    alphabet = numbers_and_letters[:]
    for i in range(4):
        winning_symbols.append(choice(alphabet))
        alphabet.remove(winning_symbols[-1])
    
    matching_symbols = 0
    for winning_symbol in winning_symbols:
        if winning_symbol in my_ticket:
            matching_symbols += 1

    if matching_symbols == len(winning_symbols):
        break

# Format the ticket neatly.
winning_ticket = ''
for winning_symbol in winning_symbols:
    winning_ticket += str(winning_symbol)

# Print the ticket
print(f"The winning ticket is: {winning_ticket}")

# Inform me about how long it took me to win.
print(f"The loop run {counter} times, before I win...")