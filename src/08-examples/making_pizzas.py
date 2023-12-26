# Importing an entire module.
import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("-- end of the first example\n")

# Importing specific functions.
from pizza_module import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("-- end of the second example\n")

# Using as to give a function an alias.
from pizza_module import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green pepers', 'extra cheese')
print("-- end of the third example\n")

# Using as to give a module an alias.
import pizza_module as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("-- end of the fourth example\n")

# Importing all functions in a module.
from pizza_module import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')