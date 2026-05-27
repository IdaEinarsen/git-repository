# 7.5 Movie Tickets

while True:
    ages = input("How old are you? (enter 'quit' to stop): ")

    if ages.lower() == "quit":
        break

    age = int(ages)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")