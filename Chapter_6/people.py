# 6.7 People

person_1 = {
    "first_name": "Ida",
    "last_name": "Einarsen",
    "age": 30,
    "city": "¨Norberg"

}

person_2 = {
    "first_name": "Javier",
    "last_name": "Amaya",
    "age": 30,
    "city": "Halmstad"

}

person_3 = {
    "first_name": "Jennifer",
    "last_name": "Walker",
    "age": 25,
    "city": "Louisiana,USA"

}

people = [person_1, person_2, person_3]

for person in people:
    print("\nPerson information:")
    print(f"First name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")