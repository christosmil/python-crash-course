import json


def retrieve_number():
    """Retrieve the favorite number if available."""
    file_name = 'favorite_number.json'
    try:
        with open(file_name) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number


def input_number():
    """Read a number from user; return None if it wasn't an integer."""
    try:
        fav_number = int(input("What's your favorite number? "))
    except ValueError:
        print("This is not an integer!")
        return None
    else:
        return fav_number


def read_new_number():
    """Store the favorite number."""
    file_name = 'favorite_number.json'
    fav_number = None
    while not fav_number:
        fav_number = input_number()
    with open(file_name, 'w') as f:
        json.dump(fav_number, f)
    return fav_number


def favorite_number():
    """Either print user's favorite number or ask for it."""
    fav_number = retrieve_number()
    if fav_number:
        print(f"I know your favorite number! It's {fav_number}.")
    else:
        fav_number = read_new_number()
        print(f"We'll remember that your favorite number is {fav_number}.")


favorite_number()