# 9.15 Lottery Analysis

import random

lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   "A", "B", "C", "D", "E")

# din egen ticket
my_ticket = (3, "A", 7, "D")

attempts = 0

while True:
    attempts += 1

    winning_ticket = random.sample(lottery_numbers, 4)

    if tuple(winning_ticket) == my_ticket:
        break

print(f"It took {attempts} attempts for your ticket to win!")

