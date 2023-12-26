# slice a list starting from index 0
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print("-- end of the first example\n")

# slice a list starting from any index other index
print(players[1:4])
print("-- end of the second example\n")

# omitting first index results in slicing from the start of the list
print(players[:4])
print("-- end of the third example\n")

# omitting second index result in slicing to the end of the list
print(players[2:])
print("-- end of the fourth example\n")

# to print the last X elements use -X as the first index and omit the
# second
print(players[-3:])
print("-- end of the fifth example\n")

# use third index as a step
print(players[::2]) # print every element in even index
print(players[1::2]) # print every element in odd index
print("-- end of the sixth example\n")

# combine sorted and slicing to get the two first names
print(sorted(players, reverse=True)[-2:])
# the next line does the same but in ascending order
print(sorted(players)[:2])