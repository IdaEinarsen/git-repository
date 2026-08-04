from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Chapter_16/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


date_index = header_row.index('DATE')
tmax_index = header_row.index('TMAX')
tmin_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

dates, highs, lows = [], [], []

for row in reader:
    try:
        current_date = datetime.strptime(
            row[date_index], '%Y-%m-%d'
        )
        high = int(row[tmax_index])
        low = int(row[tmin_index])
    except ValueError:
        print(f"Missing data for {row[date_index]}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

station_name = row[name_index]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = f"Daily High and Low Temperatures, 2021\n{station_name}"
ax.set_title(title, fontsize=20)

plt.show()