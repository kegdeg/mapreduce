#!/usr/bin/env python3

import sys
from collections import defaultdict

# Create dictionaries to accumulate values and square values for each day
daily_values = defaultdict(list)
daily_values_sq = defaultdict(list)

#print(daily_values)

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input we got from mapper.py
    line = line.strip()

    #print(line)

    #print(line.split('\t'))

    #year = line.split('\t')
    #print(dict(year))
    
    #year = dict(year)

    # Skip lines without the expected number of values
    try:
        year_month_day, dew_point = line.split('\t')
    except ValueError:
        continue

    #print(year_month_day)

    # Convert dew_point (currently a string) to float
    try:
        dew_point = float(dew_point)
    except ValueError:
        # Skip this line if dew_point can't be converted to float
        continue

    daily_values[year_month_day].append(dew_point)
    daily_values_sq[year_month_day].append(dew_point**2)

    #print(daily_values)


# Calculate the mean and variance for each day
for day, values in daily_values.items():
    mean = sum(values) / len(values)
    mean_of_squares = sum(daily_values_sq[day]) / len(daily_values_sq[day])
    variance = mean_of_squares - mean**2  # Variance = mean of squares - square of mean

    # Print the day, mean, and variance as tab-separated values
    print(f'{day}\t{mean}\t{variance}')
