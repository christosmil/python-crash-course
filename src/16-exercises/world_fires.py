import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day_2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Retrieve the indexes for longitude, latitude, brightness, and dates.
    print(header_row)
    lons_index = header_row.index('longitude')
    lats_index = header_row.index('latitude')
    brts_index = header_row.index('brightness')
    dates_index = header_row.index('acq_date')

    # Get longitude, latitude, brightness, and dates from this file.
    lons, lats, brts, dates, hover_texts = [], [], [], [], []
    for row in reader:
        lon = float(row[lons_index])
        lat = float(row[lats_index])
        current_date = datetime.strptime(row[dates_index], '%Y-%m-%d')
        try:
            brt = float(row[brts_index])
        except ValueError:
            print(f"Missing data for ({lon}, {lat})")
        else:
            lons.append(lon)
            lats.append(lat)
            brts.append(brt)
            dates.append(current_date)
            hover_texts.append(f"{current_date.strftime('%d/%m/%y')} - {brt}")

# Define the time period.
dates = list(set(dates))
starting_period = dates[0].strftime('%d/%m/%Y')
ending_period = dates[-1].strftime('%d/%m/%Y')
time_period = f'{starting_period} - {ending_period}'

# Map the active fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brt/20 for brt in brts],
        'color': brts,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Brightness',},
    }
}]
my_layout = Layout(title=f"Globally Active Fires {time_period}")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global-active-fires.html')