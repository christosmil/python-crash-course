favorite_numbers = {
    'hamilton': [44, 1, 2],
    'vettel': [5, 15, 10],
    'rosberg': [6],
    'alonso': [14, 8],
    'verstappen': [3, 33, 1],
}

for person, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{person.title()}'s favorite number is:")
    else:
        print(f"\n{person.title()}'s favorite number's are:")
    for number in numbers:
        print(f"\t{number}")