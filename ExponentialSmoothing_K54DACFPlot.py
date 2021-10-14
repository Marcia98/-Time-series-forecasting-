#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:14:54 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

series = read_excel('K54Ddata_32095422.xlsx', sheet_name='Data', header=0,
                    squeeze=True, parse_dates=True, index_col=0)
plot_acf(series, lags=50)
plt.show()
plot_pacf(series, lags=50)
plt.show()