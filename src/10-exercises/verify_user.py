import json

def get_stored_username():
    """Get stored username if available."""
    file_name = 'username.json'
    try:
        with open(file_name) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your username? ")
    file_name = 'username.json'
    with open(file_name, 'w') as f:
        json.dump(username, f)
    return username

def check_username(username):
    """Checks if a user is the correct one."""
    answer = input(f"Are you {username}? (Y/n) ")
    if answer.lower() == 'y':
        return True
    return False

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username and check_username(username):
        print(f"Welcome back, {username}!")
        return
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")

greet_user()