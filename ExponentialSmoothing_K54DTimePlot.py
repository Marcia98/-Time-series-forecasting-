#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 12:56:29 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt

series = read_excel('K54Ddata_32095422.xlsx', sheet_name='MAData', header=0, index_col=0, squeeze=True,
                    parse_dates=True)

series.plot(title='Data and trend for K54D')
plt.show()


