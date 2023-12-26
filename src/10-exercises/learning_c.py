file_name = 'learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()

contents = contents.replace('Python', 'C')
print(contents)
print("-- end of the first example\n")

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())
print("-- end of the second example\n")

# Chaining methods.
for line in lines:
    print(line.rstrip().replace('Python', 'C'))
print("-- end of the third example\n")