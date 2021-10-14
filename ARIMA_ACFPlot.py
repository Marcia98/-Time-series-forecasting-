#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:10:47 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

series_K54D = read_excel('K54Ddata_32095422.xlsx', sheet_name='Data', header=0,
                    usecols=[1], squeeze=True, dtype=float)


# K54D: ACF and PACF plot on 50 time series
plot_acf(series_K54D, title='ACF of K54D time series', lags=50)
plot_pacf(series_K54D, title='PACF of K54D time series', lags=50)
plt.show()



