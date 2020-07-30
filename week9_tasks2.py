# importing pandas module
import pandas as pd
# Define a dictionary containing employee data
data1 = {
    'Name':['Yuki', 'Nana', 'Mio', 'John'],
    'Age':[27, 24, 22, 32],
    'Address':['Niigata', 'Tokyo', 'Nagoya', 'Yokohama'],
    'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Define a dictionary containing employee data
data2 = {
    'Name':['Patrick', 'Nana', 'Yuki', 'Rachel'],
    'Age':[24, 22, 32, 27],
    'Address':['Sydney', 'Tokyo', 'Melbourne', 'Gold Coast'],
    'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data1,index=[0, 1, 2, 3])
# Convert the dictionary into DataFrame
df2 = pd.DataFrame(data2, index=[4, 5, 6, 7])

# 1. Use .concat to merge both DataFrames together.
print(pd.concat([df1,df2]))

# 2. Use .append to merge both DataFrames together.
print(df1.append(df2))

# 3. Create another DataFrame with one row specifying Name, Age, Address and Qualification and concat all 3 DataFrames.
data3 = {
    'Name':['kamegaya'],
    'Age':[77],
    'Address':['Canberra'],
    'Qualification':['abcde']}
df3 = pd.DataFrame(data3, index=[8])
print(pd.concat([df1,df2,df3]))

# 4. What happens when you use .concat and set the axis value to = 0?
print(pd.concat([df1,df2,df3],axis=0))


# 5. What happens when you use .concat and set the axis value to = 1?
print(pd.concat([df1,df2,df3],axis=1))
