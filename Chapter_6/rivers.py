# 6.5 Rivers

favorite_rivers = {
    "nile": "egypt",
    "kenai": "alaska",
    "futaleufú": "chile"
}

for river, country in sorted(favorite_rivers.items()):
 print(f"The {river.title()} runs through {country.title()}")

 
print("\nRivers:")
for river in favorite_rivers.keys():
    print(river.title())

print("\nCountries:")
for country in favorite_rivers.values():
    print(country.title())