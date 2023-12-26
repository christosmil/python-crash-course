# Assign strings to all prompts.
user_prompt = "\nHi, what's your name? "
vac_prompt = "If you could visit one place in the world, where would you go? "
continue_prompt = "Would you like to let another person respond? (yes/ no) "

# Initialize vacations dictionary.
vacations = {}

# Poll users for their favorite vacation, until prompted to quit.
polling_active = True
while polling_active:
    user = input(user_prompt)
    vacation = input(vac_prompt)

    # Add the user and its response to the dictionary.
    vacations[user] = vacation

    # Check if there is another user to be polled.
    polling = input(continue_prompt)
    if polling.lower() == 'no':
        polling_active = False

# Print the results of the poll.
print("\n--- Poll Results ---")
for user, vacation in vacations.items():
    print(f"{user.title()} would like to go to {vacation.title()}.")