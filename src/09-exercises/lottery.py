from random import choice, choices

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
winning_symbols = []
for i in range(4):
    winning_symbols.append(choice(numbers_and_letters))
    numbers_and_letters.remove(winning_symbols[-1])

# Format the ticket neatly
winning_ticket = ''
for winning_symbol in winning_symbols:
    winning_ticket += str(winning_symbol)

# Print the ticket
print(f"The winning ticket is: {winning_ticket}")