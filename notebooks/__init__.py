import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib as plt 




import os

print(os.getcwd())

df = pd.read_csv('benin-malanville.csv')

# Displaying the DataFrame
print(df)

print(df.head())

print(df.describe())

# Displaying data frame information
print(df.info())

# Displaying the null data
print(df.isnull().sum())


# print(sns.boxplot(x='DNI', y='GHI', data=df))
# print(plt.title('GHI VS DNI'))
# print(plt.show())

# print(df.columns)

# # Create the boxplot


# # Display the plot
# plt.show()
