# without list comprehension
odd_numbers = []
for number in range(1, 20, 2):
    odd_numbers.append(number)
for odd_number in odd_numbers:
    print(odd_number)

# alternatively
odd_numbers = list(range(1, 20, 2))
for odd_number in odd_numbers:
    print(odd_number)

# with list comprehension
odd_numbers = [number for number in range(1, 20, 2)]
for odd_number in odd_numbers:
    print(odd_number)