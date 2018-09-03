import csv
from matplotlib import pyplot as plt
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))
filename = './sitka_weather_07-2014.csv'

with open(filename) as f:
    render = csv.reader(f)

    header_row = next(render)

    highs = []
    for row in render:
        high = int(row[1])
        highs.append(high)


fig = plt.figure(dpi=128, figsize=(10,6))

plt.plot(highs, c='red')

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()