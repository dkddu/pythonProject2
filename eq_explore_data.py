import json

#探索数据结构
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
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])