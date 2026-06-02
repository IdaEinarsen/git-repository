# 10.14 Verify User

import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'

    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")

    filename = 'username.json'
    with open(filename, 'w') as file:
        json.dump(username, file)

    return username


def greet_user():
    """Greet the user."""
    username = get_stored_username()

    if username:
        correct = input(f"Is '{username}' your username? (yes/no) ")

        if correct.lower() == 'yes':
            print(f"Welcome back, {username}!")

    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()