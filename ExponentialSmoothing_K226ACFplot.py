#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:54:25 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

series = read_excel('K226data_32095422.xlsx', sheet_name='Data', header=0,
                    usecols=[1], squeeze=True, dtype=float)

# K226: ACF and PACF plot on 50 time series
plot_acf(series, title='ACF of K226 time series', lags=50)
plot_pacf(series, title='PACF of K226 timer series', lags=50)
plt.show()