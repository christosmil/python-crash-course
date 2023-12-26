pizzas = ['margherita', 'ham and bacon', 'pepperoni']
for pizza in pizzas:
    print(pizza)
print("--\n")

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
print("--\n")

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
print("I really love pizza!")

# exercise 011_my-pizzas-your-pizzas starts here
print("--\n")
friend_pizzas = pizzas[:]
pizzas.append('la siciliana')
friend_pizzas.append('marinara')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")