import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Values", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Set the range for the axes.
ax.axis([0, 5100, 0, 5100**3])

plt.show()