favorite_places = {
    'lewis': ['england', 'brazil'],
    'sebastian': ['germany', 'japan', 'italy'],
    'max': ['holland'],
}

for person, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{person.title()}'s favorite place is:")
    else:
        print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")