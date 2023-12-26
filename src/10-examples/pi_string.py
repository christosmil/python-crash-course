file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print("-- end of the first example\n")

# Open the file that contains pi to 1_000_000 decimal places.
file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
print("-- end of the second example\n")

# Check if my birthday appears in the first million digits of pi.
birthday = input('Enter your birthday in the form mmddyy: ')
if birthday in pi_string:
    print("Your birthday appears in first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")