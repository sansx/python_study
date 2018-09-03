import csv
from matplotlib import pyplot as plt
from datetime import datetime
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))
filename = './sitka_weather_07-2014.csv'

with open(filename) as f:
    render = csv.reader(f)

    header_row = next(render)

    dates, highs = [],[]
    for row in render:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)


fig = plt.figure(dpi=128, figsize=(10,6))

plt.plot(dates, highs, c='red')

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()