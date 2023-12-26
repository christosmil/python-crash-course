# Store information about the pizzas being ordered.
pizza_0 = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    'customer': 'potter',
    'street': 'privet drive',
    'number': 4,
}

pizza_1 = {
    'crust': 'thick',
    'toppings': ['ham', 'bacon', 'green peppers'],
    'customer': 'black',
    'street': 'grimmauld place',
    'number': 12,
}

pizza_2 = {
    'crust': 'thick',
    'toppings': ['extra cheese', 'pepperoni', 'anchovies'],
    'customer': 'weasley',
    'street': 'ottery st catchpole',
    'number': 'The Burrow',
}

pizza_3 = {
    'crust': 'thin',
    'toppings': ['ham', 'extra cheese'],
    'customer': 'granger',
    'street': 'the ministry of magic',
    'number': '',
}

orders = [pizza_0, pizza_1, pizza_2, pizza_3]

# Summarize the orders
for order in orders:
    print(f"\nOne pizza with {order['crust']} crust, having as toppings:")
    for topping in order['toppings']:
        print(f"- {topping}")
    print(f"Address:  {order['street'].title()} {order['number']}")
    print(f"Doorbell: {order['customer'].title()}")