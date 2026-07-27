import plotly.express as px

from die3 import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls.
results = []

for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []

poss_results = [
    1, 2, 3, 4, 5, 6,
    8, 9, 10, 12,
    15, 16, 18, 20,
    24, 25, 30, 36
]

for value in poss_results:
    frequencies.append(results.count(value))

# Visualize the results.
title = "Results of Multiplying Two D6 Dice 1,000 Times"
labels = {"x": "Product", "y": "Frequency"}

fig = px.bar(
    x=poss_results,
    y=frequencies,
    title=title,
    labels=labels
)

fig.show()

print(frequencies)