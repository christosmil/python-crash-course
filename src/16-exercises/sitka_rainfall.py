import csv
from datetime import datetime

from matplotlib import pyplot as plt

def get_rainfall_data(filename, dates, rainfalls):
    """Get the rainfall amounts from a data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and rainfall amounts from this file.
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                rainfall = float(row[3])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                rainfalls.append(rainfall)

# Get rainfall data for Sitka.
filename = 'data/sitka_weather_2018_simple.csv'
sitka_dates, sitka_rainfalls = [], []
get_rainfall_data(filename, sitka_dates, sitka_rainfalls)

# Get rainfall data for Death Valley.
filename = 'data/death_valley_2018_simple.csv'
dv_dates, dv_rainfalls = [], []
get_rainfall_data(filename, dv_dates, dv_rainfalls)

# Plot the rainfall amounts.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_rainfalls, c=(0.6, 0.8, 1), label='Sitka, AK')
ax.plot(dv_dates, dv_rainfalls, c=(0.8, 0.8, 0.4), label='Death Valley, CA')

# Format plot.
title = '2018 Rainfall comparison\nSitka, AK vs. Death Valley, CA'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall (in)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.legend(loc='upper right', fontsize=14)

plt.show()