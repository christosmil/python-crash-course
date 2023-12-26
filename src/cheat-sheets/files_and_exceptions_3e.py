"""
Files and Exceptions
Your programs can read information in from files, and they can write data to
files. Reading from files allows you to work with a wide variety of information;
writing to files allows users to pick up where they left off the next time they
run your program. You can write text to files, and you can store Python
structures such as lists in data files as well. Exceptions are special objects
that help your programs respond to errors in appropriate ways. For example if
your program tries to open a file that doesn't exist, you can use exceptions to
display an informative message instead of having the program crash.
"""

"""
Reading from a file
To read from a file your program needs to specify a path to the file, and then
read the contents of the file. The read_text() method returns a string
containing the entire contents of the file.
"""
# Reading an entire file at once
from pathlib import Path

path = Path('siddhartha.txt')
contents = path.read_text()
print(contents)

# Working a file's lines
from pathlib import Path

path = Path('siddhartha.txt')
contents = path.read_text()
lines = contents.splitlines()

for line in lines:
    print(line)

"""
Writing to a file
The write_text() method can be used to write text to a file. Be careful, this
will write over the current file if it already exists. To append to a file, read
the contents first and then rewrite the entire file.
"""
# Writing to a file
from pathlib import Path

path = Path('programming.txt')
msg = "I love programming!"
path.write_text(msg)

# Writing multiple lines to a file
from pathlib import Path

path = Path('programming.txt')
msg = "I love programming!"
msg += "\nI love making games."
path.write_text(msg)

# Appending to a file
from pathlib import Path

path = Path('programming.txt')
contents = path.read_text()
contents += "\nI love programming!"
contents += "\nI love making games."
path.write_text(contents)

"""
Path objects
The pathlib module makes it easier to work with files in Python. A Path object
represents a file or directory, and let's you carry out common directory and
file operations. With a relative path, Python usually looks for a location
relative to the .py file that's running. Absolute paths are relative to your
system's root folder("/"). Windows uses backslashes when displaying file paths,
but you should use forward slashes in your Python code.
"""
# Relative path
path = Path("alice.txt")

# Absolute path
path = Path("../cheat-sheets/alice.txt")

# Get just the filename from a path
print(path.name)

# Build a path
base_path = Path("../cheat-sheets")
file_path = base_path / "alice.txt"

# Check if a file exists
path = Path("../cheat-sheets/alice.txt")
print(path.exists())

# Get filetype
print(path.suffix)

"""
The try-except block
When you think an error may occur, you can write a try-except block to handle
the exception that might be raised. The try block tells Python to try running
some code, and the except block tells Python what to do if the code results in a
particular error.
"""
# Handling the ZeroDivisionError exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Handling the FileNotFoundError exception
from pathlib import Path

path = Path("sidhartha.txt")
try:
    contents = path.read_text()
except FileNotFoundError:
    msg = f"Can't find file: {path.name}."
    print(msg)

"""
The else block
The try block should only contain code that may cause an error. Any code that
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

# Preventing crashed caused by user input
print("Enter two number. I'll divide them.")
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
except block allows you to do this.
"""
# Using the pass statement in an except block
from pathlib import Path

f_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for f_name in f_names:
    path = Path(f_name)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        lines = contents.splitlines()
        msg = f"{f_name} has {len(lines)}"
        msg += " lines."
        print(msg)

"""
Avoid bare except blocks
Exception handling code should catch exceptions that you expect to happen during
your program's execution. A bare except block will catch all exceptions,
including keyboard interrupts and system exits you might need when forcing a
program to close. If you want to use a try block and you're not sure which
exception to catch, use Exception. It will catch most exceptions, but still
allow you to interrupt programs intentionally.
"""
# Don't use bare except blocks
try:
    res = 1/0
except:
    pass

# Use Exception instead
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
format is not specific to Python, so you can share this kind of data with people
who workin other languages as well. Knowing how to manage exceptions is
important when working with stored data. You'll usually want to make sure the
data you're trying to load exists before working with it.
"""
# Using json.dumps() to store data
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

# Using json.loads() to read data
from pathlib import Path
import json

path = Path("numbers.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)

# Making sure the stored data exists
from pathlib import Path
import json

path = Path("numbers1.json")

try:
    contents = path.read_text()
except FileNotFoundError:
    msg = f"Can't find file: {path}"
    print(msg)
else:
    numbers = json.loads(contents)
    print(numbers)
