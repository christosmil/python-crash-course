# Defining a function.
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
print("-- end of the first example\n")

# Passing information to a function.
def greet_user_two(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user_two('jesse')
greet_user_two('sarah')
print("-- end of the second example\n")

# Using a function with a while loop.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")