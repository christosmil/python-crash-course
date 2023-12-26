# Test strings equality and inequality
mathematician = 'euclid'
print("Is mathematician == 'euclid'? I predict True.")
print(mathematician == 'euclid')

print("\nIs mathematician == 'gauss' I predict False.")
print(mathematician == 'gauss')

# Test string equality and inequality using the lower() method
programmer = 'Dennis Ritchie'
print("\nIs programmer == 'Dennis Ritchie'? I predict True.")
print(programmer.lower() == 'dennis ritchie')

print("\nIs programmer == 'Linus Torvalds'? I predict False.")
print(programmer.lower() == 'Linus Torvalds')

# Numerical tests
year = 1970
print("\nIs year == 1970? I predict True.")
print(year == 1970)

print("\nIs year != 1970? I predict False.")
print(year != 1970)

print("\nIs year > 1970? I predict False.")
print(year > 1970)

print("\nIs year < 1970? I predict False.")
print(year < 1970)

print("\nIs year >= 1970? I predict True.")
print(year >= 1970)

print("\nIs year <= 1970? I predict True.")
print(year <= 1970)

# Tests with and keyword and or keyword
temp_inside = 22
temp_outside = 18
print("\nIs temp_inside > 21 and temp_outside > 18? I predict False.")
print(temp_inside > 21 and temp_outside > 18)

print("\nIs temp_inside != 22 or temp_outside <= 21? I predict True.")
print(temp_inside != 22 or temp_outside <= 21)

# Test whether an item is in a list
menu = ['carbonara', 'bolognese', 'cacio e pepe']
print("\nIs 'carbonara' in menu? I predict True.")
print('carbonara' in menu)

print("\nIs 'aglio e olio' in menu? I predict False.")
print('aglio e olio' in menu)

# Test whether an item is not in a list
countries = ['finland', 'russia', 'holland']
print("\nIs 'holland' not in countries? I predict False.")
print('holland' not in countries)

print("\nIs 'japan' not in countries? I predict True.")
print('japan' not in countries)