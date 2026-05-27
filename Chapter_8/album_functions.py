# 8.16 Imports

def make_album(artist_name, album_name, songs=None):
    album = {
        "artist": artist_name,
        "album": album_name
    }

    if songs:
        album["songs"] = songs

    return album
