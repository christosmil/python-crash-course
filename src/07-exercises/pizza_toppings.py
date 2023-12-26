prompt = "\nEnter a topping you want:"
prompt += "\n(Enter 'quit' to exit the program.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    print(f"Ok, I will add {topping} in the pizza!")
