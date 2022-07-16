import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

# explore the structure of the data

filename = 'Generating_data/JSON_visualization/data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'Generating_data/JSON_visualization/data/eq_data_1_day_m1.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']


mags, lons, lats, hover_texts = [], [], [], []


for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'] [0]
    lat = eq_dict['geometry']['coordinates'] [1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(eq_dict['properties']['title'])

#map the earthquakes

#data = [Scattergeo(lon=lons, lat=lats)]

#different way of specifying chart data
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [5*mag for mag in mags], #imposto la grandezza dei marker in base alla magnitudo
        'color' : mags,
        'colorscale' : 'Electric',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'} 
    },

}]

#colorscale options

""" for key in colors.PLOTLY_SCALES.keys():
    print(key) """





my_layout = Layout(title=title)

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_earthquakes.html')
