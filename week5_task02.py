import re
result_find = []
for x in dir(re):
    if "find" in x:
        result_find.append(x)
#print(dir(re))
print(result_find)