# 6.6 Polling

favorite_languages = {
 'tina': 'python',
 'tommy': 'c',
 'edwin': 'rust',
 'erika': 'python',
 }

people = ["tina", "tommy", "lisa", "edwin", "carina", "erika", "jesus"]

for person in people:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}")
    else:
        print(f"{person.title()}, please take the poll.")

