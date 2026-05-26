# 6.9 Favorite places

favorite_places = {
    "ida": ["japan", "turkey", "halmstad"],
    "malin": ["turkey", "greece", "spain"],
    "tova": ["ukraina", "polen", "Schweiz"]

}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")

    for place in places:
        print(f"- {place.title()}")