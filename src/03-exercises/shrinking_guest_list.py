guest_list = ['newton', 'euclid', 'aristarchus']
print(f"Hi {guest_list[0].title()}, can I interest you in an apple dinner?")
print(f"Hi {guest_list[1].title()}, this Saturday all the parallels lead to a"\
    " single point; dinner at my place!")
print(f"Hi {guest_list[2].title()}, tomorrow the model we follow is my-place-"\
    "centric; dinner @8:00pm with the guys!")

print(f"Awww, {guest_list[1].title()} can't make it!")

guest_list[1] = 'thales'

print(f"Hi {guest_list[0].title()}, apple dinner is still on, Saturday, "\
    "@9:00pm.")
print(f"Hi {guest_list[1].title()}, {guest_list[0].title()} will be here, "\
    f"{guest_list[2].title()} will be here, I deduct you will be here @9:00pm"\
    " on Saturday!")
print(f"Hi {guest_list[2].title()}, change of plans, dinner will be served "\
    "@9:00pm!")

print("Great! I found a bigger table, let's have some more wise guys!")

guest_list.insert(0, 'ray liotta')
guest_list.insert(2, 'robert de niro')
guest_list.append('joe pesci')

print(f"Hi {guest_list[0].title()}, let's have some dinner on Saturday "\
    "@8:30pm!")
print(f"Ok {guest_list[1].title()}, last change I swear, Saturday, @8:30pm.")
print(f"Hi {guest_list[2].title()}, dinner on Saturday @8:30!")
print(f"Hi {guest_list[3].title()}, small change of plans, Saturday @8:30pm.")
print(f"Hey {guest_list[4].title()}, eventually we'll have dinner @8:30pm.")
print(f"Hi {guest_list[5].title()}, Saturday @8:30pm we are all eating at my "\
    "place!")

print(f"Tough luck, table will arrive late, so only two friends for dinner!")

# I will remove guests 0, 2, 3, and 5.
# Be careful, each time I remove a guest, the list changes and guests may be
# shifted to the left.
miss_dinner = guest_list.pop(0)
print(f"Sorry {miss_dinner.title()}, I have to cancel the dinner invitation.")
miss_dinner = guest_list.pop(1)
print(f"Sorry {miss_dinner.title()}, I have to cancel the dinner invitation.")
miss_dinner = guest_list.pop(1)
print(f"Sorry {miss_dinner.title()}, I have to cancel the dinner invitation.")
miss_dinner = guest_list.pop()
print(f"Sorry {miss_dinner.title()}, I have to cancel the dinner invitation.")

print(f"{guest_list[0].title()}, we will only be you, me, and "\
    f"{guest_list[1].title()}.")
print(f"{guest_list[1].title()}, we will only be you, me, and "\
    f"{guest_list[0].title()}.")

del guest_list[0]
del guest_list[0]
print(guest_list)