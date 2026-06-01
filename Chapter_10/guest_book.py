# 10.5 Guest Book

from pathlib import Path

path = Path("guest_book.txt")

# using while loop to ask for guest's names

while True:
    name = input("Please enter your name (or 'quit' to quit): ")

    if name.lower() == "quit":
        break

# a = append mode is used so that the name is added to the file and 
# doesn't overwrite the existing names.    
    with open(path, "a") as file:
        file.write(name + "\n")



