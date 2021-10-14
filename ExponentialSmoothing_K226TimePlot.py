#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:39:18 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt

series_K226 = read_excel('K226data_32095422.xlsx', sheet_name='MAData', header=0,
                         index_col=0, parse_dates=True, squeeze=True)

series_K226.plot(title='Data and trend for K226')
plt.xlabel('Date')
plt.ylabel('K226')
plt.show()