def create_hp_character(first, last, *args, middle='', pet, **kwargs):
    """Build a character from the universe of Harry Potter."""
    kwargs['first'] = first
    kwargs['last'] = last
    kwargs['other characteristics'] = []
    for arg in args:
        kwargs['other characteristics'].append(arg)
    kwargs['pet'] = pet
    kwargs['middle'] = middle
    return kwargs

character = create_hp_character('ronald', 'weasley', 'won-won', 'aragog',
    pet='scabers', house='gryffindor', patronus='jack russell terrier')
print(character)

def create_sw_character(first, *args, last):
    character = {}
    character['first'] = first
    character['last'] = last
    character['other characteristics'] = []
    for arg in args:
        character['other characteristics'].append(arg)
    return character

character = create_sw_character('anakin', 'tatooine', last='skywalker')
print(character)