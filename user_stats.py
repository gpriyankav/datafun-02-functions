"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics as s

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]


# measures of central tendency (mean, median, mode, proportion)

Mean = s.mean(scores)
Median = s.median(scores)
Mode = s.mode(scores)
LowMedian = s.median_low(scores)
HighMedian = s.median_high(scores)
fmean = float(s.fmean(scores))

print(f"The mean score in Yoga Practice test: {Mean}")
print(f"The fast mean in Yoga Practice test: {fmean:.2f}")
print(f"The Low median score in Yoga Practice test: {LowMedian}")
print(f"The High median score in Yoga Practice test: {HighMedian}")
print(f"The median score in Yoga Practice test: {Median:.2f}")
print(f"The mode of Yoga Practice test:{Mode}")
print()
# measures of dispersion (range, variance, standard deviation)

StandardDeviation = s.stdev(scores)
Variance = s.variance(scores)
Populationstddev = s.pstdev(scores)
Populationvariance = s.pvariance(scores)

print(f"Yoga Practice test variance and population variance : {Variance:.3f}, {Populationvariance:.3f}")
print(f"The standard deviation and population standard deviation : {StandardDeviation:.3f} , {Populationstddev:.3f}")

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

#Using covariance from statistics module

Covariance = s.covariance(x_times,y_temps)

print('Covariance of time and temperature:',Covariance)

#Calculate strength of linear relationship between two variables
correlation_coefficient = s.correlation(x_times,y_temps)

print('Correlation between time and temp:', correlation_coefficient)

#Calculation of slope and intercept using linear regression
Slope,Intercept = s.linear_regression(x_times,y_temps)

print(f'Slope: {Slope:.3f}')
print(f'Intercept: {Intercept:.3f}')

#calculation of future temperature at Yoga Institute 
x_future = 13
y_future = Slope*x_future+Intercept

print(f'the future temperature at Yoga Center: {y_future:.4f}')

