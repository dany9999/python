import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Generating_data/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row1 = next(reader) #get first file's row
    header_row2 = next(reader) #get second file's row

    #get dates and high temperatures from this file
    dates,highs = [], []

    #print(header_row1) 
    #print(header_row2)

    #get high temperatures from this file
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

#plot the high temperatures
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates, highs, c='red')

#format plot
plt.title("daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


