# ask user for input
name = input("Please enter your name: ")
print(f"Hello, {name}!")
print("-- end of the first example\n")

# display long prompt message
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name}!")
print("-- end of the second example\n")