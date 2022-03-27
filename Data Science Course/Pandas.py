import pandas as pd
import numpy as np
from numpy.random import randn

var = np.int
data = [10, 20, 30]
labels = ['a', 'b', 'c', ]
Series = pd.Series(data=data, index=labels)  # Creates a series (a list with custom index)
# input types can be a dictionary, an array,lists etc
print(Series)
print('\n')

print(Series['a'])  # How to find a value in a series

# NOTE we can add series if there are keys that are visible in both series
# the value will add up and those that don't will show result as null

#
#
# DATA FRAMES
#
#
df = pd.DataFrame(randn(5, 4), ['a', 'b', 'c', 'd', 'e'], ['w', 'x', 'y', 'z'])
print(df)
# A DATAFRAME IS A 2d SERIES WITH THE SAME INDEX
print('\n')
print(df[['w', 'z']])  # To find 2 columns in a dataframe
print('\n')
print(df.loc['a'])  # To find a row in a dataframe using the name
print('\n')
print(df.iloc[2])  # To find a row in a dataframe using the index
print('\n')
df['new'] = df['w'] + df['z']  # To create a new series in the same dataframe called new

print(df)
print('\n')
df1 = df.drop('new', axis=1)  # To delete a column in the same data frame
print(df1)
print('\n')
df2 = df.drop('e', axis=0)  # To delete a row in the same data frame
print(df2)
print('\n')
print(df.shape)  # it will show no of rows and columns
print('\n')
print(df.loc['b', 'y'])  # it tells you the value of the location mentioned
print('\n')
print(df > 1) #returns bool values
print('\n')
print(df[df['w'] > 0])  # returns only the rows that are true (in column w)
print('\n')
# we cans stack up methods on dataframes
print(df[(df['w'] > 0) & (df['y'] > 1)])  # Use the & to compare bool of series
# in pandas to compare bool of dataframes/series use(and = &) (or = |)
print('\n')
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
d1 = pd.DataFrame(d)
print(d1)
d1.fillna(value='This',inplace=True)  # allows you to fill empty objects in a dataframe
print(d1)
