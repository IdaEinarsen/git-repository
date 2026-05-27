# 8.7 Album

def make_album(artist_name, album_name, songs=None):
    album = {"artist": artist_name, "album": album_name}
    if songs:
        album["songs"] = songs
    return album

musician_1 = make_album("Falling In Reverse", "Fashionably Late", songs= 12)
musician_2 = make_album("Alex Warren", "You'll Be Alright, Kid", songs= 21)
musician_3 = make_album("Carola", "På Egna Ben", songs= 13)

print(musician_1)
print(musician_2)
print(musician_3)
