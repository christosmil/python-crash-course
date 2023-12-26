sandwich_orders = [
    'pastrami', 'chicken', 'grilled cheese', 'tuna', 'pastrami', 'pastrami']
finished_sandwiches = []

# Remove all instances of pastrami.
run_out = 'pastrami'
if run_out in sandwich_orders:
    print(f"Sorry, we run out of {run_out}.\n")
    while run_out in sandwich_orders:
        sandwich_orders.remove(run_out)

while sandwich_orders:
    # Remove the first sandwich order.
    sandwich = sandwich_orders.pop(0)

    # Make the sandwitch.
    print(f"I made your {sandwich} sandwich.")

    # Add the finished sandwitch to the list of finished sanwitches.
    finished_sandwiches.append(sandwich)

# Print all the sandwitches that were made.
print("\nThe following sandwitches were made: ")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")