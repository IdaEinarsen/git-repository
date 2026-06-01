# 10.4 Guest

from pathlib import Path

name = input("What is your name? ")

path = Path("guest.txt")
path.write_text(name)

print("Your name has been saved.")



# input() gets the guest's name, path("guest.txt") creates a path to the file while
# write_text(name) creates the file if it doesnt exists and names it.