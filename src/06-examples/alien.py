# a simple dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print("-- end of the first example\n")

# accessing values in a dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])
print("-- end of the second example\n")

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
print("-- end of the third example\n")

# add new key-value pairs to the dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("-- end of the fourth example\n")

# start with an empty dictionary
alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print("-- end of the fifth example\n")

# modifying values in a dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
print(f"-- end of the sixth example\n")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x-position: {alien_0['x_position']}")
print("-- end of the seventh example\n")

# removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
print("-- end of the eighth example\n")

# dictionary inside a list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("-- end of the ninth example\n")

# create a list with automatic generation of multiple dictionaries
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    # I have to define new alien, else I will have copies of the same
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...\n")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Change properties to the second alien
aliens[1]['color'] = 'yellow'
aliens[1]['points'] = 10
aliens[1]['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print("...\n")

# Change properties to the first three aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
print("...\n")