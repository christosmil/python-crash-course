# use a while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print("-- end of the first example\n")

# use continue to return to the beginning of a loop
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
print("-- end of the second example\n")

# exit an infinite loop
x = 1
while x <= 5:
    print(x)
    # if I omit the following command, I will have an infinite loop
    x += 1
print("-- end of third example\n")