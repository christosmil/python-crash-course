def city_country(city, country):
    """Return the city and its country, neatly formatted."""
    neatly_formatted = f"{city}, {country}"
    return neatly_formatted.title()

neatly_formatted = city_country('santiago', 'chile')
print(neatly_formatted)

neatly_formatted = city_country('athens', 'greece')
print(neatly_formatted)

neatly_formatted = city_country('ottawa', 'canada')
print(neatly_formatted)