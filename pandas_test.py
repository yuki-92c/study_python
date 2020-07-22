import pandas as pd

staffs = [
    {'name': 'jack', 'age': 3, 'gender': 'male', 'country': 'UK'},
    {'name': 'will', 'age': 12, 'gender': 'male', 'country': 'golden FR'},
    {'name': 'anamaria', 'age': 8, 'gender': 'female', 'country': 'MX'},
    {'name': 'elizabeth', 'age': 8, 'gender': 'female', 'country': 'KH'},
    {'name': 'angelica', 'age': 36, 'gender': 'female', 'country': 'VN'},
    {'name': 'hector', 'age': 78, 'gender': 'male', 'country': 'golden AU'},
    {'name': 'henry', 'age': 28, 'gender': 'male', 'country': 'NZ'},
    {'name': 'tia', 'age': 18, 'gender': 'female', 'country': 'DO'},
]


df = pd.io.json.json_normalize(staffs)
print(df)
df.to_csv('staff.csv')