weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import pandas as pd

# Create a DataFrame df_weight_kg from weight_kg
df_weight_kg = pd.DataFrame(weight_kg)

# Create DataFrame df_weight_lbs from np_weight_kg
df_weight_lbs = df_weight_kg * 2.2

# Print out df_weight_lbs
print(df_weight_lbs)