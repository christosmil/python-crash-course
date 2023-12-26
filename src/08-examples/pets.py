def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Use positional arguments.
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Careful, not to mix up the order of positional arguments.
describe_pet('harry', 'hamster')
print("-- end of the first example")

# Use keyword arguments.
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Careful on keywords' names.
# The following code would result in a TypeError.
# describe_pet(animal_type='hamster', animal_name='harry')

# Do not mix up positional and keyword arguments.
# The following code would result in a SyntaxError.
# describe_pet(animal_type='hamster', 'harry')
# The following code could result in TypeError
# describe_pet('harry', animal_type='hamster')
# The following code execure correctly
# describe_pet('hamster', pet_name='harry')

print("-- end of the second example")

# Use default values for function parameters.
def describe_pet_default(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_default('willie')
describe_pet_default(pet_name='harry', animal_type='hamster')
print("-- end of the third example")

# Equivalent function calls.
# A dog named Willie.
describe_pet_default('willie')
describe_pet_default(pet_name='willie')

# A hamster named Harry.
describe_pet_default('harry', 'hamster')
describe_pet_default(pet_name='harry', animal_type='hamster')
describe_pet_default(animal_type='hamster', pet_name='harry')
print("-- end of the fourth example")

# Avoiding argument errors
# The following code will result in TypeError (missing arguments).
# describe_pet()
# The following code will result in TypeError (too many arguments).
# describe_pet('dog', 'willie', 'beagle')