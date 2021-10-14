#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:39:57 2021

@author: 32095422
"""

from pandas import read_excel
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

series = read_excel('K54Ddata_32095422.xlsx', sheet_name='Data', usecols = [1],
                    header=0, squeeze=True, dtype=float)

X = series.values
diff = list()
for i in range(1, len(X)):
    value = X[i] - X[i-1]
    diff.append(value)
plt.plot(diff)
plt.title('Time plot K54D 1st difference')

# ACF plot of time series
plot_acf(diff, title='ACF of K54D 1st difference', lags=50)

# PACF plot of time series
plot_pacf(diff, title='PACF of K54D 1st difference', lags=50)
plt.show()    