from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Define number of sides, and number of rolls.
SIDES = 6
ROLLS = 1_000_000

# Create three D6s.
die_1 = Die(SIDES)
die_2 = Die(SIDES)
die_3 = Die(SIDES)

# Make some rolls, and store results in a list.
results = []
for roll_sum in range(ROLLS):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling three D{SIDES}s '\
    f'{"{:,}".format(ROLLS)} times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout},
    filename=f'd{SIDES}_d{SIDES}_d{SIDES}.html')