from plotly.graph_objs import Scatter, Layout
from plotly import offline

from random_walk import RandomWalk

# Define number of steps
STEPS = 10_000

# Make a random walk.
rw = RandomWalk(STEPS)
rw.fill_walk()

# Visualize the results.
data = [
    Scatter(x=rw.x_values, y=rw.y_values, marker={'color': '#22cc88'},
        name='Random Walk'),
    Scatter(x=[0], y=[0], marker={'color': '#2266cc', 'size': 14},
        name='start point'),
    Scatter(x=[rw.x_values[-1]], y=[rw.y_values[-1]],
        marker={'color': '#dd1155', 'size': 14}, name='end point')
    ]

x_axis_config = {'title': '', 'showgrid': False, 'showticklabels': False}
y_axis_config = {'title': '', 'showgrid': False, 'showticklabels': False}

my_layout = Layout(title=f'Result of a random walk of {"{:,}".format(STEPS)} '\
    'steps', xaxis=x_axis_config, yaxis=y_axis_config, showlegend=False)
offline.plot({'data': data, 'layout': my_layout}, filename=f'rw_{STEPS}.html')