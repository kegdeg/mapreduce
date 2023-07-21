#! /usr/bin/env python3

import sys


for line in sys.stdin:

    # Split the line into columns
    columns = line.split(',')

    # Extract the relevant column
    day = columns[1]

    #Relative humidty, wind speed, dry bulb

    try:
        dry_bulb = float(columns[8])
        rel_humidity = float(columns[11])
        wind_speed = float(columns[12])

    except ValueError:
        continue

    #print(f'{day}\t{dew_point}\t{dry_bulb}\t{wind_speed}')

    # Only yield records where the dew_point is a valid float
    if isinstance(rel_humidity, float):
        if isinstance(dry_bulb, float):
            if isinstance(wind_speed, float):
                print(f'{day}\t{rel_humidity}\t{dry_bulb}\t{wind_speed}')
        
