import matplotlib.pyplot as plt

from die import Die

# Define number of sides, and number of rolls.
SIDES = 6
ROLLS = 1_000_000

# Create two D6s.
die_1 = Die(SIDES)
die_2 = Die(SIDES)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_sum in range(ROLLS)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
x_values = range(2, max_result+1)
frequencies = [results.count(value)/ROLLS for value in x_values]

# Visualize the results.
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
ax.bar(x_values, frequencies, color=(0.1, 0.4, 0.8), tick_label=x_values)
ax.set_xlabel('Results', fontsize=14)
ax.set_ylabel('Frequency of Results', fontsize=14)
ax.tick_params(axis='both', labelsize=14)
ax.set_title(f'Result of rolling two D{SIDES}s {"{:,}".format(ROLLS)} times '\
    '(pmf)', fontsize=24)
plt.savefig(f'd{SIDES}_d{SIDES}_mpl.png', bbox_inches='tight')