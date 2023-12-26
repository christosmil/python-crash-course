from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline
import requests

USERS = [
    'adobe', 'apple', 'aws', 'facebook', 'google', 'IBM', 'microsoft', 'nasa',
    'netflix', 'oracle', 'salesforce'
    ]
USER = USERS[7]
HEADERS = {'Accepts': 'application/vnd.github.v3+json'}

def api_call(url):
    """Makes an API call and stores the response."""
    r = requests.get(url, headers=HEADERS)
    print(r.status_code)
    resp_dict = r.json()
    return resp_dict

# Get the main language of each repo and count the instances of each language.
url = f'https://api.github.com/search/repositories?q=user:{USER}&per_page=100'
response_dict = api_call(url) 
total_repos = response_dict['total_count']
repos_left = total_repos - 100
languages = []
page = 1
while repos_left > -100:
    repo_dicts = response_dict['items']

    for repo_dict in repo_dicts:
        languages.append(repo_dict['language'])

    # Stop if API rate limit has been reached or 1_000 repos have been returned.
    url = 'https://api.github.com/rate_limit'
    r = requests.get(url, headers=HEADERS)
    response_dict = r.json()
    if (response_dict['resources']['search']['remaining'] == 0
        or total_repos - repos_left >= 1000):
        break

    # Make the API call for the next page.
    page += 1
    url = f'https://api.github.com/search/repositories?q=user:{USER}'\
        f'&per_page=100&page={page}'
    response_dict = api_call(url)
    repos_left -= 100

# Count the occurences of each language.
lang_dict = {}
for language in set(languages):
    lang_dict[language] = languages.count(language)

# Sort the languages by the number of occurences.
languages = sorted(lang_dict.items(), key=itemgetter(1), reverse=True)
labels, occurences = [], []
for language in languages:
    labels.append(language[0])
    occurences.append(language[1])

# Make the visualization.
data = [{
    'type': 'bar',
    'x': labels,
    'y': occurences,
    'marker': {
        'color': 'rgb(40, 120, 180)',
        'line': {'width': 2, 'color': 'rgb(20, 60, 90)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': f"Languages used in {USER.upper()}'s GitHub repositories",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': "Main Repository's Language",
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Occurences',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'further-exploration-github-{USER.lower()}.html')