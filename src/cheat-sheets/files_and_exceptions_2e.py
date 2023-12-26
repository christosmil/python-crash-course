"""
Files and Exceptions
You programs can read information in from files, and they can write data to
files. Reading from files allows you to work with a wide variety of information;
writing to files allows users to pick up where they left off the next time they
run your program. You can write text to files, and you can store Python
structures such as lists in data files. Exceptions are special objects that help
your programs respond to errors in appropriate ways. For example if your program
tries to open a file that doesn't exist, you can use exceptions to display an
informative error message instead of having the program crash.
"""

"""
Reading from a file
To read from a file your program needs to open the file and then read the
contents of the file. You can read the entire contents of the file at once, or
read the file line by line. The with statement makes sure the file is closed
properly when the program has finished accessing the file.
"""
# Reading an entire file at once
filename = 'siddhartha.txt'

with open(filename) as f_obj:
    contents = f_obj.read()

print(contents)

# Reading line by line
filename = 'siddhartha.txt'

with open(filename) as f_obj:
    for line in f_obj:
        print(line.rstrip())

# Working with a file's lines
filename = 'siddhartha.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.rstrip())

"""
Writing to a file
Passing the 'w' argument to open() tells Python you want to write to the file.
Be careful; this will erase the contents of the file if it already exists.
Passing the 'a' argument tells Python you want to append to the end of an
existing file.
"""
# Writing to an empty file
filename = 'programming.txt'

with open(filename, 'w') as f:
    f.write("I love programming!")

# Writing multiple lines to an empty file
filename = 'programming.txt'

with open(filename, 'w') as f:
    f.write("I love programming!\n")
    f.write("I love creating new games.\n")

# Appending to a file
filename = 'programming.txt'

with open(filename, 'a') as f:
    f.write("I also love working with data.\n")
    f.write("I love making apps as well.\n")

"""
File paths
When Python runs the open() function, it looks for the file in the same
directory where the program that's being executed is stored. You can open a file
from a subfolder using a relative path. You can also use an absolute path to
open any file on your system.
"""
# Opening a file from a subfolder
f_path = "text_files/alice.txt"

with open(f_path, encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

# Opening a file using an absolute path
f_path = "../../src/cheat-sheets/text_files/alice.txt"

with open(f_path, encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

# Opening a file in Windows
f_path = "..\\..\\src\\cheat-sheets\\text_files\\alice.txt"

with open(f_path, encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

"""
The try-except block
When you think an error may occur, you can write a try-except block to handle
the exception that might be raised. The try block tells Python to try running
some code, and the except block tells Python what to do if the code results in a
particular kind of error.
"""
# Handling the ZeroDivisionError exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Handling the FileNotFoundError exception
f_name = 'sidhartha.txt'

try:
    with open(f_name) as f:
        lines = f.readlines()
except FileNotFoundError:
    msg = f"Can't find file: {f_name}"
    print(msg)

"""
The else block
The try block should only contain code tha may cause an error. Any code that
depends on the try block running successfully should be placed in the else
block.
"""
# Using an else block
print("Enter two numbers. I'll divide them.")

x = input("First number: ")
y = input("Second number: ")

try:
    result = int(x) / int(y)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(result)

# Preventing crashes from user input
print("Enter two numbers. I'll divide them.")
print("Enter 'q' to quit.")

while True:
    x = input("\nFirst number: ")
    if x == 'q':
        break
    y = input("Second number: ")
    if y == 'q':
        break

    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(result)

"""
Failing silently
Sometimes you want your program to just continue running when it encounters an
error, without reporting the error to the user. Using the pass statement in an
else block allows you to do this.
"""
# Using the pass statement in an else block
f_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for f_name in f_names:
    try:
        with open(f_name) as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        num_lines = len(lines)
        msg = f"{f_name} has {num_lines} lines."
        print(msg)

"""
Avoid bare except blocks
Exception-handling code should catch specific exceptions that you expect to
happen during your program's execution. A bare except block will catch all
exceptions, including keyboard interrupts and system exits you might need when
forcing a program to close. If you want to use a try block and you're not sure
which exception to catch use Exception. It will catch most exceptions, but still
allow you to interrupt programs intentionally.
"""

# Don't use bare except blocks
try:
    res = 1/0
except:
    pass

# Use exception instead
try:
    res = 1/0
except Exception:
    pass

# Printing the exception
try:
    res = 1/0
except Exception as e:
    print(e, type(e))

"""
Storing data with json
The json module allows you to dump simple Python data structures into a file,
and load the data from that file the next time the program runs. The JSON data
format ins not specific to Python, so you can share this kind of data with
people who work in other languages as well. Knowing how to manage exceptions is
important when working with stored data. You'll usually want to make sure the
data you're trying to load exists before working with it.
"""
# Using json.dump() to store data
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# Using json.load() to read data
import json

filename = 'numbers.json'
with open(filename) as f:
    number = json.load(f)

print(numbers)

# Making sure the stored data exists
import json

f_name = 'numbers1.json'

try:
    with open(f_name) as f:
        numbers = json.load(f)
except FileNotFoundError:
    msg = f"Can't find file: {f_name}."
    print(msg)
else:
        print(numbers)