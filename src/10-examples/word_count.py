def count_words(file_name):
    """Count the approximate number of words in a file."""
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # Inform the user about the fail.
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} contains {num_words} words.")


def count_words_failing_silently(file_name):
    """Count the approximate number of words in a file."""
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # Fail silently.
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} contains {num_words} words.")


file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
    'little_women.txt']

# Inform the user about the fail.
for file_name in file_names:
    count_words(file_name)
print(f"-- end of the first example\n")

# Fail silently
for file_name in file_names:
    count_words_failing_silently(file_name)
print(f"-- end of the second example\n")