#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:05:25 2021

@author: 32095422
"""

from pandas import read_excel
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt

series1 = read_excel('K54Ddata_32095422.xlsx', sheet_name='Data', header=0,
                         index_col=0, parse_dates=True, squeeze=True)
series2 = read_excel('K54Ddata_32095422.xlsx', sheet_name='Sqrt_Data', header=0,
                        index_col=0, parse_dates=True, squeeze=True)
series3 = read_excel('K54Ddata_32095422.xlsx', sheet_name='Ln_Data', header=0,
                         index_col=0, parse_dates=True, squeeze=True)


# HoltWinter model #
fit1 = ExponentialSmoothing(series1, seasonal_periods=12, trend='add', seasonal='mul').fit()
fcast1 = fit1.forecast(12).rename('HWM of orginal data: K54D')
series1.plot(color='blue', legend=True)
fit1.fittedvalues.plot(color='red')
fcast1.plot(color='red', legend=True)
plt.show()

fit2 = ExponentialSmoothing(series2, seasonal_periods=12, trend='add', seasonal='mul').fit()
fcast2 = fit2.forecast(12).rename('HWM of ln data: K54D')
series2.plot(color='black', legend=True)
fit2.fittedvalues.plot(color='red')
fcast2.plot(color='red', legend=True)
plt.show()

fit3 = ExponentialSmoothing(series3, seasonal_periods=12, trend='add', seasonal='mul').fit()
fcast3 = fit3.forecast(12).rename('Model3: HWM of sqrt data: K54D')
series3.plot(color='black', legend=True)
fit3.fittedvalues.plot(color='red')
fcast3.plot(color='red', legend=True)
plt.show()

# Evaluating the errors
from sklearn.metrics import mean_squared_error
MSE1 = mean_squared_error(fit1.fittedvalues, series1)
MSE2 = mean_squared_error(fit2.fittedvalues, series2)
MSE3 = mean_squared_error(fit3.fittedvalues, series3)

print(MSE1)
print(MSE2)
print(MSE3)


for i in range(0, len(fit2.fittedvalues)):
    fit2.fittedvalues[i] = fit2.fittedvalues[i] ** 2
for i in range(0, len(fcast2)):
    fcast2[i] = fcast2[i] ** 2

fit2.fittedvalues.plot(color='red', legend=True, label='HWM (Backtrans)')
series1.plot(color='blue', legend=True, label='Original K54D')
fcast2.plot(color='red')
plt.title('HWM Forecast for K54D (Backtrans)', fontsize=12)
plt.show()


error_Sqrt = series1 - fit2.fittedvalues 
error_Sqrt.plot()
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(error_Sqrt, title='Residual ACF for HWM of Backtranformed K54D', lags=100)
plt.show()

















