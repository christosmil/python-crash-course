pet_0 = {
    'kind': 'cat',
    'owner': 'alice',
}

pet_1 = {
    'kind': 'dog',
    'owner': 'bob',
}

pet_2 = {
    'kind': 'bird',
    'owner': 'eve',
}

pet_3 = {
    'kind': 'fish',
    'owner': 'trudy',
}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"{owner.title()} owns a {kind}.")