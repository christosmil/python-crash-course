def build_profile(first, last, **user_info):
    """Build a dictionary containing anything we know about a user."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile(
    'christos',
    'milarokostas',
    location='athens',
    field='informatics',
    sport='football'
    )
print(user_profile)