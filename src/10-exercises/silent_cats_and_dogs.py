def read_file(file_name):
    """Reads a file, and displays its contents. Fails silently."""
    try:
        with open(file_name) as f:
            contents = f.readlines()
    except FileNotFoundError:
        pass
    else:
        for content in contents:
            print(content.strip().title())

file_name = 'cats.txt'
read_file(file_name)

file_name = 'dogs.txt'
read_file(file_name)