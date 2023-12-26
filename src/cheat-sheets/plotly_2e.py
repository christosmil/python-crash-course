"""
What is Plotly?
Data visualization involves exploring data through visual representations.
Plotly helps you make visually appealing representations of the date you're
working with. Plotly is particularly well suited for visualizations that will be
presented online, because it supports interactive elements.
"""

"""
Line graphs, scatter plots, and bar graphs
To make a plot with Plotly, you specify the data and then pass it to a graph
object. The data is stored in a list, so you can add as much data as you want to
any graph. In offline mode, the output should open automatically in a browser
window.
"""
# Making a line graph
from plotly.graph_objs import Scatter
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]

data = [Scatter(x=x_values, y=squares)]

offline.plot(data, filename='squares1.html')

# Making a scatter plot
from plotly.graph_objs import Bar
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]

data = [Bar(x=x_values, y=squares)]

offline.plot(data, filename='squares2.html')

"""
Adding a title and labels
"""
# Using layout objects
from plotly.graph_objs import Scatter, Layout
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]

data = [Scatter(x=x_values, y=squares)]

title = 'Square Numbers'
x_axis_config = {'title': 'x'}
y_axis_config = {'title': 'Square of x'}

my_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='squares3.html')

"""
Specifying Complex Data
"""
# Data as a dictionary
from plotly.graph_objs import Scatter, Layout
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]

data = [{
    'type': 'scatter',
    'x': x_values,
    'y': squares,
    'mode': 'markers',
}]

title = 'Square Numbers'
x_axis_config = {'title': 'x'}
y_axis_config = {'title': 'Square of x'}

my_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='squares4.html')

"""
Multiple plots
You can include as many data series as you want in a visualization. To do this,
create one dictionary for each data series, and put these dictionaries in the
data list. Each of these dictionaries is referred to as a trace in the Plotly
documentation.
"""
# Plotting squares and cubes
from plotly.graph_objs import Scatter
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

data = [
    {
        'type': 'scatter',
        'x': x_values,
        'y': squares,
        'name': 'Squares',
    },
    {
        'type': 'scatter',
        'x': x_values,
        'y': cubes,
        'name': 'Cubes',
    },
]

offline.plot(data, filename='squares_cubes1.html')

"""
Specifying complex layouts
You can also specify the layout of your visualization as a dictionary, which
gives you much more control of the overall layout.
"""
# Layout as a dictionary
from plotly.graph_objects import Scatter, Layout
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]

data = [{
    'type': 'scatter',
    'x': x_values,
    'y': squares,
    'mode': 'markers',
}]

my_layout = {
    'title': 'Square Numbers',
    'xaxis': {
        'title': 'x',
    },
    'yaxis': {
        'title': 'Square of x',
    },
}

offline.plot({'data': data, 'layout': my_layout}, filename='squares5.html')

# A more complex layout
from plotly.graph_objs import Scatter
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]

data = [{
    'type': 'scatter',
    'x': x_values,
    'y': squares,
    'mode': 'markers',
    'marker': {
        'size': 10,
        'color': '#6688dd',
    },
}]

my_layout = {
    'title': 'Square Numbers',
    'xaxis': {
        'title': 'x',
        'titlefont': {'family': 'monospace'},
    },
    'yaxis': {
        'title': 'Square of x',
        'titlefont': {'family': 'monospace'},
    },
}

offline.plot({'data': data, 'layout': my_layout}, filename='squares6.html')

# Using a colorscale
from plotly.graph_objs import Scatter
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]

data = [{
    'type': 'scatter',
    'x': x_values,
    'y': squares,
    'mode': 'markers',
    'marker': {
        'colorscale': 'Viridis',
        'color': squares,
        'colorbar': {'title': 'Value'},
    },
}]

my_layout = {
    'title': 'Square Numbers',
    'xaxis': {
        'title': 'x',
        'titlefont': {'family': 'monospace'},
    },
    'yaxis': {
        'title': 'Square of x',
        'titlefont': {'family': 'monospace'},
    },
}

offline.plot({'data': data, 'layout': my_layout}, filename='squares7.html')

"""
Using subplots
It's often useful to have multiple plots share the same axes. This is done using
the subplots module.
"""
# Adding subplots to a figure
from plotly.subplots import make_subplots
from plotly.graph_objs import Scatter
from plotly import offline

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

fig = make_subplots(rows=1, cols=2, shared_yaxes=True)

data = {
    'type': 'scatter',
    'x': x_values,
    'y': squares,
}
fig.add_trace(data, row=1, col=1)

data = {
    'type': 'scatter',
    'x': x_values,
    'y': cubes,
}
fig.add_trace(data, row=1, col=2)

offline.plot(fig, filename='subplots.html')

"""
Plotting global datasets
Plotly has a variety of mapping tools. For example, if you have a set of points
represented by latitude and longitude, you can create a scatter plot of those
points overlaying a map.
"""
# The scattergeo chart type
from plotly import offline

peak_coords = [(63.069, -151.0063), (60.5671, -140.4055), (46.8529, -121.7604)]

lats = [pc[0] for pc in peak_coords]
lons = [pc[1] for pc in peak_coords]
peak_names = ['Denali', 'Mt Logan', 'Mt Rainier']

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': 20,
        'color': '#227722',
    },
    'text': peak_names,
}]

my_layout = {
    'title': 'Selected High Peaks',
    'geo': {
        'scope': 'north america',
        'showland': True,
        'showocean': True,
        'showlakes': True,
        'showrivers': True,
    },
}

offline.plot({'data': data, 'layout': my_layout}, filename='peaks.html')