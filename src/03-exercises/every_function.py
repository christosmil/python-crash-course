languages = ['english', 'greek', 'german', 'spanish', 'russian']
print(f"Original: {languages}")

add_language = 'french'
languages.append(add_language)
print(f"Added {add_language.title()} in {languages}.")

del languages[5]
print(f"Deleted the last from {languages}")

add_language = 'french'
languages.insert(4, add_language)
print(f"Added {add_language.title()} in {languages}.")

popped_language = languages.pop(4)
print(f"There are no more {popped_language.title()} in {languages}.")

removed_language = 'german'
languages.remove(removed_language)
print(f"There are no more {removed_language.title()} in {languages}.")

print(f"Temporarily sorted ascending: {sorted(languages)}")
print(f"Temporarily sorted descending: {sorted(languages, reverse=True)}")

print(f"Original: {languages}")
languages.reverse()
print(f"Reversed: {languages}")

languages.sort()
print(f"Permanently sorted ascending: {languages}")

languages.sort(reverse = True)
print(f"Permanently sorted descending: {languages}")

print(f"Cool! I know {len(languages)} languages!")