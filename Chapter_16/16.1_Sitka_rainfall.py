from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('Chapter_16/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index("DATE")
prcp_index = header_row.index("PRCP")

dates = []
rainfall = []

for row in reader:
    dates.append(row[date_index])
    rainfall.append(float(row[prcp_index]))

plt.figure(figsize=(10, 6))
plt.plot(dates, rainfall)

plt.title("Daily Rainfall - Sitka, 2021")
plt.xlabel("Date")
plt.ylabel("Rainfall (inches)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()