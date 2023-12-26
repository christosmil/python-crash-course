# append values in a list through a loop
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
print("-- end of first example\n")

# do calculations inside the append() method
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print("-- end of second example\n")

# use list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)
print("-- end of third example\n")