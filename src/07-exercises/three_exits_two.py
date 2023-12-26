prompt = "\nEnter your age:\n(Enter 'quit' to exit the program.) "

# Version 1: using a conditional test in the while statement
age = ''
while age != 'quit':
    age = input(prompt)

    if age != 'quit':
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15
        print(f"Your ticket costs ${price}.")
print("-- end of the first version\n")

# Version 2: using an active variable
active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15
        print(f"Your ticket costs ${price}.")
print("-- end of the second version\n")

# Version 3: using a break statement
while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    elif age > 12:
        price = 15
    print(f"Your ticket costs ${price}.")
print("-- end of the third version\n")