import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk of 5000 points.
rw = RandomWalk(5_000)
rw.fill_walk()

# Plot the random walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
ax.plot(rw.x_values, rw.y_values, c=(0.2, 0.7, 0.4), linewidth=2, zorder=1)

# Emphasize the first and last points.
ax.scatter(0, 0, c='blue', edgecolor='none', s=100, zorder=2)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100,
    zorder=2)

plt.show()