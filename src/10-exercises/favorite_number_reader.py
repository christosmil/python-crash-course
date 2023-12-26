import json

file_name = 'favorite_number.json'
try:
    with open(file_name) as f:
        fav_number = json.load(f)
except FileNotFoundError:
    print("Awww, I don't know what is your favorite number.")
else:
    print(f"I know your favorite number! It's {fav_number}.")