# valid alien colors: 'green', 'yellow', 'red'
alien_color = 'green'

if alien_color == 'green':
    points = 5
elif alien_color != 'green':
    points = 10
print(f"You just earned {points} points!")
print("-- end of the first version\n")

alien_color = 'red'

if alien_color == 'green':
    points = 5
elif alien_color != 'green':
    points = 10
print(f"You just earned {points} points!")
print("-- end of the second version\n")