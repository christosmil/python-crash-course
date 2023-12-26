# copy a list to a new list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# The following commented command does not work as intended
# friend_foods = my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("-- end of the first example\n")

# prove that the copy work as intended
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("-- end of the second example\n")