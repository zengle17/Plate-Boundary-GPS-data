# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:31:21 2017

@author: Zach
"""

import pandas as pd
from matplotlib import pyplot as plt

# Import data
sheet_title = 'AB02.pbo.nam08' # the excel file has a tab "Renland d180
data = pd.read_csv('C:\\Users\\Zach\\My Documents\\College\\Superman Spring\\comp methods in geo\\Plate-Boundary-GPS-data\\AB02.pbo.nam08.csv', \
                      header=11, parse_dates=[0], infer_datetime_format=True)
                      # the last call turns the string of dates into a solid value
                      # pulls in a spreadsheet from the data folder in finder

# Give headers better names
data.columns = ['date [m/d/y]', 'X Mvmt [mm]', 'Y Mvmt [mm]','Z Mvmt [mm]','' ,'' ,'' ,'' ]


plt.figure(figsize=(12, 12)) 
plt.plot(data['date [m/d/y]'], data['X Mvmt [mm]'])
plt.title('PBO GPS X Movement at AB02, Nikolski, AK', fontsize=16, fontweight='bold')
plt.xlabel('date [m/d/y]', fontsize=16)
plt.ylabel('X Mvmt [mm]', fontsize=16)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 12)) 
plt.plot(data['date [m/d/y]'], data['Y Mvmt [mm]'])
plt.title('PBO GPS Y Movement at AB02, Nikolski, AK', fontsize=16, fontweight='bold')
plt.xlabel('date [m/d/y]', fontsize=16)
plt.ylabel('Y Mvmt [mm]', fontsize=16)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 12)) 
plt.plot(data['date [m/d/y]'], data['Z Mvmt [mm]'])
plt.title('PBO GPS Z Movement at AB02, Nikolski, AK', fontsize=16, fontweight='bold')
plt.xlabel('date [m/d/y]', fontsize=16)
plt.ylabel('Z Mvmt [mm]', fontsize=16)
plt.tight_layout()
plt.show()

#####
## ordinary linear regression on data
#####
