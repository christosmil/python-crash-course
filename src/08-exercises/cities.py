def describe_city(city, country='australia'):
    """Displays city's name and country."""
    print(f"{city.title()} is in {country.title()}.")

# Use positional arguments, without using the default value.
describe_city('athens', 'greece')

# Use keyword arguments, without using the default value.
describe_city(city='rome', country='italy')

# Use positional arguments, using the default value
describe_city('sydney')

# Use keyword arguments, using the default value.
describe_city(city='canberra')