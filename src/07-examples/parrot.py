# receive user input
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
print("-- end of the first example\n")

# receive user input, until the user quits
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
print("-- end of the second example\n")

# use a flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit  to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
print("-- end of the third example\n")
