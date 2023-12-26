import json

file_name = 'username.json'

with open(file_name) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")