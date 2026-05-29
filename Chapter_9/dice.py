# 9.13 Dice

# By using import random , i import pythons random module to help
# giving random numbers for exp: Dices

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


# 6
print("6-sided die:")
die_6 = Die()

for roll in range(10):
    die_6.roll_die()


# 10
print("\n10-sided die:")
die_10 = Die(10)

for roll in range(10):
    die_10.roll_die()


# 20
print("\n20-sided die:")
die_20 = Die(20)

for roll in range(10):
    die_20.roll_die()