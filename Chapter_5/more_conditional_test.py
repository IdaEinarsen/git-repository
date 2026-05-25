# 5.2 More conditional test

# Tests for equality and inequality , two of them is true
# two of them is false

animals = "Dog"

print(animals == "Dog")      
print(animals != "Cat")        
print(animals == "Cat")        
print(animals != "Dog")      

# Using the lower() method

name = "Miley"

print(name.lower() == "miley")
print(name.lower() =="MILEY")

# Numerical tests

age = 20

print(age == 20)
print(age != 23)
print(age > 18)
print(age < 18)
print(age >= 20)
print(age <= 15)

# Using and/or (and is true , or is false)

print(age > 15 and age < 25)

print(age < 18 or age > 30)

# Testing list using in and not in method

sodas = ["coke", "fanta", "sprite"]

print(sodas)

print("coke" in sodas)
print("pepsi" in sodas)
print("fanta" in sodas)
print("7up" in sodas)

print("fanta" not in sodas)
print('zingo' not in sodas)

