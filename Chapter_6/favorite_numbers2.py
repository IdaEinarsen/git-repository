# 6.10 Favorite Numbers

favorite_numbers = {
    "Malin": [6, 12],
    "Javier": [22, 8],
    "Ida": [7, 21],
    "Albin": [6, 8],
    "Cecilia": [9, 44]
}

for names, numbers in favorite_numbers.items():
     print(f"\n{names.title()}'s favorite numbers are:")

     for number in numbers:
         print(number)


# I had some trouble with this one, i put the for number in numbers: on the wrong place 
# so it only printed cecilia's favorite numbers. but i fixed it after a bit of struggle




