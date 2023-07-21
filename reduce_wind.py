#!/usr/bin/env python3

import sys
from collections import defaultdict

# Create dictionaries to accumulate values and square values for each day

daily_values = defaultdict(list)
lowest = defaultdict(lambda: float('inf'))
highest = defaultdict(lambda: float(0))  
difference = defaultdict(lambda: float(0))

#print(daily_values)

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input we got from mapper.py
    line = line.strip()


    # Skip lines without the expected number of values
    try:
        day, wind_speed = line.split('\t')
    except ValueError:
        continue


    try:
        wind_speed = float(wind_speed)
    except ValueError:
        # Skip this line if dew_point can't be converted to float
        continue


    #Find Minimum:
    #if day not in lowest:
    if wind_speed < lowest[day]:
        lowest[day] = wind_speed

    #Find Maximum
    #if day not in highest:
    if wind_speed > highest[day]:
        highest[day] = wind_speed


    

for day in lowest.keys():

    difference[day] = highest[day] - lowest[day]

    #daily_values[day].append(wind_speed)


# Calculate the mean and variance for each day
for day, difference in difference.items():

    #Prove
    minimum = lowest[day]
    maximum = highest[day]


    # Print the day, mean, and variance as tab-separated values
    print(f'{day}\t{difference}')
