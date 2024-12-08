import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib as plt 




import os

print(os.getcwd())

dfb = pd.read_csv('benin-malanville.csv')
dfs = pd.read_csv('sierraleone-bumbuna.csv')
dft = pd.read_csv('togo-dapaong_qc.csv')

# Displaying the DataFrame for benin
print(dfb)

print(dfb.head())

print(dfb.describe())

# Displaying data frame information for benin
print(dfb.info())

# Displaying the null data for benin
print(dfb.isnull().sum())

#data for sierralion

# Displaying the DataFrame for sierralion
print(dfs)

print(dfs.head())

print(dfs.describe())

# Displaying data frame information for sierralion
print(dfs.info())

# Displaying the null data for sierralion
print(dfs.isnull().sum())


#data for togo


# Displaying the DataFrame for togo
print(dft)

print(dft.head())

print(dft.describe())

# Displaying data frame information for togo
print(dft.info())

# Displaying the null data for togo
print(dft.isnull().sum())



