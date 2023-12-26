favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

voters = ['alice', 'bob', 'edward', 'phil', 'trudy']

for voter in voters:
    if voter in favorite_languages.keys():
        print(f"{voter.title()}, thank you for taking the poll.")
    else:
        print(f"{voter.title()}, please take our poll!")