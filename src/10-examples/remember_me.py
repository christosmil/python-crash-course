import json

username = input("What is your name? ")

file_name = 'username.json'
with open(file_name, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")