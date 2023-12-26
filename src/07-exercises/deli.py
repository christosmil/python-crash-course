sandwich_orders = ['pastrami', 'grilled cheese', 'chicken', 'tuna']
finished_sandwiches = []

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