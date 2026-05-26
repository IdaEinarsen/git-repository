# 6.8 Pets

pet_1 = {
    "animal": "dog",
    "name": "Bruno",
    "owner": "Lucas"
}

pet_2 = {
    "animal": "cat",
    "name": "Dotty",
    "owner": "Ritva"
}

pet_3 = {
    "animal": "bunny",
    "name": "Stampe",
    "owner": "Albin"
}

pets = [ pet_1, pet_2, pet_3]

for pet in pets:
    print("\nPet information:")
    print(f"Animal: {pet['animal'].title()}")
    print(f"Name: {pet['name'].title()}")
    print(f"Owner: {pet['owner'].title()}")
