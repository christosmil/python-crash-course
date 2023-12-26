file_name = 'programming.txt'

# Use write mode, i.e., 'w' argument.
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Use append mode, i.e., 'a' argument.
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")