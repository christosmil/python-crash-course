# Examples on ORGANIZING A LIST

#Example 1: sort ASC (by default)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Example 2: sort DESC
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Example 3: show sorted, but DO NOT sort original list
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse order sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list:")
print(cars)

# Example 4: reverse the orders of elements (NO SORTING)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
cars.reverse()
print(cars) # original list

# Example 5: find the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))