from datetime import datetime
from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(r.status_code)

# Process information about each submission.
STORIES_NUM = 30
items = r.json()
item_dicts = []
for item in items[:STORIES_NUM]:
    # Make a separate API call for each item.
    url = f'https://hacker-news.firebaseio.com/v0/item/{item}.json'
    r = requests.get(url)
    print(f'id: {item}\tstatus: {r.status_code}')
    response_dict = r.json()

    # Build a dictionary for each item.
    item_dict = {}
    try:
        num_comments = response_dict['descendants']
    except KeyError:
        print(f'\t{item} is a job posting...')
    else:
        original_title = response_dict['title']
        if len(original_title) >= 20:
            title = f"{original_title[:20]}..."
        else:
            title = original_title
        hn_url = f"https://news.ycombinator.com/item?id={item}"
        link = f"<a href='{hn_url}'>{title}</a>"
        item_dict['link'] = link

        item_dict['comments'] = num_comments

        author = response_dict['by']
        date = datetime.fromtimestamp(response_dict['time'])
        date = datetime.strftime(date, '%Y/%m/%d - %H:%M:%S')
        hover_text = f"{original_title}<br />by {author}, {date}"
        item_dict['hover_text'] = hover_text

        item_dicts.append(item_dict)

item_dicts = sorted(item_dicts, key=itemgetter('comments'), reverse=True)

# Generate lists for plotting.
links, comments, hover_texts = [], [], []
for item_dict in item_dicts:
    links.append(item_dict['link'])
    comments.append(item_dict['comments'])
    hover_texts.append(item_dict['hover_text'])

# Make visualization.
data = [{
    'type': 'bar',
    'x': links,
    'y': comments,
    'hovertext': hover_texts,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

time = datetime.now()
time = datetime.strftime(time, 'on %b %d, %Y at %H:%M:%S')
total_stories = len(item_dicts)
title = f'HackerNews Top {total_stories} Commented Active Disussions {time}'
my_layout = {
    'title': title,
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Stories',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis':  {
        'title': 'Number of Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='active-discussions.html')