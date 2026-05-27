# 8.8 User Albums

def make_album(artist_name, album_name, songs=None):
    album = {"artist": artist_name, "album": album_name}
 
    return album

while True:
    print("\nEnter the artist's name:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == "q":
        break

    album = input("Album: ")
    if album == "q":
        break

    result = make_album(artist, album)
    print(result)



