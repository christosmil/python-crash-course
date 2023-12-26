print("Enter 'q' at any time to quit.")

while True:
    try:
        first_number = input("\nPlease, type the first integer:  ")
        if first_number == 'q':
            break
        first_number = int(first_number)
        second_number = input("Please, type the second integer: ")
        if second_number == 'q':
            break
        second_number = int(second_number)
    except ValueError:
        print("This is not an integer!")
    else:
        res = first_number + second_number
        print(f"{first_number} + {second_number} = {res}")