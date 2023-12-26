while True:
    age = input("\nWhat is your age?\n(Enter 'quit' to exit the program.) ")

    if age == 'quit':
        break

    try:
        age = int(age)
    except ValueError:
        print("Please type an integer or 'quit' to exit.")
    else:
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15
        print(f"Your ticket costs ${price}.")