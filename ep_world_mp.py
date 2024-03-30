import  plotly.express as px
import  json
import  pandas as pd

filename = "data/eq_data_1_day_m1.json"

with open(filename) as f:
    all_ep_data = json.load(f)


readable_file = "data/readable_eq_data.json"
with open(readable_file,'w') as f:
    json.dump(all_ep_data,f,indent=4)

all_ep_dicks = all_ep_data['features']
print(len(all_ep_dicks))

mags,titles,lons,lats = [],[],[],[]
for ep_dicks in all_ep_dicks:
    mag = ep_dicks['properties']['mag']
    mags.append(mag)
    title = ep_dicks['properties']['title']
    lon = ep_dicks['geometry']['coordinates'][0]
    lat = ep_dicks['geometry']['coordinates'][1]
    titles.append(title)
    lons.append(lon)
    lats.append(lat)


data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['longitude','latitude','location','Magnitude']
)

fig = px.scatter(
    data,
    x='longitude',
    y='latitude',
    labels={'x':'longitude','y':'latitude'},
    range_x = [-200,200],
    range_y= [-90,90],
    width=800,
    height=800,
    title='Global earthquake scatter plot',
    size='Magnitude',
    size_max=10,
    color='Magnitude',
    hover_name='location',
)
fig.write_html('global_earrhquake.html')
fig.show()