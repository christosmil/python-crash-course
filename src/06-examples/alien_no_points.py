alien_0 = {'color': 'green', 'speed': 'slow'}
# the following code produces a KeyError
# print(alien_0['points'])

# instead use the get() method
point_value = alien_0.get('points', 'No point value asssigned.')
print(point_value)