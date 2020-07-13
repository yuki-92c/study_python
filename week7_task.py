#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

arr = np.array([range(32)])
print(arr)
arr = arr.reshape(8,4)
print(arr)
df = pd.DataFrame(arr, index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
print(df)
# 1. Select all rows for column A using .loc[]
print(df.loc[:,'A'])

# 2. Select all rows for columns A and C using .loc[]
print(df.loc[:,['A','C']])

# 3. Select rows a, b, f and h for columns A and C using .loc[]
print(df.loc[['a', 'b', 'f', 'h'],['A','C']])


# 4. Select range of rows for all columns, that is, a through to h rows.
print(df.loc[:])