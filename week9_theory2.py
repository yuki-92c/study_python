import pandas as pd

one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
    'Marks_scored':[98,90,87,69,78]},
    index=[1,2,3,4,5])

two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'Marks_scored':[89,80,79,97,88]},
    index=[1,2,3,4,5])


# print(pd.concat([one,two]))
#
# print(pd.concat([one,two],axis=0))
# print(pd.concat([one,two],axis=1))
#
# print(one.append(two))
# print(one.append([two,one,two]))
# print(one.append([two,two,one]))
print(pd.concat([one, two], join='inner'))
print(pd.concat([one, two],axis=1, join='outer'))

print(type(pd.concat([one, two],axis=1, join='outer')))
