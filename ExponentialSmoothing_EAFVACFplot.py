#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:43:10 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

series = read_excel('EAFVdata_32095422.xlsx', sheet_name='Data', header=0,
                    usecols=[1], squeeze=True, dtype=float)

# EAFV: ACF and PACF plot on 50 time series
plot_acf(series, title='ACF of EAFV time series', lags=50)
plot_pacf(series, title='PACF of EAFV time series', lags=50)
plt.show()