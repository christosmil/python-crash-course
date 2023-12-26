file_name = 'learning_python.txt'

# Print by reading the entire file.
with open(file_name) as file_object:
    contents = file_object.read()
print(contents)
print("-- end of the first example\n")

# Print by looping over the file object.
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
print("-- end of the second example\n")

# Pring by storing the lines and working with them outside the with.
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print("-- end of the third example\n")