import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Generating_data/CSV_visualization/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #get first file's row


    #get dates and high temperatures from this file
    dates,highs, lows = [], [], []

    #print(header_row1) 
    #print(header_row2)

    #get high temperatures from this file
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row [6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#plot the high and low temperatures
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #shading an area between two data sets

#format plot
plt.title("daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


