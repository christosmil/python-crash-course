dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Please follow me, your table is ready!")