import csv
import  matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DayLocator, DateFormatter
scale = 255

class Data:
    """获取数据"""
    def __init__(self,filename,index):
        self.filename = filename
        self.dates()
        self.index = index
        self.temperatures = self.temperatures(self.index)




    def dates(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            dates = []
            for row in reader:
                date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(date)
        return  dates
    def temperatures(self,index):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            temperatures = []
            for row in reader:
                try:
                    temperature = round((float(row[index]) - 32) * 5 / 9, 2)
                except ValueError:
                    print(f"wrong data{temperature}")
                else:
                    temperatures.append(temperature)
        return  temperatures

