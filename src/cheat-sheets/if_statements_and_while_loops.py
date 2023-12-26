"""
If Statements and While Loops
Python's if statements allow you to examine the current state of a program and
respond appropriately to that state. You can write a simple if statement that
checks one condition, or you can create a complex series of statements that
identify the exact conditions you're interested in. while loops run as longs as
certain conditions remain true. You can use while loops to let your programs run
as long as your users went them to.
"""

"""
Conditional Tests
A conditional test is an expression that can be evaluated as true or false.
Python uses the values True and False to decide whether the code in an if
statement should be executed.
"""
# Checking for equality
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

# Ignoring case when making a comparison
car = 'Audi'
print(car.lower() == 'audi')

# Checking for inequality
topping = 'mushrooms'
print(topping != 'anchovies')

"""
Numerical comparisons
Testing numerical values is similar to testing string values.
"""
# Testing equality and inequality
age = 18
print(age == 18)
print(age != 18)

# Comparison operators
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

"""
Checking multiple conditions
You can check multiple conditions at the same time. The and operator return True
if all the conditions listed are true. The or operator return True if any
condition is true.
"""
# Using and to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 23
print(age_0 >= 21 and age_1 >= 21)

# Using or to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

"""
Boolean values
A boolean value is either True or False. Variables with boolean values are often
used to keep track of certain conditions within a program.
"""
# Simple boolean values
game_active = True
is_valid = True
can_edit = False

"""
If statements
Several kinds of if statements exist. Your choice of which to use depends on the
number of conditions you need to test. You can have as many elif blocks as you
need and the else block is always optional.
"""
# Simple if statement
age = 19

if age >= 18:
    print("You're old enough to vote!")

# If-else statements
age = 17

if age >= 18:
    print("You're old enough to vote!")
else:
    print("You can't vote yet!")

# The if-elif-else chain
age = 12

if age < 4:
    price = 0
elif age < 19:
    price = 25
else:
    price = 40

print(f"Your cost is ${price}.")

"""
Conditional tests with lists
You can easily test whether a certain value is in a list. You can also test
whether a list is empty before trying to loop through a list.
"""
# Test if a value is in a list
players = ['al', 'bea', 'cyn', 'dale']
print('al' in players)
print('eric' in players)

# Test if two values are in a list
print('al' in players and 'cyn' in players)

# Testing if a value is not in a list
banned_users = ['ann', 'chad', 'dee']
user = 'erin'

if user not in banned_users:
    print("You can play!")

# Checking if a list is empty
players = []

if players:
    for player in players:
        print(f"Player: {player.title()}")
else:
    print("We have no players yet!")

"""
Accepting input
You can allow your users to enter input using the input() function. All input is
initially stored as a string. If you want to accept numerical input, you'll need
to convert the input string value to a numerical type.
"""
# Simple input
name = input("What's your name? ")
print(f"Hello, {name}.")

# Accepting numerical input using int()
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("\nYou can vote!")
else:
    print("\nSorry, you can't vote yet.")

# Accepting numerical input using float()
tip = input("How much do you want to tip? ")
tip = float(tip)
print(f"Tipped ${tip}")

"""
While loops
A while loop repeats a block of code as long as a condition is true.
"""
# Counting to 5
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the user choose when to quit.
prompt = "\nTell me something, and I'll repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Using a flag
prompt = "\nTell me something and I'll repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to exit a loop
prompt = "\nWhat cities have you visited? Enter 'quit' when you're done. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I've been to {city}!")

"""
Breaking out of loops
You can use the break statement and the continue statement with any of the
Python's loops. For example you can use break to quit a for loop that's working
through a list or a dictionary. You can use continue to skip over certain items
when looping through a list or dictionary as well.
"""
# Using continue in a loop
banned_users = ['eve', 'fred', 'gary', 'helen']

prompt = "\nAdd a player to your team.\nEnter 'quit' when you're done. "

players = []
while True:
    player = input(prompt)

    if player == 'quit':
        break
    elif player in banned_users:
        print(f"{player} is banned!")
        continue
    else:
        players.append(player)

print("\nYour team:")
for player in players:
    print(player)

"""
Avoiding infinite loops
Every while loop needs a way to stop running so it won't continue to run
forever. If there's no way for the condition to become false, the loop will
never stop running. You can usually press Ctrl-C to stop an infinite loop.
"""
# An infinite loop
# while True:
#     name = input("\nWho are you? ")
#     print(f"Nice to meet you, {name}!")

"""
Removing all instances of a value from a list
The remove() method removes a specific value from a list, but it only removes
the first instance of the value you provide. You can use a while loop to remove
all instances of a particular value.
"""
# Removing all cats from a list of pets
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)