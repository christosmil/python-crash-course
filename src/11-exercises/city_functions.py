"""A collection of functions for working with cities."""

def get_formatted_city(city, country, population=''):
    """Generate a neatly formatted city name."""
    formatted_name = f"{city}, {country}".title()
    if population:
        formatted_name += f" - population {population}"
    return formatted_name