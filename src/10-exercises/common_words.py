def count_words(file_name, word):
    """
    Counts the occurences of a speficic word in a file.
    The search is case-insensitive.
    """
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {file_name} does not exist.")
    else:
        word_occurences = contents.lower().count(word)
        print(f"'{word}' occurs about {word_occurences} times in {file_name}.")

file_names = ['scarlet_letter.txt', 'sherlock_holmes.txt', 'gatsby.txt']
word = 'the'
for file_name in file_names:
    count_words(file_name, word)