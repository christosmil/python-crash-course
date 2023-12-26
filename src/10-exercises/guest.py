file_name = 'guest.txt'

user_name = input("Hello, what's your name? ")

with open(file_name, 'w') as file_object:
    file_object.write(user_name)