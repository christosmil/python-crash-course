def make_album(artist, title, songs=None):
    """Return a dictionary containing information about an album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\nTell me your favorite album's artist and title:")
    print("(Enter 'q' to quit at any time.)")

    artist = input("Enter the artist: ")
    if artist == 'q':
        break

    title = input("Enter the title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)