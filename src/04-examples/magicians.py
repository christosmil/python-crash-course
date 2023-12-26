# print every element of a list via a loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print("-- end of first example")

# print the same personalized message for every element of a list via a
# loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print("-- end of second example")

# include two commands in the for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("-- end of third example")

# execute a command after the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait for your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
print("-- end of fourth example")