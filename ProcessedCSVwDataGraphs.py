# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:31:21 2017

@author: Zach
"""

import pandas as pd
from matplotlib import pyplot as plt

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

# Give headers better names
data.columns = ['date [m/d/y]', 'X Mvmt [mm]', 'Y Mvmt [mm]','Z Mvmt [mm]','' ,'' ,'' ,'' ]

fig = plt.figure(figsize=(6, 12))

ax1 = plt.subplot(3, 1, 1)
plt.plot(data['date [m/d/y]'], data['X Mvmt [mm]'])
plt.title('PBO GPS X Movement at AB02, Nikolski, AK', fontsize=16, fontweight='bold')
plt.xlabel('date [m/d/y]', fontsize=16)
plt.ylabel('X Mvmt [mm]', fontsize=16)
plt.tight_layout()
plt.show()

ax2 = plt.subplot(3, 1, 2)
plt.plot(data['date [m/d/y]'], data['Y Mvmt [mm]'])
plt.title('PBO GPS Y Movement at AB02, Nikolski, AK', fontsize=16, fontweight='bold')
plt.xlabel('date [m/d/y]', fontsize=16)
plt.ylabel('Y Mvmt [mm]', fontsize=16)
plt.tight_layout()
plt.show()

ax3 = plt.subplot(3, 1, 3)
plt.plot(data['date [m/d/y]'], data['Z Mvmt [mm]'])
plt.title('PBO GPS Z Movement at AB02, Nikolski, AK', fontsize=16, fontweight='bold')
plt.xlabel('date [m/d/y]', fontsize=16)
plt.ylabel('Z Mvmt [mm]', fontsize=16)
plt.tight_layout()
plt.show()

#####
## ordinary linear regression on data
#####
github justmarkham 08_linear_regression
scipy reference linregress
scipy numpy linalg.lstsq

# find the residuals (distance from data point to regression line)

# create histogram of data. find mean, sigma, quartiles, std error of mean
# does the regression line seem like a good fit? (symmetrical error on both sides of line)
