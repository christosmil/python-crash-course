person = {
    'first_name': 'lionel',
    'last_name': 'messi',
    'age': 35,
    'city': 'paris',
    }

print(person)

# neatly formatted
first_name = person['first_name'].title()
last_name = person['last_name'].title()
age = person['age']
city = person['city'].title()

print(f"{first_name} {last_name} is {age} years old and lives in {city}.")