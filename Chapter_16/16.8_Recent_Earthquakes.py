from pathlib import Path
import json

import plotly.express as px

# -- Using another gejson --
path = Path('Chapter_16/all_month.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']


mags, lons, lats, titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    titles.append(eq_dict['properties']['title'])

print(mags[:10])
print(lons[:5])
print(lats[:5])

title = all_eq_data['metadata']['title']
# -- Added color --
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    title=title,
    hover_name=titles,
    color=mags,
)
fig.show()