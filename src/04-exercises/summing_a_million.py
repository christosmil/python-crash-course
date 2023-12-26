# without list comprehension
numbers = []
for number in range(1, 1_000_001):
    numbers.append(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# alternatively
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# with list comprehension
numbers = [number for number in range(1, 1_000_001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))