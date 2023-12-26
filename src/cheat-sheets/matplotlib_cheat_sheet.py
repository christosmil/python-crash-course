"""
Matplotlib
Data visualization involves exploring data throufh visual representations. The
Matplotlib library helps you make visually appealing representations of the data
you're working with. Matplotlib is extremely flexible; these examples will help
you get started with a few simple visualizations. Many newer plotting libraries
are wrappers around Matplotlib, and understanding Matplotlib will help you use
those libraries more effectively as well.
"""

"""
Line graphs and scatter plots
"""
# Making a line graph
import matplotlib.pyplot as plt

x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(x_values, squares)

# plt.show()

# Making a scatter plot
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, squares, s=10)

# plt.show()

"""
Customizing plots
Plots can be customized in a wide variety of ways. Just about any element of a
plot can be modified.
"""
# Using built-in styles
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, squares, s=10)

# plt.show()

# Adding titles and labels, and scaling axes
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, squares, s=10)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

ax.axis([0, 1_100, 0, 1_100_000])
ax.tick_params(axis='both', labelsize=14)

# plt.show()

# Using a colormap
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, squares, c=x_values, cmap=plt.cm.Blues, s=10)

# plt.show()

# Emphasizing points
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, squares, c=squares, cmap=plt.cm.Blues, s=10)
ax.scatter(x_values[0], squares[0], c='green', s=100)
ax.scatter(x_values[-1], squares[-1], c='red', s=100)

ax.set_title('Square Numbers', fontsize=24)

# plt.show()

# Removing axes
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, squares, s=10)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# plt.show()

# Setting a custom figure size
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]

fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.scatter(x_values, squares, s=10)

# plt.show()

# Saving a plot
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, squares, s=10)

# plt.savefig('squares.png', bbox_inches='tight')

"""
Multiple plots
You can make as many plots as you want on one figure. When you make multiple
plots, you can emphasize relationships in the data. For example you can fill the
space between two sets of data.
"""
# Plotting two sets of data
import matplotlib.pyplot as plt

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, squares, c='blue', s=10)
ax.scatter(x_values, cubes, c='red', s=10)

# plt.show()

# Filling the space between data sets
import matplotlib.pyplot as plt

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, squares, color='blue', s=10)
ax.scatter(x_values, cubes, color='red', s=10)

ax.fill_between(x_values, cubes, squares, facecolor='blue', alpha=0.25)

# plt.show()

"""
Working with dates and times
Many interesting data sets have a date or time as the x value. Python's datetime
module helps you work with this kind of data.
"""
# Generating the current date
from datetime import datetime as dt

today = dt.now()
date_string = today.strftime('%m/%d/%Y')
print(date_string)

# Generating a specific date
from datetime import datetime as dt

new_years = dt(2023, 1, 1)
fall_equinox = dt(year=2023, month=9, day=22)
print(f"{new_years} {fall_equinox}")

# Datetime formatting arguments
new_years = dt.strptime('1/1/2023', '%m/%d/%Y')
print(new_years)

ny_string = new_years.strftime('%B %d, %Y')
print(ny_string)

# Plotting high temperatures
from datetime import datetime as dt

import matplotlib.pyplot as plt
from matplotlib import dates as mdates

dates = [dt(2023, 6, 21), dt(2023,6,22), dt(2023, 6, 23), dt(2023, 6, 24)]
highs = [56, 57, 57, 64]

plt.style.use('seaborn-v0_8');
fig, ax = plt.subplots();
ax.plot(dates, highs, c='red')

ax.set_title('Daily High Temps', fontsize=24)
ax.set_ylabel('Temp (F)', fontsize=16)
x_axis = ax.get_xaxis()
x_axis.set_major_formatter(mdates.DateFormatter('%B %d %Y'))
fig.autofmt_xdate()

# plt.show()

"""
Multiple plots in one figure
You can include as many individual graphs in one figure as you want.
"""
# Sharing an x-axis
import matplotlib.pyplot as plt

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].scatter(x_values, squares)
axs[0].set_title('Squares')

axs[1].scatter(x_values, cubes, c='red')
axs[1].set_title('Cubes')

# plt.show()

# Sharing a y-axis
import matplotlib.pyplot as plt

x_values = list(range(11))

squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, axs = plt.subplots(1, 2, sharey=True)

axs[0].scatter(x_values, squares)
axs[0].set_title('Squares')

axs[1].scatter(x_values, cubes, c='red')
axs[1].set_title('Cubes')

plt.show()