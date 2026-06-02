# 10.13 User Dictionary

import json

filename = 'user_info.json'

# User information
user_info = {
    'username': input("What is your username? "),
    'favorite_color': input("What is your favorite color? "),
    'favorite_number': input("What is your favorite number? "),
}

# Write's dictonary in a seperate file
with open(filename, 'w') as file:
    file.write(json.dumps(user_info))

# Read's dictionary back
with open(filename) as file:
    user_info = json.loads(file.read())

# Print the user information we got
print("\nHere's what I remember about you:")
print(f"Username: {user_info['username']}")
print(f"Favorite color: {user_info['favorite_color']}")
print(f"Favorite number: {user_info['favorite_number']}")