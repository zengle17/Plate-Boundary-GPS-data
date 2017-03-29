# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:31:21 2017

@author: Zach
"""

import numpy as np
import pandas as pd
from datetime import date
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt
from scipy import stats

# station AB02
# Aleutian Island (Nikolski), Alaska. Typically foggy.
# Seismometer set up at a small hut w a gps looking device outside

# Import data
sheet_title = 'AB02.pbo.nam08' # the excel file has a tab "Renland d180
data = pd.read_csv('..\\..\\..\\..\\College\\Superman Spring\\comp methods in geo\\Plate-Boundary-GPS-data\\AB02.pbo.nam08.csv', \
                      header=11, parse_dates=[0], infer_datetime_format=True)
                      # the last call turns the string of dates into a solid value
                      # pulls in a spreadsheet from the data folder in finder
                      # header11 means column variables listed in row 12
                      
                      # the dots at the beginning of the call are for
                      # the hard drive (C:), then the 3 folders you must open
                      # to get to comp methods in geo

# Give headers better names and set up variables
data.columns = ['date [m/d/y]', 'X Mvmt [mm]', 'Y Mvmt [mm]','Z Mvmt [mm]','' ,'' ,'' ,'' ]
t = data['date [m/d/y]']
x = data['X Mvmt [mm]']
y = data['Y Mvmt [mm]']
z = data['Z Mvmt [mm]']

d0 = date(2007, 5, 23)
d1 = date(2017, 3, 20)
delta = d0 - d1
print delta.days
    # there are skipped days between the last and first day in the data
    # 3322 days recorded movement but several months in 2008 and 2009 experienced no data
    # between the two dates is 3589 days
t1 = np.arange(3322)
    # need an array vector of number of days not dates for lin reg


# This also create a new column of days since the start for regression
#pbo_data['date_delta'] = (pbo_data['Date'] - pbo_data['Date'].min()) / np.timedelta64(1,'D')
                         # this subtracts date by min date and divides by 1 day
#d = pbo_data['date_delta']
#d = sm.add_constant(X)

# find least squares regression line
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(t1, x)
print("r-squared:", r_value1**2)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(t1, y)
print("r-squared:", r_value2**2)
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(t1, z)
print("r-squared:", r_value3**2)

# plot data and regression line
fig = plt.figure(figsize=(16, 12))

ax1 = plt.subplot(3, 1, 1)
plt.plot(t1, x, label = 'collected data')
plt.plot(t1, intercept1 + slope1*t1, 'r', label='fitted line')
plt.legend()
plt.title('PBO GPS X Movement at AB02, Nikolski, AK Since 5/23/2007', fontsize=16, fontweight='bold')
plt.xlabel('day', fontsize=16)
plt.ylabel('X Mvmt [mm]', fontsize=16)
plt.grid()
plt.tight_layout()
plt.show()

ax2 = plt.subplot(3, 1, 2)
plt.plot(t1, y, label = 'collected data')
plt.plot(t1, intercept2 + slope2*t1, 'r', label='fitted line')
plt.legend()
plt.title('PBO GPS Y Movement at AB02, Nikolski, AK Since 5/23/2007', fontsize=16, fontweight='bold')
plt.xlabel('day', fontsize=16)
plt.ylabel('Y Mvmt [mm]', fontsize=16)
plt.grid()
plt.tight_layout()
plt.show()

ax3 = plt.subplot(3, 1, 3)
plt.plot(t1, z, label = 'collected data')
plt.plot(t1, intercept3 + slope3*t1, 'r', label='fitted line')
plt.legend()
plt.title('PBO GPS Z Movement at AB02, Nikolski, AK Since 5/23/2007', fontsize=16, fontweight='bold')
plt.xlabel('day', fontsize=16)
plt.ylabel('Z Mvmt [mm]', fontsize=16)
plt.grid()
plt.tight_layout()
plt.show()


# find the residuals (distance from data point to least squares regression line)
# this gives a summary of regression statsistics
lm1 = smf.ols(formula='x ~ t1', data=data).fit()
print lm1.summary()
lm2 = smf.ols(formula='y ~ t1', data=data).fit()
print lm2.summary()
lm3 = smf.ols(formula='z ~ t1', data=data).fit()
print lm3.summary()

# plot residuals
fig1 = plt.figure(figsize=(16, 12))

bx1 = plt.subplot(3, 1, 1)
difference1 = (intercept1 + slope1*t1) - x
plt.plot(t1,difference1,'or')
plt.plot(t1, 0*difference1)
plt.title('Residuals X Movement', fontsize=16, fontweight='bold')
plt.grid()

bx2 = plt.subplot(3, 1, 2)
difference2 = (intercept2 + slope2*t1) - y
plt.plot(t1,difference2,'or')
plt.plot(t1, 0*difference1)
plt.title('Residuals Y Movement', fontsize=16, fontweight='bold')
plt.grid()

bx3 = plt.subplot(3, 1, 3)
difference3 = (intercept3 + slope3*t1) - z
plt.plot(t1,difference3,'or')
plt.plot(t1, 0*difference1)
plt.title('Residuals Z Movement', fontsize=16, fontweight='bold')
plt.grid()
# create histogram of data. find mean, sigma, quartiles, std error of mean
# does the regression line seem like a good fit? (symmetrical error on both sides of line)
