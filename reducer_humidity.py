#!/usr/bin/env python3

import sys
from collections import defaultdict

# Create dictionaries to accumulate values and square values for each day
lowest = defaultdict(lambda: float('inf'))
daily_values = defaultdict(list)

#print(daily_values)

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input we got from mapper.py
    line = line.strip()


    # Skip lines without the expected number of values
    try:
        year_month_day, rel_humidity = line.split('\t')
    except ValueError:
        continue

    #print(rel_humidity)

    try:
        rel_humidity = float(rel_humidity)
    except ValueError:
        # Skip this line if dew_point can't be converted to float
        continue

    #if year_month_day not in lowest:
    if rel_humidity < lowest[year_month_day]:
        lowest[year_month_day] = rel_humidity


    daily_values[year_month_day].append(rel_humidity)


# Calculate the mean and variance for each day
for day, values in daily_values.items():

    minimum = lowest[day]

    # Print the day, mean, and variance as tab-separated values
    print(f'{day}\t{minimum}')
