# 7.10 Dream Vacation

responses = {}

polling_active = True

while polling_active:
    name = input("\n What is your name? ")
    response = input("If you could travel anywhere in the world, where would you go?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to travel to {response}.")

    