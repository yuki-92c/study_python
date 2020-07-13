import pandas as pd

# 1. Create a dataframe from cars.csv
data = pd.read_csv("cars.csv")

# 2. Select the first column of the dataframe
print(data.iloc[:,0])

# 3. Select the row for Australia
print(data.loc[1])

# 4. Select the row for Japan
print(data.loc[2])

# 5. What is the difference in cars per capita between Australia and Japan?
difference =data.loc[[1,2],['cars_per_cap']]

AUS = data.loc[1,['cars_per_cap']]
JPN = data.loc[2,['cars_per_cap']]

print(AUS - JPN)

# print(difference)