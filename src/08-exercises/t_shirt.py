def make_shirt(size, text):
    """Display the size and the message of a shirt."""
    print(f"\nI made a {size.title()}-size shirt, with the message:\n{text}")

# Use positional arguments
make_shirt('medium', 'May the force be with you')

# Use keyword arguments
make_shirt(size='medium', text='May the force be with you')
make_shirt(text='May the force be with you', size='medium')