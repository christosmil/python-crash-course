numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ending = 'st'
    elif number == 2:
        ending = 'nd'
    elif number == 3:
        ending = 'rd'
    else:
        ending = 'th'
    print(f"{number}{ending}")