# Arbitrary number of arguments
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print("-- end of the first example\n")

# Mixing positional and arbitrary arguments
def make_pizza_two(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza_two(16, 'pepperoni')
make_pizza_two(12, 'mushrooms', 'green peppers', 'extra cheese')
print("-- end of the second example\n")