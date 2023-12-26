# without list comprehension
threes = []
for number in range(3, 31, 3):
    threes.append(number)
for three in threes:
    print(three)

# alternatively
three = list(range(3, 31, 3))
for three in threes:
    print(three)

# with list comprehension
threes = [number for number in range(3, 31, 3)]
for three in threes:
    print(three)