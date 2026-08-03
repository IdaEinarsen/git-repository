from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# -------------------------
# Sitka
# -------------------------
path = Path('Chapter_16/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, header in enumerate(header_row):
    print(index, header)

sitka_dates, sitka_highs = [], []

for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[7])
    except ValueError:
        print(f"Missing data for {row[2]}")
    else:
        sitka_dates.append(current_date)
        sitka_highs.append(high)

# -------------------------
# Death Valley
# -------------------------
path = Path('Chapter_16/death_valley_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, header in enumerate(header_row):
    print(index, header)

dv_dates, dv_highs = [], []

for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[6])
    except ValueError:
        print(f"Missing data for {row[2]}")
    else:
        dv_dates.append(current_date)
        dv_highs.append(high)

# -------------------------
# Plot both locations
# -------------------------
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    sitka_dates,
    sitka_highs,
    color='blue',
    alpha=0.7,
    label='Sitka'
)

ax.plot(
    dv_dates,
    dv_highs,
    color='red',
    alpha=0.7,
    label='Death Valley'
)

ax.set_title(
    "Daily High Temperatures, 2021\nSitka vs Death Valley",
    fontsize=24
)

ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)

# Same scale for comparison
ax.set_ylim(0, 130)

ax.legend()
fig.autofmt_xdate()
ax.tick_params(labelsize=16)

plt.show()