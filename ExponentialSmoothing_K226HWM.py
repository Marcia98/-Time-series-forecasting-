#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:36:18 2021

@author: 32095422
"""
from pandas import read_excel
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt
series1 = read_excel('K226data_32095422.xlsx', sheet_name='Data', header=0,
                     index_col=0, parse_dates=True, squeeze=True)
series2 = read_excel('K226data_32095422.xlsx', sheet_name='Truncated_Data', header=0,
                     index_col=0, parse_dates=True, squeeze=True)


# Model 1: 1997 - 2020
fit1 = ExponentialSmoothing(series1, seasonal_periods=12, trend='mul', seasonal='add').fit()
fit1.fittedvalues.plot(color='red', label='HWM model 1: 1997-2020', legend=True)
series1.plot(color='black', label='Original K226 (1997-2020)', legend=True)
fit1.forecast(12).plot(color='red')
plt.show()

# Model 2: 2000 - 2020
fit2 = ExponentialSmoothing(series2, seasonal_periods=12, trend='mul', seasonal='mul').fit()
fit2.fittedvalues.plot(color='red', label='HWM ', legend=True)
series2.plot(color='blue', label='Truncated K226 (2012-2020)', legend=True)
fit2.forecast(12).plot(color='red', linewidth=2)
plt.title('HWM Forecast for Truncated K226 (2012-2020)', fontsize=15)
plt.show()

# Evaluating the errors
from sklearn.metrics import mean_squared_error
MSE1 = mean_squared_error(fit1.fittedvalues, series1)
MSE2 = mean_squared_error(fit2.fittedvalues, series2)


print('Summary of errors resulting from SES model 1&2: ')
import pandas as pd
cars = {'Model': ['MSE'],
        'SES model 1': [MSE1],
        'SES model 2': [MSE2]}
AllErrors = pd.DataFrame(cars, columns=(['Model', 'SES model 1', 'SES model 2']))
print(AllErrors)
print(MSE1)
print(MSE2)


 
error2 = series2- fit2.fittedvalues
error2.plot(title='Residual Plot for HWM of Truncated K226 (2012-2020)')
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(error2, title='Residual ACF for HWM of Truncated K226 (2012-2020)', lags=100)

    





