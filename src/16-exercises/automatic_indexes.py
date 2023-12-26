import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Retrieve the column indexes of area, dates, highs, and lows.
    print(header_row)
    area_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows, = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # To get the area, use the last row, and remove from the name the state
    # and the country.
    area = row[area_index][:-7].title()

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15,9 ), dpi=128)
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title(f'{area} high and low temperatures - 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.set_ylim([20, 130])

# Remove spaces from area name, and use only small letters.
area = area.replace(' ', '_').lower()
plt.savefig(f'graphics/{area}_automatic.png', bbox_inches='tight')