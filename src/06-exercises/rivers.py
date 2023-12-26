rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'tiber': 'italy',
}

# print a sentence for each key-value pair
for river, country in rivers.items():
    if country == 'usa':
        print(f"The {river.title()} runs through {country.upper()}.")
    else:
        print(f"The {river.title()} runs through {country.title()}.")

# loop through each key
for river in rivers.keys():
    print(river.title())

# loop through each value
for country in rivers.values ():
    if country == 'usa':
        print(country.upper())
    else:
        print(country.title())