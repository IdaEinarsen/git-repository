from pathlib import Path
import csv
import plotly.express as px

path = Path("Chapter_16/world_fires_1_day.csv")

lines = path.read_text().splitlines()
reader = csv.DictReader(lines)

lats, lons, brightness = [], [], []

for row in reader:
    lats.append(float(row['latitude']))
    lons.append(float(row['longitude']))
    brightness.append(float(row['brightness']))

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    color=brightness,
    size=brightness,
    title='World Fires (Past Day)',
)

fig.show()