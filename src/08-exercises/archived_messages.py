def send_messages(messages, sent_messages):
    """
    Sends messages from a list.
    Moves the sent messages to the list sent_messages.
    """
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = ['Oh, hi Mark', 'To infinity and beyond', 'Good news everyone']
sent_messages = []
send_messages(messages[:], sent_messages)
print(f"\nList 'messages': {messages}")
print(f"List 'sent_messages': {sent_messages}")