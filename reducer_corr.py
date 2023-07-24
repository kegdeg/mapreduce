#! /usr/bin/env python3

import sys
import numpy as np

from collections import defaultdict


def pearson_correlation(x, y):
    """
    Calculates the Pearson correlation coefficient between two variables.

    Args:
        x: A list of numbers.
        y: A list of numbers.

    Returns:
        The Pearson correlation coefficient.
    """
    
    n = len(x)

   # if n == 0:
    #    raise ValueError("Input lists are empty. Cannot compute Pearson correlation.")


    x = [float(i) for i in x] 
    y = [float(i) for i in y]
    
    x_sq = [float(i**2) for i in x]
    y_sq = [float(i**2) for i in y]
    

    den_x = (sum(x_sq) - (sum(x) ** 2) / n)
    den_y = (sum(y_sq) - (sum(y) ** 2) / n)
    
    psum = sum(xi*yi for xi, yi in zip(x, y))
    num = psum - (float(sum(x)) * float(sum(y))/n)
    
    #den = ((sum(x_sq) - (sum_x ** 2) / n) * (sum(y_sq) - (sum_y ** 2) / n)) ** 0.5


    den = (den_x * den_y) ** 0.5


    if den == 0 or num == 0:
        return 0

    return num / den



#corr_matrix = {lambda: x for float(x)}
def correlation_matrix(data):
    
    """
    Calculates the correlation matrix for a data set.

    Args:
        data: A list of lists, where each inner list represents a variable.

    Returns:
        The correlation matrix.
    """

    n = len(data)
    corr = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if len(data[i]) == 0 or len(data[j]) == 0:
                corr[i, j] = 0  # If one of the variables has an empty dataset, set correlation to 0.
            else:
                corr[i, j] = pearson_correlation(data[i], data[j])
            #corr[i, j] = pearson_correlation(data[i], data[j])

    return corr


month_values = {
    "dry_bulb": [],
    "rel_humidity": [],
    "wind_speed": []
}


for line in sys.stdin:

    line = line.strip()

    try:
        month, dry_bulb, rel_humidity, wind_speed = line.split('\t')
    except ValueError:
        continue


    #if month not in month_values:
     #   month_values[month] = ([], [], [])

    month_values["dry_bulb"].append(float(dry_bulb))
    month_values["rel_humidity"].append(float(rel_humidity))
    month_values["wind_speed"].append(float(wind_speed))



variables = list(month_values.keys())
correlate = correlation_matrix(list(month_values.values()))

correlation_dict = {}

for i in range(len(variables)):
    correlation_dict[variables[i]] = {}
    for j in range(len(variables)):  
        correlation_dict[variables[i]][variables[j]] = correlate[i, j]

print(correlation_dict)





