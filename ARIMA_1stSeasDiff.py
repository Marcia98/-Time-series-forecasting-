#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:47:27 2021

@author: 32095422
"""

## removing seasonality from time series using seasonal differencing
from pandas import read_excel
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

series = read_excel('K54Ddata_32095422.xlsx', sheet_name='Data', usecols=[1],
                    header=0, squeeze=True, dtype=float)

# Seasonal difference
X = series.values
SeasDiff = list()
for i in range(12, len(X)):
    value = X[i] - X[i - 12]
    SeasDiff.append(value)
    
# Time, ACF, and PACF plot for the seasonally differenced series
plt.plot(SeasDiff)
plt.title('Time plot of seasonally differenced series')
plot_acf(SeasDiff, title='ACF plot of seasonally differenced series', lags=50)
plot_pacf(SeasDiff, title='PACF plot of seasonally differenced series', lags=50)
plt.show()


# Seasonal + Dirst difference
Y = SeasDiff
SeasFirstDiff = list()
for i in range(1, len(Y)):
    value = Y[i] - Y[i - 1]
    SeasFirstDiff.append(value)
plt.plot(SeasFirstDiff)
plt.title('Time plot seasonally + first differenced series')
plot_acf(SeasFirstDiff, title='ACF plot of seasonally + first differenced series', lags=50)
plot_pacf(SeasFirstDiff, title='PACF plot of seaonally + first differenced series', lags=50)
plt.show()








