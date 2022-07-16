#loading packages
import numpy as np
import pandas as pd
import csv

#upload the csv file
df = pd.read_csv('GOOG.csv', parse_dates=True)

#define the valid function for the window size
def is_valid(text):
    numbers = '0123456789.'
    for value in text:
        if numbers.find(value) == -1:
            return False
        return True
    if text > 252:
        return False
    return True

#input the window size
window= input('Please enter a rolling window size: ')

#verify the window size
while is_valid(window) == False:
    print('Please enter a valid window size: ')
    window = input('Please enter a rolling window size: ')
window = int(window)
#calculate the related statistics 
max_df =df.rolling(window).max().dropna().round(decimals=2)
min_df =df.rolling(window).min().dropna().round(decimals=2)
mean_df =df.rolling(window).mean().dropna().round(decimals=2)
median_df =df.rolling(window).median().dropna().round(decimals=2)
std_df =df.rolling(window).std().dropna().round(decimals=2)

#add Date to max dataframe
max_df['Date'] = df['Date'][window-1:]
max_df.insert(0,'Date',max_df.pop('Date'))

#add Date to min dataframe
min_df['Date'] = df['Date'][window-1:]
min_df.insert(0,'Date',min_df.pop('Date'))

#add Date to mean dataframe
mean_df['Date'] = df['Date'][window-1:]
mean_df.insert(0,'Date',mean_df.pop('Date'))

#add Date to median dataframe
median_df['Date'] = df['Date'][window-1:]
median_df.insert(0,'Date',median_df.pop('Date'))

#add Date to standard deviation dataframe
std_df['Date'] = df['Date'][window-1:]
std_df.insert(0,'Date',std_df.pop('Date'))

#print the dataframe and hide the index column
print('The Max of the stocks in a rolling window: ')
print(max_df.to_string(index=False))

print('The Min of the stocks in a rolling window: ')
print(min_df.to_string(index=False))

print('The Mean of the stocks in a rolling window: ')
print(mean_df.to_string(index=False))

print('The Median of the stocks in a rolling window: ')
print(median_df.to_string(index=False))

print('The Standard deviation of the stocks in a rolling window: ')
print(std_df.to_string(index=False))