# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
arr = np.array([range(32)])
arr = arr.reshape(8,4)
df = pd.DataFrame(arr, columns = ['A', 'B', 'C', 'D'])

# 1. Select all rows in the 4th column using .iloc[]
print(df.iloc[4])

# 2. Select rows 2 to 6 in the 3rd and 4th columns using iloc[] (remember 0 based indexing!)
print(df.iloc[2:6,[2,3]])
print(df.iloc[[2,3,4,5,6],[2,3]])


# 3. Select rows 1, 3 and 5 from the 2nd and 3rd columns.
print(df.iloc[[1,3,5],[1,2]])

# 4. Select rows 2 to 4 from all columns using .iloc
print(df.iloc[2:4,:])

# 5. Select all rows from columns 2 to 4 using .ilo[]
print(df.iloc[:,1:3])