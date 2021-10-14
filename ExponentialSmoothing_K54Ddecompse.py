#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:39:12 2021

@author: 32095422
"""

from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

series = read_excel('K54Ddata_32095422.xlsx', sheet_name='Data', header=0,
                    index_col=0, parse_dates=True, squeeze=True)

result = seasonal_decompose(series, model='mul')
result.plot()
plt.show()