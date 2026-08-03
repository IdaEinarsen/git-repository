import plotly.express as px

from die4 import Die

# Create three D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = [
    die_1.roll() + die_2.roll() + die_3.roll()
    for _ in range(1000)
]


max_result = (
    die_1.num_sides +
    die_2.num_sides +
    die_3.num_sides
)

poss_results = range(3, max_result + 1)

frequencies = [results.count(value) for value in poss_results]


# Visualize the results.
title = "Results of Rolling Three D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency"}

fig = px.bar(
    x=poss_results,
    y=frequencies,
    title=title,
    labels=labels
)

fig.show()

print(frequencies)