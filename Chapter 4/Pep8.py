# 4.14 PEP 8 and 4.15 Code Review

# I used 4.1 and as what i can see it comply's to PEP 8 rules.
animals = ["dog", "cat", "bunny"]

message = "All these animals have fur and are pets."

for animal in animals:
    print(f"{animal.title()} is a great pet")

print(message)

# I used 4.4 and changed so i use underscore in the large number
# and comment spacing 

numbers = list(range(1, 1_000_001))

print(numbers)

# 4.5 Summing a Million
# Using the list from 4.4

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# I changed the list so it would be less then 80 characters
#  i also did some spacing bewtween the for loop's
#to make it look cleaner.

type_pizza = [
    "hawaii",
    "hakis",
    "kebab",
    "vesuvio",
    "romeo",
    "margarita",
    "chicago",
    "milano",
    "alfungi",
]

print("The first three items in the list are:")

for pizza in type_pizza[:3]:
    print(pizza.title())

print("Three items from the middle of the list are:")

for pizza in type_pizza[3:6]:
    print(pizza.title())

print("The last three items in the list are:")

for pizza in type_pizza[6:]:
    print(pizza.title())