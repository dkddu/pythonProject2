import csv
import  matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DayLocator, DateFormatter
from get_date import Data
scale = 255
filename = 'data/sitka_weather_2018_simple.csv'
def get_index(filename,head_name):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index,column in enumerate(header_row):
            if column==head_name:
                return index
index_high = get_index(filename,"TMAX")
index_low = get_index(filename,"TMIN")
sitka_weather_high = Data(filename,index_high)
sitka_weather_low = Data(filename,index_low)
dates = sitka_weather_low.dates()
highs = sitka_weather_high.temperatures
lows = sitka_weather_low.temperatures


plt.style.use('seaborn')
fig, ax = plt.subplots()
c = (255, 69, 0)
a= (0/scale, 191/scale, 255/scale)
# Convert RGB values to floats in the range [0, 1]
c_float = (c[0] / 255, c[1] / 255, c[2] / 255)
ax.plot(dates,highs,c=c_float,alpha=0.5)
ax.plot(dates, lows, c='green',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor=a,alpha=1)
ax.set_title(f"{filename} temperature in  2018", fontsize=24)
ax.set_ylabel("data", fontsize=16)
fig.autofmt_xdate()
ax.tick_params(axis='x', labelrotation=45)  # 将日期旋转45度以避免重叠
ax.set_xlabel("temperature(c)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=10)
plt.show()