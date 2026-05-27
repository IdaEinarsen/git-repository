# 8.17 Styling Functions

# I used 8.8 user albums and i made it a little bit cleaner, following the styling functions

def make_album(artist_name, album_name, songs=None):
    """Create a dictionary containing album information."""

    album = {
        "artist": artist_name,
        "album": album_name,
    }

    if songs:
        album["songs"] = songs

    return album


while True:
    print("\nEnter the artist's name:")
    print("(Enter 'q' at any time to quit)")

    artist = input("Artist: ")

    if artist == "q":
        break

    album = input("Album: ")

    if album == "q":
        break

    result = make_album(artist, album)
    print(result)

# Using 8.12 sandwiches 

def make_sandwich(*toppings):
    """Print a summary of the sandwich toppings ordered."""

    print("\nMaking a sandwich with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")


make_sandwich("ham", "cheese")

make_sandwich("turkey", "lettuce", "tomato", "mayo")

make_sandwich(
    "cheese",
    "ham",
    "tomato",
    "red onion",
    "garlic sauce",
)

# using 8.2 

def favorite_book(title):
    """Display a message about a favorite book."""

    print(f"My favorite book is {title}.")


favorite_book("Percy Jackson and the Lightning Thief")

# I mostly added a docstring to them and cleaned them up a little bit ! 