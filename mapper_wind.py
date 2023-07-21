#! /usr/bin/env python3

import sys


for line in sys.stdin:

    # Split the line into columns
    columns = line.split(',')

    # Extract the relevant columns
    year_month_day = columns[1]
    
    # Check if dew_point is digit and can be converted to float
    try:
        wind_speed = float(columns[12])
    except ValueError:
        # Skip this line if the dew_point can't be converted to float
        continue

    # Only yield records where the dew_point is a valid float
    if isinstance(wind_speed, float):
        print(f'{year_month_day}\t{wind_speed}')
        
