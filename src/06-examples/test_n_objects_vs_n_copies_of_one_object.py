# A program to showacase the difference of creating a list with n
# different objects vs. a list with n copies of one object.

# n different objects
aliens = []
print(aliens)

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...\n")

aliens[1]['color'] = 'yellow'
aliens[1]['points'] = 10
aliens[1]['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print("...\n")

print("=== vs. ===\n")

# n copies of one object
aliens = []
print(aliens)

new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
for alien_number in range(30):
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...\n")

aliens[1]['color'] = 'yellow'
aliens[1]['points'] = 10
aliens[1]['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print("...\n")