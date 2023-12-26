current_users = ['admin', 'Alice', 'Bob', 'jAdEn', 'Trudy']

# without list comprehension
c_u_case_insensitive = []
for current_user in current_users:
    c_u_case_insensitive.append(current_user.lower())

# with list comprehension
c_u_case_insensitive = [current_user.lower() for current_user in current_users]

new_users = ['TruDY', 'Eve', 'Mallory', 'Sybil', 'Jaden']

for new_user in new_users:
    if new_user.lower() in c_u_case_insensitive:
        print(f"Enter a new username.")
    else:
        print(f"{new_user} is available!")