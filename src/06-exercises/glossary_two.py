glossary = {
    'tuple': 'an immutable list.',
    'immutable': 'An object which value cannot change.',
    'dictionary': 'A collection of key-value pairs.',
    'slice': 'A specific group of items in a list.',
    'string': 'A series of characters.',
    'set': 'A collection of unique items.',
    'list': 'A collection of (not necessarily) related items.',
    'key-value pair': 'A set of values associated with each other.',
    'variable': 'A reference to a value.',
    'method': 'An action that Python can perform on a piece of data.',
}

for term, definition in glossary.items():
    print(f"\n{term.title()}\n\t{definition}")