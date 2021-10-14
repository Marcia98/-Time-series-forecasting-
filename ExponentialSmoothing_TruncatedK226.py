#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:32:36 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf

series = read_excel('K226data_32095422.xlsx', sheet_name='Truncated_Data', header=0, index_col=0,
                    squeeze=True, parse_dates=True)
series.plot()
plt.title('Time plot of truncated K226 (2012-2020)')
plt.show()

result = seasonal_decompose(series, model='add')
result.plot()
plt.show()

plot_acf(series, title='ACF plot of truncated K226 (2012-2020)', lags=50)