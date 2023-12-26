prompt = "\nEnter a topping you want:"
prompt += "\n(Enter 'quit' to exit the program.) "

# Version 1: using a conditional test in the while statement
topping = ''
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Ok, I will add {topping} in the pizza!")
print("-- end of the first version\n")

# Version 2: using an active variable
active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Ok, I will add {topping} in the pizza!")
print("-- end of the second version\n")

# Version 3: using a break statement
while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    print(f"Ok, I will add {topping} in the pizza!")
print("-- end of the third version\n")