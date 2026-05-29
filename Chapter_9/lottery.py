# 9.14 Lottery

import random

lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   "A", "B", "C", "D", "E")

winning_ticket = random.sample(lottery_numbers, 4)

print("Any ticket matching these 4 numbers or letters wins a prize:")

for item in winning_ticket:
    print(item)
