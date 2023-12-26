file_name = 'guest_book.txt'

with open(file_name, 'w') as file_object:
    while True:
        user_name = input("\nHello, what's your name? (enter 'q' to quit) ")
        if user_name == 'q':
            break
        else:
            print(f"Hello {user_name}, nice to have you with us!")
            file_object.write(f"{user_name}\n")