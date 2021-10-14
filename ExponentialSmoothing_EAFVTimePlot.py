#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:36:40 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt

series_EAFV = read_excel('EAFVdata_32095422.xlsx', sheet_name='MAData', header=0,
                         index_col=0, parse_dates=True, squeeze=True)

series_EAFV.plot(title='Data and trend for EAFV')
plt.xlabel('Date')
plt.ylabel('EAFV')
plt.show()