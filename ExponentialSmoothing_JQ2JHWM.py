#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 23:02:46 2021

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



fit0 = ExponentialSmoothing(series0, seasonal_periods=6, trend='mul', seasonal='add').fit()
series0.plot(color='black', legend=True, linewidth=2, label='actual JQ2J')
fit0.fittedvalues.plot(color='red')
fit0.forecast(12).plot(color='red', legend=True, label='HWM', linewidth=2, alpha=0.8)
plt.title('HWM Forecast for JQ2J')
plt.show()

fit1 = ExponentialSmoothing(series1, seasonal_periods=6, trend='add', seasonal='mul').fit()
series1.plot(color='black', legend=True, label='Ln(JQ2J)', linewidth=2)
fit1.fittedvalues.plot(color='red')
fit1.forecast(12).plot(color='red', legend=True, label='HWM')
plt.title('HWM Forecast for JQ2J (ln)')
plt.show()

fit2 = ExponentialSmoothing(series2, seasonal_periods=6, trend='mul', seasonal='add').fit()
series2.plot(color='black', legend=True, label='Sqrt(JQ2J)', linewidth=2)
fit2.fittedvalues.plot(color='red')
fcast2 = fit2.forecast(12)
fcast2.plot(color='red', legend=True, label='HWM', linewidth=2)

plt.show()


# Evaluating thr errors
from sklearn.metrics import mean_squared_error
MSE0 = mean_squared_error(fit0.fittedvalues, series0)
MSE1 = mean_squared_error(fit1.fittedvalues, series1)
MSE2 = mean_squared_error(fit2.fittedvalues, series2)

print('MSE0: %s' %MSE0)
print('MSE1: %s' %MSE1)
print('MSE2: %s' %MSE2)


print(len(fit2.fittedvalues))
for i in range(0, len(fit2.fittedvalues)):
    fit2.fittedvalues[i] = fit2.fittedvalues[i] ** 2
for i in range(0, len(fcast2)):
    fcast2[i] = fcast2[i] ** 2


fit2.fittedvalues.plot(label='HWM (Backtrans)', legend=True, color='blue')
series0.plot(label='Original JQ2J', legend=True, color='red')
fcast2.plot(color='red')
plt.title('HWM Forecast for Backtransformed JQ2J', fontsize=15)
plt.show()

from statsmodels.graphics.tsaplots import plot_acf

error0 = series0 - fit0.fittedvalues
error0.plot(legend=True)

error2 = series0 - fit2.fittedvalues
error2.plot()
plt.show()


plot_acf(error2,title='Residual Plot for HWM of Backtransfromed JQ2J', lags=100) 
plot_acf(error0, title='Residual Plot for HWM of Original JQ2J', lags=100)
    











