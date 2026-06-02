# 10.11.1 Favorite Number


import json
from pathlib import Path

path = Path(r'C:\Users\EinarsenIda\Desktop\projects\Chapter_10\favorite_number.json')


# This program imports in the file using path and the load's the answer from json file by using json.load


with path.open() as file:
    favorite_number = json.load(file)

print(f"I know your favorite number! It's {favorite_number}.")