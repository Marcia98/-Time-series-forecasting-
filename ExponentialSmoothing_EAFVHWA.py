#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:51:04 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing

series1 = read_excel('EAFVdata_32095422.xlsx', sheet_name='Data', header=0, 
                     index_col=0, parse_dates=True, squeeze=True)

series3 = read_excel('EAFVdata_32095422.xlsx', sheet_name='Ln_OrigData', header=0, 
                     index_col=0, parse_dates=True, squeeze=True)

series4 = read_excel('EAFVdata_32095422.xlsx', sheet_name='Sqrt_OrigData', header=0, 
                     index_col=0, parse_dates=True, squeeze=True)

# HWA Model #
fit1 = ExponentialSmoothing(series1, seasonal_periods=12, seasonal='add', trend='add').fit()
series1.plot(color='blue', label='Orginal EAFV', legend=True)
fit1.fittedvalues.plot(color='red', label='HWA', legend=True)
fcast1 = fit1.forecast(12)
fcast1.plot(color='red')
plt.title('HWA Forecasting of EAFV')
plt.show()


fit3 = ExponentialSmoothing(series3, seasonal_periods=12, seasonal='add', trend='add').fit()
fit3.fittedvalues.plot()
fcast3 = fit3.forecast(12)
fcast3.plot()
series3.plot()
plt.show()

fit4 = ExponentialSmoothing(series4, seasonal_periods=12, seasonal='add', trend='add').fit()
fit4.fittedvalues.plot()
fcast4 = fit4.forecast(12)
fcast4.plot()
series4.plot()
plt.show()

# Evaluating the errors
from sklearn.metrics import mean_squared_error
MSE1 = mean_squared_error(fit1.fittedvalues, series1)
MSE3 = mean_squared_error(fit3.fittedvalues, series3)
MSE4 = mean_squared_error(fit4.fittedvalues, series4)


print('MSE1 (original  EAFV (1988-2020): %s' %MSE1)
print('MSE3 Ln(EAFV) (1988-2020): %s' %MSE3)
print('MSE4 Sqrt(EAFV) (2004-2020): %s' %MSE4)



for i in range(0, len(fit4.fittedvalues)):
    fit4.fittedvalues[i] = fit4.fittedvalues[i] ** 2
for i in range(0, len(fcast4)):
    fcast4[i] = fcast4[i] ** 2
    
error_sqrt = fit4.fittedvalues - series1

from statsmodels.graphics.tsaplots import plot_acf
plot_acf(error_sqrt, title='Residual ACF for HWA of Backtransformed EAFV', lags=100)

error_orig = fit1.fittedvalues - series1

plot_acf(error_orig, title='Residual ACF for HWA of EAFV', lags=100)
plt.show()

error_sqrt.plot(title='Residual Plot for HWA of backtransformed EAFV')
plt.show()

error_orig.plot(title='Residual Plot for HWA of EAFV')
plt.show()


series1.plot(color='blue', label='Original EAFV', legend=True)
fit4.fittedvalues.plot(color='red', label='HWA (Backtrans)', legend=True)
fcast4.plot(color='red')
plt.title('HWA Forecast for Backtransformed EAFV')
plt.show()
