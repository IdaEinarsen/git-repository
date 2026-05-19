print('This is where i test things in python')

# How to display each name as its own. + with a bigletter using .title()
magicians = ['houdini','mr.amazing','terrifico']
for magician in magicians:
    print(magician.title())

list_of_items = ['baseball','pen','shoe','car','bottle']
for item in list_of_items:
    print(f"{item.title()} is green")
    print(f"I would want the {item} to be red")
print("I guess green will have to work! ")

# Using the range() function 

for value in range (1, 5):
    print(value)

# How to use range function to get even numbers

even_numbers = list(range(2, 11, 2))
print(even_numbers)


numbers = list(range(1, 12, 1))
print(numbers)

# Square with range

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)


# simple statistics with digits

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


big_numbers = list(range(1, 100))
print(big_numbers)

#tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# If = Do code only IF some condition is true
#  Else do something else (you can also ad else if statements as elif)
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now singed up!")

elif age < 0:
    print("You don't exist")
else: 
    print("You most be 18+ to play this game")


name = input("Enter your gamertag: ")

if name == "":
    print("YOU DIDNT TYPE IT IN")
else:
    print(f"Hello {name}, lets slay some monster's.")


response = input("Would you like some water? (Yes/No): ")
if response == "Yes":
    print("Have some water")
else:
    print("DAMN YOU ")


#boolean true or false

for_sale = True

if for_sale:
    print("This item is for sale")
else: 
    print("This item is not for sale")