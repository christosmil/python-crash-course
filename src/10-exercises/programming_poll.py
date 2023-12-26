file_name = 'programming_poll.txt'

with open(file_name, 'w') as file_object:
    while True:
        response = input("\nWhy do you like programming? (enter 'q' to quit) ")
        if response == 'q':
            break
        else:
            file_object.write(f"{response}\n")