person_0 = {
    'first': 'lionel',
    'last': 'messi',
    'age': 35,
    'city': 'paris',
    }

person_1 = {
    'first': 'cristiano',
    'last': 'ronaldo',
    'age': 37,
    'city': 'manchester',
}

person_2 = {
    'first': 'sadio',
    'last': 'mane',
    'age': 30,
    'city': 'munich',
}

people = [person_0, person_1, person_2]

for person in people:
    first_name = person['first'].title()
    last_name = person['last'].title()
    age = person['age']
    city = person['city'].title()

    print(f"{first_name} {last_name} is {age} years old and lives in {city}.")