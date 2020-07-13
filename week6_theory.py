height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi)


var = bmi[bmi > 26]
print(var)

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
"capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
"area": [8.516, 17.10, 3.286, 9.597, 1.221],
"population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

cars = pd.read_csv('cars.csv')
print(cars)

import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars['cars_per_cap'])
print(cars[['cars_per_cap']])
print(cars[['cars_per_cap', 'drives_right']])
print(cars[3:4])

cars = pd.read_csv('cars.csv', index_col = 0)
print(cars.iloc[2])
print(cars.loc[['AUS', 'EG']])