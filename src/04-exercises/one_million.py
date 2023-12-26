# without list comprehension
numbers = []
for number in range(1, 1_000_001):
    numbers.append(number)
for number in numbers:
    print(number)

# alternatively
numbers = list(range(1, 1_000_001))
for number in numbers:
    print(number)

# with list comprehension
numbers = [number for number in range(1, 1_000_001)]
for number in numbers:
    print(number)