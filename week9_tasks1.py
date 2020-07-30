import pandas as pd

left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5']})

right = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5']})

# 1. Do a pd.merge using the ‘Name’ key. What results do you get? Why?
# print(pd.merge(left,right,on='Name'))
# Empty DataFrame
# => key isn't appropriate ??

# 2. Use pd.merge using the ‘id’ and ‘subject_id’ keys.
# print(pd.merge(left,right,on='id'))
# print(pd.merge(left,right,on=['id','subject_id']))


# 3. Use pd.merge on the subject_id key, using a left join. (hint: need to specify the ​how argument).
# print(pd.merge(left, right, how = 'left', on = 'subject_id'))

# 4. Use pd.merge on the subject_id key, using a right join.
# print(pd.merge(left, right, how = 'right', on = 'subject_id'))


# 5. Use pd.merge on the subject_id key, using an outer join.
# print(pd.merge(left, right, how = 'outer', on = 'subject_id'))

# 6. Use pd.merge on the subject_id key, using an inner join.
# print(pd.merge(left, right, how = 'inner', on = 'subject_id'))


#7. Create a DataFrame of one row with id = 6, name = ‘Billy’ and subject_id = ‘sub2’ and use the .append function to add it to the left DataFrame.
print(left.append({'id':6, 'Name':'Billy', 'subject_id':'sub2'},ignore_index=True))

# 8. Do pd.merge again using the ‘Name’ key. What results do you get and why?
print(pd.merge(left, right, how='inner', on='Name'))

print(pd.merge(left, right, on='subject_id'))
print(pd.merge(left, right, how = 'outer', on = 'subject_id'))
