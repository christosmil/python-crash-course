dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# The following command will result to a TypeError, since tuples are
# immmutable:
# dimensions[0] = 250
print("-- end of the first example\n")

# testing tuples
my_t = (3,)
print(type(my_t))
my_t = (3)
print(type(my_t))
my_t = 3,
print(type(my_t))
my_t = 3, 4
print(type(my_t))
my_t = [3,]
print(type(my_t))
print("-- end of testing some stuff\n")
# The following command will result to a ValueError
# foo, bar = 100, 200, 300

# loop through a tuple
for dimension in dimensions:
    print(dimension)
print("-- end of the second example\n")

# assign new value to a tuple variable
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
print("-- end of the third example\n")