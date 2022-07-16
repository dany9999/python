import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'Generating_data/CSV_visualization/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #get first file's row

    rainfalls, dates = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])
        dates.append(current_date)
        rainfalls.append(rainfall)

print(rainfalls)

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates, rainfalls, c='red', alpha=0.5)

plt.fill_between(dates,rainfalls, facecolor='blue', alpha=0.1) #shading an area between two data sets

plt.show() 