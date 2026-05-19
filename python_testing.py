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





   