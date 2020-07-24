# importing pandas module
import pandas as pd
import numpy as np
# Define a dictionary containing employee data
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32, 33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj','Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd', 'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)
print(df)

# 1. Use .groupby to group the data by ‘Name’. Then print the .groups of the dataframe.
name = df.groupby('Name')
print(name)
print(name.groups)

# 2. Group by [‘Name’, ‘Qualification’] and print out the groups.
name_qualification = df.groupby(['Name', 'Qualification'])
print(name_qualification)

# 3. Select the group of data that has the name ‘Jai’.
print(name.get_group('Jai'))

# 4. Select the group of data that has the name ‘Jai’ and qualification ‘Msc’.
print(name_qualification.get_group(('Jai', 'Msc')))

# 5. Use the .agg function on the data grouped by ‘Name’, and use np.sum to sum the ages.
print(name['Age'].agg(np.sum))
print(name.groups)