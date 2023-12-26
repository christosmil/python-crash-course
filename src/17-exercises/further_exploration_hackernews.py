from datetime import datetime
from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline
import requests

TIME_FORMAT = '%b %d, %Y - %H:%M'
NUM_STORIES = 30

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/askstories.json'
r = requests.get(url)
print(r.status_code)
ask_stories = r.json()

labels, scores, hover_texts = [], [], []
ask_dicts = []
for ask_story in ask_stories[:NUM_STORIES]:
    ask_dict = {}

    # Make an API call for each story.
    url = f'https://hacker-news.firebaseio.com/v0/item/{ask_story}.json'
    r = requests.get(url)
    print(f"story: {ask_story}\tstatus_code: {r.status_code}")
    story_dict = r.json()

    # Get the title, the score, the author, the comments, and the timestamp.
    original_title = story_dict['title']
    if 'Ask HN: ' in original_title:
        original_title = original_title[len('Ask HN: '):]
    elif 'Tell HN: ' in original_title:
        original_title = original_title[len('Tell HN: '):]
    if len(original_title) >= 25:
        title = f"{original_title[:25]}..."
    else:
        title = original_title
    hn_url = f"https://news.ycombinator.com/item?id={ask_story}"
    label = f"<a href='{hn_url}'>{title}</a>"
    ask_dict['label'] = label

    ask_dict['score'] = story_dict['score']

    author = story_dict['by']
    comments = story_dict['descendants']
    timestamp = datetime.fromtimestamp(story_dict['time'])
    timestamp = f"{datetime.strftime(timestamp, TIME_FORMAT)}"
    hover_text = f"{original_title}<br />by {author}, {timestamp}<br />"\
        f"{comments} comment(s)"
    ask_dict['hover_text'] = hover_text

    ask_dicts.append(ask_dict)

# Sort the ask stories by score.
ask_dicts = sorted(ask_dicts, key=itemgetter('score'), reverse=True)

# Grab the lists of labels, scores, and hover texts.
labels, scores, hover_texts = [], [], []
for ask_dict in ask_dicts:
    labels.append(ask_dict['label'])
    scores.append(ask_dict['score'])
    hover_texts.append(ask_dict['hover_text'])

# Make the visualization.
data = [{
    'type': 'bar',
    'x': labels,
    'y': scores,
    'hovertext': hover_texts,
    'marker': {
        'color': 'rgb(40, 120, 180)',
        'line': {'width': 1.5, 'color': 'rgb(20, 60, 90)'}
    },
    'opacity': 0.6
}]

time = datetime.now()
time = datetime.strftime(time, TIME_FORMAT)
my_layout = {
    'title': f"Top {NUM_STORIES} Hacker News Ask Stories (Retrieved: {time})",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Story',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14, 'color': 'rgb(0, 0, 40)'}
    },
    'yaxis': {
        'title': 'Score',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='further-exploration-hackenews.html')