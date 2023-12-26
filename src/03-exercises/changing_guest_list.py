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
print(f"Hi {guest_list[1].title()}, {guest_list[0].title()} will be here, "
    f"{guest_list[2].title()} will be here, I deduct you will be here @9.00pm"\
    f"on Saturday!")
print(f"Hi {guest_list[2].title()}, change of plans, dinner will be served "\
    "@9.00pm!")