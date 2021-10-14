#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:54:19 2021

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
fit1 = ExponentialSmoothing(series1, seasonal_periods=12, trend='add', seasonal='add').fit()
fit1.fittedvalues.plot(color='red')
fit1.forecast(12).plot(color='red')

# Model 2: 2000 - 2020
fit2 = ExponentialSmoothing(series2, seasonal_periods=12, trend='add', seasonal='add').fit()
fit2.fittedvalues.plot(color='blue')
fit2.forecast(12).plot(color='blue')
series1.plot(color='black')
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