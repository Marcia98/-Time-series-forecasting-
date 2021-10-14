#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:44:16 2021

@author: 32095422
"""

from pandas import read_excel
from statsmodels.tsa.api import Holt
import matplotlib.pyplot as plt
series1 = read_excel('K226data_32095422.xlsx', sheet_name='Data', header=0,
                     index_col=0, parse_dates=True, squeeze=True)
series2 = read_excel('K226data_32095422.xlsx', sheet_name='Truncated_Data', header=0,
                     index_col=0, parse_dates=True, squeeze=True)



# Holt model 1: Original K226
fit1 = Holt(series1).fit(optimized=True)
fcast1 = fit1.forecast(12)
series1.plot(color='blue', legend=True, label='Original K226')
fit1.fittedvalues.plot(color='red', legend=True, label='LES')
fcast1.plot(color='red')
plt.show()

# Holt model 2: Ln(K226)
fit2 = Holt(series2).fit(optimized=True)
fcast2 = fit2.forecast(12)
series2.plot(color='blue', label='Truncated K226', legend=True)
fit2.fittedvalues.plot(color='red', label='LES (Truncated)', legend=True)
fcast2.plot(color='red')
plt.title('LES Forecast for Truncated K226 (2012-2020)')
plt.show()


#Evaluating the errors 
from sklearn.metrics import mean_squared_error 
MSE1=mean_squared_error(fit1.fittedvalues, series1)
MSE2=mean_squared_error(fit2.fittedvalues, series2)

print(MSE1)
print(MSE2)

error2 = fit2.fittedvalues - series2
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(error2, title='Residual Plot for LES of Truncated K226', lags=100)

























