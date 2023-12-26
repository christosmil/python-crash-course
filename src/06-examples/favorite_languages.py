favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# additional stuff: I investigate the popularity of each language
popularity = {}
for person in favorite_languages:
    language = favorite_languages[person]
    if language in popularity:
        popularity[language] += 1
    else:
        popularity[language] = 1

for language in popularity:
    print(f"{language.title()}: {popularity[language]}")
print("-- end of the first example\n")

# loop through the key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print("-- end of the second example\n")

# loop through the keys
for name in favorite_languages.keys():
    print(name.title())

# the following code does the same; looping through the key is default
for name in favorite_languages:
    print(name.title())
print("-- end of the third example\n")

# access specific values through their keys
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}.")

    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language.title()}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print("-- end of the fourth example\n")

# loop in sorted order of keys
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print("-- end of the fifth example\n")

# loop through the values
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# better use a set, to eliminate duplicates
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print("-- end of the sixth example\n")

# store a list as a value
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# additional stuff: I investigate the popularity of each language
popularity = {}
for languages in favorite_languages.values():
    for language in languages:
        if language in popularity:
            popularity[language] += 1
        else:
            popularity[language] = 1

print(f"\nLanguages popularity")
for language, votes in popularity.items():
    print(f"{language.title()}: {votes}")
print("-- end of the seventh example\n")