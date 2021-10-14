#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 22:57:48 2021

@author: 32095422
"""

from pandas import read_excel
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt
series0 = read_excel('JQ2Jdata_32095422.xlsx', sheet_name='Data', header=0,
                    index_col=0, parse_dates=True, squeeze=True)
series1 = read_excel('JQ2Jdata_32095422.xlsx', sheet_name='Ln_Data', header=0,
                    index_col=0, parse_dates=True, squeeze=True)
series2 = read_excel('JQ2Jdata_32095422.xlsx', sheet_name='Sqrt_Data', header=0,
                    index_col=0, parse_dates=True, squeeze=True)

fit0 = ExponentialSmoothing(series0, seasonal_periods=12, trend='add', seasonal='add').fit()
series0.plot(color='black', alpha=0.8)
fit0.fittedvalues.plot(color='red', linewidth=2)
fit0.forecast(12).plot(color='red', linewidth=2)

plt.show()

fit1 = ExponentialSmoothing(series1, seasonal_periods=12, trend='add', seasonal='add').fit()
series1.plot(color='black', alpha=0.8, legend=True, label='Original Data', linewidth=2)
fit1.fittedvalues.plot(color='red', linewidth=2)
fit1.forecast(12).plot(color='red', linewidth=2, legend=True, label='HWA')

plt.show()

fit2 = ExponentialSmoothing(series2, seasonal_periods=12, trend='add', seasonal='add').fit()
series2.plot(color='black', alpha=0.8, legend=True, label='Original Data', linewidth=2)
fit2.fittedvalues.plot(color='red', linewidth=2)
fcast2 = fit2.forecast(12)
fcast2.plot(color='red', linewidth=2, legend=True, label='HWA')

plt.show()

# Evaluating yhr errors
from sklearn.metrics import mean_squared_error
MSE0 = mean_squared_error(fit0.fittedvalues, series0)
MSE1 = mean_squared_error(fit1.fittedvalues, series1)
MSE2 = mean_squared_error(fit2.fittedvalues, series2)
print('MSE0: %s' %MSE0)
print('MSE1: %s' %MSE1)
print('MSE2: %s' %MSE2)

for i in range(0, len(fit2.fittedvalues)):
    fit2.fittedvalues[i] = fit2.fittedvalues[i] ** 2
for i in range(0, len(fcast2)):
    fcast2[i] = fcast2[i] ** 2
    
from statsmodels.graphics.tsaplots import plot_acf
error = fit2.fittedvalues - series0
plot_acf(error, title='Residual Plot for HWA of backtransformed JQ2J', lags=100)
plt.show()

series0.plot(color='blue', label='Original JQ2J', legend=True)
fit2.fittedvalues.plot(color='red', label='HWA (Backtrans)', legend=True)
fcast2.plot(color='red')
plt.title('HWA Forecast for Backtransformed JQ2J')
plt.show()

















