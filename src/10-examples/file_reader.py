# Open a file.
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
print("-- end of the first example\n")

# Open a relative file path.
with open('../examples-chapter-10/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print("-- end of the second example\n")

# Open an absolute file path.
file_path = 'C:/Users/xrist/Dropbox/001_education/004_python-work/src/'\
    'examples-chapter-10/pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)
print("-- end of the third example\n")

# Open an absolute path, using backslashes (for Windows only).
file_path = 'C:\\Users\\xrist\\Dropbox\\001_education\\004_python-work\\src\\'\
    'examples-chapter-10\\pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)
print("-- end of the fourth example\n")

# Read file line-by-line
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
print("-- end of the fifth example\n")

# Store contents in a list.
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print("-- end of the sixth example\n")