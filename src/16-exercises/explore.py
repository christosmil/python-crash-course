import csv
from datetime import datetime

import matplotlib.pyplot as plt

YEAR = 2022
filename = f'data/athens-{YEAR}-simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Retrieve the column indexes of dates, rainfalls, snows, highs, and lows.
    print(header_row)
    date_index = header_row.index('DATE')
    rainfall_index = header_row.index('PRCP')
    snow_index = header_row.index('SNWD')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = float(row[high_index])
            low = float(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title(f'Athens, GR high and low temperatures - {YEAR}', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (oC)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.set_ylim([-10, 50])

plt.savefig(f'graphics/athens-temperatures-{YEAR}.png', bbox_inches='tight')