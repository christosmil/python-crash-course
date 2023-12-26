from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Define number of sides, and number of rolls.
SIDES = 6
ROLLS = 1_000_000

# Create two D6s.
die_1 = Die(SIDES)
die_2 = Die(SIDES)

# Make some rolls, and store results in a list.
results = []
for roll_sum in range(ROLLS):
    result = die_1.roll()*die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides*die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency/ROLLS)

# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequencies of Results'}
my_layout = Layout(title=f'Results of rolling two D{SIDES}s '\
    f'{"{:,}".format(ROLLS)} times and multiplying outcomes (pmf)',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename=f'd{SIDES}_'\
    f'd{SIDES}_multiplication.html')