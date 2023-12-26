def make_sandwich(*args):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a sandwich with the following items:")
    for arg in args:
        print(f"- {arg}")

make_sandwich('cheddar', 'beef', 'ketchup')
make_sandwich('extra cheese')
make_sandwich('ham', 'bacon', 'cheddar', 'potato chips')