#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:40:46 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt
series_JQ2J = read_excel('JQ2Jdata_32095422.xlsx', sheet_name='MAData', header=0,
                         index_col=0, parse_dates=True, squeeze=True)

series_JQ2J.plot(title='Data and trend for JQ2J')
plt.xlabel('Date')
plt.ylabel('JQ2J')
plt.show()