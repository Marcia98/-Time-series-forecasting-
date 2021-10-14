#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:00:35 2021

@author: 32095422
"""

from pandas import read_excel
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
plt.style.use('fivethirtyeight')

# Load the data
df = read_excel('K54Ddata_32095422.xlsx', sheet_name='Data', header=0,
           index_col=0, parse_dates=True, squeeze=True)

# Fitting the ARIMA model and printing the related statistics
# ARIMA(0,1,1)(0,1,1)12 in this case
mod = sm.tsa.statespace.SARIMAX(df,order=(1,2,2),seasonal_order=(1,2,2,12))
results = mod.fit(disp=False)
print(results.summary())

# Printing the graphical statistics of model (correlogram = ACF plot)
results.plot_diagnostics(figsize=(15,12), lags=100)
plt.show()

# =======================================
# this code requires the fitted forecasts (for accuracy evaluation) to start January 2009.
pred = results.get_prediction(start=pd.to_datetime('2009-01-01'), dynamic=False)
pred_ci = pred.conf_int()

# this code requires the whole plot to start in 2000 (start year of data)
ax = df['2000':].plot(label='Original data', linewidth=2)
pred.predicted_mean.plot(ax=ax, label='One-step ahead forecast', alpha=0.7, linewidth=2)

ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=0.2)
plt.legend()
plt.show()
# ======================================
# MSE evaluation
y_forecasted = pred.predicted_mean
y_truth = df['2009-01-01':]
# Compute the mean square error
mse = ((y_forecasted - y_truth) ** 2).mean()
print('MSE of the forecast is {}'.format(round(mse,2)))

# ======================================
# get forecast 12 steps ahead in future
pred_uc = results.get_forecast(steps=12)
# get confidence intervals of forecasts
pred_ci = pred_uc.conf_int()

# plotting forecasts ahead
ax = df.plot(label='Original data', color='blue', linewidth=2)
pred_uc.predicted_mean.plot(ax=ax, color='red', label='Forecast values', title='Forecast plot with confidence interval', linewidth=2)
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[: ,1], color='k', alpha=0.25)
plt.legend()
plt.show()
#-----------------------------------------------------------














