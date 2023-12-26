import matplotlib.pyplot as plt

from mod_random_walk import RandomWalk

# Make a random walk of 5000 points.
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the random walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=64)
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    edgecolor='none', s=15)

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolor='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

# Remove the axes.
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)

plt.show()