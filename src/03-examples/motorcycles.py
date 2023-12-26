# change value of element at index 0
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# append element in the end
motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)

# create a list via appending
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert element at index 0 [LOWER_LIMIT]
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# insert element at index 1 [MIDDLE POSITION]
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)

# insert element in the end [UPPER LIMIT]
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(3, 'ducati')
print(motorcycles)

# insert element in the end [OFF THE UPPER LIMIT]
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(10, 'ducati')
print(motorcycles)

# insert element in the second to last place [MIDDLE POSITION]
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(-1, 'ducati')
print(motorcycles)

# insert element in the start [LOWER LIMIT]
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(-3, 'ducati')
print(motorcycles)

# insert element in the start [OFF THE LOWER LIMIT]
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(-10, 'ducati')
print(motorcycles)

# remove element based on index
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# remove the last element by popping
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# example of popping
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# remove element based on index by popping
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# remove element based on value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# example of removing
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")