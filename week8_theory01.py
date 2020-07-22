# importing pandas as pd
import pandas as pd
# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95], 'Second Score': [30, 45, 56, np.nan], 'Third Score':[np.nan, 40, 80, 98]}

# creating a dataframe from list
df = pd.DataFrame(dict)

# using isnull() function
df.isnull()
print(df)
print(df.isnull())


# filling missing value using fillna()
df.fillna(0)


print(df.fillna(0))
print(df.replace())
print(df.interpolate())
