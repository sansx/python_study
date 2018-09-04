import csv
from matplotlib import pyplot as plt
from datetime import datetime
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))
# filename = './sitka_weather_2014.csv'
filename = './death_valley_2014.csv'

with open(filename) as f:
    render = csv.reader(f)

    header_row = next(render)

    dates, highs, lows = [],[],[]
    for row in render:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10,6))

plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3 )

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()