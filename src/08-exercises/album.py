def make_album(artist, title, songs=None):
    """Return a dictionary containing information about an album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('linkin park', 'hybrid theory')
print(album)

album = make_album('iron maiden', 'fear of the dark')
print(album)

album = make_album('muse', 'origin of symmetry', 4)
print(album)