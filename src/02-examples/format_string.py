"""
f-strings were introduced in Python 3.6.
For Python 3.5 or earlier, I can use the format() method.
"""

first_name = "ada"
last_name = "lovelace"
full_name = "{} {}". format(first_name, last_name)
message = "Hello, {}!".format(full_name.title())
print(message)