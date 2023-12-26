# use the range() function to iterate through integers
for value in range(1, 5):
    print(value)
print("-- end of first example\n")

# careful for off-by-one errors when using the range() function
for value in range(1, 6):
    print(value)
print("-- end of second example\n")

# use the range() without starting value (0 by default)
for value in range(6):
    print(value)
print("-- end of third example\n")

# create a list of integers using the range() function
numbers = list(range(1, 6))
print(numbers)
print("-- end of fourth example\n")

# use a step in the range() function
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print("-- end of fifth example\n")