cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

print(f"The first three items in the list are: {cubes[:3]}.")
print(f"Three items in the middle of the list are: {cubes[3:6]}.")
print(f"The last three items in the list are: {cubes[-3:]}.")