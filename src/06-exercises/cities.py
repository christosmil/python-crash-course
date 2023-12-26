cities = {
    'athens': {
        'country': 'greece',
        'population': 3_722_544,
        'fact': 'Devoted to the goddess Athena.',
    },
    'rome': {
        'country': 'italy',
        'population': 4_342_212,
        'fact': 'Founded by the king Romulus.',
    },
    'barcelona': {
        'country': 'spain',
        'population': 5_474_482,
        'fact': 'Has the best road system.',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"* Country: {info['country'].title()}")
    print(f"* Population: {info['population']}")
    print(f"* Fact: {info['fact']}")