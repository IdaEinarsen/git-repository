# 5.10 Checking Usernames

current_users = ["Admin", "Yoshi", "Jayryan", "Spaceboy", "Zakurii"]

new_users = ["tomtom", "yoshi","benito","billybob","spaceboy"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user} is already taken.")
    else:
        print(f"The username '{new_user}'is available.")



