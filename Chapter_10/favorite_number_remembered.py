# 10.12 Favorite Number Remembered 

# This program does the same as 10.11 but instead of having multiple programs this one does everything

import json

from pathlib import Path

path = Path(r'C:\Users\EinarsenIda\Desktop\projects\Chapter_10\favorite_number.json')


try:
    with path.open() as file:
        favorite_number = json.load(file)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")

    with path.open(filename, 'w') as file:
        json.dump(favorite_number, file)

    print("I'll remember your favorite number!")
else:
    print(f"I know your favorite number! It's {favorite_number}.")