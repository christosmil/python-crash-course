import json

file_name = 'favorite_number.json'

fav_number = int(input("What's your favorite number? "))
with open(file_name, 'w') as f:
    json.dump(fav_number, f)
    print(f"We'll remember that you favorite_number is {fav_number}.")