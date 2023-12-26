try:
    first_number = int(input("Please, type the first integer:  "))
    second_number = int(input("Please, type the second integer: "))
except ValueError:
    print("This is not an integer!")
else:
    res = first_number + second_number
    print(f"{first_number} + {second_number} = {res}")