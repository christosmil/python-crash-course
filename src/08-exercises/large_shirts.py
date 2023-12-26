def make_shirt(size='large', text='I love Python'):
    """
    Display the size and the message of a shirt. Both parameters take
    default values.
    """
    print(f"\nI made a {size.title()}-size shirt, with the message:\n{text}")

# Large-size shirt with default message.
make_shirt()
make_shirt(size='large')
make_shirt('large')

# Medium-size shirt with default message.
make_shirt(size='medium')
make_shirt('medium')

# Shirt of any size with a different message
#  Use the default size value
make_shirt(text='I am Groot')
#  Use positional arguments.
make_shirt('small', 'I am Groot')
#  Use keyword arguments.
make_shirt(size='small', text='I am Groot')
make_shirt(text='I am Groot', size='small')