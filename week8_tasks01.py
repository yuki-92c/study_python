#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
arr = np.array([range(32)])
arr = arr.reshape(8,4)
df = pd.DataFrame(arr,index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
df.loc['b','e','g'] = np.nan



# 1. Print the dataframe. What values are missing
print(df)

# 2. Use .isnull() to find the missing values in the dataframe.
print(df.isnull())

# 3. Use .notnull() to find the values in the dataframe.
# 4. Use .sum() on column A. What value do you get?
# 5. Use .fillna() to replace the NaNs with 1. Print your result.
# 6. Use .dropna() to drop the NaN values in the dataframe. Print your result.
# 7. Replace the value ‘31’ in the dataframe with a 0. (hint: you can google a function for this)
