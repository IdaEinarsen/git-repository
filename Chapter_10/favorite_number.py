# 10.11 Favorite Number

import json

favorite_number = input("What is your favorite number? ")

# This program ask for an answer and save's the value on a new file by using json.dumps 

with open('favorite_number.json', 'w') as file:
    file.write(json.dumps(favorite_number)) 
