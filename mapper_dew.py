#! /usr/bin/env python3

import sys


for line in sys.stdin:

    # Split the line into columns
    columns = line.split(',')

    # Extract the relevant columns
    wban_number = columns[0]
    year_month_day = columns[1]
    
    # Check if dew_point is digit and can be converted to float
    try:
        dew_point = float(columns[9])
    except ValueError:
        # Skip this line if the dew_point can't be converted to float
        continue

    # Only yield records where the dew_point is a valid float
    if isinstance(dew_point, float):
        print(f'{year_month_day}\t{dew_point}')
        
